#!/usr/bin/env python3
"""Preview an exported duplicate review. Use --publish-catalog to apply only catalog repairs.

Example (from the vault, with Python 3.10+):
  python _scripts/plan_art_cleanup.py --decisions EXPORT.json --manifest duplicates.json \
      --policy cleanup-policy.json --output REVIEW_DIRECTORY

The manifest supplies the exact two file identities and SHA-256 values for each review ID.
The catalog config supplies named collection roots (including Vault and RPGs). The optional
policy has holdDirectories and preferredKeepers, using Collection/path names. Results are
cleanup-plan.json and session-image-provenance.preview.json. The latter is the complete
merged ledger for RPGs/_by_session/session-image-provenance.json after approved retirement.
Neither command changes vault notes, the live session ledger, or the artwork.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from contextlib import contextmanager
import fcntl
import hashlib
from html import escape, unescape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata
import sys
import tempfile
from urllib.parse import quote, unquote

CATALOG_TOOLS = Path(__file__).resolve().parents[1] / '.agents/skills/classify-taelgar-art-style/scripts'
sys.path.insert(0, str(CATALOG_TOOLS))
import catalog
import gallery

LEDGER = 'session-image-provenance.json'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def optional(path, default):
    return read(path) if path.is_file() else default


def name(path, roots):
    for key, root in roots.items():
        if path.is_relative_to(root):
            return key + '/' + path.relative_to(root).as_posix()
    raise ValueError(f'Path outside collections: {path}')


def absolute(key, roots):
    collection, rel = key.split('/', 1)
    p = roots[collection] / rel
    if p.resolve() != p or not p.is_relative_to(roots[collection]) or p == roots[collection]:
        raise ValueError(f'Unsafe collection path: {key}')
    return p


def choices(export, manifest, roots, policy):
    if set(policy) - {'holdDirectories', 'preferredKeepers'}:
        raise ValueError('Unknown cleanup policy setting')
    holds = [absolute(key, roots) for key in policy.get('holdDirectories', [])]
    overrides = {absolute(k, roots): absolute(v, roots) for k, v in policy.get('preferredKeepers', {}).items()}
    pairs, files = {}, {}
    for queue, section in [('exact', 'copies'), ('visual', 'visualComparisons')]:
        for row in manifest.get(section, []):
            pair = []
            for item in (row['keeper'], row['copy']):
                path = absolute(item['collection'] + '/' + item['relative'], roots)
                if str(path) != item['path']:
                    raise ValueError(f'Manifest collection mismatch: {path}')
                if path in files and files[path]['sha256'] != item['sha256']:
                    raise ValueError(f'Conflicting manifest hashes: {path}')
                files[path] = item
                pair.append(path)
            key = (queue, row['id'])
            if key in pairs or pair[0] == pair[1]:
                raise ValueError(f'Invalid pair {key}')
            pairs[key] = pair

    candidates, keep, ids, nondeletions = defaultdict(set), set(), defaultdict(list), []
    seen = set()
    for row in export['decisions']:
        key = (row['queue'], row['id'])
        if key[0] not in ('exact', 'visual'):
            if row.get('acceptedDeletion'):
                raise ValueError(f'Unrecognized deletion queue: {key}')
            continue
        pair = pairs[key]
        if key in seen or list(map(str, pair)) != [row['source'], row['comparedPath']]:
            raise ValueError(f'Stale or repeated decision {key}')
        seen.add(key)
        choice = row['choice']
        if choice == 'Deletion accepted':
            old, new = Path(row['acceptedDeletion']), Path(row['keepPath'])
            if {old, new} != set(pair) or row.get('keepPaths', [str(new)]) != [str(new)]:
                raise ValueError(f'Invalid accepted deletion {key}')
            candidates[old].add(new)
            ids[old].append(row['id'])
            keep.add(new)
        elif choice in ('Keep as is', 'Revisit', 'Shortlist', 'Undecided'):
            if row.get('acceptedDeletion'):
                raise ValueError(f'Unexpected deletion for {key}')
            if choice == 'Keep as is':
                keep.update(pair)
            nondeletions.append(dict(id=row['id'], choice=choice, paths=[name(p, roots) for p in pair]))
        else:
            raise ValueError(f'Unrecognized decision {choice}')
    conflicts = set(candidates) & keep
    if conflicts:
        raise ValueError('Conflicting keep/delete choices: ' + ', '.join(map(str, sorted(conflicts))))
    mapping, held = {}, []
    for old, survivors in sorted(candidates.items()):
        if any(old.is_relative_to(h) for h in holds):
            held.append(dict(file=name(old, roots), decisions=ids[old]))
            continue
        target = overrides.get(old)
        if target is None and len(survivors) == 1:
            target = next(iter(survivors))
        if target not in survivors:
            raise ValueError(f'Select one of the retained targets for {old}: {sorted(survivors)}')
        mapping[old] = target
    if overrides.keys() - candidates.keys():
        raise ValueError('Keeper override does not match this export')
    for p in sorted(set(mapping) | set(mapping.values())):
        if not p.is_file() or digest(p) != files[p]['sha256']:
            raise ValueError(f'Missing or changed file: {p}')
    return mapping, files, ids, held, nondeletions


def session_ledger(mapping, roots, existing):
    """Keep one entry per original path and resolve past keepers through the new batch."""
    base = roots['RPGs'] / '_by_session'
    indexed = {}
    for entry in existing:
        actions = entry.keys() & {'deleted', 'moved'}
        if len(actions) != 1:
            raise ValueError(f'Expected one original filename in provenance row: {entry}')
        directory, filename = entry['original-directory'], entry[actions.pop()]
        if Path(filename).name != filename or Path(directory).is_absolute() or '..' in Path(directory).parts:
            raise ValueError(f'Invalid provenance row: {entry}')
        key = (directory, filename)
        old_keeper = absolute(entry['file'], roots)
        updated = {**entry, 'file': name(mapping.get(old_keeper, old_keeper), roots)}
        if key in indexed and indexed[key] != updated:
            raise ValueError(f'Conflicting session history for {key}')
        indexed[key] = updated
    for old, new in mapping.items():
        if not old.is_relative_to(base):
            continue
        directory = str(old.parent.relative_to(base))
        key = (directory, old.name)
        row = {'file': name(new, roots), 'deleted': old.name, 'original-directory': directory}
        if key in indexed and indexed[key] != row:
            raise ValueError(f'Conflicting session history for {old}')
        indexed[key] = row
    return [indexed[key] for key in sorted(indexed)]


def link_changes(mapping, files, roots):
    """Plan edits from manifest backlinks after resolving their current targets and line positions."""
    vault = roots['Vault']
    by_name = defaultdict(list)
    relevant = {p.name.casefold() for p in set(mapping) | set(mapping.values())}
    for directory, dirs, names in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in {'.git', '.trash', 'node_modules', '.backups'}]
        for n in names:
            if n.casefold() in relevant:
                by_name[n.casefold()].append(Path(directory) / n)
    evidence = {(old, ref['note'], ref['line']) for old in mapping for ref in files[old]['links']}
    ambiguous = [(old, r) for old in mapping for r in files[old]['ambiguousLinks']]
    if ambiguous:
        raise ValueError(f'Ambiguous manifest backlinks require review: {ambiguous}')
    # Scan current notes too: cached line numbers are hints and can change.
    names = {p.name for p in mapping}
    needles = {v for n in names for u in ('NFC', 'NFD')
               for v in (unicodedata.normalize(u, n), quote(unicodedata.normalize(u, n)))}
    cmd = ['rg', '--hidden', '--no-ignore', '-i', '-l', '-0', '-F', '-f', '-', '-g', '*.md',
           '-g', '*.canvas', '-g', '!**/.git/**', '-g', '!**/.trash/**', '-g', '!**/node_modules/**', '.']
    scan = subprocess.run(cmd, cwd=vault, input='\n'.join(sorted(needles)).encode(), capture_output=True) if needles else None
    if scan and scan.returncode not in (0, 1):
        raise ValueError(scan.stderr.decode())
    docs = {os.fsdecode(p).removeprefix('./') for p in (scan.stdout.split(b'\0') if scan else []) if p}
    docs.update(n for _, n, _ in evidence)
    token = re.compile(r'''\[\[(?P<wiki>[^\]|#\n]+)|!?\[[^\]\n]*\]\(\s*<?(?P<md>(?:[^()\n>]|\([^()\n]*\))+?)>?(?:\s+["'][^"']*["'])?\)|(?:src|href|poster)\s*=\s*["'](?P<html>[^"']+)["']|^\s*\[[^\]]+\]:\s*<?(?P<definition>[^<>\s]+)>?|"file"\s*:\s*(?P<canvas>"(?:[^"\\]|\\.)*")|^\s*image:\s*["']?(?P<field>[^"'\[\]\n]+?)["']?\s*$''', re.I)
    edits, found = [], set()
    for doc in sorted(docs):
        p = absolute('Vault/' + doc, roots)
        if not p.is_file():
            raise ValueError(f'Missing referenced note: {doc}')
        for line_no, line in enumerate(p.read_text().splitlines(), 1):
            for m in token.finditer(line):
                style = m.lastgroup
                value = m[style]
                target = json.loads(value) if style == 'canvas' else value
                raw, sep, anchor = target.partition('#')
                raw = unquote(unescape(raw)).strip()
                if raw.startswith('file://'):
                    raw = raw[7:]
                elif '://' in raw:
                    continue
                if style == 'wiki' and raw.endswith('\\'):
                    raw = raw[:-1]
                if Path(raw).name.casefold() not in relevant:
                    continue
                options = [p.parent / raw, vault / raw] if raw.startswith('.') or style in ('md','html','definition') else [vault / raw, p.parent / raw]
                dest = next((v.resolve() for v in options if v.is_file()), None)
                matches = by_name.get(Path(raw).name.casefold(), [])
                if dest is None and not raw.startswith(('./','../','/')):
                    fits = [v for v in matches if '/' not in raw or v.as_posix().endswith('/'+raw)]
                    if len(fits) == 1:
                        dest = fits[0]
                    elif len(fits) > 1 and any(v in mapping for v in fits):
                        raise ValueError(f'Ambiguous link {doc}:{line_no}: {raw}')
                if dest not in mapping:
                    continue
                new = mapping[dest]
                if new.is_relative_to(vault):
                    if style in ('md','html','definition'):
                        replacement = quote(os.path.relpath(new, p.parent), safe='/.-_')
                    elif '/' not in raw and len(by_name[new.name.casefold()]) == 1 and style != 'canvas':
                        replacement = new.name
                    else:
                        replacement = new.relative_to(vault).as_posix()
                elif style in ('md','html','definition'):
                    replacement = new.as_uri()
                else:
                    raise ValueError(f'External keeper needs a vault-compatible link: {doc}:{line_no}')
                if style == 'wiki' and value.endswith('\\'):
                    replacement += '\\'
                replacement += sep + anchor
                if style == 'canvas':
                    replacement = json.dumps(replacement, ensure_ascii=False)
                edits.append(dict(note=doc, line=line_no, column=m.start(style)+1, old=value, new=replacement,
                                  file=name(new,roots), retired=name(dest,roots)))
                found.add((dest,doc))
    for old, doc, _ in evidence:
        if (old,doc) not in found:
            raise ValueError(f'Manifest backlink needs fresh review: {doc} -> {old}')
    return edits


def replace_review_links(text, page, mapping):
    count = 0

    def replace(match):
        nonlocal count
        raw = unescape(match[3])
        if raw.startswith('file://'):
            source = Path(unquote(raw[7:]))
        elif raw and not raw.startswith('#') and ':' not in raw:
            source = Path(os.path.normpath(page.parent / unquote(raw)))
        else:
            return match[0]
        if source not in mapping:
            return match[0]
        count += 1
        return match[1] + match[2] + escape(mapping[source].as_uri(), quote=True) + match[2]

    new = re.sub(r'''(\b(?:href|src)\s*=\s*)(["'])([^"'<>]+)\2''', replace, text, flags=re.I)
    return new, count


def catalog_repairs(root, config, mapping, files, stage):
    """Build the exact publication in a temporary catalog; retain all historical review data."""
    for filename in ('config.json', 'styles.json', 'corrections.json', 'inventory.json'):
        shutil.copyfile(root/filename, stage/filename)
    shutil.copytree(root/'batches', stage/'batches')
    (stage/'reviews').mkdir()
    for path in (root/'reviews').glob('*.json'):
        shutil.copyfile(path, stage/'reviews'/path.name)

    redirects = optional(root/'source-replacements.json', {})
    prior_rows = catalog.records(root)
    repaired = []
    for row in prior_rows:
        uid = str(row['id'])
        current = catalog.source(config, row)
        if current not in mapping:
            continue
        dest = files[mapping[current]]
        redirects[uid] = dict(reviewedSha256=row['sha256'], collection=dest['collection'],
                              relativePath=dest['relative'], sourceSha256=dest['sha256'])
        repaired.append(dict(id=row['id'], old=str(current), new=dest['path']))
    catalog.save(stage/'source-replacements.json', redirects)
    rows = catalog.records(stage)
    styles = catalog.checked(stage, config, rows)
    for row in rows:
        original = catalog.source(config, row)
        if original in mapping:
            raise ValueError(f"Catalog #{row['id']} still points to {original}")
        if str(row['id']) in redirects and digest(original) != row['sourceSha256']:
            raise ValueError(f"Changed catalog keeper for #{row['id']}")
        if not (root/'thumbnails'/(row['sha256']+'.jpg')).is_file():
            raise ValueError(f"Missing thumbnail for #{row['id']}")

    roots = {key:Path(value) for key,value in config['roots'].items()}
    inventory = read(root/'inventory.json')
    for item in inventory:
        path = catalog.source(config, item)
        prior = item.get('cleanupReplacement')
        target = mapping.get(path)
        if target is None and prior:
            target = mapping.get(absolute(prior, roots))
        if target:
            item['cleanupReplacement'] = name(target, roots)
    primary = defaultdict(list)
    for row in rows:
        primary[catalog.source(config, row)].append(row)
    for item in inventory:
        records = primary.get(catalog.source(config,item))
        if records and any(str(r['id']) in redirects for r in records):
            chosen = min(records, key=lambda r: (r['sha256'] != item.get('sha256'), r['id']))
            item['reviewId'] = chosen['id']
            item['disposition'] = 'set aside' if catalog.set_aside(chosen) else 'style reviewed'
            item.pop('reason', None)
    catalog.save(stage/'inventory.json', inventory)
    catalog.write(stage/'index.html', gallery.render(config, rows, styles, len(inventory), stage))

    published = [Path(n) for n in ('source-replacements.json','inventory.json','index.html','set-aside.html')]
    review_links = []
    for page in sorted((root/'reviews').rglob('*.html')):
        rel = page.relative_to(root)
        rebuilt = stage/rel
        after, count = replace_review_links(page.read_text(), page, mapping)
        if count:
            catalog.write(rebuilt, after)
            review_links.append(dict(page=str(rel), links=count))
            published.append(rel)
    for filename in ('index.html','set-aside.html'):
        _, remaining = replace_review_links((stage/filename).read_text(), root/filename, mapping)
        if remaining:
            raise ValueError(f'Retiring link in rebuilt {filename}')
    return published, repaired, review_links


@contextmanager
def publishing_lock(root, publish):
    # Lock the directory inode without introducing a persistent file.
    fd = os.open(root, os.O_RDONLY)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX if publish else fcntl.LOCK_SH)
        yield
    finally:
        os.close(fd)


def publish_catalog(root, stage, files, baseline):
    changes = [f for f in files if (stage/f).read_bytes() != ((root/f).read_bytes() if (root/f).exists() else None)]
    backups = stage/'backups'
    for f in changes:
        target = root/f
        if (digest(target) if target.exists() else None) != baseline.get(f):
            raise ValueError(f'Catalog was edited during preparation: {f}')
        if target.exists():
            (backups/f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(target, backups/f)
    completed = []
    try:
        for f in changes:
            if (digest(root/f) if (root/f).exists() else None) != baseline.get(f):
                raise ValueError(f'Catalog was edited during publication: {f}')
            catalog.write(root/f, (stage/f).read_text())
            completed.append(f)
        for f in changes:
            if digest(root/f) != digest(stage/f):
                raise ValueError(f'Catalog publication failed verification: {f}')
    except BaseException:
        for f in reversed(completed):
            if digest(root/f) != digest(stage/f):
                raise ValueError(f'Concurrent edit during rollback: {f}')
            if (backups/f).exists():
                catalog.write(root/f, (backups/f).read_text())
            else:
                (root/f).unlink()
        raise


def review_markdown(plan, ledger):
    def cell(value):
        return escape(str(value)).replace('|', '&#124;').replace(chr(10), ' ')

    def table(headings, rows):
        return ['| ' + ' | '.join(headings) + ' |',
                '|' + '---|' * len(headings),
                *['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows], '']

    retirements = plan['retirements']
    catalog_plan = plan['catalog']
    text = ['# Art cleanup review', '',
            f"{len(retirements)} distinct files selected for retirement. "
            f"{len(plan['held'])} selected files held by policy. "
            f"{len(plan['vaultLinkEdits'])} proposed reference edits in {len(plan['vaultNoteHashes'])} vault notes.",
            '', '## Held files', '']
    text += table(['Keep in place'], [(item['file'],) for item in plan['held']])
    text += ['## Vault reference edits', '']
    text += table(['Note and line', 'Current target', 'New target'],
                  [(f"{r['note']} (line {r['line']})",r['old'],r['new']) for r in plan['vaultLinkEdits']])
    text += ['## Catalog', '',
             f"{len(catalog_plan['primaryRepairs'])} primary review records point to a surviving original. "
             f"The physical-file inventory includes {catalog_plan['resultingInventoryPaths']} paths.", '']
    text += table(['Review page', 'Original-file links repaired'],
                  [(r['page'],r['links']) for r in catalog_plan['reviewLinks']])
    text += ['## Session provenance', '',
             f"The merged [session ledger preview](session-image-provenance.preview.json) contains {len(ledger)} records. "
             'The original directory is relative to the RPGs images folder’s _by_session directory.', '',
             '## Proposed file retirements', '',
             'Each line pairs one retiring path with its final keeper. Files sharing a keeper appear together.', '']
    text += table(['Retire', 'Keep'], [(r['retire'],r['keep']) for r in sorted(retirements,key=lambda r:(r['keep'],r['retire']))])
    text += ['The [full plan](cleanup-plan.json) includes hashes, review IDs, and the exact reference edits.', '']
    return chr(10).join(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for arg in ('decisions', 'manifest', 'output'):
        ap.add_argument('--'+arg, required=True, type=Path)
    ap.add_argument('--catalog', type=Path, default=catalog.DEFAULT)
    ap.add_argument('--policy', type=Path)
    ap.add_argument('--publish-catalog', action='store_true')
    args=ap.parse_args()
    root = args.catalog.resolve()
    config = read(root/'config.json')
    roots = {k:Path(v).resolve() for k,v in config['roots'].items()}
    output = args.output.resolve()
    if any(output.is_relative_to(p) for p in [root, *roots.values()]):
        ap.error('Place the review directory outside the catalog and image collections')
    policy = read(args.policy) if args.policy else {}
    with publishing_lock(root, args.publish_catalog), tempfile.TemporaryDirectory() as temp:
        stage = Path(temp)
        watched = [root/n for n in ('source-replacements.json','inventory.json','index.html','set-aside.html',
                                    'config.json','corrections.json','styles.json')]
        watched += list((root/'batches').glob('*.json')) + list((root/'reviews').rglob('*.html')) + list((root/'reviews').glob('*.json'))
        baseline = {p.relative_to(root):digest(p) if p.exists() else None for p in watched}
        mapping, files, ids, held, other = choices(read(args.decisions), read(args.manifest), roots, policy)
        repairs = link_changes(mapping, files, roots)
        ledger_path = roots['RPGs']/'_by_session'/LEDGER
        ledger = session_ledger(mapping, roots, optional(ledger_path, []))
        published, records, references = catalog_repairs(root, config, mapping, files, stage)
        if any((digest(root/p) if (root/p).exists() else None) != prior for p,prior in baseline.items()):
            raise ValueError('Catalog inputs changed during preparation')
        actions = [dict(retire=name(p, roots), keep=name(q, roots), retireSha256=files[p]['sha256'],
                        keepSha256=files[q]['sha256'], decisions=ids[p]) for p,q in mapping.items()]
        note_hashes = {n:digest(roots['Vault']/n) for n in sorted({r['note'] for r in repairs})}
        target_inventory = read(stage/'inventory.json')
        plan = dict(schemaVersion=1, decisionsSha256=digest(args.decisions), manifestSha256=digest(args.manifest),
                    roots={k:str(v) for k,v in roots.items()}, policy=policy, retirements=actions,
                    held=held, otherDecisions=other, vaultLinkEdits=repairs, vaultNoteHashes=note_hashes,
                    sessionLedger=str(ledger_path), sessionRecords=len(ledger),
                    catalog=dict(primaryRepairs=records, reviewLinks=references,
                                 resultingInventoryPaths=len(target_inventory),
                                 publicationFiles=[str(p) for p in published]))
        output.mkdir(parents=True, exist_ok=True)
        catalog.save(output/'cleanup-plan.json', plan)
        catalog.save(output/'session-image-provenance.preview.json', ledger)
        catalog.write(output/'Review.md', review_markdown(plan, ledger))
        if args.publish_catalog:
            publish_catalog(root, stage, published, baseline)
        print(f'{len(actions)} retirements, {len(held)} held, {len(repairs)} vault links, '
              f'{len(ledger)} session records, {len(records)} catalog sources. '
              f'Catalog {"published" if args.publish_catalog else "previewed"}. {output}')


if __name__ == '__main__':
    main()

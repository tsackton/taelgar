#!/usr/bin/env python3
"""Audit Taelgar tilde placeholders and Obsidian link integrity.

The scan is read-only. It indexes every visible Markdown note as a possible
target, while excluding raw/generated source trees, templates, and inline or
fenced code from the source scan. Reports are written as JSON and TSV files.
"""

import argparse
import csv
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path('.').resolve()
OUT = Path('/tmp/taelgar-integrity-audit')
OLD = None

CANON_TOP = {
    'Background', 'Campaigns', 'Cosmology', 'Creatures', 'Events', 'Gazetteer',
    'Gods and Religions', 'Groups', 'History', 'People', 'Primary Sources', 'Things'
}
ATTACHMENT_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.pdf', '.mp3', '.wav',
    '.m4a', '.ogg', '.mp4', '.mov', '.webm', '.avif', '.bmp', '.tif', '.tiff',
    '.canvas', '.excalidraw'
}
LINK_RE = re.compile(r'(!?)\[\[([^\]\n]+)\]\]')
TILDE_RE = re.compile(r'~([^~\n]{1,180})~')
HEADING_RE = re.compile(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$')
BLOCK_RE = re.compile(r'(?:^|\s)\^([A-Za-z0-9_-]+)\s*$')


def rel(path):
    return path.relative_to(ROOT).as_posix()


def indexed_markdown(path):
    r = rel(path)
    parts = Path(r).parts
    if not parts or r == 'AGENTS.md':
        return False
    if parts[0] == '.backups' or any(p.startswith('.') for p in parts):
        return False
    return True


def source_category(r):
    top = Path(r).parts[0]
    if top in CANON_TOP:
        return 'canon'
    if top in {'_DM_', '_dm_notes'}:
        return 'session-dm'
    if (top == '_sessions'
            and '/sources/' not in '/' + r
            and '/cleaned/' not in '/' + r):
        return 'session-dm'
    if r.startswith('Worldbuilding/Staging/'):
        return 'staging'
    if r.startswith('Worldbuilding/Tentative/'):
        return 'tentative'
    if top == 'Worldbuilding':
        return 'worldbuilding'
    if top == '_MoC':
        return 'vault-support'
    return None


def scanned_source(path):
    r = rel(path)
    parts = Path(r).parts
    cat = source_category(r)
    if cat is None:
        return False
    if '_generated' in parts or '_templates' in parts or '_scripts' in parts:
        return False
    if ('_sessions' in parts
            and ('/sources/' in '/' + r or '/cleaned/' in '/' + r)):
        return False
    if r.startswith('Worldbuilding/Chats and Emails/'):
        return False
    if r.startswith('Campaigns/Cleenseau Campaign/Raw Emails/'):
        return False
    if r.startswith("Campaigns/Cleenseau Campaign/Celyn's Stories/"):
        return False
    return True


def split_frontmatter(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == '---':
        for i in range(1, min(len(lines), 500)):
            if lines[i].strip() == '---':
                return lines[1:i], i + 1
    return [], 0


def yaml_scalar(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value.strip()


def parse_aliases(text):
    fm, _ = split_frontmatter(text)
    aliases = []
    for i, line in enumerate(fm):
        m = re.match(r'^aliases\s*:\s*(.*)$', line, re.I)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest.startswith('[') and rest.endswith(']'):
            body = rest[1:-1]
            aliases.extend(yaml_scalar(x) for x in re.split(r'\s*,\s*', body) if yaml_scalar(x))
        elif rest:
            aliases.append(yaml_scalar(rest))
        else:
            for sub in fm[i + 1:]:
                mm = re.match(r'^\s+-\s+(.*)$', sub)
                if mm:
                    aliases.append(yaml_scalar(mm.group(1)))
                elif sub.strip() and not sub.startswith((' ', '\t')):
                    break
        break
    return [a for a in aliases if a and a not in {'[]', 'none', 'null'}]


def strip_code_line(line, in_fence):
    if re.match(r'^\s*(```|~~~)', line):
        return '', not in_fence
    if in_fence:
        return '', in_fence
    return re.sub(r'(`+).*?\1', '', line), in_fence


def contextual_lines(text):
    lines = text.splitlines()
    _, body_start = split_frontmatter(text)
    in_fence = False
    in_comment = False
    for number, original in enumerate(lines, 1):
        line, in_fence = strip_code_line(original, in_fence)
        if not line:
            yield number, '', 'frontmatter' if body_start and number <= body_start else ('comment' if in_comment else 'visible')
            continue
        if body_start and number <= body_start:
            yield number, line, 'frontmatter'
            continue
        visible_parts = []
        comment_parts = []
        pos = 0
        while True:
            marker = line.find('%%', pos)
            if marker < 0:
                (comment_parts if in_comment else visible_parts).append(line[pos:])
                break
            (comment_parts if in_comment else visible_parts).append(line[pos:marker])
            in_comment = not in_comment
            pos = marker + 2
        if visible_parts and ''.join(visible_parts).strip():
            yield number, ''.join(visible_parts), 'visible'
        if comment_parts and ''.join(comment_parts).strip():
            yield number, ''.join(comment_parts), 'comment'


def norm(s):
    return re.sub(r'\s+', ' ', s.strip()).casefold()


def norm_path(s):
    s = s.replace('\\', '/').strip().lstrip('./')
    if s.casefold().endswith('.md'):
        s = s[:-3]
    return norm(s)


def fragment_parts(target):
    if '#' in target:
        base, frag = target.split('#', 1)
        if frag.startswith('^'):
            return base, frag[1:], 'block'
        return base, frag, 'heading'
    if '^' in target:
        base, frag = target.split('^', 1)
        return base, frag, 'block'
    return target, '', None


def candidate_names(target, notes):
    needle = norm(Path(target).name)
    ranked = []
    for note in notes:
        stem = norm(note['stem'])
        score = SequenceMatcher(None, needle, stem).ratio()
        if score >= 0.72:
            ranked.append((score, note['path']))
    return [p for _, p in sorted(ranked, key=lambda x: (-x[0], x[1]))[:5]]


def write_tsv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, delimiter='\t', fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'root', nargs='?', default='.',
        help='Vault root to scan (default: current directory).'
    )
    parser.add_argument(
        '-o', '--output-dir', default='/tmp/taelgar-integrity-audit',
        help='Directory for audit.json and TSV reports.'
    )
    parser.add_argument(
        '--compare',
        help='Optional earlier audit.json used to produce comparison.json.'
    )
    return parser.parse_args()


def main():
    global ROOT, OUT, OLD
    args = parse_args()
    ROOT = Path(args.root).expanduser().resolve()
    OUT = Path(args.output_dir).expanduser().resolve()
    OLD = Path(args.compare).expanduser().resolve() if args.compare else None
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    md_paths = sorted(p for p in ROOT.rglob('*.md') if indexed_markdown(p))
    all_files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '.backups' not in p.parts)
    notes = []
    stems = defaultdict(list)
    paths = defaultdict(list)
    aliases = defaultdict(list)
    note_by_path = {}
    headings = {}
    blocks = {}
    for p in md_paths:
        r = rel(p)
        text = p.read_text(encoding='utf-8', errors='replace')
        item = {'path': r, 'stem': p.stem, 'aliases': parse_aliases(text)}
        notes.append(item)
        note_by_path[r] = item
        stems[norm(p.stem)].append(item)
        paths[norm_path(r)].append(item)
        for a in item['aliases']:
            aliases[norm(a)].append(item)
        hs, bs = set(), set()
        in_fence = False
        for line in text.splitlines():
            clean, in_fence = strip_code_line(line, in_fence)
            if not clean:
                continue
            m = HEADING_RE.match(clean)
            if m:
                hs.add(norm(re.sub(r'\s+#+\s*$', '', m.group(1))))
            m = BLOCK_RE.search(clean)
            if m:
                bs.add(norm(m.group(1)))
        headings[r] = hs
        blocks[r] = bs

    attachment_basenames = defaultdict(list)
    attachment_paths = defaultdict(list)
    for p in all_files:
        if p.suffix.casefold() == '.md':
            continue
        try:
            r = rel(p)
        except ValueError:
            continue
        attachment_basenames[norm(p.name)].append(r)
        attachment_paths[norm(r)].append(r)

    source_paths = [p for p in md_paths if scanned_source(p)]
    broken, ambiguous, tentative, fragment_issues = [], [], [], []
    placeholders, other_tilde = [], []
    link_count = 0
    status_counts = Counter()
    context_counts = Counter()
    category_counts = Counter()

    def resolve_note(base, source):
        base = base.strip()
        if not base:
            return [note_by_path[source]], 'resolved-self'
        np = norm_path(base)
        exact = paths.get(np, [])
        if exact:
            return exact, 'resolved-path'
        if '/' in base:
            suffix = [n for n in notes if norm_path(n['path']).endswith('/' + np)]
            if suffix:
                return suffix, 'resolved-path'
        by_stem = stems.get(norm(Path(base).name.removesuffix('.md')), [])
        if by_stem:
            if len(by_stem) == 1:
                return by_stem, 'resolved'
            source_parent = Path(source).parent.parts
            ranked = sorted(by_stem, key=lambda n: -sum(a == b for a, b in zip(source_parent, Path(n['path']).parent.parts)))
            if len(ranked) == 1:
                return ranked, 'resolved'
            best_score = sum(a == b for a, b in zip(source_parent, Path(ranked[0]['path']).parent.parts))
            next_score = sum(a == b for a, b in zip(source_parent, Path(ranked[1]['path']).parent.parts))
            if best_score > next_score:
                return [ranked[0]], 'resolved'
            return by_stem, 'ambiguous'
        by_alias = aliases.get(norm(base), [])
        if by_alias:
            return by_alias, 'alias-only'
        return [], 'missing'

    for p in source_paths:
        r = rel(p)
        cat = source_category(r)
        text = p.read_text(encoding='utf-8', errors='replace')
        for line_no, line, context in contextual_lines(text):
            if not line:
                continue
            for m in LINK_RE.finditer(line):
                link_count += 1
                embed = bool(m.group(1))
                raw_link = m.group(0)
                inside = m.group(2)
                # Markdown tables escape Obsidian's alias separator as \|.
                # The backslash is not part of the target.
                target_part = inside.split('|', 1)[0].rstrip('\\').strip()
                base, frag, frag_kind = fragment_parts(target_part)
                ext = Path(base).suffix.casefold()
                is_attachment = ext in ATTACHMENT_EXTS
                record = {
                    'source': r, 'source_category': cat, 'line': line_no,
                    'context': context, 'raw_link': raw_link, 'target': base,
                    'fragment': frag, 'embed': embed, 'candidates': []
                }
                category_counts[cat] += 1
                context_counts[context] += 1
                if is_attachment:
                    matches = attachment_paths.get(norm(base), [])
                    if not matches:
                        matches = attachment_basenames.get(norm(Path(base).name), [])
                    if matches:
                        record['status'] = 'resolved-attachment'
                        record['resolved_path'] = matches[0]
                    else:
                        record['status'] = 'missing-attachment'
                        broken.append(record)
                    status_counts[record['status']] += 1
                    continue
                matches, status = resolve_note(base, r)
                if status == 'ambiguous':
                    record['status'] = 'ambiguous'
                    record['candidates'] = [n['path'] for n in matches]
                    ambiguous.append(record)
                    status_counts['ambiguous'] += 1
                    continue
                if status == 'missing':
                    record['status'] = 'missing'
                    record['candidates'] = candidate_names(base, notes)
                    if '/' in base and stems.get(norm(Path(base).name.removesuffix('.md'))):
                        record['status'] = 'obsolete-path'
                        record['candidates'] = [n['path'] for n in stems[norm(Path(base).name.removesuffix('.md'))]]
                    broken.append(record)
                    status_counts[record['status']] += 1
                    continue
                if status == 'alias-only':
                    record['status'] = 'alias-only'
                    record['candidates'] = [n['path'] for n in matches]
                    broken.append(record)
                    status_counts['alias-only'] += 1
                    continue
                record['status'] = 'resolved'
                record['resolved_path'] = matches[0]['path']
                status_counts['resolved'] += 1
                if record['resolved_path'].startswith('Worldbuilding/Tentative/'):
                    tentative.append(record.copy())
                if frag:
                    check = blocks[record['resolved_path']] if frag_kind == 'block' else headings[record['resolved_path']]
                    if norm(frag) not in check:
                        frec = record.copy()
                        frec['fragment_status'] = 'missing-block' if frag_kind == 'block' else 'missing-heading'
                        fragment_issues.append(frec)

            if cat == 'canon':
                for m in TILDE_RE.finditer(line):
                    full = m.group(0)
                    inner = m.group(1).strip()
                    item = {'placeholder': full, 'source': r, 'line': line_no, 'context': context,
                            'snippet': re.sub(r'\s+', ' ', line.strip())[:300]}
                    if (re.search(r'[A-Za-z]', inner)
                            and not re.search(r'\d', inner)
                            and '[[' not in inner and ']]' not in inner
                            and ',' not in inner and ';' not in inner
                            and not inner.endswith('-')):
                        item['classification'] = 'probable-placeholder'
                        item['matching_notes'] = [n['path'] for n in stems.get(norm(inner), [])]
                        placeholders.append(item)
                    else:
                        item['classification'] = 'other-tilde-usage'
                        other_tilde.append(item)

    duplicates = {k: [n['path'] for n in v] for k, v in stems.items() if len(v) > 1}
    metadata = {
        'root': str(ROOT), 'indexed_markdown_notes': len(md_paths),
        'scanned_source_markdown': len(source_paths),
        'canon_source_markdown': sum(1 for p in source_paths if source_category(rel(p)) == 'canon'),
        'total_wikilinks': link_count, 'source_categories': dict(category_counts)
    }
    audit = {
        'metadata': metadata, 'status_counts': dict(status_counts),
        'context_counts': dict(context_counts), 'placeholders': placeholders,
        'other_tilde_usage': other_tilde, 'broken': broken, 'ambiguous': ambiguous,
        'tentative_targets': tentative, 'fragment_issues': fragment_issues,
        'duplicate_note_stems': duplicates
    }
    (OUT / 'audit.json').write_text(json.dumps(audit, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    write_tsv(OUT / 'placeholders.tsv', placeholders,
              ['classification', 'context', 'line', 'matching_notes', 'placeholder', 'snippet', 'source'])
    write_tsv(OUT / 'other_tilde_usage.tsv', other_tilde,
              ['classification', 'context', 'line', 'placeholder', 'snippet', 'source'])
    write_tsv(OUT / 'broken.tsv', broken,
              ['candidates', 'context', 'embed', 'fragment', 'line', 'raw_link', 'source', 'source_category', 'status', 'target'])
    canon_broken = [x for x in broken if x['source_category'] == 'canon']
    write_tsv(OUT / 'canon_broken.tsv', canon_broken,
              ['candidates', 'context', 'embed', 'fragment', 'line', 'raw_link', 'source', 'source_category', 'status', 'target'])
    write_tsv(OUT / 'tentative_targets.tsv', tentative,
              ['context', 'embed', 'fragment', 'line', 'raw_link', 'resolved_path', 'source', 'source_category', 'status', 'target'])
    write_tsv(OUT / 'fragment_issues.tsv', fragment_issues,
              ['context', 'fragment', 'fragment_status', 'line', 'raw_link', 'resolved_path', 'source', 'source_category', 'status', 'target'])

    old = json.loads(OLD.read_text()) if OLD and OLD.exists() else None
    def sig(x):
        return (x.get('source'), x.get('raw_link'), x.get('status'))
    comparison = {}
    if old:
        comparison = {
            'previous': {
                'wikilinks': old['metadata']['total_wikilinks'],
                'placeholders': len(old['placeholders']),
                'unique_placeholders': len({x['placeholder'] for x in old['placeholders']}),
                'broken': len(old['broken']),
                'canon_broken': sum(x.get('source_category') == 'canon' for x in old['broken']),
                'tentative_targets': len(old['tentative_targets']),
                'fragment_issues': len(old['fragment_issues'])
            },
            'current': {
                'wikilinks': link_count,
                'placeholders': len(placeholders),
                'unique_placeholders': len({x['placeholder'] for x in placeholders}),
                'broken': len(broken),
                'canon_broken': len(canon_broken),
                'tentative_targets': len(tentative),
                'fragment_issues': len(fragment_issues)
            },
            'old_broken_now_absent': [x for x in old['broken'] if sig(x) not in {sig(y) for y in broken}],
            'new_broken': [x for x in broken if sig(x) not in {sig(y) for y in old['broken']}]
        }
    (OUT / 'comparison.json').write_text(json.dumps(comparison, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({
        'metadata': metadata,
        'counts': {
            'placeholders': len(placeholders),
            'unique_placeholders': len({x['placeholder'] for x in placeholders}),
            'other_tilde_usage': len(other_tilde),
            'broken': len(broken),
            'canon_broken': len(canon_broken),
            'ambiguous': len(ambiguous),
            'tentative_targets': len(tentative),
            'canon_tentative_targets': sum(x['source_category'] == 'canon' for x in tentative),
            'fragment_issues': len(fragment_issues),
            'missing_attachments': sum(x['status'] == 'missing-attachment' for x in broken),
            'alias_only': sum(x['status'] == 'alias-only' for x in broken),
            'obsolete_paths': sum(x['status'] == 'obsolete-path' for x in broken)
        }
    }, indent=2))


if __name__ == '__main__':
    main()

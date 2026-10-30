"""Portable Markdown review: no processing queue or separate review-state file."""
import copy
import json
from pathlib import Path
import re
import yaml
import transcript_finalize as final
from transcript_core import (WORK, STATE, MARKER, require, safe, sha, current_hash,
    encoded, atomic, commit, parse_units, render_units, validate_baseline,
    validate_turns, words)

HEADER = re.compile(r'^%% transcript-review:v1 (.+) %%$', re.M)
ITEM = re.compile(r'^%% transcript-issue:v1 (.+) %%$', re.M)
POLISH = re.compile(r'^%% transcript-polish:v1 (.+) %%$', re.M)
TURN = re.compile(r'^%% (u\d+:\d+-\d+(?:, u\d+:\d+-\d+)*) %%\n([^:\n]+): (.*?)(?=^%% u\d+:|\Z)', re.M | re.S)


def context_range(units, uid, explicit=None):
    order = {u['uid']: i for i, u in enumerate(units)}
    i = order[uid]
    if explicit:
        require(set(explicit) == {'startUid', 'endUid'}, 'Invalid review context range')
        a, b = order.get(explicit['startUid'], -1), order.get(explicit['endUid'], -1)
        require(0 <= a <= i <= b < len(units), 'Review context must include its target')
    else:
        # A few caption fragments are rarely a complete exchange. Expand through
        # speaker runs, with a word/UID bound; the agent can choose a better range.
        a = b = i
        for direction in (-1, 1):
            edge, count, changes = i, 0, 0
            while 0 <= edge + direction < len(units) and abs(edge - i) < 40:
                nxt = edge + direction
                changes += units[nxt]['speaker'] != units[edge]['speaker']
                edge = nxt
                count += len(words(units[edge]['text']))
                if count >= 180 or (count >= 60 and changes >= 2):
                    break
            if direction < 0: a = edge
            else: b = edge
    return {'startUid': units[a]['uid'], 'endUid': units[b]['uid']}


def context_units(units, bounds):
    order = {u['uid']: i for i, u in enumerate(units)}
    return units[order[bounds['startUid']]:order[bounds['endUid']] + 1]


def target_text(unit, target, replacement):
    require(isinstance(target, dict), 'Review needs an exact target span')
    a, b = target.get('start'), target.get('end')
    require(type(a) is int and type(b) is int and 0 <= a < b <= len(unit['text']), 'Invalid review target bounds')
    require(target.get('before') == unit['text'][a:b], 'Review target before-text differs from source')
    require(replacement is None or (isinstance(replacement, str) and '\n' not in replacement and '\r' not in replacement), 'Invalid span replacement')
    return unit['text'] if replacement is None else unit['text'][:a] + replacement + unit['text'][b:]


def report_path(root):
    matches = list(root.glob('cleaned/*-transcript-review.md'))
    require(len(matches) <= 1, 'Multiple review Markdown files; select the intended bundle')
    return matches[0] if matches else None


def portable(root):
    path = report_path(root)
    return bool(path and HEADER.search(path.read_text(encoding='utf-8')))


def field(section, name, default=None):
    found = re.findall(r'^\*\*' + re.escape(name) + r':\*\* ?(.*)$', section, re.M)
    require(len(found) <= 1, f'Duplicate review field: {name}')
    require(found or default is not None, f'Missing review field: {name}')
    return found[0] if found else default


def read(root):
    path = report_path(root)
    require(path is not None, 'Missing review Markdown')
    text = path.read_text(encoding='utf-8')
    headers = HEADER.findall(text)
    require(len(headers) == 1, 'Review Markdown needs portable control data; do not recreate processing history')
    meta = json.loads(headers[0])
    require(meta.get('version') == 1, 'Unsupported review format')
    issues = []
    matches = list(ITEM.finditer(text))
    for n, match in enumerate(matches):
        section = text[match.end():matches[n+1].start() if n+1 < len(matches) else len(text)]
        issue = json.loads(match[1])
        issue.update(original=field(section, 'Original'), proposal=field(section, 'Proposed', ''),
                     recommendation=field(section, 'Recommendation'), question=field(section, 'Question'),
                     resolution=field(section, 'Resolution'), correction=field(section, 'Correction', ''))
        issue['alternatives'] = re.findall(r'^\*\*Alternative \d+:\*\* (.*)$', section, re.M)
        issues.append(issue)
    updates = [json.loads(m) for m in POLISH.findall(text)]
    require(len({i['id'] for i in issues}) == len(issues), 'Duplicate review issue')
    require(len({u['index'] for u in updates}) == len(updates), 'Duplicate polished turn update')
    return path, meta, issues, updates


def active(root):
    return portable(root) and bool(read(root)[1].get('revisionActive'))


def parse_markdown(text, units):
    matches = list(TURN.finditer(text))
    require(matches, 'Readable transcript has no mapped turns')
    turns = []
    i, offset = 0, 0
    for match in matches:
        sources = []
        for uid, start, end in re.findall(r'(u\d+):(\d+)-(\d+)', match[1]):
            start, end = int(start), int(end)
            require(i < len(units) and uid == units[i]['uid'] and start == offset and start < end <= len(units[i]['text']), 'Readable transcript has incomplete or reordered coverage')
            sources.append(dict(uid=uid, start=start, end=end))
            offset = end
            if offset == len(units[i]['text']): i, offset = i + 1, 0
        turns.append(dict(speaker=match[2], text=match[3].rstrip(), sources=sources))
    require(i == len(units) and offset == 0, 'Readable transcript has missing coverage')
    require(len(re.findall(r'^%% u\d+:', text, re.M)) == len(matches), 'Malformed source mapping')
    return turns, matches


def document(meta, issues, units, turns):
    by_uid = {u['uid']: u for u in units}
    lines = [f"# Transcript Review — {meta['title']}", '',
             f'Decisions awaiting review: {len(issues)}.', '',
             'Review one session at a time. Resolve each item as `proposed`, `alternative 1`, `correction`, or `retain`; leave undecided items `pending`. A correction replaces only the indicated target. Retain preserves the original uncertainty.', '',
             '%% transcript-review:v1 ' + json.dumps(meta, ensure_ascii=False) + ' %%', '']
    affected = set()
    for issue in issues:
        unit = by_uid[issue['uid']]
        target_text(unit, issue['target'], None)
        control = {k: issue[k] for k in ('id', 'uid', 'target', 'contextRange')}
        lines += ['%% transcript-issue:v1 ' + json.dumps(control, ensure_ascii=False) + ' %%',
                  f"### {issue.get('group', issue['uid'])}", '', f"{unit['uid']} · {unit['timing']} · {unit['speaker']}", '',
                  f"**Original:** {unit['text']}", '']
        if issue.get('proposal') and issue['proposal'] != unit['text']:
            lines += [f"**Proposed:** {issue['proposal']}", '']
        else:
            lines += ['**Suggested disposition:** Retain unresolved; no supported correction.', '']
        for n, alternative in enumerate(issue.get('alternatives', []), 1):
            lines += [f'**Alternative {n}:** {alternative}', '']
        lines += [f"**Recommendation:** {issue['recommendation']}", '', f"**Question:** {issue['question']}", '',
                  f"**Resolution:** {issue.get('resolution', 'pending')}", '', f"**Correction:** {issue.get('correction', '')}", '',
                  '**Conversation context:**', '']
        for u in context_units(units, issue['contextRange']):
            lines += [f"> **{u['speaker']}:** {u['text']}", '>']
        lines += ['']
        affected.update(n for n, turn in enumerate(turns) if any(s['uid'] == issue['uid'] for s in turn['sources']))
    for n in sorted(affected):
        # A reviewed turn rewrite is supplied here by the agent before applying a
        # source correction. It is control data in this Markdown, not another file.
        update = dict(index=n, before=turns[n]['text'], after=None, substitutions=[])
        lines += ['%% transcript-polish:v1 ' + json.dumps(update, ensure_ascii=False) + ' %%']
    return '\n'.join(lines) + '\n'


def exported(root, artifacts, issues, units, turns, title, ready, markdown):
    retained = {k: artifacts[k] for k in (*final.RETAINED, 'sessionMetadata')}
    hashes = {p: (sha(markdown) if k == 'polishedMarkdown' else current_hash(safe(root, p))) for k, p in retained.items()}
    meta = dict(version=1, title=title, artifacts=retained, hashes=hashes, qualityComplete=ready,
                revisionActive=False, retainedIssues=sum(i['disposition'] == 'accepted' for i in issues),
                uncertainty=bool(any(i['disposition'] == 'accepted' for i in issues) or any(t.get('substitutions') for t in turns)))
    return document(meta, [i for i in issues if i['disposition'] == 'pending'], units, turns)


def inputs(root):
    path, meta, issues, updates = read(root)
    a = meta['artifacts']
    require(set(a) == set(final.RETAINED) | {'sessionMetadata'}, 'Incomplete review references')
    require(len(set(a.values())) == len(a), 'Review artifact paths overlap')
    require(set(meta['hashes']) == set(a.values()), 'Incomplete review fingerprints')
    for rel, digest in meta['hashes'].items():
        require(current_hash(safe(root, rel)) == digest, f'Review input changed: {rel}; reconcile before applying decisions')
    units = parse_units(safe(root, a['cleaned']).read_text(encoding='utf-8'))
    validate_baseline(parse_units(safe(root, a['prepared']).read_text(encoding='utf-8')), units)
    text = safe(root, a['polishedMarkdown']).read_text(encoding='utf-8')
    turns, matches = parse_markdown(text, units)
    by_uid = {u['uid']: u for u in units}
    for issue in issues:
        require(issue['uid'] in by_uid, 'Unknown review UID')
        target_text(by_uid[issue['uid']], issue['target'], None)
        require(issue['original'] == by_uid[issue['uid']]['text'], 'Review Original differs from current full UID')
        context_range(units, issue['uid'], issue['contextRange'])
    return path, meta, issues, updates, units, text, turns, matches


def status(root):
    path, meta, issues, updates, units, text, turns, matches = inputs(root)
    return dict(bundle=str(root), status='needs_manual_review' if issues else 'ready_to_finalize', finalized=False,
                outputsCurrent=True, units=len(units), pendingMaterialIssues=len(issues),
                pendingMaterialGroups=len(issues), artifacts=dict(meta['artifacts'], review=str(path.relative_to(root))),
                review=str(path), processingStateRequired=False)


def replacement(issue, full):
    a, b = issue['target']['start'], issue['target']['end']
    prefix, suffix = issue['original'][:a], issue['original'][b:]
    require(full.startswith(prefix) and full.endswith(suffix) and len(full) >= len(prefix) + len(suffix), 'Proposal changes text outside its exact target')
    return full[a:len(full)-len(suffix) if suffix else len(full)]


def moved(point, edits):
    shift = 0
    for edit in edits:
        a, b = edit['start'], edit['end']
        require(not a < point < b, 'Correction crosses a turn/speaker boundary; split it into separate span edits')
        if point >= b: shift += len(edit['after']) - (b-a)
    return point + shift


def validate_fragment(turn, by_uid, substitutions):
    clipped, spans, mapped = [], [], []
    for n, span in enumerate(turn['sources']):
        uid = f'u{n+1:04d}'
        a, b = span['start'], span['end']
        clipped.append(dict(uid=uid, speaker=turn['speaker'], text=by_uid[span['uid']]['text'][a:b]))
        spans.append(dict(uid=uid, start=0, end=b-a))
        for sub in substitutions:
            if sub['uid'] == span['uid'] and a <= sub['start'] < sub['end'] <= b:
                mapped.append(dict(sub, uid=uid, start=sub['start']-a, end=sub['end']-a))
    require(len(mapped) == len(substitutions), 'Display substitution is outside the revised turn')
    validate_turns([dict(turn, sources=spans, substitutions=mapped)], clipped, [])


def apply(root):
    path, meta, issues, updates, units, text, turns, matches = inputs(root)
    require(meta.get('qualityComplete') is True, 'Complete source/polish quality review before the Markdown handoff')
    expected = dict(meta['hashes'], **{str(path.relative_to(root)): sha(path.read_bytes())})
    selected, patches = [], {}
    for issue in issues:
        choice = issue['resolution']
        if choice == 'pending': continue
        require(choice in {'retain', 'proposed', 'correction'} or re.fullmatch(r'alternative [1-9]\d*', choice), 'Unknown review resolution')
        selected.append(issue['id'])
        if choice == 'retain':
            meta['retainedIssues'] += 1
            meta['uncertainty'] = True
            continue
        if choice == 'correction':
            after = issue['correction']
        elif choice == 'proposed':
            require(bool(issue['proposal']), 'No proposed correction; choose retain or supply a correction')
            after = replacement(issue, issue['proposal'])
        else:
            index = int(choice.split()[1])-1
            require(index < len(issue['alternatives']), 'Unknown review alternative')
            after = replacement(issue, issue['alternatives'][index])
        require('\n' not in after and '\r' not in after, 'Correction must stay within its UID')
        require(after != issue['target']['before'], 'Unchanged wording is a retain decision, not a correction')
        patches.setdefault(issue['uid'], []).append(dict(issue['target'], after=after))
    if not selected: return status(root)
    for edits in patches.values():
        edits.sort(key=lambda e: e['start'])
        require(all(a['end'] <= b['start'] for a, b in zip(edits, edits[1:])), 'Overlapping review corrections')
    changed = copy.deepcopy(units)
    for unit in changed:
        for edit in reversed(patches.get(unit['uid'], [])):
            unit['text'] = unit['text'][:edit['start']] + edit['after'] + unit['text'][edit['end']:]
    parse_units(render_units(changed))
    by_uid = {u['uid']: u for u in changed}
    next_turns = copy.deepcopy(turns)
    supplied = {u['index']: u for u in updates}
    modified = set()
    for n, turn in enumerate(next_turns):
        touched = False
        for span in turn['sources']:
            edits = patches.get(span['uid'], [])
            touched |= any(e['start'] < span['end'] and e['end'] > span['start'] for e in edits)
            span['start'], span['end'] = moved(span['start'], edits), moved(span['end'], edits)
        if touched:
            update = supplied.get(n, {})
            require(update.get('before') == turns[n]['text'] and isinstance(update.get('after'), str), f'Supply reviewed polished text for turn {n} in the review Markdown')
            turn['text'] = update['after']
            subs = update.get('substitutions', [])
            for sub in subs:
                for edit in patches.get(sub['uid'], []):
                    start = moved(edit['start'], patches[sub['uid']])
                    require(sub['end'] <= start or sub['start'] >= start+len(edit['after']), 'A display substitution hides the accepted correction')
            validate_fragment(turn, by_uid, subs)
            modified.add(n)
    require(all(u.get('after') is None or u['index'] in modified for u in updates), 'Polished update has no corresponding source correction')
    # Preserve untouched bytes and prose; only source offsets and reviewed turns change.
    new_text = text
    for n in reversed(range(len(matches))):
        m, turn = matches[n], next_turns[n]
        mapping = ', '.join(f"{s['uid']}:{s['start']}-{s['end']}" for s in turn['sources'])
        tail = m[3][len(m[3].rstrip()):]
        new_text = new_text[:m.start()] + f"%% {mapping} %%\n{turn['speaker']}: {turn['text']}" + tail + new_text[m.end():]
    parse_markdown(new_text, changed)
    remaining = []
    for issue in issues:
        if issue['id'] in selected: continue
        new_issue = copy.deepcopy(issue)
        edits = patches.get(issue['uid'], [])
        a, b = issue['target']['start'], issue['target']['end']
        require(not any(e['start'] < b and e['end'] > a for e in edits), 'A correction overlaps another pending question; reconcile its target first')
        new_issue['target'].update(start=moved(a, edits), end=moved(b, edits))
        unit = by_uid[issue['uid']]
        new_issue['proposal'] = target_text(unit, new_issue['target'], replacement(issue, issue['proposal'])) if issue['proposal'] else ''
        new_issue['alternatives'] = [target_text(unit, new_issue['target'], replacement(issue, x)) for x in issue['alternatives']]
        remaining.append(new_issue)
    meta['revisionActive'] = True
    uncertain = meta['uncertainty'] or any(MARKER.search(u['text']) for u in changed) or bool(re.search(r'\[(?:garbled|cross-talk)\]', new_text))
    label = 'Some passages need review' if remaining else 'Complete with retained uncertainty' if uncertain else 'Complete'
    require(len(re.findall(r'^- Status: .+$', new_text, re.M)) == 1, 'Missing or duplicate readable status')
    new_text = re.sub(r'^- Status: .+$', '- Status: '+label, new_text, count=1, flags=re.M)
    source_text = safe(root, meta['artifacts']['cleaned']).read_bytes().decode('utf-8')
    for old, new in zip(units, changed):
        if old['text'] == new['text']: continue
        before = old['header'] + old['separator'] + old['text']
        require(source_text.count(before) == 1, 'Source line is not unique')
        source_text = source_text.replace(before, old['header'] + old['separator'] + new['text'], 1)
    files = {meta['artifacts']['cleaned']: source_text, meta['artifacts']['polishedMarkdown']: new_text}
    meta['hashes'].update({rel: sha(value) for rel, value in files.items()})
    files[str(path.relative_to(root))] = document(meta, remaining, changed, next_turns)
    tx = commit(root, files, 'Apply decisions recorded in the portable review Markdown', expected)
    # Recovery snapshots are transient write protection, not review state.
    if tx:
        safe(root, tx).unlink()
        for folder in (safe(root, WORK+'/transactions'), safe(root, WORK)):
            if folder.exists() and not any(folder.iterdir()): folder.rmdir()
    return status(root)


def prepare(root, uids):
    require(not report_path(root), 'A review Markdown already exists; resume it')
    completed = final.completion(root)
    require(completed, 'Preparing a new review requires finalized retained references; imported review Markdown can be used directly')
    manifest, record = completed
    require(final.completed_status(root, manifest, record)['outputsCurrent'], 'Retained references changed; reconcile them before preparing review')
    artifacts = {k: v['path'] for k, v in record['artifacts'].items()}
    artifacts['sessionMetadata'] = manifest
    units = parse_units(safe(root, artifacts['cleaned']).read_text(encoding='utf-8'))
    turns, _ = parse_markdown(safe(root, artifacts['polishedMarkdown']).read_text(encoding='utf-8'), units)
    by_uid = {u['uid']: u for u in units}
    require(uids and len(set(uids)) == len(uids) and all(uid in by_uid for uid in uids), 'Select distinct existing UIDs for bounded review')
    issues = [dict(id='revision-'+uid, uid=uid, target=dict(start=0, end=len(by_uid[uid]['text']), before=by_uid[uid]['text']),
                   contextRange=context_range(units, uid), proposal='', alternatives=[],
                   recommendation='Narrow the target to the words requiring correction; supply supported wording or retain it.',
                   question='Supply a correction or retain the original wording?', disposition='pending') for uid in uids]
    metadata = yaml.safe_load(safe(root, manifest).read_text(encoding='utf-8'))
    meta = dict(version=1, title=f"{metadata['campaign']} — Session {metadata['sessionNumber']}", artifacts=artifacts,
                hashes={p: current_hash(safe(root, p)) for p in artifacts.values()}, qualityComplete=True,
                revisionActive=True, retainedIssues=record['issues'], uncertainty=record['status']=='complete_with_uncertainty')
    review = artifacts['polishedMarkdown'].removesuffix('-transcript.md')+'-transcript-review.md'
    atomic(root, review, document(meta, issues, units, turns).encode())
    return status(root)


def finalize(root):
    path, meta, issues, updates, units, text, turns, matches = inputs(root)
    require(meta.get('qualityComplete') is True and not issues, 'Resolve every review decision before finalization')
    artifacts = meta['artifacts']
    uncertain = meta['uncertainty'] or any(MARKER.search(u['text']) for u in units) or bool(re.search(r'\[(?:garbled|cross-talk)\]', text))
    record = dict(version=1, status='complete_with_uncertainty' if uncertain else 'complete', units=len(units),
                  issues=meta['retainedIssues'], artifacts={k:dict(path=artifacts[k], sha256=meta['hashes'][artifacts[k]]) for k in final.RETAINED})
    manifest = safe(root, artifacts['sessionMetadata'])
    before = manifest.read_bytes()
    after = final.replace_completion(before, record)
    discard, directories = final.work_files(root)
    stem = artifacts['polishedMarkdown'].removesuffix('-transcript.md')
    exports = [stem+s for s in ('-transcript.json','-transcript.html','-transcript-entities.json','-transcript-review.md')]
    for rel in exports:
        digest = current_hash(safe(root, rel))
        if digest is not None: discard[rel] = digest
    plan = dict(version=1, manifest=artifacts['sessionMetadata'], manifestBefore=sha(before), manifestAfter=after.decode(),
                record=record, discard=discard, directories=directories, exports=exports)
    final.validate_plan(root, plan)
    atomic(root, final.PLAN, encoded(plan))
    return final.finish(root)

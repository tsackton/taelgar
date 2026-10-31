"""Bounded corrections to retained transcripts; shared by correct-transcript.

Plans are supplied on stdin, not retained as another review-state file. Preview
is read-only. Application uses the same locks, transactions, parsers and
finalization contracts as process-transcript.
"""
import argparse
import copy
import difflib
import json
from pathlib import Path
import re
import sys

import transcript_core as core
import transcript_finalize as final
import transcript_review as review

REASON = 'Apply bounded transcript corrections'


def fields(value, allowed, required=()):
    core.require(isinstance(value, dict), 'Expected an object')
    core.require(set(required) <= set(value) <= set(allowed), 'Missing or unsupported fields: ' + str(set(value)))


def load(root):
    core.require(not core.safe(root, final.PLAN).exists(), 'Interrupted finalization; run process-transcript finalize first')
    if review.report_path(root):
        path, meta, issues, updates, units, text, turns, matches = review.inputs(root)
        core.require(meta.get('qualityComplete') is True, 'Finish process-transcript quality review first')
        core.require(all(i['resolution'] == 'pending' for i in issues) and
                     all(u.get('after') is None for u in updates),
                     'Apply or reconcile decisions already recorded in the review Markdown first')
        artifacts = meta['artifacts']
        expected = dict(meta['hashes'])
        expected[str(path.relative_to(root))] = core.current_hash(path)
        record = None
    else:
        completed = final.completion(root)
        core.require(completed, 'Requires finalized references or a quality-complete portable review; use process-transcript first')
        manifest, record = completed
        core.require(final.completed_status(root, manifest, record)['outputsCurrent'], 'Finalized references changed; reconcile before editing')
        artifacts = {k: v['path'] for k, v in record['artifacts'].items()}
        artifacts['sessionMetadata'] = manifest
        expected = {p: core.current_hash(core.safe(root, p)) for p in artifacts.values()}
        units = core.parse_units(core.safe(root, artifacts['cleaned']).read_text(encoding='utf-8'))
        core.validate_baseline(core.parse_units(core.safe(root, artifacts['prepared']).read_text(encoding='utf-8')), units)
        text = core.safe(root, artifacts['polishedMarkdown']).read_text(encoding='utf-8')
        turns, matches = review.parse_markdown(text, units)
        path, meta, issues = None, None, []
    return dict(root=root, path=path, meta=meta, record=record, artifacts=artifacts,
                expected=expected, inputDigest=core.fingerprint(expected), units=units,
                text=text, turns=turns, matches=matches, issues=issues)


def inspect(root, uids=()):
    data = load(root)
    ids = set(uids)
    core.require(ids <= {u['uid'] for u in data['units']}, 'Unknown UID')
    turns = [dict(index=n, **t) for n, t in enumerate(data['turns']) if any(s['uid'] in ids for s in t['sources'])]
    included = ids | {s['uid'] for t in turns for s in t['sources']}
    return dict(bundle=str(root), inputDigest=data['inputDigest'],
                finalized=data['path'] is None, artifacts=data['artifacts'],
                units=[{k: u[k] for k in ('uid', 'timing', 'speaker', 'text')} for u in data['units'] if u['uid'] in included],
                turns=turns, issues=data['issues'])


def ranges(spans):
    result = []
    for s in spans:
        fields(s, ('uid', 'start', 'end'), ('uid', 'start', 'end'))
        core.require(isinstance(s['uid'], str) and type(s['start']) is int and type(s['end']) is int and
                     0 <= s['start'] < s['end'], 'Invalid source span')
        if result and result[-1]['uid'] == s['uid'] and result[-1]['end'] == s['start']:
            result[-1]['end'] = s['end']
        else:
            result.append(dict(s))
    return result


def valid_speaker(speaker):
    core.require(isinstance(speaker, str) and speaker.strip() == speaker and bool(speaker) and
                 not any(c in speaker for c in (':', '\n', '\r', '%')), 'Invalid speaker label')


def build(root, plan):
    fields(plan, ('version', 'inputDigest', 'edits', 'turns', 'decisions'), ('version', 'inputDigest'))
    core.require(plan['version'] == 1, 'Unsupported correction plan version')
    data = load(root)
    core.require(plan['inputDigest'] == data['inputDigest'], 'Stale correction plan; inspect current inputs')
    for key in ('edits', 'turns', 'decisions'):
        core.require(isinstance(plan.get(key, []), list), key + ' must be a list')
    core.require(any(plan.get(k) for k in ('edits', 'turns', 'decisions')), 'No corrections or decisions supplied')
    units = copy.deepcopy(data['units'])
    old_by = {u['uid']: u for u in data['units']}
    patches = {}
    for edit in plan.get('edits', []):
        fields(edit, ('uid', 'start', 'end', 'before', 'after'), ('uid', 'start', 'end', 'before', 'after'))
        core.require(edit['uid'] in old_by, 'Unknown correction UID')
        target = {k: edit[k] for k in ('start', 'end', 'before')}
        core.require(isinstance(edit['after'], str), 'Replacement must be text')
        review.target_text(old_by[edit['uid']], target, edit['after'])
        core.require(edit['before'] != edit['after'], 'Unchanged replacement')
        patches.setdefault(edit['uid'], []).append(dict(target, after=edit['after']))
    for edits in patches.values():
        edits.sort(key=lambda e: e['start'])
        core.require(all(a['end'] <= b['start'] for a, b in zip(edits, edits[1:])), 'Overlapping source edits')
    for unit in units:
        for edit in reversed(patches.get(unit['uid'], [])):
            unit['text'] = unit['text'][:edit['start']] + edit['after'] + unit['text'][edit['end']:]
    core.parse_units(core.render_units(units))
    by_uid = {u['uid']: u for u in units}
    supplied = {}
    for item in plan.get('turns', []):
        fields(item, ('index', 'before', 'after', 'speaker', 'parts', 'substitutions'), ('index', 'before'))
        n = item['index']
        core.require(type(n) is int and 0 <= n < len(data['turns']) and n not in supplied, 'Unknown or duplicate turn index')
        core.require(item['before'] == data['turns'][n]['text'], 'Polished before-text differs')
        core.require(set(item) - {'index', 'before'}, 'Turn update has no change')
        core.require('parts' not in item or not set(item).intersection(('after', 'speaker', 'substitutions')),
                     'Use either parts or a single-turn update')
        supplied[n] = item
    groups, next_turns = [], []
    for n, original in enumerate(data['turns']):
        turn = copy.deepcopy(original)
        touched = []
        for span in turn['sources']:
            edits = patches.get(span['uid'], [])
            touched.extend(e for e in edits if e['start'] < span['end'] and e['end'] > span['start'])
            span['start'], span['end'] = review.moved(span['start'], edits), review.moved(span['end'], edits)
        item = supplied.get(n)
        if item and 'parts' in item:
            parts = copy.deepcopy(item['parts'])
            core.require(isinstance(parts, list) and parts, 'Split needs complete replacement parts')
            for part in parts:
                fields(part, ('speaker', 'text', 'sources', 'substitutions'), ('speaker', 'text', 'sources'))
            core.require(ranges([s for part in parts for s in part['sources']]) == ranges(turn['sources']),
                         'Split parts must partition exactly the original turn source ranges')
        else:
            if item and 'after' in item:
                turn['text'] = item['after']
            elif touched:
                # Only exact, unique display matches are automatic. Punctuation,
                # repetitions or substitutions may require a supplied full turn.
                for edit in reversed(touched):
                    core.require(turn['text'].count(edit['before']) == 1,
                                 f'Supply explicit after text for polished turn {n}; display match is ambiguous or absent')
                    turn['text'] = turn['text'].replace(edit['before'], edit['after'], 1)
            if item and 'speaker' in item:
                turn['speaker'] = item['speaker']
            if item and 'substitutions' in item:
                turn['substitutions'] = item['substitutions']
            parts = [turn]
        for part in parts:
            valid_speaker(part['speaker'])
            core.require(isinstance(part['text'], str) and part['text'].strip(), 'Empty polished text')
            # Pure relabelling preserves already-reviewed text, including labels
            # whose transient substitution records were retired at finalization.
            unchanged_speech = not touched and len(parts) == 1 and part['text'] == original['text'] and part['sources'] == original['sources']
            if (item or touched) and not unchanged_speech:
                review.validate_fragment(part, by_uid, part.get('substitutions', []))
            next_turns.append({k: part[k] for k in ('speaker', 'text', 'sources')})
        groups.append(parts)
    text = data['text']
    for n in reversed(range(len(groups))):
        parts = groups[n]
        if len(parts) == 1 and all(parts[0][k] == data['turns'][n][k] for k in ('speaker', 'text', 'sources')):
            continue
        match = data['matches'][n]
        rendered = []
        for part in parts:
            mapping = ', '.join(f"{s['uid']}:{s['start']}-{s['end']}" for s in part['sources'])
            rendered.append(f"%% {mapping} %%\n{part['speaker']}: {part['text']}")
        tail = match[3][len(match[3].rstrip()):]
        text = text[:match.start()] + '\n\n'.join(rendered) + tail + text[match.end():]
    review.parse_markdown(text, units)
    decisions = {}
    issue_by = {i['id']: i for i in data['issues']}
    retained = data['meta']['retainedIssues'] if data['meta'] else data['record']['issues']
    for decision in plan.get('decisions', []):
        fields(decision, ('id', 'resolution'), ('id', 'resolution'))
        key, choice = decision['id'], decision['resolution']
        core.require(key in issue_by and key not in decisions, 'Unknown or duplicate review decision')
        core.require(choice in ('corrected', 'retain', 'confirmed'), 'Unknown decision resolution')
        decisions[key] = choice
        if choice == 'retain': retained += 1
    remaining = []
    for issue in data['issues']:
        edits = patches.get(issue['uid'], [])
        a, b = issue['target']['start'], issue['target']['end']
        overlaps = [e for e in edits if e['start'] < b and e['end'] > a]
        choice = decisions.get(issue['id'])
        core.require(not overlaps or choice in ('corrected', 'confirmed'), 'Correction overlaps an unresolved issue; supply its actual decision')
        display_changed = any(
            any(s['uid'] == issue['uid'] and s['start'] < b and s['end'] > a for s in data['turns'][n]['sources'])
            and [{k: p[k] for k in ('speaker','text','sources')} for p in groups[n]] != [data['turns'][n]]
            for n in supplied)
        core.require(choice != 'corrected' or overlaps or display_changed,
                     'Corrected decision needs a matching source or polished-turn change; use confirmed for an already-correct passage')
        if choice: continue
        updated = copy.deepcopy(issue)
        updated['target'].update(start=review.moved(a, edits), end=review.moved(b, edits))
        unit = by_uid[issue['uid']]
        updated['proposal'] = review.target_text(unit, updated['target'], review.replacement(issue, issue['proposal'])) if issue['proposal'] else ''
        updated['alternatives'] = [review.target_text(unit, updated['target'], review.replacement(issue, alt)) for alt in issue['alternatives']]
        remaining.append(updated)
    previous_uncertainty = data['meta']['uncertainty'] if data['meta'] else data['record']['status'] == 'complete_with_uncertainty'
    uncertain = previous_uncertainty or retained > 0 or any(core.MARKER.search(u['text']) for u in units) or bool(re.search(r'\[(?:garbled|cross-talk)\]', text))
    label = 'Some passages need review' if remaining else 'Complete with retained uncertainty' if uncertain else 'Complete'
    core.require(len(re.findall(r'^- Status: .+$', text, re.M)) == 1, 'Missing or duplicate polished status')
    text = re.sub(r'^- Status: .+$', '- Status: ' + label, text, count=1, flags=re.M)
    a = data['artifacts']
    source = core.safe(root, a['cleaned']).read_bytes().decode('utf-8')
    for old, new in zip(data['units'], units):
        if old['text'] == new['text']: continue
        before = old['header'] + old['separator'] + old['text']
        core.require(source.count(before) == 1, 'Source line is not unique')
        source = source.replace(before, old['header'] + old['separator'] + new['text'], 1)
    files = {a['cleaned']: source, a['polishedMarkdown']: text}
    hashes = dict(data['expected'])
    hashes.update({p: core.sha(value) for p, value in files.items()})
    if data['path']:
        meta = copy.deepcopy(data['meta'])
        meta.update(revisionActive=True, retainedIssues=retained, uncertainty=bool(uncertain))
        meta['hashes'] = {p: hashes[p] for p in a.values()}
        files[str(data['path'].relative_to(root))] = review.document(meta, remaining, units, next_turns)
    else:
        record = dict(version=core.VERSION, status='complete_with_uncertainty' if uncertain else 'complete',
                      units=len(units), issues=retained,
                      artifacts={k: dict(path=a[k], sha256=hashes[a[k]]) for k in final.RETAINED})
        files[a['sessionMetadata']] = final.replace_completion(core.safe(root, a['sessionMetadata']).read_bytes(), record)
    changed_files = {p: value for p, value in files.items() if core.sha(value) != data['expected'].get(p)}
    diff = ''.join(''.join(difflib.unified_diff(core.safe(root, p).read_text(encoding='utf-8').splitlines(True),
                         (value.decode() if isinstance(value, bytes) else value).splitlines(True), fromfile=p, tofile=p))
                   for p, value in changed_files.items())
    dependencies = [str(p.relative_to(root)) for pattern in ('*-scene-map.json', '*-entity-map.json', '*-interactions-draft.md', '*-beats.json', '*-beat-facts.json', '*-session-recap.md')
                    for p in (root/'cleaned').glob(pattern)]
    return dict(data=data, files=changed_files, remaining=remaining, preview=dict(
        inputDigest=data['inputDigest'], changedFiles=list(changed_files), diff=diff,
        pendingIssues=len(remaining), finalizesReview=bool(data['path'] and not remaining),
        downstreamToInspect=dependencies))


def retire_transactions(root):
    """Retire only committed correction snapshots, never active pipeline work."""
    folder = core.safe(root, core.WORK + '/transactions')
    for path in sorted(folder.glob('*.json')) if folder.exists() else []:
        tx = core.read_json(path)
        if tx.get('reason') == REASON and tx.get('status') == 'committed':
            path.unlink()
    for rel in (core.WORK + '/transactions', core.WORK):
        folder = core.safe(root, rel)
        if folder.exists() and not any(folder.iterdir()): folder.rmdir()


def recover(root):
    with core.lock(root):
        recovered = core.recover(root)
        if core.safe(root, final.PLAN).exists(): final.finish(root)
        data = load(root)
        retire_transactions(root)
        if data['path']:
            status = review.status(root) if data['issues'] else review.finalize(root)
        else:
            status = final.completed_status(root, *final.completion(root))
        return dict(recovered=recovered, status=status)


def apply(root, plan):
    with core.lock(root):
        core.recover(root)
        result = build(root, plan)
        core.commit(root, result['files'], REASON, result['data']['expected'])
        retire_transactions(root)
        if result['data']['path']:
            status = review.status(root) if result['remaining'] else review.finalize(root)
        else:
            status = final.completed_status(root, *final.completion(root))
        return dict(result['preview'], applied=True, status=status)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', required=True, type=Path)
    sub = parser.add_subparsers(dest='command', required=True)
    show = sub.add_parser('inspect')
    show.add_argument('--uid', action='append', default=[])
    sub.add_parser('recover')
    for name in ('preview', 'apply'):
        command = sub.add_parser(name)
        command.add_argument('--plan', choices=['-'], required=True, help='Read the correction object from stdin')
    args = parser.parse_args()
    try:
        root = args.bundle.expanduser().resolve()
        core.require(root.is_dir(), 'Session bundle does not exist')
        if args.command == 'inspect': result = inspect(root, args.uid)
        elif args.command == 'recover': result = recover(root)
        else:
            plan = json.load(sys.stdin)
            result = build(root, plan)['preview'] if args.command == 'preview' else apply(root, plan)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (core.PipelineError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

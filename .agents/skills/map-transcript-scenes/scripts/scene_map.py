#!/usr/bin/env python3
"""Read, validate and save agent-authored scene maps; no model calls or segmentation heuristics."""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import sys
from urllib.parse import quote

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'prepare-interaction-transcript' / 'scripts'))
import interaction_draft as draft
from transcript_core import atomic, lock, safe

VAULT = Path(__file__).resolve().parents[4]
SCENE_TYPES = {'conversation', 'exploration', 'combat', 'travel'}
CONTEXT_KINDS = {'recap', 'loreDiscussion', 'tableChatter'}
FINDING_KINDS = {'boundary', 'context', 'location', 'dateConflict'}
YAML_TIME_FIELDS = {'drStart', 'drEnd', 'drStartTime', 'drEndTime'}
YAML_DATE_FIELDS = YAML_TIME_FIELDS | {'realWorldDate'}
DATE_RESULTS = {'consistent', 'conflict', 'insufficientEvidence'}


class MapError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise MapError(message)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def digest(value):
    return draft.sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                               separators=(',', ':'), default=str))


def object_fields(value, required, optional, label):
    require(isinstance(value, dict), f'{label} must be an object')
    require(required <= value.keys(), f'{label} missing fields: {sorted(required - value.keys())}')
    require(value.keys() <= required | optional,
            f'{label} has unknown fields: {sorted(value.keys() - required - optional)}')


def string(value, label, limit=None, nullable=False):
    if value is None and nullable:
        return
    require(isinstance(value, str) and value.strip() and '\n' not in value and '\r' not in value,
            f'{label} must be nonempty single-line text')
    if limit:
        require(len(value.split()) <= limit, f'{label} exceeds {limit} words')


def load(session_yaml, vault_root=VAULT):
    bundle = draft.load(session_yaml)
    vault = Path(vault_root).resolve()
    require(bundle['manifest'].is_relative_to(vault), 'Session YAML must be inside the selected vault')
    session_relative = bundle['manifest'].relative_to(vault).as_posix()
    safe(vault, session_relative)
    groups, lines = [], {}
    line = bundle['header'].count('\n') + 1
    for turn in bundle['turns']:
        for uid, _, _ in turn['spans']:
            lines.setdefault(uid, line)
        line += turn['raw'].count('\n')
        start, end = turn['spans'][0][0], turn['spans'][-1][0]
        if groups and start == groups[-1]['endUid']:
            groups[-1]['endUid'] = end
            groups[-1]['turns'].append(turn)
        else:
            groups.append({'startUid': start, 'endUid': end, 'turns': [turn]})
    sources = {draft.SOURCE_ID: bundle['sourceSha256']}
    artifacts = bundle['data']['transcriptProcessing']['artifacts']
    if artifacts.get('cleaned'):
        sources['transcriptProcessing.artifacts.cleaned'] = bundle['fingerprints'][artifacts['cleaned']['path']]
    metadata = {k: v for k, v in bundle['data'].items() if k != 'interactionExtraction'}
    inputs = {'sessionYamlDigest': digest(metadata), 'sources': sources}
    stem = bundle['manifest'].name.removesuffix('-session.yaml')
    bundle.update(vault=vault, sessionYaml=session_relative, groups=groups, lines=lines, inputs=inputs,
                  positions={uid: i for i, (uid, _, _) in enumerate(bundle['coverage'])},
                  mapPath=safe(bundle['root'], f'cleaned/{stem}-scene-map.json'))
    bundle['inputDigest'] = digest({'sessionYaml': session_relative, 'inputs': inputs})
    return bundle


def source(start, end):
    return {'kind': 'transcript', 'sourceId': draft.SOURCE_ID, 'startUid': start, 'endUid': end}


def source_bounds(bundle, value, label, boundary=True):
    object_fields(value, {'kind', 'sourceId', 'startUid', 'endUid'}, set(), label)
    require(value['kind'] == 'transcript' and value['sourceId'] == draft.SOURCE_ID,
            f'{label} must reference the YAML polished transcript artifact')
    for key in ('startUid', 'endUid'):
        require(isinstance(value[key], str) and value[key] in bundle['positions'],
                f'{label} has unknown {key}: {value[key]}')
    start, end = (bundle['positions'][value[k]] for k in ('startUid', 'endUid'))
    require(start <= end, f'{label} range is reversed')
    if boundary:
        require(value['startUid'] in {g['startUid'] for g in bundle['groups']}
                and value['endUid'] in {g['endUid'] for g in bundle['groups']},
                f'{label} boundary splits a polished turn or shared UID group')
    return start, end


def date_value(value, label):
    if value is None:
        return None
    string(value, label)
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise MapError(f'{label} must be an ISO date') from exc
    require(parsed.isoformat() == value, f'{label} must be YYYY-MM-DD')
    return parsed


def validate(bundle, document):
    object_fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'scenes', 'contextBlocks'},
                  {'findings', 'dateValidation'}, 'map')
    require(type(document['schemaVersion']) is int and document['schemaVersion'] == 1,
            'Unsupported scene-map version')
    require(document['sessionYaml'] == bundle['sessionYaml'], 'Map belongs to a different session YAML')
    require(document['inputs'] == bundle['inputs'], 'Map inputs changed; recheck the map against current sources/YAML')
    intervals, notices = [], []
    yaml_start, yaml_end = (date.fromisoformat(str(bundle['data'][k])) for k in ('drStart', 'drEnd'))
    for collection in ('scenes', 'contextBlocks'):
        rows = document[collection]
        require(isinstance(rows, list), f'{collection} must be an array')
        last_position, last_index = -1, 0
        for n, row in enumerate(rows):
            label = f'{collection}[{n}]'
            if collection == 'scenes':
                object_fields(row, {'index', 'source'},
                              {'type', 'location', 'locationDetail', 'dateStart', 'dateEnd', 'time', 'aiSummary'}, label)
                require(type(row['index']) is int and row['index'] > last_index,
                        'Scene indexes must be positive, unique and increasing')
                last_index = row['index']
                if 'type' in row:
                    require(isinstance(row['type'], str) and row['type'] in SCENE_TYPES, f'{label} has unknown scene type')
                for key in ('location', 'locationDetail', 'time'):
                    if key in row:
                        string(row[key], f'{label}.{key}', nullable=True)
                if row.get('location'):
                    path = safe(bundle['vault'], row['location'])
                    require(path.suffix == '.md' and path.is_file(), f'{label} location note does not exist')
                    require(not any(p.startswith('_DM_') or p == '_dm_notes' for p in path.relative_to(bundle['vault']).parts),
                            f'{label} cannot expose private DM paths')
                starts, ends = (date_value(row.get(k), f'{label}.{k}') for k in ('dateStart', 'dateEnd'))
                require(not (starts and ends and ends < starts), f'{label} dateEnd precedes dateStart')
                if any(v and not yaml_start <= v <= yaml_end for v in (starts, ends)):
                    notices.append({'severity': 'warning', 'kind': 'dateOutsideYaml', 'scene': row['index'],
                                    'reason': 'Scene date is outside the YAML span; check source framing and the assignment.'})
            else:
                object_fields(row, {'kind', 'source', 'aiSummary'}, set(), label)
                require(isinstance(row['kind'], str) and row['kind'] in CONTEXT_KINDS, f'{label} has unknown context kind')
            if 'aiSummary' in row:
                string(row['aiSummary'], f'{label}.aiSummary', limit=25)
            start, end = source_bounds(bundle, row['source'], label + '.source')
            require(start > last_position, f'{collection} must be ordered and non-overlapping')
            last_position = end
            intervals.append((start, end, label))
    cursor = 0
    for start, end, label in sorted(intervals):
        require(start == cursor, f'Source coverage gap or overlap before {label}')
        cursor = end + 1
    require(cursor == len(bundle['coverage']), 'Source coverage incomplete at end of transcript')
    findings = document.get('findings', [])
    require(isinstance(findings, list), 'findings must be an array')
    for n, finding in enumerate(findings):
        label = f'findings[{n}]'
        object_fields(finding, {'kind', 'source', 'reason'}, {'yamlFields'}, label)
        require(isinstance(finding['kind'], str) and finding['kind'] in FINDING_KINDS, f'{label} has unknown kind')
        source_bounds(bundle, finding['source'], label + '.source')
        string(finding['reason'], label + '.reason')
        if finding['kind'] == 'dateConflict':
            fields = finding.get('yamlFields')
            require(isinstance(fields, list) and fields and all(isinstance(k, str) and k in YAML_DATE_FIELDS for k in fields),
                    'dateConflict must identify affected YAML date/time fields')
            require(len(fields) == len(set(fields)), 'yamlFields must not contain duplicates')
        else:
            require('yamlFields' not in finding, 'yamlFields applies only to dateConflict')
        notices.append({'severity': 'critical' if finding['kind'] == 'dateConflict' else 'info', **finding})
    assessment = document.get('dateValidation')
    if 'dateValidation' not in document:
        assessment = {'result': 'notChecked', 'reason': 'No session date assessment recorded; structural coverage is not date validation.',
                      'evidence': []}
    else:
        object_fields(assessment, {'result', 'reason', 'evidence'}, set(), 'dateValidation')
        require(isinstance(assessment['result'], str) and assessment['result'] in DATE_RESULTS,
                'Unknown dateValidation result')
        string(assessment['reason'], 'dateValidation.reason')
        require(isinstance(assessment['evidence'], list), 'dateValidation.evidence must be an array')
        for ref in assessment['evidence']:
            source_bounds(bundle, ref, 'dateValidation.evidence')
        require(assessment['result'] == 'insufficientEvidence' or assessment['evidence'],
                'A consistent/conflict date assessment requires transcript evidence')
        has_conflict = any(f['kind'] == 'dateConflict' for f in findings)
        require(has_conflict == (assessment['result'] == 'conflict'),
                'Date assessment must agree with recorded dateConflict findings')
    return {'coverage': 'complete', 'sourceUids': len(bundle['coverage']),
            'scenes': len(document['scenes']), 'contextBlocks': len(document['contextBlocks']),
            'dateValidation': assessment, 'findings': notices, 'semanticReview': 'not established by validation'}


def build(bundle, proposal):
    object_fields(proposal, {'scenes', 'contextBlocks', 'dateValidation'}, {'findings'}, 'proposal')
    document = {'schemaVersion': 1, 'sessionYaml': bundle['sessionYaml'],
                'inputs': bundle['inputs'], **proposal}
    validate(bundle, document)
    return document


def check_inputs(bundle):
    for relative, expected in bundle['fingerprints'].items():
        require(draft.sha(safe(bundle['root'], relative).read_bytes()) == expected,
                f'Input changed during mapping: {relative}')


def save(bundle, proposal, expected=None):
    document = build(bundle, proposal)
    with lock(bundle['root']):
        check_inputs(bundle)
        path = safe(bundle['root'], bundle['mapPath'].relative_to(bundle['root']))
        input_paths = {safe(bundle['root'], p) for p in bundle['fingerprints']} | {bundle['draft']}
        require(path not in input_paths, 'Map output aliases an input')
        if path.exists():
            require(path.is_file() and path.stat().st_nlink == 1, 'Existing map must be a regular file, not a hard link')
            require(expected is not None and draft.sha(path.read_bytes()) == expected,
                    'Existing map requires its inspected --expect-sha256; do not overwrite concurrent/human changes')
        else:
            require(expected is None, 'Expected existing map is missing')
        atomic(bundle['root'], path.relative_to(bundle['root']), encoded(document))
    return document


def window(bundle, start_uid=None, end_uid=None, view='auto'):
    require(view in {'auto', 'draft', 'polished'}, 'Unknown reading view')
    start_uid = start_uid or bundle['coverage'][0][0]
    end_uid = end_uid or bundle['coverage'][-1][0]
    start, end = source_bounds(bundle, source(start_uid, end_uid), 'reading window', boundary=False)
    selected = [g for g in bundle['groups']
                if bundle['positions'][g['endUid']] >= start and bundle['positions'][g['startUid']] <= end]
    start, end = bundle['positions'][selected[0]['startUid']], bundle['positions'][selected[-1]['endUid']]
    use_draft = view == 'draft' or (view == 'auto' and bundle['draft'].exists())
    note = ''
    if use_draft:
        _, blocks, _ = draft.inspect_draft(bundle)
        # Do not attribute a collapsed snip from outside the window to this scene.
        relevant = [b for b in blocks if bundle['positions'][b['spans'][-1][0]] >= start
                    and bundle['positions'][b['spans'][0][0]] <= end]
        if any(bundle['positions'][b['spans'][0][0]] < start or bundle['positions'][b['spans'][-1][0]] > end
               for b in relevant):
            use_draft = False
            note = 'Collapsed draft snip crosses this window; showing polished source.\n\n'
    if not use_draft:
        relevant = [t for group in selected for t in group['turns']]
    # Merge adjacent turns sharing a UID so displayed endpoints are always safe.
    rendered = []
    for block in relevant:
        first, last = block['spans'][0][0], block['spans'][-1][0]
        if rendered and rendered[-1][1] == first:
            rendered[-1][1] = last
            rendered[-1][2] += block['body']
        else:
            rendered.append([first, last, block['body']])
    label = 'draft; ((labels)) are generated' if use_draft else 'polished source'
    return note + f'View: {label}\n\n' + ''.join(f'[{a}–{z}]\n{body}' for a, z, body in rendered)


def read_map(bundle, path=None):
    document = json.loads(Path(path or bundle['mapPath']).read_text(encoding='utf-8'))
    validate(bundle, document)
    return document


def cell(value):
    return str(value or '—').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '\\|').replace('\n', ' ')


def source_link(bundle, ref):
    label = f"{ref['startUid']}–{ref['endUid']}"
    line = bundle['lines'][ref['startUid']]
    return f"[{label}](<{quote(str(bundle['source']), safe='/')}:{line}>)"


def finding_line(bundle, item):
    ref = item.get('source')
    where = source_link(bundle, ref) if ref else f"scene {item['scene']}"
    fields = ', '.join(f"{k}={cell(bundle['data'].get(k))}" for k in item.get('yamlFields', []))
    return f"- {item['severity']}: {where}" + (f"; YAML {fields}" if fields else '') + f" — {cell(item['reason'])}"


def preview(bundle, document):
    result = validate(bundle, document)
    assessment = result['dateValidation']
    text = ['Provisional scene map; structural validation does not establish semantic review.', '',
            f"Session date validation: **{assessment['result']}** (agent assessment).",
            'YAML: ' + ', '.join(f"{k}={cell(bundle['data'][k])}" for k in ('drStart', 'drEnd', 'drStartTime', 'drEndTime')
                                if bundle['data'].get(k) is not None) + '.',
            cell(assessment['reason'])]
    if assessment['evidence']:
        text.append('Evidence: ' + ', '.join(source_link(bundle, ref) for ref in assessment['evidence']) + '.')
    date_findings = [item for item in result['findings'] if item['kind'] in {'dateConflict', 'dateOutsideYaml'}]
    if date_findings:
        text.extend(['', 'Date findings:', ''])
        text.extend(finding_line(bundle, item) for item in sorted(date_findings, key=lambda f: f['severity'] != 'critical'))
    text.extend(['', '| Scene / context | Source UIDs | Type | Place | Time | AI summary |',
                 '| --- | --- | --- | --- | --- | --- |'])
    rows = [*document['scenes'], *document['contextBlocks']]
    for row in sorted(rows, key=lambda r: bundle['positions'][r['source']['startUid']]):
        ref = row['source']
        label = f"Scene {row['index']}" if 'index' in row else row['kind']
        dates = [row.get(k) for k in ('dateStart', 'dateEnd', 'time') if row.get(k)]
        location = ' / '.join(filter(None, (Path(row['location']).stem if row.get('location') else None, row.get('locationDetail'))))
        values = (label, f"{ref['startUid']}–{ref['endUid']}", row.get('type'), location, ', '.join(dates), row.get('aiSummary'))
        cells = [cell(v) for v in values]
        cells[1] = source_link(bundle, ref)
        text.append('| ' + ' | '.join(cells) + ' |')
    other_findings = [item for item in result['findings'] if item not in date_findings]
    if other_findings:
        text.extend(['', 'Other findings:', ''])
        text.extend(finding_line(bundle, item) for item in other_findings)
    relative = bundle['source'].relative_to(bundle['vault']).as_posix()
    text.extend(['', f"Polished source: [{cell(relative)}](<{quote(str(bundle['source']), safe='/')}>)",
                 'Source links open the first mapped line; use the UID range to retrieve the whole passage.'])
    return '\n'.join(text) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session-yaml', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('inspect')
    show = sub.add_parser('show')
    show.add_argument('--start-uid')
    show.add_argument('--end-uid')
    show.add_argument('--view', choices=['auto', 'draft', 'polished'], default='auto')
    for command in ('validate', 'preview'):
        sub.add_parser(command).add_argument('--map')
    writer = sub.add_parser('save')
    writer.add_argument('--proposal', required=True, help='JSON file, or - for stdin')
    writer.add_argument('--expect-input-digest', required=True, help='inputDigest returned by inspect when the mapping began')
    writer.add_argument('--expect-sha256', help='Hash of an existing map, required only for intentional revision')
    args = parser.parse_args()
    try:
        bundle = load(args.session_yaml)
        if args.command == 'inspect':
            result = {'sessionYaml': bundle['sessionYaml'], 'inputDigest': bundle['inputDigest'],
                      'dates': {k: str(bundle['data'][k]) for k in ('realWorldDate', 'drStart', 'drEnd')},
                      'sourceUids': len(bundle['coverage']), 'safeGroups': len(bundle['groups']),
                      'draftAvailable': bundle['draft'].exists(), 'map': str(bundle['mapPath']),
                      'mapSha256': draft.sha(bundle['mapPath'].read_bytes()) if bundle['mapPath'].exists() else None}
        elif args.command == 'show':
            print(window(bundle, args.start_uid, args.end_uid, args.view), end='')
            return
        elif args.command == 'save':
            require(args.expect_input_digest == bundle['inputDigest'], 'Inputs changed since inspect; recheck before saving')
            proposal = json.load(sys.stdin) if args.proposal == '-' else json.loads(Path(args.proposal).read_text(encoding='utf-8'))
            result = validate(bundle, save(bundle, proposal, args.expect_sha256))
        else:
            document = read_map(bundle, args.map)
            if args.command == 'preview':
                print(preview(bundle, document), end='')
                return
            result = validate(bundle, document)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

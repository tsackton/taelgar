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
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / '_scripts'))
from taelgar_session.sources import (load, source, source_bounds, check_inputs,
                                     window, source_link)
from taelgar_session import transcript as draft
from taelgar_session.storage import atomic, lock, safe
from taelgar_session.validation import (MapError, require, encoded, digest,
    object_fields, string, validate_review, CONFIDENCE_RATINGS, REVIEW_STATUSES, cell)

VAULT = Path(__file__).resolve().parents[4]
SCENE_TYPES = {'conversation', 'exploration', 'combat', 'travel'}
CONTEXT_KINDS = {'recap', 'loreDiscussion', 'tableChatter'}
LEGACY_FINDING_KINDS = {'boundary', 'context', 'location', 'dateConflict'}
YAML_TIME_FIELDS = {'drStart', 'drEnd', 'drStartTime', 'drEndTime'}
YAML_DATE_FIELDS = YAML_TIME_FIELDS | {'realWorldDate'}
LEGACY_DATE_RESULTS = {'consistent', 'conflict', 'insufficientEvidence'}
SCHEMA_VERSION = 2


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


def validate_issues(bundle, issues):
    require(isinstance(issues, list), 'issues must be an array')
    for n, issue in enumerate(issues):
        label = f'issues[{n}]'
        object_fields(issue, {'description'}, {'evidence'}, label)
        string(issue['description'], label + '.description')
        if 'evidence' in issue:
            require(isinstance(issue['evidence'], list) and issue['evidence'],
                    f'{label}.evidence must be a nonempty array when supplied')
            for ref in issue['evidence']:
                source_bounds(bundle, ref, label + '.evidence')
    return issues


def legacy_issues(bundle, document):
    """Read v1 concerns without writing a migration or retaining positive assessments."""
    findings = document.get('findings', [])
    require(isinstance(findings, list), 'Legacy findings must be an array')
    issues = []
    for finding in findings:
        object_fields(finding, {'kind', 'source', 'reason'}, {'yamlFields'}, 'legacy finding')
        require(isinstance(finding['kind'], str) and finding['kind'] in LEGACY_FINDING_KINDS,
                'Unknown legacy finding kind')
        source_bounds(bundle, finding['source'], 'legacy finding.source')
        string(finding['reason'], 'legacy finding.reason')
        prefix = finding['kind']
        if finding['kind'] == 'dateConflict':
            fields = finding.get('yamlFields')
            require(isinstance(fields, list) and fields
                    and all(isinstance(k, str) and k in YAML_DATE_FIELDS for k in fields),
                    'Legacy dateConflict must identify affected YAML date/time fields')
            require(len(fields) == len(set(fields)), 'yamlFields must not contain duplicates')
            prefix = 'Date concern (' + ', '.join(fields) + ')'
        else:
            require('yamlFields' not in finding, 'yamlFields applies only to legacy dateConflict')
        issues.append({'description': prefix + ': ' + finding['reason'],
                       'evidence': [finding['source']]})
    if 'dateValidation' in document:
        old = document['dateValidation']
        object_fields(old, {'result', 'reason', 'evidence'}, set(), 'legacy dateValidation')
        require(isinstance(old['result'], str) and old['result'] in LEGACY_DATE_RESULTS,
                'Unknown legacy dateValidation result')
        string(old['reason'], 'legacy dateValidation.reason')
        require(isinstance(old['evidence'], list), 'Legacy date evidence must be an array')
        for ref in old['evidence']:
            source_bounds(bundle, ref, 'legacy date evidence')
        require(old['result'] == 'insufficientEvidence' or old['evidence'],
                'Legacy consistent/conflict assessment requires evidence')
        require(any(f['kind'] == 'dateConflict' for f in findings) == (old['result'] == 'conflict'),
                'Legacy date assessment must agree with its findings')
        if old['result'] == 'insufficientEvidence':
            issue = {'description': old['reason']}
            if old['evidence']:
                issue['evidence'] = old['evidence']
            issues.append(issue)
    return validate_issues(bundle, issues)


def validate(bundle, document):
    object_fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'scenes', 'contextBlocks'},
                  {'issues', 'review', 'findings', 'dateValidation', 'splitConfidence'}, 'map')
    require(type(document['schemaVersion']) is int and document['schemaVersion'] in (1, SCHEMA_VERSION),
            'Unsupported scene-map version')
    if document['schemaVersion'] == SCHEMA_VERSION:
        object_fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'scenes', 'contextBlocks',
                                'review'}, {'issues'}, 'map')
        validate_review(document['review'])
    else:
        object_fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'scenes', 'contextBlocks'},
                      {'findings', 'dateValidation', 'splitConfidence'}, 'legacy map')
        if 'splitConfidence' in document:
            legacy = document['splitConfidence']
            object_fields(legacy, {'rating', 'reason'}, set(), 'legacy splitConfidence')
            require(isinstance(legacy['rating'], str) and legacy['rating'] in CONFIDENCE_RATINGS,
                    'Unknown legacy splitConfidence rating')
            string(legacy['reason'], 'legacy splitConfidence.reason')
    require(document['sessionYaml'] == bundle['sessionYaml'], 'Map belongs to a different session YAML')
    require(document['inputs'] == bundle['inputs'], 'Map inputs changed; recheck the map against current sources/YAML')
    intervals = []
    for collection in ('scenes', 'contextBlocks'):
        rows = document[collection]
        require(isinstance(rows, list), f'{collection} must be an array')
        last_position, last_index = -1, 0
        for n, row in enumerate(rows):
            label = f'{collection}[{n}]'
            if collection == 'scenes':
                time_fields = {'time'} if document['schemaVersion'] == 1 else {'timeStart', 'timeEnd'}
                object_fields(row, {'index', 'source'},
                              {'type', 'location', 'locationDetail', 'dateStart', 'dateEnd', 'aiSummary'} | time_fields, label)
                require(type(row['index']) is int and row['index'] > last_index,
                        'Scene indexes must be positive, unique and increasing')
                last_index = row['index']
                if 'type' in row:
                    require(isinstance(row['type'], str) and row['type'] in SCENE_TYPES, f'{label} has unknown scene type')
                for key in ('location', 'locationDetail', *sorted(time_fields)):
                    if key in row:
                        string(row[key], f'{label}.{key}', nullable=True)
                if row.get('location'):
                    path = safe(bundle['vault'], row['location'])
                    require(path.suffix == '.md' and path.is_file(), f'{label} location note does not exist')
                    require(not any(p.startswith('_DM_') or p == '_dm_notes' for p in path.relative_to(bundle['vault']).parts),
                            f'{label} cannot expose private DM paths')
                starts, ends = (date_value(row.get(k), f'{label}.{k}') for k in ('dateStart', 'dateEnd'))
                require(not (starts and ends and ends < starts), f'{label} dateEnd precedes dateStart')
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
    issues = (legacy_issues(bundle, document) if document['schemaVersion'] == 1
              else validate_issues(bundle, document.get('issues', [])))
    return {'coverage': 'complete', 'sourceUids': len(bundle['coverage']),
            'scenes': len(document['scenes']), 'contextBlocks': len(document['contextBlocks']),
            'review': document.get('review'), 'issues': issues, 'semanticReview': 'not established by validation'}


def build(bundle, proposal):
    object_fields(proposal, {'scenes', 'contextBlocks', 'review'}, {'issues'}, 'proposal')
    document = {'schemaVersion': SCHEMA_VERSION, 'sessionYaml': bundle['sessionYaml'],
                'inputs': bundle['inputs'], **proposal}
    validate(bundle, document)
    return document


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


def read_map(bundle, path=None):
    document = json.loads(Path(path or bundle['mapPath']).read_text(encoding='utf-8'))
    validate(bundle, document)
    return document


def issue_line(bundle, issue):
    text = '- ' + cell(issue['description'])
    evidence = issue.get('evidence', [])
    if evidence:
        text += ' — ' + ', '.join(source_link(bundle, ref) for ref in evidence)
    return text


def preview(bundle, document):
    result = validate(bundle, document)
    text = ['Provisional scene map; structural validation does not establish semantic review.', '']
    if result['issues']:
        text.extend(['AI-generated concerns:', ''])
        text.extend(issue_line(bundle, issue) for issue in result['issues'])
        text.append('')
    text.append('YAML: ' + ', '.join(f"{k}={cell(bundle['data'][k])}"
                for k in ('drStart', 'drEnd', 'drStartTime', 'drEndTime')
                if bundle['data'].get(k) is not None) + '.')
    review = result['review']
    review_text = (f"**{review['confidence']} / {review['status']}**" if review
                   else '**not recorded** (legacy map)')
    text.extend(['', f'Scene map review: {review_text}.'])
    legacy_times = document['schemaVersion'] == 1
    dates = [row.get('dateStart') for row in document['scenes']]
    common_date = dates[0] if dates and dates[0] and all(
        row.get('dateStart') == dates[0] and (row.get('dateEnd') == dates[0]
            or (legacy_times and row.get('dateEnd') is None))
        for row in document['scenes']) else None
    if common_date:
        text.extend(['', f'Played scenes: {common_date}.'])
    if legacy_times:
        time_headings = ['Time (legacy)' if common_date else 'Date/Time (legacy)']
    else:
        time_headings = ['Start time', 'End time'] if common_date else ['Start', 'End']
    headings = ['Scene / context', 'Source UIDs', 'Type', 'Place', *time_headings, 'AI summary']
    text.extend(['', '| ' + ' | '.join(headings) + ' |',
                 '| ' + ' | '.join('---' for _ in headings) + ' |'])
    rows = [*document['scenes'], *document['contextBlocks']]
    for row in sorted(rows, key=lambda r: bundle['positions'][r['source']['startUid']]):
        ref = row['source']
        label = f"Scene {row['index']}" if 'index' in row else row['kind']
        if legacy_times:
            dates = [] if common_date else list(dict.fromkeys(
                row[k] for k in ('dateStart', 'dateEnd') if row.get(k)))
            timing = [', '.join([*dates, *([row['time']] if row.get('time') else [])])]
        else:
            timing = [', '.join(filter(None, (
                None if common_date else row.get('date' + endpoint), row.get('time' + endpoint))))
                for endpoint in ('Start', 'End')]
        location = []
        if row.get('location'):
            path = bundle['vault'] / row['location']
            location.append(f'[{cell(path.stem)}](<{quote(path.as_posix(), safe="/")}>)')
        if row.get('locationDetail'):
            location.append(cell(row['locationDetail']))
        values = (label, f"{ref['startUid']}–{ref['endUid']}", row.get('type'), '', *timing, row.get('aiSummary'))
        cells = [cell(v) for v in values]
        cells[1] = source_link(bundle, ref)
        cells[3] = ' / '.join(location) or '—'
        text.append('| ' + ' | '.join(cells) + ' |')
    relative = bundle['source'].relative_to(bundle['vault']).as_posix()
    text.extend(['', f"Polished source: [{cell(relative)}](<{quote(bundle['source'].as_posix(), safe='/')}>)",
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

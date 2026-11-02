#!/usr/bin/env python3
"""Check/save entity maps from YAML-registered transcripts or prepared narratives."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'map-transcript-scenes' / 'scripts'))
import scene_map as scenes

require = scenes.require
fields = scenes.object_fields
string = scenes.string
KINDS = {'npc', 'divine', 'item', 'organization'}
IMPORTANCE = ('star', 'supporting', 'cameo')
CONFIDENCE = scenes.CONFIDENCE_RATINGS
STATUS = scenes.REVIEW_STATUSES
SCHEMA_VERSION = 4


def note_path(bundle, value):
    string(value, 'note path')
    relative = Path(value)
    require(not relative.is_absolute() and relative.as_posix() == value
            and '..' not in relative.parts, 'Note must be a vault-relative path')
    require(not any(p.startswith(('.', '_')) for p in relative.parts),
            'Private/support paths cannot be entity evidence or targets')
    path = scenes.safe(bundle['vault'], value)
    require(path.suffix == '.md' and path.is_file(), f'Note does not exist: {value}')
    return path


def note_hashes(bundle, paths):
    return {p: scenes.draft.sha(note_path(bundle, p).read_bytes()) for p in sorted(set(paths))}


def note_refs(proposal):
    paths = list(proposal.get('evidenceNotes', []))
    for row in proposal.get('entities', []):
        if row.get('note'):
            paths.append(row['note'])
        paths.extend(row.get('candidates', []))
    return paths


def load(session_yaml, vault_root=scenes.VAULT, notes=()):
    # Reuse source/UID parsing only; scenes.load does not read a scene map.
    data = scenes.draft.yaml.safe_load(Path(session_yaml).read_bytes())
    bundle = (load_narrative(session_yaml, vault_root)
              if isinstance(data, dict) and data.get('sourceType') == 'narrative'
              else scenes.load(session_yaml, vault_root))
    inputs = {'sessionInputs': bundle['inputs'], 'vaultNotes': note_hashes(bundle, notes)}
    stem = bundle['manifest'].name.removesuffix('-session.yaml')
    bundle.update(entityInputs=inputs,
                  entityPath=scenes.safe(bundle['root'], f'cleaned/{stem}-entity-map.json'))
    bundle['entityInputDigest'] = scenes.digest({'sessionYaml': bundle['sessionYaml'], 'inputs': inputs})
    return bundle


def load_narrative(session_yaml, vault_root):
    """Read the registered prepared narrative, never guess a cleaned replacement."""
    manifest = Path(session_yaml).absolute()
    require(manifest.name.endswith('-session.yaml') and manifest.parent.name == 'cleaned',
            'Expected cleaned/<stem>-session.yaml inside a session bundle')
    root, vault = manifest.parent.parent.resolve(), Path(vault_root).resolve()
    manifest = scenes.safe(root, 'cleaned/' + manifest.name)
    require(manifest.is_relative_to(vault), 'Session YAML must be inside the selected vault')
    relative = manifest.relative_to(vault).as_posix()
    scenes.safe(vault, relative)
    raw_yaml = manifest.read_bytes()
    data = scenes.draft.yaml.safe_load(raw_yaml)
    require(isinstance(data, dict) and data.get('sourceType') == 'narrative',
            'YAML sourceType must be narrative')
    registered = data.get('preparedSourcePath')
    string(registered, 'preparedSourcePath')
    stem = manifest.name.removesuffix('-session.yaml')
    path = Path(registered)
    if path.is_absolute():
        # Legacy manifests retain a different machine's vault prefix. Only the
        # exact bundle/cleaned/filename suffix may relocate into this bundle.
        expected = (root.name, 'cleaned', f'{stem}-source-prepared.md')
        require(path.parts[-3:] == expected, 'Unexpected legacy preparedSourcePath')
        path = Path('cleaned') / path.name
    source = scenes.safe(root, path.as_posix())
    require(source != manifest and source.suffix == '.md', 'Invalid narrative source path')
    raw = source.read_bytes()
    units, positions, lines = [], {}, {}
    for line, text in enumerate(raw.decode('utf-8').splitlines(keepends=True), 1):
        if not text.strip():
            continue
        match = re.fullmatch(r'\[(u\d{4,})\] ([^\r\n]+)\n?', text)
        require(match is not None, f'Invalid prepared narrative UID line {line}')
        uid, wording = match.groups()
        require(uid not in positions and wording.strip(), 'Duplicate UID or empty narrative unit')
        positions[uid], lines[uid] = len(units), line
        units.append((uid, text))
    require(units, 'Narrative source is empty')
    inputs = {'sessionYamlDigest': scenes.digest({k: v for k, v in data.items() if k != 'interactionExtraction'}),
              'sources': {'preparedSourcePath': scenes.draft.sha(raw)}}
    return {'root': root, 'vault': vault, 'manifest': manifest, 'data': data,
            'sessionYaml': relative, 'source': source, 'narrativeUnits': units,
            'positions': positions, 'lines': lines, 'inputs': inputs,
            'fingerprints': {manifest.relative_to(root).as_posix(): scenes.draft.sha(raw_yaml),
                             source.relative_to(root).as_posix(): scenes.draft.sha(raw)},
            'draft': scenes.safe(root, f'cleaned/{stem}-interactions-draft.md'),
            'mapPath': scenes.safe(root, f'cleaned/{stem}-scene-map.json')}


def source_bounds(bundle, value, label):
    if 'narrativeUnits' not in bundle:
        return scenes.source_bounds(bundle, value, label)
    fields(value, {'kind', 'sourceId', 'startUid', 'endUid'}, set(), label)
    require(value['kind'] == 'narrative' and value['sourceId'] == 'preparedSourcePath',
            f'{label} must reference the YAML prepared narrative')
    for key in ('startUid', 'endUid'):
        require(isinstance(value[key], str) and value[key] in bundle['positions'],
                f'{label} has unknown {key}')
    start, end = (bundle['positions'][value[k]] for k in ('startUid', 'endUid'))
    require(start <= end, f'{label} range is reversed')
    return start, end


def window(bundle, start_uid, end_uid):
    if 'narrativeUnits' not in bundle:
        return scenes.window(bundle, start_uid, end_uid, 'polished')
    ref = {'kind': 'narrative', 'sourceId': 'preparedSourcePath',
           'startUid': start_uid, 'endUid': end_uid}
    start, end = source_bounds(bundle, ref, 'reading window')
    return 'View: prepared narrative source\n\n' + ''.join(t for _, t in bundle['narrativeUnits'][start:end + 1])


def text_array(value, label):
    require(isinstance(value, list), f'{label} must be an array')
    for item in value:
        string(item, label)
    require(len(value) == len(set(value)), f'{label} contains duplicates')


def validate_occurrences(bundle, value, label):
    require(isinstance(value, list) and value, f'{label} needs occurrence evidence')
    last_end = -1
    for item in value:
        fields(item, {'source'}, set(), 'occurrence')
        start, end = source_bounds(bundle, item['source'], f'{label} occurrence source')
        require(start > last_end, f'{label} occurrences must be ordered and non-overlapping')
        last_end = end


def validate(bundle, document):
    fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'entities'},
           {'exclusions', 'evidenceNotes'}, 'entity map')
    if type(document['schemaVersion']) is int and document['schemaVersion'] == 2:
        raise scenes.MapError('Entity-map v2 needs explicit removal of entity reasons, exclusion occurrence arrays, session importance assessment, and a guarded version 4 save')
    require(type(document['schemaVersion']) is int and document['schemaVersion'] in (3, SCHEMA_VERSION),
            'Unsupported entity-map version; recheck legacy decisions and save as version 4')
    rated = document['schemaVersion'] == SCHEMA_VERSION
    require(document['sessionYaml'] == bundle['sessionYaml'], 'Different session YAML')
    expected = {'sessionInputs': bundle['inputs'],
                'vaultNotes': note_hashes(bundle, note_refs(document))}
    require(document['inputs'] == expected, 'Entity inputs changed; recheck sources and vault notes')
    text_array(document.get('evidenceNotes', []), 'evidenceNotes')
    rows = document['entities']
    require(isinstance(rows, list), 'entities must be an array')
    ids, matched, priorities = set(), set(), []
    for row in rows:
        fields(row, {'id', 'kind', 'label', 'occurrences', 'review'} | ({'importance'} if rated else set()),
               {'note', 'names', 'candidates', 'identifiedLater'} |
               ({'examinedInMirrorOfPast'} if rated else set()), 'entity')
        string(row['id'], 'id')
        require(re.fullmatch(r'[a-z][a-z0-9_-]*', row['id']) and row['id'] not in ids,
                'Entity IDs must be unique stable lowercase identifiers')
        ids.add(row['id'])
        require(isinstance(row['kind'], str) and row['kind'] in KINDS, 'Unknown entity kind')
        if 'examinedInMirrorOfPast' in row:
            require(row['kind'] == 'item', 'examinedInMirrorOfPast is only valid for items')
            require(type(row['examinedInMirrorOfPast']) is bool,
                    'examinedInMirrorOfPast must be a boolean')
        if rated:
            require(isinstance(row['importance'], str) and row['importance'] in IMPORTANCE,
                    'Entity importance must be star, supporting, or cameo')
        string(row['label'], 'label')
        text_array(row.get('names', []), 'names')
        text_array(row.get('candidates', []), 'candidates')
        require(type(row.get('identifiedLater', False)) is bool,
                'identifiedLater must be a boolean')
        if row.get('identifiedLater'):
            require(bool(row.get('note')), 'Later identification requires a chosen note')
        scenes.validate_review(row['review'])
        confidence, status = row['review']['confidence'], row['review']['status']
        if 'note' in row:
            string(row['note'], 'note', nullable=True)
        if row.get('note'):
            require(not row.get('candidates'), 'Resolve note OR retain candidates, not both')
            require(row['note'] not in matched, 'Multiple entities matched to the same note')
            matched.add(row['note'])
        validate_occurrences(bundle, row['occurrences'], 'Entity')
        if confidence != 'high' or status == 'unreviewed':
            priorities.append(row['id'])
    excluded = document.get('exclusions', [])
    require(isinstance(excluded, list), 'exclusions must be an array')
    for row in excluded:
        fields(row, {'label', 'reason', 'occurrences'}, set(), 'exclusion')
        string(row['label'], 'exclusion label')
        string(row['reason'], 'exclusion reason', limit=40)
        validate_occurrences(bundle, row['occurrences'], 'Exclusion')
    return {'entities': len(rows), 'matched': len(matched), 'reviewPriority': priorities,
            'importanceCounts': {level: sum(r.get('importance') == level for r in rows) for level in IMPORTANCE},
            'unassessedImportance': 0 if rated else len(rows),
            'exclusions': len(excluded), 'semanticReview': 'not established by validation'}


def build(bundle, proposal):
    fields(proposal, {'entities'}, {'exclusions', 'evidenceNotes'}, 'proposal')
    require(note_hashes(bundle, note_refs(proposal)) == bundle['entityInputs']['vaultNotes'],
            'Vault evidence changed or differs from inspection; inspect every consulted note')
    document = {'schemaVersion': SCHEMA_VERSION, 'sessionYaml': bundle['sessionYaml'],
                'inputs': bundle['entityInputs'], **proposal}
    validate(bundle, document)
    return document


def save(bundle, proposal, expected=None):
    document = build(bundle, proposal)
    with scenes.lock(bundle['root']):
        scenes.check_inputs(bundle)
        require(note_hashes(bundle, note_refs(document)) == document['inputs']['vaultNotes'],
                'Vault notes changed during entity checking')
        path = scenes.safe(bundle['root'], bundle['entityPath'].relative_to(bundle['root']))
        protected = {scenes.safe(bundle['root'], p) for p in bundle['fingerprints']}
        protected.update((bundle['draft'], bundle['mapPath']))
        require(path not in protected, 'Entity output aliases an input')
        if path.exists():
            require(path.is_file() and path.stat().st_nlink == 1, 'Entity map must be regular, not a hard link')
            require(expected is not None and scenes.draft.sha(path.read_bytes()) == expected,
                    'Existing entity map requires its inspected --expect-sha256')
        else:
            require(expected is None, 'Expected entity map is missing')
        scenes.atomic(bundle['root'], path.relative_to(bundle['root']), scenes.encoded(document))
    return document


def read_map(bundle):
    doc = json.loads(bundle['entityPath'].read_text(encoding='utf-8'))
    validate(bundle, doc)
    return doc


def priority(row):
    return (row['review']['confidence'] == 'high', row['review']['status'] != 'unreviewed', row['label'].casefold())


def preview(bundle, document, entity_id=None, kind=None, importance=None):
    result = validate(bundle, document)
    rows = sorted(document['entities'], key=priority)
    if entity_id:
        rows = [r for r in rows if r['id'] == entity_id]
        require(rows, f'Unknown entity: {entity_id}')
    if kind is not None:
        require(kind in KINDS, 'Unknown entity kind filter')
        rows = [r for r in rows if r['kind'] == kind]
    if importance is not None:
        require(importance in IMPORTANCE, 'Unknown importance filter')
        rows = [r for r in rows if r.get('importance') == importance]
    cell = scenes.cell
    out = ['# Session entity check', '',
           f"{result['entities']} entities; {result['matched']} vault matches; "
           f"{len(result['reviewPriority'])} review priorities. Structural validation does not establish semantic review.", '']
    out.extend(['Session importance: ' + ', '.join(f'{result["importanceCounts"][level]} {level}' for level in IMPORTANCE) + '.', ''])
    if result['unassessedImportance']:
        out.extend(['Legacy v3 map: session importance has not been assessed. Reassess before importance-guided extraction; no tiers are inferred.', ''])
    if kind is not None:
        out.extend([f'Showing {len(rows)} {kind} entities; counts above describe the full map.', ''])
    if importance is not None:
        out.extend([f'Showing {len(rows)} {importance} entities; counts above describe the full map.', ''])
    out.extend(['| ID | Entity | Kind | Importance in this session | Vault match | Confidence / review | Evidence |',
                '| --- | --- | --- | --- | --- | --- | --- |'])
    for row in rows:
        note = row.get('note')
        match = f"[{cell(Path(note).stem)}](<{quote(str(bundle['vault'] / note), safe='/')}>)" if note else 'Unlinked'
        if row.get('identifiedLater'):
            match += ' — identified later'
        refs = row['occurrences']
        evidence = ', '.join(scenes.source_link(bundle, r['source']) for r in refs)
        label = cell(row['label'])
        if row.get('examinedInMirrorOfPast'):
            label += ' — Mirror of the Past: examined'
        out.append('| ' + ' | '.join([cell(row['id']), label, row['kind'], row.get('importance', 'Not assessed'), match,
                   cell(row['review']['confidence'] + ' / ' + row['review']['status']),
                   evidence]) + ' |')
    candidates = [row for row in rows if row.get('candidates')]
    if candidates:
        out.extend(['', '## Unresolved candidates', ''])
    for row in candidates:
        links = ', '.join(f"[{cell(Path(p).stem)}](<{quote(str(bundle['vault']/p), safe='/')}>)" for p in row['candidates'])
        out.append(f"- **{cell(row['id'])} — {cell(row['label'])}**: {links}")
    if entity_id:
        for row in rows:
            for item in row['occurrences']:
                ref = item['source']
                out.extend(['', f"**Source** — {scenes.source_link(bundle, ref)}", '',
                            '````text', window(bundle, ref['startUid'], ref['endUid']).rstrip(), '````', ''])
    if not entity_id and kind is None and importance is None and document.get('exclusions'):
        out.extend(['', '## Excluded candidates', ''])
        for row in document['exclusions']:
            evidence = ', '.join(scenes.source_link(bundle, item['source']) for item in row['occurrences'])
            out.append(f"- **{cell(row['label'])}**: {cell(row['reason'])} — {evidence}")
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session-yaml', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    inspect = sub.add_parser('inspect')
    inspect.add_argument('--note', action='append', default=[])
    show = sub.add_parser('show')
    show.add_argument('--start-uid', required=True)
    show.add_argument('--end-uid', required=True)
    view = sub.add_parser('preview')
    selection = view.add_mutually_exclusive_group()
    selection.add_argument('--entity')
    selection.add_argument('--kind', choices=sorted(KINDS))
    view.add_argument('--importance', choices=IMPORTANCE)
    sub.add_parser('validate')
    writer = sub.add_parser('save')
    writer.add_argument('--proposal', required=True)
    writer.add_argument('--expect-input-digest', required=True)
    writer.add_argument('--expect-sha256')
    args = parser.parse_args()
    try:
        proposal = None
        notes = getattr(args, 'note', [])
        if args.command == 'save':
            proposal = json.load(sys.stdin) if args.proposal == '-' else json.loads(Path(args.proposal).read_text(encoding='utf-8'))
            notes = note_refs(proposal)
        bundle = load(args.session_yaml, notes=notes)
        if args.command == 'inspect':
            result = {'sessionYaml': bundle['sessionYaml'], 'inputDigest': bundle['entityInputDigest'],
                      'notes': bundle['entityInputs']['vaultNotes'], 'output': str(bundle['entityPath']),
                      'mapSha256': scenes.draft.sha(bundle['entityPath'].read_bytes()) if bundle['entityPath'].exists() else None}
        elif args.command == 'show':
            print(window(bundle, args.start_uid, args.end_uid), end='')
            return
        elif args.command == 'save':
            require(args.expect_input_digest == bundle['entityInputDigest'], 'Inputs changed since inspect')
            result = validate(bundle, save(bundle, proposal, args.expect_sha256))
        else:
            document = read_map(bundle)
            if args.command == 'preview':
                print(preview(bundle, document, args.entity, args.kind, args.importance), end='')
                return
            result = validate(bundle, document)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

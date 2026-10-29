#!/usr/bin/env python3
"""Check/save agent-authored entity maps using the existing session and scene readers."""
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
CONFIDENCE = {'high', 'medium', 'low'}
STATUS = {'unreviewed', 'automatedReviewed', 'humanReviewed'}


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
    bundle = scenes.load(session_yaml, vault_root)
    scene_bytes = bundle['mapPath'].read_bytes()
    scene_doc = json.loads(scene_bytes)
    scenes.validate(bundle, scene_doc)
    inputs = {'sessionInputs': bundle['inputs'], 'sceneMapSha256': scenes.draft.sha(scene_bytes),
              'vaultNotes': note_hashes(bundle, notes)}
    stem = bundle['manifest'].name.removesuffix('-session.yaml')
    bundle.update(sceneDocument=scene_doc, entityInputs=inputs,
                  entityPath=scenes.safe(bundle['root'], f'cleaned/{stem}-entity-map.json'))
    bundle['entityInputDigest'] = scenes.digest({'sessionYaml': bundle['sessionYaml'], 'inputs': inputs})
    return bundle


def owner(bundle, ref):
    start, end = scenes.source_bounds(bundle, ref, 'entity source')
    for row in [*bundle['sceneDocument']['scenes'], *bundle['sceneDocument']['contextBlocks']]:
        a, z = scenes.source_bounds(bundle, row['source'], 'scene/context source')
        if a <= start <= end <= z:
            return f"Scene {row['index']}" if 'index' in row else f"{row['kind']} {row['source']['startUid']}"
    raise scenes.MapError('Entity source crosses a scene/context boundary')


def text_array(value, label):
    require(isinstance(value, list), f'{label} must be an array')
    for item in value:
        string(item, label)
    require(len(value) == len(set(value)), f'{label} contains duplicates')


def validate(bundle, document):
    fields(document, {'schemaVersion', 'sessionYaml', 'inputs', 'entities'},
           {'exclusions', 'evidenceNotes'}, 'entity map')
    require(type(document['schemaVersion']) is int and document['schemaVersion'] == 1,
            'Unsupported entity-map version')
    require(document['sessionYaml'] == bundle['sessionYaml'], 'Different session YAML')
    expected = {'sessionInputs': bundle['inputs'],
                'sceneMapSha256': bundle['entityInputs']['sceneMapSha256'],
                'vaultNotes': note_hashes(bundle, note_refs(document))}
    require(document['inputs'] == expected, 'Entity inputs changed; recheck sources, scene map, and vault notes')
    text_array(document.get('evidenceNotes', []), 'evidenceNotes')
    rows = document['entities']
    require(isinstance(rows, list), 'entities must be an array')
    ids, matched, priorities = set(), set(), []
    for row in rows:
        fields(row, {'id', 'kind', 'label', 'occurrences', 'review'},
               {'note', 'names', 'candidates', 'reason'}, 'entity')
        string(row['id'], 'id')
        require(re.fullmatch(r'[a-z][a-z0-9_-]*', row['id']) and row['id'] not in ids,
                'Entity IDs must be unique stable lowercase identifiers')
        ids.add(row['id'])
        require(isinstance(row['kind'], str) and row['kind'] in KINDS, 'Unknown entity kind')
        string(row['label'], 'label')
        text_array(row.get('names', []), 'names')
        text_array(row.get('candidates', []), 'candidates')
        fields(row['review'], {'confidence', 'status'}, set(), 'review')
        confidence, status = row['review']['confidence'], row['review']['status']
        require(isinstance(confidence, str) and confidence in CONFIDENCE, 'Unknown confidence')
        require(isinstance(status, str) and status in STATUS, 'Unknown review status')
        if 'note' in row:
            string(row['note'], 'note', nullable=True)
        if row.get('note'):
            require(not row.get('candidates'), 'Resolve note OR retain candidates, not both')
            require(row['note'] not in matched, 'Multiple entities matched to the same note')
            matched.add(row['note'])
        if not row.get('note') or confidence != 'high':
            require('reason' in row, 'Unresolved or uncertain entities need a reason')
        if 'reason' in row:
            string(row['reason'], 'reason', limit=40)
        refs = row['occurrences']
        require(isinstance(refs, list) and refs, 'Entity needs occurrence evidence')
        last_end = -1
        for item in refs:
            fields(item, {'source'}, set(), 'occurrence')
            start, end = scenes.source_bounds(bundle, item['source'], 'occurrence source')
            require(start > last_end, 'Entity occurrences must be ordered and non-overlapping')
            last_end = end
            owner(bundle, item['source'])
        if confidence != 'high' or status == 'unreviewed':
            priorities.append(row['id'])
    excluded = document.get('exclusions', [])
    require(isinstance(excluded, list), 'exclusions must be an array')
    for row in excluded:
        fields(row, {'label', 'reason', 'source'}, set(), 'exclusion')
        string(row['label'], 'exclusion label')
        string(row['reason'], 'exclusion reason', limit=40)
        owner(bundle, row['source'])
    return {'entities': len(rows), 'matched': len(matched), 'reviewPriority': priorities,
            'exclusions': len(excluded), 'semanticReview': 'not established by validation'}


def build(bundle, proposal):
    fields(proposal, {'entities'}, {'exclusions', 'evidenceNotes'}, 'proposal')
    require(note_hashes(bundle, note_refs(proposal)) == bundle['entityInputs']['vaultNotes'],
            'Vault evidence changed or differs from inspection; inspect every consulted note')
    document = {'schemaVersion': 1, 'sessionYaml': bundle['sessionYaml'],
                'inputs': bundle['entityInputs'], **proposal}
    validate(bundle, document)
    return document


def save(bundle, proposal, expected=None):
    document = build(bundle, proposal)
    with scenes.lock(bundle['root']):
        scenes.check_inputs(bundle)
        require(scenes.draft.sha(bundle['mapPath'].read_bytes()) == document['inputs']['sceneMapSha256'],
                'Scene map changed during entity checking')
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


def preview(bundle, document, entity_id=None, kind=None):
    result = validate(bundle, document)
    rows = sorted(document['entities'], key=priority)
    if entity_id:
        rows = [r for r in rows if r['id'] == entity_id]
        require(rows, f'Unknown entity: {entity_id}')
    if kind is not None:
        require(kind in KINDS, 'Unknown entity kind filter')
        rows = [r for r in rows if r['kind'] == kind]
    cell = scenes.cell
    out = ['# Session entity check', '',
           f"{result['entities']} entities; {result['matched']} vault matches; "
           f"{len(result['reviewPriority'])} review priorities. Structural validation does not establish semantic review.", '']
    if kind is not None:
        out.extend([f'Showing {len(rows)} {kind} entities; counts above describe the full map.', ''])
    assessment = bundle['sceneDocument'].get('dateValidation', {})
    if assessment.get('result') in {'conflict', 'insufficientEvidence'}:
        out.extend([f"Existing scene-map date finding: **{assessment['result']}** — {cell(assessment['reason'])}", ''])
    out.extend(['| ID | Entity | Kind | Vault match | Confidence / review | Evidence |',
                '| --- | --- | --- | --- | --- | --- |'])
    for row in rows:
        note = row.get('note')
        match = f"[{cell(Path(note).stem)}](<{quote(str(bundle['vault'] / note), safe='/')}>)" if note else 'Unlinked'
        refs = row['occurrences']
        evidence = ', '.join(dict.fromkeys(owner(bundle, r['source']) for r in refs))
        first = refs[0]['source']
        out.append('| ' + ' | '.join([cell(row['id']), cell(row['label']), row['kind'], match,
                   cell(row['review']['confidence'] + ' / ' + row['review']['status']),
                   cell(evidence) + '; ' + scenes.source_link(bundle, first)]) + ' |')
    explained = [row for row in rows if row.get('reason') or row.get('candidates') or entity_id]
    if explained:
        out.extend(['', '## Identity questions and rationale', ''])
    for row in explained:
        out.append(f"- **{cell(row['id'])} — {cell(row['label'])}**: {cell(row.get('reason', 'Matched against source and vault note.'))}")
        if row.get('candidates'):
            out.append('  Candidates: ' + ', '.join(f"[{cell(Path(p).stem)}](<{quote(str(bundle['vault']/p), safe='/')}>)" for p in row['candidates']))
        if entity_id:
            for item in row['occurrences']:
                ref = item['source']
                out.extend(['', f"**{cell(owner(bundle, ref))}** — {scenes.source_link(bundle, ref)}", '',
                            '````text', scenes.window(bundle, ref['startUid'], ref['endUid'], 'polished').rstrip(), '````', ''])
    if not entity_id and kind is None and document.get('exclusions'):
        out.extend(['', '## Excluded candidates', ''])
        for row in document['exclusions']:
            out.append(f"- **{cell(row['label'])}**: {cell(row['reason'])} — {scenes.source_link(bundle, row['source'])}")
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
            proposal = json.load(sys.stdin) if args.proposal == '-' else json.loads(Path(args.proposal).read_text())
            notes = note_refs(proposal)
        bundle = load(args.session_yaml, notes=notes)
        if args.command == 'inspect':
            result = {'sessionYaml': bundle['sessionYaml'], 'inputDigest': bundle['entityInputDigest'],
                      'notes': bundle['entityInputs']['vaultNotes'], 'output': str(bundle['entityPath']),
                      'mapSha256': scenes.draft.sha(bundle['entityPath'].read_bytes()) if bundle['entityPath'].exists() else None}
        elif args.command == 'show':
            print(scenes.window(bundle, args.start_uid, args.end_uid, 'polished'), end='')
            return
        elif args.command == 'save':
            require(args.expect_input_digest == bundle['entityInputDigest'], 'Inputs changed since inspect')
            result = validate(bundle, save(bundle, proposal, args.expect_sha256))
        else:
            document = read_map(bundle)
            if args.command == 'preview':
                print(preview(bundle, document, args.entity, args.kind), end='')
                return
            result = validate(bundle, document)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Read-only structural/provenance validation of extracted interactions v1.

Selection, retained wording, cut meaning, and semantic review remain editorial.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'check-session-entities' / 'scripts'))
import entity_map
import jsonschema

scenes = entity_map.scenes
require = scenes.require
SCHEMA = Path(__file__).resolve().parents[1] / 'references/interactions.schema.json'


def validate_schema(document):
    schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
    jsonschema.Draft202012Validator(schema).validate(document)


def canonical_path(vault, relative):
    path = scenes.safe(vault, relative)
    require(path.relative_to(vault).as_posix() == relative,
            f'Expected canonical vault-relative path: {relative}')
    return path


def validate_spans(bundle, interaction, start, end):
    """Check mapped source accounting, without claiming text/cut verification."""
    text = '\n'.join(interaction['lines']) + '\n'
    header, blocks = scenes.draft.parse_polished(text)
    require(not header, f"{interaction['id']}: lines must begin with the original source comment")
    expected = [span for turn in bundle['turns'] for span in turn['spans']
                if start <= bundle['positions'][span[0]] <= end]
    actual = [span for block in blocks for span in block['spans']]
    require(actual == expected,
            f"{interaction['id']}: lines source spans differ from the original range")


def review_context(bundle, start, end):
    """Five nonblank physical text lines outside the complete source range.

    The shared source reader has already separated out UID/offset comments.
    Unknown dates do not affect this transcript-order context.
    """
    before, after = [], []
    for turn in bundle['turns']:
        first = bundle['positions'][turn['spans'][0][0]]
        last = bundle['positions'][turn['spans'][-1][0]]
        lines = [line for line in turn['body'].splitlines() if line.strip()]
        if last < start:
            before.extend(lines)
        elif first > end:
            after.extend(lines)
    return {'before': before[-5:], 'after': after[:5]}


def validate(document, vault_root=scenes.VAULT):
    validate_schema(document)
    vault = Path(vault_root).resolve()
    manifest = canonical_path(vault, document['sessionYaml'])
    bundle = entity_map.load(manifest, vault)
    require('narrativeUnits' not in bundle, 'Interactions v1 requires a polished transcript')
    # entity_map.load allows source-change inspection; read_map then rejects stale maps.
    mapped = entity_map.read_map(bundle)
    require(mapped['schemaVersion'] == 4, 'Interactions require a current v4 entity map')
    require(document['sessionYaml'] == bundle['sessionYaml'], 'Different session YAML')
    inputs = document['inputs']
    require(inputs['transcript']['sha256'] == bundle['sourceSha256'],
            'Polished transcript hash differs; review changed evidence before updating provenance')
    map_path = canonical_path(vault, inputs['entityMap']['path'])
    require(map_path == bundle['entityPath'], 'Entity map belongs to a different session')
    require(inputs['entityMap']['sha256'] == scenes.draft.sha(map_path.read_bytes()),
            'Entity map hash differs; review changed decisions before updating provenance')
    known = {row['id'] for row in mapped['entities']}
    ids, previous = set(), None
    for row in document['interactions']:
        require(row['id'] not in ids, f"Duplicate interaction ID: {row['id']}")
        ids.add(row['id'])
        participants = [item['id'] for item in row['entities']]
        require(len(participants) == len(set(participants)),
                f"{row['id']}: duplicate entity ID")
        require(set(participants) <= known,
                f"{row['id']}: unknown entity IDs: {sorted(set(participants) - known)}")
        source = scenes.source(row['source']['startUid'], row['source']['endUid'])
        bounds = scenes.source_bounds(bundle, source, row['id'])
        require(previous is None or previous <= bounds, 'Interactions are not in source order')
        previous = bounds
        validate_spans(bundle, row, *bounds)
        require(row['reviewContext'] == review_context(bundle, *bounds),
                f"{row['id']}: reviewContext differs from the five adjacent original text lines")
    return {
        'schemaVersion': 1,
        'interactions': len(ids),
        'semanticReview': 'not established by validation',
        'textAndCuts': 'require comparison with original speech',
        'coverage': 'partial collections are permitted; completeness is not established'
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('validate')
    check.add_argument('path', type=Path)
    check.add_argument('--vault-root', type=Path, default=scenes.VAULT)
    context = sub.add_parser('context', help='Print reviewContext for one source range without writing')
    context.add_argument('--session-yaml', required=True)
    context.add_argument('--start-uid', required=True)
    context.add_argument('--end-uid', required=True)
    context.add_argument('--vault-root', type=Path, default=scenes.VAULT)
    args = parser.parse_args()
    try:
        if args.command == 'context':
            vault = args.vault_root.resolve()
            bundle = entity_map.load(canonical_path(vault, args.session_yaml), vault)
            mapped = entity_map.read_map(bundle)
            require(mapped['schemaVersion'] == 4 and 'narrativeUnits' not in bundle,
                    'Review context requires a current v4 transcript entity map')
            bounds = scenes.source_bounds(bundle, scenes.source(args.start_uid, args.end_uid), 'source')
            result = review_context(bundle, *bounds)
        else:
            document = json.loads(args.path.read_text(encoding='utf-8'))
            result = validate(document, args.vault_root)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, jsonschema.ValidationError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

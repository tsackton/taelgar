#!/usr/bin/env python3
"""Read-only v7 session validation and projection from current scene/entity maps.

No interaction generation, review application, completion, or YAML registration.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity_map as entities
import jsonschema

scenes = entities.scenes
require = scenes.require
SCHEMA = Path(__file__).resolve().parents[1] / 'references/session.schema.json'


def validate_schema(document):
    schema = json.loads(SCHEMA.read_text())
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(document)


def unique(rows, key, label):
    result = {}
    for row in rows:
        require(row[key] not in result, f'Duplicate {label}: {row[key]}')
        result[row[key]] = row
    return result


def span(bundle, ref):
    a, z = scenes.source_bounds(bundle, ref, 'source')
    return set(range(a, z + 1))


def validate(document, vault_root=scenes.VAULT, require_coverage=False):
    validate_schema(document)
    vault = Path(vault_root).resolve()
    manifest = scenes.safe(vault, document['sessionYaml'])
    bundle = scenes.load(manifest, vault)
    require(bundle['sessionYaml'] == document['sessionYaml'], 'Noncanonical sessionYaml path')
    played = unique(document.get('scenes', []), 'index', 'scene index')
    contexts = unique(document.get('contextBlocks', []), 'index', 'context index')
    people = unique(document.get('entities', []), 'id', 'entity ID')
    records = unique(document.get('interactions', []), 'id', 'interaction ID')
    coverage = set()
    for collection, label in ((played, 'scenes'), (contexts, 'contexts')):
        require(list(collection) == sorted(collection), f'{label} indexes must be ordered')
        last = -1
        for row in collection.values():
            a, z = scenes.source_bounds(bundle, row['source'], label)
            require(a > last, f'{label} ranges overlap or are out of order')
            last = z
            own = set(range(a, z + 1))
            require(not coverage & own, 'Scene/context source ranges overlap')
            coverage.update(own)
            require(len(row.get('aiSummary', '').split()) <= 25, 'Scene/context summary exceeds 25 words')
            if row.get('location'):
                entities.note_path(bundle, row['location'])
            if row.get('dateStart') and row.get('dateEnd'):
                require(row['dateStart'] <= row['dateEnd'], 'Reversed scene date range')
    for note in document.get('locations', []):
        entities.note_path(bundle, note)
    for row in people.values():
        if row.get('note'):
            entities.note_path(bundle, row['note'])
    quotes = {}
    for row in records.values():
        require(row['entity'] in people, 'Broken entity reference')
        scene_ids, context_ids = row.get('scenes', []), row.get('contexts', [])
        require(scene_ids == sorted(scene_ids) and context_ids == sorted(context_ids),
                'Interaction anchor indexes must be ordered')
        require(all(i in played for i in scene_ids), 'Broken scene reference')
        require(all(i in contexts for i in context_ids), 'Broken context reference')
        allowed = set()
        for anchor in [*(played[i] for i in scene_ids), *(contexts[i] for i in context_ids)]:
            allowed.update(span(bundle, anchor['source']))
        # Context material can support mentions, never evidence of a played encounter.
        if row['interaction'] != 'mentioned':
            require(not context_ids, 'Non-play context can only anchor mentioned interactions')
        last = -1
        for passage in row.get('passages', []):
            own = span(bundle, passage['source'])
            require(own <= allowed, 'Passage outside interaction anchors')
            require(min(own) > last, 'Passages overlap or are out of order')
            last = max(own)
        for q in row.get('quotes', []):
            require(q['id'] not in quotes, 'Duplicate quote ID')
            own = span(bundle, q['source'])
            require(own <= allowed, 'Quote outside interaction anchors')
            a, z = min(own), max(own)
            turns = [t for g in bundle['groups']
                     if bundle['positions'][g['startUid']] >= a and bundle['positions'][g['endUid']] <= z
                     for t in g['turns']]
            original = ''.join(t['body'] for t in turns)
            require(q['text'] in original, 'Quote is not verbatim polished source text')
            quotes[q['id']] = row['entity']
    for row in people.values():
        require(all(quotes.get(q) == row['id'] for q in row.get('aiSuggestedFeaturedQuotes', [])),
                'Featured quote does not belong to entity')
    total = len(bundle['coverage'])
    if require_coverage:
        require(len(coverage) == total, 'Source coverage incomplete: account for all UIDs as scenes or context blocks')
    return {'schemaVersion': 7, 'entities': len(people), 'interactions': len(records),
            'scenes': len(played), 'contextBlocks': len(contexts), 'sourceUids': total,
            'accountedUids': len(coverage), 'unaccountedUids': total - len(coverage),
            'semanticReview': 'not established by validation', 'publicationReady': False}


def project(session_yaml, vault_root=scenes.VAULT):
    """Project identity decisions and source structure, without inventing interactions."""
    bundle = entities.load(session_yaml, vault_root)
    mapped = entities.read_map(bundle)
    scene_doc = scenes.read_map(bundle)
    doc = {'schemaVersion': 7, 'sessionYaml': bundle['sessionYaml'],
           'scenes': copy.deepcopy(scene_doc['scenes']),
           'contextBlocks': [dict(index=i, **copy.deepcopy(row)) for i, row in
                             enumerate(scene_doc['contextBlocks'], 1)],
           'entities': [{k: copy.deepcopy(row[k]) for k in ('id', 'kind', 'label', 'note', 'review') if k in row}
                        for row in mapped['entities']]}
    # Aggregate location review is separate; do not imply acceptance by deduplicating scene links.
    # Per-entity status is carried, but it cannot establish final output review/currentness.
    validate(doc, vault_root, require_coverage=True)
    return doc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    check = sub.add_parser('validate')
    check.add_argument('session_json')
    check.add_argument('--require-coverage', action='store_true')
    projection = sub.add_parser('project')
    projection.add_argument('--session-yaml', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'project':
            result = project(args.session_yaml)
        else:
            doc = json.loads(Path(args.session_json).read_text())
            result = validate(doc, require_coverage=args.require_coverage)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, jsonschema.ValidationError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

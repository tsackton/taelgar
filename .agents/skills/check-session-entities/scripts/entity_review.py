#!/usr/bin/env python3
"""JSON stdin/stdout entity review API for Obsidian and agent feedback handoff."""
import copy
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import entity_map as maps
import entity_review_store as store

scenes = maps.scenes
require = maps.require


def context(request, vault):
    relative = request.get('sessionYaml')
    maps.string(relative, 'sessionYaml')
    manifest = scenes.safe(vault, relative)
    bundle = maps.load(manifest, vault)
    # Recover before validation, using only bundle-owned paths.
    with scenes.lock(bundle['root']):
        store.current(bundle, scenes)
    raw = bundle['entityPath'].read_bytes()
    document = json.loads(raw)
    notes = sorted(set(maps.note_refs(document) + request.get('notes', request.get('token', {}).get('notes', []))))
    bundle = maps.load(manifest, vault, notes)
    maps.validate(bundle, document)
    return bundle, document


def token(bundle):
    path = store.review_path(bundle)
    return {'mapSha256': store.sha(bundle['entityPath'].read_bytes()),
            'reviewSha256': store.sha(path.read_bytes()) if path.exists() else None,
            'inputDigest': bundle['entityInputDigest'], 'notes': sorted(bundle['entityInputs']['vaultNotes'])}


def inspect(bundle, document, state):
    return {'token': token(bundle), 'document': document, 'review': state,
            'reviewPath': store.review_path(bundle).relative_to(bundle['vault']).as_posix(),
            'session': {'campaign': bundle['data'].get('campaign', ''), 'number': bundle['data'].get('sessionNumber')},
            'evidence': {r['id']: [{'source': o['source'], 'path': bundle['source'].relative_to(bundle['vault']).as_posix(),
                                   'line': bundle['lines'][o['source']['startUid']] - 1} for o in r['occurrences']]
                         for r in document['entities']}}


def dispatch(request, vault=scenes.VAULT):
    require(isinstance(request, dict), 'Expected a request object')
    bundle, document = context(request, Path(vault))
    command = request.get('command')
    with scenes.lock(bundle['root']):
        state = store.current(bundle, scenes)
        scenes.check_inputs(bundle)
        require(json.loads(bundle['entityPath'].read_bytes()) == document, 'Map changed; reload before continuing')
        if command == 'inspect':
            return inspect(bundle, document, state)
        if command == 'evidence':
            require(request.get('mapSha256') == token(bundle)['mapSha256'], 'Map changed; reload evidence')
            row = next((r for r in document['entities'] if r['id'] == request.get('entity')), None)
            require(row is not None, 'Unknown entity')
            return {'passages': [{'source': o['source'], 'text': maps.window(bundle, o['source']['startUid'], o['source']['endUid']),
                                  'path': bundle['source'].relative_to(bundle['vault']).as_posix(),
                                  'line': bundle['lines'][o['source']['startUid']] - 1} for o in row['occurrences']]}
        require(request.get('token') == token(bundle), 'Stale review; reload before saving')
        reason = request.get('reason', '')
        require(isinstance(reason, str) and len(reason) <= 10000, 'Invalid reason')
        key = request.get('entity')
        row = next((r for r in document['entities'] if r['id'] == key), None)
        before = copy.deepcopy(row)
        feedback = None
        if command == 'entityUpdate':
            require(row is not None, 'Unknown entity')
            action = request.get('action', 'edit')
            if action == 'remove':
                document['entities'].remove(row)
            else:
                require(action == 'edit', 'Unknown entity action')
                changes = request.get('changes', {})
                require(isinstance(changes, dict) and changes.keys() <= {'label', 'note', 'kind', 'importance', 'status'}, 'Unsupported entity changes')
                for name, value in changes.items():
                    if name == 'status':
                        require(value in maps.STATUS, 'Invalid review status')
                        row['review']['status'] = value
                    else:
                        row[name] = value
                if 'note' in changes:
                    row.pop('candidates', None)
                    if not row.get('note'):
                        row.pop('identifiedLater', None)
                if row.get('kind') != 'item':
                    row.pop('examinedInMirrorOfPast', None)
            # A new target must have been inspected, not merely named at save time.
            required = maps.note_refs(document)
            require(set(required) <= set(bundle['entityInputs']['vaultNotes']), 'Inspect new vault targets before saving')
            document['inputs']['vaultNotes'] = maps.note_hashes(bundle, required)
            maps.validate(bundle, document)
        elif command == 'entityFeedback':
            require(row is not None or key is None, 'Unknown entity')
            comment = request.get('comment', '').strip()
            require(comment and len(comment) <= 20000, 'Enter a comment for the agent')
            feedback = {'entity': key, 'comment': comment, 'status': 'open', 'record': before,
                        'author': 'human'}
            action = 'comment'
        elif command == 'resolveFeedback':
            item = next((f for f in state['feedback'] if f['id'] == request.get('feedbackId')), None)
            require(item is not None and item['status'] == 'open', 'Unknown or already resolved feedback')
            resolution = request.get('resolution', '').strip()
            require(resolution, 'A resolution explaining the outcome is required')
            item.update(status='resolved', resolution=resolution, resolvedBy='agent')
            action = 'resolveFeedback'
        else:
            raise ValueError('Unknown review command')
        require(maps.note_hashes(bundle, bundle['entityInputs']['vaultNotes']) == bundle['entityInputs']['vaultNotes'], 'Vault notes changed; reload')
        store.commit(bundle, scenes, before, document, state,
                     'agent' if command == 'resolveFeedback' else 'human', action, key, reason, feedback)
    # New input digest excludes notes no longer referenced after a link edit/removal.
    fresh = maps.load(bundle['manifest'], bundle['vault'], maps.note_refs(document))
    with scenes.lock(fresh['root']):
        return inspect(fresh, document, store.current(fresh, scenes))


def main():
    try:
        print(json.dumps(dispatch(json.load(sys.stdin)), ensure_ascii=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()

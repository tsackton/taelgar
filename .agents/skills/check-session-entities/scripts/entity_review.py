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
import entity_review_staging as staging

sources = maps.sources
# Compatibility alias for existing review clients.
scenes = sources
require = maps.require


def context(request, vault):
    relative = request.get('sessionYaml')
    maps.string(relative, 'sessionYaml')
    manifest = sources.safe(vault, relative)
    bundle = maps.load(manifest, vault)
    # Recover before validation, using only bundle-owned paths.
    with sources.lock(bundle['root']):
        store.current(bundle, sources)
    raw = bundle['entityPath'].read_bytes()
    document = json.loads(raw)
    notes = sorted(set(maps.note_refs(document) + request.get('notes', request.get('token', {}).get('notes', []))))
    bundle = maps.load(manifest, vault, notes)
    # Stale sources must reach the confirmation screen before strict validation.
    if not maps.source_changes(bundle, document):
        maps.validate(bundle, document)
    return bundle, document


def token(bundle):
    path = store.review_path(bundle)
    return {'mapSha256': store.sha(bundle['entityPath'].read_bytes()),
            'reviewSha256': store.sha(path.read_bytes()) if path.exists() else None,
            'inputDigest': bundle['entityInputDigest'], 'notes': bundle['inspectedNotes']}


def session_metadata(bundle):
    data = bundle['data']
    result = {'campaign': data.get('campaign', ''), 'number': data.get('sessionNumber'),
              'drStart': str(data.get('drStart') or ''), 'drEnd': str(data.get('drEnd') or ''),
              'realWorldDate': str(data.get('realWorldDate') or '')}
    if data.get('sourceType', 'transcript') == 'transcript':
        result['transcriptPath'] = bundle['source'].relative_to(bundle['vault']).as_posix()
    try:
        campaign = staging.campaign_config(bundle, sources)
        if campaign:
            if data.get('sessionNumber') is not None:
                number = str(data['sessionNumber'])
                whole, dot, fraction = number.partition('.')
                pattern = campaign.get('notePattern', '').replace('{session_padded}', whole.zfill(2) + dot + fraction).replace('{session}', number)
                if pattern and campaign.get('campaignRoot'):
                    relative = campaign['campaignRoot'].rstrip('/') + '/' + pattern
                    note = sources.safe(bundle['vault'], relative)
                    if note.is_file():
                        result['sessionNotePath'] = note.relative_to(bundle['vault']).as_posix()
    except (ValueError, OSError, TypeError, AttributeError) as exc:
        result['metadataWarning'] = 'Session-note link unavailable: ' + str(exc)
    try:
        result['stagingFolder'] = staging.folder(bundle, sources)
    except (ValueError, OSError, TypeError, AttributeError) as exc:
        result['stagingUnavailable'] = str(exc)
    return result


def exclusion_record(request, document):
    index = request.get('exclusionIndex')
    rows = document.get('exclusions', [])
    require(type(index) is int and 0 <= index < len(rows), 'Unknown excluded entity; reload the list')
    return rows[index]


def archived_record(state, exclusion):
    return next((r for r in state.get('excludedRecords', []) if r['exclusion'] == exclusion), None)


def inspect(bundle, document, state):
    def evidence(row):
        return [{'source': o['source'], 'path': bundle['source'].relative_to(bundle['vault']).as_posix(),
                 'line': bundle['lines'][o['source']['startUid']] - 1} for o in row['occurrences']]
    excluded = []
    for row in document.get('exclusions', []):
        archived = archived_record(state, row)
        excluded.append({'restorable': archived is not None,
                         'restoreNotes': maps.note_refs({'entities': [archived['record']]}) if archived else [],
                         'evidence': evidence(row)})
    return {'token': token(bundle), 'document': document, 'review': state,
            'reviewPath': store.review_path(bundle).relative_to(bundle['vault']).as_posix(),
            'session': session_metadata(bundle), 'exclusionDetails': excluded,
            'evidence': {r['id']: evidence(r) for r in document['entities']}}


def apply_entity_changes(row, changes):
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


def validate_edit(bundle, document):
    required = maps.note_refs(document)
    require(set(required) <= set(bundle['inspectedNotes']), 'Inspect new vault targets before saving')
    document['inputs'] = copy.deepcopy(bundle['entityInputs'])
    maps.validate(bundle, document)


def dispatch(request, vault=sources.VAULT):
    require(isinstance(request, dict), 'Expected a request object')
    bundle, document = context(request, Path(vault))
    command = request.get('command')
    with sources.lock(bundle['root']):
        state = store.current(bundle, sources)
        sources.check_inputs(bundle)
        require(json.loads(bundle['entityPath'].read_bytes()) == document, 'Map changed; reload before continuing')
        changes = maps.source_changes(bundle, document)
        if command == 'inspect' and changes:
            return {'confirmationRequired': True, 'sourceChanges': changes,
                    'token': token(bundle), 'session': session_metadata(bundle)}
        if command == 'confirmSourceChanges':
            require(request.get('token') == token(bundle), 'Inputs or review changed since confirmation; reload and confirm again')
            maps.acknowledge_sources(bundle, document, state)
            return inspect(bundle, document, store.current(bundle, sources))
        require(not changes, 'Transcript/session inputs changed; reload and confirm before continuing')
        if command == 'inspect':
            return inspect(bundle, document, state)
        if command == 'evidence':
            require(request.get('mapSha256') == token(bundle)['mapSha256'], 'Map changed; reload evidence')
            row = (exclusion_record(request, document) if 'exclusionIndex' in request else
                   next((r for r in document['entities'] if r['id'] == request.get('entity')), None))
            require(row is not None, 'Unknown entity')
            return {'passages': [{'source': o['source'], 'text': maps.window(bundle, o['source']['startUid'], o['source']['endUid']),
                                  'path': bundle['source'].relative_to(bundle['vault']).as_posix(),
                                  'line': bundle['lines'][o['source']['startUid']] - 1} for o in row['occurrences']]}
        require(request.get('token') == token(bundle), 'Stale review; reload before saving')
        document['inputs'] = copy.deepcopy(bundle['entityInputs'])
        reason = request.get('reason', '')
        require(isinstance(reason, str) and len(reason) <= 10000, 'Invalid reason')
        key = request.get('entity')
        row = next((r for r in document['entities'] if r['id'] == key), None)
        before = copy.deepcopy(row)
        feedback = None
        created_note = None
        if command in ('entityUpdate', 'exclusionInclude', 'createStagingNote'):
            if command == 'exclusionInclude':
                excluded = exclusion_record(request, document)
                archived = archived_record(state, excluded)
                before = copy.deepcopy(excluded)
                if archived:
                    row = copy.deepcopy(archived['record'])
                    require(not any(r['id'] == row['id'] for r in document['entities']), 'Restored entity ID already exists')
                    state['excludedRecords'].remove(archived)
                else:
                    used = {r['id'] for r in document['entities']}
                    used.update(r['record']['id'] for r in state.get('excludedRecords', []))
                    used.update(e.get('entity') for e in state['history'])
                    number = 1
                    while f'e{number:03}' in used:
                        number += 1
                    row = {'id': f'e{number:03}', 'label': excluded['label'],
                           'kind': request.get('kind'), 'importance': request.get('importance'),
                           'occurrences': copy.deepcopy(excluded['occurrences']),
                           'review': {'confidence': 'low', 'status': 'unreviewed'}}
                    require(row['kind'] in maps.KINDS and row['importance'] in maps.IMPORTANCE,
                            'Choose an entity type and role before including this candidate')
                key = row['id']
                row['review']['status'] = 'unreviewed'
                document['entities'].append(row)
                document['exclusions'].remove(excluded)
                action = 'include'
            require(row is not None, 'Unknown entity')
            action = ('include' if command == 'exclusionInclude' else
                      'createStagingNote' if command == 'createStagingNote' else request.get('action', 'edit'))
            if action == 'createStagingNote':
                require(not row.get('note'), 'This entity already has a linked vault note')
                changes = request.get('changes', {})
                require(isinstance(changes, dict) and changes.keys() <= {'label', 'kind', 'importance'},
                        'Unsupported staging-note changes')
                row.update(changes)
                row['review']['status'] = 'unreviewed'
                if row.get('kind') != 'item':
                    row.pop('examinedInMirrorOfPast', None)
                maps.validate(bundle, document)
                created_note = staging.create(bundle, request.get('name'), sources, request.get('noteIndex'))
                row['note'] = created_note
                row.pop('candidates', None)
                bundle['inspectedNotes'].append(created_note)
            elif action == 'exclude':
                maps.string(reason, 'exclusion reason', limit=40)
                apply_entity_changes(row, request.get('changes', {}))
                validate_edit(bundle, document)
                excluded = {'label': row['label'], 'reason': reason, 'occurrences': copy.deepcopy(row['occurrences'])}
                require(excluded not in document.get('exclusions', []), 'This exclusion already exists')
                state.setdefault('excludedRecords', []).append({'exclusion': copy.deepcopy(excluded), 'record': copy.deepcopy(row)})
                document.setdefault('exclusions', []).append(excluded)
                document['entities'].remove(row)
            elif action == 'remove':
                document['entities'].remove(row)
            elif action != 'include':
                require(action == 'edit', 'Unknown entity action')
                apply_entity_changes(row, request.get('changes', {}))
            try:
                # A new target must have been inspected, not merely named at save time.
                validate_edit(bundle, document)
            except (ValueError, OSError) as exc:
                if created_note:
                    raise ValueError(f'Created empty note {created_note}, but validation did not finish: {exc}. The note has been preserved.') from exc
                raise
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
        try:
            sources.check_inputs(bundle)
            store.commit(bundle, sources, before, document, state,
                         'agent' if command == 'resolveFeedback' else 'human', action, key, reason, feedback)
        except (ValueError, OSError) as exc:
            if created_note:
                raise ValueError(f'Created empty note {created_note}, but linking did not finish: {exc}. Reload to recover; the note has been preserved.') from exc
            raise
    # New input digest excludes notes no longer referenced after a link edit/removal.
    fresh = maps.load(bundle['manifest'], bundle['vault'], maps.note_refs(document))
    with sources.lock(fresh['root']):
        return inspect(fresh, document, store.current(fresh, sources))


def main():
    try:
        print(json.dumps(dispatch(json.load(sys.stdin)), ensure_ascii=False))
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()

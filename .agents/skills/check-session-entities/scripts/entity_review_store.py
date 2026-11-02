"""Recoverable map + feedback writes. Caller holds the shared session lock."""
import copy
import json
from datetime import datetime, timezone


def review_path(bundle):
    return bundle['entityPath'].with_name(bundle['entityPath'].name.replace('-entity-map.json', '-entities-review.json'))


def sha(data):
    import hashlib
    return hashlib.sha256(data).hexdigest()


def read(bundle, scenes):
    path = scenes.safe(bundle['root'], review_path(bundle).relative_to(bundle['root']))
    if not path.exists():
        return {'schemaVersion': 1, 'purpose': 'session-entities-review', 'sessionYaml': bundle['sessionYaml'],
                'mapSha256': sha(bundle['entityPath'].read_bytes()), 'history': [], 'feedback': []}
    scenes.require(path.is_file() and path.stat().st_nlink == 1, 'Review must be a regular file')
    state = json.loads(path.read_bytes())
    scenes.require(state.get('schemaVersion') == 1 and state.get('purpose') == 'session-entities-review'
                   and state.get('sessionYaml') == bundle['sessionYaml']
                   and isinstance(state.get('history'), list) and isinstance(state.get('feedback'), list),
                   'Invalid entities review JSON')
    return state


def write(bundle, scenes, state):
    path = review_path(bundle)
    scenes.atomic(bundle['root'], path.relative_to(bundle['root']), scenes.encoded(state))


def recover(bundle, scenes):
    state = read(bundle, scenes)
    pending = state.get('transaction')
    if pending:
        current = sha(bundle['entityPath'].read_bytes())
        after = scenes.encoded(pending['document'])
        scenes.require(current in (pending['beforeSha256'], sha(after)),
                       'Interrupted entity review conflicts with current map; reconcile before continuing')
        if current != sha(after):
            scenes.atomic(bundle['root'], bundle['entityPath'].relative_to(bundle['root']), after)
        del state['transaction']
        write(bundle, scenes, state)
    return state


def current(bundle, scenes):
    state = recover(bundle, scenes)
    scenes.require(state['mapSha256'] == sha(bundle['entityPath'].read_bytes()),
                   'Entity map changed outside the guarded workflow; reconcile review JSON before continuing')
    return state


def commit(bundle, scenes, before, document, state, actor, action, entity=None, reason='', feedback=None):
    state = copy.deepcopy(state)
    scenes.require(bundle['entityPath'].is_file() and bundle['entityPath'].stat().st_nlink == 1, 'Map must be a regular file')
    previous = sha(bundle['entityPath'].read_bytes())
    after = scenes.encoded(document)
    stamp = datetime.now(timezone.utc).isoformat()
    event = {'id': f'h{len(state["history"]) + 1:06}', 'at': stamp, 'actor': actor,
             'action': action, 'entity': entity, 'reason': reason,
             'beforeMapSha256': previous, 'afterMapSha256': sha(after),
             'before': before, 'after': copy.deepcopy(document if entity is None else
                 next((r for r in document['entities'] if r['id'] == entity), None))}
    state['history'].append(event)
    if feedback:
        feedback = copy.deepcopy(feedback)
        feedback.update(id=f'f{len(state["feedback"]) + 1:06}', at=stamp, mapSha256=previous)
        state['feedback'].append(feedback)
    state['mapSha256'] = sha(after)
    state['transaction'] = {'beforeSha256': previous, 'document': document}
    # Write-ahead record makes an interruption recoverable without losing feedback.
    write(bundle, scenes, state)
    scenes.atomic(bundle['root'], bundle['entityPath'].relative_to(bundle['root']), after)
    del state['transaction']
    write(bundle, scenes, state)
    return state


def protect_human(before, after, scenes):
    rows = {r['id']: r for r in after['entities']}
    old = {r['id']: r for r in before.get('entities', [])}
    changed_evidence = set()
    before_inputs, after_inputs = before.get('inputs', {}), after.get('inputs', {})
    source_changed = before_inputs.get('sessionInputs') != after_inputs.get('sessionInputs')
    for key, row in old.items():
        stale = source_changed
        if stale:
            changed_evidence.add(key)
        if row['review']['status'] == 'humanReviewed':
            expected = copy.deepcopy(row)
            if stale:
                expected['review']['status'] = 'unreviewed'
            scenes.require(rows.get(key) == expected,
                           f'Preserve human-reviewed entity {key}; changed evidence requires an unchanged record reset to unreviewed, otherwise reopen it in review before changing it')
    for key, row in rows.items():
        if row['review']['status'] == 'humanReviewed':
            scenes.require(old.get(key) == row and key not in changed_evidence,
                           'Agent regeneration cannot create human approval')

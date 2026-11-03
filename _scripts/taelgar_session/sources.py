"""Source bundles, whole-UID reading windows, evidence ranges, and input guards."""
from pathlib import Path
from urllib.parse import quote
from . import transcript as draft
from .storage import atomic, lock, safe, sha, open_no_follow
from .validation import (MapError, require, encoded, digest, object_fields, string,
                         validate_review, CONFIDENCE_RATINGS, REVIEW_STATUSES, cell)

VAULT = Path(__file__).resolve().parents[2]


def load(session_yaml, vault_root=VAULT, *, allow_unknown_dates=False, allow_source_changes=False):
    bundle = draft.load(session_yaml, allow_unknown_dates=allow_unknown_dates,
                        allow_source_changes=allow_source_changes)
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


def check_inputs(bundle):
    for relative, expected in bundle['fingerprints'].items():
        require(draft.sha(safe(bundle['root'], relative).read_bytes()) == expected,
                f'Input changed during mapping: {relative}')


def window(bundle, start_uid=None, end_uid=None):
    start_uid = start_uid or bundle['coverage'][0][0]
    end_uid = end_uid or bundle['coverage'][-1][0]
    start, end = source_bounds(bundle, source(start_uid, end_uid), 'reading window', boundary=False)
    selected = [g for g in bundle['groups']
                if bundle['positions'][g['endUid']] >= start and bundle['positions'][g['startUid']] <= end]
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
    return 'View: polished source\n\n' + ''.join(f'[{a}–{z}]\n{body}' for a, z, body in rendered)


def source_link(bundle, ref):
    label = f"{ref['startUid']}–{ref['endUid']}"
    line = bundle['lines'][ref['startUid']]
    return f"[{label}](<{quote(bundle['source'].as_posix(), safe='/')}:{line}>)"

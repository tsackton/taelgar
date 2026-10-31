#!/usr/bin/env python3
"""Deterministic, session-local work queue for the process-transcript skill.

The agent supplies semantic cleanup, entity inspection, punctuation and review.
This helper owns normalization, transactions, resumption and validation.
"""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import argparse
import copy
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import uuid
import yaml
import transcript_finalize as finalization
import transcript_review as review
from transcript_core import (VERSION, EDITORIAL_POLICY, WORK, STATE, LINE, MARKER, KINDS, CHECKS,
    PipelineError, require, encoded, sha, fingerprint, read_json, safe, lock,
    recover, commit, parse_units, render_units, validate_baseline, words,
    chunk_units, selected, validate_attributions, draft_turns, validate_turns,
    render_polished)


def resolve(vault, campaign, session):
    registry = read_json(vault / '_scripts/session_note_campaigns.json')['campaigns']
    key = re.sub(r'[^a-z0-9]', '', campaign.lower())
    aliases = {'dunmar': 'dunmar-frontier', 'dunmari': 'dunmar-frontier', 'chasm': 'into-the-chasm', 'lab lost': 'labyrinths-of-the-lost'}
    matches = []
    for slug, item in registry.items():
        names = [slug, item['name'], item['code'], item['sessionRoot'], *item.get('aliases', [])]
        if aliases.get(campaign.lower()) == slug or any(re.sub(r'[^a-z0-9]', '', n.lower()) == key for n in names):
            matches.append(item)
    require(len(matches) == 1, f'Campaign is unknown or ambiguous: {campaign}')
    item = matches[0]
    candidates = []
    for manifest in (vault / '_sessions' / item['sessionRoot']).glob('*/cleaned/*-session.yaml'):
        data = yaml.safe_load(manifest.read_text())
        if str(data.get('sessionNumber')) == str(session) or str(data.get('sessionNumber')).lstrip('0') == str(session).lstrip('0'):
            candidates.append(str(manifest.parent.parent))
    require(len(candidates) == 1, f'Expected one existing bundle for {campaign} {session}; found {len(candidates)}. If none exists, ask whether to use prepare-session-source to create one; if ambiguous, select the intended existing bundle.')
    return {'bundle': candidates[0], 'campaign': item['name'], 'sessionNumber': str(session)}


def one(root, pattern, explicit=None, required=True):
    if explicit:
        path = safe(root, explicit)
        require(path.is_file(), f'Missing input: {explicit}')
        return path
    matches = sorted(root.glob(pattern))
    require(len(matches) <= 1, f'Ambiguous {pattern}: supply an explicit path')
    require(matches or not required, f'Missing {pattern}')
    return matches[0] if matches else None


def local_reference(root, reference, directory):
    if not reference:
        return None
    p = Path(reference)
    # Copied bundles must never follow old absolute paths back into the vault.
    foreign = PureWindowsPath(reference) if PureWindowsPath(reference).is_absolute() else PurePosixPath(reference)
    if not p.is_absolute() and not foreign.is_absolute():
        candidate = safe(root, reference)
        if candidate.is_file():
            return candidate
    elif p.is_absolute() and p.is_relative_to(root):
        candidate = safe(root, str(p.relative_to(root)))
        if candidate.is_file():
            return candidate
    candidate = safe(root, directory + '/' + foreign.name)
    return candidate if candidate.is_file() else None


def original_path(root, metadata, source):
    if source:
        return safe(root, source)
    path = local_reference(root, metadata.get('sourceInputPath'), 'sources')
    if path:
        return path
    matches = [p for p in (root / 'sources').glob('*') if p.suffix.lower() in {'.vtt', '.srt'}]
    require(len(matches) == 1, 'Archived original is missing or ambiguous; select an existing bundle-local original with --source, or use prepare-session-source to repair intake. Do not manufacture an original from cleaned text.')
    return matches[0]


def initialize(root, args):
    if review.portable(root) and (review.active(root) or not safe(root, STATE).exists()):
        return review.status(root)
    if safe(root, STATE).exists():
        return status(root)
    completed = finalization.completion(root)
    if completed:
        return finalization.completed_status(root, *completed)
    manifest = one(root, 'cleaned/*-session.yaml', args.manifest, required=False)
    require(manifest is not None, 'Missing session YAML: process-transcript requires an existing prepared bundle. Ask whether to use prepare-session-source to create one.')
    prepared_path = one(root, 'cleaned/*-source-prepared.md', args.prepared, required=False)
    require(prepared_path is not None, 'Missing prepared UID transcript: use prepare-session-source to complete or repair the bundle before processing; do not rebuild from raw input here.')
    manifest_bytes = manifest.read_bytes()
    metadata = yaml.safe_load(manifest_bytes.decode('utf-8-sig'))
    require(isinstance(metadata, dict), 'Session YAML must be a mapping')
    require(metadata.get('sourceType', 'transcript') == 'transcript', 'This pipeline accepts transcripts, not narrative/raw-notes bundles')
    require(metadata.get('campaign') and metadata.get('sessionNumber') is not None, 'Existing session YAML needs campaign and sessionNumber; resolve intake metadata through prepare-session-source')
    original = original_path(root, metadata, args.source)
    require(original.is_file(), f'Missing archived source: {original}; use prepare-session-source to repair intake')
    archived = str(original.relative_to(root))
    require(archived.startswith('sources/'), 'Original input must already be archived under this bundle sources/ directory; use prepare-session-source for intake')
    original_bytes = original.read_bytes()
    cleaned_path = one(root, 'cleaned/*-source-cleaned.md', args.cleaned, required=False)
    stem = manifest.name.removesuffix('-session.yaml')
    require(bool(re.fullmatch(r'[\w.-]+', stem)), 'Bundle file prefix must be a filename-safe identifier')
    prepared_bytes = prepared_path.read_bytes()
    cleaned_bytes = cleaned_path.read_bytes() if cleaned_path else None
    prepared = parse_units(prepared_bytes.decode('utf-8-sig'))
    cleaned = parse_units(cleaned_bytes.decode('utf-8-sig')) if cleaned_path else copy.deepcopy(prepared)
    validate_baseline(prepared, cleaned)
    artifacts = {'original': archived, 'prepared': str(prepared_path.relative_to(root)),
                 'cleaned': str(cleaned_path.relative_to(root)) if cleaned_path else f'cleaned/{stem}-source-cleaned.md',
                 'polishedMarkdown': f'cleaned/{stem}-transcript.md', 'polishedJson': f'cleaned/{stem}-transcript.json',
                 'polishedHtml': f'cleaned/{stem}-transcript.html', 'review': f'cleaned/{stem}-transcript-review.md',
                 'entities': f'cleaned/{stem}-transcript-entities.json',
                 'sessionMetadata': str(manifest.relative_to(root))}
    for path in artifacts.values():
        safe(root, path)
    expected = {STATE: None, archived: sha(original_bytes),
                artifacts['prepared']: sha(prepared_bytes),
                artifacts['cleaned']: sha(cleaned_bytes) if cleaned_bytes is not None else None,
                artifacts['sessionMetadata']: sha(manifest_bytes)}
    inherited = []
    if cleaned_path:
        for p in (root / 'cleaned/cleanup-artifacts').glob('*-cleanup-decisions.json'):
            data = read_json(p)
            if data.get('transcriptSha256') != sha(cleaned_bytes):
                continue
            for u in cleaned:
                decision = data.get('decisions', {}).get(u['uid'], {})
                if decision.get('action') == 'skip':
                    for match in MARKER.finditer(u['text']):
                        inherited.append({'uid': u['uid'], 'span': match[1], 'textSha256': sha(u['text']), 'contextSha256': issue_context(cleaned, u['uid']),
                                          'reason': decision.get('reason', 'Previously recorded human acceptance'), 'source': str(p.relative_to(root))})
    state = {'schemaVersion': VERSION, 'contractVersion': VERSION, 'session': json.loads(encoded(metadata)), 'artifacts': artifacts,
             'originalSha256': sha(original_bytes), 'preparedSha256': sha(prepared_bytes),
             'chunks': chunk_units(cleaned, args.chunk_words), 'cleanReviews': {}, 'polish': {}, 'quality': {},
             'attributions': [], 'humanDecisions': {}, 'inheritedAcceptance': inherited, 'revision': 1}
    files = {artifacts['cleaned']: render_units(cleaned), STATE: encoded(state)}
    commit(root, files, 'Initialize transcript processing from existing prepared references', expected)
    return status(root)


def load(root):
    require(not review.active(root), 'Resume decisions from review Markdown with the review command; processing state is no longer authoritative')
    require(not safe(root, finalization.PLAN).exists(), 'Finalization was interrupted; run finalize or recover first')
    require(safe(root, STATE).is_file(), 'No active processing state. A finalized transcript keeps its references; use status to inspect it.')
    state = read_json(safe(root, STATE))
    require(state.get('schemaVersion') == VERSION and state.get('contractVersion') == VERSION, 'Unsupported pipeline contract; migrate explicitly')
    a = state['artifacts']
    require(sha(safe(root, a['original']).read_bytes()) == state['originalSha256'], 'Archived original changed')
    require(sha(safe(root, a['prepared']).read_bytes()) == state['preparedSha256'], 'Prepared baseline changed; preserve IDs and resolve source revision explicitly')
    units = parse_units(safe(root, a['cleaned']).read_text())
    validate_baseline(parse_units(safe(root, a['prepared']).read_text()), units)
    validate_attributions(units, state['attributions'])
    require([u['uid'] for c in state['chunks'] for u in selected(units, c)] == [u['uid'] for u in units], 'Work chunks have duplicate or missing UIDs')
    return state, units


def expected_inputs(state, units):
    return {STATE: sha(encoded(state)), state['artifacts']['cleaned']: sha(render_units(units)),
            state['artifacts']['prepared']: state['preparedSha256'], state['artifacts']['original']: state['originalSha256']}


def signature(state, units, chunk, stage):
    chosen = selected(units, chunk, context=2)
    ids = {u['uid'] for u in chosen}
    value = {'contractVersion': VERSION, 'editorialPolicy': EDITORIAL_POLICY, 'source': chosen,
             'attributions': sorted((a for a in state['attributions'] if a['uid'] in ids),
                                    key=lambda a: (a['uid'], a['start'], a['end']))}
    if stage == 'quality':
        value['polish'] = state['polish'].get(chunk['id'])
        position = state['chunks'].index(chunk)
        value['neighbors'] = {c['id']: state['polish'].get(c['id']) for i, c in enumerate(state['chunks']) if abs(i-position) == 1}
    return fingerprint(value)


def is_current(state, units, chunk, stage):
    table = {'clean': 'cleanReviews', 'polish': 'polish', 'quality': 'quality'}[stage]
    record = state[table].get(chunk['id'])
    return bool(record and record['sourceSha256'] == signature(state, units, chunk, stage))


def all_issues(state, units):
    issues = []
    for c in state['chunks']:
        if is_current(state, units, c, 'clean'):
            for item in state['cleanReviews'][c['id']]['issues']:
                item = copy.deepcopy(item)
                prior = next((x for x in state['inheritedAcceptance'] if all(x[k] == item[k] for k in ('uid', 'span', 'textSha256', 'contextSha256'))), None)
                decision = state['humanDecisions'].get(item['id'])
                item['disposition'] = 'accepted' if prior or decision else 'pending' if item['importance'] == 'material' else 'incidental'
                if prior or decision:
                    item['decision'] = decision or prior
                issues.append(item)
    return issues


def status(root):
    if safe(root, finalization.PLAN).exists():
        plan = read_json(safe(root, finalization.PLAN))
        return finalization.completed_status(root, plan['manifest'], plan['record'], finalizing=True)
    if review.portable(root) and (review.active(root) or not safe(root, STATE).exists()):
        return review.status(root)
    if not safe(root, STATE).exists():
        completed = finalization.completion(root)
        require(completed, 'This bundle has not been initialized')
        return finalization.completed_status(root, *completed)
    state, units = load(root)
    pending = {stage: [c['id'] for c in state['chunks'] if not is_current(state, units, c, stage)] for stage in ('clean', 'polish', 'quality')}
    issues = all_issues(state, units)
    material = sum(i['disposition'] == 'pending' for i in issues)
    done = not any(pending.values())
    substitutions = sum(len(t.get('substitutions', [])) for c in state['chunks'] if is_current(state, units, c, 'polish') for t in state['polish'][c['id']]['turns'])
    outcome = 'needs_work' if not done else 'needs_manual_review' if material else 'complete_with_uncertainty' if issues or substitutions else 'complete'
    output_matches = bool(state.get('exportSha256') == export_signature(state, units))
    if output_matches:
        disposable = {state['artifacts']['polishedHtml']}
        if done and not material:
            disposable.add(state['artifacts']['review'])
        output_matches = all((p in disposable and not safe(root, p).exists()) or
                             (safe(root, p).is_file() and sha(safe(root, p).read_bytes()) == h)
                             for p, h in state.get('outputHashes', {}).items())
    if done and not output_matches:
        outcome = 'ready_to_export' if not material else 'ready_to_export_with_review'
    return {'bundle': str(root), 'status': outcome, 'finalized': False, 'outputsCurrent': output_matches, 'units': len(units),
            'pending': pending, 'pendingMaterialIssues': material, 'pendingMaterialGroups': len({i.get('group', i['id']) for i in issues if i['disposition'] == 'pending'}), 'issues': len(issues), 'displaySubstitutions': substitutions, 'artifacts': state['artifacts']}


def legacy_candidates(root, units):
    """Read old excerpts as candidates, never as corrective authority or completion."""
    order = {u['uid']: i for i, u in enumerate(units)}
    candidates = []
    for path in sorted(safe(root, 'cleaned/beat-transcripts').glob('*-transcript.md')):
        marker = None
        for line in path.read_text().splitlines():
            match = re.fullmatch(r'%%\s*(u\d+)(?:-(u\d+))?\s*%%', line.strip())
            if match:
                marker = match.groups()
                continue
            if marker and line.strip():
                turn = re.fullmatch(r'(?:\*\*)?([^:]+):(?:\*\*)?\s*(.+)', line.strip())
                a, b = marker[0], marker[1] or marker[0]
                if turn and a in order and b in order and order[a] <= order[b]:
                    source = units[order[a]:order[b]+1]
                    candidate = {'speaker': turn[1], 'text': turn[2], 'sources': [{'uid': u['uid'], 'start': 0, 'end': len(u['text'])} for u in source]}
                    try:
                        validate_turns([candidate], source, [])
                        fidelity = 'words_and_speakers_match'
                    except PipelineError:
                        fidelity = 'requires_reconciliation'
                    candidates.append({'path': str(path.relative_to(root)), 'fidelity': fidelity, 'turn': candidate})
                marker = None
    return candidates


def make_work(root, stage, chunk_id=None):
    state, units = load(root)
    expected = expected_inputs(state, units)
    chunks = [c for c in state['chunks'] if c['id'] == chunk_id] if chunk_id else [c for c in state['chunks'] if not is_current(state, units, c, stage)]
    require(chunks, f'No pending {stage} work (or unknown chunk)')
    c = chunks[0]
    if stage in {'polish', 'quality'}:
        require(all(is_current(state, units, x, 'clean') for x in state['chunks']), 'Complete the session cleanup/recovery pass before polishing or quality review')
    if stage == 'quality':
        require(is_current(state, units, c, 'polish'), 'Polished chunk is missing/stale')
    source = selected(units, c)
    ids = {u['uid'] for u in source}
    payload = {'schemaVersion': VERSION, 'stage': stage, 'chunk': c, 'sourceSha256': signature(state, units, c, stage),
               'reviewScope': 'Recover likely speech using sounds, syntax and the full exchange. Apply reasonable contextual repairs automatically; exact wording uncertainty alone is not human work. Preserve spoken mistakes and meaningful table talk. Remove incidental flags. Only competing substantive readings need review, with proposed wording, a recommendation, and a concrete question. Polished-only garbled/cross-talk substitutions need exact source spans and a reason.',
               'session': state['session'], 'source': source, 'context': selected(units, c, 2),
               'attributions': [a for a in state['attributions'] if a['uid'] in ids],
               'responsePath': f'{WORK}/responses/{stage}-{c["id"]}.json'}
    if stage in {'clean', 'polish'}:
        payload['legacyCandidates'] = [x for x in legacy_candidates(root, units) if any(s['uid'] in ids for s in x['turn']['sources'])]
    if stage == 'clean':
        payload['previousReview'] = state['cleanReviews'].get(c['id'])
        payload['existingDecisions'] = {key: value for key, value in state['humanDecisions'].items() if value['issue']['uid'] in ids}
    if stage == 'polish':
        payload['draftTurns'] = draft_turns(source, state['attributions'])
    if stage == 'quality':
        payload['turns'] = state['polish'][c['id']]['turns']
        by_uid = {u['uid']: u for u in units}
        payload['recoveryCandidates'] = [dict(s, recognized=by_uid[s['uid']]['text'][s['start']:s['end']],
            context=review.context_units(units, review.context_range(units, s['uid'])))
            for t in payload['turns'] for s in t.get('substitutions', [])]
        payload['neighborTurns'] = {other['id']: state['polish'][other['id']]['turns'][-2:] if i < state['chunks'].index(c) else state['polish'][other['id']]['turns'][:2]
                                  for i, other in enumerate(state['chunks']) if abs(i-state['chunks'].index(c)) == 1 and is_current(state, units, other, 'polish')}
    path = f'{WORK}/jobs/{stage}-{c["id"]}.json'
    commit(root, {path: encoded(payload)}, f'Prepare {stage} work for {c["id"]}', expected)
    return {'job': str(root / path), 'response': str(root / payload['responsePath']), 'sourceSha256': payload['sourceSha256']}


def issue_context(units, uid, bounds=None):
    return fingerprint(review.context_units(units, review.context_range(units, uid, bounds)))


def validate_issues(raw, selected_units, all_units=None):
    by_uid = {u['uid']: u for u in selected_units}
    context = all_units or selected_units
    result, unique = [], set()
    for issue in raw:
        require(issue.get('uid') in by_uid and issue.get('kind') in KINDS, 'Invalid issue UID or kind')
        unit = by_uid[issue['uid']]
        require(issue.get('importance') == 'material' and bool(issue.get('reason', '').strip()), 'Only consequential review decisions belong in issues; remove incidental flags')
        for key in ('recommendation', 'question'):
            require(isinstance(issue.get(key), str) and bool(issue[key].strip()), f'Review issue needs {key}')
        require('proposal' not in issue, 'Supply a target and replacement, not a free-form full-UID proposal')
        require('replacement' in issue, 'Review issue needs replacement (null means retain unresolved)')
        proposal = review.target_text(unit, issue.get('target'), issue['replacement'])
        require(issue['replacement'] is None or issue['replacement'] != issue['target']['before'], 'Use null replacement for a retain-unresolved recommendation')
        alternatives = issue.get('alternatives', [])
        require(isinstance(alternatives, list) and all(isinstance(x, str) and x.strip() for x in alternatives), 'Review alternatives must be nonempty span replacements')
        bounds = review.context_range(context, issue['uid'], issue.get('contextRange'))
        item = dict(issue, span=issue['target']['before'], proposal=proposal,
                    alternatives=[review.target_text(unit, issue['target'], x) for x in alternatives],
                    contextRange=bounds, textSha256=sha(unit['text']), contextSha256=issue_context(context, issue['uid'], bounds))
        item['id'] = 'issue-' + fingerprint({k: item[k] for k in ('uid', 'kind', 'target', 'textSha256', 'contextSha256')})[:16]
        require(item['id'] not in unique, 'Duplicate issue')
        unique.add(item['id'])
        result.append(item)
    for unit in selected_units:
        for match in MARKER.finditer(unit['text']):
            require(any(i['uid'] == unit['uid'] and (match[1] in i['span'] or i['span'] in match[1]) for i in result), f"Unassessed uncertainty marker: {unit['uid']} {match[0]}")
    return result


def submit(root, response_path):
    state, units = load(root)
    expected = expected_inputs(state, units)
    response_path = safe(root, response_path)
    r = read_json(response_path)
    require(r.get('schemaVersion') == VERSION and r.get('stage') in {'clean', 'polish', 'quality'}, 'Invalid response schema/stage')
    stage = r['stage']
    chunks = [c for c in state['chunks'] if c['id'] == r.get('chunkId')]
    require(len(chunks) == 1, 'Unknown chunk')
    c = chunks[0]
    require(r.get('sourceSha256') == signature(state, units, c, stage), 'Stale work response; regenerate this job against current inputs')
    source = selected(units, c)
    ids = {u['uid'] for u in source}
    files = {}
    if stage == 'clean':
        require(set(r.get('checks', [])) == CHECKS, 'Complete all entity/action checks and the second inspection pass')
        by_uid = {u['uid']: u for u in units}
        edited = set()
        for edit in r.get('edits', []):
            require(edit.get('uid') in ids and edit['uid'] not in edited, 'Edit is outside this chunk or duplicated')
            unit = by_uid[edit['uid']]
            require(edit.get('before') == unit['text'], 'Edit before-text differs from current source')
            require(isinstance(edit.get('after'), str) and edit['after'].strip() and '\n' not in edit['after'] and '\r' not in edit['after'], 'Invalid replacement line')
            require(edit.get('kind') in {'name', 'asr', 'punctuation', 'uncertainty'} and edit.get('reason') and edit.get('evidence'), 'Each correction needs kind, reason, and evidence')
            unit['text'] = edit['after']
            edited.add(unit['uid'])
        parse_units(render_units(units))
        # The submitted list replaces attribution overlays within the current chunk.
        require('attributions' in r or not any(a['uid'] in edited for a in state['attributions']), 'Changed wording has speaker overrides; explicitly recheck and resubmit their offsets')
        corrections = r.get('attributions', [a for a in state['attributions'] if a['uid'] in ids])
        require(all(a.get('uid') in ids for a in corrections), 'Attribution is outside this chunk')
        for a in corrections:
            a['textSha256'] = sha(by_uid[a['uid']]['text'])
        state['attributions'] = [a for a in state['attributions'] if a['uid'] not in ids] + corrections
        validate_attributions(units, state['attributions'])
        source = selected(units, c)
        issues = validate_issues(r.get('issues', []), source, units)
        mentions = r.get('mentions', [])
        for mention in mentions:
            require(mention.get('uid') in ids and mention.get('kind') in {'person', 'group', 'place', 'time', 'item'}, 'Invalid entity mention')
            require(mention.get('text') and mention['text'] in by_uid[mention['uid']]['text'], 'Entity mention must quote current source wording')
        state['cleanReviews'][c['id']] = {'sourceSha256': signature(state, units, c, 'clean'), 'checks': r['checks'], 'issues': issues, 'mentions': mentions}
        files[state['artifacts']['cleaned']] = render_units(units)
    elif stage == 'polish':
        require(all(is_current(state, units, x, 'clean') for x in state['chunks']), 'Cleanup/recovery work is incomplete or stale')
        validate_turns(r.get('turns'), source, state['attributions'])
        state['polish'][c['id']] = {'sourceSha256': signature(state, units, c, 'polish'), 'turns': r['turns']}
    else:
        require(is_current(state, units, c, 'polish'), 'Polished chunk is stale')
        require(r.get('verdict') == 'pass' and not r.get('findings'), 'Quality review requires rework; fix the cited source/polish and review again')
        require(set(r.get('checks', [])) == {'wording', 'punctuation', 'speaker_turns', 'uncertainty', 'boundary_continuity'}, 'Incomplete quality review')
        require(bool(r.get('note', '').strip()), 'Quality review needs a brief substantive assessment')
        state['quality'][c['id']] = {'sourceSha256': signature(state, units, c, 'quality'), 'note': r['note']}
    state['revision'] += 1
    files[WORK + '/history/' + uuid.uuid4().hex + '.json'] = encoded(r)
    files[STATE] = encoded(state)
    commit(root, files, f'Apply reviewed {stage} response for {c["id"]}', expected)
    return status(root)


def export_signature(state, units):
    return fingerprint({'editorialPolicy': EDITORIAL_POLICY, 'source': units, 'clean': state['cleanReviews'], 'attributions': state['attributions'], 'polish': state['polish'], 'quality': state['quality'], 'issues': all_issues(state, units)})


def export(root, replace_exports=False):
    state, units = load(root)
    expected = expected_inputs(state, units)
    require(all(is_current(state, units, c, 'clean') and is_current(state, units, c, 'polish') for c in state['chunks']), 'Finish cleanup and polishing before exporting the complete transcript')
    turns = []
    for c in state['chunks']:
        for t in state['polish'][c['id']]['turns']:
            turn = copy.deepcopy(t)
            join = turn.pop('joinPrevious', False)
            if join:
                require(turns and turns[-1]['speaker'] == turn['speaker'], 'Cannot join a chunk boundary across different speakers or at the start of the transcript')
                turns[-1]['sources'].extend(turn['sources'])
                turns[-1]['text'] = turns[-1]['text'].rstrip() + ' ' + turn['text'].lstrip()
                if turn.get('substitutions'):
                    turns[-1].setdefault('substitutions', []).extend(turn['substitutions'])
            else:
                turns.append(turn)
    validate_turns(turns, units, state['attributions'])
    outcome = status(root)
    issues = all_issues(state, units)
    label = ('needs_quality_review' if outcome['pending']['quality'] else 'needs_manual_review' if outcome['pendingMaterialIssues'] else 'complete_with_uncertainty' if issues or outcome['displaySubstitutions'] else 'complete')
    title = f"{state['session']['campaign']} — Session {state['session']['sessionNumber']}"
    a = state['artifacts']
    md, page = render_polished(turns, title, Path(a['cleaned']).name, label)
    review_artifacts = dict(a, sessionMetadata=a.get('sessionMetadata') or str(one(root, 'cleaned/*-session.yaml').relative_to(root)))
    review_md = review.exported(root, review_artifacts, issues, units, turns, title, not outcome['pending']['quality'], md)
    mentions = [m for c in state['chunks'] for m in state['cleanReviews'][c['id']]['mentions']]
    source_hash = sha(safe(root, a['cleaned']).read_bytes())
    payload = {'schemaVersion': VERSION, 'status': label, 'sourceTranscript': Path(a['cleaned']).name,
               'sourceSha256': source_hash, 'turns': turns, 'attributions': state['attributions'], 'issues': issues}
    files = {a['polishedMarkdown']: md, a['polishedHtml']: page, a['polishedJson']: encoded(payload),
             a['review']: review_md, a['entities']: encoded({'schemaVersion': VERSION, 'sourceSha256': source_hash,
                 'scope': 'Agent-reviewed transcript mentions, not canonical facts or an inferred chronology', 'mentions': mentions})}
    for path in files:
        existing = safe(root, path)
        if existing.exists() and not replace_exports:
            require(state.get('outputHashes', {}).get(path) == sha(existing.read_bytes()),
                    f'Existing export has unregistered/manual changes: {path}. Reconcile them before --replace-exports.')
    state['exportSha256'] = export_signature(state, units)
    state['outputHashes'] = {p: sha(data if isinstance(data, bytes) else data.encode()) for p, data in files.items()}
    files[STATE] = encoded(state)
    commit(root, files, 'Export complete transcript, provenance, entity references and review queue', expected)
    return status(root)


def accept(root, issue_id, reason):
    state, units = load(root)
    expected = expected_inputs(state, units)
    matches = [i for i in all_issues(state, units) if i['id'] == issue_id]
    require(len(matches) == 1 and bool(reason.strip()), 'Unknown/stale issue or missing actual human decision')
    state['humanDecisions'][issue_id] = {'action': 'accept_uncertainty', 'reason': reason, 'issue': matches[0]}
    commit(root, {STATE: encoded(state)}, 'Record explicit human acceptance of uncertainty', expected)
    return status(root)


def finalize(root):
    if safe(root, finalization.PLAN).exists():
        return finalization.finish(root)
    if review.portable(root) and (review.active(root) or not safe(root, STATE).exists()):
        return review.finalize(root)
    outcome = status(root)
    require(outcome['outputsCurrent'] and outcome['status'] in {'complete', 'complete_with_uncertainty'},
            'Finish current cleanup, polish, quality/manual review, and export before finalization')
    if outcome['finalized']:
        return outcome
    state, units = load(root)
    # Existing work queues predate the explicit metadata-path field.
    manifest = state['artifacts'].get('sessionMetadata')
    if not manifest:
        manifest = str(one(root, 'cleaned/*-session.yaml').relative_to(root))
    expected = expected_inputs(state, units)
    require(all(sha(safe(root, path).read_bytes()) == digest for path, digest in expected.items()),
            'Inputs changed before finalization')
    return finalization.begin(root, state, outcome, manifest, expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('resolve')
    default_vault = next((p for p in Path(__file__).resolve().parents if (p / '_scripts/session_note_campaigns.json').is_file()), Path.cwd())
    p.add_argument('--vault-root', type=Path, default=default_vault)
    p.add_argument('--campaign', required=True)
    p.add_argument('--session', required=True)
    for name in ('init', 'status', 'work', 'submit', 'export', 'accept', 'recover', 'finalize', 'review'):
        p = sub.add_parser(name)
        p.add_argument('--bundle', type=Path, required=True)
        if name == 'review':
            mode = p.add_mutually_exclusive_group()
            mode.add_argument('--prepare', nargs='+', metavar='UID')
            mode.add_argument('--apply', action='store_true')
            mode.add_argument('--finalize', dest='review_finalize', action='store_true')
        elif name == 'init':
            for opt in ('source', 'manifest', 'prepared', 'cleaned'):
                p.add_argument('--' + opt)
            p.add_argument('--chunk-words', type=int, default=1800)
        elif name == 'work':
            p.add_argument('--stage', choices=['clean', 'polish', 'quality'], required=True)
            p.add_argument('--chunk')
        elif name == 'submit':
            p.add_argument('--response', required=True, help='Bundle-relative response path')
        elif name == 'accept':
            p.add_argument('--issue', required=True)
            p.add_argument('--reason', required=True)
        elif name == 'export':
            p.add_argument('--replace-exports', action='store_true', help='Replace exports only after reconciling their manual changes')
    args = parser.parse_args()
    try:
        if args.command == 'resolve':
            result = resolve(args.vault_root.resolve(), args.campaign, args.session)
        else:
            root = args.bundle.expanduser().resolve()
            require(root.is_dir(), 'The prepared session bundle must already exist. Ask whether to use prepare-session-source to create one.')
            if args.command == 'status':
                result = status(root)
            elif args.command == 'review' and not (args.prepare or args.apply or args.review_finalize):
                result = review.status(root)
            else:
                with lock(root):
                    require(not safe(root, finalization.PLAN).exists() or args.command in {'finalize', 'recover'},
                            'Finalization was interrupted; run finalize or recover first')
                    recovered = recover(root)
                    if args.command == 'review':
                        if args.prepare: result = review.prepare(root, args.prepare)
                        elif args.apply: result = review.apply(root)
                        else: result = review.finalize(root)
                    elif args.command == 'init':
                        require(args.chunk_words > 0, 'Chunk size must be positive')
                        result = initialize(root, args)
                    elif args.command == 'work': result = make_work(root, args.stage, args.chunk)
                    elif args.command == 'submit': result = submit(root, args.response)
                    elif args.command == 'export': result = export(root, args.replace_exports)
                    elif args.command == 'accept': result = accept(root, args.issue, args.reason)
                    elif args.command == 'finalize': result = finalize(root)
                    else: result = finalization.finish(root) if safe(root, finalization.PLAN).exists() else {'recovered': recovered}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (PipelineError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())

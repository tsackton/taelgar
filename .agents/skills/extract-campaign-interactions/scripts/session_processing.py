"""Execution evidence, source coverage and completion of a YAML-owned session."""
import copy
import importlib.util
import json
import os
import re
from pathlib import Path

import jsonschema
import yaml
from session_bundle import OUTPUT_KEY, fingerprint
from session_model import SCHEMA, apply_review, check_correction, check_evidence, require, validate, render


def processing_digest(processing):
    # Review history/stage change on handoff; input and semantic evidence do not.
    return fingerprint({k: v for k, v in processing.items() if k not in {'reviews', 'stage'}})


def new_processing(data, catalog):
    findings = []
    for n, proposal in enumerate(catalog.bundle['proposals'], 1):
        finding = {'id': f'path-{n}', 'kind': 'pathIssue', 'severity': 'info', 'status': 'open',
                   'reason': proposal['reason'], 'evidence': [{'yamlField': proposal['field']}]}
        if proposal.get('proposed'):
            finding['proposedChange'] = {'field': proposal['field'], 'value': proposal['proposed']}
        findings.append(finding)
    return {'schemaVersion': 1, 'sessionYaml': data['sessionYaml'], 'inputs': catalog.inputs,
            'stage': 'prepared', 'fullTranscriptRead': False, 'excludedBlocks': [],
            'metadataFindings': findings, 'reviews': []}


def validate_processing(data, processing, vault, catalog=None, coverage=None, complete=False):
    schema = json.loads(SCHEMA.with_name('session-processing-data.schema.json').read_text())
    jsonschema.Draft202012Validator(schema).validate(processing)
    require(data.get('schemaVersion') == 6, 'Processing data requires session schema v6')
    if catalog is None:
        catalog = validate(data, vault)['catalog']
    require(processing['sessionYaml'] == data['sessionYaml'], 'Processing belongs to another session YAML')
    require(processing['inputs'] == catalog.inputs, 'Session YAML or transcript changed since preparation; prepare/review a new execution')
    if coverage is None:
        coverage = set().union(*(catalog.span(s['source']) for s in data.get('scenes', [])))
    excluded, ends = set(), {}
    for block in processing['excludedBlocks']:
        span = catalog.span(block['source'])
        sid, start, end = catalog.bounds(block['source'])
        require(start > ends.get(sid, -1), 'Excluded blocks overlap or are out of source order')
        ends[sid] = end
        require(not span & coverage, 'Excluded block overlaps a scene')
        require(block['reason'].strip(), 'Excluded block requires a reason')
        excluded.update(span)
    ids = set()
    for finding in processing['metadataFindings']:
        require(finding['id'] not in ids, 'Duplicate metadata finding ID')
        ids.add(finding['id'])
        check_evidence(finding, catalog, vault)
        if finding['kind'] == 'dateConflict':
            require(finding['severity'] == 'critical', 'A clear date contradiction must be critical')
            require(any(e.get('kind') == 'transcript' for e in finding['evidence']) and
                    any(e.get('yamlField') in {'drStart', 'drEnd', 'drStartTime', 'drEndTime'} for e in finding['evidence']),
                    'Date contradiction requires both transcript and YAML date evidence')
    open_critical = any(f['severity'] == 'critical' and f['status'] == 'open' for f in processing['metadataFindings'])
    total = sum(len(rows) for rows in catalog.rows.values())
    missing = total - len(coverage | excluded)
    require(len(processing['reviews']) <= 2, 'At most one targeted correction attempt per execution')
    for i, review in enumerate(processing['reviews']):
        require(review['report']['attempt'] == i, 'Review attempts are repeated or incomplete')
    if complete:
        require(not (open_critical and data.get('review', {}).get('confidence') == 'high'),
                'Open critical metadata finding cannot have high session confidence')
        require(processing['fullTranscriptRead'], 'No complete transcript-read attestation')
        require(missing == 0, 'Unexplained transcript coverage; add scenes or explicit excluded blocks with reasons')
        require(processing['reviews'], 'Completion requires a semantic review')
        latest = processing['reviews'][-1]
        require(latest['outputDigest'] == fingerprint(data), 'Candidate changed after semantic review')
        require(latest['report']['processingDigest'] == processing_digest(processing), 'Processing evidence changed after review')
        reviewed = {'automatedReviewed', 'humanReviewed'}
        for target in [data, *data.get('entities', [])]:
            require(target.get('review', {}).get('status') in reviewed, 'Critical record has not received semantic review')
        require(data.get('sceneReview', {}).get('status') in reviewed, 'Scene division and exclusions have not received semantic review')
    return {'excludedUtterances': len(excluded), 'unexplainedUtterances': missing,
            'reviewCurrent': bool(processing['reviews'] and
                                  processing['reviews'][-1]['outputDigest'] == fingerprint(data) and
                                  processing['reviews'][-1]['report']['processingDigest'] == processing_digest(processing)),
            'criticalMetadataFindings': sum(f['severity'] == 'critical' and f['status'] == 'open' for f in processing['metadataFindings'])}


def audit_reviews(processing, vault):
    """Replay retained candidates and evidence; a final hash alone is not a review."""
    prior = None
    for index, record in enumerate(processing['reviews']):
        snapshot = {**processing, **record['evidence'], 'reviews': [], 'stage': 'extracted'}
        candidate, report = record['candidate'], record['report']
        require(report['attempt'] == index, 'Review attempt sequence is incomplete or repeated')
        if prior is not None:
            check_correction(prior, candidate, report, vault, processing=snapshot)
        prior = apply_review(candidate, report, vault, record['stage'], processing=snapshot)
        require(fingerprint(prior) == record['outputDigest'], 'Saved review result differs from replay')
    return prior


def apply_processing_review(data, processing, report, vault, stage='automatedReviewed'):
    require(report.get('attempt') == len(processing['reviews']), 'Review attempt sequence is incomplete or repeated')
    validate(data, vault, processing=processing)
    # A changed exclusion or chronology record must be covered by fresh decisions.
    targets = {d['target'] for d in report.get('decisions', [])}
    require({'session', 'scenes'} <= targets, 'v6 review must assess YAML consistency and scene coverage/exclusions')
    if processing['reviews']:
        prior = audit_reviews(processing, vault)
        check_correction(prior, data, report, vault, processing=processing)
    result = apply_review(data, report, vault, stage, processing=processing)
    require(not (result.get('review', {}).get('confidence') == 'high' and
                 any(f['severity'] == 'critical' and f['status'] == 'open' for f in processing['metadataFindings'])),
            'Open critical metadata finding cannot have high session confidence')
    evidence = copy.deepcopy(processing)
    evidence['stage'] = 'reviewed'
    evidence['reviews'].append({'report': copy.deepcopy(report), 'stage': stage, 'outputDigest': fingerprint(result),
                               'candidate': copy.deepcopy(data),
                               'evidence': {k: copy.deepcopy(processing[k]) for k in ('fullTranscriptRead', 'excludedBlocks', 'metadataFindings')}})
    validate(result, vault, processing=evidence)
    return result, evidence


def shared_storage():
    # Reuse the transcript pipeline's bundle lock and atomic writes. Do not create
    # transcript-work state or resurrect its discarded processing artifacts.
    path = Path(__file__).resolve().parents[2] / 'process-transcript/scripts/transcript_core.py'
    spec = importlib.util.spec_from_file_location('_interaction_transcript_storage', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def complete(data, processing, vault, output):
    """Save reviewed derived files, then append relative pointers without YAML churn.

    Low-confidence records may complete with visible critical findings. Completion
    is execution status, never acceptance of all claims. Existing files are only
    reused if byte-identical; different accepted/human-edited data is protected.
    """
    checked = validate(data, vault, processing=processing)
    catalog = checked['catalog']
    validate_processing(data, processing, vault, catalog, complete=True)
    require(audit_reviews(processing, vault) == data, 'Completed session differs from replayed review chain')
    root, manifest = catalog.bundle['root'], catalog.bundle['manifest']
    output = Path(output).resolve()
    require(output.is_relative_to(root) and output != root, 'Completed extraction must live inside its session bundle')
    storage = shared_storage()
    with storage.lock(root):
        # Recheck under the shared bundle lock, including current source hashes.
        checked = validate(data, vault, processing=processing)
        validate_processing(data, processing, vault, checked['catalog'], complete=True)
        before = manifest.read_bytes()
        entry = {'sessionJson': os.path.relpath(output / 'session.json', manifest.parent),
                 'processingData': os.path.relpath(output / 'session-processing-data.json', manifest.parent)}
        metadata = yaml.safe_load(before)
        if OUTPUT_KEY in metadata:
            require(metadata[OUTPUT_KEY] == entry, 'YAML already points to another extraction; propose a replacement explicitly')
            after = before
        else:
            # No reserialization: preserve comments, quoting and all other fields.
            require(not re.search(rb'^\.\.\.\s*$', before, re.M), 'YAML has an explicit document end; propose pointer edit manually')
            after = before + (b'' if before.endswith(b'\n') else b'\n') + b'\n' + yaml.safe_dump({OUTPUT_KEY: entry}, sort_keys=False).encode()
        final_processing = copy.deepcopy(processing)
        final_processing['stage'] = 'completed'
        payloads = {
            output / 'session.json': (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode(),
            output / 'session-processing-data.json': (json.dumps(final_processing, ensure_ascii=False, indent=2) + '\n').encode(),
            output / 'review.md': render(data, vault, output / 'review.md', processing=final_processing).encode(),
        }
        for path, value in payloads.items():
            safe = storage.safe(root, str(path.relative_to(root)))
            require(not safe.exists() or safe.read_bytes() == value, 'Refusing to overwrite existing extraction or human-edited review')
        for path, value in payloads.items():
            storage.atomic(root, str(path.relative_to(root)), value)
        require(manifest.read_bytes() == before, 'Session YAML changed during completion')
        for source in checked['catalog'].bundle['sources'].values():
            require(storage.sha((Path(vault) / source['path']).read_bytes()) == source['sha256'],
                    'Transcript changed during completion')
        # The manifest is the last write; it can never advertise missing outputs.
        storage.atomic(root, str(manifest.relative_to(root)), after)
    return entry

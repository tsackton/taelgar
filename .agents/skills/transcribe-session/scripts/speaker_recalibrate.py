#!/usr/bin/env python3
"""Create recording-local calibration layers without discarding prior evidence."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from speaker_audit import validate_audit, validate_decisions
from speaker_model import load_embedding_metadata, validate_embedding_source
from speaker_review import (
    SpeakerReviewError, atomic_write_json, ensure_writable_outputs,
    load_json_object, load_numpy, normalize_identifier, resolve_input,
    sha256_file, utc_now, validate_attributions,
)
from workspace_paths import resolve_transcription_output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('review', type=Path)
    parser.add_argument('--attributions', type=Path, required=True)
    parser.add_argument('--embeddings', type=Path, help='Reuse a complete, provenanced cache.')
    parser.add_argument('--audit', type=Path, help='Import completed human listening decisions from this exact source review.')
    parser.add_argument('--audit-decisions', type=Path, help='Decision file for --audit; never imports hidden model labels.')
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--review-id-prefix', required=True)
    return parser


def import_audit_decisions(
    review: dict[str, Any], attributions: dict[str, Any],
    audit: dict[str, Any], decisions: dict[str, Any], provenance: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_audit(audit)
    validate_decisions(audit, decisions)
    if set(decisions['decisions']) != {item['id'] for item in audit['items']}:
        raise SpeakerReviewError('finish every blind audit item before importing human decisions')
    if audit['participants'] != review['participants']:
        raise SpeakerReviewError('audit participants differ from the source review')
    result, attrs = copy.deepcopy(review), copy.deepcopy(attributions)
    utterances = {u['id']: u for u in review['utterances']}
    for item in audit['items']:
        u = utterances.get(item['utteranceId'])
        if u is None or any(u.get(k) != item.get(k) for k in ('recordingId', 'start', 'end', 'text')):
            raise SpeakerReviewError('audit does not describe these exact source utterances')
        decision = decisions['decisions'][item['id']]
        # The attribution schema has no overlap identity. Keep reviewed cross-talk
        # explicitly Unknown, with its original listening decision retained.
        attrs['utteranceOverrides'][u['id']] = {
            'status': 'unknown' if decision['status'] == 'overlap' else decision['status'],
            'participantId': decision['participantId'], 'humanVerified': True,
            'provenance': 'blind-audit', 'auditItemId': item['id'],
            'auditDecision': copy.deepcopy(decision),
        }
    attrs['verification'] = {}
    attrs['updatedAt'] = utc_now()
    result['humanAuditEvidence'] = {
        **copy.deepcopy(provenance), 'importedDecisionCount': len(audit['items']),
        'overlapUtteranceIds': [item['utteranceId'] for item in audit['items']
                                if decisions['decisions'][item['id']]['status'] == 'overlap'],
        'use': 'Human listening decisions only; hidden model predictions are not imported.',
    }
    validate_attributions(result, attrs)
    return result, attrs


def automated_decision(label: dict[str, Any]) -> bool:
    """The review UI replaces model metadata when a human changes a label."""
    if label.get('humanVerified') is True:
        return False
    return (
        'modelMargin' in label or 'modelCosine' in label
        or label.get('humanVerified') is False
        or label.get('method') == 'legacy-word-time-alignment'
        or label.get('provenance') in {'scribe-id-fallback', 'qualified-scribe-id'}
    )


def recording_layer(
    review: dict[str, Any], attributions: dict[str, Any], recording_id: str,
    review_id: str, parent: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    recordings = [r for r in review['recordings'] if r['id'] == recording_id]
    if len(recordings) != 1:
        raise SpeakerReviewError('recording ids must be unique and present')
    result = copy.deepcopy(review)
    result.update(reviewId=review_id, createdAt=utc_now(), recordings=copy.deepcopy(recordings))
    result['utterances'] = [copy.deepcopy(u) for u in review['utterances'] if u['recordingId'] == recording_id]
    result['groups'] = [copy.deepcopy(g) for g in review['groups'] if g['recordingId'] == recording_id]
    ids = {u['id'] for u in result['utterances']}
    group_ids = {g['id'] for g in result['groups']}
    result['exceptions'] = copy.deepcopy(review.get('exceptions', {}))
    result['exceptions']['unclusteredUtteranceIds'] = [
        u for u in review.get('exceptions', {}).get('unclusteredUtteranceIds', []) if u in ids
    ]
    manual, predictions = {}, {}
    for uid, label in attributions['utteranceOverrides'].items():
        if uid in ids:
            (predictions if automated_decision(label) else manual)[uid] = copy.deepcopy(label)
    result['priorSpeakerEvidence'] = {
        **parent, 'predictions': predictions,
        'modelAttribution': copy.deepcopy(review.get('modelAttribution', {})),
        'verification': copy.deepcopy(attributions.get('verification', {})),
        'earlierEvidence': copy.deepcopy(review.get('priorSpeakerEvidence', {})),
        'use': 'Retain as comparison evidence and candidate references; not active identity assignments.',
    }
    result.pop('modelAttribution', None)
    result.pop('scribeFallback', None)
    result['parentReview'] = copy.deepcopy(parent)
    result['verification'] = {
        'samplesPerParticipant': review.get('verification', {}).get('samplesPerParticipant', 10)
    }
    result['calibrationPolicy'] = {
        'scope': 'recording', 'recordingId': recording_id,
        'audioSha256': recordings[0].get('audioSha256'),
        'externalReferenceRole': 'comparison',
        'requiresConfidencePolicy': True,
        'notes': 'Use clean local references. Test prior banks independently; do not pool microphones or chunks without transfer evidence.',
    }
    decisions = {
        'schemaVersion': 1, 'reviewId': review_id, 'updatedAt': utc_now() if manual else None,
        'groupLabels': {gid: copy.deepcopy(v) for gid, v in attributions['groupLabels'].items() if gid in group_ids},
        'utteranceOverrides': manual, 'verification': {},
        'parentAttributions': copy.deepcopy(parent),
    }
    validate_attributions(result, decisions)
    return result, decisions


def provenanced_cache(np: Any, path: Path, review: dict[str, Any]) -> tuple[Any, Any, dict[str, Any]]:
    metadata = load_embedding_metadata(np, path)
    if not metadata:
        raise SpeakerReviewError('cache reuse requires provenance metadata')
    source = resolve_input(Path(metadata.get('sourcePath', '')), 'embedding source review')
    validate_embedding_source(metadata, source_type='speaker-review', source_sha256=sha256_file(source), label='embedding cache')
    original = load_json_object(source, 'embedding source review')
    source_recordings = {r['id']: r for r in original['recordings']}
    for recording in review['recordings']:
        old = source_recordings.get(recording['id'])
        if old is None or any(old.get(k) != recording.get(k) for k in ('audioSha256', 'transcriptSha256')):
            raise SpeakerReviewError('embedding cache belongs to a different recording or transcript')
    source_utterances = {u['id']: u for u in original['utterances']}
    for u in review['utterances']:
        old = source_utterances.get(u['id'])
        if old is None or any(old.get(k) != u.get(k) for k in ('recordingId', 'start', 'end', 'text')):
            raise SpeakerReviewError('embedding cache does not describe these exact utterances')
    with np.load(path, allow_pickle=False) as cache:
        ids, vectors = cache['ids'].copy(), cache['embeddings'].copy()
    if vectors.ndim != 2 or len(ids) != len(vectors) or len(set(map(str, ids))) != len(ids):
        raise SpeakerReviewError('embedding cache dimensions or ids are invalid')
    if not set(map(str, ids)).issubset(source_utterances) or not np.isfinite(vectors).all():
        raise SpeakerReviewError('embedding cache contains invalid vectors or unknown ids')
    if metadata.get('completedCount') != len(ids) or metadata.get('plannedCount') != len(ids):
        raise SpeakerReviewError('embedding cache counts do not match its vectors')
    return ids, vectors, metadata


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        review_path = resolve_input(args.review, 'speaker review')
        attrs_path = resolve_input(args.attributions, 'speaker attributions')
        review = load_json_object(review_path, 'speaker review')
        attrs = load_json_object(attrs_path, 'speaker attributions')
        validate_attributions(review, attrs)
        output = resolve_transcription_output(args.output_dir, error_type=SpeakerReviewError, label='local-calibration output')
        prefix = normalize_identifier(args.review_id_prefix)
        parent = {'reviewPath': str(review_path), 'reviewSha256': sha256_file(review_path),
                  'attributionsPath': str(attrs_path), 'attributionsSha256': sha256_file(attrs_path)}
        if bool(args.audit) != bool(args.audit_decisions):
            raise SpeakerReviewError('--audit and --audit-decisions must be supplied together')
        audit_inputs = {}
        if args.audit:
            audit_path = resolve_input(args.audit, 'speaker audit')
            decisions_path = resolve_input(args.audit_decisions, 'speaker audit decisions')
            audit = load_json_object(audit_path, 'speaker audit')
            decisions = load_json_object(decisions_path, 'speaker audit decisions')
            validate_decisions(audit, decisions, audit_path=audit_path)
            for key, path in [('sourceReview', review_path), ('sourceAttributions', attrs_path)]:
                source = audit.get(key, {})
                if Path(source.get('path', '')).resolve() != path or source.get('sha256') != sha256_file(path):
                    raise SpeakerReviewError('audit source paths and hashes must match the supplied review and attributions')
            audit_inputs = {'auditPath': str(audit_path), 'auditSha256': sha256_file(audit_path),
                            'decisionsPath': str(decisions_path), 'decisionsSha256': sha256_file(decisions_path)}
            review, attrs = import_audit_decisions(review, attrs, audit, decisions, audit_inputs)
            parent['humanAuditInputs'] = audit_inputs
        np = ids = vectors = metadata = cache_path = None
        if args.embeddings:
            cache_path = resolve_input(args.embeddings, 'embedding cache')
            np = load_numpy()
            ids, vectors, metadata = provenanced_cache(np, cache_path, review)
        prepared, paths = [], []
        for recording in review['recordings']:
            rid = f"{prefix}-{normalize_identifier(recording['id'])}-local-calibration"
            layer, decisions = recording_layer(review, attrs, recording['id'], rid, parent)
            rp, ap = output / f'{rid}.speaker-review.json', output / f'{rid}.speaker-attributions.json'
            ep = output / f'{rid}.ecapa.npz' if cache_path else None
            paths.extend([rp, ap] + ([ep] if ep else []))
            prepared.append((layer, decisions, rp, ap, ep))
        report_path = output / f'{prefix}.local-calibration.json'
        paths.append(report_path)
        if len(set(paths)) != len(paths) or {review_path, attrs_path, cache_path}.intersection(paths):
            raise SpeakerReviewError('calibration must write distinct new output paths')
        ensure_writable_outputs(paths, force=False)
        # Preflight every layer before creating any output; original artifacts stay unchanged.
        output.mkdir(parents=True, exist_ok=True)
        results = []
        for layer, decisions, rp, ap, ep in prepared:
            atomic_write_json(rp, layer)
            atomic_write_json(ap, decisions)
            count = 0
            if ep:
                selected = {u['id'] for u in layer['utterances']}
                mask = np.array([str(uid) in selected for uid in ids], dtype=bool)
                count = int(mask.sum())
                updated = copy.deepcopy(metadata)
                updated.update(sourcePath=str(rp), sourceSha256=sha256_file(rp), createdAt=utc_now(), updatedAt=utc_now(), plannedCount=count, completedCount=count)
                updated['parentCache'] = {'path': str(cache_path), 'sha256': sha256_file(cache_path), 'sourceSha256': metadata['sourceSha256'], 'reuse': 'exact utterance ids, recording ids, text, and timings checked; vectors unchanged'}
                np.savez_compressed(ep, ids=ids[mask], embeddings=vectors[mask], metadata_json=np.array(json.dumps(updated, sort_keys=True)))
            results.append({'recordingId': layer['recordings'][0]['id'], 'reviewPath': str(rp), 'reviewSha256': sha256_file(rp),
                            'attributionsPath': str(ap), 'attributionsSha256': sha256_file(ap),
                            'embeddingPath': str(ep) if ep else None, 'embeddingSha256': sha256_file(ep) if ep else None,
                            'reusedEmbeddingCount': count, 'groupCount': len(layer['groups']),
                            'carriedHumanOverrideCount': len(decisions['utteranceOverrides']),
                            'retainedPriorPredictionCount': len(layer['priorSpeakerEvidence']['predictions'])})
        if sha256_file(review_path) != parent['reviewSha256'] or sha256_file(attrs_path) != parent['attributionsSha256']:
            raise SpeakerReviewError('source changed during calibration; inspect the new layers before use')
        if audit_inputs and (sha256_file(Path(audit_inputs['auditPath'])) != audit_inputs['auditSha256']
                            or sha256_file(Path(audit_inputs['decisionsPath'])) != audit_inputs['decisionsSha256']):
            raise SpeakerReviewError('audit changed during import; inspect the new layers before use')
        report = {'schemaVersion': 1, 'createdAt': utc_now(), 'parent': parent, 'layers': results, 'sourceFilesUnchanged': True}
        atomic_write_json(report_path, report)
        print(json.dumps(report, indent=2))
        return 0
    except (SpeakerReviewError, OSError, ValueError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

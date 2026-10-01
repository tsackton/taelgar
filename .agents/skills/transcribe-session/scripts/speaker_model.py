#!/usr/bin/env python3
"""Materialize speaker-model labels and export verified reference clips."""

from __future__ import annotations

import argparse
import json
import math
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Sequence

from media_tools import (
    MediaToolError,
    extract_audio_clip,
    prepare_clip_source,
    resolve_clip_backend,
)
from speaker_audit import build_profile_references, load_embedding_cache, validate_audit, validate_decisions
from speaker_review import (
    SpeakerReviewError,
    atomic_write_json,
    ensure_writable_outputs,
    load_json_object,
    load_numpy,
    normalize_identifier,
    resolve_input,
    sha256_file,
    utc_now,
    validate_attributions,
    validate_verification_sample_count,
)
from workspace_paths import resolve_transcription_output


DEFAULT_MODEL_NAME = "speechbrain/spkrec-ecapa-voxceleb"
DEFAULT_MINIMUM_SECONDS = 1.5
DEFAULT_MINIMUM_WORDS = 4
DEFAULT_REFERENCE_SAMPLES = 5
DEFAULT_SCRIBE_ID_ACCURACY = 0.8


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Apply an audited speaker-embedding model as a new attribution layer, "
            "then export confirmed verification clips as a local reference bank."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    apply = subparsers.add_parser(
        "apply", help="Create a model-assisted review and attribution layer."
    )
    apply.add_argument("review", type=Path)
    apply.add_argument("--attributions", type=Path, required=True)
    apply.add_argument("--embeddings", type=Path, required=True)
    apply.add_argument(
        "--reference-bank",
        type=Path,
        help="Verified reference-bank.json used instead of current-session group labels.",
    )
    apply.add_argument(
        "--reference-embeddings",
        type=Path,
        help="Embedding cache created from --reference-bank clips.",
    )
    apply.add_argument(
        "--compare-reference", action="store_true",
        help="Use local profiles for labels; record the prior bank only as independent comparison evidence.",
    )
    apply.add_argument("--reference-transfer-audit", type=Path,
                       help="Completed current-recording blind audit validating a bank transfer after poor local profiles.")
    apply.add_argument("--reference-transfer-decisions", type=Path,
                       help="Human decisions already imported into this review for --reference-transfer-audit.")
    apply.add_argument("--minimum-model-margin", type=float, help="Reject weaker matches as Unknown; choose from the local audit.")
    apply.add_argument("--minimum-model-cosine", type=float, help="Reject weaker matches as Unknown; cosine is not a probability.")
    apply.add_argument("--output-dir", type=Path, required=True)
    apply.add_argument("--review-id", required=True)
    apply.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    apply.add_argument(
        "--minimum-duration-seconds", type=float, default=DEFAULT_MINIMUM_SECONDS
    )
    apply.add_argument(
        "--minimum-word-count", type=int, default=DEFAULT_MINIMUM_WORDS
    )
    apply.add_argument(
        "--exclude-utterance",
        action="append",
        default=[],
        help="Preserve the current label for this utterance instead of applying the model.",
    )
    apply.add_argument(
        "--allow-unresolved-verification",
        action="store_true",
        help=(
            "Permit time-spread verification when short cues retain mixed or unknown "
            "labels. Rendering still requires an explicit --allow-unresolved choice."
        ),
    )
    apply.add_argument("--force", action="store_true")

    fallback = subparsers.add_parser(
        "apply-scribe-fallback",
        help=(
            "Assign short cues from Scribe IDs whose durable model labels meet "
            "a minimum agreement rate."
        ),
    )
    fallback.add_argument("review", type=Path)
    fallback.add_argument("--attributions", type=Path, required=True)
    fallback.add_argument("--output-dir", type=Path, required=True)
    fallback.add_argument("--review-id", required=True)
    fallback.add_argument(
        "--minimum-accuracy", type=float, default=DEFAULT_SCRIBE_ID_ACCURACY
    )
    fallback.add_argument("--minimum-support-cues", type=int, default=1,
                          help="Minimum substantial model cues supporting each Scribe-ID policy (default: 1).")
    fallback.add_argument("--check-human-agreement", action="store_true",
                          help="Also require current explicit/confirmed listening to support the same identity at the chosen agreement threshold.")
    fallback.add_argument("--force", action="store_true")

    export = subparsers.add_parser(
        "export-reference-bank",
        help="Extract a compact local bank from confirmed verification samples.",
    )
    export.add_argument("review", type=Path)
    export.add_argument("--attributions", type=Path, required=True)
    export.add_argument("--output-dir", type=Path, required=True)
    export.add_argument(
        "--samples-per-participant", type=int, default=DEFAULT_REFERENCE_SAMPLES
    )
    export.add_argument("--force", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "apply":
            return apply_model(args)
        if args.command == "apply-scribe-fallback":
            return apply_scribe_fallback(args)
        if args.command == "export-reference-bank":
            return export_reference_bank(args)
    except (SpeakerReviewError, MediaToolError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    raise AssertionError(f"unknown command {args.command}")


def apply_model(args: argparse.Namespace) -> int:
    if args.minimum_duration_seconds <= 0:
        raise SpeakerReviewError("--minimum-duration-seconds must be positive")
    if args.minimum_word_count < 1:
        raise SpeakerReviewError("--minimum-word-count must be positive")
    validate_confidence_policy(args.minimum_model_margin, args.minimum_model_cosine)
    review_path = resolve_input(args.review, "speaker review")
    attributions_path = resolve_input(args.attributions, "speaker attributions")
    embeddings_path = resolve_input(args.embeddings, "speaker embeddings")
    review = load_json_object(review_path, "speaker review")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)
    np = load_numpy()
    embedding_by_id, embedding_dimension = load_embedding_cache(np, embeddings_path)
    embedding_metadata = load_embedding_metadata(np, embeddings_path)
    resolved_model_name = args.model_name
    if embedding_metadata:
        validate_embedding_source(
            embedding_metadata,
            source_type="speaker-review",
            source_sha256=sha256_file(review_path),
            label="review embedding cache",
        )
        resolved_model_name = str(
            embedding_metadata.get("modelName") or resolved_model_name
        )

    if bool(args.reference_bank) != bool(args.reference_embeddings):
        raise SpeakerReviewError(
            "--reference-bank and --reference-embeddings must be supplied together"
        )
    if args.compare_reference and not args.reference_bank:
        raise SpeakerReviewError("--compare-reference requires a reference bank and its embeddings")
    external_references = None
    profile_metadata = None
    if args.reference_bank:
        reference_bank_path = resolve_input(args.reference_bank, "reference-bank manifest")
        reference_embeddings_path = resolve_input(
            args.reference_embeddings, "reference-bank embeddings"
        )
        reference_bank = load_json_object(reference_bank_path, "reference-bank manifest")
        reference_embedding_by_id, reference_dimension = load_embedding_cache(
            np, reference_embeddings_path
        )
        if reference_dimension != embedding_dimension:
            raise SpeakerReviewError(
                "review and reference-bank embedding dimensions do not match"
            )
        reference_embedding_metadata = load_embedding_metadata(
            np, reference_embeddings_path
        )
        if not reference_embedding_metadata:
            raise SpeakerReviewError(
                "reference-bank embedding cache lacks provenance metadata; recreate it "
                "with speaker_embeddings.py"
            )
        validate_embedding_source(
            reference_embedding_metadata,
            source_type="reference-bank",
            source_sha256=sha256_file(reference_bank_path),
            label="reference-bank embedding cache",
        )
        if (
            embedding_metadata
            and resolved_model_name
            != reference_embedding_metadata.get("modelName")
        ):
            raise SpeakerReviewError(
                "review and reference-bank caches use different embedding models"
            )
        external_references, profile_metadata = build_reference_bank_references(
            review=review,
            manifest=reference_bank,
            embedding_by_id=reference_embedding_by_id,
            manifest_path=reference_bank_path,
            embeddings_path=reference_embeddings_path,
        )

    transfer = None
    if bool(args.reference_transfer_audit) != bool(args.reference_transfer_decisions):
        raise SpeakerReviewError("reference transfer requires both the audit and its decisions")
    if args.reference_transfer_audit:
        if external_references is None or args.compare_reference:
            raise SpeakerReviewError("validated transfer requires a reference bank used for assignment")
        transfer = validate_reference_transfer(
            np=np, review=review, attributions=attributions, embedding_by_id=embedding_by_id,
            references=external_references, profile_metadata=profile_metadata,
            audit_path=resolve_input(args.reference_transfer_audit, "transfer audit"),
            decisions_path=resolve_input(args.reference_transfer_decisions, "transfer decisions"),
            minimum_margin=args.minimum_model_margin, minimum_cosine=args.minimum_model_cosine,
        )

    utterance_ids = {item["id"] for item in review.get("utterances", [])}
    excluded_ids = set(args.exclude_utterance)
    unknown_exclusions = sorted(excluded_ids - utterance_ids)
    if unknown_exclusions:
        raise SpeakerReviewError(
            "model exclusions name unknown utterances: " + ", ".join(unknown_exclusions)
        )

    review_id = normalize_identifier(args.review_id)
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="model-attribution output directory",
    )
    output_review_path = output_dir / f"{review_id}.speaker-review.json"
    output_attributions_path = output_dir / f"{review_id}.speaker-attributions.json"
    if output_review_path == review_path or output_attributions_path == attributions_path:
        raise SpeakerReviewError("model application must write a new review layer")
    ensure_writable_outputs(
        [output_review_path, output_attributions_path], force=args.force
    )

    review_payload, attribution_payload, summary = materialize_model_layer(
        np=np,
        review=review,
        attributions=attributions,
        review_id=review_id,
        review_path=review_path,
        attributions_path=attributions_path,
        embeddings_path=embeddings_path,
        embedding_dimension=embedding_dimension,
        embedding_by_id=embedding_by_id,
        model_name=resolved_model_name,
        minimum_duration_seconds=args.minimum_duration_seconds,
        minimum_word_count=args.minimum_word_count,
        excluded_ids=excluded_ids,
        allow_unresolved_verification=args.allow_unresolved_verification,
        external_references=external_references,
        profile_metadata=profile_metadata,
        compare_reference=args.compare_reference,
        minimum_model_margin=args.minimum_model_margin,
        minimum_model_cosine=args.minimum_model_cosine,
        validated_reference_transfer=transfer,
    )
    validate_attributions(review_payload, attribution_payload)
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(output_review_path, review_payload)
    atomic_write_json(output_attributions_path, attribution_payload)
    print(f"Wrote {output_review_path}")
    print(f"Wrote {output_attributions_path}")
    print(json.dumps(summary, indent=2))
    return 0


def validate_reference_transfer(
    *, np: Any, review: dict[str, Any], attributions: dict[str, Any],
    embedding_by_id: dict[str, Any], references: list[dict[str, Any]],
    profile_metadata: dict[str, Any], audit_path: Path, decisions_path: Path,
    minimum_margin: float | None, minimum_cosine: float | None,
) -> dict[str, Any]:
    """Re-score a verified bank on exact imported listening decisions; never use hidden labels."""
    validate_confidence_policy(minimum_margin, minimum_cosine)
    if minimum_margin is None or minimum_cosine is None:
        raise SpeakerReviewError("validated bank transfer requires both acceptance thresholds")
    audit = load_json_object(audit_path, "transfer audit")
    decisions = load_json_object(decisions_path, "transfer decisions")
    validate_audit(audit)
    validate_decisions(audit, decisions, audit_path=audit_path)
    if set(decisions["decisions"]) != {item["id"] for item in audit["items"]}:
        raise SpeakerReviewError("complete the entire transfer audit before applying bank labels")
    evidence = review.get("humanAuditEvidence", {})
    expected = {"auditPath": str(audit_path), "auditSha256": sha256_file(audit_path),
                "decisionsPath": str(decisions_path), "decisionsSha256": sha256_file(decisions_path)}
    if any(evidence.get(key) != value for key, value in expected.items()):
        raise SpeakerReviewError("transfer decisions must be imported into this exact review first")
    if audit["participants"] != review["participants"] or audit["recordings"] != review["recordings"]:
        raise SpeakerReviewError("transfer audit roster or recordings differ from this review")
    for key in ("sourceReview", "sourceAttributions"):
        source = audit[key]
        if sha256_file(resolve_input(Path(source["path"]), "transfer audit source")) != source["sha256"]:
            raise SpeakerReviewError("transfer audit source changed after listening")
    utterances = {u["id"]: u for u in review["utterances"]}
    participant_ids = [p["id"] for p in review["participants"]]
    rows, passing_people = [], set()
    named, correct, passing, errors = 0, 0, 0, 0
    for item in audit["items"]:
        uid = item["utteranceId"]
        u = utterances.get(uid)
        decision = decisions["decisions"][item["id"]]
        label = attributions.get("utteranceOverrides", {}).get(uid, {})
        if (u is None or any(u.get(k) != item.get(k) for k in ("recordingId", "start", "end", "text"))
                or uid not in embedding_by_id):
            raise SpeakerReviewError("transfer audit does not match the cached source utterances")
        if (label.get("humanVerified") is not True or label.get("auditDecision") != decision
                or label.get("status") != ("unknown" if decision["status"] == "overlap" else decision["status"])
                or label.get("participantId") != decision["participantId"]):
            raise SpeakerReviewError("preserve each imported human decision before validating transfer")
        score = score_participant(np=np, participant_ids=participant_ids, references=references,
                                  embedding=embedding_by_id[uid], excluded_group_id=None)
        if score is None:
            raise SpeakerReviewError("transfer bank lacks a profile for a participant")
        accepted = score[1] >= minimum_margin and score[2] >= minimum_cosine
        matches = decision["status"] == "assigned" and score[0] == decision["participantId"]
        if decision["status"] == "assigned":
            named += 1
            correct += int(matches)
            if accepted:
                passing += 1
                errors += int(not matches)
                if matches:
                    passing_people.add(decision["participantId"])
        rows.append({"auditItemId": item["id"], "utteranceId": uid, "humanDecision": decision,
                     "participantId": score[0], "margin": round(score[1], 6), "cosine": round(score[2], 6),
                     "passesPolicy": accepted, "matchesHumanIdentity": matches})
    if errors or passing_people != set(participant_ids):
        raise SpeakerReviewError("transfer policy must have no passing named errors and cover every voice in the listened sample")
    return {"method": "verified-bank-transfer-checked-against-imported-blind-listening",
            **expected, "referenceBank": profile_metadata,
            "confidencePolicy": {"minimumMargin": minimum_margin, "minimumCosine": minimum_cosine},
            "identifiedSampleCount": named, "bankMatchesIdentified": correct,
            "passingIdentifiedCount": passing, "passingIdentityErrors": errors,
            "passingParticipantIds": sorted(passing_people), "scoreRows": rows,
            "limits": "Selected current-recording audit and thresholds chosen from it; no whole-recording accuracy claim. Independent time-spread verification remains required. All human identities, Unknown and Overlap decisions win."}


def apply_scribe_fallback(args: argparse.Namespace) -> int:
    if not 0 < args.minimum_accuracy <= 1:
        raise SpeakerReviewError("--minimum-accuracy must be greater than 0 and at most 1")
    review_path = resolve_input(args.review, "speaker review")
    attributions_path = resolve_input(args.attributions, "speaker attributions")
    review = load_json_object(review_path, "speaker review")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)

    review_id = normalize_identifier(args.review_id)
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="Scribe-fallback output directory",
    )
    output_review_path = output_dir / f"{review_id}.speaker-review.json"
    output_attributions_path = output_dir / f"{review_id}.speaker-attributions.json"
    if output_review_path == review_path or output_attributions_path == attributions_path:
        raise SpeakerReviewError("Scribe fallback must write a new review layer")
    ensure_writable_outputs(
        [output_review_path, output_attributions_path], force=args.force
    )

    review_payload, attribution_payload, summary = materialize_scribe_fallback_layer(
        review=review,
        attributions=attributions,
        review_id=review_id,
        review_path=review_path,
        attributions_path=attributions_path,
        minimum_accuracy=args.minimum_accuracy,
        minimum_support_cues=args.minimum_support_cues,
        check_human_agreement=args.check_human_agreement,
    )
    validate_attributions(review_payload, attribution_payload)
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(output_review_path, review_payload)
    atomic_write_json(output_attributions_path, attribution_payload)
    print(f"Wrote {output_review_path}")
    print(f"Wrote {output_attributions_path}")
    print(json.dumps(summary, indent=2))
    return 0


def materialize_scribe_fallback_layer(
    *,
    review: dict[str, Any],
    attributions: dict[str, Any],
    review_id: str,
    review_path: Path,
    attributions_path: Path,
    minimum_accuracy: float,
    minimum_support_cues: int = 1,
    check_human_agreement: bool = False,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    if minimum_support_cues < 1:
        raise SpeakerReviewError("minimum Scribe-ID support must be at least one cue")
    participants = review.get("participants", [])
    participant_by_id = {item["id"]: item for item in participants}
    utterance_by_id = {item["id"]: item for item in review.get("utterances", [])}
    source_overrides = attributions.get("utteranceOverrides", {})
    model_ids = set(
        attributions.get("modelAttribution", {}).get(
            "modelOverrideUtteranceIds", []
        )
    )
    if not model_ids:
        raise SpeakerReviewError(
            "Scribe fallback requires a model-assisted attribution layer"
        )
    unknown_model_ids = sorted(model_ids - set(utterance_by_id))
    if unknown_model_ids:
        raise SpeakerReviewError(
            "model attribution names unknown utterances: "
            + ", ".join(unknown_model_ids)
        )

    counts_by_scribe: dict[str, dict[str, int]] = defaultdict(
        lambda: defaultdict(int)
    )
    seconds_by_scribe: dict[str, dict[str, float]] = defaultdict(
        lambda: defaultdict(float)
    )
    skipped_model_cues = 0
    for utterance_id in sorted(model_ids):
        utterance = utterance_by_id[utterance_id]
        label = source_overrides.get(utterance_id)
        if not label or label.get("status") != "assigned":
            raise SpeakerReviewError(
                f"model-attributed utterance lacks a current assignment: {utterance_id}"
            )
        scribe_ids = utterance.get("scribeSpeakerIds", [])
        if len(scribe_ids) != 1:
            skipped_model_cues += 1
            continue
        scribe_id = str(scribe_ids[0])
        participant_id = label["participantId"]
        counts_by_scribe[scribe_id][participant_id] += 1
        seconds_by_scribe[scribe_id][participant_id] += float(
            utterance.get("durationSeconds", 0.0)
        )

    listened_ids = set(review.get("modelAttribution", {}).get("manualOverrideUtteranceIds", []))
    listened_ids.update(uid for uid, label in source_overrides.items()
                        if label.get("humanVerified") is True)
    for participant_id, confirmation in attributions.get("verification", {}).items():
        if confirmation.get("status") == "confirmed":
            listened_ids.update(uid for uid in confirmation.get("sampleUtteranceIds", [])
                                if source_overrides.get(uid, {}).get("participantId") == participant_id)
    human_by_scribe: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for uid in listened_ids:
        u = utterance_by_id.get(uid, {})
        label = source_overrides.get(uid, {})
        ids = u.get("scribeSpeakerIds", [])
        if label.get("status") == "assigned" and len(ids) == 1:
            human_by_scribe[str(ids[0])][label["participantId"]] += 1
    mappings: dict[str, dict[str, Any]] = {}
    scribe_audit: list[dict[str, Any]] = []
    for scribe_id in sorted(counts_by_scribe):
        rows = sorted(
            counts_by_scribe[scribe_id].items(),
            key=lambda item: (-item[1], item[0]),
        )
        total = sum(count for _participant_id, count in rows)
        top_participant_id, top_count = rows[0]
        accuracy = top_count / total
        tied = len(rows) > 1 and rows[1][1] == top_count
        human_counts = human_by_scribe.get(scribe_id, {})
        human_total = sum(human_counts.values())
        human_matching = human_counts.get(top_participant_id, 0)
        human_agreement = human_matching / human_total if human_total else 0.0
        human_supported = human_total > 0 and human_agreement >= minimum_accuracy
        accepted = (accuracy >= minimum_accuracy and not tied
                    and total >= minimum_support_cues
                    and (not check_human_agreement or human_supported))
        detail = {
            "scribeSpeakerId": scribe_id,
            "participantId": top_participant_id,
            "gameRole": participant_by_id[top_participant_id]["gameRole"],
            "correctCueCount": top_count,
            "classifiedCueCount": total,
            "accuracy": round(accuracy, 6),
            "accepted": accepted,
            "minimumSupportCues": minimum_support_cues,
            "humanAgreementChecked": check_human_agreement,
            "humanIdentifiedCueCount": human_total,
            "humanMatchingCueCount": human_matching,
            "humanAgreement": round(human_agreement, 6),
            "humanByParticipant": dict(human_counts),
            "byParticipant": [
                {
                    "participantId": participant_id,
                    "gameRole": participant_by_id[participant_id]["gameRole"],
                    "cueCount": count,
                    "speechSeconds": round(
                        seconds_by_scribe[scribe_id][participant_id], 3
                    ),
                }
                for participant_id, count in rows
            ],
        }
        scribe_audit.append(detail)
        if accepted:
            mappings[scribe_id] = detail

    model_metadata = review.get("modelAttribution", {})
    minimum_duration_seconds = float(
        model_metadata.get("minimumDurationSeconds", DEFAULT_MINIMUM_SECONDS)
    )
    minimum_word_count = int(
        model_metadata.get("minimumWordCount", DEFAULT_MINIMUM_WORDS)
    )
    output_overrides = json.loads(json.dumps(source_overrides))
    fallback_ids: list[str] = []
    fallback_counts: dict[str, int] = defaultdict(int)
    fallback_seconds: dict[str, float] = defaultdict(float)
    unresolved_counts: dict[str, int] = defaultdict(int)
    unresolved_seconds: dict[str, float] = defaultdict(float)
    unresolved_by_scribe: dict[str, dict[str, float | int]] = defaultdict(
        lambda: {"cueCount": 0, "speechSeconds": 0.0}
    )

    for utterance in review.get("utterances", []):
        utterance_id = utterance["id"]
        if utterance_id in output_overrides:
            continue
        duration = float(utterance.get("durationSeconds", 0.0))
        word_count = int(utterance.get("wordCount", 0))
        is_short = (
            duration < minimum_duration_seconds
            or word_count < minimum_word_count
        )
        scribe_ids = utterance.get("scribeSpeakerIds", [])
        if is_short and len(scribe_ids) == 1 and str(scribe_ids[0]) in mappings:
            mapping = mappings[str(scribe_ids[0])]
            participant_id = str(mapping["participantId"])
            output_overrides[utterance_id] = {
                "status": "assigned",
                "participantId": participant_id,
                "provenance": "scribe-id-fallback",
                "scribeSpeakerId": str(scribe_ids[0]),
                "scribeIdAccuracy": mapping["accuracy"],
                "scribeIdSupportCueCount": mapping["classifiedCueCount"],
            }
            fallback_ids.append(utterance_id)
            fallback_counts[participant_id] += 1
            fallback_seconds[participant_id] += duration
            continue

        if not is_short:
            reason = "non-short-without-explicit-assignment"
        elif not scribe_ids:
            reason = "no-scribe-id"
        elif len(scribe_ids) > 1:
            reason = "multiple-scribe-ids"
        elif str(scribe_ids[0]) not in counts_by_scribe:
            reason = "scribe-id-without-model-evidence"
        else:
            reason = "scribe-id-below-accuracy-threshold"
        unresolved_counts[reason] += 1
        unresolved_seconds[reason] += duration
        if len(scribe_ids) == 1:
            item = unresolved_by_scribe[str(scribe_ids[0])]
            item["cueCount"] = int(item["cueCount"]) + 1
            item["speechSeconds"] = float(item["speechSeconds"]) + duration

    ignored_group_labels = attributions.get("groupLabels", {})
    summary: dict[str, Any] = {
        "minimumAccuracy": minimum_accuracy,
        "accuracyUnit": "model-assigned durable cue count per Scribe ID",
        "minimumSupportCues": minimum_support_cues,
        "humanAgreementChecked": check_human_agreement,
        "modelCueCount": len(model_ids),
        "modelCuesSkippedForAmbiguousScribeIds": skipped_model_cues,
        "acceptedScribeIdCount": len(mappings),
        "scribeIdAudit": scribe_audit,
        "shortCueFallbackCount": len(fallback_ids),
        "shortCueFallbackSpeechSeconds": round(sum(fallback_seconds.values()), 3),
        "fallbackByParticipant": [
            {
                "participantId": participant_id,
                "gameRole": participant_by_id[participant_id]["gameRole"],
                "cueCount": fallback_counts[participant_id],
                "speechSeconds": round(fallback_seconds[participant_id], 3),
            }
            for participant_id in sorted(fallback_counts)
        ],
        "unresolvedCueCount": sum(unresolved_counts.values()),
        "unresolvedSpeechSeconds": round(sum(unresolved_seconds.values()), 3),
        "unresolvedByReason": [
            {
                "reason": reason,
                "cueCount": unresolved_counts[reason],
                "speechSeconds": round(unresolved_seconds[reason], 3),
            }
            for reason in sorted(unresolved_counts)
        ],
        "unresolvedByScribeId": [
            {
                "scribeSpeakerId": scribe_id,
                "cueCount": int(item["cueCount"]),
                "speechSeconds": round(float(item["speechSeconds"]), 3),
            }
            for scribe_id, item in sorted(unresolved_by_scribe.items())
        ],
        "ignoredAcousticGroupLabelCount": len(ignored_group_labels),
        "ignoredMixedAcousticGroupCount": sum(
            1
            for label in ignored_group_labels.values()
            if label.get("status") == "mixed"
        ),
    }
    fallback_metadata = {
        "createdAt": utc_now(),
        "method": "verified-model-to-scribe-id-short-cue-fallback",
        "minimumAccuracy": minimum_accuracy,
        "minimumDurationSeconds": minimum_duration_seconds,
        "minimumWordCount": minimum_word_count,
        "sourceModelOverrideUtteranceIds": sorted(model_ids),
        "fallbackUtteranceIds": fallback_ids,
        "summary": summary,
    }

    review_payload = json.loads(json.dumps(review))
    review_payload.update(
        {
            "reviewId": review_id,
            "createdAt": utc_now(),
            "scribeFallback": fallback_metadata,
            "parentReview": {
                "reviewId": review.get("reviewId"),
                "reviewPath": str(review_path),
                "reviewSha256": sha256_file(review_path),
                "attributionsPath": str(attributions_path),
                "attributionsSha256": sha256_file(attributions_path),
            },
        }
    )
    attribution_payload = {
        "schemaVersion": 1,
        "reviewId": review_id,
        "updatedAt": None,
        "groupLabels": {},
        "utteranceOverrides": output_overrides,
        "verification": json.loads(json.dumps(attributions.get("verification", {}))),
        "parentAttributions": {
            "reviewId": review.get("reviewId"),
            "path": str(attributions_path),
            "sha256": sha256_file(attributions_path),
        },
        "modelAttribution": json.loads(
            json.dumps(attributions.get("modelAttribution", {}))
        ),
        "scribeFallback": {
            "minimumAccuracy": minimum_accuracy,
            "fallbackUtteranceIds": fallback_ids,
            "summary": summary,
        },
    }
    return review_payload, attribution_payload, summary


def materialize_model_layer(
    *,
    np: Any,
    review: dict[str, Any],
    attributions: dict[str, Any],
    review_id: str,
    review_path: Path,
    attributions_path: Path,
    embeddings_path: Path,
    embedding_dimension: int,
    embedding_by_id: dict[str, Any],
    model_name: str,
    minimum_duration_seconds: float,
    minimum_word_count: int,
    excluded_ids: set[str],
    allow_unresolved_verification: bool,
    external_references: list[dict[str, Any]] | None = None,
    profile_metadata: dict[str, Any] | None = None,
    compare_reference: bool = False,
    minimum_model_margin: float | None = None,
    minimum_model_cosine: float | None = None,
    validated_reference_transfer: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    validate_confidence_policy(minimum_model_margin, minimum_model_cosine)
    policy = review.get("calibrationPolicy", {})
    if validated_reference_transfer is not None:
        if (external_references is None or compare_reference
                or validated_reference_transfer.get("passingIdentityErrors") != 0
                or set(validated_reference_transfer.get("passingParticipantIds", [])) != {p["id"] for p in review["participants"]}
                or validated_reference_transfer.get("confidencePolicy") != {"minimumMargin": minimum_model_margin, "minimumCosine": minimum_model_cosine}
                or validated_reference_transfer.get("referenceBank") != profile_metadata):
            raise SpeakerReviewError("validated transfer evidence does not match this application")
    if (policy.get("externalReferenceRole") == "comparison" and external_references is not None
            and not compare_reference and validated_reference_transfer is None):
        raise SpeakerReviewError("recording-local calibration requires comparison-only banks or a checked --reference-transfer-audit")
    if policy.get("requiresConfidencePolicy") and (minimum_model_margin is None or minimum_model_cosine is None):
        raise SpeakerReviewError("recording-local calibration requires --minimum-model-margin and --minimum-model-cosine chosen from the local audit")
    if compare_reference and external_references is None:
        raise SpeakerReviewError("prior comparison requires external reference embeddings")
    participants = review.get("participants", [])
    participant_ids = [item["id"] for item in participants]
    group_by_id = {item["id"]: item for item in review.get("groups", [])}
    utterance_by_id = {item["id"]: item for item in review.get("utterances", [])}
    group_labels = attributions.get("groupLabels", {})
    source_overrides = attributions.get("utteranceOverrides", {})
    references = (
        external_references
        if external_references is not None and not compare_reference
        else build_profile_references(
            group_by_id, group_labels, utterance_by_id, embedding_by_id, source_overrides
        )
    )
    missing_profiles = set(participant_ids) - {
        item["participantId"] for item in references
    }
    if missing_profiles:
        raise SpeakerReviewError(
            "cannot apply model without reference embeddings for participants: "
            + ", ".join(sorted(missing_profiles))
        )

    output_overrides = json.loads(json.dumps(source_overrides))
    model_override_ids: list[str] = []
    predicted_counts: dict[str, int] = defaultdict(int)
    prior_comparison: dict[str, Any] = {}
    rejected_ids: list[str] = []
    summary: dict[str, Any] = {
        "utteranceCount": len(utterance_by_id),
        "eligibleUtteranceCount": 0,
        "modelOverrideCount": 0,
        "manualOverrideCountPreserved": len(source_overrides),
        "shortCueCountPreserved": 0,
        "explicitExclusionCountPreserved": 0,
        "missingEmbeddingCountPreserved": 0,
        "insufficientProfileCountPreserved": 0,
        "lowConfidenceUnknownCount": 0,
        "predictedByParticipant": {},
    }
    for utterance in review.get("utterances", []):
        utterance_id = utterance["id"]
        duration = float(utterance.get("durationSeconds", 0.0))
        word_count = int(utterance.get("wordCount", 0))
        if utterance_id in source_overrides:
            continue
        if duration < minimum_duration_seconds or word_count < minimum_word_count:
            summary["shortCueCountPreserved"] += 1
            continue
        summary["eligibleUtteranceCount"] += 1
        if utterance_id in excluded_ids:
            summary["explicitExclusionCountPreserved"] += 1
            continue
        embedding = embedding_by_id.get(utterance_id)
        if embedding is None:
            summary["missingEmbeddingCountPreserved"] += 1
            continue
        prediction = score_participant(
            np=np,
            participant_ids=participant_ids,
            references=references,
            embedding=embedding,
            excluded_group_id=(
                None if external_references is not None and not compare_reference else utterance.get("groupId")
            ),
        )
        if prediction is None:
            summary["insufficientProfileCountPreserved"] += 1
            continue
        participant_id, margin, cosine = prediction
        if compare_reference:
            prior = score_participant(np=np, participant_ids=participant_ids, references=external_references,
                                      embedding=embedding, excluded_group_id=None)
            if prior:
                prior_comparison[utterance_id] = {"participantId": prior[0], "margin": round(prior[1], 6),
                                                  "cosine": round(prior[2], 6), "localParticipantId": participant_id,
                                                  "agreesWithLocal": participant_id == prior[0], "usedForAssignment": False}
        if ((minimum_model_margin is not None and margin < minimum_model_margin)
                or (minimum_model_cosine is not None and cosine < minimum_model_cosine)):
            output_overrides[utterance_id] = {
                "status": "unknown", "participantId": None, "modelMargin": round(margin, 6),
                "modelCosine": round(cosine, 6), "provenance": "model-low-confidence", "humanVerified": False,
            }
            rejected_ids.append(utterance_id)
            summary["lowConfidenceUnknownCount"] += 1
            continue
        output_overrides[utterance_id] = {
            "status": "assigned",
            "participantId": participant_id,
            "modelMargin": round(float(margin), 6),
            "modelCosine": round(cosine, 6),
            "provenance": "model", "humanVerified": False,
        }
        model_override_ids.append(utterance_id)
        predicted_counts[participant_id] += 1

    summary["modelOverrideCount"] = len(model_override_ids)
    summary["predictedByParticipant"] = dict(sorted(predicted_counts.items()))
    model_metadata = {
        "createdAt": utc_now(),
        "method": (
            "reference-bank-nearest-profile"
            if external_references is not None and not compare_reference
            else "leave-current-group-out-nearest-profile"
        ),
        "modelName": model_name,
        "embeddingDimension": embedding_dimension,
        "sourceEmbeddingsPath": str(embeddings_path),
        "sourceEmbeddingsSha256": sha256_file(embeddings_path),
        "minimumDurationSeconds": minimum_duration_seconds,
        "minimumWordCount": minimum_word_count,
        "manualOverrideUtteranceIds": sorted(source_overrides),
        "modelOverrideUtteranceIds": model_override_ids,
        "preservedExcludedUtteranceIds": sorted(excluded_ids),
        "rejectedModelUtteranceIds": rejected_ids,
        "confidencePolicy": {"minimumMargin": minimum_model_margin, "minimumCosine": minimum_model_cosine},
        "summary": summary,
    }
    if validated_reference_transfer is not None:
        model_metadata["validatedReferenceTransfer"] = validated_reference_transfer
    if profile_metadata:
        model_metadata["comparisonReference" if compare_reference else "profileReference"] = profile_metadata
    if compare_reference:
        model_metadata["priorComparison"] = prior_comparison
        summary["priorComparisonCount"] = len(prior_comparison)
        summary["priorDisagreementCount"] = sum(not p["agreesWithLocal"] for p in prior_comparison.values())
    review_payload = json.loads(json.dumps(review))
    verification = json.loads(json.dumps(review.get("verification", {})))
    verification["allowUnresolved"] = bool(allow_unresolved_verification)
    review_payload.update(
        {
            "reviewId": review_id,
            "createdAt": utc_now(),
            "verification": verification,
            "modelAttribution": model_metadata,
            "parentReview": {
                "reviewId": review.get("reviewId"),
                "reviewPath": str(review_path),
                "reviewSha256": sha256_file(review_path),
                "attributionsPath": str(attributions_path),
                "attributionsSha256": sha256_file(attributions_path),
            },
        }
    )
    attribution_payload = {
        "schemaVersion": 1,
        "reviewId": review_id,
        "updatedAt": None,
        "groupLabels": json.loads(json.dumps(group_labels)),
        "utteranceOverrides": output_overrides,
        "verification": {},
        "parentAttributions": {
            "reviewId": review.get("reviewId"),
            "path": str(attributions_path),
            "sha256": sha256_file(attributions_path),
        },
        "modelAttribution": {
            "sourceEmbeddingsSha256": model_metadata["sourceEmbeddingsSha256"],
            "modelOverrideUtteranceIds": model_override_ids,
            **({"comparisonReference" if compare_reference else "profileReference": profile_metadata} if profile_metadata else {}),
        },
    }
    return review_payload, attribution_payload, summary


def predict_participant(
    *,
    np: Any,
    participant_ids: list[str],
    references: list[dict[str, Any]],
    embedding: Any,
    excluded_group_id: str | None,
) -> tuple[str, float] | None:
    prediction = score_participant(np=np, participant_ids=participant_ids, references=references,
                                  embedding=embedding, excluded_group_id=excluded_group_id)
    return (prediction[0], prediction[1]) if prediction else None


def validate_confidence_policy(margin: float | None, cosine: float | None) -> None:
    if margin is not None and (not math.isfinite(margin) or not 0 <= margin <= 2):
        raise SpeakerReviewError("--minimum-model-margin must be finite and between 0 and 2")
    if cosine is not None and (not math.isfinite(cosine) or not -1 <= cosine <= 1):
        raise SpeakerReviewError("--minimum-model-cosine must be finite and between -1 and 1")


def score_participant(
    *, np: Any, participant_ids: list[str], references: list[dict[str, Any]],
    embedding: Any, excluded_group_id: str | None,
) -> tuple[str, float, float] | None:
    vectors_by_participant: dict[str, list[Any]] = defaultdict(list)
    for reference in references:
        if excluded_group_id is None or reference["groupId"] != excluded_group_id:
            vectors_by_participant[reference["participantId"]].append(
                reference["embedding"]
            )
    if any(not vectors_by_participant.get(item) for item in participant_ids):
        return None
    profiles = []
    for participant_id in participant_ids:
        profile = np.mean(vectors_by_participant[participant_id], axis=0)
        norm = float(np.linalg.norm(profile))
        if norm <= 1e-12:
            raise SpeakerReviewError(
                f"participant {participant_id} produced a zero profile vector"
            )
        profiles.append(profile / norm)
    scores = embedding @ np.vstack(profiles).T
    order = np.argsort(scores)
    predicted_id = participant_ids[int(order[-1])]
    margin = (
        float(scores[order[-1]] - scores[order[-2]])
        if len(participant_ids) > 1
        else float("inf")
    )
    return predicted_id, margin, float(scores[order[-1]])


def load_embedding_metadata(np: Any, path: Path) -> dict[str, Any] | None:
    try:
        with np.load(path, allow_pickle=False) as payload:
            if "metadata_json" not in payload.files:
                return None
            metadata = json.loads(str(payload["metadata_json"].item()))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SpeakerReviewError(
            f"could not read speaker embedding metadata {path}: {exc}"
        ) from exc
    if not isinstance(metadata, dict):
        raise SpeakerReviewError("speaker embedding metadata must be an object")
    return metadata


def validate_embedding_source(
    metadata: dict[str, Any],
    *,
    source_type: str,
    source_sha256: str,
    label: str,
) -> None:
    if metadata.get("sourceType") != source_type:
        raise SpeakerReviewError(f"{label} has the wrong source type")
    if metadata.get("sourceSha256") != source_sha256:
        raise SpeakerReviewError(f"{label} was created from a different source file")
    if metadata.get("complete") is not True:
        raise SpeakerReviewError(f"{label} is incomplete; resume embedding before use")


def build_reference_bank_references(
    *,
    review: dict[str, Any],
    manifest: dict[str, Any],
    embedding_by_id: dict[str, Any],
    manifest_path: Path,
    embeddings_path: Path,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("clips"), list):
        raise SpeakerReviewError("reference-bank manifest has an unsupported schema")
    participants = review.get("participants", [])
    current_by_name: dict[str, dict[str, Any]] = {}
    for participant in participants:
        key = person_name_key(participant.get("name"))
        if not key or key in current_by_name:
            raise SpeakerReviewError(
                "current participant names must be present and unique for reference-bank matching"
            )
        current_by_name[key] = participant

    references = []
    bank_names = set()
    role_mismatches = []
    used_hashes = set()
    for clip in manifest["clips"]:
        if not isinstance(clip, dict):
            raise SpeakerReviewError("reference-bank clip is malformed")
        clip_hash = str(clip.get("clipSha256") or "")
        name = str(clip.get("name") or "")
        key = person_name_key(name)
        if not clip_hash or not key:
            raise SpeakerReviewError("reference-bank clip requires name and SHA-256")
        if clip_hash in used_hashes:
            raise SpeakerReviewError("reference-bank contains duplicate clip hashes")
        used_hashes.add(clip_hash)
        participant = current_by_name.get(key)
        if participant is None:
            raise SpeakerReviewError(
                f"reference-bank participant is absent from the current roster: {name}"
            )
        embedding = embedding_by_id.get(clip_hash)
        if embedding is None:
            raise SpeakerReviewError(
                f"reference-bank embedding cache is missing clip {clip_hash}"
            )
        bank_names.add(key)
        bank_role = str(clip.get("gameRole") or "")
        if bank_role and bank_role != participant.get("gameRole"):
            role_mismatches.append(
                {
                    "name": participant["name"],
                    "referenceGameRole": bank_role,
                    "currentGameRole": participant.get("gameRole"),
                }
            )
        references.append(
            {
                "utteranceId": str(clip.get("utteranceId") or clip_hash),
                "participantId": participant["id"],
                "groupId": f"reference:{clip_hash}",
                "embedding": embedding,
            }
        )
    missing_names = [
        participant["name"]
        for key, participant in current_by_name.items()
        if key not in bank_names
    ]
    if missing_names:
        raise SpeakerReviewError(
            "reference bank lacks clips for current participants: "
            + ", ".join(missing_names)
        )
    return references, {
        "method": "verified-reference-bank-matched-by-participant-name",
        "manifestPath": str(manifest_path),
        "manifestSha256": sha256_file(manifest_path),
        "embeddingsPath": str(embeddings_path),
        "embeddingsSha256": sha256_file(embeddings_path),
        "clipCount": len(references),
        "participantCount": len(bank_names),
        "roleMismatches": role_mismatches,
    }


def person_name_key(value: Any) -> str:
    return " ".join(str(value or "").split()).casefold()


def export_reference_bank(args: argparse.Namespace) -> int:
    validate_verification_sample_count(args.samples_per_participant)
    review_path = resolve_input(args.review, "speaker review")
    attributions_path = resolve_input(args.attributions, "speaker attributions")
    review = load_json_object(review_path, "speaker review")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)
    selected = select_verified_reference_samples(
        review, attributions, args.samples_per_participant
    )
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="reference-bank output directory",
    )
    manifest_path = output_dir / "reference-bank.json"
    planned_paths = [
        output_dir
        / slugify(item["participant"]["gameRole"])
        / f"{item['participantIndex']:02d}-{item['utterance']['id']}.m4a"
        for item in selected
    ]
    ensure_writable_outputs([manifest_path, *planned_paths], force=args.force)

    recordings = {item["id"]: item for item in review.get("recordings", [])}
    prepared_sources: dict[str, tuple[Path, Any]] = {}
    manifest_items = []
    with tempfile.TemporaryDirectory(prefix="speaker-reference-bank-") as raw_temp:
        backend = resolve_clip_backend()
        work_dir = Path(raw_temp)
        for item, output_path in zip(selected, planned_paths):
            utterance = item["utterance"]
            recording = recordings[utterance["recordingId"]]
            if utterance["recordingId"] not in prepared_sources:
                source = resolve_input(Path(recording["audioPath"]), "reference audio")
                prepared_sources[utterance["recordingId"]] = prepare_clip_source(
                    source, backend=backend, work_dir=work_dir
                )
            source, prepared_backend = prepared_sources[utterance["recordingId"]]
            extract_audio_clip(
                source,
                output_path,
                start_seconds=float(utterance["start"]),
                end_seconds=float(utterance["end"]),
                backend=prepared_backend,
            )
            manifest_items.append(
                {
                    "participantId": item["participant"]["id"],
                    "name": item["participant"]["name"],
                    "gameRole": item["participant"]["gameRole"],
                    "utteranceId": utterance["id"],
                    "recordingId": utterance["recordingId"],
                    "start": utterance["start"],
                    "end": utterance["end"],
                    "text": utterance.get("text", ""),
                    "clipPath": str(output_path),
                    "clipSha256": sha256_file(output_path),
                    "provenance": reference_provenance(attributions, utterance),
                }
            )

    manifest = {
        "schemaVersion": 1,
        "createdAt": utc_now(),
        "scope": "per-session",
        "sourceReview": {
            "reviewId": review.get("reviewId"),
            "path": str(review_path),
            "sha256": sha256_file(review_path),
        },
        "sourceAttributions": {
            "path": str(attributions_path),
            "sha256": sha256_file(attributions_path),
        },
        "selection": {
            "source": "confirmed time-spread verification samples",
            "samplesPerParticipant": args.samples_per_participant,
        },
        "clips": manifest_items,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(manifest_path, manifest)
    print(f"Wrote {manifest_path}")
    print(
        f"Reference bank: participants={len({item['participantId'] for item in manifest_items})} "
        f"clips={len(manifest_items)}"
    )
    return 0


def select_verified_reference_samples(
    review: dict[str, Any],
    attributions: dict[str, Any],
    count: int,
) -> list[dict[str, Any]]:
    participants = review.get("participants", [])
    utterance_by_id = {item["id"]: item for item in review.get("utterances", [])}
    group_labels = attributions.get("groupLabels", {})
    overrides = attributions.get("utteranceOverrides", {})
    confirmations = attributions.get("verification", {})
    selected: list[dict[str, Any]] = []
    for participant in participants:
        confirmation = confirmations.get(participant["id"])
        if not confirmation or confirmation.get("status") != "confirmed":
            raise SpeakerReviewError(
                f"cannot export reference clips before verifying {participant['gameRole']}"
            )
        verified = []
        for utterance_id in confirmation.get("sampleUtteranceIds", []):
            utterance = utterance_by_id.get(utterance_id)
            if utterance is None:
                continue
            label = overrides.get(utterance_id)
            if label is None and utterance.get("groupId"):
                label = group_labels.get(utterance["groupId"])
            if label and label.get("status") == "assigned" and label.get(
                "participantId"
            ) == participant["id"]:
                verified.append(utterance)
        if not verified:
            raise SpeakerReviewError(
                f"{participant['gameRole']} has no current confirmed verification samples"
            )
        picked = spread_by_time(verified, min(count, len(verified)))
        for index, utterance in enumerate(picked, start=1):
            selected.append(
                {
                    "participant": participant,
                    "participantIndex": index,
                    "utterance": utterance,
                }
            )
    return selected


def spread_by_time(items: list[dict[str, Any]], count: int) -> list[dict[str, Any]]:
    ordered = sorted(items, key=lambda item: (float(item["start"]), item["id"]))
    if count >= len(ordered):
        return ordered
    positions = [
        round(index * (len(ordered) - 1) / max(1, count - 1))
        for index in range(count)
    ]
    return [ordered[position] for position in positions]


def reference_provenance(
    attributions: dict[str, Any], utterance: dict[str, Any]
) -> str:
    model_ids = set(
        attributions.get("modelAttribution", {}).get("modelOverrideUtteranceIds", [])
    )
    if utterance["id"] in model_ids:
        return "model-assisted-and-time-spread-verified"
    if utterance["id"] in attributions.get("utteranceOverrides", {}):
        return "manual-override-and-time-spread-verified"
    return "manual-group-and-time-spread-verified"


def slugify(value: str) -> str:
    normalized = "".join(
        character.lower() if character.isalnum() else "-" for character in value
    )
    return "-".join(part for part in normalized.split("-") if part) or "speaker"


if __name__ == "__main__":
    raise SystemExit(main())

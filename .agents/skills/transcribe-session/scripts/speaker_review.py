#!/usr/bin/env python3
"""Build and serve cluster-level speaker review for Scribe v2 transcripts."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Sequence
from urllib.parse import urlparse

from workspace_paths import resolve_transcription_output

try:
    import yaml
except ImportError:  # pragma: no cover - optional when using the strict roster fallback
    yaml = None


SAMPLE_RATE = 16_000
MIN_FEATURE_SECONDS = 0.45
MIN_FEATURE_WORDS = 1
SENTENCE_SPLIT_SECONDS = 1.2
SILENCE_SPLIT_SECONDS = 0.75
MAX_UTTERANCE_SECONDS = 10.0
DEFAULT_GROUPS_PER_SPEAKER = 3
DEFAULT_REPRESENTATIVES = 3
DEFAULT_REFINEMENT_GROUPS = 8
DEFAULT_VERIFICATION_SAMPLES = 10


class SpeakerReviewError(RuntimeError):
    """A user-facing speaker-review failure."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Group Scribe v2 utterances by local acoustic similarity, review only "
            "representative clips, and render an attributed VTT."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Create cluster-review artifacts.")
    prepare.add_argument("--audio", action="append", type=Path, required=True)
    prepare.add_argument("--transcript", action="append", type=Path, required=True)
    prepare.add_argument("--participants", type=Path, required=True)
    prepare.add_argument("--output-dir", type=Path, required=True)
    prepare.add_argument("--review-id", required=True)
    prepare.add_argument(
        "--groups-per-speaker",
        type=int,
        default=DEFAULT_GROUPS_PER_SPEAKER,
        help="Microclusters per roster participant for each recording (default: 3).",
    )
    prepare.add_argument(
        "--representatives",
        type=int,
        default=DEFAULT_REPRESENTATIVES,
        help="Representative clips offered for each group (default: 3).",
    )
    prepare.add_argument(
        "--verification-samples",
        type=int,
        default=DEFAULT_VERIFICATION_SAMPLES,
        help="Time-spread samples per participant in the verification view (default: 10).",
    )
    prepare.add_argument(
        "--ffmpeg",
        type=Path,
        help="Optional ffmpeg executable when it is not available on PATH.",
    )
    prepare.add_argument("--force", action="store_true")

    refine = subparsers.add_parser(
        "refine",
        help="Replace mixed or unknown groups with smaller child groups.",
    )
    refine.add_argument("review", type=Path)
    refine.add_argument("--attributions", type=Path, required=True)
    refine.add_argument("--output-dir", type=Path, required=True)
    refine.add_argument("--review-id", required=True)
    refine.add_argument(
        "--groups-per-parent",
        type=int,
        default=DEFAULT_REFINEMENT_GROUPS,
        help="Child groups created for each mixed or unknown parent (default: 8).",
    )
    refine.add_argument(
        "--representatives",
        type=int,
        default=DEFAULT_REPRESENTATIVES,
        help="Representative clips offered for each child group (default: 3).",
    )
    refine.add_argument(
        "--verification-samples",
        type=int,
        default=DEFAULT_VERIFICATION_SAMPLES,
        help="Time-spread samples per participant in the verification view (default: 10).",
    )
    refine.add_argument(
        "--ffmpeg",
        type=Path,
        help="Optional ffmpeg executable when it is not available on PATH.",
    )
    refine.add_argument("--force", action="store_true")

    serve = subparsers.add_parser("serve", help="Serve the local review page.")
    serve.add_argument("review", type=Path)
    serve.add_argument("--attributions", type=Path)
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8765)

    render = subparsers.add_parser("render", help="Render reviewed assignments as VTT.")
    render.add_argument("review", type=Path)
    render.add_argument("--attributions", type=Path, required=True)
    render.add_argument("--output", type=Path, required=True)
    render.add_argument(
        "--label-mode",
        choices=("game-role", "name"),
        default="game-role",
    )
    render.add_argument("--allow-unresolved", action="store_true")
    render.add_argument(
        "--allow-unverified",
        action="store_true",
        help="Render a draft without participant verification confirmations.",
    )
    render.add_argument("--force", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "prepare":
            return prepare_review(args)
        if args.command == "refine":
            return refine_review(args)
        if args.command == "serve":
            return serve_review(args)
        if args.command == "render":
            return render_review(args)
        raise SpeakerReviewError(f"unsupported command: {args.command}")
    except SpeakerReviewError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def prepare_review(args: argparse.Namespace) -> int:
    np = load_numpy()
    if len(args.audio) != len(args.transcript):
        raise SpeakerReviewError("supply one --transcript for each --audio, in matching order")
    if args.groups_per_speaker < 1:
        raise SpeakerReviewError("--groups-per-speaker must be positive")
    if not 1 <= args.representatives <= 5:
        raise SpeakerReviewError("--representatives must be between 1 and 5")
    validate_verification_sample_count(args.verification_samples)
    review_id = normalize_identifier(args.review_id)
    participants_path = resolve_input(args.participants, "participant roster")
    participants = load_participants(participants_path)
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="speaker-review output directory",
    )
    review_path = output_dir / f"{review_id}.speaker-review.json"
    attributions_path = output_dir / f"{review_id}.speaker-attributions.json"
    ensure_writable_outputs([review_path, attributions_path], force=args.force)

    audio_paths = [resolve_input(path, "audio") for path in args.audio]
    transcript_paths = [resolve_input(path, "Scribe transcript") for path in args.transcript]
    recordings: list[dict[str, Any]] = []
    utterances: list[dict[str, Any]] = []
    groups: list[dict[str, Any]] = []
    unclustered_ids: list[str] = []

    with tempfile.TemporaryDirectory(prefix="speaker-review-") as raw_temp_dir:
        temp_dir = Path(raw_temp_dir)
        decoder = resolve_pcm_decoder(explicit_ffmpeg=args.ffmpeg)
        for recording_index, (audio_path, transcript_path) in enumerate(
            zip(audio_paths, transcript_paths), start=1
        ):
            recording_id = f"r{recording_index:02d}"
            payload = load_scribe_payload(transcript_path)
            recording_utterances = build_utterances(payload["words"], recording_id)
            if not recording_utterances:
                raise SpeakerReviewError(f"no timed utterances found in {transcript_path}")

            pcm_path = temp_dir / f"{recording_id}.pcm"
            duration_seconds, decoded_sample_rate = decode_to_pcm(audio_path, pcm_path, decoder)
            samples = np.memmap(pcm_path, dtype="<i2", mode="r")
            feature_ids: list[str] = []
            feature_rows: list[Any] = []
            mel_filters, dct_basis = feature_bases(np)
            for utterance in recording_utterances:
                if not is_feature_eligible(utterance):
                    unclustered_ids.append(utterance["id"])
                    continue
                vector = acoustic_feature_vector(
                    np,
                    samples,
                    start=float(utterance["start"]),
                    end=float(utterance["end"]),
                    decoded_sample_rate=decoded_sample_rate,
                    mel_filters=mel_filters,
                    dct_basis=dct_basis,
                )
                if vector is None:
                    unclustered_ids.append(utterance["id"])
                    continue
                feature_ids.append(utterance["id"])
                feature_rows.append(vector)

            if not feature_rows:
                raise SpeakerReviewError(f"no usable speech features found in {audio_path}")
            features = np.vstack(feature_rows)
            normalized = robust_normalize(np, features)
            group_count = min(
                len(feature_ids), len(participants) * args.groups_per_speaker
            )
            labels, centroids = kmeans(np, normalized, group_count, seed=recording_index)
            by_id = {utterance["id"]: utterance for utterance in recording_utterances}
            for cluster_index in range(group_count):
                member_positions = np.flatnonzero(labels == cluster_index).tolist()
                if not member_positions:
                    continue
                group_id = f"{recording_id}-g{cluster_index + 1:03d}"
                member_ids = [feature_ids[position] for position in member_positions]
                representative_ids = choose_representatives(
                    np,
                    normalized,
                    centroids[cluster_index],
                    member_positions,
                    by_id,
                    feature_ids,
                    args.representatives,
                )
                source_ids = sorted(
                    {
                        speaker
                        for member_id in member_ids
                        for speaker in by_id[member_id]["scribeSpeakerIds"]
                    }
                )
                group_duration = sum(
                    by_id[member_id]["end"] - by_id[member_id]["start"]
                    for member_id in member_ids
                )
                groups.append(
                    {
                        "id": group_id,
                        "recordingId": recording_id,
                        "memberUtteranceIds": member_ids,
                        "representativeUtteranceIds": representative_ids,
                        "utteranceCount": len(member_ids),
                        "speechSeconds": round(group_duration, 3),
                        "scribeSpeakerIds": source_ids,
                    }
                )
                for member_id in member_ids:
                    by_id[member_id]["groupId"] = group_id

            recordings.append(
                {
                    "id": recording_id,
                    "audioPath": str(audio_path),
                    "audioSha256": sha256_file(audio_path),
                    "transcriptPath": str(transcript_path),
                    "transcriptSha256": sha256_file(transcript_path),
                    "durationSeconds": round(duration_seconds, 3),
                    "decodedSampleRate": decoded_sample_rate,
                    "utteranceCount": len(recording_utterances),
                    "clusteredUtteranceCount": len(feature_ids),
                }
            )
            utterances.extend(recording_utterances)

    review_payload = {
        "schemaVersion": 1,
        "reviewId": review_id,
        "createdAt": utc_now(),
        "participantsPath": str(participants_path),
        "participants": participants,
        "algorithm": {
            "name": "local-mfcc-microclusters",
            "version": 1,
            "sampleRate": SAMPLE_RATE,
            "groupsPerSpeakerPerRecording": args.groups_per_speaker,
            "representativesPerGroup": args.representatives,
            "notes": (
                "Scribe speaker IDs are retained only as weak evidence; cluster labels "
                "must be confirmed from representative audio."
            ),
        },
        "recordings": recordings,
        "utterances": utterances,
        "groups": groups,
        "exceptions": {"unclusteredUtteranceIds": unclustered_ids},
        "verification": {"samplesPerParticipant": args.verification_samples},
    }
    attribution_payload = {
        "schemaVersion": 1,
        "reviewId": review_id,
        "updatedAt": None,
        "groupLabels": {},
        "utteranceOverrides": {},
        "verification": {},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(review_path, review_payload)
    atomic_write_json(attributions_path, attribution_payload)
    print(f"Wrote {review_path}")
    print(f"Wrote {attributions_path}")
    print(
        f"Review: recordings={len(recordings)} utterances={len(utterances)} "
        f"groups={len(groups)} unclustered={len(unclustered_ids)}"
    )
    return 0


def refine_review(args: argparse.Namespace) -> int:
    np = load_numpy()
    if args.groups_per_parent < 2:
        raise SpeakerReviewError("--groups-per-parent must be at least 2")
    if not 1 <= args.representatives <= 5:
        raise SpeakerReviewError("--representatives must be between 1 and 5")
    validate_verification_sample_count(args.verification_samples)

    source_review_path = resolve_input(args.review, "speaker review")
    source_attributions_path = resolve_input(args.attributions, "speaker attributions")
    source_review = load_json_object(source_review_path, "speaker review")
    source_attributions = load_json_object(
        source_attributions_path, "speaker attributions"
    )
    validate_attributions(source_review, source_attributions)

    group_by_id = {item["id"]: item for item in source_review.get("groups", [])}
    parent_ids = [
        group_id
        for group_id, label in source_attributions["groupLabels"].items()
        if label["status"] in {"mixed", "unknown"}
    ]
    if not parent_ids:
        raise SpeakerReviewError("no mixed or unknown calibration groups to refine")
    missing_parents = sorted(set(parent_ids) - set(group_by_id))
    if missing_parents:
        raise SpeakerReviewError(
            "attributions reference missing refinement parents: "
            + ", ".join(missing_parents)
        )

    review_id = normalize_identifier(args.review_id)
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="speaker-refinement output directory",
    )
    review_path = output_dir / f"{review_id}.speaker-review.json"
    attributions_path = output_dir / f"{review_id}.speaker-attributions.json"
    if review_path == source_review_path or attributions_path == source_attributions_path:
        raise SpeakerReviewError("refinement must write new review and attribution files")
    ensure_writable_outputs([review_path, attributions_path], force=args.force)

    utterances = json.loads(json.dumps(source_review.get("utterances", [])))
    utterance_by_id = {item["id"]: item for item in utterances}
    recordings = json.loads(json.dumps(source_review.get("recordings", [])))
    recording_by_id = {item["id"]: item for item in recordings}
    target_utterance_ids = {
        utterance_id
        for parent_id in parent_ids
        for utterance_id in group_by_id[parent_id]["memberUtteranceIds"]
    }
    unknown_utterance_ids = sorted(target_utterance_ids - set(utterance_by_id))
    if unknown_utterance_ids:
        raise SpeakerReviewError(
            "refinement parent contains unknown utterances: "
            + ", ".join(unknown_utterance_ids[:10])
        )

    feature_by_id: dict[str, Any] = {}
    newly_unclustered: set[str] = set()
    mel_filters, dct_basis = feature_bases(np)
    decoder = resolve_pcm_decoder(explicit_ffmpeg=args.ffmpeg)
    with tempfile.TemporaryDirectory(prefix="speaker-refine-") as raw_temp_dir:
        temp_dir = Path(raw_temp_dir)
        target_recording_ids = sorted(
            {
                utterance_by_id[utterance_id]["recordingId"]
                for utterance_id in target_utterance_ids
            }
        )
        for recording_id in target_recording_ids:
            recording = recording_by_id.get(recording_id)
            if recording is None:
                raise SpeakerReviewError(
                    f"refinement utterance references unknown recording {recording_id}"
                )
            audio_path = resolve_input(Path(recording["audioPath"]), "review audio")
            pcm_path = temp_dir / f"{recording_id}.pcm"
            _, decoded_sample_rate = decode_to_pcm(audio_path, pcm_path, decoder)
            samples = np.memmap(pcm_path, dtype="<i2", mode="r")
            for utterance_id in sorted(target_utterance_ids):
                utterance = utterance_by_id[utterance_id]
                if utterance["recordingId"] != recording_id:
                    continue
                vector = acoustic_feature_vector(
                    np,
                    samples,
                    start=float(utterance["start"]),
                    end=float(utterance["end"]),
                    decoded_sample_rate=decoded_sample_rate,
                    mel_filters=mel_filters,
                    dct_basis=dct_basis,
                )
                if vector is None:
                    newly_unclustered.add(utterance_id)
                    utterance["groupId"] = None
                else:
                    feature_by_id[utterance_id] = vector
            del samples

    children_by_parent: dict[str, list[dict[str, Any]]] = {}
    for parent_id in parent_ids:
        parent = group_by_id[parent_id]
        feature_ids = [
            utterance_id
            for utterance_id in parent["memberUtteranceIds"]
            if utterance_id in feature_by_id
        ]
        if len(feature_ids) < 2:
            raise SpeakerReviewError(
                f"refinement parent {parent_id} has fewer than two usable utterances"
            )
        feature_rows = np.vstack([feature_by_id[item] for item in feature_ids])
        normalized = robust_normalize(np, feature_rows)
        group_count = min(len(feature_ids), args.groups_per_parent)
        seed = int(hashlib.sha256(parent_id.encode("utf-8")).hexdigest()[:8], 16)
        labels, centroids = kmeans(np, normalized, group_count, seed=seed)
        child_groups: list[dict[str, Any]] = []
        for cluster_index in range(group_count):
            member_positions = np.flatnonzero(labels == cluster_index).tolist()
            if not member_positions:
                continue
            group_id = f"{parent_id}-r{cluster_index + 1:02d}"
            member_ids = [feature_ids[position] for position in member_positions]
            representative_ids = choose_representatives(
                np,
                normalized,
                centroids[cluster_index],
                member_positions,
                utterance_by_id,
                feature_ids,
                args.representatives,
            )
            source_ids = sorted(
                {
                    speaker
                    for member_id in member_ids
                    for speaker in utterance_by_id[member_id].get(
                        "scribeSpeakerIds", []
                    )
                }
            )
            group_duration = sum(
                float(utterance_by_id[member_id]["end"])
                - float(utterance_by_id[member_id]["start"])
                for member_id in member_ids
            )
            child_groups.append(
                {
                    "id": group_id,
                    "recordingId": parent["recordingId"],
                    "refinedFromGroupId": parent_id,
                    "memberUtteranceIds": member_ids,
                    "representativeUtteranceIds": representative_ids,
                    "utteranceCount": len(member_ids),
                    "speechSeconds": round(group_duration, 3),
                    "scribeSpeakerIds": source_ids,
                }
            )
            for member_id in member_ids:
                utterance_by_id[member_id]["groupId"] = group_id
        children_by_parent[parent_id] = child_groups

    groups: list[dict[str, Any]] = []
    for source_group in source_review["groups"]:
        if source_group["id"] in children_by_parent:
            groups.extend(children_by_parent[source_group["id"]])
        else:
            groups.append(json.loads(json.dumps(source_group)))

    unclustered_ids = set(
        source_review.get("exceptions", {}).get("unclusteredUtteranceIds", [])
    )
    unclustered_ids.update(newly_unclustered)
    algorithm = json.loads(json.dumps(source_review.get("algorithm", {})))
    refinement_history = list(algorithm.get("refinements", []))
    refinement_history.append(
        {
            "createdAt": utc_now(),
            "parentReviewId": source_review.get("reviewId"),
            "parentGroupIds": parent_ids,
            "groupsPerParent": args.groups_per_parent,
            "representativesPerGroup": args.representatives,
        }
    )
    algorithm["refinements"] = refinement_history

    review_payload = json.loads(json.dumps(source_review))
    review_payload.update(
        {
            "reviewId": review_id,
            "createdAt": utc_now(),
            "algorithm": algorithm,
            "recordings": recordings,
            "utterances": utterances,
            "groups": groups,
            "exceptions": {"unclusteredUtteranceIds": sorted(unclustered_ids)},
            "verification": {
                "samplesPerParticipant": args.verification_samples
            },
            "parentReview": {
                "reviewId": source_review.get("reviewId"),
                "reviewPath": str(source_review_path),
                "reviewSha256": sha256_file(source_review_path),
                "attributionsPath": str(source_attributions_path),
                "attributionsSha256": sha256_file(source_attributions_path),
            },
        }
    )
    carried_group_labels = {
        group_id: json.loads(json.dumps(label))
        for group_id, label in source_attributions["groupLabels"].items()
        if group_id not in set(parent_ids)
    }
    attribution_payload = {
        "schemaVersion": 1,
        "reviewId": review_id,
        "updatedAt": None,
        "groupLabels": carried_group_labels,
        "utteranceOverrides": json.loads(
            json.dumps(source_attributions.get("utteranceOverrides", {}))
        ),
        "verification": {},
        "parentAttributions": {
            "reviewId": source_review.get("reviewId"),
            "path": str(source_attributions_path),
            "sha256": sha256_file(source_attributions_path),
        },
    }
    validate_attributions(review_payload, attribution_payload)
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(review_path, review_payload)
    atomic_write_json(attributions_path, attribution_payload)
    child_count = sum(len(items) for items in children_by_parent.values())
    print(f"Wrote {review_path}")
    print(f"Wrote {attributions_path}")
    print(
        f"Refinement: parents={len(parent_ids)} child_groups={child_count} "
        f"carried_labels={len(carried_group_labels)} "
        f"newly_unclustered={len(newly_unclustered)}"
    )
    return 0


def validate_verification_sample_count(value: int) -> None:
    if not 1 <= value <= 20:
        raise SpeakerReviewError("verification samples must be between 1 and 20")


def load_numpy() -> Any:
    try:
        import numpy as np
    except ImportError as exc:
        raise SpeakerReviewError(
            "speaker clustering requires NumPy; run this command with a Python environment that provides numpy"
        ) from exc
    return np


def resolve_input(path: Path, label: str) -> Path:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise SpeakerReviewError(f"{label} file not found: {resolved}")
    if resolved.stat().st_size == 0:
        raise SpeakerReviewError(f"{label} file is empty: {resolved}")
    return resolved


def normalize_identifier(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9._-]+", "-", value.strip()).strip("-.")
    if not normalized:
        raise SpeakerReviewError("--review-id must contain a letter or number")
    return normalized


def load_participants(path: Path) -> list[dict[str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
        payload = yaml.safe_load(text) if yaml is not None else parse_simple_participant_yaml(text)
    except (OSError, UnicodeError, ValueError) as exc:
        raise SpeakerReviewError(f"could not read participant roster {path}: {exc}") from exc
    except Exception as exc:
        if yaml is not None and isinstance(exc, yaml.YAMLError):
            raise SpeakerReviewError(f"could not read participant roster {path}: {exc}") from exc
        raise
    raw_participants = payload.get("participants") if isinstance(payload, dict) else None
    if not isinstance(raw_participants, list) or not raw_participants:
        raise SpeakerReviewError("participant roster must contain a non-empty participants list")
    participants: list[dict[str, str]] = []
    for index, raw in enumerate(raw_participants, start=1):
        if not isinstance(raw, dict):
            raise SpeakerReviewError(f"participant {index} is not a mapping")
        name = normalize_text(raw.get("name"))
        game_role = normalize_text(raw.get("gameRole"))
        if not name or not game_role:
            raise SpeakerReviewError(f"participant {index} requires name and gameRole")
        participants.append(
            {
                "id": f"p{index:02d}",
                "name": name,
                "gameRole": game_role,
                "display": f"{name} / {game_role}",
            }
        )
    return participants


def parse_simple_participant_yaml(text: str) -> dict[str, Any]:
    """Parse the skill's small participant-roster subset when PyYAML is unavailable."""
    participants: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    saw_header = False
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped == "participants:":
            saw_header = True
            continue
        match = re.fullmatch(r"-\s+name:\s*(.+)", stripped)
        if match:
            if current is not None:
                participants.append(current)
            current = {"name": parse_yaml_scalar(match.group(1))}
            continue
        match = re.fullmatch(r"gameRole:\s*(.+)", stripped)
        if match and current is not None:
            current["gameRole"] = parse_yaml_scalar(match.group(1))
            continue
        if saw_header and current is not None and re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*:\s*.*", stripped):
            continue
        raise ValueError(f"unsupported participant roster syntax at line {line_number}")
    if current is not None:
        participants.append(current)
    return {"participants": participants} if saw_header else {}


def parse_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        if value[0] == '"':
            try:
                return str(json.loads(value))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid quoted YAML scalar: {value}") from exc
        return value[1:-1].replace("''", "'")
    return value.split(" #", 1)[0].rstrip()


def load_scribe_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SpeakerReviewError(f"could not read Scribe JSON {path}: {exc}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("words"), list):
        raise SpeakerReviewError(f"Scribe JSON is missing its words list: {path}")
    return payload


def build_utterances(items: Sequence[dict[str, Any]], recording_id: str) -> list[dict[str, Any]]:
    utterances: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    def flush() -> None:
        nonlocal current
        if current is None:
            return
        text = normalize_text("".join(current.pop("pieces")))
        if text:
            utterance_index = len(utterances) + 1
            current["id"] = f"{recording_id}-u{utterance_index:05d}"
            current["text"] = text
            current["durationSeconds"] = round(current["end"] - current["start"], 3)
            current["scribeSpeakerIds"] = sorted(current["scribeSpeakerIds"])
            current["groupId"] = None
            utterances.append(current)
        current = None

    for item in items:
        if not isinstance(item, dict):
            continue
        start = item.get("start")
        end = item.get("end")
        text = item.get("text")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            continue
        if not isinstance(text, str) or not text:
            continue
        start_value = float(start)
        end_value = float(end)
        if start_value < 0 or end_value < start_value:
            continue
        item_type = str(item.get("type") or "word")
        speaker = normalize_text(item.get("speaker_id")) or "unknown"
        if current is not None and item_type != "spacing":
            previous_text = normalize_text("".join(current["pieces"]))
            gap = start_value - float(current["end"])
            duration = float(current["end"]) - float(current["start"])
            speaker_changed = speaker not in current["scribeSpeakerIds"]
            sentence_ended = bool(re.search(r"[.!?][\"')\]]*$", previous_text))
            if (
                speaker_changed
                or gap >= SILENCE_SPLIT_SECONDS
                or duration >= MAX_UTTERANCE_SECONDS
                or (sentence_ended and duration >= SENTENCE_SPLIT_SECONDS)
            ):
                flush()
        if current is None:
            current = {
                "recordingId": recording_id,
                "start": start_value,
                "end": end_value,
                "pieces": [],
                "wordCount": 0,
                "scribeSpeakerIds": set(),
            }
        current["pieces"].append(text)
        current["end"] = max(float(current["end"]), end_value)
        current["scribeSpeakerIds"].add(speaker)
        if item_type == "word" and re.search(r"[\w']", text, flags=re.UNICODE):
            current["wordCount"] += 1
    flush()
    return utterances


def is_feature_eligible(utterance: dict[str, Any]) -> bool:
    return (
        utterance["end"] - utterance["start"] >= MIN_FEATURE_SECONDS
        and utterance["wordCount"] >= MIN_FEATURE_WORDS
    )


def resolve_pcm_decoder(*, explicit_ffmpeg: Path | None = None) -> tuple[str, str]:
    candidates: list[Path] = []
    if explicit_ffmpeg is not None:
        candidates.append(explicit_ffmpeg.expanduser())
    discovered = shutil.which("ffmpeg")
    if discovered:
        candidates.append(Path(discovered))
    candidates.extend(
        [
            Path("/Applications/Codex.app/Contents/Resources/bin/ffmpeg"),
            Path("/Applications/editor.app/Contents/Resources/bin/ffmpeg"),
        ]
    )
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.is_file() and os.access(resolved, os.X_OK):
            return "ffmpeg", str(resolved)
    raise SpeakerReviewError(
        "speaker clustering requires ffmpeg; place it on PATH or pass --ffmpeg"
    )


def decode_to_pcm(audio_path: Path, pcm_path: Path, decoder: tuple[str, str]) -> tuple[float, int]:
    name, executable = decoder
    command = [
        executable,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(audio_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        str(SAMPLE_RATE),
        "-f",
        "s16le",
        str(pcm_path),
    ]
    try:
        completed = subprocess.run(
            command, text=True, capture_output=True, check=False, timeout=600
        )
    except subprocess.TimeoutExpired as exc:
        raise SpeakerReviewError(f"timed out decoding {audio_path}") from exc
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise SpeakerReviewError(f"could not decode {audio_path.name}: {detail[:1600]}")
    if not pcm_path.is_file() or pcm_path.stat().st_size < 2:
        raise SpeakerReviewError(f"decoder produced no PCM audio for {audio_path}")
    if pcm_path.stat().st_size % 2:
        raise SpeakerReviewError(f"decoder produced malformed 16-bit PCM for {audio_path}")
    decoded_sample_rate = SAMPLE_RATE
    if decoded_sample_rate <= 0:
        raise SpeakerReviewError("decoder returned a non-positive sample rate")
    return pcm_path.stat().st_size / 2 / decoded_sample_rate, decoded_sample_rate


def feature_bases(np: Any) -> tuple[Any, Any]:
    fft_size = 512
    mel_count = 26
    frequencies = np.linspace(0.0, SAMPLE_RATE / 2.0, fft_size // 2 + 1)
    low_mel = hz_to_mel(80.0)
    high_mel = hz_to_mel(min(7600.0, SAMPLE_RATE / 2.0 - 1.0))
    mel_points = np.linspace(low_mel, high_mel, mel_count + 2)
    hz_points = mel_to_hz(mel_points)
    filters = np.zeros((mel_count, len(frequencies)), dtype=np.float64)
    for index in range(mel_count):
        left, center, right = hz_points[index : index + 3]
        rising = (frequencies - left) / max(center - left, 1e-9)
        falling = (right - frequencies) / max(right - center, 1e-9)
        filters[index] = np.maximum(0.0, np.minimum(rising, falling))
    mel_indices = np.arange(mel_count, dtype=np.float64) + 0.5
    coefficient_indices = np.arange(13, dtype=np.float64)[:, None]
    dct = np.cos(np.pi / mel_count * coefficient_indices * mel_indices[None, :])
    return filters, dct


def hz_to_mel(value: Any) -> Any:
    import numpy as np

    return 2595.0 * np.log10(1.0 + np.asarray(value) / 700.0)


def mel_to_hz(value: Any) -> Any:
    import numpy as np

    return 700.0 * (np.power(10.0, np.asarray(value) / 2595.0) - 1.0)


def acoustic_feature_vector(
    np: Any,
    samples: Any,
    *,
    start: float,
    end: float,
    decoded_sample_rate: int,
    mel_filters: Any,
    dct_basis: Any,
) -> Any | None:
    start_sample = max(0, int(round((start - 0.08) * decoded_sample_rate)))
    end_sample = min(len(samples), int(round((end + 0.08) * decoded_sample_rate)))
    if end_sample - start_sample < int(MIN_FEATURE_SECONDS * decoded_sample_rate):
        return None
    signal = np.asarray(samples[start_sample:end_sample], dtype=np.float64) / 32768.0
    if decoded_sample_rate != SAMPLE_RATE:
        source_positions = np.arange(len(signal), dtype=np.float64)
        output_length = max(1, round(len(signal) * SAMPLE_RATE / decoded_sample_rate))
        target_positions = np.linspace(0.0, max(0.0, len(signal) - 1.0), output_length)
        signal = np.interp(target_positions, source_positions, signal)
    signal -= np.mean(signal)
    peak = float(np.max(np.abs(signal)))
    if peak < 1e-5:
        return None
    signal = np.append(signal[0], signal[1:] - 0.97 * signal[:-1])
    frame_length = int(round(0.025 * SAMPLE_RATE))
    hop_length = int(round(0.010 * SAMPLE_RATE))
    if len(signal) < frame_length:
        return None
    frame_count = 1 + (len(signal) - frame_length) // hop_length
    shape = (frame_count, frame_length)
    strides = (signal.strides[0] * hop_length, signal.strides[0])
    frames = np.lib.stride_tricks.as_strided(signal, shape=shape, strides=strides).copy()
    windowed = frames * np.hamming(frame_length)[None, :]
    energy = np.mean(windowed * windowed, axis=1) + 1e-12
    log_energy = 10.0 * np.log10(energy)
    threshold = max(float(np.max(log_energy)) - 38.0, float(np.percentile(log_energy, 25)))
    voiced = windowed[log_energy >= threshold]
    voiced_log_energy = log_energy[log_energy >= threshold]
    if len(voiced) < 4:
        voiced = windowed
        voiced_log_energy = log_energy
    power = np.abs(np.fft.rfft(voiced, n=512, axis=1)) ** 2
    mel_energy = np.maximum(power @ mel_filters.T, 1e-12)
    mfcc = np.log(mel_energy) @ dct_basis.T
    mfcc = mfcc[:, 1:13]
    frequencies = np.linspace(0.0, SAMPLE_RATE / 2.0, power.shape[1])
    power_sum = np.maximum(np.sum(power, axis=1), 1e-12)
    centroid = np.sum(power * frequencies[None, :], axis=1) / power_sum
    zcr = np.mean(np.abs(np.diff(np.signbit(voiced), axis=1)), axis=1)
    return np.concatenate(
        [
            np.mean(mfcc, axis=0),
            np.std(mfcc, axis=0),
            np.array(
                [
                    np.mean(voiced_log_energy),
                    np.std(voiced_log_energy),
                    np.mean(centroid),
                    np.std(centroid),
                    np.mean(zcr),
                    np.std(zcr),
                ]
            ),
        ]
    )


def robust_normalize(np: Any, features: Any) -> Any:
    median = np.median(features, axis=0)
    deviation = np.median(np.abs(features - median), axis=0)
    scale = np.where(deviation > 1e-8, deviation * 1.4826, np.std(features, axis=0))
    scale = np.where(scale > 1e-8, scale, 1.0)
    normalized = (features - median) / scale
    norms = np.linalg.norm(normalized, axis=1, keepdims=True)
    return normalized / np.where(norms > 1e-8, norms, 1.0)


def kmeans(np: Any, features: Any, group_count: int, *, seed: int) -> tuple[Any, Any]:
    rng = np.random.default_rng(seed)
    centroids = [features[int(rng.integers(len(features)))]]
    closest_sq = np.sum((features - centroids[0]) ** 2, axis=1)
    while len(centroids) < group_count:
        total = float(np.sum(closest_sq))
        if total <= 1e-12:
            next_index = len(centroids) % len(features)
        else:
            next_index = int(rng.choice(len(features), p=closest_sq / total))
        centroids.append(features[next_index])
        distance_sq = np.sum((features - features[next_index]) ** 2, axis=1)
        closest_sq = np.minimum(closest_sq, distance_sq)
    centroid_array = np.vstack(centroids)
    labels = np.full(len(features), -1, dtype=np.int64)
    for _ in range(100):
        distances = np.sum(
            (features[:, None, :] - centroid_array[None, :, :]) ** 2, axis=2
        )
        new_labels = np.argmin(distances, axis=1)
        if np.array_equal(labels, new_labels):
            break
        labels = new_labels
        for cluster_index in range(group_count):
            members = features[labels == cluster_index]
            if len(members):
                centroid_array[cluster_index] = np.mean(members, axis=0)
            else:
                farthest = int(np.argmax(np.min(distances, axis=1)))
                centroid_array[cluster_index] = features[farthest]
    return labels, centroid_array


def choose_representatives(
    np: Any,
    features: Any,
    centroid: Any,
    member_positions: list[int],
    by_id: dict[str, dict[str, Any]],
    feature_ids: list[str],
    count: int,
) -> list[str]:
    identifiable = [
        position
        for position in member_positions
        if by_id[feature_ids[position]]["durationSeconds"] >= 1.5
        and by_id[feature_ids[position]]["wordCount"] >= 4
    ]
    ranked = sorted(
        identifiable or member_positions,
        key=lambda position: float(np.sum((features[position] - centroid) ** 2)),
    )
    selected: list[int] = []
    for position in ranked:
        start = by_id[feature_ids[position]]["start"]
        if all(abs(start - by_id[feature_ids[other]]["start"]) >= 20.0 for other in selected):
            selected.append(position)
            if len(selected) == count:
                break
    if len(selected) < count:
        for position in ranked:
            if position not in selected:
                selected.append(position)
                if len(selected) >= count:
                    break
    return [feature_ids[position] for position in selected]


def serve_review(args: argparse.Namespace) -> int:
    review_path = resolve_input(args.review, "speaker review")
    review = load_json_object(review_path, "speaker review")
    attributions_path = (
        args.attributions.expanduser().resolve()
        if args.attributions
        else review_path.with_name(review_path.name.replace(".speaker-review.json", ".speaker-attributions.json"))
    )
    resolve_transcription_output(
        attributions_path,
        error_type=SpeakerReviewError,
        label="speaker-review decisions",
    )
    attributions_path = resolve_input(attributions_path, "speaker attributions")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)
    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        raise SpeakerReviewError("the review server may bind only to localhost")
    html_path = Path(__file__).parents[1] / "assets" / "speaker-review.html"
    html = resolve_input(html_path, "speaker review interface").read_bytes()
    recordings = {item["id"]: Path(item["audioPath"]) for item in review["recordings"]}
    for path in recordings.values():
        resolve_input(path, "review audio")

    class ReviewHandler(BaseHTTPRequestHandler):
        server_version = "SpeakerReview/1"

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path in {"/", "/index.html"}:
                self.send_bytes(html, "text/html; charset=utf-8")
                return
            if parsed.path == "/api/review":
                self.send_json(review)
                return
            if parsed.path == "/api/attributions":
                self.send_json(load_json_object(attributions_path, "speaker attributions"))
                return
            match = re.fullmatch(r"/audio/([A-Za-z0-9_-]+)", parsed.path)
            if match and match.group(1) in recordings:
                self.send_audio(recordings[match.group(1)])
                return
            self.send_error(HTTPStatus.NOT_FOUND)

        def do_POST(self) -> None:  # noqa: N802
            if urlparse(self.path).path != "/api/attributions":
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length <= 0 or length > 2_000_000:
                    raise SpeakerReviewError("invalid attribution request size")
                payload = json.loads(self.rfile.read(length).decode("utf-8"))
                validate_attributions(review, payload)
                payload["updatedAt"] = utc_now()
                atomic_write_json(attributions_path, payload)
            except (UnicodeError, json.JSONDecodeError, SpeakerReviewError) as exc:
                self.send_json({"error": str(exc)}, status=HTTPStatus.BAD_REQUEST)
                return
            self.send_json({"ok": True, "updatedAt": payload["updatedAt"]})

        def send_json(self, payload: Any, status: HTTPStatus = HTTPStatus.OK) -> None:
            data = (json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def send_bytes(self, data: bytes, content_type: str) -> None:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def send_audio(self, path: Path) -> None:
            total = path.stat().st_size
            start, end = 0, total - 1
            range_header = self.headers.get("Range")
            status = HTTPStatus.OK
            if range_header:
                match = re.fullmatch(r"bytes=(\d*)-(\d*)", range_header.strip())
                if not match:
                    self.send_error(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                    return
                if match.group(1):
                    start = int(match.group(1))
                if match.group(2):
                    end = min(int(match.group(2)), total - 1)
                if start > end or start >= total:
                    self.send_error(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                    return
                status = HTTPStatus.PARTIAL_CONTENT
            length = end - start + 1
            content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Length", str(length))
            if status == HTTPStatus.PARTIAL_CONTENT:
                self.send_header("Content-Range", f"bytes {start}-{end}/{total}")
            self.end_headers()
            with path.open("rb") as handle:
                handle.seek(start)
                remaining = length
                while remaining:
                    chunk = handle.read(min(64 * 1024, remaining))
                    if not chunk:
                        break
                    try:
                        self.wfile.write(chunk)
                    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                        return
                    remaining -= len(chunk)

        def log_message(self, format: str, *values: Any) -> None:
            print(f"review: {self.address_string()} - {format % values}")

    server = ThreadingHTTPServer((args.host, args.port), ReviewHandler)
    print(f"Speaker review: http://{args.host}:{server.server_port}/")
    print(f"Saving decisions to {attributions_path}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def validate_attributions(review: dict[str, Any], payload: Any) -> None:
    if not isinstance(payload, dict):
        raise SpeakerReviewError("speaker attributions must be a JSON object")
    if payload.get("schemaVersion") != 1 or payload.get("reviewId") != review.get("reviewId"):
        raise SpeakerReviewError("speaker attributions do not match this review")
    group_ids = {item["id"] for item in review.get("groups", [])}
    utterance_ids = {item["id"] for item in review.get("utterances", [])}
    participant_ids = {item["id"] for item in review.get("participants", [])}
    group_labels = payload.get("groupLabels")
    overrides = payload.get("utteranceOverrides")
    verification = payload.get("verification", {})
    if not isinstance(group_labels, dict) or not isinstance(overrides, dict):
        raise SpeakerReviewError("speaker attributions require groupLabels and utteranceOverrides objects")
    if not isinstance(verification, dict):
        raise SpeakerReviewError("speaker attribution verification must be an object")
    if not set(group_labels).issubset(group_ids):
        raise SpeakerReviewError("speaker attributions contain an unknown group id")
    if not set(overrides).issubset(utterance_ids):
        raise SpeakerReviewError("speaker attributions contain an unknown utterance id")
    for label in [*group_labels.values(), *overrides.values()]:
        if not isinstance(label, dict) or label.get("status") not in {"assigned", "mixed", "unknown"}:
            raise SpeakerReviewError("each attribution must have status assigned, mixed, or unknown")
        participant_id = label.get("participantId")
        if label["status"] == "assigned" and participant_id not in participant_ids:
            raise SpeakerReviewError("assigned attribution has an unknown participant id")
        if label["status"] != "assigned" and participant_id is not None:
            raise SpeakerReviewError("mixed and unknown attributions cannot name a participant")
    for participant_id, confirmation in verification.items():
        if participant_id not in participant_ids:
            raise SpeakerReviewError("speaker verification names an unknown participant")
        if not isinstance(confirmation, dict) or confirmation.get("status") != "confirmed":
            raise SpeakerReviewError("speaker verification status must be confirmed")
        sample_ids = confirmation.get("sampleUtteranceIds")
        if not isinstance(sample_ids, list) or not sample_ids:
            raise SpeakerReviewError("speaker verification requires sample utterance ids")
        if len(sample_ids) > 20 or len(set(sample_ids)) != len(sample_ids):
            raise SpeakerReviewError("speaker verification samples must be unique and at most 20")
        if not set(sample_ids).issubset(utterance_ids):
            raise SpeakerReviewError("speaker verification contains an unknown utterance id")


def render_review(args: argparse.Namespace) -> int:
    review_path = resolve_input(args.review, "speaker review")
    attributions_path = resolve_input(args.attributions, "speaker attributions")
    review = load_json_object(review_path, "speaker review")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)
    output_path = resolve_transcription_output(
        args.output,
        error_type=SpeakerReviewError,
        label="identified VTT output",
    )
    ensure_writable_outputs([output_path], force=args.force)
    participant_by_id = {item["id"]: item for item in review["participants"]}
    group_labels = attributions["groupLabels"]
    overrides = attributions["utteranceOverrides"]
    lines = ["WEBVTT", ""]
    counts = {
        "assigned": 0,
        "mixed": 0,
        "unknown": 0,
        "unreviewedGroup": 0,
        "unclustered": 0,
    }
    effective_labels: dict[str, dict[str, Any] | None] = {}
    for utterance in review["utterances"]:
        label = overrides.get(utterance["id"])
        if label is None and utterance.get("groupId"):
            label = group_labels.get(utterance["groupId"])
        effective_labels[utterance["id"]] = label
        if label is None:
            status = "unreviewedGroup" if utterance.get("groupId") else "unclustered"
            display = "Unknown"
        elif label["status"] == "assigned":
            status = "assigned"
            participant = participant_by_id[label["participantId"]]
            display = participant["gameRole"] if args.label_mode == "game-role" else participant["name"]
        elif label["status"] == "mixed":
            status = "mixed"
            display = "Unknown"
        else:
            status = "unknown"
            display = "Unknown"
        counts[status] += 1
        lines.append(f"{format_vtt_time(utterance['start'])} --> {format_vtt_time(utterance['end'])}")
        lines.append(f"{display}: {utterance['text']}")
        lines.append("")
    blocking_unresolved = (
        counts["mixed"] + counts["unknown"] + counts["unreviewedGroup"]
    )
    total_unresolved = blocking_unresolved + counts["unclustered"]
    if blocking_unresolved and not args.allow_unresolved:
        raise SpeakerReviewError(
            f"refusing pipeline VTT with {blocking_unresolved} utterances in unreviewed, mixed, or unknown groups; finish calibration or add --allow-unresolved for a draft"
        )
    verification_target = int(
        review.get("verification", {}).get(
            "samplesPerParticipant", DEFAULT_VERIFICATION_SAMPLES
        )
    )
    validate_verification_sample_count(verification_target)
    confirmations = attributions.get("verification", {})
    verification_failures: list[str] = []
    verified_participants = 0
    for participant_id, participant in participant_by_id.items():
        assigned = [
            utterance
            for utterance in review["utterances"]
            if (effective_labels.get(utterance["id"]) or {}).get("status")
            == "assigned"
            and effective_labels[utterance["id"]]["participantId"] == participant_id
        ]
        if not assigned:
            continue
        eligible = [
            utterance
            for utterance in assigned
            if float(utterance.get("durationSeconds", 0.0)) >= 1.5
            and int(utterance.get("wordCount", 0)) >= 4
        ]
        candidates = eligible or assigned
        required_count = min(verification_target, len(candidates))
        confirmation = confirmations.get(participant_id)
        if not isinstance(confirmation, dict) or confirmation.get("status") != "confirmed":
            verification_failures.append(participant["gameRole"])
            continue
        sample_ids = confirmation.get("sampleUtteranceIds", [])
        valid_ids = {
            utterance["id"]
            for utterance in candidates
            if (effective_labels.get(utterance["id"]) or {}).get("status")
            == "assigned"
            and effective_labels[utterance["id"]]["participantId"] == participant_id
        }
        if len(sample_ids) < required_count or not set(sample_ids).issubset(valid_ids):
            verification_failures.append(participant["gameRole"])
            continue
        verified_participants += 1
    if verification_failures and not args.allow_unverified:
        raise SpeakerReviewError(
            "refusing pipeline VTT without current verification samples for: "
            + ", ".join(verification_failures)
            + "; finish the verification view or add --allow-unverified for a draft"
        )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(output_path, "\n".join(lines))
    print(f"Wrote {output_path}")
    print(
        json.dumps(
            {
                "utteranceCounts": counts,
                "blockingUnresolved": blocking_unresolved,
                "totalUnresolved": total_unresolved,
                "verifiedParticipants": verified_participants,
                "verificationFailures": verification_failures,
            },
            indent=2,
        )
    )
    return 0


def format_vtt_time(seconds: float) -> str:
    milliseconds = max(0, round(float(seconds) * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    whole_seconds, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d}.{millis:03d}"


def load_json_object(path: Path, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SpeakerReviewError(f"could not read {label} {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SpeakerReviewError(f"{label} must be a JSON object: {path}")
    return payload


def ensure_writable_outputs(paths: Sequence[Path], *, force: bool) -> None:
    existing = [path for path in paths if path.exists()]
    if existing and not force:
        formatted = "\n".join(f"- {path}" for path in existing)
        raise SpeakerReviewError("refusing to replace existing outputs without --force:\n" + formatted)


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_json(path: Path, payload: Any) -> None:
    atomic_write_text(path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    raise SystemExit(main())

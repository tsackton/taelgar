#!/usr/bin/env python3
"""Prepare, serve, and report a blind audit of speaker-model predictions."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import random
import re
import sys
from collections import defaultdict
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Sequence
from urllib.parse import urlparse

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
)
from workspace_paths import resolve_transcription_output


SCHEMA_VERSION = 1
DEFAULT_SAMPLE_COUNT = 50
DEFAULT_DISAGREEMENT_COUNT = 35
DEFAULT_SEED = 13501
MIN_AUDIT_SECONDS = 1.5
MIN_AUDIT_WORDS = 4


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Create a leakage-controlled blind audit of participant predictions, "
            "serve it locally, and summarize the saved decisions."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Create blind-audit artifacts.")
    prepare.add_argument("review", type=Path)
    prepare.add_argument("--attributions", type=Path, required=True)
    prepare.add_argument("--embeddings", type=Path, required=True)
    prepare.add_argument("--output-dir", type=Path, required=True)
    prepare.add_argument("--audit-id", required=True)
    prepare.add_argument("--sample-count", type=int, default=DEFAULT_SAMPLE_COUNT)
    prepare.add_argument(
        "--disagreement-count", type=int, default=DEFAULT_DISAGREEMENT_COUNT
    )
    prepare.add_argument("--seed", type=int, default=DEFAULT_SEED)
    prepare.add_argument(
        "--model-name", default="speechbrain/spkrec-ecapa-voxceleb"
    )
    prepare.add_argument("--force", action="store_true")

    serve = subparsers.add_parser("serve", help="Serve the blind review page.")
    serve.add_argument("audit", type=Path)
    serve.add_argument("--decisions", type=Path)
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8767)

    report = subparsers.add_parser("report", help="Summarize completed audit decisions.")
    report.add_argument("audit", type=Path)
    report.add_argument("--decisions", type=Path, required=True)
    report.add_argument("--output", type=Path)
    report.add_argument("--force", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "prepare":
            return prepare_audit(args)
        if args.command == "serve":
            return serve_audit(args)
        if args.command == "report":
            return report_audit(args)
    except SpeakerReviewError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    raise AssertionError(f"unknown command {args.command}")


def prepare_audit(args: argparse.Namespace) -> int:
    validate_sample_counts(args.sample_count, args.disagreement_count)
    review_path = resolve_input(args.review, "speaker review")
    attributions_path = resolve_input(args.attributions, "speaker attributions")
    embeddings_path = resolve_input(args.embeddings, "speaker embeddings")
    review = load_json_object(review_path, "speaker review")
    attributions = load_json_object(attributions_path, "speaker attributions")
    validate_attributions(review, attributions)
    np = load_numpy()
    embedding_by_id, embedding_dimension = load_embedding_cache(np, embeddings_path)

    participants = review.get("participants", [])
    participant_ids = [item["id"] for item in participants]
    participant_id_set = set(participant_ids)
    utterance_by_id = {item["id"]: item for item in review.get("utterances", [])}
    group_by_id = {item["id"]: item for item in review.get("groups", [])}
    group_labels = attributions.get("groupLabels", {})
    overrides = attributions.get("utteranceOverrides", {})
    references = build_profile_references(
        group_by_id, group_labels, utterance_by_id, embedding_by_id
    )
    missing_profiles = participant_id_set - {item["participantId"] for item in references}
    if missing_profiles:
        raise SpeakerReviewError(
            "cannot audit without reference embeddings for participants: "
            + ", ".join(sorted(missing_profiles))
        )

    candidates = build_candidates(
        np=np,
        review=review,
        participant_ids=participant_ids,
        references=references,
        embedding_by_id=embedding_by_id,
        group_labels=group_labels,
        overrides=overrides,
    )
    disagreements = [item for item in candidates if item["kind"] == "disagreement"]
    controls = [item for item in candidates if item["kind"] == "control"]
    control_count = args.sample_count - args.disagreement_count
    if len(disagreements) < args.disagreement_count:
        raise SpeakerReviewError(
            f"requested {args.disagreement_count} disagreements but only {len(disagreements)} are available"
        )
    if len(controls) < control_count:
        raise SpeakerReviewError(
            f"requested {control_count} controls but only {len(controls)} are available"
        )

    selected_disagreements = select_stratified(
        disagreements,
        args.disagreement_count,
        group_key=lambda item: (
            item["currentParticipantId"],
            item["predictedParticipantId"],
        ),
        balanced=False,
        seed=args.seed,
    )
    selected_controls = select_stratified(
        controls,
        control_count,
        group_key=lambda item: (item["currentParticipantId"],),
        balanced=True,
        seed=args.seed + 1,
    )
    selected = selected_disagreements + selected_controls
    random.Random(args.seed).shuffle(selected)

    audit_id = normalize_identifier(args.audit_id)
    output_dir = resolve_transcription_output(
        args.output_dir,
        error_type=SpeakerReviewError,
        label="speaker-audit output directory",
    )
    audit_path = output_dir / f"{audit_id}.speaker-audit.json"
    decisions_path = output_dir / f"{audit_id}.speaker-audit-decisions.json"
    ensure_writable_outputs([audit_path, decisions_path], force=args.force)

    items = []
    for index, candidate in enumerate(selected, start=1):
        utterance = utterance_by_id[candidate["utteranceId"]]
        item = {
            "id": f"a{index:03d}",
            "utteranceId": utterance["id"],
            "recordingId": utterance["recordingId"],
            "start": float(utterance["start"]),
            "end": float(utterance["end"]),
            "durationSeconds": float(utterance["durationSeconds"]),
            "text": str(utterance.get("text", "")),
            "hidden": {
                "kind": candidate["kind"],
                "currentParticipantId": candidate["currentParticipantId"],
                "predictedParticipantId": candidate["predictedParticipantId"],
                "margin": round(float(candidate["margin"]), 6),
                "currentGroupId": candidate.get("currentGroupId"),
                "samplingGroup": candidate["samplingGroup"],
                "populationSize": candidate["populationSize"],
                "sampleSize": candidate["sampleSize"],
                "analysisWeight": round(float(candidate["analysisWeight"]), 6),
            },
        }
        items.append(item)

    audit_payload = {
        "schemaVersion": SCHEMA_VERSION,
        "auditId": audit_id,
        "createdAt": utc_now(),
        "sourceReview": {
            "reviewId": review.get("reviewId"),
            "path": str(review_path),
            "sha256": sha256_file(review_path),
        },
        "sourceAttributions": {
            "path": str(attributions_path),
            "sha256": sha256_file(attributions_path),
        },
        "sourceEmbeddings": {
            "path": str(embeddings_path),
            "sha256": sha256_file(embeddings_path),
            "modelName": args.model_name,
            "dimension": embedding_dimension,
        },
        "method": {
            "name": "leave-current-group-out-nearest-profile",
            "version": 1,
            "profileReference": "reviewed group representatives",
            "minimumDurationSeconds": MIN_AUDIT_SECONDS,
            "minimumWordCount": MIN_AUDIT_WORDS,
            "notes": (
                "Each candidate is scored against participant profiles after excluding "
                "all reference utterances from that candidate's current acoustic group."
            ),
        },
        "selection": {
            "seed": args.seed,
            "sampleCount": len(items),
            "disagreementCount": len(selected_disagreements),
            "controlCount": len(selected_controls),
            "candidateCount": len(candidates),
            "candidateDisagreementCount": len(disagreements),
            "candidateControlCount": len(controls),
        },
        "participants": participants,
        "recordings": review.get("recordings", []),
        "items": items,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(audit_path, audit_payload)
    decisions_payload = {
        "schemaVersion": SCHEMA_VERSION,
        "auditId": audit_id,
        "sourceAuditSha256": sha256_file(audit_path),
        "createdAt": utc_now(),
        "updatedAt": utc_now(),
        "decisions": {},
    }
    atomic_write_json(decisions_path, decisions_payload)
    print(f"Wrote {audit_path}")
    print(f"Wrote {decisions_path}")
    print(
        f"Audit: candidates={len(candidates)} disagreements={len(disagreements)} "
        f"selected={len(items)} selected_disagreements={len(selected_disagreements)} "
        f"controls={len(selected_controls)}"
    )
    return 0


def validate_sample_counts(sample_count: int, disagreement_count: int) -> None:
    if not 10 <= sample_count <= 200:
        raise SpeakerReviewError("audit sample count must be between 10 and 200")
    if not 1 <= disagreement_count < sample_count:
        raise SpeakerReviewError(
            "audit disagreement count must be positive and smaller than the total sample count"
        )


def load_embedding_cache(np: Any, path: Path) -> tuple[dict[str, Any], int]:
    try:
        with np.load(path, allow_pickle=False) as payload:
            if "ids" not in payload.files or "embeddings" not in payload.files:
                raise SpeakerReviewError("speaker embedding cache requires ids and embeddings arrays")
            ids = [str(item) for item in payload["ids"]]
            matrix = np.asarray(payload["embeddings"], dtype=np.float64)
    except (OSError, ValueError) as exc:
        raise SpeakerReviewError(f"could not read speaker embedding cache {path}: {exc}") from exc
    if matrix.ndim != 2 or len(ids) != matrix.shape[0] or not len(ids):
        raise SpeakerReviewError("speaker embedding cache has inconsistent dimensions")
    if len(ids) != len(set(ids)):
        raise SpeakerReviewError("speaker embedding cache contains duplicate utterance ids")
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms <= 1e-12):
        raise SpeakerReviewError("speaker embedding cache contains a zero vector")
    matrix = matrix / norms
    return {utterance_id: matrix[index] for index, utterance_id in enumerate(ids)}, int(
        matrix.shape[1]
    )


def build_profile_references(
    group_by_id: dict[str, dict[str, Any]],
    group_labels: dict[str, dict[str, Any]],
    utterance_by_id: dict[str, dict[str, Any]],
    embedding_by_id: dict[str, Any],
) -> list[dict[str, Any]]:
    references = []
    for group_id, label in sorted(group_labels.items()):
        if label.get("status") != "assigned" or group_id not in group_by_id:
            continue
        group = group_by_id[group_id]
        for utterance_id in group.get("representativeUtteranceIds", []):
            utterance = utterance_by_id.get(utterance_id)
            if (
                utterance
                and utterance_id in embedding_by_id
                and float(utterance.get("durationSeconds", 0.0)) >= 1.2
                and int(utterance.get("wordCount", 0)) >= 3
            ):
                references.append(
                    {
                        "utteranceId": utterance_id,
                        "participantId": label["participantId"],
                        "groupId": group_id,
                        "embedding": embedding_by_id[utterance_id],
                    }
                )
    return references


def build_candidates(
    *,
    np: Any,
    review: dict[str, Any],
    participant_ids: list[str],
    references: list[dict[str, Any]],
    embedding_by_id: dict[str, Any],
    group_labels: dict[str, dict[str, Any]],
    overrides: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    candidates = []
    for utterance in review.get("utterances", []):
        utterance_id = utterance["id"]
        if (
            utterance_id not in embedding_by_id
            or float(utterance.get("durationSeconds", 0.0)) < MIN_AUDIT_SECONDS
            or int(utterance.get("wordCount", 0)) < MIN_AUDIT_WORDS
        ):
            continue
        label = overrides.get(utterance_id)
        if label is None and utterance.get("groupId"):
            label = group_labels.get(utterance["groupId"])
        if not label or label.get("status") != "assigned":
            continue
        excluded_group = utterance.get("groupId")
        vectors_by_participant: dict[str, list[Any]] = defaultdict(list)
        for reference in references:
            if reference["groupId"] != excluded_group:
                vectors_by_participant[reference["participantId"]].append(
                    reference["embedding"]
                )
        if any(not vectors_by_participant.get(item) for item in participant_ids):
            continue
        profile_rows = []
        for participant_id in participant_ids:
            profile = np.mean(vectors_by_participant[participant_id], axis=0)
            norm = float(np.linalg.norm(profile))
            if norm <= 1e-12:
                raise SpeakerReviewError(
                    f"participant {participant_id} produced a zero profile vector"
                )
            profile_rows.append(profile / norm)
        scores = embedding_by_id[utterance_id] @ np.vstack(profile_rows).T
        order = np.argsort(scores)
        predicted_id = participant_ids[int(order[-1])]
        margin = float(scores[order[-1]] - scores[order[-2]])
        current_id = label["participantId"]
        candidates.append(
            {
                "utteranceId": utterance_id,
                "currentParticipantId": current_id,
                "predictedParticipantId": predicted_id,
                "margin": margin,
                "start": float(utterance["start"]),
                "currentGroupId": excluded_group,
                "kind": "control" if current_id == predicted_id else "disagreement",
            }
        )
    return candidates


def select_stratified(
    candidates: list[dict[str, Any]],
    count: int,
    *,
    group_key: Any,
    balanced: bool,
    seed: int,
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        grouped[tuple(group_key(candidate))].append(candidate)
    sizes = {key: len(values) for key, values in grouped.items()}
    allocation = allocate_strata(sizes, count, balanced=balanced)
    selected: list[dict[str, Any]] = []
    for key in sorted(allocation):
        sample_size = allocation[key]
        if not sample_size:
            continue
        stable_seed = int.from_bytes(
            hashlib.sha256((str(seed) + "|" + "|".join(key)).encode("utf-8")).digest()[:8],
            "big",
        )
        picked = choose_spread(grouped[key], sample_size, seed=stable_seed)
        sampling_group = " -> ".join(key) if len(key) > 1 else key[0]
        for item in picked:
            item = dict(item)
            item["samplingGroup"] = sampling_group
            item["populationSize"] = sizes[key]
            item["sampleSize"] = sample_size
            item["analysisWeight"] = sizes[key] / sample_size
            selected.append(item)
    return selected


def allocate_strata(
    sizes: dict[tuple[str, ...], int], count: int, *, balanced: bool
) -> dict[tuple[str, ...], int]:
    if count < 0 or count > sum(sizes.values()):
        raise SpeakerReviewError("audit stratum allocation exceeds available candidates")
    allocation = {key: 0 for key in sizes}
    active = [key for key, size in sizes.items() if size]
    if not count or not active:
        return allocation
    priority = sorted(active, key=lambda key: (-sizes[key], key))
    for key in priority[: min(count, len(priority))]:
        allocation[key] = 1
    remaining = count - sum(allocation.values())
    while remaining:
        available = [key for key in active if allocation[key] < sizes[key]]
        if not available:
            break
        if balanced:
            chosen = min(
                available,
                key=lambda key: (allocation[key], -sizes[key], key),
            )
        else:
            total = sum(sizes.values())
            chosen = max(
                available,
                key=lambda key: (
                    sizes[key] * count / total - allocation[key],
                    sizes[key],
                    tuple(reversed(key)),
                ),
            )
        allocation[chosen] += 1
        remaining -= 1
    return allocation


def choose_spread(
    candidates: list[dict[str, Any]], count: int, *, seed: int
) -> list[dict[str, Any]]:
    if count >= len(candidates):
        return sorted(candidates, key=lambda item: item["utteranceId"])
    shuffled = list(candidates)
    random.Random(seed).shuffle(shuffled)
    starts = [float(item["start"]) for item in shuffled]
    margins = [float(item["margin"]) for item in shuffled]
    start_min, start_max = min(starts), max(starts)
    margin_min, margin_max = min(margins), max(margins)

    def coordinates(item: dict[str, Any]) -> tuple[float, float]:
        time_value = (
            (float(item["start"]) - start_min) / (start_max - start_min)
            if start_max > start_min
            else 0.5
        )
        margin_value = (
            (float(item["margin"]) - margin_min) / (margin_max - margin_min)
            if margin_max > margin_min
            else 0.5
        )
        return time_value, margin_value

    coords = [coordinates(item) for item in shuffled]
    first = min(
        range(len(shuffled)),
        key=lambda index: (
            (coords[index][0] - 0.5) ** 2 + (coords[index][1] - 0.5) ** 2,
            shuffled[index]["utteranceId"],
        ),
    )
    selected = [first]
    while len(selected) < count:
        remaining = [index for index in range(len(shuffled)) if index not in selected]
        next_index = max(
            remaining,
            key=lambda index: (
                min(
                    (coords[index][0] - coords[other][0]) ** 2
                    + (coords[index][1] - coords[other][1]) ** 2
                    for other in selected
                ),
                -index,
            ),
        )
        selected.append(next_index)
    return [shuffled[index] for index in selected]


def serve_audit(args: argparse.Namespace) -> int:
    audit_path = resolve_input(args.audit, "speaker audit")
    audit = load_json_object(audit_path, "speaker audit")
    validate_audit(audit)
    decisions_path = (
        args.decisions.expanduser().resolve()
        if args.decisions
        else audit_path.with_name(
            audit_path.name.replace(".speaker-audit.json", ".speaker-audit-decisions.json")
        )
    )
    resolve_transcription_output(
        decisions_path,
        error_type=SpeakerReviewError,
        label="speaker-audit decisions",
    )
    decisions_path = resolve_input(decisions_path, "speaker audit decisions")
    decisions = load_json_object(decisions_path, "speaker audit decisions")
    validate_decisions(audit, decisions, audit_path=audit_path)
    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        raise SpeakerReviewError("the blind audit server may bind only to localhost")
    html_path = Path(__file__).parents[1] / "assets" / "speaker-audit.html"
    html = resolve_input(html_path, "speaker audit interface").read_bytes()
    recordings = {
        item["id"]: resolve_input(Path(item["audioPath"]), "speaker audit audio")
        for item in audit["recordings"]
    }
    public_payload = public_audit_payload(audit)

    class AuditHandler(BaseHTTPRequestHandler):
        server_version = "SpeakerAudit/1"

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path in {"/", "/index.html"}:
                self.send_bytes(html, "text/html; charset=utf-8")
                return
            if parsed.path == "/api/audit":
                self.send_json(public_payload)
                return
            if parsed.path == "/api/decisions":
                self.send_json(load_json_object(decisions_path, "speaker audit decisions"))
                return
            match = re.fullmatch(r"/audio/([A-Za-z0-9_-]+)", parsed.path)
            if match and match.group(1) in recordings:
                self.send_audio(recordings[match.group(1)])
                return
            self.send_error(HTTPStatus.NOT_FOUND)

        def do_POST(self) -> None:  # noqa: N802
            if urlparse(self.path).path != "/api/decisions":
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length <= 0 or length > 1_000_000:
                    raise SpeakerReviewError("invalid audit decision request size")
                payload = json.loads(self.rfile.read(length).decode("utf-8"))
                validate_decisions(audit, payload, audit_path=audit_path)
                payload["updatedAt"] = utc_now()
                atomic_write_json(decisions_path, payload)
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
            status = HTTPStatus.OK
            range_header = self.headers.get("Range")
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
            print(f"audit: {self.address_string()} - {format % values}")

    server = ThreadingHTTPServer((args.host, args.port), AuditHandler)
    print(f"Blind speaker audit: http://{args.host}:{server.server_port}/")
    print(f"Saving decisions to {decisions_path}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def validate_audit(audit: Any) -> None:
    if not isinstance(audit, dict) or audit.get("schemaVersion") != SCHEMA_VERSION:
        raise SpeakerReviewError("speaker audit has an unsupported schema")
    if not audit.get("auditId") or not isinstance(audit.get("items"), list):
        raise SpeakerReviewError("speaker audit requires auditId and items")
    participant_ids = {item.get("id") for item in audit.get("participants", [])}
    recording_ids = {item.get("id") for item in audit.get("recordings", [])}
    item_ids = set()
    utterance_ids = set()
    for item in audit["items"]:
        if not isinstance(item, dict) or not item.get("id") or not item.get("utteranceId"):
            raise SpeakerReviewError("speaker audit item is malformed")
        if item["id"] in item_ids or item["utteranceId"] in utterance_ids:
            raise SpeakerReviewError("speaker audit items must be unique")
        item_ids.add(item["id"])
        utterance_ids.add(item["utteranceId"])
        if item.get("recordingId") not in recording_ids:
            raise SpeakerReviewError("speaker audit item references an unknown recording")
        hidden = item.get("hidden")
        if not isinstance(hidden, dict):
            raise SpeakerReviewError("speaker audit item is missing hidden comparison data")
        if hidden.get("currentParticipantId") not in participant_ids:
            raise SpeakerReviewError("speaker audit item has an unknown current participant")
        if hidden.get("predictedParticipantId") not in participant_ids:
            raise SpeakerReviewError("speaker audit item has an unknown predicted participant")


def public_audit_payload(audit: dict[str, Any]) -> dict[str, Any]:
    return {
        "schemaVersion": audit["schemaVersion"],
        "auditId": audit["auditId"],
        "participants": audit["participants"],
        "recordings": [
            {"id": item["id"], "name": Path(item["audioPath"]).name}
            for item in audit["recordings"]
        ],
        "items": [
            {
                key: value
                for key, value in item.items()
                if key
                in {
                    "id",
                    "utteranceId",
                    "recordingId",
                    "start",
                    "end",
                    "durationSeconds",
                    "text",
                }
            }
            for item in audit["items"]
        ],
    }


def validate_decisions(
    audit: dict[str, Any], payload: Any, *, audit_path: Path | None = None
) -> None:
    if not isinstance(payload, dict):
        raise SpeakerReviewError("speaker audit decisions must be a JSON object")
    if payload.get("schemaVersion") != SCHEMA_VERSION or payload.get("auditId") != audit.get(
        "auditId"
    ):
        raise SpeakerReviewError("speaker audit decisions do not match this audit")
    if audit_path is not None and payload.get("sourceAuditSha256") != sha256_file(audit_path):
        raise SpeakerReviewError("speaker audit decisions reference a different audit file")
    decisions = payload.get("decisions")
    if not isinstance(decisions, dict):
        raise SpeakerReviewError("speaker audit decisions require a decisions object")
    item_ids = {item["id"] for item in audit.get("items", [])}
    participant_ids = {item["id"] for item in audit.get("participants", [])}
    if not set(decisions).issubset(item_ids):
        raise SpeakerReviewError("speaker audit decisions contain an unknown item id")
    for decision in decisions.values():
        if not isinstance(decision, dict) or decision.get("status") not in {
            "assigned",
            "unknown",
            "overlap",
        }:
            raise SpeakerReviewError(
                "each audit decision must be assigned, unknown, or overlap"
            )
        participant_id = decision.get("participantId")
        if decision["status"] == "assigned" and participant_id not in participant_ids:
            raise SpeakerReviewError("assigned audit decision has an unknown participant")
        if decision["status"] in {"unknown", "overlap"} and participant_id is not None:
            raise SpeakerReviewError(
                "unknown and overlap audit decisions cannot name a participant"
            )
        if not isinstance(decision.get("transcriptRevealed", False), bool):
            raise SpeakerReviewError("audit transcriptRevealed must be true or false")


def report_audit(args: argparse.Namespace) -> int:
    audit_path = resolve_input(args.audit, "speaker audit")
    decisions_path = resolve_input(args.decisions, "speaker audit decisions")
    audit = load_json_object(audit_path, "speaker audit")
    decisions = load_json_object(decisions_path, "speaker audit decisions")
    validate_audit(audit)
    validate_decisions(audit, decisions, audit_path=audit_path)
    report = build_report(audit, decisions)
    if args.output:
        output_path = resolve_transcription_output(
            args.output,
            error_type=SpeakerReviewError,
            label="speaker-audit report",
        )
        ensure_writable_outputs([output_path], force=args.force)
        atomic_write_json(output_path, report)
        print(f"Wrote {output_path}")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


def build_report(audit: dict[str, Any], decisions: dict[str, Any]) -> dict[str, Any]:
    decision_by_id = decisions.get("decisions", {})
    participants = {item["id"]: item for item in audit.get("participants", [])}
    rows = []
    for item in audit.get("items", []):
        decision = decision_by_id.get(item["id"])
        actual_id = (
            decision.get("participantId")
            if decision and decision.get("status") == "assigned"
            else None
        )
        hidden = item["hidden"]
        rows.append(
            {
                "itemId": item["id"],
                "kind": hidden["kind"],
                "samplingGroup": hidden["samplingGroup"],
                "populationSize": int(hidden["populationSize"]),
                "sampleSize": int(hidden["sampleSize"]),
                "weight": float(hidden["analysisWeight"]),
                "margin": float(hidden["margin"]),
                "currentId": hidden["currentParticipantId"],
                "modelId": hidden["predictedParticipantId"],
                "actualId": actual_id,
                "decisionStatus": decision.get("status") if decision else None,
                "transcriptRevealed": bool(
                    decision and decision.get("transcriptRevealed", False)
                ),
            }
        )

    scored = [item for item in rows if item["actualId"]]
    disagreements = [item for item in rows if item["kind"] == "disagreement"]
    controls = [item for item in rows if item["kind"] == "control"]
    weighted_total = sum(item["weight"] for item in scored)
    weighted_model = sum(
        item["weight"] for item in scored if item["modelId"] == item["actualId"]
    )
    weighted_current = sum(
        item["weight"] for item in scored if item["currentId"] == item["actualId"]
    )

    def outcome_counts(values: list[dict[str, Any]]) -> dict[str, int]:
        counts = {
            "modelCorrect": 0,
            "currentCorrect": 0,
            "bothCorrect": 0,
            "neitherCorrect": 0,
            "unknown": 0,
            "overlap": 0,
        }
        for item in values:
            if not item["actualId"]:
                counts[
                    "overlap" if item.get("decisionStatus") == "overlap" else "unknown"
                ] += 1
                continue
            model_correct = item["modelId"] == item["actualId"]
            current_correct = item["currentId"] == item["actualId"]
            if model_correct and current_correct:
                counts["bothCorrect"] += 1
            elif model_correct:
                counts["modelCorrect"] += 1
            elif current_correct:
                counts["currentCorrect"] += 1
            else:
                counts["neitherCorrect"] += 1
        return counts

    pair_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in disagreements:
        pair_groups[row["samplingGroup"]].append(row)
    pair_breakdown = []
    for pair, values in sorted(
        pair_groups.items(), key=lambda item: (-item[1][0]["populationSize"], item[0])
    ):
        current_id, model_id = pair.split(" -> ", 1)
        pair_breakdown.append(
            {
                "current": participants[current_id]["gameRole"],
                "model": participants[model_id]["gameRole"],
                "population": values[0]["populationSize"],
                "sample": len(values),
                "outcomes": outcome_counts(values),
            }
        )

    margin_groups = {
        "below0.10": [item for item in disagreements if item["margin"] < 0.10],
        "0.10to0.20": [
            item for item in disagreements if 0.10 <= item["margin"] < 0.20
        ],
        "atLeast0.20": [item for item in disagreements if item["margin"] >= 0.20],
    }
    return {
        "schemaVersion": SCHEMA_VERSION,
        "auditId": audit["auditId"],
        "createdAt": utc_now(),
        "completion": {
            "sampleCount": len(rows),
            "assignedCount": len(scored),
            "unknownCount": sum(
                item.get("decisionStatus") != "overlap" and not item["actualId"]
                for item in rows
            ),
            "overlapCount": sum(
                item.get("decisionStatus") == "overlap" for item in rows
            ),
            "transcriptRevealedCount": sum(item["transcriptRevealed"] for item in rows),
        },
        "weightedPopulationEstimate": {
            "modelAccuracy": round(weighted_model / weighted_total, 4)
            if weighted_total
            else None,
            "currentAccuracy": round(weighted_current / weighted_total, 4)
            if weighted_total
            else None,
            "note": (
                "Exploratory estimate using inverse stratum sampling weights; the "
                "time-and-margin-spread sample is not a simple random sample."
            ),
        },
        "disagreementOutcomes": outcome_counts(disagreements),
        "controlOutcomes": outcome_counts(controls),
        "pairBreakdown": pair_breakdown,
        "disagreementMarginBreakdown": {
            key: {"sample": len(values), "outcomes": outcome_counts(values)}
            for key, values in margin_groups.items()
        },
    }


if __name__ == "__main__":
    raise SystemExit(main())

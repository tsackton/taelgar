#!/usr/bin/env python3
"""Validate and resolve a multi-track RPG session recording manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

import yaml

from media_tools import MediaBackend, MediaToolError, probe_duration, resolve_probe_backend
from workspace_paths import resolve_transcription_output


SCHEMA_VERSION = 1
TRACK_ROLES = {"primary", "alternate", "candidate"}
TRACK_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
MANIFEST_KEYS = {"schemaVersion", "campaign", "sessionNumber", "tracks"}
TRACK_KEYS = {"trackId", "role", "recordedBy", "alignment", "parts"}
ALIGNMENT_KEYS = {"referenceTrackId", "offsetSeconds"}
PART_KEYS = {"sequence", "path", "gapBeforeSeconds"}


class ManifestError(RuntimeError):
    """A user-facing recording manifest failure."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a session recording manifest, probe every audio part, and "
            "optionally write a normalized JSON inventory."
        )
    )
    parser.add_argument("manifest", type=Path, help="Authored YAML recording manifest.")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional normalized JSON output; omit to print the resolved manifest.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing normalized JSON output.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        source_path = resolve_input_file(args.manifest)
        try:
            probe_backend = resolve_probe_backend()
        except MediaToolError as exc:
            raise ManifestError(str(exc)) from exc
        resolved = resolve_manifest(source_path, probe_backend=probe_backend)
        rendered = json.dumps(resolved, indent=2, ensure_ascii=False) + "\n"
        if args.output is None:
            print(rendered, end="")
            return 0

        output_path = resolve_transcription_output(
            args.output,
            error_type=ManifestError,
            label="resolved recording manifest",
        )
        if output_path == source_path:
            raise ManifestError("normalized output cannot replace the authored YAML manifest")
        if output_path.exists() and not args.force:
            raise ManifestError(f"refusing to replace existing output without --force: {output_path}")
        atomic_write_text(output_path, rendered)
        print(f"Wrote {output_path}")
        print(
            f"Resolved {len(resolved['tracks'])} tracks and "
            f"{sum(len(track['parts']) for track in resolved['tracks'])} audio parts"
        )
        return 0
    except ManifestError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def resolve_input_file(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    if not resolved.is_file():
        raise ManifestError(f"recording manifest not found: {resolved}")
    return resolved


def resolve_manifest(
    source_path: Path, *, probe_backend: MediaBackend
) -> dict[str, Any]:
    try:
        payload = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ManifestError(f"could not read {source_path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ManifestError("recording manifest must be a YAML mapping")
    reject_unknown_keys(payload, MANIFEST_KEYS, "recording manifest")

    schema_version = payload.get("schemaVersion")
    if schema_version != SCHEMA_VERSION:
        raise ManifestError(
            f"schemaVersion must be {SCHEMA_VERSION}, got {schema_version!r}"
        )
    campaign = required_text(payload.get("campaign"), "campaign")
    session_number = parse_session_number(payload.get("sessionNumber"))
    raw_tracks = payload.get("tracks")
    if not isinstance(raw_tracks, list) or not raw_tracks:
        raise ManifestError("tracks must be a non-empty list")

    track_ids: list[str] = []
    roles: list[str] = []
    for index, raw_track in enumerate(raw_tracks, start=1):
        if not isinstance(raw_track, dict):
            raise ManifestError(f"tracks[{index}] must be a mapping")
        reject_unknown_keys(raw_track, TRACK_KEYS, f"tracks[{index}]")
        track_id = required_text(raw_track.get("trackId"), f"tracks[{index}].trackId")
        if not TRACK_ID_RE.fullmatch(track_id):
            raise ManifestError(
                f"trackId must use lowercase letters, numbers, hyphens, or underscores: {track_id!r}"
            )
        if track_id in track_ids:
            raise ManifestError(f"duplicate trackId: {track_id}")
        role = required_text(raw_track.get("role"), f"tracks[{index}].role")
        if role not in TRACK_ROLES:
            raise ManifestError(
                f"track {track_id} role must be one of {sorted(TRACK_ROLES)}, got {role!r}"
            )
        track_ids.append(track_id)
        roles.append(role)

    primary_ids = [track_id for track_id, role in zip(track_ids, roles) if role == "primary"]
    if len(primary_ids) > 1:
        raise ManifestError(f"at most one track may be primary: {primary_ids}")
    primary_track_id = primary_ids[0] if primary_ids else None

    seen_paths: set[Path] = set()
    resolved_tracks: list[dict[str, Any]] = []
    for index, raw_track in enumerate(raw_tracks, start=1):
        resolved_tracks.append(
            resolve_track(
                raw_track,
                index=index,
                manifest_dir=source_path.parent,
                known_track_ids=set(track_ids),
                primary_track_id=primary_track_id,
                seen_paths=seen_paths,
                probe_backend=probe_backend,
            )
        )
    apply_session_offsets(resolved_tracks, primary_track_id=primary_track_id)

    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceManifestPath": str(source_path),
        "campaign": campaign,
        "sessionNumber": session_number,
        "primaryTrackId": primary_track_id,
        "probeBackend": probe_backend.name,
        "tracks": resolved_tracks,
    }


def resolve_track(
    raw_track: dict[str, Any],
    *,
    index: int,
    manifest_dir: Path,
    known_track_ids: set[str],
    primary_track_id: str | None,
    seen_paths: set[Path],
    probe_backend: MediaBackend,
) -> dict[str, Any]:
    track_id = str(raw_track["trackId"])
    role = str(raw_track["role"])
    recorded_by = optional_text(raw_track.get("recordedBy"), f"track {track_id}.recordedBy")
    alignment = resolve_alignment(
        raw_track.get("alignment"),
        track_id=track_id,
        role=role,
        known_track_ids=known_track_ids,
        primary_track_id=primary_track_id,
    )
    raw_parts = raw_track.get("parts")
    if not isinstance(raw_parts, list) or not raw_parts:
        raise ManifestError(f"track {track_id} parts must be a non-empty list")
    for part_index, raw_part in enumerate(raw_parts, start=1):
        if not isinstance(raw_part, dict):
            raise ManifestError(f"track {track_id} part {part_index} must be a mapping")
        reject_unknown_keys(
            raw_part,
            PART_KEYS,
            f"track {track_id} part {part_index}",
        )

    expected_sequences = list(range(1, len(raw_parts) + 1))
    actual_sequences = [
        parse_positive_int(
            part.get("sequence") if isinstance(part, dict) else None,
            f"track {track_id} part sequence",
        )
        for part in raw_parts
    ]
    if actual_sequences != expected_sequences:
        raise ManifestError(
            f"track {track_id} part sequences must be listed consecutively from 1; got {actual_sequences}"
        )

    elapsed = 0.0
    resolved_parts: list[dict[str, Any]] = []
    for part_index, raw_part in enumerate(raw_parts, start=1):
        assert isinstance(raw_part, dict)
        raw_path = required_text(
            raw_part.get("path"), f"track {track_id} part {part_index}.path"
        )
        source_path = Path(raw_path).expanduser()
        if not source_path.is_absolute():
            source_path = manifest_dir / source_path
        source_path = source_path.resolve()
        if not source_path.is_file():
            raise ManifestError(f"audio part not found: {source_path}")
        if source_path in seen_paths:
            raise ManifestError(f"audio part appears more than once: {source_path}")
        seen_paths.add(source_path)

        gap_before = parse_nonnegative_number(
            raw_part.get("gapBeforeSeconds", 0),
            f"track {track_id} part {part_index}.gapBeforeSeconds",
        )
        if part_index == 1 and gap_before != 0:
            raise ManifestError(
                f"track {track_id} first part must use gapBeforeSeconds: 0; use alignment.offsetSeconds for track timing"
            )
        elapsed += gap_before
        try:
            duration = probe_duration(source_path, backend=probe_backend)
        except MediaToolError as exc:
            raise ManifestError(str(exc)) from exc

        resolved_parts.append(
            {
                "sequence": part_index,
                "path": str(source_path),
                "bytes": source_path.stat().st_size,
                "sha256": sha256_file(source_path),
                "durationSeconds": round(duration, 3),
                "gapBeforeSeconds": round(gap_before, 3),
                "trackStartSeconds": round(elapsed, 3),
                "sessionStartSeconds": None,
            }
        )
        elapsed += duration

    result: dict[str, Any] = {
        "trackId": track_id,
        "role": role,
        "alignment": alignment,
        "durationSeconds": round(elapsed, 3),
        "parts": resolved_parts,
    }
    if recorded_by is not None:
        result["recordedBy"] = recorded_by
    return result


def resolve_alignment(
    raw_alignment: Any,
    *,
    track_id: str,
    role: str,
    known_track_ids: set[str],
    primary_track_id: str | None,
) -> dict[str, Any]:
    if raw_alignment is None:
        raw_alignment = {}
    if not isinstance(raw_alignment, dict):
        raise ManifestError(f"track {track_id} alignment must be a mapping")
    reject_unknown_keys(raw_alignment, ALIGNMENT_KEYS, f"track {track_id}.alignment")

    reference = optional_text(
        raw_alignment.get("referenceTrackId"),
        f"track {track_id}.alignment.referenceTrackId",
    )
    raw_offset = raw_alignment.get("offsetSeconds")

    if role == "primary":
        if reference is not None:
            raise ManifestError(f"primary track {track_id} cannot reference another track")
        if raw_offset not in (None, 0, 0.0):
            raise ManifestError(f"primary track {track_id} offsetSeconds must be 0")
        return {"referenceTrackId": None, "offsetSeconds": 0.0, "status": "resolved"}

    if reference is None and primary_track_id is not None:
        reference = primary_track_id
    if reference == track_id:
        raise ManifestError(f"track {track_id} cannot align to itself")
    if reference is not None and reference not in known_track_ids:
        raise ManifestError(f"track {track_id} references unknown track {reference!r}")
    if raw_offset is None:
        offset: float | None = None
    else:
        offset = parse_finite_number(
            raw_offset, f"track {track_id}.alignment.offsetSeconds"
        )
        if reference is None:
            raise ManifestError(
                f"track {track_id} supplies offsetSeconds without referenceTrackId"
            )
    return {
        "referenceTrackId": reference,
        "offsetSeconds": round(offset, 3) if offset is not None else None,
        "status": "resolved" if offset is not None else "unresolved",
    }


def apply_session_offsets(
    tracks: list[dict[str, Any]], *, primary_track_id: str | None
) -> None:
    by_id = {str(track["trackId"]): track for track in tracks}
    memo: dict[str, float | None] = {}

    def resolve(track_id: str, active: tuple[str, ...] = ()) -> float | None:
        if track_id in memo:
            return memo[track_id]
        if track_id in active:
            cycle = " -> ".join((*active, track_id))
            raise ManifestError(f"alignment references contain a cycle: {cycle}")
        if track_id == primary_track_id:
            memo[track_id] = 0.0
            return 0.0

        alignment = by_id[track_id]["alignment"]
        reference = alignment["referenceTrackId"]
        if reference is None:
            memo[track_id] = None
            return None
        reference_offset = resolve(str(reference), (*active, track_id))
        relative_offset = alignment["offsetSeconds"]
        if reference_offset is None or relative_offset is None:
            memo[track_id] = None
            return None
        memo[track_id] = reference_offset + float(relative_offset)
        return memo[track_id]

    for track in tracks:
        session_offset = resolve(str(track["trackId"]))
        track["sessionOffsetSeconds"] = (
            round(session_offset, 3) if session_offset is not None else None
        )
        for part in track["parts"]:
            part["sessionStartSeconds"] = (
                round(session_offset + float(part["trackStartSeconds"]), 3)
                if session_offset is not None
                else None
            )


def reject_unknown_keys(
    value: dict[str, Any], allowed: set[str], label: str
) -> None:
    unknown = sorted(str(key) for key in value if key not in allowed)
    if unknown:
        raise ManifestError(f"{label} contains unknown fields: {unknown}")


def required_text(value: Any, label: str) -> str:
    text = str(value).strip() if value is not None else ""
    if not text:
        raise ManifestError(f"{label} is required")
    return text


def optional_text(value: Any, label: str) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        raise ManifestError(f"{label} cannot be blank")
    return text


def parse_session_number(value: Any) -> int:
    session_number = parse_positive_int(value, "sessionNumber", allow_zero=True)
    return session_number


def parse_positive_int(value: Any, label: str, *, allow_zero: bool = False) -> int:
    if isinstance(value, bool):
        raise ManifestError(f"{label} must be an integer")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ManifestError(f"{label} must be an integer") from exc
    if str(parsed) != str(value).strip() and not isinstance(value, int):
        raise ManifestError(f"{label} must be an integer")
    minimum = 0 if allow_zero else 1
    if parsed < minimum:
        raise ManifestError(f"{label} must be at least {minimum}")
    return parsed


def parse_nonnegative_number(value: Any, label: str) -> float:
    parsed = parse_finite_number(value, label)
    if parsed < 0:
        raise ManifestError(f"{label} cannot be negative")
    return parsed


def parse_finite_number(value: Any, label: str) -> float:
    if isinstance(value, bool):
        raise ManifestError(f"{label} must be a number")
    try:
        parsed = float(value)
    except (TypeError, ValueError) as exc:
        raise ManifestError(f"{label} must be a number") from exc
    if not math.isfinite(parsed):
        raise ManifestError(f"{label} must be finite")
    return parsed


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw_temp = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    os.close(descriptor)
    temp_path = Path(raw_temp)
    try:
        temp_path.write_text(content, encoding="utf-8")
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())

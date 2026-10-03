#!/usr/bin/env python3

"""Validate and preview an approved recap-scene grouping."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "beat-annotator" / "scripts"))
from review_timeline import check_current


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate recap scene groups against finalized beats and facts.")
    parser.add_argument("--beats-json", type=Path, required=True, help="Finalized beats JSON path.")
    parser.add_argument("--beat-facts-json", type=Path, required=True, help="Finalized beat-facts JSON path.")
    parser.add_argument("--recap-scenes-json", type=Path, required=True, help="Proposed or approved recap-scenes JSON path.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for the recap-scenes preview.")
    parser.add_argument("--file-prefix", type=str, required=True, help="Stable session bundle prefix.")
    parser.add_argument("--validate-only", action="store_true", help="Validate without rewriting the preview.")
    parser.add_argument("--transcript", type=Path, help="Cleaned source for scene elapsed times.")
    parser.add_argument("--timeline-review", type=Path, help="Current chronology review for the transition table.")
    parser.add_argument("--require-review-fields", action="store_true", help="Require overview and transitionToNext on each scene.")
    parser.add_argument("--record-approval", help="Record explicit human approval of the displayed proposal; quote the decision.")
    parser.add_argument("--require-approval", action="store_true", help="Require a saved approval matching this proposal and its inputs.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    beats_path = args.beats_json.expanduser().resolve()
    beat_facts_path = args.beat_facts_json.expanduser().resolve()
    recap_scenes_path = args.recap_scenes_json.expanduser().resolve()
    for path, argument in (
        (beats_path, "--beats-json"),
        (beat_facts_path, "--beat-facts-json"),
        (recap_scenes_path, "--recap-scenes-json"),
    ):
        assert_not_in_sources_dir(path, argument)

    beats_payload = read_json_mapping(beats_path)
    facts_payload = read_json_mapping(beat_facts_path)
    scenes_payload = read_json_mapping(recap_scenes_path)
    beats = parse_beats(beats_payload)
    facts = parse_facts(facts_payload)
    errors = validate_recap_scenes(scenes_payload, beats, facts)
    if not errors and (args.require_review_fields or args.record_approval or args.require_approval):
        for scene in scenes_payload.get("scenes", []):
            for field in ("overview", "transitionToNext"):
                if not normalize_optional_string(scene.get(field)):
                    errors.append(f"{scene.get('sceneId')}: missing {field}.")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    timeline = read_json_mapping(args.timeline_review) if args.timeline_review else None
    if timeline:
        check_current(timeline)
        for key, path in (("beats", beats_path), ("facts", beat_facts_path), ("transcript", args.transcript)):
            if path is None or fingerprint_file(path) != timeline["inputs"][key]["sha256"]:
                raise SystemExit(f"Timeline review does not match supplied {key}.")
        if timeline.get("needsHumanInput"):
            raise SystemExit("Resolve the chronology review before proposing recap scenes.")
    if args.require_review_fields or args.record_approval or args.require_approval:
        if timeline is None or args.transcript is None:
            raise SystemExit("The full scene review requires --transcript and --timeline-review.")
    rows = read_timed_source(args.transcript) if args.transcript else []
    approval_path = args.output_dir.expanduser().resolve() / f"{args.file_prefix}-scene-approval.json"
    current = proposal_fingerprint(scenes_payload, beats_payload, facts_payload, timeline, rows)
    if args.require_approval:
        approval = read_json_mapping(approval_path) if approval_path.exists() else {}
        if approval.get("proposalSha256") != current or not normalize_optional_string(approval.get("decision")):
            raise SystemExit("The displayed scene proposal needs explicit human approval.")
    if args.record_approval:
        if not args.record_approval.strip():
            raise SystemExit("Approval must contain the user's explicit decision.")
        approval_path.parent.mkdir(parents=True, exist_ok=True)
        approval_path.write_text(json.dumps({"proposalSha256": current, "decision": args.record_approval}, indent=2) + "\n")

    if not args.validate_only:
        output_dir = args.output_dir.expanduser().resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        file_prefix = args.file_prefix.strip()
        if not file_prefix:
            raise SystemExit("--file-prefix must be non-empty.")
        preview_path = output_dir / f"{file_prefix}-recap-scenes-preview.md"
        preview_path.write_text(render_preview(scenes_payload, beats, facts, rows, timeline), encoding="utf-8")
        print(f"Wrote {preview_path}")

    print(f"Validated {recap_scenes_path}")
    return 0


def read_json_mapping(path: Path) -> Dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit(f"Expected a JSON object in {path}")
    return payload


def parse_beats(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    raw_beats = payload.get("beats")
    if not isinstance(raw_beats, list) or not raw_beats:
        raise SystemExit("Beat JSON must contain a non-empty 'beats' list.")
    beats: List[Dict[str, Any]] = []
    for raw in raw_beats:
        if not isinstance(raw, dict):
            raise SystemExit("Each beat must be an object.")
        beat_id = normalize_optional_string(raw.get("beatId"))
        title = normalize_optional_string(raw.get("title"))
        if beat_id is None or title is None:
            raise SystemExit("Each beat must contain beatId and title.")
        beats.append({**raw, "beatId": beat_id, "title": title})
    return beats


def parse_facts(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    raw_facts = payload.get("facts")
    if not isinstance(raw_facts, list) or not raw_facts:
        raise SystemExit("Beat-facts JSON must contain a non-empty 'facts' list.")
    return [fact for fact in raw_facts if isinstance(fact, dict)]


def validate_recap_scenes(
    payload: Dict[str, Any],
    beats: Sequence[Dict[str, Any]],
    facts: Sequence[Dict[str, Any]],
) -> List[str]:
    errors: List[str] = []
    if normalize_optional_string(payload.get("schemaVersion")) != "1.0":
        errors.append("recap-scenes.json schemaVersion must be '1.0'.")

    scenes = payload.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        return [*errors, "recap-scenes.json must contain a non-empty 'scenes' list."]

    expected_beat_ids = [str(beat["beatId"]) for beat in beats]
    fact_beat_ids = [normalize_optional_string(fact.get("beatId")) for fact in facts]
    if fact_beat_ids != expected_beat_ids:
        errors.append("Beat-facts order/content does not match beats.json.")

    flattened: List[str] = []
    for index, raw_scene in enumerate(scenes, start=1):
        label = f"scene #{index}"
        if not isinstance(raw_scene, dict):
            errors.append(f"{label} must be an object.")
            continue
        expected_scene_id = f"scene-{index:03d}"
        if normalize_optional_string(raw_scene.get("sceneId")) != expected_scene_id:
            errors.append(f"{label} sceneId must be {expected_scene_id}.")
        if normalize_optional_string(raw_scene.get("title")) is None:
            errors.append(f"{expected_scene_id} must include a title.")
        if normalize_optional_string(raw_scene.get("rationale")) is None:
            errors.append(f"{expected_scene_id} must include a concise rationale.")
        beat_ids = raw_scene.get("beatIds")
        if not isinstance(beat_ids, list) or not beat_ids:
            errors.append(f"{expected_scene_id} must include one or more beatIds.")
            continue
        normalized_ids: List[str] = []
        for beat_id in beat_ids:
            normalized = normalize_optional_string(beat_id)
            if normalized is None:
                errors.append(f"{expected_scene_id} contains an empty beatId.")
                continue
            normalized_ids.append(normalized)
        if len(normalized_ids) != len(set(normalized_ids)):
            errors.append(f"{expected_scene_id} repeats a beatId.")
        flattened.extend(normalized_ids)

    if flattened != expected_beat_ids:
        errors.append(
            "Scene beatIds must cover every beat exactly once in original order; "
            f"expected {', '.join(expected_beat_ids)}, got {', '.join(flattened) or 'none'}."
        )
    return errors


def scene_groups(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [
        {
            "sceneId": str(scene["sceneId"]),
            "title": str(scene["title"]).strip(),
            "rationale": str(scene["rationale"]).strip(),
            "beatIds": [str(beat_id).strip() for beat_id in scene["beatIds"]],
            "overview": str(scene.get("overview", "")).strip(),
            "transitionToNext": str(scene.get("transitionToNext", "")).strip(),
        }
        for scene in payload["scenes"]
    ]


def render_preview(
    scenes_payload: Dict[str, Any],
    beats: Sequence[Dict[str, Any]],
    facts: Sequence[Dict[str, Any]],
    rows: Sequence[Dict[str, Any]] = (),
    timeline: Dict[str, Any] | None = None,
) -> str:
    beat_by_id = {str(beat["beatId"]): beat for beat in beats}
    fact_by_id = {str(fact.get("beatId")): fact for fact in facts}
    groups = scene_groups(scenes_payload)
    lines = [
        "# Recap Scene Proposal",
        "",
        f"- Scene Count: {len(groups)}",
        f"- Beat Coverage: {sum(len(group['beatIds']) for group in groups)}/{len(beats)}",
        "",
    ]
    lines.extend(["| Scene name | Beats covered | Time in play | Brief overview | Transition to next scene |",
                  "|---|---|---|---|---|"])
    for group in groups:
        cells = [group["title"], ", ".join(group["beatIds"]), scene_duration(group, beat_by_id, rows),
                 group["overview"] or "Overview not supplied", group["transitionToNext"] or "Transition not supplied"]
        lines.append("| " + " | ".join(table_cell(cell) for cell in cells) + " |")
    lines.extend(["", "Time in play is elapsed transcript time, including pauses; unavailable timing is not estimated from line counts.", ""])
    if timeline:
        scenes_by_beat = {bid: group["title"] for group in groups for bid in group["beatIds"]}
        lines.extend(["## Date/time transitions", "", "| In-world date/time or transition | Beats | Scenes | Evidence |", "|---|---|---|---|"])
        for transition in timeline["transitions"]:
            bid = transition["beatId"]
            cells = [f"{transition['label']}: {transition.get('date') or 'date unknown'} {transition.get('time') or ''}".strip(),
                     bid, scenes_by_beat[bid], f"{transition['uid']} ({transition['basis']}): {transition['evidence']}"]
            lines.append("| " + " | ".join(table_cell(cell) for cell in cells) + " |")
        lines.append("")
    for group in groups:
        lines.extend(
            [
                f"## {group['sceneId']} | {group['title']}",
                "",
                f"- Beat IDs: {', '.join(group['beatIds'])}",
                f"- Rationale: {group['rationale']}",
                "",
                "### Beats",
                "",
            ]
        )
        for beat_id in group["beatIds"]:
            beat = beat_by_id[beat_id]
            fact = fact_by_id.get(beat_id, {})
            summary = normalize_optional_string(fact.get("shortSummary")) or "No short summary available."
            lines.append(f"- {beat_id} | {beat['title']}: {summary}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def fingerprint_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def proposal_fingerprint(*values: Any) -> str:
    return hashlib.sha256(json.dumps(values, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def table_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def read_timed_source(path: Path) -> List[Dict[str, Any]]:
    assert_not_in_sources_dir(path.resolve(), "--transcript")
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        match = re.fullmatch(r"\[(u\d{4,})(?:\s*\|([^\]]+))?\]\s*(.*)", raw)
        if not match:
            raise ValueError("Invalid cleaned source line.")
        timing = re.match(r"\s*(\d+(?::\d+){0,2}(?:\.\d+)?)\s*-\s*(\d+(?::\d+){0,2}(?:\.\d+)?)\s*(?:\||$)", match[2] or "")
        def seconds(value: str) -> float:
            parts = [float(part) for part in value.split(":")]
            if (len(parts) > 1 and parts[-1] >= 60) or (len(parts) == 3 and parts[1] >= 60):
                raise ValueError("Invalid transcript timestamp.")
            return sum(part * 60 ** index for index, part in enumerate(reversed(parts)))
        rows.append({"uid": match[1], "raw": raw, "start": seconds(timing[1]) if timing else None,
                     "end": seconds(timing[2]) if timing else None})
    return rows


def scene_duration(group: dict, beats: dict, rows: Sequence[dict]) -> str:
    if not rows:
        return "Unavailable (no transcript timestamps)"
    positions = {row["uid"]: i for i, row in enumerate(rows)}
    start_uid = beats[group["beatIds"][0]].get("startUid")
    end_uid = beats[group["beatIds"][-1]].get("endUid")
    if start_uid not in positions or end_uid not in positions or positions[start_uid] > positions[end_uid]:
        return "Unavailable (missing source range)"
    selected = rows[positions[start_uid]:positions[end_uid] + 1]
    if any(row["start"] is None or row["end"] is None for row in selected):
        return "Unavailable (no transcript timestamps)"
    if any(row["end"] < row["start"] for row in selected) or any(b["start"] < a["start"] for a, b in zip(selected, selected[1:])):
        return "Unavailable (discontinuous timestamps)"
    first, last = selected[0]["start"], max(row["end"] for row in selected)
    if last <= first:
        return "Unavailable (no usable transcript timestamps)"
    def clock(seconds: float) -> str:
        whole = int(seconds)
        return f"{whole // 3600:02}:{whole // 60 % 60:02}:{whole % 60:02}"
    return f"{clock(first)}–{clock(last)} ({(last - first) / 60:.1f} min)"


def assert_not_in_sources_dir(path: Path, arg_name: str) -> None:
    if "sources" in path.parts:
        raise SystemExit(f"{arg_name} must not point inside a bundle 'sources' directory: {path}")


def normalize_optional_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


if __name__ == "__main__":
    raise SystemExit(main())

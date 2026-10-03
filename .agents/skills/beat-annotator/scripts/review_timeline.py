#!/usr/bin/env python3
"""Check an agent's source-based chronology without editing session dates."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path

import yaml


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_records(paths: dict[str, Path]) -> dict:
    return {key: {"path": str(path.resolve()), "sha256": sha256(path)} for key, path in paths.items()}


def check_current(report: dict) -> None:
    if not report.get("inputs"):
        raise ValueError("Timeline review has no input fingerprints; regenerate it.")
    for key, record in report["inputs"].items():
        if sha256(Path(record["path"])) != record["sha256"]:
            raise ValueError(f"Timeline review is stale: {key} changed.")


def optional_date(value) -> str | None:
    if value is None or not str(value).strip():
        return None
    return date.fromisoformat(str(value)).isoformat()


def read_source(path: Path) -> list[dict]:
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        match = re.fullmatch(r"\[(u\d{4,})(?:\s*\|[^\]]+)?\]\s*(.*)", raw)
        if not match:
            raise ValueError("Invalid prepared source line.")
        rows.append({"uid": match[1], "text": match[2], "raw": raw})
    if not rows or len({row["uid"] for row in rows}) != len(rows):
        raise ValueError("Source must contain distinct line IDs.")
    return rows


def review_timeline(session: dict, beats: list[dict], facts: list[dict], evidence: dict, rows: list[dict]) -> dict:
    """Checks are mechanical; the agent supplies actual rests, transitions, and meaning."""
    if not beats or [b["beatId"] for b in beats] != [f["beatId"] for f in facts]:
        raise ValueError("Facts must cover all beats in order.")
    positions = {row["uid"]: i for i, row in enumerate(rows)}
    by_uid = {}
    for beat in beats:
        start, end = positions[beat["startUid"]], positions[beat["endUid"]]
        for row in rows[start:end + 1]:
            if row["uid"] in by_uid:
                raise ValueError("Overlapping beat ranges.")
            by_uid[row["uid"]] = beat
    if set(by_uid) != set(positions):
        raise ValueError("Beat ranges do not cover the source.")
    transitions = evidence.get("transitions", [])
    if not transitions or transitions[0].get("uid") != rows[0]["uid"]:
        raise ValueError("Transitions must begin with session start at the first source UID.")
    issues = []

    def flag(key: str, detail: str, kind: str = "chronology"):
        issues.append({"key": key, "kind": kind, "detail": detail})

    last_position = -1
    last_date = None
    checked_transitions = []
    for index, transition in enumerate(transitions):
        uid = transition.get("uid")
        if uid not in positions or positions[uid] < last_position:
            raise ValueError("Transitions must reference source UIDs in order.")
        if transition.get("basis") not in {"explicit", "inferred", "unknown"} or not str(transition.get("evidence", "")).strip():
            raise ValueError("Each transition needs evidence and an explicit/inferred/unknown basis.")
        current = optional_date(transition.get("date"))
        if current and last_date and current < last_date:
            flag(f"transition:{index}:backwards", f"At {uid}, the date moves backwards from {last_date} to {current}.")
        beat = by_uid[uid]
        start, end = optional_date(beat.get("dateStart")), optional_date(beat.get("dateEnd")) or optional_date(beat.get("dateStart"))
        if current and start and end and not start <= current <= end:
            flag(f"transition:{index}:beat-date", f"At {uid}, {current} disagrees with {beat['beatId']}'s {start}–{end}.")
        checked_transitions.append({**transition, "date": current, "beatId": beat["beatId"],
                                    "sourceText": rows[positions[uid]]["text"],
                                    "label": transition.get("label") or ("Session start" if index == 0 else "Transition")})
        last_position = positions[uid]
        last_date = current or last_date

    inferred_start = optional_date(evidence.get("inferredStart"))
    inferred_end = optional_date(evidence.get("inferredEnd"))
    for label, inferred, endpoint in (("start", inferred_start, checked_transitions[0]["date"]),
                                       ("end", inferred_end, checked_transitions[-1]["date"])):
        if inferred != endpoint:
            flag(f"evidence:{label}", f"Inferred {label} {inferred} disagrees with the transition record {endpoint}.")
    if inferred_start and inferred_end and inferred_end < inferred_start:
        flag("evidence:span", "The inferred session end precedes its start.")
    proposals = []
    yaml_start, yaml_end = optional_date(session.get("drStart")), optional_date(session.get("drEnd"))
    if yaml_start and yaml_end and yaml_end < yaml_start:
        flag("yaml:range", f"YAML drEnd {yaml_end} precedes drStart {yaml_start}.")
    for field, inferred in (("drStart", inferred_start), ("drEnd", inferred_end)):
        current = optional_date(session.get(field))
        if inferred and current != inferred:
            proposals.append({"field": field, "current": current, "proposed": inferred})
            flag(f"yaml:{field}", f"{field}: {current or 'blank'} → proposed {inferred}; requires user approval.", "yaml-change")

    previous = None
    for index, (beat, fact) in enumerate(zip(beats, facts)):
        bid = beat["beatId"]
        start = optional_date(beat.get("dateStart"))
        end = optional_date(beat.get("dateEnd")) or start
        for field in ("dateStart", "dateEnd", "timeWindow"):
            if (str(beat.get(field) or "")) != (str(fact.get(field) or "")):
                flag(f"{bid}:{field}", f"{bid}: {field} differs between beats and facts.")
        if start and end and end < start:
            flag(f"{bid}:range", f"{bid}: end precedes start.")
        if start and previous and (date.fromisoformat(start) - date.fromisoformat(previous)).days not in (0, 1):
            flag(f"{bid}:sequence", f"{bid}: {previous} → {start} needs an explanation from the source.")
        if index == 0 and start != inferred_start:
            flag("beats:start", f"First beat starts {start}; source review infers {inferred_start}.")
        if index == len(beats) - 1 and end != inferred_end:
            flag("beats:end", f"Final beat ends {end}; source review infers {inferred_end}.")
        for field, uid, assigned in (("start", beat["startUid"], start), ("end", beat["endUid"], end)):
            active = [t for t in checked_transitions if positions[t["uid"]] <= positions[uid]][-1]
            if assigned and active["date"] and assigned != active["date"]:
                flag(f"{bid}:transition-{field}", f"{bid} {field} is {assigned}, but the transition record at {uid} is {active['date']}.")
        previous = end

    for index, issue in enumerate(evidence.get("issues", [])):
        if not issue.get("detail") or not issue.get("evidence"):
            raise ValueError("Agent-reported issues need detail and evidence.")
        flag(f"source:{index}", f"{issue['detail']} Evidence: {issue['evidence']}")
    resolutions = evidence.get("resolutions", {})
    keys = {issue["key"] for issue in issues}
    if set(resolutions) - keys:
        raise ValueError("Remove stale resolutions for issues that no longer exist.")
    for issue in issues:
        resolution = resolutions.get(issue["key"])
        if resolution:
            if resolution.get("by") not in {"source", "human"} or not resolution.get("reason", "").strip():
                raise ValueError("Resolution needs by=source|human and a specific reason.")
            if issue["kind"] == "yaml-change" and resolution["by"] != "human":
                raise ValueError("Only the user can accept keeping discrepant or blank YAML dates.")
            issue["resolution"] = resolution
    return {"schemaVersion": 1, "inferredStart": inferred_start, "inferredEnd": inferred_end,
            "proposedYamlChanges": proposals, "issues": issues,
            "needsHumanInput": any("resolution" not in item for item in issues),
            "transitions": checked_transitions}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ("session", "beats-json", "beat-facts-json", "transcript", "evidence-json", "output"):
        parser.add_argument("--" + field, type=Path, required=True)
    args = parser.parse_args()
    paths = {"session": args.session, "beats": args.beats_json, "facts": args.beat_facts_json,
             "transcript": args.transcript, "evidence": args.evidence_json}
    if any("sources" in path.resolve().parts for path in paths.values()):
        raise ValueError("Chronology review must use cleaned bundle artifacts, not sources/.")
    report = review_timeline(yaml.safe_load(args.session.read_text()),
                            json.loads(args.beats_json.read_text())["beats"],
                            json.loads(args.beat_facts_json.read_text())["facts"],
                            json.loads(args.evidence_json.read_text()), read_source(args.transcript))
    report["inputs"] = input_records(paths)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    for issue in report["issues"]:
        print(f"{'Resolved' if 'resolution' in issue else 'Review'}: {issue['key']}: {issue['detail']}")
    print(f"Wrote {args.output}; needs human input: {report['needsHumanInput']}")
    return 2 if report["needsHumanInput"] else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(str(error))

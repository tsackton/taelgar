#!/usr/bin/env python3
"""Collect ASR issues, record tolerance, and serve an optional local audio review."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import secrets
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

import yaml

LINE = re.compile(r"^(\[(u\d{4,})\s*\|\s*([^|]+)\|\s*([^\]]+)\])(\s)(.*)$")
MARKER = re.compile(r"\[\[(.+?)\]\]")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict:
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict):
        raise ValueError(f"Expected an object: {path}")
    return result


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def seconds(value: str) -> float:
    if not re.fullmatch(r"\d+(?::\d+){0,2}(?:\.\d+)?", value.strip()):
        raise ValueError(f"Invalid transcript time: {value}")
    parts = [float(part) for part in value.strip().split(":")]
    if (len(parts) > 1 and parts[-1] >= 60) or (len(parts) == 3 and parts[1] >= 60):
        raise ValueError(f"Invalid transcript time: {value}")
    return sum(part * 60 ** index for index, part in enumerate(reversed(parts)))


def read_lines(path: Path) -> list[dict]:
    lines = []
    seen = set()
    for index, raw in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if not raw.strip():
            continue
        match = LINE.fullmatch(raw)
        if not match or match[2] in seen:
            raise ValueError(f"Invalid or duplicate transcript header at line {index + 1}")
        seen.add(match[2])
        start, end = (seconds(part) for part in match[3].strip().split("-"))
        if end < start:
            raise ValueError(f"Inverted timestamp: {match[2]}")
        lines.append(dict(uid=match[2], header=match[1], separator=match[5],
                          speaker=match[4].strip(), text=match[6], raw=raw,
                          index=index, start=start, end=end))
    return lines


def inventory(cleaned: Path, assessment: dict | None = None, decisions: dict | None = None) -> dict:
    lines = read_lines(cleaned)
    sha = digest(cleaned)
    assessment = assessment or {}
    decisions = decisions or {}
    if assessment and assessment.get("transcriptSha256") != sha:
        raise ValueError("Cleanup assessment is stale; reassess the current transcript.")
    ratings = {}
    for item in assessment.get("issues", []):
        if item["uid"] in ratings or item.get("importance") not in {"material", "incidental"} or not item.get("reason", "").strip():
            raise ValueError("Each assessed UID needs one importance and a reason.")
        ratings[item["uid"]] = item
    # Stale acceptance must never silently accept changed transcript content.
    saved = decisions.get("decisions", {}) if decisions.get("transcriptSha256") == sha else {}
    issues = []
    for index, line in enumerate(lines):
        phrases = MARKER.findall(line["text"])
        if not phrases:
            continue
        rating = ratings.pop(line["uid"], {})
        decision = saved.get(line["uid"], {})
        issues.append({**line, "phrases": phrases,
                       "importance": rating.get("importance", "material"),
                       "reason": rating.get("reason", "Unassessed unresolved meaning; assess its significance."),
                       "before": [row["raw"] for row in lines[max(0, index - 2):index]],
                       "after": [row["raw"] for row in lines[index + 1:index + 3]],
                       "accepted": decision.get("status") == "skip"})
    if ratings:
        raise ValueError(f"Assessment references unmarked or missing lines: {', '.join(ratings)}")
    pending = [item for item in issues if item["importance"] == "material" and not item["accepted"]]
    return {"schemaVersion": 1, "transcriptPath": str(cleaned.resolve()),
            "transcriptSha256": sha, "issues": issues, "pendingMaterialCount": len(pending),
            "incidentalCount": sum(item["importance"] == "incidental" for item in issues),
            "acceptedCount": sum(item["accepted"] for item in issues),
            "assessment": assessment.get("judgment", "")}


def validate_decision(item: dict) -> dict:
    if item.get("status") == "skip":
        return {"status": "skip"}
    text = item.get("text")
    if item.get("status") != "correct" or not isinstance(text, str) or not text.strip():
        raise ValueError("Provide a correction or skip this issue.")
    if any(char in text for char in "\r\n\u2028\u2029") or "[[" in text or "]]" in text:
        raise ValueError("A correction must be one transcript line without unresolved markers; use Skip if unclear.")
    return {"status": "correct", "text": text}


def save_decision(review: dict, path: Path, action: dict) -> dict:
    cleaned = Path(review["transcriptPath"])
    if digest(cleaned) != review["transcriptSha256"]:
        raise ValueError("Transcript changed since this review was built; rebuild the review.")
    value = read_json(path) if path.exists() else {
        "schemaVersion": 1, "transcriptSha256": review["transcriptSha256"], "decisions": {}}
    if value.get("transcriptSha256") != review["transcriptSha256"]:
        raise ValueError("Saved decisions belong to another transcript version.")
    valid = {item["uid"] for item in review["issues"]}
    if action.get("skipRemaining") is True:
        for uid in valid:
            value["decisions"].setdefault(uid, {"status": "skip"})
    else:
        uid = action.get("uid")
        if uid not in valid:
            raise ValueError("Unknown review issue.")
        value["decisions"][uid] = validate_decision(action)
    write_json(path, value)
    return value


def apply_decisions(review: dict, decisions_path: Path) -> int:
    cleaned = Path(review["transcriptPath"])
    decisions = read_json(decisions_path)
    current_sha = digest(cleaned)
    decision_sha = hashlib.sha256(json.dumps(decisions.get("decisions", {}), sort_keys=True).encode()).hexdigest()
    if (decisions.get("appliedSha256") == current_sha
            and decisions.get("reviewSha256") == review["transcriptSha256"]
            and decisions.get("appliedDecisionSha256") == decision_sha):
        return 0
    if current_sha != review["transcriptSha256"] or decisions.get("transcriptSha256") != current_sha:
        raise ValueError("Transcript or decisions changed since review; refusing stale corrections.")
    issues = {item["uid"]: item for item in review["issues"]}
    raw = cleaned.read_bytes().decode("utf-8").splitlines(keepends=True)
    count = 0
    for uid, decision in decisions.get("decisions", {}).items():
        if uid not in issues:
            raise ValueError(f"Unknown issue in decisions: {uid}")
        decision = validate_decision(decision)
        if decision["status"] == "correct":
            issue = issues[uid]
            line = raw[issue["index"]]
            if line.rstrip("\r\n") != issue["raw"]:
                raise ValueError(f"Review line {uid} no longer matches its transcript position.")
            ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            raw[issue["index"]] = issue["header"] + issue["separator"] + decision["text"] + ending
            count += 1
    updated = "".join(raw).encode("utf-8")
    # Preserve a recoverable snapshot before replacing the cleaned transcript.
    backup = decisions_path.with_name(decisions_path.stem + ".before-apply.md")
    if count:
        if backup.exists() and backup.read_bytes() != cleaned.read_bytes():
            raise ValueError("A different before-apply snapshot exists; use a fresh review directory.")
        backup.write_bytes(cleaned.read_bytes())
        temporary = cleaned.with_name(cleaned.name + ".cleanup-tmp")
        temporary.write_bytes(updated)
        temporary.replace(cleaned)
    decisions["reviewSha256"] = review["transcriptSha256"]
    decisions["transcriptSha256"] = digest(cleaned)
    decisions["appliedSha256"] = decisions["transcriptSha256"]
    decisions["appliedDecisionSha256"] = decision_sha
    write_json(decisions_path, decisions)
    return count


def add_clips(review: dict, mappings: list[dict], output: Path) -> None:
    """Map transcript time to recording time explicitly; do not infer chunk offsets."""
    media_scripts = Path(__file__).resolve().parents[2] / "transcribe-session" / "scripts"
    sys.path.insert(0, str(media_scripts))
    from media_tools import extract_audio_clip, prepare_clip_source, resolve_clip_backend, probe_duration
    lines = read_lines(Path(review["transcriptPath"]))
    positions = {line["uid"]: index for index, line in enumerate(lines)}
    resolved = []
    for mapping in mappings:
        first, last = positions[mapping["startUid"]], positions[mapping["endUid"]]
        offset = float(mapping.get("offsetSeconds", 0))
        audio = Path(mapping["audioPath"]).expanduser().resolve()
        if first > last or not math.isfinite(offset) or not audio.is_file():
            raise ValueError("Invalid audio mapping.")
        segment = lines[first:last + 1]
        if any(b["start"] < a["start"] for a, b in zip(segment, segment[1:])):
            raise ValueError("Audio mapping crosses a timestamp reset; supply separate mappings.")
        resolved.append((first, last, offset, audio))
    backend = resolve_clip_backend()
    prepared = {}
    durations = {}
    for issue in review["issues"]:
        index = positions[issue["uid"]]
        matches = [row for row in resolved if row[0] <= index <= row[1]]
        if len(matches) != 1:
            raise ValueError(f"Need exactly one audio mapping for {issue['uid']}.")
        first, last, offset, audio = matches[0]
        if audio not in durations:
            durations[audio] = probe_duration(audio)
        if issue["end"] + offset > durations[audio] + 0.05:
            raise ValueError(f"Audio mapping puts {issue['uid']} beyond the recording's duration.")
        start = max(0, lines[first]["start"] + offset, issue["start"] + offset - 3)
        end = min(durations[audio], max(row["end"] for row in lines[first:last + 1]) + offset, issue["end"] + offset + 3)
        if issue["start"] + offset < 0 or end <= start:
            raise ValueError(f"Audio mapping puts {issue['uid']} outside the recording.")
        if audio not in prepared:
            prepared[audio] = prepare_clip_source(audio, backend=backend, work_dir=output)
        source, clip_backend = prepared[audio]
        clip = output / f"{issue['uid']}.m4a"
        extract_audio_clip(source, clip, start_seconds=start, end_seconds=end, backend=clip_backend)
        issue["clip"] = clip.name
        issue["audioSource"] = {"path": str(audio), "start": start, "end": end}


def make_server(review_path: Path, decisions_path: Path, port: int = 0) -> ThreadingHTTPServer:
    review = read_json(review_path)
    if digest(Path(review["transcriptPath"])) != review["transcriptSha256"]:
        raise ValueError("Transcript changed or corrections were applied; rebuild before starting another review.")
    if decisions_path.exists() and read_json(decisions_path).get("transcriptSha256") != review["transcriptSha256"]:
        raise ValueError("Saved decisions belong to another transcript version.")
    token = secrets.token_urlsafe(24)
    html = (Path(__file__).resolve().parents[1] / "assets" / "cleanup-review.html").read_text(encoding="utf-8").replace("__REVIEW_TOKEN__", token).encode()
    clips = {f"/clips/{issue['uid']}": review_path.parent / issue["clip"] for issue in review["issues"] if issue.get("clip")}
    lock = threading.Lock()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def send(self, data: bytes, content_type: str, status: int = 200):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def json(self, data: dict, status: int = 200):
            self.send(json.dumps(data).encode(), "application/json", status)

        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send(html, "text/html; charset=utf-8")
            elif path == "/api/review":
                decisions = read_json(decisions_path) if decisions_path.exists() else {}
                self.json({"review": review, "decisions": decisions.get("decisions", {})})
            elif path in clips and clips[path].resolve().parent == review_path.parent.resolve():
                self.send(clips[path].read_bytes(), "audio/mp4")
            else:
                self.send_error(404)

        def do_POST(self):
            if self.path != "/api/decision" or self.headers.get("X-Review-Token") != token:
                self.send_error(403)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 100_000:
                    raise ValueError("Invalid request size.")
                action = json.loads(self.rfile.read(length))
                if not isinstance(action, dict):
                    raise ValueError("Expected a decision object.")
                with lock:
                    value = save_decision(review, decisions_path, action)
                self.json(value)
            except (ValueError, OSError, KeyError) as error:
                self.json({"error": str(error)}, 400)

    return ThreadingHTTPServer(("127.0.0.1", port), Handler)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("inventory", "accept", "prepare"):
        p = sub.add_parser(command)
        p.add_argument("--cleaned", type=Path, required=True)
        p.add_argument("--assessment", type=Path)
        p.add_argument("--decisions", type=Path)
        p.add_argument("--output", type=Path, required=command != "accept")
        if command == "accept":
            p.add_argument("--reason", required=True, help="User's explicit tolerance decision.")
        if command == "prepare":
            p.add_argument("--session", type=Path)
            p.add_argument("--audio-map", type=Path)
    for command in ("serve", "apply"):
        p = sub.add_parser(command)
        p.add_argument("--review", type=Path, required=True)
        p.add_argument("--decisions", type=Path, required=True)
        if command == "serve":
            p.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    if args.command == "serve":
        server = make_server(args.review.resolve(), args.decisions, args.port)
        print(f"Review: http://127.0.0.1:{server.server_port}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
        return 0
    if args.command == "apply":
        print(f"Applied {apply_decisions(read_json(args.review), args.decisions)} corrected lines.")
        return 0
    review = inventory(args.cleaned, read_json(args.assessment) if args.assessment else None,
                       read_json(args.decisions) if args.decisions and args.decisions.exists() else None)
    if args.command == "accept":
        if not args.decisions or not args.reason.strip():
            raise ValueError("accept needs --decisions and the user's --reason.")
        value = save_decision(review, args.decisions, {"skipRemaining": True})
        value["acceptanceReason"] = args.reason
        write_json(args.decisions, value)
    else:
        if args.command == "prepare":
            if args.output.exists():
                raise ValueError("Review output exists; resume it or use a new review directory.")
            if args.audio_map:
                mappings = read_json(args.audio_map)["recordings"]
            else:
                session = yaml.safe_load(args.session.read_text()) if args.session else {}
                if not session.get("sourceAudioPath"):
                    raise ValueError("Need a verified sourceAudioPath or an explicit --audio-map.")
                lines = read_lines(args.cleaned)
                mappings = [{"startUid": lines[0]["uid"], "endUid": lines[-1]["uid"],
                             "audioPath": session["sourceAudioPath"], "offsetSeconds": 0}]
            args.output.parent.mkdir(parents=True, exist_ok=True)
            add_clips(review, mappings, args.output.parent)
        write_json(args.output, review)
    print(f"{len(review['issues'])} unresolved lines; {review['pendingMaterialCount']} material lines awaiting a decision.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))

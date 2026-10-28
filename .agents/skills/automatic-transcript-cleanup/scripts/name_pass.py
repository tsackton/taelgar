#!/usr/bin/env python3
"""Deterministic marker inventory, logged application, reports, and selective undo.

Name decisions are supplied by an agent in a versioned plan. This program never
guesses a name and never edits text outside complete existing ASR markers.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import difflib
import fcntl
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shlex
import stat
import sys
import tempfile
from datetime import datetime, timezone
from uuid import uuid4

VERSION = "names-v1"
SCHEMA = 1
MARKER = re.compile(r"(?<!\{)\{\{([^{}\r\n]*)\}\}(?!\})")
BMARKER = re.compile(rb"(?<!\{)\{\{[^{}\r\n]*\}\}(?!\})")
HEADER = re.compile(r"^(\[(u\d+)\s*\|[^\]\r\n]*\][ \t]*)")
GROUP_KEYS = {"id", "action", "confidence", "reason", "evidence", "candidates", "markerIds", "replacements"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def inside(root, path):
    root = Path(root).resolve()
    p = Path(path)
    p = (root / p).resolve() if not p.is_absolute() else p.resolve()
    require(p.is_relative_to(root), f"Path outside vault: {path}")
    return p


def relative(root, path):
    return inside(root, path).relative_to(Path(root).resolve()).as_posix()


def transcript_path(root, path):
    p = inside(root, path)
    rel = p.relative_to(Path(root).resolve())
    require(len(rel.parts) >= 5 and rel.parts[0] == "_sessions" and p.parent.name == "cleaned", "Only _sessions/*/*/cleaned source transcripts are writable")
    require(p.name.endswith("-source-cleaned.md") or p.name == "source.cleaned.md", "Not a cleaned source transcript")
    require(p.is_file(), f"Missing transcript: {p}")
    return p


def cheap_count(path):
    """Stream bytes; no decoding, full-text read, YAML, evidence, or logs."""
    count = 0
    malformed = False
    with Path(path).open("rb") as stream:
        for line in stream:
            count += len(BMARKER.findall(line))
            rest = BMARKER.sub(b"", line)
            malformed |= b"{{" in rest or b"}}" in rest
    require(not malformed, "Malformed/nested/multiline ASR markers; leave source unchanged")
    return count


def parse(raw):
    text = raw.decode("utf-8")
    lines = text.splitlines(keepends=True)
    units, markers = {}, []
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        match = HEADER.match(line)
        require(match is not None, f"Invalid transcript header at line {index + 1}")
        header, uid = match.groups()
        require(uid not in units, f"Duplicate UID: {uid}")
        units[uid] = {"index": index, "header": header, "raw": line}
        for ordinal, span in enumerate(MARKER.finditer(line), 1):
            require(span.start() >= len(header), "Marker in transcript header")
            markers.append({"markerId": f"{uid}:m{ordinal}", "uid": uid, "ordinal": ordinal,
                            "lineNumber": index + 1, "start": span.start(), "end": span.end(),
                            "before": span.group(), "span": span.group(1)})
    return lines, units, markers


def scan(root, path):
    p = transcript_path(root, path)
    count = cheap_count(p)  # Mandatory first content operation.
    result = {"schemaVersion": SCHEMA, "passVersion": VERSION, "transcript": relative(root, p),
              "session": p.parent.parent.name, "status": "ready" if count else "skipped_no_markers",
              "transcriptSha256": None, "markerCount": count, "markers": []}
    if not count:
        return result
    raw = p.read_bytes()
    lines, _, markers = parse(raw)
    require(len(markers) == count, "Transcript changed during inventory; rescan")
    result["transcriptSha256"] = digest(raw)
    for marker in markers:
        index = marker["lineNumber"] - 1
        result["markers"].append({**marker, "line": lines[index].rstrip("\r\n"),
                                  "contextBefore": [s.rstrip("\r\n") for s in lines[max(0, index - 2):index]],
                                  "contextAfter": [s.rstrip("\r\n") for s in lines[index + 1:index + 3]]})
    return result


def keys(value, expected, label):
    require(isinstance(value, dict) and set(value) == expected, f"Unexpected/missing fields in {label}; use the documented schema")


def validate_plan(root, path, plan):
    inv = scan(root, path)
    if inv["status"] == "skipped_no_markers":
        return inv
    keys(plan, {"schemaVersion", "passVersion", "transcriptSha256", "groups"}, "plan")
    require(plan["schemaVersion"] == SCHEMA and plan["passVersion"] == VERSION, "Unsupported schema/pass version")
    require(plan["transcriptSha256"] == inv["transcriptSha256"], "Stale plan; rescan current transcript")
    require(isinstance(plan["groups"], list), "groups must be a list")
    inventory = {m["markerId"]: m for m in inv["markers"]}
    seen, group_ids, groups, changes = set(), set(), [], []
    for supplied in plan["groups"]:
        keys(supplied, GROUP_KEYS, "group")
        g = dict(supplied)
        require(isinstance(g["id"], str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", g["id"]), "Group ID must be a lowercase slug")
        require(g["id"] not in group_ids, "Duplicate group ID")
        group_ids.add(g["id"])
        require(isinstance(g["reason"], str) and bool(g["reason"].strip()), "Every group needs a reason")
        for field in ["markerIds", "candidates", "evidence"]:
            require(isinstance(g[field], list) and all(isinstance(x, str) for x in g[field]), f"{field} must be a string list")
        require(isinstance(g["replacements"], dict), "replacements must be a map")
        if g["action"] == "replace":
            require(g["confidence"] in ["high", "supported"], "Replacement confidence must be high or supported")
            require(not g["markerIds"] and g["replacements"] and not g["candidates"], "Replacement group needs replacements only")
            require(g["evidence"], "Every replacement needs source evidence")
            ids = list(g["replacements"])
        else:
            require(g["action"] in ["review", "leave"], "Unknown group action")
            require(g["confidence"] == ("unresolved" if g["action"] == "review" else "not_applicable"), "Invalid retained-group confidence")
            require(g["markerIds"] and not g["replacements"], "Retained group needs markerIds only")
            ids = g["markerIds"]
        evidence = []
        for source in g["evidence"]:
            p = inside(root, source)
            require(p.is_file(), f"Missing evidence: {source}")
            require("sources" not in p.relative_to(Path(root).resolve()).parts, "Archival sources/ inputs are not correction evidence")
            evidence.append({"path": relative(root, p), "sha256": digest(p.read_bytes())})
        g["evidence"] = evidence
        g["markerIds"] = sorted(ids, key=lambda x: (inventory.get(x, {}).get("lineNumber", 10**12), inventory.get(x, {}).get("ordinal", 0)))
        for marker_id in ids:
            require(marker_id in inventory, f"Unknown marker: {marker_id}")
            require(marker_id not in seen, f"Marker classified twice: {marker_id}")
            seen.add(marker_id)
            if g["action"] == "replace":
                after = g["replacements"][marker_id]
                require(isinstance(after, str) and after.strip() == after and bool(after), "Replacement must be nonempty plain text without edge whitespace")
                require(not any(c in after for c in "\r\n{}[]"), "Replacement cannot introduce lines, markers, links, or annotations")
                require(not any(ord(c) < 32 or ord(c) == 127 for c in after), "Replacement contains a control character")
                changes.append({**inventory[marker_id], "after": after, "group": g["id"], "confidence": g["confidence"]})
        groups.append(g)
    require(seen == set(inventory), f"Every marker needs one decision; missing: {sorted(set(inventory) - seen)}")
    p = transcript_path(root, path)
    raw = p.read_bytes()
    require(digest(raw) == inv["transcriptSha256"], "Transcript changed while validating; rescan")
    lines, units, _ = parse(raw)
    changed = {c["uid"] for c in changes}
    line_snapshots = {uid: {"before": units[uid]["raw"]} for uid in changed}
    after_lines = list(lines)
    for uid in changed:
        own = [c for c in changes if c["uid"] == uid]
        after = render_line(units[uid]["raw"], own, set())
        require(HEADER.match(after).group(1) == units[uid]["header"], "Header changed")
        after_lines[units[uid]["index"]] = after
        line_snapshots[uid]["after"] = after
    after_raw = "".join(after_lines).encode("utf-8")
    require(len(after_lines) == len(lines), "Line count changed")
    require(after_raw.count(b"{{") == inv["markerCount"] - len(changes), "Marker accounting failed")
    record = {"schemaVersion": SCHEMA, "passVersion": VERSION, "session": inv["session"], "transcript": inv["transcript"],
              "beforeSha256": inv["transcriptSha256"], "afterSha256": digest(after_raw), "markersBefore": inv["markerCount"],
              "groups": sorted(groups, key=lambda g: g["id"]), "changes": sorted(changes, key=lambda c: (c["lineNumber"], c["ordinal"])),
              "lines": line_snapshots, "undoneMarkerIds": [], "state": "preview", "pending": None, "events": []}
    return record


def render_line(before, changes, undone):
    result = before
    for c in sorted(changes, key=lambda c: c["start"], reverse=True):
        require(before[c["start"]:c["end"]] == c["before"], "Corrupt change offsets in journal")
        if c["markerId"] not in undone:
            result = result[:c["start"]] + c["after"] + result[c["end"]:]
    return result


def atomic_write(path, raw):
    path = Path(path)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
    fd, temp = tempfile.mkstemp(prefix=".name-pass-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temp, mode)
        os.replace(temp, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


@contextmanager
def transcript_lock(path):
    folder = path.parent / "cleanup-artifacts" / "automatic-transcript-cleanup"
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / ".lock").open("a+b") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def inline(value):
    return "<code>" + html.escape(str(value)).replace("|", "&#124;").replace("\n", " ") + "</code>"


def cell(value):
    return html.escape(str(value)).replace("|", "&#124;").replace("\n", " ")


def counts(record):
    undone = set(record["undoneMarkerIds"])
    active = [c for c in record["changes"] if c["markerId"] not in undone]
    return {"markersBefore": record["markersBefore"], "appliedHigh": sum(c["confidence"] == "high" for c in active),
            "appliedSupported": sum(c["confidence"] == "supported" for c in active),
            "markerOnly": sum(c["before"][2:-2] == c["after"] for c in active),
            "retainedReview": sum(len(g["markerIds"]) for g in record["groups"] if g["action"] == "review"),
            "retainedOutsideScope": sum(len(g["markerIds"]) for g in record["groups"] if g["action"] == "leave"),
            "markersAfter": record["markersBefore"] - len(active),
            "changedLines": len({c["uid"] for c in active}), "undone": len(undone)}


def render_report(record, journal=None):
    if record.get("status") == "skipped_no_markers":
        return f"{record['session']}: skipped_no_markers; no transcript, evidence, or log write.\n"
    c = counts(record)
    out = ["# Automatic transcript cleanup", "", f"Session: {inline(record['session'])}",
           f"Status: {inline(record['state'])}", f"Pass: {inline(VERSION)}", "",
           "| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |",
           "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
           f"| {c['markersBefore']} | {c['appliedHigh']} | {c['appliedSupported']} | {c['markerOnly']} | {c['retainedReview']} | {c['retainedOutsideScope']} | {c['markersAfter']} | {c['undone']} |",
           "", "Counts describe this run and its recorded reversions; other later edits are excluded.",
           "", "## Applied replacements", "",
           "| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    groups = {g["id"]: g for g in record["groups"]}
    for change in record["changes"]:
        g = groups[change["group"]]
        out.append("| " + " | ".join([inline(g["id"]), g["confidence"], inline(change["markerId"]), inline(change["before"]),
                    inline(change["after"]), cell(g["reason"]), ", ".join(inline(e["path"]) for e in g["evidence"]),
                    "yes" if change["markerId"] in record["undoneMarkerIds"] else "no"]) + " |")
    if not record["changes"]:
        out.append("| — | — | — | — | — | No replacements. | — | — |")
    out += ["", "## Name decisions left for review", "", "| Group | Markers | Before | Candidates | Reason |", "| --- | --- | --- | --- | --- |"]
    for g in record["groups"]:
        if g["action"] == "review":
            out.append("| " + " | ".join([inline(g["id"]), ", ".join(inline(x) for x in g["markerIds"]),
                       ", ".join(inline(g["retainedSpans"][x]) for x in g["markerIds"]),
                       ", ".join(inline(x) for x in g["candidates"]) or "—", cell(g["reason"])]) + " |")
    if not any(g["action"] == "review" for g in record["groups"]):
        out.append("| — | — | — | — | No name decisions remain. |")
    out += ["", "## Outside this pass", "", "| Group | Marker IDs | Reason |", "| --- | --- | --- |"]
    for g in record["groups"]:
        if g["action"] == "leave":
            out.append(f"| {inline(g['id'])} | {', '.join(inline(x) for x in g['markerIds'])} | {cell(g['reason'])} |")
    if not any(g["action"] == "leave" for g in record["groups"]):
        out.append("| — | — | No outside-scope markers. |")
    out += ["", "## Reversion", ""]
    if journal:
        out += ["Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.", "", "```text",
                f"python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal {shlex.quote(str(journal))}", "```"]
    else:
        out.append("Preview only; no journal or transcript was written.")
    out += ["", "## Provenance", "", f"Transcript: {inline(record['transcript'])}",
            f"Before SHA-256: {inline(record['beforeSha256'])}", f"Planned after SHA-256: {inline(record['afterSha256'])}",
            "", "## Downstream artifacts", "",
            "Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.", ""]
    return "\n".join(out)


def enrich_retained(root, path, record):
    _, _, markers = parse(transcript_path(root, path).read_bytes())
    lookup = {m["markerId"]: m["before"] for m in markers}
    for g in record["groups"]:
        g["retainedSpans"] = {m: lookup[m] for m in g["markerIds"]} if g["action"] != "replace" else {}
    return record


def save_journal(path, record):
    atomic_write(path, (json.dumps(record, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def save_outputs(path, record):
    # Journal is authoritative; both display files can be regenerated after a crash.
    save_journal(path, record)
    atomic_write(path.parent / "review.md", render_report(record, path).encode("utf-8"))
    diff = []
    for uid in sorted(record["lines"], key=lambda u: int(u[1:])):
        line = record["lines"][uid]
        diff += list(difflib.unified_diff([line["before"]], [line["after"]], fromfile=f"before/{uid}", tofile=f"after/{uid}"))
    atomic_write(path.parent / "changes.diff", "".join(diff).encode("utf-8"))


def check_evidence(root, record):
    for g in record["groups"]:
        for e in g["evidence"]:
            p = inside(root, e["path"])
            acceptable = {e["sha256"]}
            if e["path"] == record["transcript"]:
                acceptable.add(record["afterSha256"])
            require(p.is_file() and digest(p.read_bytes()) in acceptable, f"Evidence changed: {e['path']}")


def _apply(root, path, plan):
    record = validate_plan(root, path, plan)
    if record.get("status") == "skipped_no_markers":
        return record, None
    record = enrich_retained(root, path, record)
    p = transcript_path(root, path)
    raw = p.read_bytes()
    require(digest(raw) == record["beforeSha256"], "Stale transcript before apply")
    lines, units, _ = parse(raw)
    for uid, saved in record["lines"].items():
        lines[units[uid]["index"]] = saved["after"]
    after = "".join(lines).encode("utf-8")
    require(digest(after) == record["afterSha256"], "After fingerprint mismatch")
    check_evidence(root, record)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + "-" + uuid4().hex[:8]
    journal = p.parent / "cleanup-artifacts" / "automatic-transcript-cleanup" / run_id / "journal.json"
    journal.parent.mkdir(parents=True, exist_ok=False)
    record.update(runId=run_id, createdAt=datetime.now(timezone.utc).isoformat(), state="prepared",
                  pending={"kind": "apply", "beforeSha256": record["beforeSha256"], "afterSha256": record["afterSha256"]})
    save_outputs(journal, record)  # Write-ahead audit exists before any source mutation.
    require(digest(p.read_bytes()) == record["beforeSha256"], f"Source changed; no write. Recover journal: {journal}")
    if after != raw:
        atomic_write(p, after)
    require(digest(p.read_bytes()) == record["afterSha256"], f"Post-write mismatch; recover journal: {journal}")
    record["state"] = "applied" if record["changes"] else "reviewed_no_changes"
    record["pending"] = None
    record["events"].append({"kind": "apply", "at": datetime.now(timezone.utc).isoformat(), "sha256": record["afterSha256"]})
    save_outputs(journal, record)
    return record, journal


def apply(root, path, plan):
    # Validate before creating a lock/log directory; revalidate under the lock.
    checked = validate_plan(root, path, plan)
    if checked.get("status") == "skipped_no_markers":
        return checked, None
    with transcript_lock(transcript_path(root, path)):
        return _apply(root, path, plan)


def load_journal(root, path):
    p = inside(root, path)
    record = read_json(p)
    require(record.get("schemaVersion") == SCHEMA and record.get("passVersion") == VERSION, "Unsupported journal version")
    target = transcript_path(root, record["transcript"])
    require(p.parent.parent == target.parent / "cleanup-artifacts" / "automatic-transcript-cleanup", "Journal is not beside its transcript")
    ids = {c["markerId"] for c in record["changes"]}
    require(len(ids) == len(record["changes"]) and set(record["undoneMarkerIds"]) <= ids, "Corrupt journal IDs")
    for uid, saved in record["lines"].items():
        require(HEADER.match(saved["before"]) and HEADER.match(saved["before"]).group(2) == uid, "Corrupt journal header")
        require(saved["after"] == render_line(saved["before"], [c for c in record["changes"] if c["uid"] == uid], set()), "Corrupt journal line")
    return p, target, record


def _undo(root, journal_path, marker_ids=None):
    journal, p, record = load_journal(root, journal_path)
    require(record["pending"] is None, "Unfinished transaction; run recover first")
    require(record["state"] in ["applied", "reviewed_no_changes", "partially_reverted", "reverted"], "Journal has no completed application")
    all_ids = {c["markerId"] for c in record["changes"]}
    selected = set(marker_ids) if marker_ids else all_ids
    require(selected <= all_ids, "Unknown replacement ID for undo")
    undone = set(record["undoneMarkerIds"])
    selected -= undone
    if not selected:
        return record, journal
    raw = p.read_bytes()
    lines, units, _ = parse(raw)
    affected = {c["uid"] for c in record["changes"] if c["markerId"] in selected}
    for uid in affected:
        own = [c for c in record["changes"] if c["uid"] == uid]
        expected = render_line(record["lines"][uid]["before"], own, undone)
        require(uid in units and units[uid]["raw"] == expected, f"Undo conflict at {uid}; later edits preserved; no selected change reverted")
        lines[units[uid]["index"]] = render_line(record["lines"][uid]["before"], own, undone | selected)
    after = "".join(lines).encode("utf-8")
    record["pending"] = {"kind": "undo", "markerIds": sorted(selected), "beforeSha256": digest(raw), "afterSha256": digest(after)}
    save_journal(journal, record)
    require(digest(p.read_bytes()) == digest(raw), "Source changed before undo; run recover")
    atomic_write(p, after)
    require(digest(p.read_bytes()) == digest(after), "Post-undo mismatch; run recover")
    record["undoneMarkerIds"] = sorted(undone | selected)
    record["state"] = "reverted" if set(record["undoneMarkerIds"]) == all_ids else "partially_reverted"
    record["events"].append({**record["pending"], "at": datetime.now(timezone.utc).isoformat()})
    record["pending"] = None
    save_outputs(journal, record)
    return record, journal


def undo(root, journal_path, marker_ids=None):
    _, target, _ = load_journal(root, journal_path)
    with transcript_lock(target):
        return _undo(root, journal_path, marker_ids)


def _recover(root, journal_path):
    journal, target, record = load_journal(root, journal_path)
    pending = record["pending"]
    if pending:
        current = digest(target.read_bytes())
        require(current in [pending["beforeSha256"], pending["afterSha256"]], "Recovery conflict; transcript and audit preserved for manual inspection")
        completed = current == pending["afterSha256"]
        if pending["kind"] == "apply":
            record["state"] = ("applied" if record["changes"] else "reviewed_no_changes") if completed else "aborted"
        elif completed:
            record["undoneMarkerIds"] = sorted(set(record["undoneMarkerIds"]) | set(pending["markerIds"]))
            record["state"] = "reverted" if len(record["undoneMarkerIds"]) == len(record["changes"]) else "partially_reverted"
        record["events"].append({**pending, "kind": "recovered-" + pending["kind"], "completed": completed, "at": datetime.now(timezone.utc).isoformat()})
        record["pending"] = None
    save_outputs(journal, record)
    return record, journal


def recover(root, journal_path):
    _, target, _ = load_journal(root, journal_path)
    with transcript_lock(target):
        return _recover(root, journal_path)


def batch(root, campaign_root):
    campaign = inside(root, campaign_root)
    require(campaign.is_dir() and campaign.parent == Path(root).resolve() / "_sessions", "Choose one _sessions campaign directory")
    rows = []
    for session in sorted(p for p in campaign.iterdir() if p.is_dir() and not p.name.startswith((".", "_"))):
        choices = sorted((session / "cleaned").glob("*-source-cleaned.md"))
        alternate = session / "cleaned" / "source.cleaned.md"
        if alternate.is_file():
            choices.append(alternate)
        row = {"session": session.name, "transcript": None, "status": "missing_cleaned", "markers": None, "journal": None}
        if len(choices) > 1:
            row["status"] = "ambiguous_cleaned"
        elif choices:
            p = transcript_path(root, choices[0])
            row["transcript"] = relative(root, p)
            try:
                row["markers"] = cheap_count(p)
                row["status"] = "ready" if row["markers"] else "skipped_no_markers"
                logs = sorted((p.parent / "cleanup-artifacts" / "automatic-transcript-cleanup").glob("*/journal.json"))
                if row["markers"] and logs:
                    _, _, latest = load_journal(root, logs[-1])
                    if latest["pending"]:
                        row["status"] = "recovery_required"
                    elif latest["state"] in ["applied", "reviewed_no_changes"] and digest(p.read_bytes()) == latest["afterSha256"]:
                        try:
                            check_evidence(root, latest)
                            row["status"] = "reviewed_current"
                        except ValueError:
                            pass
                    row["journal"] = relative(root, logs[-1])
            except (ValueError, KeyError, json.JSONDecodeError) as error:
                row["status"], row["error"] = "blocked", str(error)
        rows.append(row)
    return {"schemaVersion": SCHEMA, "passVersion": VERSION, "sessions": rows}


def render_batch(root, manifest, journals):
    require(manifest.get("schemaVersion") == SCHEMA and manifest.get("passVersion") == VERSION, "Unsupported manifest version")
    rows = manifest["sessions"]
    known = {row["session"]: row for row in rows}
    require(len(known) == len(rows), "Duplicate manifest sessions")
    selected = {}
    for path in journals:
        journal, _, record = load_journal(root, path)
        session = record["session"]
        require(session in known and known[session]["transcript"] == record["transcript"], "Journal outside selected manifest scope")
        require(session not in selected, "Supply only one invocation journal per session")
        require(record["pending"] is None and record["state"] in ["applied", "reviewed_no_changes"], "Only completed application journals belong in batch totals")
        selected[session] = (journal, record)
    columns = ["markersBefore", "appliedHigh", "appliedSupported", "retainedReview", "retainedOutsideScope", "markersAfter"]
    totals = dict.fromkeys(columns, 0)
    out = ["| Session | Status | Markers before | High | Supported | Name review | Outside scope | Markers after | Log |",
           "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |"]
    for row in rows:
        session = row["session"]
        if session in selected:
            journal, record = selected[session]
            c = counts(record)
            for column in columns:
                totals[column] += c[column]
            values = [str(c[column]) for column in columns]
            status = record["state"]
            log = (journal.parent / "review.md").as_posix()
            link = f"[review log](<{log}>)"
        else:
            status = row["status"]
            values = ["0"] * 6 if status == "skipped_no_markers" else ["—"] * 6
            link = "—"
        out.append("| " + " | ".join([inline(session), cell(status), *values, link]) + " |")
    out.append("| Total | evaluated this invocation | " + " | ".join(str(totals[column]) for column in columns) + " | — |")
    out += ["", "Totals include only supplied completed run journals; resumed sessions are not counted again. Retained ordinary wording is outside this pass, not a request for human review.", ""]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["scan", "batch", "summary", "preview", "apply", "report", "undo", "recover"])
    parser.add_argument("--vault-root", type=Path, default=Path.cwd())
    parser.add_argument("--transcript", type=Path)
    parser.add_argument("--campaign-root", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--journal", type=Path)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--journals", nargs="*", type=Path, default=[])
    parser.add_argument("--marker-id", action="append")
    args = parser.parse_args()
    root = args.vault_root.resolve()
    try:
        if args.command == "summary":
            require(args.manifest is not None or args.campaign_root is not None, "--manifest or --campaign-root required")
            manifest = read_json(args.manifest) if args.manifest else batch(root, args.campaign_root)
            print(render_batch(root, manifest, args.journals), end="")
        elif args.command == "batch":
            require(args.campaign_root is not None, "--campaign-root required")
            result = batch(root, args.campaign_root)
            print(json.dumps(result, ensure_ascii=False, indent=2))
        elif args.command == "scan":
            require(args.transcript is not None, "--transcript required")
            print(json.dumps(scan(root, args.transcript), ensure_ascii=False, indent=2))
        elif args.command in ["preview", "apply"]:
            require(args.transcript is not None, "--transcript required")
            # The zero-marker guard precedes even opening a supplied plan.
            inv = scan(root, args.transcript)
            if inv["status"] == "skipped_no_markers":
                print(render_report(inv), end="")
                return 0
            require(args.plan is not None, "--plan required")
            plan = read_json(args.plan)
            if args.command == "apply":
                record, journal = apply(root, args.transcript, plan)
            else:
                record = enrich_retained(root, args.transcript, validate_plan(root, args.transcript, plan))
                journal = None
            print(render_report(record, journal), end="")
        else:
            require(args.journal is not None, "--journal required")
            if args.command == "undo":
                record, journal = undo(root, args.journal, args.marker_id)
            elif args.command == "recover":
                record, journal = recover(root, args.journal)
            else:
                journal, _, record = load_journal(root, args.journal)
            print(render_report(record, journal), end="")
        return 0
    except (ValueError, OSError, UnicodeError, KeyError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

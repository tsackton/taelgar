#!/usr/bin/env python3
"""Maintain a contiguous reviewed-day checkpoint for a Discord channel."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


def valid_day(value: str) -> date:
    try:
        day = date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc
    if day.isoformat() != value:
        raise argparse.ArgumentTypeError("Use YYYY-MM-DD")
    return day


def read_state(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        state = json.load(stream)
    if state.get("version") != 1 or state.get("timezone") != "America/New_York":
        raise ValueError("Unsupported checkpoint format or timezone")
    valid_day(state["first_day"])
    if state.get("last_complete_day") is not None:
        valid_day(state["last_complete_day"])
    if not isinstance(state.get("days"), dict):
        raise ValueError("Checkpoint has no days map")
    return state


def write_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    try:
        with temporary.open("w", encoding="utf-8", newline="\n") as stream:
            json.dump(state, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    sub = parser.add_subparsers(dest="action", required=True)

    initialize = sub.add_parser("init", help="Begin a new review range")
    initialize.add_argument("--first-day", type=valid_day, required=True)
    initialize.add_argument("--channel-id", required=True)

    sub.add_parser("show", help="Show checkpoint and next day")

    advance = sub.add_parser("advance", help="Mark one completely reviewed day")
    advance.add_argument("--day", type=valid_day, required=True)
    advance.add_argument("--status", choices=("written", "no-taelgar", "no-relevant"), required=True)
    advance.add_argument("--source-count", type=int, required=True)
    advance.add_argument("--retained-count", type=int, required=True)
    advance.add_argument("--note", action="append", default=[])

    args = parser.parse_args()
    path = args.state.resolve()

    if args.action == "init":
        if path.exists():
            parser.error("Checkpoint already exists; use a separate path for a re-export")
        if not args.channel_id.isdecimal():
            parser.error("Channel ID must contain digits only")
        state = {
            "version": 1,
            "channel_id": args.channel_id,
            "timezone": "America/New_York",
            "first_day": args.first_day.isoformat(),
            "last_complete_day": None,
            "days": {},
        }
        write_state(path, state)
    else:
        state = read_state(path)

    if args.action == "advance":
        last = state["last_complete_day"]
        expected = valid_day(last) + timedelta(days=1) if last else valid_day(state["first_day"])
        if args.day != expected:
            parser.error(f"Next day must be {expected.isoformat()}")
        if args.source_count < 0 or not 0 <= args.retained_count <= args.source_count:
            parser.error("Counts must satisfy 0 <= retained <= source")
        if args.status == "written" and (not args.note or args.retained_count == 0):
            parser.error("A written day needs a note and retained messages")
        if args.status in ("no-taelgar", "no-relevant") and (args.note or args.retained_count):
            parser.error("A skipped day must have no note or retained messages")
        state["days"][args.day.isoformat()] = {
            "status": args.status,
            "source_count": args.source_count,
            "retained_count": args.retained_count,
            "notes": args.note,
            "reviewed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        state["last_complete_day"] = args.day.isoformat()
        write_state(path, state)

    last = state["last_complete_day"]
    next_day = valid_day(last) + timedelta(days=1) if last else valid_day(state["first_day"])
    print(f"last_complete_day: {last or '(none)'}")
    print(f"next_day: {next_day.isoformat()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

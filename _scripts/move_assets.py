#!/usr/bin/env python3
"""Validate a potential-moves JSON file; move its selected entries with --apply.

The default is a dry run. Keep only the approved entries in the moves array;
never modify an entry's evidence or destination. Held entries are not executable.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil

from find_misplaced_images import EXCLUDED_ASSET_DIRS, SCHEMA_VERSION, digest_file, encoded, outside_scan, scan


def validate_plan(plan: dict, *, snapshot: dict | None = None) -> tuple[Path, list[dict]]:
    if plan.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError("Unsupported move-plan schema")
    policy = plan["policy"]
    if policy["excludedAssetDirs"] != list(EXCLUDED_ASSET_DIRS):
        raise ValueError("The plan's exclusions differ from the current scanner")
    vault = Path(plan["vault"]).resolve()
    fresh = scan(vault, media=policy["media"], consumer_roots=[Path(p) for p in policy["consumerRoots"]], state=snapshot)
    current = {move["source"]: move for move in fresh["moves"]}
    selected = plan["moves"]
    if not isinstance(selected, list) or any(not isinstance(move, dict) for move in selected):
        raise ValueError("moves must be a list of move entries")
    if len({move["source"] for move in selected}) != len(selected):
        raise ValueError("Duplicate source in move plan")
    for move in selected:
        if current.get(move["source"]) != move:
            raise ValueError(f"Stale or unsafe move: {move['source']}. Re-scan and review a fresh proposal.")
        for relative in (move["source"], move["destination"]):
            path = vault / relative
            if not path.resolve().is_relative_to(vault / "assets"):
                raise ValueError(f"Asset path escapes assets/: {relative}")
            if path.is_symlink() or any(p.is_symlink() for p in path.parents if p.is_relative_to(vault)):
                raise ValueError(f"Symlink in asset path: {relative}")
    return vault, selected


def transfer(source: Path, destination: Path, sha256: str) -> None:
    """Copy exclusively, verify bytes, then remove the original. Never overwrite."""
    if digest_file(source) != sha256:
        raise ValueError(f"Source changed: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with source.open("rb") as incoming, destination.open("xb") as outgoing:
            created = True
            shutil.copyfileobj(incoming, outgoing, 1024 * 1024)
        shutil.copystat(source, destination)
        if digest_file(destination) != sha256 or digest_file(source) != sha256:
            raise ValueError(f"File changed during transfer: {source}")
        source.unlink()
    except BaseException:
        if created and source.exists() and destination.exists():
            # The original is still present; this is our incomplete copy.
            destination.unlink()
        raise


def apply_plan(plan: dict, receipt: Path) -> dict:
    before = {}
    vault, moves = validate_plan(plan, snapshot=before)
    outside_scan(receipt, vault, [Path(p).resolve() for p in plan["policy"]["consumerRoots"]])
    if receipt.exists():
        raise ValueError(f"Receipt already exists: {receipt}. Inspect it before choosing a new receipt.")
    receipt.parent.mkdir(parents=True, exist_ok=True)
    state = {"schemaVersion": SCHEMA_VERSION, "status": "in-progress", "vault": str(vault), "moves": []}
    with receipt.open("x", encoding="utf8") as stream:
        stream.write(encoded(state))
    created_dirs = {str((vault / m["destination"]).parent) for m in moves if not (vault / m["destination"]).parent.exists()}
    try:
        for move in moves:
            state["pending"] = move
            receipt.write_text(encoded(state), encoding="utf8")
            transfer(vault / move["source"], vault / move["destination"], move["sha256"])
            state["moves"].append(move)
            state.pop("pending")
            receipt.write_text(encoded(state), encoding="utf8")
        for move in moves:
            if (vault / move["source"]).exists() or digest_file(vault / move["destination"]) != move["sha256"]:
                raise ValueError(f"Post-move verification failed: {move['destination']}")
        after = {}
        scan(vault, media=plan["policy"]["media"], consumer_roots=[Path(p) for p in plan["policy"]["consumerRoots"]], state=after)
        for move in moves:
            old, new = before["assets"][move["source"]], after["assets"][move["destination"]]
            for field in ("references", "mentions"):
                if old[field] != new[field]:
                    raise ValueError(f"References changed during moves: {move['source']}")
            for reference in old["references"] + old["mentions"]:
                source = reference["source"]
                if before["sourceHashes"].get(source) != after["sourceHashes"].get(source):
                    raise ValueError(f"Referencing source changed during moves: {source}")
    except BaseException:
        failures = []
        pending = state.pop("pending", None)
        if pending and pending not in state["moves"] and not (vault / pending["source"]).exists() and (vault / pending["destination"]).exists():
            state["moves"].append(pending)
        for move in reversed(state["moves"]):
            try:
                transfer(vault / move["destination"], vault / move["source"], move["sha256"])
            except (OSError, ValueError) as error:
                failures.append(str(error))
        for directory in sorted(created_dirs, reverse=True):
            try:
                Path(directory).rmdir()
            except OSError:
                pass
        state["status"] = "recovery-required" if failures else "rolled-back"
        state["recoveryErrors"] = failures
        receipt.write_text(encoded(state), encoding="utf8")
        raise
    state["status"] = "verified"
    receipt.write_text(encoded(state), encoding="utf8")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--apply", action="store_true", help="Apply the reviewed moves (otherwise dry-run)")
    parser.add_argument("--receipt", type=Path, help="New private receipt outside the vault; defaults beside the plan")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf8"))
        if args.apply:
            receipt = args.receipt or args.plan.with_name(args.plan.stem + "-applied.json")
            if receipt.resolve() == args.plan.resolve():
                raise ValueError("Receipt must not overwrite the proposal")
            state = apply_plan(plan, receipt)
            print(f"Moved and verified {len(state['moves'])} assets. Receipt: {receipt}")
        else:
            _, moves = validate_plan(plan)
            print(f"Dry run passed: {len(moves)} moves. No files changed.")
            for move in moves:
                print(f"{move['source']} -> {move['destination']}")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Move stopped: {error}\n")


if __name__ == "__main__":
    main()

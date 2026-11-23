#!/usr/bin/env python3
"""Apply approved entries from an unedited proposal with --apply.

Use --source to select a subset. Without --apply, print a dry run.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil

from find_misplaced_images import (
    EXCLUDED_ASSET_DIRS, SCHEMA_VERSION, digest_file, encoded, ignored_paths,
    outside_scan, proposal_checksum,
)


def check_git_exposure(vault: Path, moves: list[dict]) -> None:
    ignored = ignored_paths(vault, [move[key] for move in moves for key in ("source", "destination")])
    for move in moves:
        if move["source"] in ignored and move["destination"] not in ignored:
            raise ValueError(f"Move would expose a Git-ignored asset: {move['source']}")


def validate_plan(plan: dict, *, sources: list[str] | None = None) -> tuple[Path, list[dict]]:
    if plan.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError("Unsupported move-plan schema. Scan again for a fresh proposal.")
    if plan.get("proposalSha256") != proposal_checksum(plan):
        raise ValueError("The move proposal was edited. Use the original proposal with --source.")
    policy = plan["policy"]
    if policy["excludedAssetDirs"] != list(EXCLUDED_ASSET_DIRS):
        raise ValueError("The plan's exclusions differ from the current scanner")
    vault = Path(plan["vault"]).resolve()
    moves = {move["source"]: move for move in plan["moves"]}
    if len(moves) != len(plan["moves"]):
        raise ValueError("Duplicate source in move proposal")
    approved = set(moves if sources is None else sources)
    if missing := approved - moves.keys():
        raise ValueError(f"Source is unavailable for moves in this proposal: {', '.join(sorted(missing))}")
    selected = [move for name, move in moves.items() if name in approved]
    for move in selected:
        if Path(move["source"]).name != Path(move["destination"]).name:
            raise ValueError(f"Move would rename an asset: {move['source']}")
        for relative in (move["source"], move["destination"]):
            path = vault / relative
            if not path.resolve().is_relative_to(vault / "assets"):
                raise ValueError(f"Asset path escapes assets/: {relative}")
            if path.is_symlink() or any(p.is_symlink() for p in path.parents if p.is_relative_to(vault)):
                raise ValueError(f"Symlink in asset path: {relative}")
        if (vault / move["destination"]).exists():
            raise ValueError(f"Move destination already exists: {move['destination']}")
        if not (vault / move["source"]).is_file():
            raise ValueError(f"Move source no longer exists: {move['source']}")
    check_git_exposure(vault, selected)
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


def apply_plan(plan: dict, receipt: Path, *, sources: list[str] | None = None) -> dict:
    vault, moves = validate_plan(plan, sources=sources)
    if not moves:
        raise ValueError("The proposal has no moves to apply")
    consumers = [Path(p) for p in plan["policy"]["consumerRoots"]]
    outside_scan(receipt, vault, consumers)
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
    parser.add_argument("--source", action="append", help="Approved vault-relative source path; repeat for a subset")
    parser.add_argument("--receipt", type=Path, help="New private receipt outside the vault; defaults beside the plan")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf8"))
        if args.apply:
            receipt = args.receipt or args.plan.with_name(args.plan.stem + "-applied.json")
            if receipt.resolve() == args.plan.resolve():
                raise ValueError("Receipt must not overwrite the proposal")
            state = apply_plan(plan, receipt, sources=args.source)
            print(f"Moved and verified {len(state['moves'])} assets. Receipt: {receipt}")
        else:
            vault, moves = validate_plan(plan, sources=args.source)
            for move in moves:
                if digest_file(vault / move["source"]) != move["sha256"]:
                    raise ValueError(f"Source changed: {move['source']}")
            print(f"Dry run passed: {len(moves)} moves. No files changed.")
            for move in moves:
                print(f"{move['source']} -> {move['destination']}")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Move stopped: {error}\n")


if __name__ == "__main__":
    main()

"""Locate numbered Taelgar bundles by registered directory and session suffix."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from campaign_registry import load_campaigns

PREFIX = r"[a-z0-9]+(?:-[a-z0-9]+)*"
BUNDLE = re.compile(rf"({PREFIX})-([0-9]{{3}}|[1-9][0-9]{{3,}})(\.[0-9]+)?")


def session_number(value: str) -> str:
    whole, dot, fraction = str(value).partition(".")
    if not re.fullmatch(r"[0-9]+", whole) or (dot and not re.fullmatch(r"[0-9]+", fraction)):
        raise ValueError(f"Invalid session number: {value!r}")
    return str(int(whole)) + dot + fraction


def bundle_parts(path: Path) -> tuple[str, str]:
    match = BUNDLE.fullmatch(path.name)
    if not match:
        raise ValueError(f"Expected a numbered bundle such as cleenseau-012.4: {path}")
    return match[1], session_number(match[2] + (match[3] or ""))


def select_bundle(directory: Path, number: str, *, create=False, prefix=None, prompt=False) -> Path:
    """Select a destination without creating anything. Only immediate children count."""
    number = session_number(number)
    matches = []
    prefixes = set()
    for child in directory.iterdir() if directory.exists() else ():
        if not child.is_dir():
            continue
        if BUNDLE.fullmatch(child.name):
            child_prefix, child_number = bundle_parts(child)
            prefixes.add(child_prefix)
            if child_number == number:
                matches.append(child)
        else:
            suffix = re.search(r"-([0-9]+(?:\.[0-9]+)?)$", child.name)
            if suffix and session_number(suffix[1]) == number:
                raise ValueError(f"Invalid numbered bundle name for session {number}: {child}")
    if len(matches) > 1:
        raise ValueError(f"Several bundles for session {number}: " + ", ".join(map(str, sorted(matches))))
    if matches:
        bundle = matches[0]
        if bundle.is_symlink():
            raise ValueError(f"Session bundle is a symbolic link: {bundle}")
        if prefix is not None and prefix != bundle_parts(bundle)[0]:
            raise ValueError(f"Session {number} already uses {bundle.name}")
        return bundle
    if not create:
        raise ValueError(f"No bundle for session {number} in {directory}")
    if len(prefixes) == 1:
        established = next(iter(prefixes))
        if prefix is not None and prefix != established:
            raise ValueError(f"Established prefix in {directory}: {established}")
        prefix = established
    if prefix is None:
        reason = "Existing prefixes: " + ", ".join(sorted(prefixes)) if prefixes else "First bundle"
        message = f"{reason} in {directory}. Choose a bundle prefix"
        if not prompt:
            raise ValueError(f"{message} with --prefix.")
        print(f"{message}: ", end="", file=sys.stderr, flush=True)
        prefix = input().strip()
    if not re.fullmatch(PREFIX, prefix):
        raise ValueError("Use a lowercase bundle prefix with letters, digits, and optional hyphens.")
    whole, dot, fraction = number.partition(".")
    return directory / f"{prefix}-{int(whole):03d}{dot}{fraction}"


def session_manifest(bundle: Path, *, required=True) -> Path | None:
    matches = sorted((bundle / "cleaned").glob("*-session.yaml"))
    if len(matches) > 1:
        raise ValueError("Multiple session manifests: " + ", ".join(map(str, matches)))
    if required and not matches:
        raise ValueError(f"No prepared session manifest in {bundle}")
    return matches[0] if matches else None


def main() -> None:
    parser = argparse.ArgumentParser(description="Print the destination for a numbered vault bundle.")
    parser.add_argument("campaign", help="Registered campaign ID")
    parser.add_argument("session", help="Session number, e.g. 12.4")
    parser.add_argument("--prefix", help="Prefix to use when none is established")
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    vault = args.vault.resolve()
    try:
        campaigns = load_campaigns(vault)
        if args.campaign not in campaigns:
            raise ValueError(f"Unknown campaign ID: {args.campaign}")
        directory = campaigns[args.campaign].get("sessionBundleDirectory")
        if not directory:
            raise ValueError(f"No sessionBundleDirectory configured for {args.campaign}")
        destination = select_bundle(vault / directory, args.session, create=True,
                                    prefix=args.prefix, prompt=sys.stdin.isatty())
        print(destination.relative_to(vault).as_posix())
    except (ValueError, OSError, EOFError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()

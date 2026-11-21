"""Locate numbered Taelgar bundles by registered directory and session suffix."""
from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterator
from pathlib import Path

from campaign_registry import bundle_owner, campaign_bundle_directory, containing_vault

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


def _bundle_inventory(directory: Path) -> tuple[dict[str, list[Path]], list[Path]]:
    numbered: dict[str, list[Path]] = {}
    other = []
    for child in sorted(directory.iterdir()) if directory.exists() else ():
        if not child.is_dir():
            continue
        if not child.is_symlink() and BUNDLE.fullmatch(child.name):
            _, number = bundle_parts(child)
            numbered.setdefault(number, []).append(child)
        else:
            other.append(child)
    return numbered, other


def _unique_bundle(number: str, paths: list[Path]) -> Path | None:
    if len(paths) > 1:
        raise ValueError(f"Several bundles for session {number}: " + ", ".join(map(str, paths)))
    return paths[0] if paths else None


def registered_bundle_identity(
    bundle: Path, *, vault: Path | None = None, campaigns: dict | None = None
) -> tuple[str, str] | None:
    """Return the owner and textual session number of a registered bundle."""
    bundle = bundle.resolve()
    vault = vault or containing_vault(bundle)
    if vault is None or not (vault / "_sessions/campaign-registry.json").is_file():
        return None
    owner = bundle_owner(vault, bundle, campaigns=campaigns)
    if owner is not None and BUNDLE.fullmatch(bundle.name):
        _, number = bundle_parts(bundle)
        numbered, _ = _bundle_inventory(bundle.parent)
        if _unique_bundle(number, numbered.get(number, [])) == bundle:
            return owner, number
    return None


def numbered_bundles(directory: Path) -> Iterator[Path]:
    """Yield numbered bundle folders after checking the directory for duplicates."""
    numbered, _ = _bundle_inventory(directory)
    for number, paths in numbered.items():
        _unique_bundle(number, paths)
    yield from sorted(paths[0] for paths in numbered.values())


def session_identity(manifest: Path, metadata: dict, *, vault: Path | None = None) -> tuple:
    """Project identity for display and lookup without changing source metadata."""
    if manifest.parent.name == "cleaned":
        identity = registered_bundle_identity(manifest.parent.parent, vault=vault)
        if identity is not None:
            return identity
    return metadata.get("campaign"), metadata.get("sessionNumber")


def select_bundle(directory: Path, number: str, *, create=False, prefix=None, prompt=False) -> Path:
    """Select a destination without creating anything. Only immediate children count."""
    number = session_number(number)
    numbered, other = _bundle_inventory(directory)
    bundle = _unique_bundle(number, numbered.get(number, []))
    for child in other:
        suffix = re.search(r"-([0-9]+(?:\.[0-9]+)?)$", child.name)
        if suffix and session_number(suffix[1]) == number:
            if child.is_symlink() and BUNDLE.fullmatch(child.name):
                raise ValueError(f"Session bundle is a symbolic link: {child}")
            raise ValueError(f"Invalid numbered bundle name for session {number}: {child}")
    if bundle is not None:
        if prefix is not None and prefix != bundle_parts(bundle)[0]:
            raise ValueError(f"Session {number} already uses {bundle.name}")
        return bundle
    if not create:
        raise ValueError(f"No bundle for session {number} in {directory}")
    prefixes = {bundle_parts(path)[0] for paths in numbered.values() for path in paths}
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


def resolve_bundle(vault: Path, campaign: str, number: str, *, campaigns=None,
                   create=False, prefix=None, prompt=False) -> Path:
    """Look up a numbered bundle by campaign ID and session number."""
    directory = campaign_bundle_directory(vault, campaign, campaigns=campaigns)
    return select_bundle(directory, number, create=create, prefix=prefix, prompt=prompt)


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
        destination = resolve_bundle(vault, args.campaign, args.session, create=True,
                                     prefix=args.prefix, prompt=sys.stdin.isatty())
        print(destination.relative_to(vault).as_posix())
    except (ValueError, OSError, EOFError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()

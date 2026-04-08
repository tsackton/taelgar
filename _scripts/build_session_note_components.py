#!/usr/bin/env python3

"""Build composable session-note components from a reviewed session recap."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


VAULT_ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN_MAP_PATH = Path(__file__).with_name("session_note_campaigns.json")
TAELGAR_UTILS_BUILDER = Path("/Users/tim/RPGs/taelgar-utils/skills/session-summary/scripts/build_session_note_components.py")
AI_TAG = "status/check/ai"
SESSION_NOTE_TAG = "session-note"


def slugify_text(value: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in str(value or ""))
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def load_campaigns() -> Dict[str, Dict[str, Any]]:
    payload = json.loads(CAMPAIGN_MAP_PATH.read_text(encoding="utf-8"))
    campaigns = payload.get("campaigns")
    if not isinstance(campaigns, dict) or not campaigns:
        raise SystemExit(f"Campaign map is missing a non-empty 'campaigns' object: {CAMPAIGN_MAP_PATH}")
    return campaigns


def build_campaign_lookup(campaigns: Dict[str, Dict[str, Any]]) -> Dict[str, str]:
    lookup: Dict[str, str] = {}
    for canonical_slug, config in campaigns.items():
        keys = [canonical_slug, *(config.get("aliases") or [])]
        for key in keys:
            normalized = slugify_text(key)
            if not normalized:
                continue
            lookup[normalized] = canonical_slug
    return lookup


def format_campaign_help(campaigns: Dict[str, Dict[str, Any]]) -> str:
    lines = ["Available campaigns:"]
    for canonical_slug in sorted(campaigns):
        aliases = campaigns[canonical_slug].get("aliases") or []
        alias_text = f" (aliases: {', '.join(aliases)})" if aliases else ""
        lines.append(f"  - {canonical_slug}{alias_text}")
    return "\n".join(lines)


def parse_args(campaigns: Dict[str, Dict[str, Any]]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build session-note components from a reviewed session recap.",
        epilog=format_campaign_help(campaigns),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-c", "--campaign", required=True, help="Campaign code or alias.")
    parser.add_argument("-n", "--session", required=True, type=int, help="Session number.")
    return parser.parse_args()


def resolve_campaign(selection: str, campaigns: Dict[str, Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
    lookup = build_campaign_lookup(campaigns)
    normalized = slugify_text(selection)
    canonical = lookup.get(normalized)
    if canonical is None:
        available = ", ".join(sorted(campaigns))
        raise SystemExit(f"Unknown campaign '{selection}'. Available campaigns: {available}")
    return canonical, campaigns[canonical]


def read_yaml_mapping(path: Path) -> Dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit(f"Expected a YAML mapping in {path}")
    return payload


def find_session_manifest(canonical_slug: str, config: Dict[str, Any], session_number: int) -> Path:
    session_root = VAULT_ROOT / "_sessions" / str(config["sessionRoot"])
    if not session_root.exists():
        raise SystemExit(f"Session root does not exist for campaign '{canonical_slug}': {session_root}")

    matches: List[Path] = []
    for manifest_path in sorted(session_root.rglob("*-session.yaml")):
        payload = read_yaml_mapping(manifest_path)
        try:
            manifest_session_number = int(payload.get("sessionNumber"))
        except (TypeError, ValueError):
            continue
        if manifest_session_number != session_number:
            continue
        matches.append(manifest_path)

    if not matches:
        raise SystemExit(f"No session manifest found for campaign '{canonical_slug}' session {session_number}.")
    if len(matches) > 1:
        formatted = "\n".join(f"  - {path}" for path in matches)
        raise SystemExit(
            f"Multiple session manifests found for campaign '{canonical_slug}' session {session_number}:\n{formatted}"
        )
    return matches[0]


def derive_session_recap_path(session_manifest: Path) -> Path:
    if not session_manifest.name.endswith("-session.yaml"):
        raise SystemExit(f"Cannot derive session recap path from unexpected manifest name: {session_manifest}")
    recap_name = session_manifest.name.replace("-session.yaml", "-session-recap.md")
    recap_path = session_manifest.with_name(recap_name)
    if not recap_path.exists():
        raise SystemExit(f"Session recap not found: {recap_path}")
    return recap_path


def build_session_key(session_payload: Dict[str, Any], *, fallback: str) -> str:
    campaign = str(session_payload.get("campaign") or "").strip()
    session_number = str(session_payload.get("sessionNumber") or "").strip()
    scope = str(session_payload.get("scope") or "session").strip() or "session"
    if campaign and session_number:
        return f"{slugify_text(campaign)}-{slugify_text(scope)}-{slugify_text(session_number)}"
    return slugify_text(fallback)


def render_note_filename(pattern: str, session_number: int) -> str:
    return pattern.format(session=session_number, session_padded=f"{session_number:02d}")


def split_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            frontmatter = yaml.safe_load("\n".join(lines[1:index])) or {}
            if not isinstance(frontmatter, dict):
                frontmatter = {}
            body = "\n".join(lines[index + 1 :])
            return frontmatter, body
    return {}, text


def normalize_tags(value: Any) -> List[str]:
    if isinstance(value, list):
        tags = [str(item).strip() for item in value if str(item).strip()]
    elif isinstance(value, str) and value.strip():
        tags = [value.strip()]
    else:
        tags = []
    for required in (SESSION_NOTE_TAG, AI_TAG):
        if required not in tags:
            tags.append(required)
    return tags


def ensure_base_note(
    *,
    note_path: Path,
    session_key: str,
    template_name: str,
) -> str:
    if note_path.exists():
        frontmatter, body = split_frontmatter(note_path.read_text(encoding="utf-8"))
        frontmatter = dict(frontmatter)
        frontmatter["headerVersion"] = frontmatter.get("headerVersion") or "2023.11.25"
        frontmatter["tags"] = normalize_tags(frontmatter.get("tags"))
        frontmatter["sessionKey"] = session_key
        if not str(frontmatter.get("template") or "").strip():
            frontmatter["template"] = template_name
        frontmatter.pop("sessionManifest", None)
        body_text = body.lstrip("\n")
        status = "Updated"
    else:
        frontmatter = {
            "headerVersion": "2023.11.25",
            "tags": [SESSION_NOTE_TAG, AI_TAG],
            "sessionKey": session_key,
            "template": template_name,
        }
        body_text = ""
        status = "Created"

    frontmatter_text = yaml.safe_dump(frontmatter, sort_keys=False).strip()
    if body_text:
        text = f"---\n{frontmatter_text}\n---\n{body_text.rstrip()}\n"
    else:
        text = f"---\n{frontmatter_text}\n---\n"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(text, encoding="utf-8")
    return status


def main() -> int:
    campaigns = load_campaigns()
    args = parse_args(campaigns)
    canonical_slug, config = resolve_campaign(args.campaign, campaigns)

    if not TAELGAR_UTILS_BUILDER.exists():
        raise SystemExit(f"Component builder script not found: {TAELGAR_UTILS_BUILDER}")

    session_manifest = find_session_manifest(canonical_slug, config, args.session)
    session_recap = derive_session_recap_path(session_manifest)
    session_payload = read_yaml_mapping(session_manifest)

    command = [
        sys.executable,
        str(TAELGAR_UTILS_BUILDER),
        "--session",
        str(session_manifest),
        "--session-recap-md",
        str(session_recap),
    ]
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        return completed.returncode

    note_root = VAULT_ROOT / str(config["campaignRoot"])
    note_filename = render_note_filename(str(config["notePattern"]), args.session)
    note_path = note_root / note_filename
    template_name = str(config.get("defaultTemplate") or "composable-session-note.md").strip()
    session_key = build_session_key(session_payload, fallback=session_manifest.stem)
    status = ensure_base_note(note_path=note_path, session_key=session_key, template_name=template_name)
    print(f"{status} {note_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

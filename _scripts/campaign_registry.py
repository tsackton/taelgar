"""Read campaign index frontmatter, keyed by the ID in the vault registry."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


def _unique_entries(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    entries = {}
    for key, value in pairs:
        if key in entries:
            raise ValueError(f"duplicate key {key!r}")
        entries[key] = value
    return entries


def _read_index_note(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8-sig") as note:
        if note.readline().rstrip() != "---":
            raise ValueError("missing opening frontmatter delimiter")
        lines = []
        for line in note:
            if line.rstrip() == "---":
                break
            lines.append(line)
        else:
            raise ValueError("missing closing frontmatter delimiter")

    fields = yaml.safe_load("".join(lines))
    if not isinstance(fields, dict):
        raise ValueError("expected a frontmatter mapping")
    if not isinstance(fields.get("name"), str) or not fields["name"].strip():
        raise ValueError("missing campaign name")
    return fields


def load_campaigns(vault_root: Path) -> dict[str, dict[str, Any]]:
    """Load all registered campaigns. Session configuration is optional."""
    vault_root = vault_root.resolve()
    registry_path = vault_root / "_sessions" / "campaign-registry.json"
    try:
        entries = json.loads(registry_path.read_text(encoding="utf-8"), object_pairs_hook=_unique_entries)
    except (OSError, ValueError) as exc:
        raise ValueError(f"{registry_path}: {exc}") from exc
    if not isinstance(entries, dict) or not entries:
        raise ValueError(f"{registry_path}: expected a nonempty mapping of IDs to index notes")

    campaigns = {}
    owners = {}
    for campaign_id, target in entries.items():
        if not re.fullmatch(r"[a-z][a-z0-9]*", campaign_id):
            raise ValueError(f"{registry_path}: invalid campaign ID {campaign_id!r}")
        if not isinstance(target, str) or Path(target).is_absolute() or Path(target).suffix != ".md":
            raise ValueError(f"{campaign_id}: expected a vault-relative Markdown path, got {target!r}")
        path = (vault_root / target).resolve()
        if not path.is_relative_to(vault_root):
            raise ValueError(f"{campaign_id}: {target} points outside the vault")
        if path in owners:
            raise ValueError(f"{campaign_id}: {target} already belongs to {owners[path]}")
        try:
            campaigns[campaign_id] = _read_index_note(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            raise ValueError(f"{campaign_id}: {target}: {exc}") from exc
        owners[path] = campaign_id
    return campaigns


def session_campaign_id(manifest: Path, declared: str | None) -> str | None:
    """Project a registered bundle's ID without changing its fingerprinted source."""
    manifest = manifest.resolve()
    directory = manifest.parent.parent.parent
    if manifest.parent.name != "cleaned":
        return declared
    vault = next((p for p in directory.parents if (p / "_sessions/campaign-registry.json").is_file()), None)
    if vault is None:
        return declared  # Standalone bundle outside a registered vault.
    campaigns = load_campaigns(vault)
    owners = [key for key, row in campaigns.items() if row.get("sessionBundleDirectory")
              and (vault / row["sessionBundleDirectory"]).resolve() == directory]
    if len(owners) != 1 or (declared in campaigns and declared != owners[0]):
        raise ValueError(f"Missing or conflicting campaign ownership for {manifest}")
    return owners[0]

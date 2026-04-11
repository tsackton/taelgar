#!/usr/bin/env python

"""Build session-note components from a reviewed session recap."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import yaml


VAULT_ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN_MAP_PATH = Path(__file__).with_name("session_note_campaigns.json")
AI_TAG = "status/check/ai"
SESSION_NOTE_TAG = "session-note"


class SessionRecapParseError(Exception):
    def __init__(self, errors: Sequence[str]) -> None:
        self.errors = list(errors)
        super().__init__("\n".join(self.errors))


@dataclass
class SectionRange:
    heading: str
    start: int
    end: int


class ResolutionResult:
    def __init__(self, name: str, note: Optional[Dict[str, Any]], warning: Optional[str] = None) -> None:
        self.name = name
        self.note = note
        self.warning = warning

    def link(self, display_name: str) -> str:
        if self.note is None:
            return display_name
        basename = self.note["path"].stem
        if basename == display_name:
            return f"[[{basename}]]"
        return f"[[{basename}|{display_name}]]"

    def simple_whereabouts(self) -> Optional[str]:
        if self.note is None:
            return None
        frontmatter = self.note.get("frontmatter", {})
        where = frontmatter.get("whereabouts")
        if isinstance(where, str):
            return normalize_optional_string(where)
        return None


class VaultNoteIndex:
    def __init__(self, vault_root: Path, generated_root: Path) -> None:
        self.vault_root = vault_root
        self.generated_root = generated_root
        self.by_basename: Dict[str, List[Dict[str, Any]]] = {}
        self.by_alias: Dict[str, List[Dict[str, Any]]] = {}
        self._load()

    def _load(self) -> None:
        for path in self.vault_root.rglob("*.md"):
            if not should_index_path(path, self.vault_root, self.generated_root):
                continue
            note = {"path": path, "frontmatter": read_markdown_frontmatter(path)}
            self.by_basename.setdefault(normalize_name(path.stem), []).append(note)
            aliases = note["frontmatter"].get("aliases")
            for alias in normalize_aliases(aliases):
                self.by_alias.setdefault(normalize_name(alias), []).append(note)

    def resolve(self, name: str) -> ResolutionResult:
        key = normalize_name(name)
        candidates = dedupe_notes([*self.by_basename.get(key, []), *self.by_alias.get(key, [])])
        if not candidates:
            return ResolutionResult(name, None, "no matching note found in the vault index")
        if len(candidates) > 1:
            paths = ", ".join(str(note["path"].relative_to(self.vault_root)) for note in candidates[:5])
            return ResolutionResult(name, None, f"multiple matching notes found ({paths})")
        return ResolutionResult(name, candidates[0])


def parse_args(campaigns: Dict[str, Dict[str, Any]]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build session-note components from a reviewed session recap.",
        epilog=format_campaign_help(campaigns),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-c", "--campaign", required=True, help="Campaign code or alias.")
    parser.add_argument("-n", "--session", required=True, type=int, help="Session number.")
    return parser.parse_args()


def main() -> int:
    campaigns = load_campaigns()
    args = parse_args(campaigns)
    canonical_slug, config = resolve_campaign(args.campaign, campaigns)

    session_manifest = find_session_manifest(canonical_slug, config, args.session)
    session_recap = derive_session_recap_path(session_manifest)
    session_payload = read_yaml_mapping(session_manifest)
    recap_text = session_recap.read_text(encoding="utf-8")
    try:
        recap = parse_session_recap(recap_text)
    except SessionRecapParseError as exc:
        for error in exc.errors:
            print(f"ERROR: {error}")
        return 1

    generated_root = (VAULT_ROOT / str(config["campaignRoot"]) / "_generated" / "session-notes").resolve()
    component_dir = generated_root / build_component_dir_name(session_payload, fallback=session_manifest.stem)
    component_dir.mkdir(parents=True, exist_ok=True)

    note_index = VaultNoteIndex(VAULT_ROOT, generated_root)
    slots = build_slots(recap=recap, note_index=note_index, session_payload=session_payload)

    write_component_file(
        component_dir / "01-session-info.md",
        title="Session Info",
        session_manifest=str(session_manifest),
        slots=slots["info"],
    )
    write_component_file(
        component_dir / "02-technical-updates.md",
        title="Technical Updates",
        session_manifest=str(session_manifest),
        slots=slots["technical"],
    )
    write_component_file(
        component_dir / "03-narrative.md",
        title="Narrative",
        session_manifest=str(session_manifest),
        slots=slots["narrative"],
    )

    print(f"Wrote {component_dir / '01-session-info.md'}")
    print(f"Wrote {component_dir / '02-technical-updates.md'}")
    print(f"Wrote {component_dir / '03-narrative.md'}")

    note_root = VAULT_ROOT / str(config["campaignRoot"])
    note_filename = render_note_filename(str(config["notePattern"]), args.session)
    note_path = note_root / note_filename
    template_name = str(config.get("defaultTemplate") or "composable-session-note.md").strip()
    session_key = build_session_key(session_payload, fallback=session_manifest.stem)
    status = ensure_base_note(note_path=note_path, session_key=session_key, template_name=template_name)
    print(f"{status} {note_path}")
    return 0


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
            if normalized:
                lookup[normalized] = canonical_slug
    return lookup


def format_campaign_help(campaigns: Dict[str, Dict[str, Any]]) -> str:
    lines = ["Available campaigns:"]
    for canonical_slug in sorted(campaigns):
        aliases = campaigns[canonical_slug].get("aliases") or []
        alias_text = f" (aliases: {', '.join(aliases)})" if aliases else ""
        lines.append(f"  - {canonical_slug}{alias_text}")
    return "\n".join(lines)


def resolve_campaign(selection: str, campaigns: Dict[str, Dict[str, Any]]) -> Tuple[str, Dict[str, Any]]:
    lookup = build_campaign_lookup(campaigns)
    canonical = lookup.get(slugify_text(selection))
    if canonical is None:
        available = ", ".join(sorted(campaigns))
        raise SystemExit(f"Unknown campaign '{selection}'. Available campaigns: {available}")
    return canonical, campaigns[canonical]


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
        if manifest_session_number == session_number:
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
    recap_path = session_manifest.with_name(session_manifest.name.replace("-session.yaml", "-session-recap.md"))
    if not recap_path.exists():
        raise SystemExit(f"Session recap not found: {recap_path}")
    return recap_path


def build_session_key(session_payload: Dict[str, Any], *, fallback: str) -> str:
    campaign = normalize_optional_string(session_payload.get("campaign"))
    session_number = normalize_optional_string(session_payload.get("sessionNumber"))
    scope = normalize_optional_string(session_payload.get("scope")) or "session"
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
            body = "\n".join(lines[index + 1 :])
            return (frontmatter if isinstance(frontmatter, dict) else {}), body
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


def ensure_base_note(*, note_path: Path, session_key: str, template_name: str) -> str:
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


def parse_session_recap(text: str) -> Dict[str, Any]:
    lines = text.splitlines()
    errors: List[str] = []

    if not lines or lines[0].strip() != "# Session Recap":
        errors.append("Session recap must start with '# Session Recap'.")

    sections = collect_level2_sections(lines)
    required_sections = [
        "## Session Header",
        "## Timeline",
        "## Recap",
        "## Cast",
        "## Locations",
        "## Organizations And Items",
        "## Combat",
        "## Source Files",
    ]
    for heading in required_sections:
        if heading not in sections:
            errors.append(f"Missing required section for downstream parsing: {heading}")

    if errors:
        raise SessionRecapParseError(errors)

    header = parse_header_section(get_section_lines(lines, sections["## Session Header"]), errors)
    timeline = parse_timeline_section(get_section_lines(lines, sections["## Timeline"]), errors)
    recap = parse_recap_section(get_section_lines(lines, sections["## Recap"]), errors)
    cast = parse_cast_section(get_section_lines(lines, sections["## Cast"]), errors)
    locations = parse_locations_section(get_section_lines(lines, sections["## Locations"]), errors)
    organizations_and_items = parse_orgs_items_section(
        get_section_lines(lines, sections["## Organizations And Items"]),
        errors,
    )
    combat = parse_combat_section(get_section_lines(lines, sections["## Combat"]), errors)
    source_files = parse_keyed_bullets(
        get_section_lines(lines, sections["## Source Files"]),
        label="Source Files",
        errors=errors,
    )

    if errors:
        raise SessionRecapParseError(errors)

    return {
        "header": header,
        "timeline": timeline,
        "recap": recap,
        "cast": cast,
        "locations": locations,
        "organizations": organizations_and_items["organizations"],
        "items": organizations_and_items["items"],
        "combat": combat,
        "sourceFiles": source_files,
        "rawText": text,
    }


def collect_level2_sections(lines: Sequence[str]) -> Dict[str, SectionRange]:
    sections: Dict[str, SectionRange] = {}
    headings: List[Tuple[str, int]] = []
    for index, line in enumerate(lines):
        if line.startswith("## "):
            headings.append((line.strip(), index))
    for position, (heading, start) in enumerate(headings):
        end = headings[position + 1][1] if position + 1 < len(headings) else len(lines)
        sections[heading] = SectionRange(heading=heading, start=start, end=end)
    return sections


def get_section_lines(lines: Sequence[str], section: SectionRange) -> List[str]:
    return list(lines[section.start + 1 : section.end])


def parse_header_section(lines: Sequence[str], errors: List[str]) -> Dict[str, str]:
    data = parse_keyed_bullets(lines, label="Session Header", errors=errors)
    required = [
        "Title",
        "Desc Title",
        "Tagline",
        "One-Sentence Summary",
        "Campaign",
        "Session Number",
        "DR Date",
        "Real Date",
        "DM",
        "PCs",
    ]
    for key in required:
        if key not in data:
            errors.append(f"Session Header is missing '{key}'.")
    return data


def parse_timeline_section(lines: Sequence[str], errors: List[str]) -> List[Dict[str, Any]]:
    blocks = split_level3_blocks(lines, label="Timeline", errors=errors)
    parsed: List[Dict[str, Any]] = []
    for heading, block_lines in blocks:
        data = parse_keyed_bullets(block_lines, label=f"Timeline block {heading}", errors=errors)
        block_id = data.get("Timeline Segment")
        if not block_id:
            errors.append(f"Timeline block '{heading}' is missing Timeline Segment.")
        parsed.append(
            {
                "heading": heading,
                "blockId": block_id,
                "timelineKey": data.get("Timeline Key", ""),
                "resolution": data.get("Resolution", ""),
                "beatIds": parse_name_list(data.get("Beat IDs")),
                "locations": parse_name_list(data.get("Locations")),
                "npcs": parse_name_list(data.get("NPCs")),
                "organizations": parse_name_list(data.get("Organizations")),
                "items": parse_name_list(data.get("Items")),
                "combatBeats": parse_name_list(data.get("Combat Beats")),
                "short": parse_required_subsection(block_lines, "#### Short", f"timeline {block_id or heading}", errors),
                "long": parse_required_subsection(block_lines, "#### Long", f"timeline {block_id or heading}", errors),
            }
        )
    return parsed


def parse_recap_section(lines: Sequence[str], errors: List[str]) -> List[Dict[str, Any]]:
    blocks = split_level3_blocks(lines, label="Recap", errors=errors)
    parsed: List[Dict[str, Any]] = []
    for heading, block_lines in blocks:
        match = re.match(r"^(?P<block_id>recap-\d+)\s+\|\s+(?P<title>.+)$", heading)
        if not match:
            errors.append(f"Recap block heading is malformed: {heading}")
            continue
        data = parse_keyed_bullets(block_lines, label=f"Recap block {heading}", errors=errors)
        parsed.append(
            {
                "blockId": match.group("block_id"),
                "title": match.group("title").strip(),
                "kind": data.get("Kind", ""),
                "beatIds": parse_name_list(data.get("Beat IDs")),
                "date": data.get("Date", ""),
                "time": data.get("Time", ""),
                "sourceRange": data.get("Source Range", ""),
                "locations": parse_name_list(data.get("Locations")),
                "npcs": parse_name_list(data.get("NPCs")),
                "organizations": parse_name_list(data.get("Organizations")),
                "items": parse_name_list(data.get("Items")),
                "enemies": parse_name_list(data.get("Enemies")),
                "short": parse_required_subsection(block_lines, "#### Short", f"recap {match.group('block_id')}", errors),
                "intermediate": parse_required_subsection(
                    block_lines, "#### Intermediate", f"recap {match.group('block_id')}", errors
                ),
                "long": parse_required_subsection(block_lines, "#### Long", f"recap {match.group('block_id')}", errors),
            }
        )
    return parsed


def parse_cast_section(lines: Sequence[str], errors: List[str]) -> List[Dict[str, Any]]:
    npc_section = extract_required_subsection(lines, "### NPCs", "Cast", errors)
    return parse_history_entries(npc_section, "Cast/NPCs", errors)


def parse_locations_section(lines: Sequence[str], errors: List[str]) -> List[Dict[str, Any]]:
    return parse_location_entries(lines, "Locations", errors)


def parse_orgs_items_section(lines: Sequence[str], errors: List[str]) -> Dict[str, List[Dict[str, Any]]]:
    org_lines = extract_required_subsection(lines, "### Organizations", "Organizations And Items", errors)
    item_lines = extract_required_subsection(lines, "### Items", "Organizations And Items", errors)
    return {
        "organizations": parse_history_entries(org_lines, "Organizations", errors),
        "items": parse_history_entries(item_lines, "Items", errors),
    }


def parse_combat_section(lines: Sequence[str], errors: List[str]) -> List[Dict[str, Any]]:
    if only_blank_or_none(lines):
        return []
    blocks = split_level3_blocks(lines, label="Combat", errors=errors)
    parsed: List[Dict[str, Any]] = []
    for heading, block_lines in blocks:
        match = re.match(r"^(?P<block_id>recap-\d+)\s+\|\s+(?P<title>.+)$", heading)
        if not match:
            errors.append(f"Combat block heading is malformed: {heading}")
            continue
        data = parse_keyed_bullets(block_lines, label=f"Combat block {heading}", errors=errors)
        parsed.append(
            {
                "blockId": match.group("block_id"),
                "title": match.group("title").strip(),
                "beatIds": parse_name_list(data.get("Beat IDs")),
                "enemies": parse_name_list(data.get("Enemies")),
                "contextOutcome": data.get("Context / Outcome", ""),
            }
        )
    return parsed


def only_blank_or_none(lines: Sequence[str]) -> bool:
    stripped = [line.strip() for line in lines if line.strip()]
    return stripped == ["- none"] or not stripped


def split_level3_blocks(lines: Sequence[str], *, label: str, errors: List[str]) -> List[Tuple[str, List[str]]]:
    headings: List[Tuple[str, int]] = []
    for index, line in enumerate(lines):
        if line.startswith("### "):
            headings.append((line.strip()[4:], index))
    if not headings and not only_blank_or_none(lines):
        errors.append(f"{label} section must contain level-3 blocks or '- none'.")
        return []
    blocks: List[Tuple[str, List[str]]] = []
    for position, (heading, start) in enumerate(headings):
        end = headings[position + 1][1] if position + 1 < len(headings) else len(lines)
        blocks.append((heading, list(lines[start + 1 : end])))
    return blocks


def parse_keyed_bullets(lines: Sequence[str], *, label: str, errors: List[str]) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped or not stripped.startswith("- "):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped[2:].split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            errors.append(f"{label} contains an empty keyed bullet: {raw_line}")
            continue
        data[key] = value
    return data


def parse_required_subsection(lines: Sequence[str], heading: str, label: str, errors: List[str]) -> str:
    text = parse_subsection(lines, heading)
    if text is None:
        errors.append(f"{label} is missing subsection {heading}.")
        return ""
    if not text.strip():
        errors.append(f"{label} subsection {heading} is empty.")
        return ""
    return text


def parse_subsection(lines: Sequence[str], heading: str) -> Optional[str]:
    start_index: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start_index = index + 1
            break
    if start_index is None:
        return None
    end_index = len(lines)
    for index in range(start_index, len(lines)):
        if lines[index].startswith("#### ") or lines[index].startswith("### "):
            end_index = index
            break
    return "\n".join(lines[start_index:end_index]).strip()


def extract_required_subsection(lines: Sequence[str], heading: str, label: str, errors: List[str]) -> List[str]:
    start_index: Optional[int] = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start_index = index + 1
            break
    if start_index is None:
        errors.append(f"{label} section is missing subsection {heading}.")
        return []
    end_index = len(lines)
    for index in range(start_index, len(lines)):
        if lines[index].startswith("### "):
            end_index = index
            break
    return list(lines[start_index:end_index])


def parse_history_entries(lines: Sequence[str], label: str, errors: List[str]) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    current: Optional[Dict[str, Any]] = None
    for raw_line in lines:
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - "):
            if current is None:
                errors.append(f"{label} contains a history line before any entry: {raw_line.strip()}")
                continue
            parsed_history = parse_history_line(raw_line[4:].strip(), label, errors)
            if parsed_history is not None:
                current["history"].append(parsed_history)
            continue
        if not raw_line.startswith("- "):
            errors.append(f"{label} contains an unparseable line: {raw_line.strip()}")
            continue
        entry = parse_named_entry(raw_line.strip()[2:], label, errors)
        if entry is None:
            continue
        entry["history"] = []
        entries.append(entry)
        current = entry
    return entries


def parse_location_entries(lines: Sequence[str], label: str, errors: List[str]) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    current: Optional[Dict[str, Any]] = None
    for raw_line in lines:
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - "):
            if current is None:
                errors.append(f"{label} contains a visit line before any entry: {raw_line.strip()}")
                continue
            detail = parse_location_detail_line(raw_line[4:].strip())
            if detail is not None:
                key, value = detail
                current[key] = value
                continue
            parsed_visit = parse_visit_line(raw_line[4:].strip(), label, errors)
            if parsed_visit is not None:
                current["visits"].append(parsed_visit)
                if current.get("dateVisited") is None:
                    current["dateVisited"] = parsed_visit["date"]
            continue
        if not raw_line.startswith("- "):
            errors.append(f"{label} contains an unparseable line: {raw_line.strip()}")
            continue
        body = raw_line.strip()[2:]
        if ":" in body:
            entry = parse_named_entry(body, label, errors, allow_relation=False)
            if entry is None:
                continue
            current = {
                "name": entry["name"],
                "summary": entry["context"],
                "sublocations": None,
                "dateVisited": None,
                "visits": [],
                "legacyFormat": True,
            }
        else:
            current = {
                "name": body.strip(),
                "summary": None,
                "sublocations": None,
                "dateVisited": None,
                "visits": [],
                "legacyFormat": False,
            }
        entries.append(current)
    for entry in entries:
        if entry.get("legacyFormat"):
            continue
        if normalize_optional_string(entry.get("summary")) is None:
            errors.append(f"{label} entry '{entry['name']}' is missing Summary.")
        if normalize_optional_string(entry.get("sublocations")) is None:
            errors.append(f"{label} entry '{entry['name']}' is missing Sublocations.")
        if normalize_optional_string(entry.get("dateVisited")) is None:
            errors.append(f"{label} entry '{entry['name']}' is missing Date Visited.")
    return entries


def parse_location_detail_line(body: str) -> Optional[Tuple[str, str]]:
    if ":" not in body:
        return None
    key, value = body.split(":", 1)
    normalized_key = key.strip().lower()
    mapped = {
        "summary": "summary",
        "sublocations": "sublocations",
        "date visited": "dateVisited",
    }.get(normalized_key)
    if mapped is None:
        return None
    return mapped, value.strip()


def parse_named_entry(body: str, label: str, errors: List[str], *, allow_relation: bool = True) -> Optional[Dict[str, Any]]:
    if allow_relation:
        match = re.match(r"^(?P<name>.+?)(?:\s+\((?P<relation>[^)]+)\))?:\s+(?P<context>.+)$", body)
    else:
        match = re.match(r"^(?P<name>.+?):\s+(?P<context>.+)$", body)
    if not match:
        errors.append(f"{label} entry is malformed: {body}")
        return None
    return {
        "name": match.group("name").strip(),
        "relation": (match.groupdict().get("relation") or "").strip(),
        "context": match.group("context").strip(),
    }


def parse_history_line(body: str, label: str, errors: List[str]) -> Optional[Dict[str, str]]:
    if ", " not in body:
        errors.append(f"{label} history line is malformed: {body}")
        return None
    location, date_text = body.rsplit(", ", 1)
    return {"raw": body, "location": location.strip(), "date": date_text.strip()}


def parse_visit_line(body: str, label: str, errors: List[str]) -> Optional[Dict[str, str]]:
    if " on " not in body:
        errors.append(f"{label} visit line is malformed: {body}")
        return None
    relation, date_text = body.split(" on ", 1)
    return {"raw": body, "relation": relation.strip(), "date": date_text.strip()}


def parse_name_list(value: Optional[str]) -> List[str]:
    if value is None:
        return []
    stripped = value.strip()
    if not stripped or stripped == "none":
        return []
    return [item.strip() for item in stripped.split(",") if item.strip()]


def build_component_dir_name(session_payload: Dict[str, Any], *, fallback: str) -> str:
    campaign = normalize_optional_string(session_payload.get("campaign"))
    session_number = normalize_optional_string(session_payload.get("sessionNumber"))
    scope = normalize_optional_string(session_payload.get("scope")) or "session"
    if campaign and session_number:
        return f"{slugify_text(campaign)}-{slugify_text(scope)}-{slugify_text(session_number)}"
    return slugify_text(fallback)


def build_slots(*, recap: Dict[str, Any], note_index: VaultNoteIndex, session_payload: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    review_lines: List[str] = []
    info_slots: Dict[str, str] = {}
    technical_slots: Dict[str, str] = {}
    narrative_slots: Dict[str, str] = {}

    header = recap["header"]
    info_slots["session.title"] = header.get("Title", "")
    info_slots["session.desc_title"] = header.get("Desc Title", "")
    info_slots["session.tagline"] = header.get("Tagline", "")
    info_slots["session.summary"] = header.get("One-Sentence Summary", "")
    info_slots["session.dm"] = header.get("DM", "")
    info_slots["session.pcs"] = render_inline_csv_as_bullets(header.get("PCs", ""))
    info_slots["session.pcs_inline"] = render_inline_csv_as_links(header.get("PCs", ""), note_index)
    info_slots["session.session_number"] = render_scalar(session_payload.get("sessionNumber"))
    info_slots["session.dr_date"] = header.get("DR Date", "")
    info_slots["session.dr_start"] = normalize_optional_string(session_payload.get("drStart")) or header.get("DR Date", "")
    info_slots["session.dr_end"] = normalize_optional_string(session_payload.get("drEnd")) or header.get("DR Date", "")
    info_slots["session.real_date"] = header.get("Real Date", "")
    info_slots["session.real_date_long"] = format_real_date_long(header.get("Real Date", ""))
    info_slots["timeline"] = render_timeline_slot(recap["timeline"])

    cast_text, cast_reviews = render_entity_slot(recap["cast"], note_index, entity_kind="person")
    info_slots["cast"] = cast_text
    review_lines.extend(cast_reviews)

    locations_text, location_reviews = render_location_slot(recap["locations"], note_index)
    info_slots["locations"] = locations_text
    info_slots["locations.inline"] = render_inline_location_links(recap["locations"], note_index)
    review_lines.extend(location_reviews)

    info_slots["combat.summary"] = render_combat_slot(recap["combat"])

    items_text, item_reviews = render_entity_slot(recap["items"], note_index, entity_kind="object", include_history=True)
    info_slots["items.treasure"] = items_text
    review_lines.extend(item_reviews)

    final_timeline = recap["timeline"][-1] if recap["timeline"] else None
    technical_slots["updates.whereabouts.party"] = build_party_whereabouts_slot(final_timeline)
    technical_slots["updates.whereabouts.locations"] = build_location_whereabouts_slot(recap["locations"], note_index)
    npc_updates, npc_reviews = build_entity_whereabouts_updates(recap["cast"], note_index, final_timeline)
    technical_slots["updates.whereabouts.npcs"] = npc_updates
    review_lines.extend(npc_reviews)
    technical_slots["updates.timeline"] = build_timeline_updates_slot(recap["timeline"])
    item_updates, item_update_reviews = build_item_updates_slot(recap["items"], note_index, final_timeline)
    technical_slots["updates.items"] = item_updates
    review_lines.extend(item_update_reviews)
    technical_slots["updates.review"] = render_review_lines(review_lines)

    narrative_slots["narrative.short"] = join_recap_zoom(recap["recap"], "short")
    narrative_slots["narrative.intermediate"] = join_recap_zoom(recap["recap"], "intermediate")
    narrative_slots["narrative.long"] = join_recap_zoom(recap["recap"], "long")

    return {"info": info_slots, "technical": technical_slots, "narrative": narrative_slots}


def render_timeline_slot(timeline_blocks: Sequence[Dict[str, Any]]) -> str:
    lines = []
    for block in timeline_blocks:
        key = block.get("timelineKey") or block.get("heading") or "undated"
        summary = block.get("short", "")
        if summary:
            lines.append(f"- {key}: {summary}")
    return "\n".join(lines).strip()


def render_entity_slot(
    entries: Sequence[Dict[str, Any]],
    note_index: VaultNoteIndex,
    *,
    entity_kind: str,
    include_history: bool = False,
) -> Tuple[str, List[str]]:
    lines: List[str] = []
    review_lines: List[str] = []
    for entry in entries:
        resolution = note_index.resolve(entry["name"])
        if resolution.warning:
            review_lines.append(f"- {entry['name']}: {resolution.warning}")
        display_name = resolution.link(entry["name"])
        note_context, context_reviews = build_note_context(entry, resolution, entity_kind=entity_kind)
        review_lines.extend(context_reviews)
        context_text = entry["context"]
        if note_context:
            context_text = f"{context_text}. Existing note context: {note_context}."
        lines.append(f"- {display_name}: {context_text}")
        if include_history:
            for history in entry.get("history", []):
                lines.append(f"  - {history['raw']}")
    return "\n".join(lines).strip(), dedupe_lines(review_lines)


def render_location_slot(entries: Sequence[Dict[str, Any]], note_index: VaultNoteIndex) -> Tuple[str, List[str]]:
    lines: List[str] = []
    review_lines: List[str] = []
    for entry in entries:
        resolution = note_index.resolve(entry["name"])
        if resolution.warning:
            review_lines.append(f"- {entry['name']}: {resolution.warning}")
        display_name = resolution.link(entry["name"])
        note_context, context_reviews = build_note_context(entry, resolution, entity_kind="place")
        review_lines.extend(context_reviews)
        context_text = normalize_optional_string(entry.get("summary")) or normalize_optional_string(entry.get("context")) or "TODO"
        sublocations = normalize_optional_string(entry.get("sublocations"))
        if sublocations and sublocations.casefold() != "none":
            display_name = f"{display_name} ({sublocations})"
        if note_context:
            context_text = f"{context_text}. Existing note context: {note_context}."
        lines.append(f"- {display_name}: {context_text}")
    return "\n".join(lines).strip(), dedupe_lines(review_lines)


def render_combat_slot(entries: Sequence[Dict[str, Any]]) -> str:
    if not entries:
        return "- none"
    lines: List[str] = []
    for entry in entries:
        enemies = ", ".join(entry.get("enemies", [])) or "none"
        lines.append(f"- {entry['title']}: {enemies}. {entry['contextOutcome']}")
    return "\n".join(lines).strip()


def build_party_whereabouts_slot(final_timeline: Optional[Dict[str, Any]]) -> str:
    if not final_timeline or not final_timeline.get("locations"):
        return "- none"
    final_location = final_timeline["locations"][-1]
    return (
        f"- Candidate party whereabouts: {final_timeline.get('timelineKey') or final_timeline.get('heading')}: "
        f"party ends at {format_wikilink(final_location)}."
    )


def build_location_whereabouts_slot(entries: Sequence[Dict[str, Any]], note_index: VaultNoteIndex) -> str:
    lines: List[str] = []
    for entry in entries:
        date_visited = infer_location_date_visited(entry)
        if date_visited is None:
            continue
        display_name = note_index.resolve(entry["name"]).link(entry["name"])
        lines.append(f"- {display_name}: visited on {date_visited}.")
    return "\n".join(lines).strip() or "- none"


def build_entity_whereabouts_updates(
    entries: Sequence[Dict[str, Any]],
    note_index: VaultNoteIndex,
    final_timeline: Optional[Dict[str, Any]],
) -> Tuple[str, List[str]]:
    if final_timeline is None:
        return "- none", []
    final_npcs = set(final_timeline.get("npcs", []))
    lines: List[str] = []
    review_lines: List[str] = []
    for entry in entries:
        if entry["name"] not in final_npcs:
            continue
        final_location = infer_last_history_location(entry.get("history", []))
        if final_location is None:
            review_lines.append(f"- {entry['name']}: appears in the final timeline block but has no parseable end-state history.")
            continue
        resolution = note_index.resolve(entry["name"])
        display_name = resolution.link(entry["name"])
        lines.append(
            f"- {display_name}: candidate whereabouts update from {final_timeline.get('timelineKey') or final_timeline.get('heading')} -> {format_wikilink(final_location)}."
        )
        metadata_location = resolution.simple_whereabouts()
        if metadata_location and normalize_name(metadata_location) != normalize_name(final_location):
            review_lines.append(
                f"- {display_name}: note currently says whereabouts '{metadata_location}', but the reviewed recap ends them at '{final_location}'."
            )
    return ("\n".join(lines).strip() or "- none"), dedupe_lines(review_lines)


def build_timeline_updates_slot(timeline_blocks: Sequence[Dict[str, Any]]) -> str:
    lines = [
        f"- {block.get('timelineKey') or block.get('heading')}: {block.get('short', '')}"
        for block in timeline_blocks
        if block.get("short")
    ]
    return "\n".join(lines).strip() or "- none"


def build_item_updates_slot(
    items: Sequence[Dict[str, Any]],
    note_index: VaultNoteIndex,
    final_timeline: Optional[Dict[str, Any]],
) -> Tuple[str, List[str]]:
    lines: List[str] = []
    review_lines: List[str] = []
    for entry in items:
        history = entry.get("history", [])
        if len(history) < 2:
            continue
        final_location = infer_last_history_location(history)
        if not final_location:
            continue
        resolution = note_index.resolve(entry["name"])
        display_name = resolution.link(entry["name"])
        prefix = final_timeline.get("timelineKey") if final_timeline else history[-1]["date"]
        lines.append(f"- {display_name}: candidate item-location update from {prefix} -> {format_wikilink(final_location)}.")
        metadata_location = resolution.simple_whereabouts()
        if metadata_location and normalize_name(metadata_location) != normalize_name(final_location):
            review_lines.append(
                f"- {display_name}: note currently says whereabouts '{metadata_location}', but the reviewed recap last places it at '{final_location}'."
            )
    return ("\n".join(lines).strip() or "- none"), dedupe_lines(review_lines)


def render_review_lines(lines: Sequence[str]) -> str:
    unique = dedupe_lines(lines)
    return "\n".join(unique).strip() if unique else "- none"


def join_recap_zoom(recap_blocks: Sequence[Dict[str, Any]], field_name: str) -> str:
    parts = [block[field_name].strip() for block in recap_blocks if block.get(field_name)]
    return "\n\n".join(parts).strip()


def build_note_context(entry: Dict[str, Any], resolution: ResolutionResult, *, entity_kind: str) -> Tuple[str, List[str]]:
    if resolution.note is None:
        return "", []
    metadata = resolution.note.get("frontmatter", {})
    context_bits: List[str] = []
    review_lines: List[str] = []

    if entity_kind == "person":
        if normalize_optional_string(metadata.get("ancestry")):
            context_bits.append(str(metadata["ancestry"]).strip())
        if normalize_optional_string(metadata.get("species")):
            context_bits.append(str(metadata["species"]).strip())
        if normalize_optional_string(metadata.get("gender")):
            context_bits.append(str(metadata["gender"]).strip())
        if normalize_optional_string(metadata.get("pronunciation")):
            context_bits.append(f"pronounced {str(metadata['pronunciation']).strip()}")
    elif entity_kind == "place":
        if normalize_optional_string(metadata.get("partOf")):
            context_bits.append(f"part of {metadata['partOf']}")
        if normalize_optional_string(metadata.get("whereabouts")):
            context_bits.append(f"located in {metadata['whereabouts']}")
        if normalize_optional_string(metadata.get("typeOf")):
            context_bits.append(str(metadata["typeOf"]).strip())
    elif entity_kind == "object":
        if normalize_optional_string(metadata.get("typeOf")):
            context_bits.append(str(metadata["typeOf"]).strip())
        if normalize_optional_string(metadata.get("owner")):
            context_bits.append(f"owned by {metadata['owner']}")
        if normalize_optional_string(metadata.get("whereabouts")):
            context_bits.append(f"kept in {metadata['whereabouts']}")
    else:
        if normalize_optional_string(metadata.get("typeOf")):
            context_bits.append(str(metadata["typeOf"]).strip())
        if normalize_optional_string(metadata.get("whereabouts")):
            context_bits.append(str(metadata["whereabouts"]).strip())

    return "; ".join(context_bits), review_lines


def infer_last_history_location(history: Sequence[Dict[str, str]]) -> Optional[str]:
    if not history:
        return None
    raw_location = history[-1]["location"]
    if "->" in raw_location:
        return raw_location.split("->")[-1].strip()
    return raw_location.strip() or None


def infer_location_date_visited(entry: Dict[str, Any]) -> Optional[str]:
    direct = normalize_optional_string(entry.get("dateVisited"))
    if direct is not None:
        return direct
    visits = entry.get("visits", [])
    if not visits:
        return None
    return visits[0].get("date")


def render_inline_csv_as_bullets(value: str) -> str:
    parts = [part.strip() for part in value.split(",") if part.strip()]
    return "\n".join(f"- {part}" for part in parts) if parts else "- none"


def render_inline_csv_as_links(value: str, note_index: VaultNoteIndex) -> str:
    parts = [part.strip() for part in value.split(",") if part.strip()]
    rendered = [note_index.resolve(part).link(part) for part in parts]
    return ", ".join(rendered) if rendered else "none"


def render_inline_location_links(entries: Sequence[Dict[str, Any]], note_index: VaultNoteIndex) -> str:
    names = [entry["name"] for entry in entries if entry.get("name")]
    if not names:
        return "none"
    rendered = [note_index.resolve(name).link(name) for name in names]
    if len(rendered) == 1:
        return rendered[0]
    if len(rendered) == 2:
        return f"{rendered[0]} and {rendered[1]}"
    return ", ".join(rendered[:-1]) + f", and {rendered[-1]}"


def format_real_date_long(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""
    try:
        dt = datetime.strptime(text, "%Y-%m-%d")
    except ValueError:
        return text
    return f"{dt.strftime('%A')}, {dt.strftime('%B')} {dt.day}, {dt.year}"


def render_scalar(value: Any) -> str:
    return "" if value is None else str(value).strip()


def write_component_file(path: Path, *, title: str, session_manifest: str, slots: Dict[str, str]) -> None:
    lines: List[str] = [
        "---",
        f"tags: [{AI_TAG}]",
        'excludePublish: ["all"]',
        f"sessionManifest: {json.dumps(session_manifest)}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    for slot_name, slot_body in slots.items():
        lines.append(f"<!-- SLOT: {slot_name} -->")
        if slot_body:
            lines.append(slot_body)
        lines.append("<!-- /SLOT -->")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def dedupe_notes(notes: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set[Path] = set()
    result: List[Dict[str, Any]] = []
    for note in notes:
        path = note["path"]
        if path in seen:
            continue
        seen.add(path)
        result.append(note)
    return result


def normalize_aliases(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def should_index_path(path: Path, vault_root: Path, generated_root: Path) -> bool:
    if path.is_relative_to(generated_root):
        return False
    relative = path.relative_to(vault_root)
    for part in relative.parts:
        if part.startswith(".") or part == "_sessions" or part.startswith("_"):
            return False
    return True


def read_markdown_frontmatter(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return {}
    payload = yaml.safe_load("\n".join(lines[1:end_index])) or {}
    return payload if isinstance(payload, dict) else {}


def read_yaml_mapping(path: Path) -> Dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(payload, dict):
        raise SystemExit(f"Expected a YAML mapping in {path}")
    return payload


def normalize_optional_string(value: Any) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def slugify_text(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")
    return re.sub(r"-{2,}", "-", slug)


def format_wikilink(value: str) -> str:
    text = value.strip()
    return f"[[{text}]]" if text else text


def dedupe_lines(lines: Sequence[str]) -> List[str]:
    seen: set[str] = set()
    result: List[str] = []
    for line in lines:
        normalized = line.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result


if __name__ == "__main__":
    raise SystemExit(main())

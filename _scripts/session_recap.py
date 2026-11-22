"""Parse the Markdown shared by draft recap validation and session-note rendering."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple

IMAGE_ROLES = {"aside", "figure", "hero"}
IMAGE_SIZES = {"small", "standard", "large"}


class SessionRecapParseError(Exception):
    def __init__(self, errors: Sequence[str]) -> None:
        self.errors = list(errors)
        super().__init__("\n".join(self.errors))


@dataclass
class SectionRange:
    heading: str
    start: int
    end: int


def parse_recap_body(text: str, *, header_heading: Optional[str] = None) -> Dict[str, Any]:
    lines = text.splitlines()
    errors: List[str] = []

    if not lines or lines[0].strip() != "# Session Recap":
        errors.append("Session recap must start with '# Session Recap'.")

    sections = collect_level2_sections(lines)
    if header_heading is None:
        header_heading = "## Arc Header" if "## Arc Header" in sections and "## Session Header" not in sections else "## Session Header"
    required_sections = [
        header_heading,
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

    header = parse_header_section(get_section_lines(lines, sections[header_heading]), header_heading[3:], errors)
    timeline = (
        parse_timeline_section(get_section_lines(lines, sections["## Timeline"]), errors)
        if "## Timeline" in sections
        else []
    )
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
    related_writings = parse_related_writings(
        get_section_lines(lines, sections["## Related Writings"])
        if "## Related Writings" in sections else [],
        errors,
    )
    pull_quotes = parse_review_entries(
        get_section_lines(lines, sections["## Pull Quotes"]) if "## Pull Quotes" in sections else [],
        label="Pull Quotes",
        required=("ID", "Quote", "Speaker", "Source Lines"),
        errors=errors,
    )
    audio_highlights = parse_review_entries(
        get_section_lines(lines, sections["## Audio Highlights"]) if "## Audio Highlights" in sections else [],
        label="Audio Highlights",
        required=("ID", "Speaker", "Source Lines"),
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
        "relatedWritings": related_writings,
        "pullQuotes": pull_quotes,
        "audioHighlights": audio_highlights,
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


def parse_related_writings(lines: Sequence[str], errors: List[str]) -> List[str]:
    links: List[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if not stripped.startswith("- [[") or not stripped.endswith("]]"):
            errors.append(f"Related Writings expects a wikilink bullet: {line}")
            continue
        links.append(stripped)
    return links


def parse_header_section(lines: Sequence[str], label: str, errors: List[str]) -> Dict[str, str]:
    data = parse_keyed_bullets(lines, label=label, errors=errors)
    required = [
        "Title",
        "Desc Title",
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
            errors.append(f"{label} is missing '{key}'.")
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
                "long": parse_subsection(block_lines, "#### Long") or "",
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
                "images": parse_recap_images(data, f"recap {match.group('block_id')}", errors),
                "short": parse_subsection(block_lines, "#### Short") or "",
                "intermediate": parse_subsection(block_lines, "#### Intermediate") or "",
                "long": parse_subsection(block_lines, "#### Long") or "",
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


def parse_recap_images(data: Dict[str, str], label: str, errors: List[str]) -> List[Dict[str, str]]:
    image_numbers: List[int] = []
    if "Image" in data or "Image 1" in data:
        image_numbers.append(1)
    image_numbers.extend(
        sorted(
            int(match.group(1))
            for key in data
            if (match := re.fullmatch(r"Image (\d+)", key)) and int(match.group(1)) > 1
        )
    )

    images: List[Dict[str, str]] = []
    for number in image_numbers:
        image_key = "Image" if number == 1 and "Image" in data else f"Image {number}"
        image_value = normalize_optional_string(data.get(image_key))
        if image_value is None or image_value.casefold() == "none":
            continue

        path, render_from_embed = parse_image_path_and_render(image_value)
        if not path:
            errors.append(f"{label} has an empty {image_key} value.")
            continue

        prefix = image_key
        role = normalize_image_role(data.get(f"{prefix} Role"))
        render = normalize_optional_string(data.get(f"{prefix} Render")) or render_from_embed or ""
        _align, render_size, _remaining = parse_semantic_image_render(render)
        size = normalize_image_size(data.get(f"{prefix} Size")) or render_size or ""
        placement = normalize_optional_string(data.get(f"{prefix} Placement"))
        if placement is None:
            placement = "end" if role in {"figure", "hero"} else "start"
        placement = placement.casefold()
        if placement in {"before", "top", "beginning"}:
            placement = "start"
        elif placement in {"after", "bottom"}:
            placement = "end"
        if placement not in {"start", "end"}:
            errors.append(f"{label} {image_key} Placement must be 'start' or 'end', got {placement!r}.")
            placement = "start"

        images.append(
            {
                "path": path,
                "placement": placement,
                "render": render,
                "caption": normalize_optional_string(data.get(f"{prefix} Caption")) or "",
                "role": role or "",
                "size": size,
                "alt": normalize_optional_string(data.get(f"{prefix} Alt")) or "",
            }
        )
    return images


def normalize_image_role(value: Any) -> Optional[str]:
    role = (normalize_optional_string(value) or "").casefold()
    return role if role in IMAGE_ROLES else None


def normalize_image_size(value: Any) -> Optional[str]:
    size = (normalize_optional_string(value) or "").casefold()
    return size if size in IMAGE_SIZES else None


def parse_image_path_and_render(value: str) -> Tuple[str, str]:
    text = value.strip()
    match = re.fullmatch(r"!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", text)
    if match:
        return match.group(1).strip(), (match.group(2) or "").strip()
    return text, ""


def parse_review_entries(
    lines: Sequence[str],
    *,
    label: str,
    required: Sequence[str],
    errors: List[str],
) -> List[Dict[str, str]]:
    entries: List[Dict[str, str]] = []
    current: Optional[Dict[str, str]] = None
    seen_ids: set[str] = set()

    for raw_line in lines:
        if not raw_line.strip():
            continue
        stripped = raw_line.strip()
        if stripped in {"- none", "None identified.", "- None identified."}:
            continue
        if raw_line.startswith("- ID:"):
            entry_id = raw_line.split(":", 1)[1].strip()
            if not entry_id:
                errors.append(f"{label} contains an entry with an empty ID.")
                current = None
                continue
            if entry_id in seen_ids:
                errors.append(f"{label} contains duplicate ID {entry_id!r}.")
            seen_ids.add(entry_id)
            current = {"ID": entry_id}
            entries.append(current)
            continue
        if raw_line.startswith("  - "):
            if current is None:
                errors.append(f"{label} contains a detail line before any ID: {stripped}")
                continue
            if ":" not in stripped:
                errors.append(f"{label} contains a malformed detail line: {stripped}")
                continue
            key, value = stripped[2:].split(":", 1)
            current[key.strip()] = value.strip()
            continue
        errors.append(f"{label} contains an unparseable line: {stripped}")

    for entry in entries:
        for key in required:
            if not normalize_optional_string(entry.get(key)):
                errors.append(f"{label} entry {entry.get('ID', '<unknown>')} is missing {key}.")
    return entries


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
                "displayName": entry["displayName"],
                "summary": entry["context"],
                "sublocations": None,
                "dateVisited": None,
                "visits": [],
                "legacyFormat": True,
            }
        else:
            raw_name = body.strip()
            current = {
                "name": normalize_wikilink_name(raw_name),
                "displayName": wikilink_display_name(raw_name),
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
    raw_name = match.group("name").strip()
    return {
        "name": normalize_wikilink_name(raw_name),
        "displayName": wikilink_display_name(raw_name),
        "relation": (match.groupdict().get("relation") or "").strip(),
        "context": match.group("context").strip(),
    }


def parse_history_line(body: str, label: str, errors: List[str]) -> Optional[Dict[str, str]]:
    if ", " not in body:
        errors.append(f"{label} history line is malformed: {body}")
        return None
    location, date_text = body.rsplit(", ", 1)
    return {"raw": body, "location": normalize_wikilink_name(location.strip()), "date": date_text.strip()}


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
    return [normalize_wikilink_name(item.strip()) for item in stripped.split(",") if item.strip()]


def normalize_wikilink_name(value: str) -> str:
    text = value.strip()
    match = re.fullmatch(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", text)
    if not match:
        return text
    return (match.group(1) or "").strip()


def wikilink_display_name(value: str) -> str:
    text = value.strip()
    match = re.fullmatch(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", text)
    if not match:
        return text
    return (match.group(2) or match.group(1) or "").strip()


def parse_semantic_image_render(render: str) -> Tuple[str, str, str]:
    align = ""
    size = ""
    remaining: List[str] = []
    for raw_token in render.split("|"):
        token = raw_token.strip()
        lowered = token.casefold()
        if not token:
            continue
        if lowered in {"left", "right"} and not align:
            align = lowered
        elif lowered in IMAGE_SIZES and not size:
            size = lowered
        else:
            remaining.append(token)
    return align, size, "|".join(remaining)


def normalize_optional_string(value: Any) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text or None

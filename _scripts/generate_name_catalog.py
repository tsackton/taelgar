#!/usr/bin/env python3
"""Generate the Taelgar name catalog.

The catalog is deliberately note-based: it indexes every note with frontmatter
tags, except notes in Worldbuilding or underscore-prefixed directories. It does
not attempt named entity recognition across general prose.

Outputs:

* ``_Plugins/Name Explorer/Name Catalog.md``: human-browsable tables grouped by
  in-world language.
* ``_Plugins/Name Explorer/Name Catalog.jsonl``: one machine-readable JSON
  object per note.

Only the Python standard library is required. The frontmatter reader is narrow
but tolerant of the vault's YAML-like conventions, including inline and
multi-line lists.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


NOTE_TYPES: tuple[str, ...] = (
    "person",
    "power",
    "place",
    "event",
    "object",
    "group",
    "ancestry",
    "creature",
    "session-note",
    "source",
    "background",
    "meta",
)

TAG_ORDER = {tag: idx for idx, tag in enumerate(NOTE_TYPES)}

LANGUAGE_KEYWORDS: tuple[tuple[tuple[str, ...], str, str], ...] = (
    (("katonylev", "army tongue"), "Goblin", "Katonylev"),
    (("hobgoblin", "goblin"), "Goblin", "Goblin/Katonylev"),
    (("svolhasian", "svolhas"), "Unclassified", "Svolhasian"),
    (("drankorian", "drankor"), "Drankorian", "Drankorian"),
    (("chardonian", "chardon"), "Drankorian", "Chardonian"),
    (("cymean", "cymea"), "Drankorian", "Cymean"),
    (("isinguese", "isinguer", "isingue"), "Drankorian", "Isinguese"),
    (("illorian", "illoria"), "Drankorian", "Illorian"),
    (("deno'qai", "deno’qai"), "Northros", "Deno'qai"),
    (("mawaran", "mawar"), "Northros", "Mawaran"),
    (("vargaldi",), "Northros", "Vargaldi"),
    (("old zimkovan",), "Northros", "Old Zimkovan"),
    (("northros",), "Northros", "Unclassified Northros"),
    (("skaegish", "skaer"), "Eastros", "Skaegish"),
    (("urksan", "urskan", "ursk"), "Eastros", "Urskan"),
    (("old tollish",), "Eastros", "Old Tollish"),
    (("zimkovan", "zimka"), "Eastros", "Zimkovan"),
    (("semb aran", "sembaran", "sembara"), "Eastros", "Sembaran"),
    (("tollish", "tollender", "tollen"), "Eastros", "Tollish"),
    (("eastros",), "Eastros", "Unclassified Eastros"),
    (("dunmari", "dunmar"), "Independent human", "Dunmari"),
    (("tyrwinghan", "tyrwingha"), "Independent human", "Tyrwinghan"),
    (("vosic", "vostok", "vos "), "Mixed/uncertain human", "Vosic"),
    (("hkaran", "hkar"), "Hkaran", "Hkaran"),
    (("dwarvish", "dwarven", "dwarf"), "Non-human", "Dwarvish"),
    (("elvish", "elven", "elf"), "Non-human", "Elvish"),
    (("lizardling", "lizardfolk"), "Non-human", "Lizardling"),
    (("free orcish", "free orc"), "Non-human", "Free Orcish"),
    (("orcish", "orc "), "Non-human", "Orcish"),
    (("stoneborn",), "Non-human", "Stoneborn"),
    (("halfling",), "Non-human", "Halfling"),
    (("giant",), "Exotic", "Giant"),
    (("kenku",), "Exotic", "Kenku"),
    (("merfolk",), "Exotic", "Merfolk"),
    (("centaur",), "Exotic", "Centaur"),
    (("gnoll",), "Exotic", "Gnoll"),
    (("sylvan", "fey "), "Extraplanar", "Sylvan"),
    (("primordial", "elemental"), "Extraplanar", "Primordial"),
    (("common",), "Trade", "Common"),
)

ANCESTRY_LANGUAGE_RULES: tuple[tuple[tuple[str, ...], str, str], ...] = (
    (("deno'qai", "deno’qai"), "Northros", "Deno'qai"),
    (("mawaran",), "Northros", "Mawaran"),
    (("vargaldi",), "Northros", "Vargaldi"),
    (("zimka", "zimkovan"), "Eastros", "Zimkovan"),
    (("semb aran", "sembaran", "addermarian"), "Eastros", "Sembaran"),
    (("tollish", "tollender", "tollen"), "Eastros", "Tollish"),
    (("skaer",), "Eastros", "Skaegish"),
    (("urskan", "urksan"), "Eastros", "Urskan"),
    (("chardonian", "apporian"), "Drankorian", "Chardonian"),
    (("drankorian",), "Drankorian", "Drankorian"),
    (("cymean",), "Drankorian", "Cymean"),
    (
        ("isinguer", "isinguese", "aurbeze", "mazeanne", "maseaun"),
        "Drankorian",
        "Isinguese",
    ),
    (("illorian",), "Drankorian", "Illorian"),
    (("dunmari",), "Independent human", "Dunmari"),
    (("tyrwinghan",), "Independent human", "Tyrwinghan"),
    (("vos", "vosic"), "Mixed/uncertain human", "Vosic"),
    (("hkaran",), "Hkaran", "Hkaran"),
    (("dwarven", "dwarf"), "Non-human", "Dwarvish"),
    (("elven", "elf"), "Non-human", "Elvish"),
    (("lizardfolk",), "Non-human", "Lizardling"),
    (("free orc",), "Non-human", "Free Orcish"),
    (("orcish", "orc"), "Non-human", "Orcish"),
    (("hobgoblin", "goblin"), "Goblin", "Goblin/Katonylev"),
    (("stoneborn",), "Non-human", "Stoneborn"),
    (("halfling",), "Non-human", "Halfling"),
    (("frost giant", "giant"), "Exotic", "Giant"),
    (("kenku",), "Exotic", "Kenku"),
    (("merfolk",), "Exotic", "Merfolk"),
    (("centaur",), "Exotic", "Centaur"),
    (("fey",), "Extraplanar", "Sylvan"),
)

PATH_LANGUAGE_RULES: tuple[tuple[str, str, str], ...] = (
    ("People/Deno'qai/", "Northros", "Deno'qai"),
    ("People/Mawarans/", "Northros", "Mawaran"),
    ("People/Sembarans/", "Eastros", "Sembaran"),
    ("People/Addermarians/", "Eastros", "Sembaran"),
    ("People/Maseauns/", "Drankorian", "Isinguese"),
    ("People/Chardonians/", "Drankorian", "Chardonian"),
    ("People/Dunmari/", "Independent human", "Dunmari"),
    ("People/Dwarves/", "Non-human", "Dwarvish"),
    ("People/Elves/", "Non-human", "Elvish"),
    ("People/Giants/", "Exotic", "Giant"),
    ("People/Halflings/", "Non-human", "Halfling"),
    ("People/Kenku/", "Exotic", "Kenku"),
    ("People/Lizardfolk/", "Non-human", "Lizardling"),
    ("People/Orcs/", "Non-human", "Orcish"),
    ("People/Skaer/", "Eastros", "Skaegish"),
    ("People/Tollenders/", "Eastros", "Tollish"),
    ("People/Tyrwinghans/", "Independent human", "Tyrwinghan"),
    ("Groups/Dwarven ", "Non-human", "Dwarvish"),
    ("Groups/Dwarven/", "Non-human", "Dwarvish"),
    ("Groups/Hobgoblin Clans/", "Goblin", "Goblin/Katonylev"),
    ("Groups/Orc Hordes/", "Non-human", "Orcish"),
    ("Groups/Sembaran ", "Eastros", "Sembaran"),
    ("Groups/Tollen ", "Eastros", "Tollish"),
    ("Groups/Urskan ", "Eastros", "Urskan"),
    ("Gazetteer/Drankorian Hinterland/", "Drankorian", "Drankorian"),
    ("Gazetteer/Greater Chardon/Chardonian Empire/", "Drankorian", "Chardonian"),
    ("Gazetteer/Greater Chardon/", "Drankorian", "Chardonian"),
    ("Gazetteer/Upper Istaros/", "Drankorian", "Isinguese"),
    ("Gazetteer/Western Green Sea/Cymea/", "Drankorian", "Cymean"),
    ("Gazetteer/Greater Sembara/Tyrwingha/", "Independent human", "Tyrwinghan"),
    ("Gazetteer/Greater Sembara/Vostok/", "Mixed/uncertain human", "Vosic"),
    ("Gazetteer/Greater Sembara/", "Eastros", "Sembaran"),
    ("Gazetteer/Greater Dunmar/", "Independent human", "Dunmari"),
    ("Gazetteer/Northwest Coast/Mawar", "Northros", "Mawaran"),
    ("Gazetteer/Northwest Coast/Northern Provinces/", "Drankorian", "Chardonian"),
    ("Gazetteer/Northern Green Sea/Ursk", "Eastros", "Urskan"),
    ("Gazetteer/Northern Green Sea/Skaer", "Eastros", "Skaegish"),
    ("Gazetteer/Central Highlands/Dwarven", "Non-human", "Dwarvish"),
    ("Gazetteer/Extraplanar/Feywild/", "Extraplanar", "Sylvan"),
)

LOCATION_LANGUAGE_RULES: tuple[tuple[tuple[str, ...], str, str], ...] = (
    (("elderwood", "forest of dreams"), "Northros", "Deno'qai"),
    (("mawakel", "mawar"), "Northros", "Mawaran"),
    (("sembara", "addermarch"), "Eastros", "Sembaran"),
    (("tollen",), "Eastros", "Tollish"),
    (("skaerhem",), "Eastros", "Skaegish"),
    (("ursk",), "Eastros", "Urskan"),
    (("chardon", "chardonian empire"), "Drankorian", "Chardonian"),
    (("cymea",), "Drankorian", "Cymean"),
    (("isingue", "aurbez", "maseau"), "Drankorian", "Isinguese"),
    (("dunmar",), "Independent human", "Dunmari"),
    (("tyrwingha",), "Independent human", "Tyrwinghan"),
    (("vostok",), "Mixed/uncertain human", "Vosic"),
    (("feywild",), "Extraplanar", "Sylvan"),
)

COMMON_DESCRIPTOR_WORDS = {
    "abbey",
    "alliance",
    "army",
    "archipelago",
    "archive",
    "barony",
    "battle",
    "bay",
    "bridge",
    "canal",
    "castle",
    "cavern",
    "city",
    "clan",
    "cliffs",
    "coast",
    "company",
    "confederacy",
    "county",
    "crossing",
    "desert",
    "duchy",
    "empire",
    "falls",
    "fellowship",
    "fens",
    "forest",
    "fort",
    "fortress",
    "freehold",
    "gap",
    "garden",
    "gate",
    "gorge",
    "guild",
    "gulf",
    "hall",
    "harbor",
    "haven",
    "heights",
    "highlands",
    "hill",
    "hills",
    "hold",
    "house",
    "inn",
    "island",
    "islands",
    "isle",
    "isles",
    "kingdom",
    "lake",
    "lands",
    "library",
    "manor",
    "march",
    "marsh",
    "mine",
    "monastery",
    "mount",
    "mountain",
    "mountains",
    "ocean",
    "order",
    "palace",
    "pass",
    "peak",
    "plains",
    "plateau",
    "port",
    "province",
    "range",
    "realm",
    "republic",
    "river",
    "road",
    "sea",
    "settlement",
    "siege",
    "society",
    "spring",
    "stones",
    "strait",
    "swamp",
    "temple",
    "tower",
    "trail",
    "university",
    "vale",
    "valley",
    "village",
    "war",
    "waters",
    "watershed",
    "wood",
    "woods",
}

COMMON_COMPOUND_PARTS = {
    "black",
    "blood",
    "bone",
    "bronze",
    "cleaver",
    "copper",
    "crown",
    "dark",
    "dream",
    "fang",
    "fire",
    "flood",
    "flower",
    "frost",
    "gem",
    "green",
    "grey",
    "hammer",
    "heart",
    "ice",
    "iron",
    "light",
    "mist",
    "moon",
    "reaver",
    "red",
    "shadow",
    "silver",
    "skull",
    "sky",
    "snake",
    "star",
    "stone",
    "storm",
    "sun",
    "thorn",
    "water",
    "white",
    "wild",
    "wind",
    "wolf",
}


@dataclass(frozen=True)
class Language:
    family: str
    language: str
    confidence: str
    basis: str

    def as_dict(self) -> dict[str, str]:
        return {
            "family": self.family,
            "language": self.language,
            "confidence": self.confidence,
            "basis": self.basis,
        }


UNKNOWN_LANGUAGE = Language(
    "Unknown",
    "Unknown",
    "unknown",
    "No reliable language evidence found",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Vault root (default: current directory)",
    )
    parser.add_argument(
        "--markdown",
        default="_Plugins/Name Explorer/Name Catalog.md",
        help="Markdown output path, relative to root",
    )
    parser.add_argument(
        "--jsonl",
        default="_Plugins/Name Explorer/Name Catalog.jsonl",
        help="JSONL output path, relative to root",
    )
    return parser.parse_args()


def split_frontmatter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        return [], text
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[1:idx], "\n".join(lines[idx + 1 :])
    return [], text


def strip_inline_comment(value: str) -> str:
    quote: str | None = None
    depth = 0
    for idx, char in enumerate(value):
        if quote:
            if char == quote and (idx == 0 or value[idx - 1] != "\\"):
                quote = None
            continue
        if char in {"'", '"'}:
            quote = char
        elif char in "[{(":
            depth += 1
        elif char in "]})":
            depth = max(0, depth - 1)
        elif char == "#" and depth == 0 and idx and value[idx - 1].isspace():
            return value[:idx].rstrip()
    return value.rstrip()


def strip_scalar(value: str) -> str:
    value = strip_inline_comment(value.strip())
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip()


def split_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        scalar = strip_scalar(value)
        return [scalar] if scalar else []
    inner = value[1:-1]
    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None
    depth = 0
    for idx, char in enumerate(inner):
        if quote:
            current.append(char)
            if char == quote and (idx == 0 or inner[idx - 1] != "\\"):
                quote = None
            continue
        if char in {"'", '"'}:
            quote = char
            current.append(char)
        elif char in "[{(":
            depth += 1
            current.append(char)
        elif char in "]})":
            depth = max(0, depth - 1)
            current.append(char)
        elif char == "," and depth == 0:
            item = strip_scalar("".join(current))
            if item:
                parts.append(item)
            current = []
        else:
            current.append(char)
    item = strip_scalar("".join(current))
    if item:
        parts.append(item)
    return parts


def parse_frontmatter(frontmatter: Sequence[str]) -> dict[str, object]:
    """Parse the small top-level subset needed by the catalog."""
    fields: dict[str, object] = {}
    idx = 0
    while idx < len(frontmatter):
        raw = frontmatter[idx]
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", raw)
        if not match:
            idx += 1
            continue
        key, raw_value = match.group(1), (match.group(2) or "")
        if raw_value:
            if raw_value.lstrip().startswith("["):
                fields[key] = split_inline_list(raw_value)
            else:
                fields[key] = strip_scalar(raw_value)
            idx += 1
            continue

        values: list[str] = []
        next_idx = idx + 1
        while next_idx < len(frontmatter):
            child = frontmatter[next_idx]
            if re.match(r"^[A-Za-z][A-Za-z0-9_-]*:", child):
                break
            child_match = re.match(r"^\s*-\s+(.*)$", child)
            if child_match:
                item = strip_scalar(child_match.group(1))
                if item:
                    values.append(item)
            next_idx += 1
        fields[key] = values
        idx = next_idx
    return fields


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def as_scalar(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return strip_scalar(str(value[0])) if value else ""
    return strip_scalar(str(value))


def normalize_tag(tag: str) -> str:
    return tag.strip().strip("'\"").lstrip("#").strip().lower()


def choose_note_type(tags: Sequence[str]) -> str:
    tag_set = {normalize_tag(tag) for tag in tags}
    base_tags = {tag.split("/", 1)[0] for tag in tag_set}
    for note_type in NOTE_TYPES:
        if note_type in tag_set or note_type in base_tags:
            return note_type
    return "unknown"


def should_scan(path: Path) -> bool:
    directory_parts = path.parts[:-1]
    if path.parts and path.parts[0] == "Worldbuilding":
        return False
    return not any(
        part.startswith("_") or part.startswith(".")
        for part in directory_parts
    )


def iter_markdown(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if path.is_file():
            rel = path.relative_to(root)
            if should_scan(rel):
                yield path


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.replace("’", "'").casefold()
    value = re.sub(r"\bthe\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_alias(value: str) -> str:
    value = re.sub(r"!\[\[[^\]]+\]\]", "", value)
    value = re.sub(r"\[\[([^]|]+)\|([^]]+)\]\]", r"\2", value)
    value = re.sub(r"\[\[([^]]+)\]\]", r"\1", value)
    value = value.strip().strip("*_`\"'“”‘’")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" ,;:.")


def plausible_alias(value: str) -> bool:
    if not value or len(value) > 90 or len(value) < 2:
        return False
    if value.count(" ") > 9:
        return False
    if any(token in value for token in ("$=", "dv.view", "<", ">", "::")):
        return False
    if value.casefold() in {"names", "name", "information", "dm notes"}:
        return False
    if re.search(r"[.!?]\s", value):
        return False
    return bool(re.search(r"[A-Za-zÀ-ž]", value))


def remove_obsidian_comments(text: str) -> str:
    return re.sub(r"%%.*?%%", "", text, flags=re.DOTALL)


def extract_text_aliases(body: str, primary: str) -> list[dict[str, object]]:
    """Conservatively extract headings and explicit naming statements."""
    cleaned = remove_obsidian_comments(body)
    cleaned = re.split(
        r"^##\s+DM\s+notes?\s*$",
        cleaned,
        maxsplit=1,
        flags=re.IGNORECASE | re.MULTILINE,
    )[0]
    lines = cleaned.splitlines()
    candidates: list[dict[str, object]] = []

    for line_no, line in enumerate(lines[:80], start=1):
        if line.startswith("# "):
            heading = clean_alias(line[2:])
            if plausible_alias(heading) and normalize_name(heading) != normalize_name(primary):
                candidates.append(
                    {
                        "name": heading,
                        "source": "heading",
                        "line": line_no,
                        "evidence": line.strip(),
                    }
                )
            break

    called_quote_pattern = re.compile(
        r"\b(?:also\s+known\s+as|known\s+as|called|named)\s+"
        r"[“\"]([^”\"\n]{2,90})[”\"]",
        flags=re.IGNORECASE,
    )
    called_bold_pattern = re.compile(
        r"\b(?:also\s+known\s+as|known\s+as|called|named)\s+"
        r"(?:the\s+)?\*\*([^*\n]{2,90})\*\*",
        flags=re.IGNORECASE,
    )

    for line_no, line in enumerate(lines, start=1):
        # Requiring the primary name on the same line prevents a quoted nickname
        # or bold table cell belonging to another subject from becoming an alias
        # of the note itself.
        if f" {normalize_name(primary)} " not in f" {normalize_name(line)} ":
            continue
        for pattern in (called_quote_pattern, called_bold_pattern):
            for match in pattern.finditer(line):
                alias = clean_alias(match.group(1))
                if (
                    plausible_alias(alias)
                    and normalize_name(alias) != normalize_name(primary)
                ):
                    candidates.append(
                        {
                            "name": alias,
                            "source": "text",
                            "line": line_no,
                            "evidence": line.strip()[:280],
                        }
                    )

    output: list[dict[str, object]] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = normalize_name(str(candidate["name"]))
        if not key or key in seen:
            continue
        seen.add(key)
        output.append(candidate)
    return output


def language_from_context(context: str, basis: str) -> Language | None:
    lowered = f" {context.casefold()} "
    for keywords, family, language in LANGUAGE_KEYWORDS:
        if any(keyword in lowered for keyword in keywords):
            return Language(family, language, "explicit", basis)
    return None


def language_from_naming_context(
    context: str,
    name: str,
    basis: str,
) -> Language | None:
    """Read only linguistic constructions, not arbitrary nearby place words."""
    context_without_name = re.sub(
        re.escape(name),
        " ",
        context,
        flags=re.IGNORECASE,
    )
    lowered = (
        context_without_name.casefold()
        .replace("[[", " ")
        .replace("]]", " ")
    )
    for keywords, family, language in LANGUAGE_KEYWORDS:
        for keyword in keywords:
            keyword = keyword.strip()
            escaped = re.escape(keyword)
            patterns = (
                rf"\bin\s+(?:the\s+)?{escaped}\b",
                rf"\b{escaped}\b[^.;:]{{0,35}}"
                rf"\b(?:name|term|phrase|word|exonym|endonym|translation)\b",
                rf"\b(?:name|term|phrase|word|exonym|endonym|translation)\b"
                rf"[^.;:]{{0,55}}\b{escaped}\b",
            )
            if any(re.search(pattern, lowered) for pattern in patterns):
                return Language(family, language, "explicit", basis)
    return None


def explicit_language_for_name(body: str, name: str, label: str) -> Language | None:
    """Find and rank lines that explicitly identify a name form's language."""
    needle = normalize_name(name)
    if not needle:
        return None
    naming_words = re.compile(
        r"\b(?:name|called|known|rendered|translated|translation|term|"
        r"phrase|word|exonym|endonym|in\s+common|locally)\b",
        flags=re.IGNORECASE,
    )
    candidates: list[tuple[int, Language]] = []
    in_comment = False
    in_names_section = False
    for line_no, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if re.match(r"^##\s+Names?\s*$", stripped, flags=re.IGNORECASE):
            in_names_section = True
        elif in_names_section and re.match(r"^##\s+", stripped):
            in_names_section = False

        marker_count = line.count("%%")
        line_is_comment = in_comment or marker_count > 0
        haystack = f" {normalize_name(line)} "
        if f" {needle} " in haystack and naming_words.search(line):
            suffix = " (comment)" if line_is_comment else ""
            explicit = language_from_naming_context(
                line,
                name,
                f"{label}, body line {line_no}{suffix}",
            )
            if explicit:
                score = 0
                if re.search(r"\bin\s+(?:the\s+)?common\b", line, re.IGNORECASE):
                    score += 8
                if in_names_section:
                    score += 5
                if re.search(
                    r"\b(?:name|term|phrase|word|exonym|endonym|translation)\b",
                    line,
                    re.IGNORECASE,
                ):
                    score += 4
                if re.search(r"\b(?:called|known)\b", line, re.IGNORECASE):
                    score += 2
                if line_is_comment:
                    score -= 1
                candidates.append((score, explicit))
        if marker_count % 2:
            in_comment = not in_comment

    if not candidates:
        return None
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1]


def looks_common(name: str) -> bool:
    words = re.findall(r"[A-Za-z]+", normalize_name(name))
    if any(word in COMMON_DESCRIPTOR_WORDS for word in words):
        return True
    squashed = "".join(words)
    matches = sum(part in squashed for part in COMMON_COMPOUND_PARTS)
    return matches >= 2


def language_from_ancestry(values: Sequence[str], basis_prefix: str) -> Language | None:
    lowered = " ".join(values).casefold()
    for keywords, family, language in ANCESTRY_LANGUAGE_RULES:
        if any(keyword in lowered for keyword in keywords):
            return Language(
                family,
                language,
                "inferred",
                f"{basis_prefix}: {', '.join(values)}",
            )
    return None


def language_from_path(path: str) -> Language | None:
    for fragment, family, language in PATH_LANGUAGE_RULES:
        if fragment in path:
            return Language(
                family,
                language,
                "inferred",
                f"vault path: {fragment.rstrip('/')}",
            )
    return None


def extract_locations(frontmatter: Sequence[str], fields: dict[str, object]) -> list[str]:
    values = as_list(fields.get("whereabouts"))
    for line in frontmatter:
        for match in re.finditer(r"\blocation:\s*([^,}\]]+)", line):
            location = strip_scalar(match.group(1))
            if location:
                values.append(location)
    return list(dict.fromkeys(values))


def language_from_locations(locations: Sequence[str]) -> Language | None:
    lowered = " ".join(locations).casefold()
    for keywords, family, language in LOCATION_LANGUAGE_RULES:
        if any(keyword in lowered for keyword in keywords):
            return Language(
                family,
                language,
                "inferred",
                f"whereabouts: {', '.join(locations)}",
            )
    return None


def infer_primary_language(
    name: str,
    note_type: str,
    path: str,
    fields: dict[str, object],
    frontmatter: Sequence[str],
    body: str,
) -> Language:
    explicit = explicit_language_for_name(body, name, "explicit primary-name text")
    if explicit:
        return explicit

    ancestry_values = as_list(fields.get("ancestry"))
    species_values = as_list(fields.get("species")) + as_list(fields.get("subspecies"))

    if note_type != "person" and looks_common(name):
        return Language(
            "Trade",
            "Common",
            "inferred",
            "descriptive or translated Common-form name",
        )

    inferred = language_from_ancestry(ancestry_values, "ancestry")
    if inferred:
        return inferred
    inferred = language_from_ancestry(species_values, "species")
    if inferred:
        return inferred
    inferred = language_from_path(path)
    if inferred:
        return inferred

    locations = extract_locations(frontmatter, fields)
    inferred = language_from_locations(locations)
    if inferred:
        return inferred

    if looks_common(name):
        return Language(
            "Trade",
            "Common",
            "inferred",
            "descriptive or translated Common-form name",
        )
    return UNKNOWN_LANGUAGE


def alias_language(
    alias: dict[str, object],
    primary_name: str,
    primary_language: Language,
    body: str,
) -> Language:
    explicit = explicit_language_for_name(
        body,
        str(alias["name"]),
        "explicit alias text",
    )
    if explicit:
        return explicit
    evidence = str(alias.get("evidence", ""))
    explicit_from_evidence = language_from_naming_context(
        evidence,
        str(alias["name"]),
        f"explicit alias text, body line {alias.get('line')}",
    )
    if explicit_from_evidence:
        return explicit_from_evidence
    alias_name = str(alias["name"])
    if normalize_name(alias_name) == normalize_name(primary_name):
        return Language(
            primary_language.family,
            primary_language.language,
            primary_language.confidence,
            "orthographic variant of primary name",
        )
    if looks_common(alias_name):
        return Language(
            "Trade",
            "Common",
            "inferred",
            "descriptive or translated Common-form alias",
        )
    if primary_language.language != "Unknown":
        return Language(
            primary_language.family,
            primary_language.language,
            "inferred",
            "same-note naming context; alias language is not explicit",
        )
    return UNKNOWN_LANGUAGE


def make_record(root: Path, path: Path) -> dict[str, object] | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    frontmatter, body = split_frontmatter(text)
    fields = parse_frontmatter(frontmatter)
    rel = path.relative_to(root)
    rel_path = rel.as_posix()
    tags = [normalize_tag(tag) for tag in as_list(fields.get("tags"))]
    if not tags:
        return None
    record_note_type = choose_note_type(tags)

    raw_name = as_scalar(fields.get("name"))
    name = raw_name or path.stem
    pronunciation = as_scalar(fields.get("pronunciation"))
    text_aliases = extract_text_aliases(body, name)

    aliases: list[dict[str, object]] = []
    seen_aliases = {normalize_name(name)}
    text_aliases_by_key = {
        normalize_name(str(alias["name"])): alias for alias in text_aliases
    }
    for raw_alias in as_list(fields.get("aliases")):
        cleaned = clean_alias(raw_alias)
        key = normalize_name(cleaned)
        if plausible_alias(cleaned) and key and key not in seen_aliases:
            seen_aliases.add(key)
            text_match = text_aliases_by_key.get(key)
            aliases.append(
                {
                    "name": cleaned,
                    "source": "frontmatter+text" if text_match else "frontmatter",
                    "line": text_match.get("line") if text_match else None,
                    "evidence": text_match.get("evidence", "") if text_match else "",
                }
            )
    for alias in text_aliases:
        key = normalize_name(str(alias["name"]))
        if key and key not in seen_aliases:
            seen_aliases.add(key)
            aliases.append(alias)

    primary_language = infer_primary_language(
        name,
        record_note_type,
        rel_path,
        fields,
        frontmatter,
        body,
    )
    alias_records: list[dict[str, object]] = []
    for alias in aliases:
        language = alias_language(alias, name, primary_language, body)
        alias_records.append(
            {
                **alias,
                "normalized": normalize_name(str(alias["name"])),
                "language": language.as_dict(),
            }
        )

    return {
        "name": name,
        "normalized": normalize_name(name),
        "file_name": path.stem,
        "path": rel_path,
        "link_target": rel.with_suffix("").as_posix(),
        "note_type": record_note_type,
        "language": primary_language.as_dict(),
        "status_check_name": "status/check/name" in set(tags),
        "pronunciation": pronunciation,
        "aliases": alias_records,
        "tags": tags,
    }


def build_records(root: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in iter_markdown(root):
        try:
            record = make_record(root, path)
        except OSError:
            continue
        if record:
            records.append(record)
    records.sort(
        key=lambda record: (
            str(record["language"]["family"]).casefold(),
            str(record["language"]["language"]).casefold(),
            TAG_ORDER.get(str(record["note_type"]), 999),
            str(record["name"]).casefold(),
            str(record["path"]).casefold(),
        )
    )
    return records


def jsonl_text(records: Sequence[dict[str, object]]) -> str:
    return "\n".join(
        json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records
    ) + "\n"


def escape_table(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def link_for(record: dict[str, object]) -> str:
    target = str(record["link_target"])
    name = escape_table(record["name"])
    return f"[[{target}\\|{name}]]"


def aliases_label(record: dict[str, object]) -> str:
    values: list[str] = []
    for alias in record["aliases"]:
        marker = "†" if alias["source"] in {"text", "heading"} else ""
        language = alias["language"]
        language_label = ""
        if language["language"] != "Unknown":
            language_label = f" ({language['language']})"
        values.append(f"{alias['name']}{marker}{language_label}")
    return "; ".join(values)


def markdown_text(records: Sequence[dict[str, object]]) -> str:
    by_language: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        language = record["language"]
        by_language[(language["family"], language["language"])].append(record)

    category_counts = Counter(
        str(record["note_type"]) for record in records
    )
    name_review_count = sum(bool(record["status_check_name"]) for record in records)
    pronunciation_count = sum(bool(record["pronunciation"]) for record in records)
    unknown_count = sum(
        record["language"]["language"] == "Unknown" for record in records
    )

    lines = [
        "---",
        "headerVersion: 2023.11.25",
        "tags: [meta, status/check/ai]",
        "---",
        "# Name Catalog",
        "",
        "<!-- Generated by _scripts/generate_name_catalog.py; do not edit tables by hand. -->",
        "",
        "This is a note-based catalog of names in the Taelgar vault. It is designed "
        "for both human browsing and machine-assisted naming searches. The companion "
        "machine-readable file is [[Name Catalog.jsonl]].",
        "",
        "The catalog includes every Markdown note with frontmatter tags, except "
        "notes anywhere under `Worldbuilding` or a directory whose name begins "
        "with `_` or `.`.",
        "",
        "Note type is the single primary descriptive tag defined by "
        "[[Note Categorization]]: `person`, `power`, `place`, `event`, `object`, "
        "`group`, `ancestry`, `creature`, `session-note`, `source`, `background`, "
        "or `meta`. Tagged notes without one of these primary tags are listed as "
        "`unknown`.",
        "",
        "Language assignments describe the language of the primary displayed name, "
        "not necessarily every culture associated with the subject. They are "
        "best-effort inferences from explicit naming text, ancestry/species metadata, "
        "vault location, whereabouts, and the rules in [[Languages]]. `Unknown` is "
        "intentional where the vault does not support a responsible inference.",
        "",
        "Text-derived aliases are marked **†**. These are extracted conservatively "
        "from headings and explicit naming statements, but should still be reviewed "
        "against the linked note.",
        "",
        "## Using the catalog",
        "",
        "For a quick collision search:",
        "",
        "```sh",
        'rg -i "candidate|similar-form" "_Plugins/Name Explorer/Name Catalog.jsonl"',
        "```",
        "",
        "Useful JSONL fields include `name`, `normalized`, `aliases`, `note_type`, "
        "`language`, `status_check_name`, `pronunciation`, and `path`.",
        "",
        "Regenerate after names or metadata change:",
        "",
        "```sh",
        "python3 _scripts/generate_name_catalog.py --root .",
        "```",
        "",
        "## Coverage",
        "",
        f"- **Cataloged notes:** {len(records)}",
        f"- **With pronunciation:** {pronunciation_count}",
        f"- **Tagged `status/check/name`:** {name_review_count}",
        f"- **Unknown primary-name language:** {unknown_count}",
        "",
        "### By note type",
        "",
        "| Note type | Count |",
        "|---|---:|",
    ]
    for category, count in sorted(
        category_counts.items(), key=lambda item: (TAG_ORDER.get(item[0], 999), item[0])
    ):
        lines.append(f"| {escape_table(category)} | {count} |")

    lines.extend(
        [
            "",
            "### By language",
            "",
            "| Family | Language | Notes | Name review |",
            "|---|---|---:|---:|",
        ]
    )
    for (family, language), group in sorted(
        by_language.items(),
        key=lambda item: (
            item[0][0] == "Unknown",
            item[0][0].casefold(),
            item[0][1].casefold(),
        ),
    ):
        review = sum(bool(record["status_check_name"]) for record in group)
        lines.append(
            f"| {escape_table(family)} | {escape_table(language)} | "
            f"{len(group)} | {review} |"
        )

    lines.extend(["", "## Catalog", ""])
    sorted_groups = sorted(
        by_language.items(),
        key=lambda item: (
            item[0][0] == "Unknown",
            item[0][0].casefold(),
            item[0][1].casefold(),
        ),
    )
    current_family: str | None = None
    for (family, language), group in sorted_groups:
        if family != current_family:
            lines.extend([f"### {family}", ""])
            current_family = family
        lines.extend(
            [
                f"#### {language}",
                "",
                "| Name | Aliases | Note type | Name review | Pronunciation | Basis |",
                "|---|---|---|:---:|---|---|",
            ]
        )
        for record in group:
            language_data = record["language"]
            confidence = language_data["confidence"]
            basis = language_data["basis"]
            basis_label = f"{confidence}: {basis}"
            review = "✓" if record["status_check_name"] else ""
            lines.append(
                "| "
                + " | ".join(
                    (
                        link_for(record),
                        escape_table(aliases_label(record)),
                        escape_table(record["note_type"]),
                        review,
                        escape_table(record["pronunciation"]),
                        escape_table(basis_label),
                    )
                )
                + " |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Vault root does not exist: {root}")

    records = build_records(root)
    markdown_path = root / args.markdown
    jsonl_path = root / args.jsonl
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(markdown_text(records), encoding="utf-8")
    jsonl_path.write_text(jsonl_text(records), encoding="utf-8")

    print(f"Wrote {len(records)} records to {markdown_path.relative_to(root)}")
    print(f"Wrote {len(records)} records to {jsonl_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

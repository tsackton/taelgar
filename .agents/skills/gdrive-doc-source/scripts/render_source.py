#!/usr/bin/env python3
"""Render a Google Docs structured resource and Drive comment threads to Markdown."""

import argparse
from datetime import datetime
import html
import json
import re
from pathlib import Path


def fail(message):
    raise SystemExit(message)


def obsidian_safe(value):
    """Render source-authored bracket notation without Obsidian link/HTML syntax."""
    value = re.sub(r"<([^<>\n]+)>", lambda match: f"~~{match.group(1)}~~", value)
    value = re.sub(r"\[([^\[\]\n]*)\]", lambda match: f"({match.group(1)})", value)
    return value.translate(str.maketrans({"<": "", ">": "", "[": "", "]": ""}))


def text_run(run, strike_mode):
    style = run.get("textStyle") or {}
    if strike_mode == "drop" and style.get("strikethrough"):
        return ""
    value = obsidian_safe(run.get("content", "").rstrip("\n"))
    if not value:
        return ""
    leading = value[:len(value) - len(value.lstrip())]
    trailing = value[len(value.rstrip()):]
    core = value.strip()
    if not core:
        return value
    if style.get("link", {}).get("url"):
        core = f"[{core}]({style['link']['url']})"
    if style.get("bold"):
        core = f"**{core}**"
    if style.get("italic"):
        core = f"*{core}*"
    return leading + core + trailing


def render_paragraph(paragraph, strike_mode, inline_objects=None, image_paths=None):
    pieces = []
    for element in paragraph.get("elements", []):
        if "inlineObjectElement" in element:
            object_id = element["inlineObjectElement"].get("inlineObjectId")
            obj = (inline_objects or {}).get(object_id) or {}
            uri = (((obj.get("inlineObjectProperties") or {}).get("embeddedObject") or {})
                   .get("imageProperties") or {}).get("contentUri")
            if not uri:
                fail(f"Image {object_id} has no content URI")
            local_path = (image_paths or {}).get(object_id)
            if not local_path:
                fail(f"Image {object_id} needs a local asset in imagePaths")
            pieces.append(f"![[{local_path}]]")
            continue
        if "pageBreak" in element:
            pieces.append("\n\n---\n\n")
            continue
        if "textRun" not in element:
            fail(f"Unsupported paragraph element: {list(element)}")
        pieces.append(text_run(element["textRun"], strike_mode))
    value = "".join(pieces).strip()
    if not value:
        return ""
    if (value.startswith("![[")
            and all(not piece for piece in pieces[1:])):
        return value
    style = (paragraph.get("paragraphStyle") or {}).get("namedStyleType", "NORMAL_TEXT")
    heading = {"TITLE": 1, "SUBTITLE": 2, "HEADING_1": 1, "HEADING_2": 2,
               "HEADING_3": 3, "HEADING_4": 4, "HEADING_5": 5, "HEADING_6": 6}.get(style)
    if heading:
        return f"{'#' * heading} {value}"
    bullet = paragraph.get("bullet")
    if bullet:
        level = int(bullet.get("nestingLevel", 0))
        return f"{'  ' * level}- {value}"
    return value


def render_table(table, strike_mode, inline_objects=None, image_paths=None):
    rows = []
    for row in table.get("tableRows", []):
        cells = []
        for cell in row.get("tableCells", []):
            style = cell.get("tableCellStyle") or {}
            if style.get("rowSpan", 1) != 1 or style.get("columnSpan", 1) != 1:
                fail("Merged table cells need review before rendering")
            parts = []
            for element in cell.get("content", []):
                if "paragraph" not in element:
                    fail(f"Unsupported table cell element: {list(element)}")
                part = render_paragraph(element["paragraph"], strike_mode,
                                        inline_objects, image_paths)
                if part:
                    parts.append(part.replace("\n", " ").replace("|", r"\|"))
            cells.append("; ".join(parts))
        rows.append(cells)
    if not rows:
        fail("Empty table")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        fail("Uneven table rows need review before rendering")
    lines = ["| " + " | ".join(rows[0]) + " |",
             "| " + " | ".join("---" for _ in range(width)) + " |"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return "\n".join(lines)


def walk_tab(tab, strike_mode, image_paths=None):
    body = tab.get("body") or (tab.get("documentTab") or {}).get("body") or {}
    lines = []
    for element in body.get("content", []):
        if "sectionBreak" in element:
            continue
        if "table" in element:
            lines.append(render_table(element["table"], strike_mode,
                                      tab.get("inlineObjects"), image_paths))
            continue
        if "paragraph" not in element:
            fail(f"Unsupported document element in tab {tab.get('title')}: {list(element)}")
        value = render_paragraph(element["paragraph"], strike_mode,
                                 tab.get("inlineObjects"), image_paths)
        if value:
            lines.append(value)
    return lines


def date(value):
    return value or "unknown time"


def quote_lines(value):
    value = obsidian_safe(html.unescape(value or ""))
    return ["> " + line for line in value.splitlines()] or ["> *(No quoted anchor supplied)*"]


def normalize(value):
    return re.sub(r"\s+", " ", value).strip()


def source_units(document, revisions):
    current = []
    def add_element(element):
        paragraph = element.get("paragraph")
        if paragraph:
            current.append({"text": normalize("".join(
                part.get("textRun", {}).get("content", "") for part in paragraph.get("elements", []))),
                "heading": (paragraph.get("paragraphStyle") or {}).get("namedStyleType", "").startswith("HEADING_")})
        table = element.get("table")
        if table:
            for row in table.get("tableRows", []):
                for cell in row.get("tableCells", []):
                    for child in cell.get("content", []):
                        add_element(child)
    for tab in document.get("tabs") or [{"body": document.get("body")}]:
        body = tab.get("body") or (tab.get("documentTab") or {}).get("body") or {}
        for element in body.get("content", []):
            add_element(element)
    snapshots = [{"id": "current", "modifiedTime": document.get("modifiedTime"), "units": current}]
    for revision in revisions:
        content = (revision.get("content") or "").replace("\r\n", "\n")
        content = re.split(r"(?m)^\[[a-z]{1,2}\]", content, maxsplit=1)[0]
        lines = [re.sub(r"\[[a-z]{1,2}\]", "", line).strip(" \t*\ufeff")
                 for line in content.splitlines()]
        snapshots.append({"id": revision["revisionId"], "modifiedTime": revision.get("revisionModifiedTime"),
                          "units": [{"text": normalize(line), "heading": False} for line in lines if line.strip()]})
    return snapshots


def sentence_context(text, quote):
    """Return whole sentence(s) that contain the selected text."""
    text = normalize(text)
    match = re.search(re.escape(normalize(quote)), text, flags=re.IGNORECASE)
    if not match:
        return text
    boundaries = [0] + [item.end() for item in re.finditer(r"(?<=[.!?])\s+", text)] + [len(text)]
    start = max(point for point in boundaries if point <= match.start())
    end = min(point for point in boundaries if point >= match.end())
    return text[start:end].strip()


def matching_units(units, quote):
    quote = normalize(quote)
    if not quote:
        return []
    escaped = re.escape(quote).replace(r"\ ", r"\s+")
    pattern = re.compile(escaped, flags=re.IGNORECASE)
    strict = [unit for unit in units if any(
        (not quote[0].isalnum() or match.start() == 0 or not unit["text"][match.start() - 1].isalnum())
        and (not quote[-1].isalnum() or match.end() == len(unit["text"]) or not unit["text"][match.end()].isalnum())
        for match in pattern.finditer(unit["text"]))]
    return strict or [unit for unit in units if pattern.search(unit["text"])]


def context_for(comment, snapshots):
    quote = html.unescape((comment.get("quotedFileContent") or {}).get("value") or "")
    created = comment.get("createdTime") or ""
    candidates = []
    for snapshot in snapshots:
        hits = matching_units(snapshot["units"], quote)
        if not hits:
            continue
        exact_hits = [unit for unit in hits if normalize(unit["text"]).casefold() == normalize(quote).casefold()]
        if exact_hits:
            hits = exact_hits
        contexts = list(dict.fromkeys(sentence_context(unit["text"], quote) for unit in hits))
        if len(contexts) == 1:
            modified = snapshot.get("modifiedTime") or ""
            candidates.append((modified < created, abs((datetime.fromisoformat(modified.replace("Z", "+00:00")) -
                                                           datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds())
                               if modified and created else float("inf"),
                               snapshot["id"] != "current", snapshot["id"], contexts[0], len(hits)))
    if candidates:
        _, _, _, revision_id, context, count = min(candidates)
        where = "current document" if revision_id == "current" else f"document revision `{revision_id}`"
        suffix = " (the same wording appears more than once)" if count > 1 else ""
        return f"Context in {where}{suffix}: {obsidian_safe(context)}"
    current_hits = matching_units(snapshots[0]["units"], quote)
    if current_hits:
        return f"Context: the quoted selection occurs in {len(current_hits)} distinct passages in the current document; its exact location is ambiguous."
    return "Context: this selection is not present in the current document or the available historical revisions."


def render_comments(comments, snapshots):
    output = ["## Google Docs comments", ""]
    if not comments:
        return output + ["No comments were present in the source document."]
    for index, comment in enumerate(comments, 1):
        if comment.get("deleted"):
            fail(f"Deleted comment in response: {comment.get('id')}")
        status = "resolved" if comment.get("resolved") else "open"
        cid = comment.get("id") or fail("Comment without ID")
        output += [f"### {index}. {status.capitalize()} · {cid}", ""]
        output += ["**Original selection:**"] + quote_lines((comment.get("quotedFileContent") or {}).get("value"))
        context_label, _, context_text = context_for(comment, snapshots).partition(": ")
        output += ["", f"**{context_label}:** {context_text}"]
        output.append("")
        if comment.get("anchor"):
            output += [f"Google anchor: `{comment['anchor']}`", ""]
        author = (comment.get("author") or {}).get("displayName") or "Unknown author"
        output += [f"**{author}** · {date(comment.get('createdTime'))}", "", obsidian_safe(comment.get("content") or ""), ""]
        if comment.get("modifiedTime") and comment.get("modifiedTime") != comment.get("createdTime"):
            output += [f"Last edited: {comment['modifiedTime']}", ""]
        for reply in comment.get("replies") or []:
            if reply.get("deleted"):
                fail(f"Deleted reply in comment {cid}")
            rauthor = (reply.get("author") or {}).get("displayName") or "Unknown author"
            output += [f"**Reply — {rauthor}** · {date(reply.get('createdTime'))}", "", obsidian_safe(reply.get("content") or "*(Empty reply)*"), ""]
            if reply.get("modifiedTime") and reply.get("modifiedTime") != reply.get("createdTime"):
                output += [f"Last edited: {reply['modifiedTime']}", ""]
    return output


def has_suggestions(value):
    if isinstance(value, dict):
        if any(key.lower().startswith("suggested") for key in value):
            return True
        return any(has_suggestions(item) for item in value.values())
    if isinstance(value, list):
        return any(has_suggestions(item) for item in value)
    return False


def render(bundle, strike_mode="keep"):
    doc = bundle["document"]
    comments = bundle["comments"]
    revisions = bundle.get("revisions") or []
    tabs = doc.get("tabs") or [{"title": doc.get("title"), "body": doc.get("body")}]
    if not tabs:
        fail("No document tabs")
    if has_suggestions(doc):
        fail("Document suggestions need review before rendering")
    if any(doc.get(key) for key in ("headers", "footers", "footnotes", "inlineObjects", "positionedObjects")):
        fail("Document has headers, footers, footnotes, or objects needing review")
    if len(tabs) > 1:
        body = []
        for tab in tabs:
            body += [f"# Tab: {tab.get('title') or tab.get('tabId')}", ""] + walk_tab(tab, strike_mode, bundle.get("imagePaths")) + [""]
    else:
        body = walk_tab(tabs[0], strike_mode, bundle.get("imagePaths"))
    if not body:
        fail("Strikeout treatment produced an empty reading copy")
    if not isinstance(comments, list):
        fail("Comments must be a complete list of threads")
    body_text = ""
    for line in body:
        separator = "\n" if body_text.rstrip().split("\n")[-1].lstrip().startswith("- ") and line.lstrip().startswith("- ") else "\n\n"
        body_text += (separator if body_text else "") + line
    text = body_text.rstrip() + "\n\n" + "\n".join(render_comments(comments, source_units(doc, revisions))).rstrip() + "\n"
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return "\n".join(line.rstrip(" \t") for line in text.split("\n"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--strike-mode", default="keep", choices=["drop", "keep"],
                        help="Keep struck text without strikeout styling (default); drop only when explicitly requested")
    args = parser.parse_args()
    bundle = json.loads(args.input.read_text(encoding="utf-8"))
    result = render(bundle, args.strike_mode)
    args.output.write_text(result, encoding="utf-8")
    comments = bundle["comments"]
    print(json.dumps({"threads": len(comments), "open": sum(not c.get("resolved") for c in comments),
                      "resolved": sum(bool(c.get("resolved")) for c in comments),
                      "replies": sum(len(c.get("replies") or []) for c in comments)}))


if __name__ == "__main__":
    main()

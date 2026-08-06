#!/usr/bin/env python3
"""Audit Taelgar tilde placeholders and internal link integrity.

The scan is read-only. It scans every Markdown note Obsidian indexes, apart
from the generated clickable unresolved-link report itself, while excluding
inline and fenced code. Both Obsidian wikilinks and local Markdown links ending
in .md are checked. Reports are written as JSON and TSV files.
"""

import argparse
import csv
import json
import os
import re
import shutil
from collections import Counter, defaultdict
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path('.').resolve()
OUT = Path('/tmp/taelgar-integrity-audit')
OLD = None

CANON_TOP = {
    'Background', 'Campaigns', 'Cosmology', 'Creatures', 'Events', 'Gazetteer',
    'Gods and Religions', 'Groups', 'History', 'People', 'Primary Sources', 'Things'
}
ATTACHMENT_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.pdf', '.mp3', '.wav',
    '.m4a', '.ogg', '.mp4', '.mov', '.webm', '.avif', '.bmp', '.tif', '.tiff',
    '.canvas', '.excalidraw'
}
LINK_RE = re.compile(r'(!?)\[\[([^\]\n]+)\]\]')
TILDE_RE = re.compile(r'~([^~\n]{1,180})~')
HEADING_RE = re.compile(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$')
BLOCK_RE = re.compile(r'(?:^|\s)\^([A-Za-z0-9_-]+)\s*$')
REPORT_SOURCE_EXCLUSIONS = {
    '_MoC/Data Quality/Links/Unresolved Links.md',
}
OBSIDIAN_IGNORE_FILTERS = []


def rel(path):
    return path.relative_to(ROOT).as_posix()


def indexed_markdown(path):
    r = rel(path)
    parts = Path(r).parts
    if not parts:
        return False
    if parts[0] == '.backups' or any(p.startswith('.') for p in parts):
        return False
    for pattern in OBSIDIAN_IGNORE_FILTERS:
        try:
            if re.search(pattern, r):
                return False
        except re.error:
            if pattern in r:
                return False
    return True


def load_obsidian_ignore_filters():
    """Read the same excluded-file patterns used by the Obsidian vault."""
    config = ROOT / '.obsidian' / 'app.json'
    if not config.exists():
        return []
    try:
        data = json.loads(config.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return []
    return [
        pattern for pattern in data.get('userIgnoreFilters', [])
        if isinstance(pattern, str) and pattern
    ]


def source_category(r):
    parts = Path(r).parts
    top = parts[0]
    if '_generated' in parts:
        return 'generated'
    if '_templates' in parts:
        return 'template'
    if top in CANON_TOP:
        return 'canon'
    if top in {'_DM_', '_dm_notes'}:
        return 'session-dm'
    if top == '_sessions':
        return 'session-dm'
    if r.startswith('Worldbuilding/Staging/'):
        return 'staging'
    if r.startswith('Worldbuilding/Tentative/'):
        return 'tentative'
    if top == 'Worldbuilding':
        return 'worldbuilding'
    if top == '_MoC':
        return 'vault-support'
    return 'other'


def scanned_source(path):
    r = rel(path)
    if r in REPORT_SOURCE_EXCLUSIONS:
        return False
    return indexed_markdown(path)


def split_frontmatter(text):
    lines = text.splitlines()
    if lines and lines[0].strip() == '---':
        for i in range(1, min(len(lines), 500)):
            if lines[i].strip() == '---':
                return lines[1:i], i + 1
    return [], 0


def yaml_scalar(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        value = value[1:-1]
    return value.strip()


def parse_aliases(text):
    fm, _ = split_frontmatter(text)
    aliases = []
    for i, line in enumerate(fm):
        m = re.match(r'^aliases\s*:\s*(.*)$', line, re.I)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest.startswith('[') and rest.endswith(']'):
            body = rest[1:-1]
            aliases.extend(yaml_scalar(x) for x in re.split(r'\s*,\s*', body) if yaml_scalar(x))
        elif rest:
            aliases.append(yaml_scalar(rest))
        else:
            for sub in fm[i + 1:]:
                mm = re.match(r'^\s+-\s+(.*)$', sub)
                if mm:
                    aliases.append(yaml_scalar(mm.group(1)))
                elif sub.strip() and not sub.startswith((' ', '\t')):
                    break
        break
    return [a for a in aliases if a and a not in {'[]', 'none', 'null'}]


def strip_code_line(line, in_fence):
    if re.match(r'^\s*(```|~~~)', line):
        return '', not in_fence
    if in_fence:
        return '', in_fence
    return re.sub(r'(`+).*?\1', '', line), in_fence


def contextual_lines(text):
    lines = text.splitlines()
    _, body_start = split_frontmatter(text)
    in_fence = False
    in_comment = False
    for number, original in enumerate(lines, 1):
        line, in_fence = strip_code_line(original, in_fence)
        if not line:
            yield number, '', 'frontmatter' if body_start and number <= body_start else ('comment' if in_comment else 'visible')
            continue
        if body_start and number <= body_start:
            yield number, line, 'frontmatter'
            continue
        visible_parts = []
        comment_parts = []
        pos = 0
        while True:
            marker = line.find('%%', pos)
            if marker < 0:
                (comment_parts if in_comment else visible_parts).append(line[pos:])
                break
            (comment_parts if in_comment else visible_parts).append(line[pos:marker])
            in_comment = not in_comment
            pos = marker + 2
        if visible_parts and ''.join(visible_parts).strip():
            yield number, ''.join(visible_parts), 'visible'
        if comment_parts and ''.join(comment_parts).strip():
            yield number, ''.join(comment_parts), 'comment'


def norm(s):
    return re.sub(r'\s+', ' ', s.strip()).casefold()


def norm_path(s):
    s = s.replace('\\', '/').strip().lstrip('./')
    if s.casefold().endswith('.md'):
        s = s[:-3]
    return norm(s)


def fragment_parts(target):
    if '#' in target:
        base, frag = target.split('#', 1)
        if frag.startswith('^'):
            return base, frag[1:], 'block'
        return base, frag, 'heading'
    if '^' in target:
        base, frag = target.split('^', 1)
        return base, frag, 'block'
    return target, '', None


def candidate_names(target, notes):
    needle = norm(Path(target).name)
    ranked = []
    for note in notes:
        stem = norm(note['stem'])
        score = SequenceMatcher(None, needle, stem).ratio()
        if score >= 0.72:
            ranked.append((score, note['path']))
    return [p for _, p in sorted(ranked, key=lambda x: (-x[0], x[1]))[:5]]


def write_tsv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, delimiter='\t', fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def parse_markdown_links(line):
    """Return non-image inline Markdown links, including balanced parentheses."""
    links = []
    position = 0
    while position < len(line):
        start = line.find('[', position)
        if start < 0:
            break
        if start > 0 and line[start - 1] == '!':
            position = start + 1
            continue
        label_end = line.find(']', start + 1)
        if label_end < 0 or label_end + 1 >= len(line) or line[label_end + 1] != '(':
            position = start + 1
            continue
        cursor = label_end + 2
        depth = 1
        escaped = False
        while cursor < len(line):
            char = line[cursor]
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth == 0:
                    break
            cursor += 1
        if depth:
            position = start + 1
            continue
        links.append({
            'start': start,
            'end': cursor + 1,
            'raw_link': line[start:cursor + 1],
            'label': line[start + 1:label_end],
            'body': line[label_end + 2:cursor].strip(),
        })
        position = cursor + 1
    return links


def local_markdown_target(body):
    """Decode a local Markdown destination ending in .md; ignore URLs and others."""
    if not body:
        return None
    if body.startswith('<') and '>' in body:
        destination = body[1:body.find('>')]
    else:
        match = re.match(
            r'^(.*?\.md(?:#[^\s]+)?)(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?\s*$',
            body,
            re.I,
        )
        if not match:
            return None
        destination = match.group(1)
    destination = unquote(destination).replace('\\', '/').strip()
    parsed = urlsplit(destination)
    if parsed.scheme or parsed.netloc or not parsed.path.casefold().endswith('.md'):
        return None
    return parsed.path, unquote(parsed.fragment)


def plain_markdown_links(line):
    """Render inline Markdown links as their labels without leaving live links."""
    links = parse_markdown_links(line)
    for item in reversed(links):
        line = line[:item['start']] + item['label'] + line[item['end']:]
    return line


def plain_link_text(match):
    """Render an Obsidian link as its visible text without leaving a live link."""
    inside = match.group(2)
    if '|' in inside:
        return inside.split('|', 1)[1]
    base, frag, _ = fragment_parts(inside)
    display = Path(base).name if base else frag
    return display or inside


def short_context(line, raw_link, limit=240):
    """Return a compact plain-text excerpt centered on the matched link."""
    plain = plain_markdown_links(line)
    plain = re.sub(r'\s+', ' ', LINK_RE.sub(plain_link_text, plain).strip())
    raw_display = plain_markdown_links(raw_link)
    raw_display = LINK_RE.sub(plain_link_text, raw_display)
    if len(plain) <= limit:
        return plain
    center = plain.find(raw_display)
    if center < 0:
        center = len(plain) // 2
    start = max(0, center - limit // 3)
    end = min(len(plain), start + limit)
    start = max(0, end - limit)
    excerpt = plain[start:end].strip()
    return ('…' if start else '') + excerpt + ('…' if end < len(plain) else '')


def inline_code(value):
    fence = '`' if '`' not in value else '``'
    return f'{fence}{value}{fence}'


def source_link(source):
    target = source[:-3] if source.casefold().endswith('.md') else source
    return f'[[{target}|{Path(target).name}]]'


def write_unresolved_note(path, broken, metadata):
    """Write a human-reviewable snapshot of unresolved links."""
    groups = defaultdict(list)
    for item in broken:
        groups[item['target']].append(item)

    ordered = []
    for target, items in groups.items():
        sources = {item['source'] for item in items}
        ordered.append((len(sources), target, items))
    ordered.sort(key=lambda row: (-row[0], row[1].casefold(), row[1]))

    unique_sources = {item['source'] for item in broken}
    missing_attachments = {
        item['target'] for item in broken if item['status'] == 'missing-attachment'
    }
    missing_notes = set(groups) - missing_attachments

    lines = [
        '---',
        'headerVersion: 2023.11.25',
        'tags: [status/check/ai]',
        '---',
        '# Unresolved Links',
        '',
        f'*Generated {date.today().isoformat()} by `_scripts/vault_integrity_audit.py`.*',
        '',
        'This is a static review list of links whose note or attachment target does not exist. '
        'The live target beneath each heading is intentionally clickable so the missing note can be created directly. '
        'This report is excluded from the audit source set, so those convenience links do not affect later counts.',
        '',
        f'- **{len(groups)}** unresolved targets: **{len(missing_notes)}** notes and **{len(missing_attachments)}** attachments',
        f'- **{len(broken)}** occurrences across **{len(unique_sources)}** source files',
        f'- **{metadata["scanned_source_markdown"]}** Obsidian-indexed source notes scanned; this report itself excluded',
        f'- Includes **{metadata.get("total_markdown_links", 0)}** local `.md`-style Markdown links in addition to Obsidian wikilinks',
        '- Sorted by number of distinct source files, then alphabetically',
        '- One representative context snippet is shown per source file; repeated occurrences in that file are counted',
        '',
    ]

    for file_count, target, items in ordered:
        per_source = defaultdict(list)
        for item in items:
            per_source[item['source']].append(item)
        occurrence_count = len(items)
        file_word = 'file' if file_count == 1 else 'files'
        occurrence_word = 'occurrence' if occurrence_count == 1 else 'occurrences'
        attachment = all(item['status'] == 'missing-attachment' for item in items)
        unresolved = f'![[{target}]]' if attachment else f'[[{target}]]'
        lines.extend([
            f'## {inline_code(unresolved)} — {file_count} {file_word} · {occurrence_count} {occurrence_word}',
            '',
            unresolved,
            '',
        ])
        for source in sorted(per_source, key=str.casefold):
            occurrences = sorted(per_source[source], key=lambda item: item['line'])
            first = occurrences[0]
            repeat = ''
            if len(occurrences) > 1:
                repeat = f'; {len(occurrences)} occurrences in this file'
            context_label = '' if first['context'] == 'visible' else f'; {first["context"]}'
            style_label = '; Markdown link' if any(
                item.get('link_style') == 'markdown' for item in occurrences
            ) else ''
            lines.append(
                f'- {source_link(source)} — line {first["line"]}{repeat}{context_label}{style_label}'
            )
            lines.append(f'  > {first["snippet"]}')
        lines.append('')

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'root', nargs='?', default='.',
        help='Vault root to scan (default: current directory).'
    )
    parser.add_argument(
        '-o', '--output-dir', default='/tmp/taelgar-integrity-audit',
        help='Directory for audit.json and TSV reports.'
    )
    parser.add_argument(
        '--compare',
        help='Optional earlier audit.json used to produce comparison.json.'
    )
    parser.add_argument(
        '--unresolved-note',
        help='Optional Markdown path for a static unresolved-link review note.'
    )
    return parser.parse_args()


def main():
    global ROOT, OUT, OLD, OBSIDIAN_IGNORE_FILTERS
    args = parse_args()
    ROOT = Path(args.root).expanduser().resolve()
    OUT = Path(args.output_dir).expanduser().resolve()
    OLD = Path(args.compare).expanduser().resolve() if args.compare else None
    OBSIDIAN_IGNORE_FILTERS = load_obsidian_ignore_filters()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    md_paths = sorted(p for p in ROOT.rglob('*.md') if indexed_markdown(p))
    all_files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '.backups' not in p.parts)
    notes = []
    stems = defaultdict(list)
    paths = defaultdict(list)
    aliases = defaultdict(list)
    note_by_path = {}
    headings = {}
    blocks = {}
    for p in md_paths:
        r = rel(p)
        text = p.read_text(encoding='utf-8', errors='replace')
        item = {'path': r, 'stem': p.stem, 'aliases': parse_aliases(text)}
        notes.append(item)
        note_by_path[r] = item
        stems[norm(p.stem)].append(item)
        paths[norm_path(r)].append(item)
        for a in item['aliases']:
            aliases[norm(a)].append(item)
        hs, bs = set(), set()
        in_fence = False
        for line in text.splitlines():
            clean, in_fence = strip_code_line(line, in_fence)
            if not clean:
                continue
            m = HEADING_RE.match(clean)
            if m:
                hs.add(norm(re.sub(r'\s+#+\s*$', '', m.group(1))))
            m = BLOCK_RE.search(clean)
            if m:
                bs.add(norm(m.group(1)))
        headings[r] = hs
        blocks[r] = bs

    attachment_basenames = defaultdict(list)
    attachment_paths = defaultdict(list)
    for p in all_files:
        if p.suffix.casefold() == '.md':
            continue
        try:
            r = rel(p)
        except ValueError:
            continue
        attachment_basenames[norm(p.name)].append(r)
        attachment_paths[norm(r)].append(r)

    source_paths = [p for p in md_paths if scanned_source(p)]
    broken, ambiguous, tentative, fragment_issues = [], [], [], []
    placeholders, other_tilde = [], []
    link_count = 0
    markdown_link_count = 0
    status_counts = Counter()
    context_counts = Counter()
    category_counts = Counter()
    markdown_category_counts = Counter()

    def resolve_note(base, source):
        base = base.strip()
        if not base:
            return [note_by_path[source]], 'resolved-self'
        np = norm_path(base)
        exact = paths.get(np, [])
        if exact:
            return exact, 'resolved-path'
        if '/' in base:
            suffix = [n for n in notes if norm_path(n['path']).endswith('/' + np)]
            if suffix:
                return suffix, 'resolved-path'
        by_stem = stems.get(norm(Path(base).name.removesuffix('.md')), [])
        if by_stem:
            if len(by_stem) == 1:
                return by_stem, 'resolved'
            source_parent = Path(source).parent.parts
            ranked = sorted(by_stem, key=lambda n: -sum(a == b for a, b in zip(source_parent, Path(n['path']).parent.parts)))
            if len(ranked) == 1:
                return ranked, 'resolved'
            best_score = sum(a == b for a, b in zip(source_parent, Path(ranked[0]['path']).parent.parts))
            next_score = sum(a == b for a, b in zip(source_parent, Path(ranked[1]['path']).parent.parts))
            if best_score > next_score:
                return [ranked[0]], 'resolved'
            return by_stem, 'ambiguous'
        by_alias = aliases.get(norm(base), [])
        if by_alias:
            return by_alias, 'alias-only'
        return [], 'missing'

    def resolve_markdown_path(decoded_path, source):
        """Resolve an old Markdown path locally, from vault root, or by note name."""
        source_path = ROOT / source
        candidates = []
        if decoded_path.startswith('/'):
            candidates.append(ROOT / decoded_path.lstrip('/'))
        else:
            candidates.extend((source_path.parent / decoded_path, ROOT / decoded_path))
        for candidate in candidates:
            candidate = candidate.resolve()
            try:
                candidate_rel = candidate.relative_to(ROOT).as_posix()
            except ValueError:
                continue
            if candidate_rel in note_by_path:
                return [note_by_path[candidate_rel]], 'resolved-markdown-path'
        # Old OneNote links frequently retain only a filename. Once exact path
        # checks fail, resolve its stem using the same names and aliases as a
        # wikilink (for example, Halfling.md -> alias on Halflings.md).
        matches, status = resolve_note(Path(decoded_path).stem, source)
        if status == 'alias-only':
            return matches, 'resolved-markdown-name'
        if status in {'resolved', 'resolved-path', 'resolved-self'}:
            return matches, 'resolved-markdown-name'
        return matches, status

    for p in source_paths:
        r = rel(p)
        cat = source_category(r)
        text = p.read_text(encoding='utf-8', errors='replace')
        for line_no, line, context in contextual_lines(text):
            if not line:
                continue
            for m in LINK_RE.finditer(line):
                link_count += 1
                embed = bool(m.group(1))
                raw_link = m.group(0)
                inside = m.group(2)
                # Markdown tables escape Obsidian's alias separator as \|.
                # The backslash is not part of the target.
                target_part = inside.split('|', 1)[0].rstrip('\\').strip()
                base, frag, frag_kind = fragment_parts(target_part)
                ext = Path(base).suffix.casefold()
                is_attachment = ext in ATTACHMENT_EXTS
                record = {
                    'source': r, 'source_category': cat, 'line': line_no,
                    'context': context, 'raw_link': raw_link, 'target': base,
                    'fragment': frag, 'embed': embed, 'candidates': [],
                    'snippet': short_context(line, raw_link),
                    'link_style': 'wikilink', 'markdown_destination': ''
                }
                category_counts[cat] += 1
                context_counts[context] += 1
                if is_attachment:
                    matches = attachment_paths.get(norm(base), [])
                    if not matches:
                        matches = attachment_basenames.get(norm(Path(base).name), [])
                    if matches:
                        record['status'] = 'resolved-attachment'
                        record['resolved_path'] = matches[0]
                    else:
                        record['status'] = 'missing-attachment'
                        broken.append(record)
                    status_counts[record['status']] += 1
                    continue
                matches, status = resolve_note(base, r)
                if status == 'ambiguous':
                    record['status'] = 'ambiguous'
                    record['candidates'] = [n['path'] for n in matches]
                    ambiguous.append(record)
                    status_counts['ambiguous'] += 1
                    continue
                if status == 'missing':
                    record['status'] = 'missing'
                    record['candidates'] = candidate_names(base, notes)
                    if '/' in base and stems.get(norm(Path(base).name.removesuffix('.md'))):
                        record['status'] = 'obsolete-path'
                        record['candidates'] = [n['path'] for n in stems[norm(Path(base).name.removesuffix('.md'))]]
                    broken.append(record)
                    status_counts[record['status']] += 1
                    continue
                if status == 'alias-only':
                    record['status'] = 'alias-only'
                    record['candidates'] = [n['path'] for n in matches]
                    broken.append(record)
                    status_counts['alias-only'] += 1
                    continue
                record['status'] = 'resolved'
                record['resolved_path'] = matches[0]['path']
                status_counts['resolved'] += 1
                if record['resolved_path'].startswith('Worldbuilding/Tentative/'):
                    tentative.append(record.copy())
                if frag:
                    check = blocks[record['resolved_path']] if frag_kind == 'block' else headings[record['resolved_path']]
                    if norm(frag) not in check:
                        frec = record.copy()
                        frec['fragment_status'] = 'missing-block' if frag_kind == 'block' else 'missing-heading'
                        fragment_issues.append(frec)

            for markdown_link in parse_markdown_links(line):
                target_parts = local_markdown_target(markdown_link['body'])
                if not target_parts:
                    continue
                markdown_link_count += 1
                decoded_path, frag = target_parts
                display_target = Path(decoded_path).stem
                raw_link = markdown_link['raw_link']
                record = {
                    'source': r, 'source_category': cat, 'line': line_no,
                    'context': context, 'raw_link': raw_link,
                    'target': display_target, 'fragment': frag, 'embed': False,
                    'candidates': [], 'snippet': short_context(line, raw_link),
                    'link_style': 'markdown',
                    'markdown_destination': decoded_path,
                }
                markdown_category_counts[cat] += 1
                context_counts[context] += 1
                matches, status = resolve_markdown_path(decoded_path, r)
                if status == 'ambiguous':
                    record['status'] = 'ambiguous-markdown'
                    record['candidates'] = [n['path'] for n in matches]
                    ambiguous.append(record)
                    status_counts['ambiguous-markdown'] += 1
                    continue
                if status == 'missing':
                    record['status'] = 'missing-markdown'
                    record['candidates'] = candidate_names(display_target, notes)
                    broken.append(record)
                    status_counts['missing-markdown'] += 1
                    continue
                record['status'] = status
                record['resolved_path'] = matches[0]['path']
                status_counts[status] += 1
                if record['resolved_path'].startswith('Worldbuilding/Tentative/'):
                    tentative.append(record.copy())

            if cat == 'canon':
                for m in TILDE_RE.finditer(line):
                    full = m.group(0)
                    inner = m.group(1).strip()
                    item = {'placeholder': full, 'source': r, 'line': line_no, 'context': context,
                            'snippet': re.sub(r'\s+', ' ', line.strip())[:300]}
                    if (re.search(r'[A-Za-z]', inner)
                            and not re.search(r'\d', inner)
                            and '[[' not in inner and ']]' not in inner
                            and ',' not in inner and ';' not in inner
                            and not inner.endswith('-')):
                        item['classification'] = 'probable-placeholder'
                        item['matching_notes'] = [n['path'] for n in stems.get(norm(inner), [])]
                        placeholders.append(item)
                    else:
                        item['classification'] = 'other-tilde-usage'
                        other_tilde.append(item)

    duplicates = {k: [n['path'] for n in v] for k, v in stems.items() if len(v) > 1}
    metadata = {
        'root': str(ROOT), 'indexed_markdown_notes': len(md_paths),
        'scanned_source_markdown': len(source_paths),
        'canon_source_markdown': sum(1 for p in source_paths if source_category(rel(p)) == 'canon'),
        'total_wikilinks': link_count,
        'total_markdown_links': markdown_link_count,
        'total_links': link_count + markdown_link_count,
        'source_categories': dict(category_counts),
        'markdown_source_categories': dict(markdown_category_counts),
    }
    audit = {
        'metadata': metadata, 'status_counts': dict(status_counts),
        'context_counts': dict(context_counts), 'placeholders': placeholders,
        'other_tilde_usage': other_tilde, 'broken': broken, 'ambiguous': ambiguous,
        'tentative_targets': tentative, 'fragment_issues': fragment_issues,
        'duplicate_note_stems': duplicates
    }
    (OUT / 'audit.json').write_text(json.dumps(audit, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    write_tsv(OUT / 'placeholders.tsv', placeholders,
              ['classification', 'context', 'line', 'matching_notes', 'placeholder', 'snippet', 'source'])
    write_tsv(OUT / 'other_tilde_usage.tsv', other_tilde,
              ['classification', 'context', 'line', 'placeholder', 'snippet', 'source'])
    write_tsv(OUT / 'broken.tsv', broken,
              ['candidates', 'context', 'embed', 'fragment', 'line', 'link_style',
               'markdown_destination', 'raw_link', 'snippet', 'source',
               'source_category', 'status', 'target'])
    canon_broken = [x for x in broken if x['source_category'] == 'canon']
    write_tsv(OUT / 'canon_broken.tsv', canon_broken,
              ['candidates', 'context', 'embed', 'fragment', 'line', 'link_style',
               'markdown_destination', 'raw_link', 'snippet', 'source',
               'source_category', 'status', 'target'])
    write_tsv(OUT / 'tentative_targets.tsv', tentative,
              ['context', 'embed', 'fragment', 'line', 'raw_link', 'resolved_path', 'source', 'source_category', 'status', 'target'])
    write_tsv(OUT / 'fragment_issues.tsv', fragment_issues,
              ['context', 'fragment', 'fragment_status', 'line', 'raw_link', 'resolved_path', 'source', 'source_category', 'status', 'target'])

    old = json.loads(OLD.read_text()) if OLD and OLD.exists() else None
    def sig(x):
        return (x.get('source'), x.get('raw_link'), x.get('status'))
    comparison = {}
    if old:
        comparison = {
            'previous': {
                'wikilinks': old['metadata']['total_wikilinks'],
                'markdown_links': old['metadata'].get('total_markdown_links', 0),
                'placeholders': len(old['placeholders']),
                'unique_placeholders': len({x['placeholder'] for x in old['placeholders']}),
                'broken': len(old['broken']),
                'canon_broken': sum(x.get('source_category') == 'canon' for x in old['broken']),
                'tentative_targets': len(old['tentative_targets']),
                'fragment_issues': len(old['fragment_issues'])
            },
            'current': {
                'wikilinks': link_count,
                'markdown_links': markdown_link_count,
                'placeholders': len(placeholders),
                'unique_placeholders': len({x['placeholder'] for x in placeholders}),
                'broken': len(broken),
                'canon_broken': len(canon_broken),
                'tentative_targets': len(tentative),
                'fragment_issues': len(fragment_issues)
            },
            'old_broken_now_absent': [x for x in old['broken'] if sig(x) not in {sig(y) for y in broken}],
            'new_broken': [x for x in broken if sig(x) not in {sig(y) for y in old['broken']}]
        }
    (OUT / 'comparison.json').write_text(json.dumps(comparison, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    if args.unresolved_note:
        report_path = Path(args.unresolved_note).expanduser()
        if not report_path.is_absolute():
            report_path = ROOT / report_path
        write_unresolved_note(report_path.resolve(), broken, metadata)
    print(json.dumps({
        'metadata': metadata,
        'counts': {
            'placeholders': len(placeholders),
            'unique_placeholders': len({x['placeholder'] for x in placeholders}),
            'other_tilde_usage': len(other_tilde),
            'broken': len(broken),
            'canon_broken': len(canon_broken),
            'ambiguous': len(ambiguous),
            'tentative_targets': len(tentative),
            'canon_tentative_targets': sum(x['source_category'] == 'canon' for x in tentative),
            'fragment_issues': len(fragment_issues),
            'missing_attachments': sum(x['status'] == 'missing-attachment' for x in broken),
            'missing_markdown': sum(x['status'] == 'missing-markdown' for x in broken),
            'alias_only': sum(x['status'] == 'alias-only' for x in broken),
            'obsolete_paths': sum(x['status'] == 'obsolete-path' for x in broken)
        }
    }, indent=2))


if __name__ == '__main__':
    main()

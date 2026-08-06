#!/usr/bin/env python3
"""Convert resolvable local Markdown .md links to Obsidian wikilinks.

The default is a read-only dry run. Pass --apply to write the planned link-only
changes. This script never creates or changes YAML frontmatter.
"""

import argparse
import importlib.util
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


def load_audit_module():
    path = Path(__file__).with_name('vault_integrity_audit.py')
    spec = importlib.util.spec_from_file_location('vault_integrity_audit', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.', help='Vault root')
    parser.add_argument('--apply', action='store_true', help='Apply safe conversions')
    parser.add_argument(
        '--output', default='/tmp/taelgar-markdown-link-conversion.json',
        help='JSON report path',
    )
    return parser.parse_args()


def unique_notes(items):
    return list({item['path']: item for item in items}.values())


def dirty_paths(root):
    commands = (
        ['git', 'diff', '--name-only'],
        ['git', 'diff', '--cached', '--name-only'],
        ['git', 'ls-files', '--others', '--exclude-standard'],
    )
    dirty = set()
    for command in commands:
        result = subprocess.run(command, cwd=root, capture_output=True, text=True)
        if result.returncode == 0:
            dirty.update(line for line in result.stdout.splitlines() if line)
    return dirty


def main():
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    audit = load_audit_module()
    audit.ROOT = root

    notes = []
    notes_by_path = {}
    stems = defaultdict(list)
    aliases = defaultdict(list)
    for path in sorted(root.rglob('*.md')):
        if not audit.indexed_markdown(path):
            continue
        text = path.read_text(encoding='utf-8', errors='replace')
        item = {
            'path': audit.rel(path),
            'stem': path.stem,
            'aliases': audit.parse_aliases(text),
        }
        notes.append(item)
        notes_by_path[item['path']] = item
        stems[audit.norm(path.stem)].append(item)
        for alias in item['aliases']:
            aliases[audit.norm(alias)].append(item)

    def named_matches(name):
        filename_matches = unique_notes(stems.get(audit.norm(name), []))
        if filename_matches:
            return filename_matches, 'filename'
        alias_matches = unique_notes(aliases.get(audit.norm(name), []))
        if alias_matches:
            return alias_matches, 'alias'
        return [], None

    def exact_path_matches(destination, source):
        source_path = root / source
        if destination.startswith('/'):
            candidates = [root / destination.lstrip('/')]
        else:
            candidates = [source_path.parent / destination, root / destination]
        matches = []
        for candidate in candidates:
            candidate = candidate.resolve()
            try:
                candidate_path = candidate.relative_to(root).as_posix()
            except ValueError:
                continue
            if candidate_path in notes_by_path:
                matches.append(notes_by_path[candidate_path])
        return unique_notes(matches)

    def fallback_names(base):
        root_name = re.sub(r'(?i)(?: - DM Notes| \(OneNote\))$', '', base)
        return [root_name + ' - DM Notes', root_name + ' (OneNote)']

    def resolve(destination, source):
        exact = exact_path_matches(destination, source)
        if len(exact) == 1:
            return 'resolved-path', exact
        if len(exact) > 1:
            return 'ambiguous-path', exact

        base = Path(destination).stem
        matches, kind = named_matches(base)
        if len(matches) == 1:
            return 'resolved-' + kind, matches
        if len(matches) > 1:
            return 'ambiguous-' + kind, matches

        fallback = []
        for name in fallback_names(base):
            found, _ = named_matches(name)
            fallback.extend(found)
        fallback = unique_notes(fallback)
        if len(fallback) == 1:
            return 'resolved-fallback', fallback
        if len(fallback) > 1:
            return 'ambiguous-fallback', fallback
        return 'missing', []

    def note_reference(note):
        same_stem = unique_notes(stems[audit.norm(note['stem'])])
        if len(same_stem) == 1:
            return note['stem']
        return note['path'][:-3] if note['path'].casefold().endswith('.md') else note['path']

    def replacement_for(note, label, fragment):
        target = note_reference(note)
        if fragment:
            target += '#' + fragment
        if not label or (label == note['stem'] and not fragment):
            return f'[[{target}]]'
        return f'[[{target}|{label}]]'

    records = []
    rewrites = defaultdict(lambda: defaultdict(list))
    for path in sorted(root.rglob('*.md')):
        if not (audit.indexed_markdown(path) and audit.scanned_source(path)):
            continue
        source = audit.rel(path)
        lines = path.read_text(encoding='utf-8', errors='replace').splitlines(keepends=True)
        in_fence = False
        for line_number, line in enumerate(lines, 1):
            if re.match(r'^\s*(```|~~~)', line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            code_spans = [match.span() for match in re.finditer(r'(`+).*?\1', line)]
            wiki_spans = [match.span() for match in audit.LINK_RE.finditer(line)]
            for markdown_link in audit.parse_markdown_links(line):
                start, end = markdown_link['start'], markdown_link['end']
                if any(left <= start < right for left, right in code_spans + wiki_spans):
                    continue
                parsed = audit.local_markdown_target(markdown_link['body'])
                if not parsed:
                    continue
                destination, fragment = parsed
                status, matches = resolve(destination, source)
                record = {
                    'source': source,
                    'line': line_number,
                    'raw_link': markdown_link['raw_link'],
                    'label': markdown_link['label'],
                    'destination': destination,
                    'fragment': fragment,
                    'status': status,
                    'candidates': [item['path'] for item in matches],
                }
                if status.startswith('resolved-'):
                    replacement = replacement_for(matches[0], markdown_link['label'], fragment)
                    record['replacement'] = replacement
                    rewrites[source][line_number - 1].append((start, end, replacement))
                records.append(record)

    convertible = [item for item in records if item['status'].startswith('resolved-')]
    affected_files = sorted({item['source'] for item in convertible})
    overlap = sorted(set(affected_files) & dirty_paths(root))
    summary = {
        'mode': 'apply' if args.apply else 'dry-run',
        'total_local_markdown_links': len(records),
        'convertible_links': len(convertible),
        'affected_files': len(affected_files),
        'status_counts': dict(Counter(item['status'] for item in records)),
        'ambiguous_links': sum(item['status'].startswith('ambiguous-') for item in records),
        'missing_links': sum(item['status'] == 'missing' for item in records),
        'dirty_affected_files': overlap,
    }
    report = {
        'summary': summary,
        'ambiguous': [item for item in records if item['status'].startswith('ambiguous-')],
        'missing': [item for item in records if item['status'] == 'missing'],
        'conversions': convertible,
    }
    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    if args.apply:
        if overlap:
            raise SystemExit(
                'Refusing to modify files with existing uncommitted changes:\n'
                + '\n'.join(overlap)
            )
        for source, line_rewrites in rewrites.items():
            path = root / source
            lines = path.read_text(encoding='utf-8', errors='replace').splitlines(keepends=True)
            for line_index, replacements in line_rewrites.items():
                line = lines[line_index]
                for start, end, replacement in sorted(replacements, reverse=True):
                    line = line[:start] + replacement + line[end:]
                lines[line_index] = line
            path.write_text(''.join(lines), encoding='utf-8')

    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Conservative, single-output derivative of a YAML-registered polished transcript.

No LLM or heuristic deletion: an agent selects turns or small passages after reading
their context. All persistent state lives in the draft; every other input is read-only.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'process-transcript' / 'scripts'))
from transcript_core import lock, safe, parse_units  # shared read-only parsing / directory lock
import yaml

SOURCE_ID = 'transcriptProcessing.artifacts.polishedMarkdown'
META = '%% interactions-draft: '
INLINE = re.compile(r'\(\(([^()\n]+)\)\)')
SPAN = re.compile(r'^%% ([^\n%]+) %%\n', re.M)
PART = re.compile(r'(u\d{4,}):(\d+)-(\d+)')


class DraftError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise DraftError(message)


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def comment(prefix, value):
    text = compact(value)
    require('%%' not in text, 'Comment values cannot contain %%')
    return prefix + text + ' %%\n'


def read_comment(line, prefix, value_type=dict):
    require(line.startswith(prefix) and line.endswith(' %%'), 'Malformed draft control comment')
    value = json.loads(line[len(prefix):-3])
    require(isinstance(value, value_type), f'Control comment must contain a {value_type.__name__}')
    return value


def parse_polished(text):
    require('\r' not in text, 'Expected LF polished Markdown; do not normalize the source here')
    matches = [m for m in SPAN.finditer(text) if PART.match(m.group(1))]
    require(matches, 'Polished transcript has no supported UID:offset source comments')
    header = text[:matches[0].start()]
    turns = []
    for i, match in enumerate(matches):
        spans = []
        for part in match.group(1).split(', '):
            m = PART.fullmatch(part)
            require(m is not None, f'Malformed source span: {part}')
            uid, start, end = m.groups()
            require(int(end) > int(start), f'Empty or reversed source span: {part}')
            spans.append((uid, int(start), int(end)))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end():end]
        require(body.strip(), 'Empty mapped turn')
        turns.append({'spans': spans, 'body': body, 'raw': text[match.start():end]})
    return header, turns


def coverage(turns):
    result, seen = [], set()
    for turn in turns:
        for uid, start, end in turn['spans']:
            if result and uid == result[-1][0]:
                require(start == result[-1][2], f'Gap or overlap inside {uid}')
                result[-1] = (uid, result[-1][1], end)
            else:
                require(uid not in seen and start == 0, f'Reordered, repeated or partial UID: {uid}')
                seen.add(uid)
                result.append((uid, start, end))
    return result


def load(session_yaml):
    manifest = Path(session_yaml).absolute()
    require(manifest.name.endswith('-session.yaml') and manifest.parent.name == 'cleaned',
            'Expected cleaned/<stem>-session.yaml inside a session bundle')
    root = manifest.parent.parent.resolve()
    manifest = safe(root, 'cleaned/' + manifest.name)
    manifest_bytes = manifest.read_bytes()
    try:
        data = yaml.safe_load(manifest_bytes)
    except (yaml.YAMLError, ValueError) as exc:
        raise DraftError(f'Invalid session YAML: {exc}') from exc
    require(isinstance(data, dict) and data.get('sourceType') == 'transcript', 'YAML sourceType must be transcript')
    dates = {}
    for field in ('realWorldDate', 'drStart', 'drEnd'):
        value = str(data.get(field, ''))
        require(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', value)), f'YAML needs a known {field} date (YYYY-MM-DD)')
        try:
            dates[field] = date.fromisoformat(value)
        except ValueError as exc:
            raise DraftError(f'Invalid {field}: {value}') from exc
    require(dates['drEnd'] >= dates['drStart'], 'YAML drEnd precedes drStart')
    artifacts = data.get('transcriptProcessing', {}).get('artifacts', {})
    artifact = artifacts.get('polishedMarkdown', {})
    require(isinstance(artifact, dict) and artifact.get('path'), f'YAML must register {SOURCE_ID}.path; propose a repair without editing YAML')
    source = safe(root, artifact['path'])
    require(source.is_file(), f'YAML polished transcript cannot be located: {source}')
    source_bytes = source.read_bytes()
    require(not artifact.get('sha256') or sha(source_bytes) == artifact['sha256'], 'Polished transcript differs from its YAML fingerprint')
    header, turns = parse_polished(source_bytes.decode('utf-8'))
    mapped = coverage(turns)
    require(META not in header, 'Input is already a derivative')
    for turn in turns:
        require(re.match(r'[^\n:]+: ', turn['body']) is not None, 'Expected a speaker-labelled polished turn')
        require('((' not in turn['body'] and '))' not in turn['body'], 'Polished source uses reserved ((...)) syntax; report the collision without editing it')
        require(not re.search(r'^%%', turn['body'], re.M), 'Unsupported or malformed comment in polished turn; inspect without altering source')
    # Strengthen coverage against retained cleaned text when registered. It is never edited.
    fingerprints = {str(manifest.relative_to(root)): sha(manifest_bytes), artifact['path']: sha(source_bytes)}
    cleaned = artifacts.get('cleaned')
    if cleaned:
        path = safe(root, cleaned['path'])
        raw = path.read_bytes()
        require(not cleaned.get('sha256') or sha(raw) == cleaned['sha256'], 'Cleaned transcript differs from its YAML fingerprint')
        units = parse_units(raw.decode('utf-8'))
        require(mapped == [(u['uid'], 0, len(u['text'])) for u in units], 'Polished mapping does not completely cover cleaned UIDs')
        fingerprints[cleaned['path']] = sha(raw)
    stem = manifest.name.removesuffix('-session.yaml')
    draft = safe(root, f'cleaned/{stem}-interactions-draft.md')
    require(draft not in (manifest, source), 'Draft aliases an input')
    return {'root': root, 'manifest': manifest, 'data': data, 'source': source, 'draft': draft,
            'header': header, 'turns': turns, 'fingerprints': fingerprints, 'coverage': mapped,
            'sourceSha256': sha(source_bytes)}


def metadata(bundle):
    return {'version': 4, 'sessionYaml': str(bundle['manifest'].relative_to(bundle['root'])),
            'sourceSha256': bundle['sourceSha256']}


def assemble(bundle, meta, blocks):
    return (comment(META, meta) + '# Interaction processing draft\n\n'
            '> Derived working copy. Double-parenthesized snips are generated, not dialogue.\n\n'
            + bundle['header'] + ''.join(blocks))


def check_label(label, limit):
    require(isinstance(label, str) and label.strip() and '\n' not in label and '%%' not in label, 'Label must be one nonempty line')
    require(not any(c in label for c in '<>[]()\r'), 'Labels must be plain text, without parentheses, links or markup')
    require(len(label.split()) <= limit, f'Label exceeds {limit} words')
    require(not re.search(r'[.!?]\s+\S', label), 'A snip may contain at most one sentence')


def apply_cuts(turn, cuts):
    """Validate transient matches against source; no cut positions are persisted."""
    original = turn['body']
    prefix = re.match(r'[^\n:]+: ', original).end()
    require(isinstance(cuts, list) and cuts, 'Inline cuts must be a nonempty list')
    cursor, output, retained = 0, [], []
    protected = list(re.finditer(r'\{\{.*?\}\}|\[\[.*?\]\]|%%.*?%%', original, re.S))
    for item in cuts:
        require(isinstance(item, list) and len(item) == 3, 'Each inline cut is [start,end,label]')
        start, end, label = item
        require(type(start) is int and type(end) is int, 'Inline offsets must be integers')
        require(prefix <= start < end <= len(original.rstrip()), 'Inline cut must stay inside speech, outside speaker/separator')
        require(start >= cursor, 'Inline cuts overlap or are out of order')
        require(original[start:end].strip(), 'Do not substitute whitespace alone')
        word = lambda c: c.isalnum() or c in "_'’"
        require(not (word(original[start-1]) and word(original[start])), 'Inline cut starts inside a word')
        require(end == len(original) or not (word(original[end-1]) and word(original[end])), 'Inline cut ends inside a word')
        require(not any(start < m.end() and m.start() < end for m in protected),
                'Inline cut overlaps an uncertainty marker, wikilink or source comment')
        check_label(label, 6)
        output.extend([original[cursor:start], '((' + label + '))'])
        retained.append(original[max(cursor, prefix):start])
        cursor = end
    output.append(original[cursor:])
    retained.append(original[cursor:])
    require(any(c.isalnum() for c in ''.join(retained)), 'Inline cuts must leave original speech; use a whole-turn snip otherwise')
    return ''.join(output)


def match_inline(turn, body):
    """Check retained wording in order, treating ((labels)) as omitted source text.

    Matches exist only during validation. Restoration always uses the whole turn;
    there is no stored sub-turn alignment or individually restorable cut.
    """
    if body == turn['body']:
        return []
    markers = list(INLINE.finditer(body))
    literals = INLINE.split(body)[::2]
    require(markers and all('((' not in part and '))' not in part for part in literals),
            'Unmarked change or malformed ((label)) in retained turn')
    pattern = '(.+?)'.join(re.escape(part) for part in literals)
    match = re.fullmatch(pattern, turn['body'], flags=re.S)
    require(match is not None, 'Unmarked change to retained wording or speaker')
    cuts = [[*match.span(i + 1), marker.group(1)] for i, marker in enumerate(markers)]
    require(apply_cuts(turn, cuts) == body, 'Invalid inline substitution')
    return cuts


def inspect_draft(bundle, text=None):
    if text is None:
        text = bundle['draft'].read_text(encoding='utf-8')
    line, rest = text.split('\n', 1)
    meta = read_comment(line, META)
    require(type(meta.get('version')) is int and meta['version'] == 4, 'Unsupported draft version')
    require(meta == metadata(bundle), 'Draft source or metadata changed; do not overwrite or silently rebase this draft')
    header, blocks = parse_polished(rest)
    expected_header = assemble(bundle, meta, []).split('\n', 1)[1]
    require(header == expected_header, 'Draft/source header changed outside permitted substitutions')
    require(coverage(blocks) == bundle['coverage'], 'Draft source coverage differs from polished transcript')
    cursor, snippets = 0, []
    for block in blocks:
        start, spans = cursor, []
        # Exact inherited span partitions identify the original turns, even when
        # a turn combines UIDs or a UID spans multiple turns. No saved turn IDs.
        while len(spans) < len(block['spans']):
            require(cursor < len(bundle['turns']), 'Block has no source turn')
            spans.extend(bundle['turns'][cursor]['spans'])
            cursor += 1
        require(block['spans'] == spans, 'A block source map was reassigned or changed')
        block['startTurn'], block['endTurn'] = start + 1, cursor
        marker = re.fullmatch(INLINE.pattern + r'\n\n', block['body'])
        block['snipped'] = marker is not None
        if marker:
            label = marker.group(1)
            check_label(label, 40)
            snippets.append({'startTurn': start + 1, 'endTurn': cursor, 'label': label})
        else:
            require(cursor == start + 1, 'Retained text must stay within one original polished turn')
            block['cuts'] = match_inline(bundle['turns'][start], block['body'])
    require(cursor == len(bundle['turns']), 'Some polished turns are missing')
    return meta, blocks, snippets


def write_only_draft(bundle, text, before=None):
    """One permitted pathname, no sidecars/temporary files; caller holds bundle lock.

    An interrupted in-place update can leave an invalid draft. Validation detects
    that; never repair by overwriting source or silently discarding human edits.
    """
    inspect_draft(bundle, text)
    for relative, digest in bundle['fingerprints'].items():
        require(sha(safe(bundle['root'], relative).read_bytes()) == digest, f'Input changed during work: {relative}')
    path = safe(bundle['root'], str(bundle['draft'].relative_to(bundle['root'])))
    if before is None:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
    else:
        require(path.read_bytes() == before, 'Draft changed concurrently')
        flags = os.O_RDWR | os.O_NOFOLLOW
    fd = os.open(path, flags, 0o644)
    try:
        require(os.fstat(fd).st_nlink == 1, 'Draft must not be a hard link')
        if before is not None:
            with os.fdopen(os.dup(fd), 'rb') as check:
                require(check.read() == before, 'Draft changed while opening')
        os.lseek(fd, 0, os.SEEK_SET)
        raw = text.encode('utf-8')
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            require(written > 0, 'Incomplete draft write')
            view = view[written:]
        os.ftruncate(fd, len(raw))
        os.fsync(fd)
    finally:
        os.close(fd)


def initialize(bundle):
    with lock(bundle['root']):
        require(not bundle['draft'].exists(), 'Draft already exists; inspect/resume it rather than replacing it')
        write_only_draft(bundle, assemble(bundle, metadata(bundle), [t['raw'] for t in bundle['turns']]))


def snip(bundle, start, end, label, names=()):
    with lock(bundle['root']):
        before = bundle['draft'].read_bytes()
        meta, blocks, _ = inspect_draft(bundle, before.decode())
        selected = [b for b in blocks if b['startTurn'] >= start and b['endTurn'] <= end]
        require(selected and selected[0]['startTurn'] == start and selected[-1]['endTurn'] == end,
                'Snip boundaries must match complete original turns')
        require(all(not b['snipped'] and not b.get('cuts') for b in selected), 'Range already includes a snip or inline cuts; restore them first')
        check_label(label, 40)
        original = ''.join(b['body'] for b in selected)
        for name in names:
            require(isinstance(name, str) and name.strip() and name in original and name in label,
                    f'Preserved name must occur in the source and label: {name}')
        spans = [s for b in selected for s in b['spans']]
        marker = '%% ' + ', '.join(f'{u}:{a}-{z}' for u, a, z in spans) + ' %%\n'
        replacement = marker + '((' + label + '))\n\n'
        rendered = []
        for b in blocks:
            if b['startTurn'] == start:
                rendered.append(replacement)
            elif start < b['startTurn'] <= end:
                continue
            else:
                rendered.append(b['raw'])
        write_only_draft(bundle, assemble(bundle, meta, rendered), before)


def restore(bundle, turn_number):
    """Restore the complete polished turn, or complete snip covering that turn."""
    with lock(bundle['root']):
        before = bundle['draft'].read_bytes()
        meta, blocks, _ = inspect_draft(bundle, before.decode())
        matches = [b for b in blocks if b['startTurn'] <= turn_number <= b['endTurn']
                   and (b['snipped'] or b.get('cuts'))]
        require(len(matches) == 1, 'No snips on that original turn')
        target = matches[0]
        replacement = ''.join(t['raw'] for t in bundle['turns'][target['startTurn']-1:target['endTurn']])
        write_only_draft(bundle, assemble(bundle, meta, [replacement if b is target else b['raw'] for b in blocks]), before)


def cut(bundle, turn_number, text, label, occurrence=None):
    """Replace exact retained words; optionally select a one-based occurrence."""
    require(type(turn_number) is int and 1 <= turn_number <= len(bundle['turns']), 'Invalid original turn number')
    require(isinstance(text, str) and text.strip(), 'Select nonempty exact retained text')
    with lock(bundle['root']):
        before = bundle['draft'].read_bytes()
        meta, blocks, _ = inspect_draft(bundle, before.decode())
        targets = [b for b in blocks if b['startTurn'] == b['endTurn'] == turn_number and not b['snipped']]
        require(len(targets) == 1, 'Turn is already covered by a whole-turn snip; restore it first')
        target = targets[0]
        body = target['body']
        markers = list(INLINE.finditer(body))
        matches = [m.start() for m in re.finditer('(?=' + re.escape(text) + ')', body)
                   if not any(m.start() < marker.end() and marker.start() < m.start() + len(text) for marker in markers)]
        if occurrence is None:
            require(len(matches) == 1, 'Text must occur exactly once in retained speech; use --occurrence when repeated')
            occurrence = 1
        require(type(occurrence) is int and 1 <= occurrence <= len(matches), 'No such occurrence in retained speech')
        start = matches[occurrence - 1]
        replacement = target['raw'][:-len(body)] + body[:start] + '((' + label + '))' + body[start + len(text):]
        write_only_draft(bundle, assemble(bundle, meta, [replacement if b is target else b['raw'] for b in blocks]), before)


def stats(bundle):
    _, blocks, snippets = inspect_draft(bundle)
    original = sum(len(t['body'].split()) for t in bundle['turns'])
    retained, reading, inline = 0, 0, []
    for block in blocks:
        if block['snipped']:
            continue
        source = bundle['turns'][block['startTurn']-1]
        cuts = block.get('cuts', [])
        inline.extend(cuts)
        reading += len((apply_cuts(source, cuts) if cuts else source['body']).split())
        cursor = 0
        for start, end, _ in cuts:
            retained += len(source['body'][cursor:start].split())
            cursor = end
        retained += len(source['body'][cursor:].split())
    generated = sum(len(s['label'].split()) for s in snippets)
    reading += generated
    generated += sum(len(c[2].split()) for c in inline)
    return {'draft': str(bundle['draft']), 'sourceTurns': len(bundle['turns']), 'sourceUids': len(bundle['coverage']),
            'snips': len(snippets),
            'inlineSnips': len(inline), 'editedTurns': sum(bool(b.get('cuts')) for b in blocks),
            'sourceWords': original, 'retainedWords': retained, 'generatedWords': generated,
            'readingTextReductionPercent': round(100 * (1 - reading / original), 1),
            'coverage': 'complete',
            'note': 'Coverage and verbatim checks do not prove that omitted material is unimportant.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session-yaml', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('inspect')
    sub.add_parser('init')
    sub.add_parser('validate')
    show = sub.add_parser('show')
    show.add_argument('--start', type=int, default=1)
    show.add_argument('--end', type=int)
    snip_cmd = sub.add_parser('snip')
    snip_cmd.add_argument('--start', type=int, required=True)
    snip_cmd.add_argument('--end', type=int, required=True)
    snip_cmd.add_argument('--label', required=True)
    snip_cmd.add_argument('--name', action='append', default=[])
    inline = sub.add_parser('cut')
    inline.add_argument('--turn', type=int, required=True)
    inline.add_argument('--text', required=True)
    inline.add_argument('--label', default='rolls')
    inline.add_argument('--occurrence', type=int, help='One-based occurrence in remaining speech, only needed for repeated text')
    undo = sub.add_parser('restore')
    undo.add_argument('--turn', type=int, required=True)
    args = parser.parse_args()
    try:
        bundle = load(args.session_yaml)
        if args.command == 'show':
            end = args.end or len(bundle['turns'])
            require(1 <= args.start <= end <= len(bundle['turns']), 'Invalid original turn range')
            for i in range(args.start - 1, end):
                turn = bundle['turns'][i]
                print(f"TURN {i+1} [{turn['spans'][0][0]}–{turn['spans'][-1][0]}]\n{turn['body']}", end='')
            return
        if args.command == 'inspect':
            result = {'sessionYaml': str(bundle['manifest']), 'polishedTranscript': str(bundle['source']),
                      'draft': str(bundle['draft']), 'dates': {k: str(bundle['data'][k]) for k in ('realWorldDate', 'drStart', 'drEnd')},
                      'turns': len(bundle['turns']), 'uids': len(bundle['coverage'])}
        else:
            if args.command == 'init':
                initialize(bundle)
            elif args.command == 'snip':
                snip(bundle, args.start, args.end, args.label, args.name)
            elif args.command == 'restore':
                restore(bundle, args.turn)
            elif args.command == 'cut':
                cut(bundle, args.turn, args.text, args.label, args.occurrence)
            result = stats(bundle)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.exit(1, f'error: {exc}\n')


if __name__ == '__main__':
    main()

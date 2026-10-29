#!/usr/bin/env python3
"""Session-local storage, UID parsing, source mapping and speech-fidelity checks."""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True
import base64
import contextlib
import fcntl
import hashlib
import html
import json
import os
from pathlib import Path
import re
import unicodedata
import uuid

VERSION = 1
EDITORIAL_POLICY = 3
WORK = 'cleaned/transcript-work'
STATE = WORK + '/state.json'
LINE = re.compile(r'^(\[(u\d{4,})\s*\|\s*([^|]+)\|\s*([^\]]+)\])(\s+)(.*)$')
MARKER = re.compile(r'\{\{([^{}\n]+)\}\}')
KINDS = {'person', 'group', 'place', 'time', 'item', 'action', 'speaker', 'other'}
CHECKS = {'people', 'groups', 'places', 'time_transitions', 'items', 'actions', 'unmarked_errors', 'second_pass'}
ANNOTATION = re.compile(r'\[\[[^\n]*?\]\]|\[[^\]\n]+\]')


class PipelineError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise PipelineError(message)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, default=str) + '\n').encode()


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def fingerprint(value):
    return sha(encoded(value))


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def safe(root, relative):
    root = Path(root).resolve()
    require(not Path(relative).is_absolute(), f'Managed path must be relative: {relative}')
    candidate = root / relative
    resolved = candidate.resolve()
    require(resolved.is_relative_to(root) and resolved != root, f'Path escapes session bundle: {relative}')
    for part in [candidate, *candidate.parents]:
        if part == root:
            break
        require(not part.is_symlink(), f'Managed path is a symlink: {relative}')
    return candidate


def atomic(root, relative, data):
    path = safe(root, relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        with temp.open('xb') as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


@contextlib.contextmanager
def lock(root):
    # The bundle directory survives finalization; a deleted lock file would let
    # another writer acquire a different inode before the first writer exits.
    handle = os.open(root, os.O_RDONLY)
    try:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise PipelineError('Another writer is working in this session bundle.') from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)
    finally:
        os.close(handle)


def current_hash(path):
    return sha(path.read_bytes()) if path.exists() else None


def finish_transaction(root, relative, tx):
    require(tx['status'] == 'pending', 'Transaction is not pending')
    written = {item['path'] for item in tx['files']}
    for path, digest in tx.get('inputs', {}).items():
        if path not in written:
            require(current_hash(safe(root, path)) == digest, f'Transaction input changed: {path}')
    for item in tx['files']:
        require(current_hash(safe(root, item['path'])) in {item['beforeSha256'], item['afterSha256']},
                f"Transaction conflicts with a later edit: {item['path']}")
    for item in tx['files']:
        path = safe(root, item['path'])
        if current_hash(path) != item['afterSha256']:
            require(current_hash(path) == item['beforeSha256'], f"Concurrent edit: {item['path']}")
            data = base64.b64decode(item['after'])
            require(sha(data) == item['afterSha256'], 'Corrupt transaction payload')
            atomic(root, item['path'], data)
    tx['status'] = 'committed'
    atomic(root, relative, encoded(tx))


def recover(root):
    root = Path(root).resolve()
    folder = safe(root, WORK + '/transactions')
    recovered = []
    for path in sorted(folder.glob('*.json')) if folder.exists() else []:
        tx = read_json(path)
        if tx['status'] == 'pending':
            relative = str(path.relative_to(root))
            finish_transaction(root, relative, tx)
            recovered.append(relative)
    return recovered


def commit(root, files, reason, expected=None):
    """Caller holds the session lock. Snapshots and intended writes stay in-bundle."""
    for relative, digest in (expected or {}).items():
        require(current_hash(safe(root, relative)) == digest, f'Input changed before commit: {relative}')
    records = []
    for relative, data in files.items():
        path = safe(root, relative)
        data = data if isinstance(data, bytes) else data.encode()
        before = path.read_bytes() if path.exists() else None
        if before == data:
            continue
        records.append({'path': relative, 'beforeSha256': sha(before) if before is not None else None,
                        'afterSha256': sha(data), 'before': base64.b64encode(before).decode() if before is not None else None,
                        'after': base64.b64encode(data).decode()})
    for relative, digest in (expected or {}).items():
        require(current_hash(safe(root, relative)) == digest, f'Input changed while preparing commit: {relative}')
    if not records:
        return None
    relative = WORK + '/transactions/' + uuid.uuid4().hex + '.json'
    tx = {'schemaVersion': VERSION, 'status': 'pending', 'reason': reason, 'files': records, 'inputs': expected or {}}
    atomic(root, relative, encoded(tx))
    finish_transaction(root, relative, tx)
    return relative


def seconds(value):
    require(bool(re.fullmatch(r'\d+(?::\d+){0,2}(?:\.\d+)?', value.strip())), f'Invalid time: {value}')
    parts = [float(x) for x in value.split(':')]
    require(len(parts) == 1 or parts[-1] < 60, f'Invalid seconds: {value}')
    require(len(parts) < 3 or parts[1] < 60, f'Invalid minutes: {value}')
    return sum(x * 60 ** i for i, x in enumerate(reversed(parts)))


def parse_units(text):
    units, seen = [], set()
    for number, line in enumerate(text.lstrip('\ufeff').splitlines(), 1):
        if not line.strip():
            continue
        match = LINE.fullmatch(line)
        require(match is not None, f'Invalid UID transcript line {number}')
        header, uid, timing, speaker, separator, wording = match.groups()
        require(uid not in seen, f'Duplicate UID: {uid}')
        seen.add(uid)
        pair = timing.strip().split('-')
        require(len(pair) == 2 and seconds(pair[1]) >= seconds(pair[0]), f'Invalid timing: {uid}')
        remainder = MARKER.sub('', wording)
        require('{{' not in remainder and '}}' not in remainder, f'Malformed uncertainty marker: {uid}')
        require(bool(wording.strip()), f'Empty source unit: {uid}')
        units.append({'uid': uid, 'header': header, 'separator': separator,
                      'speaker': speaker.strip(), 'timing': timing.strip(), 'text': wording})
    require(bool(units), 'Transcript is empty')
    return units


def render_units(units):
    return ''.join(u['header'] + u.get('separator', ' ') + u['text'] + '\n' for u in units)


def validate_baseline(prepared, cleaned):
    require([u['header'] for u in prepared] == [u['header'] for u in cleaned],
            'Prepared/cleaned IDs, timestamps, order, or speaker headers differ; resolve explicitly before processing')


def words(text):
    """Preserve contractions and numeric punctuation; permit case/typography changes."""
    text = unicodedata.normalize('NFC', text).replace('’', "'").replace('‘', "'").casefold()
    return re.findall(r"[+-]?\d+(?:[.,:/-]\d+)*|[^\W\d_]+(?:'[^\W\d_]+)*|_+", text, re.UNICODE)


def symbols(text):
    text = unicodedata.normalize('NFC', text)
    return [c for i, c in enumerate(text) if (unicodedata.category(c).startswith('S') or c in '%‰‱#'
            or (c == '-' and (i == 0 or not text[i-1].isalnum()) and re.match(r'\s*\d', text[i+1:])))]


def markers(text):
    return [words(x) for x in MARKER.findall(text)]


def chunk_units(units, target=1800):
    chunks, start, count = [], 0, 0
    for i, unit in enumerate(units):
        count += len(words(unit['text']))
        boundary = i == len(units)-1 or units[i+1]['speaker'] != unit['speaker'] or bool(re.search(r'[.!?…][\"\x27)]?$', unit['text']))
        if (count >= target and boundary) or i == len(units) - 1:
            chunks.append({'id': f'chunk-{len(chunks) + 1:03d}', 'startUid': units[start]['uid'], 'endUid': unit['uid']})
            start, count = i + 1, 0
    return chunks


def selected(units, chunk, context=0):
    order = {u['uid']: i for i, u in enumerate(units)}
    require(chunk['startUid'] in order and chunk['endUid'] in order, 'Source segmentation changed; preserve existing UIDs')
    a, b = order[chunk['startUid']], order[chunk['endUid']]
    return units[max(0, a-context):min(len(units), b+context+1)]


def speaker_for(unit, start, end, attributions):
    relevant = [a for a in attributions if a['uid'] == unit['uid'] and a['start'] < end and a['end'] > start]
    if not relevant:
        return unit['speaker']
    require(len(relevant) == 1 and relevant[0]['start'] <= start and relevant[0]['end'] >= end,
            f"Turn crosses a speaker correction boundary: {unit['uid']}")
    item = relevant[0]
    require(item['textSha256'] == sha(unit['text']), f"Speaker correction is stale: {unit['uid']}")
    return item['speaker']


def validate_attributions(units, attributions):
    by_uid = {u['uid']: u for u in units}
    occupied = {}
    for a in attributions:
        require(a.get('uid') in by_uid, 'Unknown attribution UID')
        u = by_uid[a['uid']]
        require(type(a.get('start')) is int and type(a.get('end')) is int and 0 <= a['start'] < a['end'] <= len(u['text']), 'Invalid attribution bounds')
        require(a.get('textSha256') == sha(u['text']), f"Speaker correction is stale: {u['uid']}")
        require(isinstance(a.get('speaker'), str) and bool(a['speaker'].strip()) and ':' not in a['speaker'] and '\n' not in a['speaker'], 'Invalid corrected speaker')
        require(bool(a.get('reason', '').strip()) and bool(a.get('evidence')), 'Speaker correction needs reason and evidence')
        for start, end in occupied.setdefault(u['uid'], []):
            require(end <= a['start'] or start >= a['end'], 'Overlapping speaker corrections')
        occupied[u['uid']].append((a['start'], a['end']))


def draft_turns(units, attributions):
    result = []
    for unit in units:
        boundaries = {0, len(unit['text'])}
        for a in attributions:
            if a['uid'] == unit['uid']:
                boundaries.update([a['start'], a['end']])
        points = sorted(boundaries)
        for start, end in zip(points, points[1:]):
            result.append({'speaker': speaker_for(unit, start, end, attributions),
                           'sources': [{'uid': unit['uid'], 'start': start, 'end': end}],
                           'text': unit['text'][start:end]})
    return result


def validate_turns(turns, units, attributions):
    require(isinstance(turns, list) and turns, 'Polished turns are required')
    i, offset = 0, 0
    for position, turn in enumerate(turns):
        require('joinPrevious' not in turn or (position == 0 and type(turn['joinPrevious']) is bool), 'joinPrevious is permitted only on the first turn of a chunk')
        require(isinstance(turn.get('text'), str) and bool(turn['text'].strip()), 'Empty polished turn')
        require(isinstance(turn.get('sources'), list) and turn['sources'], 'Missing source spans')
        source = []
        substitutions = turn.get('substitutions', [])
        require(isinstance(substitutions, list), 'Substitutions must be a list')
        used = set()
        for span in turn['sources']:
            require(i < len(units), 'Duplicate or extra source coverage')
            unit = units[i]
            require(span.get('uid') == unit['uid'] and type(span.get('start')) is int and span['start'] == offset,
                    'Source spans must cover every character once, in source order')
            end = span.get('end')
            require(type(end) is int and offset < end <= len(unit['text']), 'Invalid source span end')
            for point in (offset, end):
                require(not (0 < point < len(unit['text']) and (unit['text'][point-1].isalnum() or unit['text'][point-1] in "'’") and (unit['text'][point].isalnum() or unit['text'][point] in "'’")), f"Source span splits a word: {unit['uid']}")
                require(not any(m.start() < point < m.end() for pattern in (MARKER, ANNOTATION) for m in pattern.finditer(unit['text'])), 'Source span splits a marker or annotation')
            require(turn.get('speaker') == speaker_for(unit, offset, end, attributions), f"Unlogged speaker change in {unit['uid']}")
            text = unit['text'][offset:end]
            replacements = []
            for number, replacement in enumerate(substitutions):
                require(isinstance(replacement, dict), 'Invalid substitution')
                if replacement.get('uid') != unit['uid']:
                    continue
                a, b = replacement.get('start'), replacement.get('end')
                require(type(a) is int and type(b) is int and 0 <= a < b <= len(unit['text']), 'Invalid substitution bounds')
                if a >= end or b <= offset:
                    continue
                require(offset <= a < b <= end, 'Substitution crosses a source-span boundary')
                require(replacement.get('kind') in {'garbled', 'cross-talk'}, 'Unsupported substitution label')
                require(isinstance(replacement.get('reason'), str) and bool(replacement['reason'].strip()), 'Substitution needs an editorial reason')
                for point in (a, b):
                    require(not (0 < point < len(unit['text']) and (unit['text'][point-1].isalnum() or unit['text'][point-1] in "'’") and (unit['text'][point].isalnum() or unit['text'][point] in "'’")), 'Substitution splits a word')
                require(not any(m.start() < b and m.end() > a for pattern in (MARKER, ANNOTATION) for m in pattern.finditer(unit['text'])), 'Substitution hides a review marker, annotation, or wikilink')
                replacements.append((a-offset, b-offset, replacement['kind']))
                used.add(number)
            replacements.sort()
            require(all(left[1] <= right[0] for left, right in zip(replacements, replacements[1:])), 'Overlapping substitutions')
            for a, b, kind in reversed(replacements):
                text = text[:a] + '[' + kind + ']' + text[b:]
            source.append(text)
            offset = end
            if offset == len(unit['text']):
                i, offset = i + 1, 0
        require(len(used) == len(substitutions), 'Substitution is outside this turn or duplicates another source span')
        wording = ' '.join(source)
        require(words(wording) == words(turn['text']), 'Polishing changed words; record a supported upstream correction first')
        require(symbols(wording) == symbols(turn['text']), 'Polishing changed a meaningful symbol')
        require(ANNOTATION.findall(wording) == ANNOTATION.findall(turn['text']), 'Polishing changed an annotation or wikilink')
        require(markers(wording) == markers(turn['text']), 'Polishing changed or removed uncertainty markers')
        remainder = MARKER.sub('', turn['text'])
        require('{{' not in remainder and '}}' not in remainder, 'Malformed polished marker')
    require(i == len(units) and offset == 0, 'Polished transcript has missing source coverage')


def render_polished(turns, title, source, status):
    display_status = {'complete': 'Complete', 'complete_with_uncertainty': 'Complete with retained uncertainty', 'needs_manual_review': 'Some passages need review', 'needs_quality_review': 'Draft awaiting quality review'}.get(status, status)
    md = [f'# {title}', '', f'- Status: {display_status}', f'- Source Transcript: {source}', '', '## Transcript', '']
    paragraphs = []
    for index, turn in enumerate(turns, 1):
        spans = ', '.join(f"{s['uid']}:{s['start']}-{s['end']}" for s in turn['sources'])
        md += [f'%% {spans} %%', f"{turn['speaker']}: {turn['text']}", '']
        paragraphs.append(f'<p id="turn-{index:05d}"><strong>{html.escape(turn["speaker"])}:</strong> {html.escape(turn["text"])}</p>')
    page = ('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
            f'<title>{html.escape(title)}</title><style>body{{max-width:48rem;margin:3rem auto;padding:0 1rem;font:18px/1.6 system-ui}}'
            'p{white-space:pre-wrap}.status{color:#555}</style>'
            f'<h1>{html.escape(title)}</h1><p class="status">{html.escape(display_status)}</p>' + '\n'.join(paragraphs) + '</html>\n')
    return '\n'.join(md), page

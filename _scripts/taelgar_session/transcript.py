"""Read the YAML-registered polished transcript and verify original UID coverage."""
from datetime import date
from pathlib import Path
import re
import yaml
from .storage import safe, sha, open_no_follow
from .units import parse_units

SOURCE_ID = 'transcriptProcessing.artifacts.polishedMarkdown'
# Reject a former derivative accidentally registered as original polished speech.
DERIVATIVE_MARKER = '%% interactions-draft: '
SPAN = re.compile(r'^%% ([^\n%]+) %%\n', re.M)
PART = re.compile(r'(u\d{4,}):(\d+)-(\d+)')


class SourceError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise SourceError(message)


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


def load(session_yaml, *, allow_unknown_dates=False, allow_source_changes=False):
    """Read shared sources; source-change inspection is a read-only entity opt-in."""
    manifest = Path(session_yaml).absolute()
    require(manifest.name.endswith('-session.yaml') and manifest.parent.name == 'cleaned',
            'Expected cleaned/<stem>-session.yaml inside a session bundle')
    root = manifest.parent.parent.resolve()
    manifest = safe(root, 'cleaned/' + manifest.name)
    manifest_bytes = manifest.read_bytes()
    try:
        data = yaml.safe_load(manifest_bytes)
    except (yaml.YAMLError, ValueError) as exc:
        raise SourceError(f'Invalid session YAML: {exc}') from exc
    require(isinstance(data, dict) and data.get('sourceType') == 'transcript', 'YAML sourceType must be transcript')
    dates = {}
    for field in ('realWorldDate', 'drStart', 'drEnd'):
        if allow_unknown_dates and data.get(field) is None:
            continue
        value = str(data.get(field, ''))
        require(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', value)), f'YAML needs a known {field} date (YYYY-MM-DD)')
        try:
            dates[field] = date.fromisoformat(value)
        except ValueError as exc:
            raise SourceError(f'Invalid {field}: {value}') from exc
    if 'drStart' in dates and 'drEnd' in dates:
        require(dates['drEnd'] >= dates['drStart'], 'YAML drEnd precedes drStart')
    artifacts = data.get('transcriptProcessing', {}).get('artifacts', {})
    artifact = artifacts.get('polishedMarkdown', {})
    require(isinstance(artifact, dict) and artifact.get('path'), f'YAML must register {SOURCE_ID}.path; propose a repair without editing YAML')
    source = safe(root, artifact['path'])
    require(source.is_file(), f'YAML polished transcript cannot be located: {source}')
    source_bytes = source.read_bytes()
    require(allow_source_changes or not artifact.get('sha256') or sha(source_bytes) == artifact['sha256'], 'Polished transcript differs from its YAML fingerprint')
    header, turns = parse_polished(source_bytes.decode('utf-8'))
    mapped = coverage(turns)
    require(DERIVATIVE_MARKER not in header, 'Input is already a derivative')
    for turn in turns:
        require(re.match(r'[^\n:]+: ', turn['body']) is not None, 'Expected a speaker-labelled polished turn')
        require(not re.search(r'^%%', turn['body'], re.M), 'Unsupported or malformed comment in polished turn; inspect without altering source')
    # Strengthen coverage against retained cleaned text when registered. It is never edited.
    fingerprints = {manifest.relative_to(root).as_posix(): sha(manifest_bytes), artifact['path']: sha(source_bytes)}
    cleaned = artifacts.get('cleaned')
    if cleaned:
        path = safe(root, cleaned['path'])
        raw = path.read_bytes()
        require(allow_source_changes or not cleaned.get('sha256') or sha(raw) == cleaned['sha256'], 'Cleaned transcript differs from its YAML fingerprint')
        units = parse_units(raw.decode('utf-8'))
        require(mapped == [(u['uid'], 0, len(u['text'])) for u in units], 'Polished mapping does not completely cover cleaned UIDs')
        fingerprints[cleaned['path']] = sha(raw)
    return {'root': root, 'manifest': manifest, 'data': data, 'source': source,
            'header': header, 'turns': turns, 'fingerprints': fingerprints, 'coverage': mapped,
            'sourceSha256': sha(source_bytes)}

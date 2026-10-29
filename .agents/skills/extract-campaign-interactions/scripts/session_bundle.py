"""Read authoritative session bundles and map polished prose to retained UIDs.

No inferred path becomes an extraction input. Repairs are proposals for YAML.
The processing pipeline's artifact paths are bundle-relative; legacy explicit
cleanedSourcePath and new output pointers are relative to the YAML directory.
"""
import copy
import hashlib
import json
import os
import re
from pathlib import Path

import yaml
from session_model import SourceCatalog, digest, require, vault_path

PREFIX = 'transcriptProcessing.artifacts.'
CLEANED = PREFIX + 'cleaned'
POLISHED = PREFIX + 'polishedMarkdown'
LEGACY = 'cleanedSourcePath'
OUTPUT_KEY = 'interactionExtraction'


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()


class BundleError(ValueError):
    def __init__(self, message, proposals=None):
        super().__init__(message)
        self.proposals = proposals or []


def bundle_root(manifest):
    return manifest.parent.parent if manifest.parent.name == 'cleaned' else manifest.parent


def load_bundle(vault, reference):
    vault = Path(vault).resolve()
    manifest = vault_path(vault, reference)
    metadata = yaml.safe_load(manifest.read_text())
    require(isinstance(metadata, dict), 'Session YAML must be a mapping')
    for key in ('campaign', 'sessionNumber', 'realWorldDate'):
        require(metadata.get(key) is not None, f'Session YAML lacks {key}')
    require(metadata.get('sourceType') == 'transcript', 'Only transcript extraction is supported')
    root = bundle_root(manifest)
    proposals, descriptors = [], {}

    def resolve(field, value, base, preferred=None):
        if not isinstance(value, str) or not value:
            return None
        candidate = Path(value) if Path(value).is_absolute() else base / value
        exact = True
        try:
            resolved = vault_path(vault, str(candidate.relative_to(vault)))
        except (ValueError, OSError):
            exact = False
            # Look only inside this bundle to suggest a repair; never use it silently.
            matches = [p for p in (root / 'cleaned' / Path(value).name,
                                   root / 'sources' / Path(value).name) if p.is_file()]
            matches = list(dict.fromkeys(matches))
            resolved = matches[0] if len(matches) == 1 else None
        if not exact or resolved is None or Path(value).is_absolute():
            proposal = {'field': field, 'current': value,
                        'reason': 'Missing or machine-specific source path in session YAML.'}
            if resolved is not None:
                proposal['proposed'] = os.path.relpath(resolved, preferred or base)
            proposals.append(proposal)
            return None
        return resolved

    artifacts = metadata.get('transcriptProcessing', {}).get('artifacts', {})
    for key in ('cleaned', 'polishedMarkdown'):
        if key in artifacts:
            item = artifacts[key]
            require(isinstance(item, dict) and item.get('path'), f'Invalid YAML artifact: {key}')
            path = resolve(PREFIX + key + '.path', item['path'], root)
            if path:
                if item.get('sha256') and digest(path) != item['sha256']:
                    raise BundleError(f'Source hash changed for YAML artifact {key}; recheck transcript processing provenance.')
                descriptors[PREFIX + key] = {'id': PREFIX + key, 'kind': 'transcript',
                                            'path': str(path.relative_to(vault)), 'sha256': digest(path)}
    if CLEANED not in descriptors and LEGACY in metadata:
        path = resolve(LEGACY, metadata[LEGACY], manifest.parent)
        if path:
            descriptors[LEGACY] = {'id': LEGACY, 'kind': 'transcript',
                                   'path': str(path.relative_to(vault)), 'sha256': digest(path)}
    cleaned_id = CLEANED if CLEANED in descriptors else LEGACY
    if cleaned_id not in descriptors:
        candidate = manifest.with_name(manifest.name.replace('-session.yaml', '-source-cleaned.md'))
        if LEGACY not in metadata and 'cleaned' not in artifacts:
            proposal = {'field': LEGACY, 'reason': 'YAML does not identify a cleaned transcript.'}
            if candidate.is_file() and candidate != manifest:
                proposal['proposed'] = os.path.relpath(candidate, manifest.parent)
            proposals.append(proposal)
        raise BundleError('Register/fix the cleaned transcript in session YAML before extraction.', proposals)
    if 'polishedMarkdown' in artifacts and POLISHED not in descriptors:
        raise BundleError('Fix the registered polished transcript path before extraction.', proposals)

    # Report stale ancillary paths without blocking a valid retained transcript.
    for key in ('sourceInputPath', 'sourceConfigPath', 'participantsPath', 'preparedSourcePath',
                'speakerMappingsPath', 'speakerStatsPath', 'sourceAudioPath'):
        if metadata.get(key):
            resolve(key, metadata[key], manifest.parent)
    selected = POLISHED if POLISHED in descriptors else cleaned_id
    canonical = {k: v for k, v in metadata.items() if k != OUTPUT_KEY}
    return {'manifest': manifest, 'metadata': metadata, 'root': root, 'sources': descriptors,
            'sourceId': selected, 'cleanedId': cleaned_id, 'proposals': proposals,
            'inputs': {'sessionYamlDigest': fingerprint(canonical),
                       'sources': {sid: item['sha256'] for sid, item in descriptors.items()}}}


def parse_polished(raw, rows):
    """Read %% uid:start-end %% comments, including multiline speaker turns.

    Character offsets remain in original cleaned wording, not polished wording.
    Require complete ordered provenance; malformed comments cannot hide text.
    """
    lines = raw.splitlines()
    require('## Transcript' in lines, 'Missing polished transcript section')
    begin = lines.index('## Transcript') + 1
    comments = []
    for i in range(begin, len(lines)):
        if lines[i].startswith('%%'):
            match = re.fullmatch(r'%%\s+(u\d+:\d+-\d+(?:,\s*u\d+:\d+-\d+)*)\s+%%', lines[i])
            require(match, f'Malformed polished source comment at line {i + 1}')
            comments.append((i, re.findall(r'(u\d+):(\d+)-(\d+)', match[1])))
    require(comments, 'No polished UID comments')
    require(not any(line.strip() for line in lines[begin:comments[0][0]]), 'Unmapped polished text before first comment')
    ordered = list(rows)
    cursor, offset, turns = 0, 0, []
    for n, (line, spans) in enumerate(comments):
        stop = comments[n + 1][0] if n + 1 < len(comments) else len(lines)
        body = '\n'.join(lines[line + 1:stop]).strip()
        match = re.fullmatch(r'([^:\n]+):\s*(.+)', body, re.S)
        require(match, f'Missing speaker/text after polished comment at line {line + 1}')
        refs = []
        for uid, start, end in spans:
            start, end = int(start), int(end)
            require(cursor < len(ordered) and uid == ordered[cursor] and start == offset,
                    'Polished provenance has missing, repeated or out-of-order source coverage')
            require(start < end <= len(rows[uid]['text']), 'Invalid polished source offsets')
            refs.append({'uid': uid, 'start': start, 'end': end})
            offset = end
            if end == len(rows[uid]['text']):
                cursor, offset = cursor + 1, 0
        turns.append({'speaker': match[1], 'text': match[2], 'sources': refs,
                      'line': line + 1, 'endLine': stop})
    require(cursor == len(ordered) and offset == 0, 'Polished transcript has missing source coverage')
    return turns


def corrected_turns(rows, corrections):
    by_uid = {}
    for correction in corrections:
        require(correction.get('uid') in rows, 'Speaker correction has unknown UID')
        by_uid.setdefault(correction['uid'], []).append(correction)
    turns = []
    for uid, row in rows.items():
        text = row['text']
        changes = sorted(by_uid.get(uid, []), key=lambda c: c['start'])
        end = 0
        for change in changes:
            require(type(change.get('start')) is int and type(change.get('end')) is int and
                    end <= change['start'] < change['end'] <= len(text) and change.get('speaker'),
                    'Invalid or overlapping speaker corrections')
            end = change['end']
        bounds = sorted({0, len(text), *(x for c in changes for x in (c['start'], c['end']))})
        for start, end in zip(bounds, bounds[1:]):
            speaker = next((c['speaker'] for c in changes if c['start'] <= start and end <= c['end']),
                           row['speaker'].split('|')[-1].strip())
            turns.append({'speaker': speaker, 'text': text[start:end],
                          'sources': [{'uid': uid, 'start': start, 'end': end}],
                          'line': row['line'], 'endLine': row['line']})
    return turns


class BundleCatalog(SourceCatalog):
    def __init__(self, data, vault):
        self.bundle = load_bundle(vault, data['sessionYaml'])
        bundle = self.bundle
        cleaned = bundle['sources'][bundle['cleanedId']]
        for line in (Path(vault) / cleaned['path']).read_text().lstrip('\ufeff').splitlines():
            require(not line.strip() or re.match(r'^\[u\d+(?:\s*\|\s*.*?)?\]\s?.*$', line),
                    'Unmapped cleaned transcript text; repair its source format before extraction')
        super().__init__({'sources': [cleaned]}, vault)
        rows = self.rows[bundle['cleanedId']]
        self.raw_rows = copy.deepcopy(rows)
        sid = bundle['sourceId']
        source = bundle['sources'][sid]
        corrections = bundle['metadata'].get('transcriptProcessing', {}).get('speakerCorrections', [])
        clean_turns = corrected_turns(rows, corrections)
        if sid == POLISHED:
            self.turns = parse_polished((Path(vault) / source['path']).read_text(), rows)
            clean_by_uid = {}
            polished_by_uid = {}
            for turn in clean_turns:
                clean_by_uid.setdefault(turn['sources'][0]['uid'], []).append(turn)
            # Saved speaker overrides are functional data; ensure polish agrees.
            for turn in self.turns:
                for span in turn['sources']:
                    relevant = [t for t in clean_by_uid[span['uid']] if
                                t['sources'][0]['start'] < span['end'] and t['sources'][0]['end'] > span['start']]
                    require(all(t['speaker'] == turn['speaker'] for t in relevant),
                            'Polished speaker disagrees with YAML speaker corrections')
                    polished_by_uid.setdefault(span['uid'], []).append(turn)
            for uid, row in rows.items():
                relevant = polished_by_uid[uid]
                row['line'] = relevant[0]['line']
                row['endLine'] = relevant[-1]['endLine']
        else:
            self.turns = clean_turns
        self.rows = {sid: rows}
        self.sources = {sid: source}
        self.hashes = {sid: source['sha256']}
        self.metadata = bundle['metadata']
        self.inputs = bundle['inputs']

    def passage(self, locator):
        sid, start, end = self.bounds(locator)
        # A quote must include the full provenance of each contributing polished
        # turn. Do not assign a merged paragraph's words to a single original UID.
        if sid == POLISHED:
            return ' '.join(t['text'] for t in self.turns
                            if all(start <= self.rows[sid][s['uid']]['position'] <= end for s in t['sources']))
        return super().passage(locator)

    def compact(self):
        return '\n\n'.join('%% ' + ', '.join(f"{s['uid']}:{s['start']}-{s['end']}" for s in t['sources']) +
                           ' %%\n' + t['speaker'] + ': ' + t['text'] for t in self.turns) + '\n'

    def display_metadata(self):
        m = self.metadata
        # Read explicit resolved pages only; participant role mappings are not an
        # authoritative PC attendance list. Show those separately in the review.
        pcs = [p for p in (m.get('pcs') or []) if isinstance(p, str) and (self.vault / p).is_file()]
        return {'campaign': m['campaign'], 'session': m['sessionNumber'], 'realWorldDate': str(m['realWorldDate']),
                'dateStart': str(m['drStart']) if m.get('drStart') else None,
                'dateEnd': str(m['drEnd']) if m.get('drEnd') else None, 'pcs': pcs}

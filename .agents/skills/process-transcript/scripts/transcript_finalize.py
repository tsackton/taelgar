"""Retain transcript references and retire completed session-local processing files."""
from pathlib import Path
import re
import yaml
from transcript_core import WORK, VERSION, require, safe, sha, current_hash, atomic, encoded, read_json

PLAN = 'cleaned/transcript-finalization.json'
KEY = 'transcriptProcessing'
RETAINED = ('original', 'prepared', 'cleaned', 'polishedMarkdown')
DISPOSABLE = ('polishedJson', 'polishedHtml', 'entities', 'review')


def completion(root):
    """Locate completion in existing metadata, including explicitly named manifests."""
    matches = []
    for path in sorted({*root.rglob('*.yaml'), *root.rglob('*.yml')}):
        relative = path.relative_to(root).as_posix()
        if relative.startswith(WORK + '/'):
            continue
        data = safe(root, relative).read_bytes()
        if re.search(rb'^transcriptProcessing:', data, re.M):
            record = yaml.safe_load(data).get(KEY)
            if record:
                matches.append((relative, record))
    require(len(matches) <= 1, 'Multiple transcript completion records; select the intended session bundle')
    return matches[0] if matches else None


def completed_status(root, manifest, record, finalizing=False):
    require(record.get('version') == VERSION, 'Unsupported transcript completion record')
    changed = [item['path'] for item in record['artifacts'].values()
               if current_hash(safe(root, item['path'])) != item['sha256']]
    outcome = 'needs_finalization' if finalizing else 'changed_after_finalization' if changed else record['status']
    return {'bundle': str(root), 'status': outcome, 'finalized': not finalizing,
            'outputsCurrent': not changed, 'changedArtifacts': changed,
            'units': record['units'], 'issues': record['issues'],
            'pending': {'clean': [], 'polish': [], 'quality': []},
            'pendingMaterialIssues': 0, 'pendingMaterialGroups': 0,
            'artifacts': {**{k: v['path'] for k, v in record['artifacts'].items()}, 'sessionMetadata': manifest}}


def append_completion(data, record):
    """Append one field without reformatting existing metadata or comments."""
    text = data.decode('utf-8')
    metadata = yaml.safe_load(text)
    require(isinstance(metadata, dict) and KEY not in metadata, 'Session metadata already has transcript processing information')
    addition = yaml.safe_dump({KEY: record}, sort_keys=False, allow_unicode=True)
    end = re.search(r'^\.\.\.[ \t]*(?:#.*)?$', text, re.M)
    position = end.start() if end else len(text)
    result = text[:position].rstrip('\r\n') + '\n\n' + addition + text[position:]
    require(yaml.safe_load(result) == dict(metadata, **{KEY: record}), 'Cannot append completion to this metadata format')
    return result.encode('utf-8')


def replace_completion(data, record):
    """Replace only the owned completion field, preserving surrounding metadata."""
    text = data.decode('utf-8')
    metadata = yaml.safe_load(text)
    if KEY not in metadata:
        return append_completion(data, record)
    node = yaml.compose(text)
    matches = [(key, value) for key, value in node.value if key.value == KEY]
    require(len(matches) == 1, 'Duplicate transcript completion fields')
    key, value = matches[0]
    addition = yaml.safe_dump({KEY: record}, sort_keys=False, allow_unicode=True)
    owned = text[key.start_mark.index:value.end_mark.index].splitlines(keepends=True)
    trailing = ''
    while owned and (not owned[-1].strip() or owned[-1].lstrip().startswith('#')):
        trailing = owned.pop() + trailing
    result = text[:key.start_mark.index] + addition + trailing + text[value.end_mark.index:]
    require(yaml.safe_load(result) == dict(metadata, **{KEY: record}), 'Cannot replace completion without changing other metadata')
    return result.encode('utf-8')


def work_files(root):
    folder = safe(root, WORK)
    files, directories = {}, []
    if folder.exists():
        for path in [folder, *folder.rglob('*')]:
            relative = path.relative_to(root).as_posix()
            path = safe(root, relative)
            if path.is_dir():
                directories.append(relative)
            else:
                require(path.is_file(), f'Unexpected processing artifact: {relative}')
                files[relative] = current_hash(path)
    return files, directories


def begin(root, state, outcome, manifest, expected):
    """Caller has verified review/export readiness and holds the session lock."""
    a = state['artifacts']
    record = {'version': VERSION, 'status': outcome['status'], 'units': outcome['units'],
              'issues': outcome['issues'], 'artifacts': {
                  key: {'path': a[key], 'sha256': (state['outputHashes'][a[key]] if key == 'polishedMarkdown'
                                                 else expected[a[key]])} for key in RETAINED}}
    metadata = safe(root, manifest).read_bytes()
    after = append_completion(metadata, record)
    discard, directories = work_files(root)
    for key in DISPOSABLE:
        relative = a[key]
        digest = current_hash(safe(root, relative))
        if digest is not None:
            require(digest == state['outputHashes'].get(relative), f'Processing export changed: {relative}')
            discard[relative] = digest
    plan = {'version': VERSION, 'manifest': manifest, 'manifestBefore': sha(metadata),
            'manifestAfter': after.decode('utf-8'), 'record': record, 'discard': discard,
            'directories': directories, 'exports': [a[key] for key in DISPOSABLE]}
    validate_plan(root, plan)
    require(all(current_hash(safe(root, path)) == digest for path, digest in expected.items()),
            'Inputs changed while preparing finalization')
    atomic(root, PLAN, encoded(plan))
    return finish(root)


def validate_plan(root, plan):
    require(plan.get('version') == VERSION, 'Unsupported finalization plan')
    record = plan['record']
    require(set(record['artifacts']) == set(RETAINED), 'Incomplete permanent transcript references')
    keep = [plan['manifest'], PLAN, *[item['path'] for item in record['artifacts'].values()]]
    require(len(keep) == len(set(keep)), 'Permanent and processing paths overlap')
    for relative in keep:
        safe(root, relative)
        require(relative != WORK and not relative.startswith(WORK + '/'), 'A permanent reference is inside the processing folder')
    # Restrict retirement outside the work directory to the four known exports.
    md = record['artifacts']['polishedMarkdown']['path']
    require(md.endswith('-transcript.md'), 'Unexpected polished transcript filename')
    stem = md.removesuffix('-transcript.md')
    exports = {stem + suffix for suffix in ('-transcript.json', '-transcript.html', '-transcript-entities.json', '-transcript-review.md')}
    require(set(plan['exports']) == exports, 'Unexpected retirement export paths')
    require(not exports.intersection(keep), 'A permanent reference overlaps a disposable export')
    for relative in plan['discard']:
        safe(root, relative)
        require(relative not in keep and (relative.startswith(WORK + '/') or relative in exports),
                f'Unmanaged deletion target: {relative}')
    for relative in plan['directories']:
        safe(root, relative)
        require(relative == WORK or relative.startswith(WORK + '/'), 'Unmanaged processing directory')


def finish(root):
    """Resume an interrupted retirement; no historical archive survives success."""
    plan = read_json(safe(root, PLAN))
    validate_plan(root, plan)
    record = plan['record']
    result = completed_status(root, plan['manifest'], record, finalizing=True)
    require(not result['changedArtifacts'], 'Permanent transcript changed during finalization: ' + ', '.join(result['changedArtifacts']))
    manifest = safe(root, plan['manifest'])
    after = plan['manifestAfter'].encode('utf-8')
    require(yaml.safe_load(after).get(KEY) == record, 'Completion metadata differs from finalization plan')
    require(current_hash(manifest) in {plan['manifestBefore'], sha(after)}, 'Session metadata changed during finalization; reconcile it before retrying')
    current, directories = work_files(root)
    require(set(current).issubset(plan['discard']) and set(directories).issubset(plan['directories']),
            'New processing files appeared during finalization; reconcile them before retrying')
    # Check all targets before removing any, and again just before each removal.
    for relative, digest in plan['discard'].items():
        require(current_hash(safe(root, relative)) in {None, digest}, f'Processing file changed during finalization: {relative}')
    for relative, digest in plan['discard'].items():
        path = safe(root, relative)
        if path.exists():
            require(current_hash(path) == digest, f'Concurrent edit during finalization: {relative}')
            path.unlink()
    for relative in sorted(plan['directories'], key=lambda p: len(Path(p).parts), reverse=True):
        path = safe(root, relative)
        if path.exists():
            path.rmdir()
    require(current_hash(manifest) in {plan['manifestBefore'], sha(after)}, 'Session metadata changed during finalization')
    if current_hash(manifest) != sha(after):
        atomic(root, plan['manifest'], after)
    safe(root, PLAN).unlink()
    return completed_status(root, plan['manifest'], record)

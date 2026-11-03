"""Empty staging-note paths, name collisions, and exclusive file creation."""
import json
import yaml
import os
from pathlib import Path
import re
import unicodedata


def normalized(value):
    return unicodedata.normalize('NFC', str(value)).strip().casefold()


def campaign_config(bundle, sources):
    registry = sources.safe(bundle['vault'], '_scripts/session_note_campaigns.json')
    if not registry.is_file():
        return None
    campaigns = json.loads(registry.read_bytes()).get('campaigns', {})
    name = normalized(bundle['data'].get('campaign', ''))
    matches = [dict(c, registryKey=key) for key, c in campaigns.items() if name in
               {normalized(v) for v in [key, c.get('name'), c.get('code'), *c.get('aliases', [])]}]
    sources.require(len(matches) <= 1, 'Ambiguous campaign registry entry')
    return matches[0] if matches else None


def component(value, sources):
    sources.require(isinstance(value, str), 'Enter a note name')
    value = unicodedata.normalize('NFC', value).strip()
    sources.require(value and len(value) <= 180 and not re.search(r'[<>:"/\\|?*\x00-\x1f]', value)
                   and not value.startswith(('.', '_')) and not value.endswith(('.', ' ')),
                   'Use a plain name without slashes, reserved filename characters, or leading dots/underscores')
    sources.require(not re.fullmatch(r'(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', value, re.I),
                   'That name is reserved by Windows')
    return value


def folder(bundle, sources):
    config = campaign_config(bundle, sources) or {}
    campaign = component(config.get('name') or bundle['data'].get('campaign', ''), sources)
    names = [campaign, bundle['data'].get('campaign', ''), config.get('registryKey', ''),
             config.get('code', ''), config.get('sessionRoot', ''), *config.get('aliases', [])]
    words = lambda text: ' '.join(re.findall(r'\w+', normalized(text)))
    identities = [words(name) for name in names if name]
    base = sources.safe(bundle['vault'], 'Worldbuilding/Staging')
    existing = []
    if base.is_dir():
        for item in base.iterdir():
            if item.is_symlink() or item.resolve() != item.absolute():
                continue
            try:
                if component(item.name, sources) != item.name:
                    continue
            except ValueError:
                continue
            candidate = sources.safe(bundle['vault'], item.relative_to(bundle['vault']))
            if candidate.is_dir() and any(f' {words(item.name)} ' in f' {name} ' for name in identities):
                existing.append(item.name)
    exact = [name for name in existing if words(name) in identities]
    choices = exact or existing
    sources.require(len(choices) <= 1, 'Multiple staging folders match this campaign; resolve the folder choice before creating a note')
    return 'Worldbuilding/Staging/' + (choices[0] if choices else campaign)


def collisions(vault, name, sources, note_index=None):
    candidates, indexed_matches = [], []
    if note_index is not None:
        sources.require(isinstance(note_index, list), 'Invalid note index')
        for item in note_index:
            sources.object_fields(item, {'path'}, {'names'}, 'note index entry')
            relative = Path(item['path'])
            sources.require(not relative.is_absolute() and relative.as_posix() == item['path']
                           and '..' not in relative.parts and relative.suffix.lower() == '.md',
                           'Invalid indexed note path')
            if any(p.startswith('.') or p == 'node_modules' for p in relative.parts):
                continue
            # The host's metadata index already parsed cached frontmatter. No
            # content hashes or filesystem-wide reopen are needed for names.
            names = item.get('names')
            if names is not None:
                sources.require(isinstance(names, list) and all(isinstance(n, str) for n in names),
                               'Invalid indexed note names')
            if normalized(relative.stem) == normalized(name) or (names is not None and
                    any(normalized(n) == normalized(name) for n in names)):
                path = sources.safe(vault, item['path'])
                if path.is_file():
                    indexed_matches.append(path)
            elif names is None:
                path = sources.safe(vault, item['path'])
                if path.is_file():
                    candidates.append(path)
        if indexed_matches:
            return indexed_matches
    for directory, folders, files in (() if note_index is not None else os.walk(vault, followlinks=False)):
        parent = sources.safe(vault, os.path.relpath(directory, vault)) if directory != str(vault) else vault
        folders[:] = [f for f in folders if not f.startswith('.') and f != 'node_modules'
                      and (parent / f).resolve() == (parent / f).absolute()]
        for filename in files:
            if filename.lower().endswith('.md'):
                path = parent / filename
                if path.is_symlink() or path.resolve() != path.absolute():
                    continue
                candidates.append(path)
    matches = [p for p in candidates if normalized(p.stem) == normalized(name)]
    if matches:
        return matches
    for path in candidates:
        try:
            with path.open(encoding='utf-8') as stream:
                if stream.readline().strip() != '---':
                    continue
                lines, size, closed = [], 0, False
                for line in stream:
                    size += len(line)
                    if line.strip() in ('---', '...'):
                        closed = True
                        break
                    if size > 65536:
                        break
                    lines.append(line)
                if not closed:
                    continue
            data = yaml.safe_load(''.join(lines))
        except (UnicodeError, yaml.YAMLError):
            continue
        if not isinstance(data, dict):
            continue
        aliases = data.get('aliases', [])
        aliases = aliases if isinstance(aliases, list) else [aliases]
        if any(isinstance(value, str) and normalized(value) == normalized(name)
               for value in [data.get('name'), *aliases]):
            matches.append(path)
    return matches


def create(bundle, name, sources, note_index=None):
    if isinstance(name, str) and name.lower().endswith('.md'):
        name = name[:-3]
    name = component(name, sources)
    matches = collisions(bundle['vault'], name, sources, note_index)
    sources.require(not matches, 'A note with that name or alias already exists: ' +
                   ', '.join(p.relative_to(bundle['vault']).as_posix() for p in matches[:8]))
    relative = folder(bundle, sources) + '/' + name + '.md'
    target = sources.safe(bundle['vault'], relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    target = sources.safe(bundle['vault'], relative)
    descriptor = sources.open_no_follow(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    os.close(descriptor)
    return relative

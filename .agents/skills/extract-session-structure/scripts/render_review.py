#!/usr/bin/env python3
"""Render an editorial review against the six extraction products for a session."""
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'map-transcript-scenes/scripts'))
import scene_map
from transcript_core import atomic, current_hash, lock, parse_units, safe, seconds

VAULT = scene_map.VAULT

WATCHES = {'dawn', 'morning', 'midday', 'afternoon', 'dusk', 'midnight'}
CLASSES = ['gameplay', 'combat', 'meta_discussion', 'table_talk', 'session_framing']
VERSIONS = {'time-markers': '0.5-time-markers-draft', 'location-markers': '0.4-location-markers-draft',
            'entity-map': 4, 'interactions': 1, 'combat': '0.1-combat-draft',
            'segments': '0.1-transcript-segments-draft'}
OUTPUTS = ('time-watches.json', 'structured-data-review.md')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_sources(manifest, input_dir, time_path):
    bundle = scene_map.load(manifest, allow_unknown_dates=True)
    stem = manifest.name.removesuffix('-session.yaml')
    paths = {key: input_dir / f'{stem}-{key}.json' for key in VERSIONS}
    if time_path is not None:
        paths['time-markers'] = time_path
    sources = {}
    fingerprints = {}
    for key, path in paths.items():
        require(path.is_relative_to(VAULT), f'{key} must be inside the vault: {path}')
        require(path.is_file(), f'Missing {key}: {path}')
        raw = path.read_bytes()
        sources[key] = json.loads(raw)
        require(sources[key].get('schemaVersion') == VERSIONS[key],
                f'Unsupported {key} version in {path.name}. Expected {VERSIONS[key]}.')
        fingerprints[key] = {'path': path.relative_to(VAULT).as_posix(),
                             'sha256': hashlib.sha256(raw).hexdigest()}

    def check_binding(binding, key):
        expected = fingerprints[key]
        require(all(binding[k] == v for k, v in expected.items()),
                f'A dependency refers to a different {key} file or revision')

    expected = {'sessionId': stem, 'sessionYaml': bundle['sessionYaml'],
                'sessionYamlSha256': bundle['fingerprints'][str(manifest.relative_to(bundle['root']))],
                'transcriptPath': bundle['source'].relative_to(VAULT).as_posix(),
                'transcriptSha256': bundle['sourceSha256']}
    for key in ('time-markers', 'location-markers', 'combat', 'segments'):
        binding = sources[key]['provenance']
        require(all(binding[k] == v for k, v in expected.items()), f'Stale source for {key}')
    for key in ('interactions', 'entity-map'):
        require(sources[key]['sessionYaml'] == bundle['sessionYaml'], f'Wrong session for {key}')
    require(sources['entity-map']['inputs']['sessionInputs'] == bundle['inputs'], 'Stale entity inputs')
    require(sources['interactions']['inputs']['transcript']['sha256'] == bundle['sourceSha256'],
            'Stale transcript in interactions')
    check_binding(sources['interactions']['inputs']['entityMap'], 'entity-map')
    check_binding(sources['combat']['provenance']['segments'], 'segments')
    if 'timeMarkers' in sources['location-markers']['provenance']:
        check_binding(sources['location-markers']['provenance']['timeMarkers'], 'time-markers')
    return bundle, paths, sources, fingerprints


def speaking_time(bundle, segments):
    artifact = bundle['data']['transcriptProcessing']['artifacts'].get('cleaned')
    if not artifact:
        return None, 0
    raw = (bundle['root'] / artifact['path']).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == bundle['fingerprints'][artifact['path']],
            'Timed transcript changed during review')
    units = parse_units(raw.decode())
    totals = dict.fromkeys(CLASSES, 0)
    start_group = {g['startUid'] for g in bundle['groups']}
    end_group = {g['endUid'] for g in bundle['groups']}
    pos = bundle['positions']
    next_pos = 0
    intervals = []
    for segment in segments:
        category = segment['category']
        start, end = (segment['source'][k] for k in ('startUid', 'endUid'))
        require(category in totals and start in start_group and end in end_group,
                f"Invalid classification or boundary at {segment['id']}")
        require(pos[start] == next_pos and pos[end] >= next_pos,
                f"Segment gap or overlap at {segment['id']}")
        for unit in units[next_pos:pos[end] + 1]:
            begin, finish = (round(seconds(v) * 1000) for v in unit['timing'].split('-'))
            intervals.append((begin, finish))
            totals[category] += finish - begin
        next_pos = pos[end] + 1
    require(next_pos == len(units), 'Segments do not cover all timed speech')
    covered = 0
    prior_end = 0
    for begin, finish in sorted(intervals):
        covered += max(0, finish - max(begin, prior_end))
        prior_end = max(prior_end, finish)
    return totals, sum(totals.values()) - covered


def check_rows(edit, sources, bundle):
    def ids(key, field):
        return {entry['id'] for entry in sources[key][field]}

    all_times = ids('time-markers', 'markers')
    primary = []
    for row in edit['watches']:
        require(row['markers'] and row['summary'] and row['day'], 'Empty watch row')
        require(len(row['summary'].split()) <= 28, 'Condense watch evidence to the anchor or elapsed time')
        require(row['basis'] in {'stated', 'mixed', 'inferred', 'open'}, 'Invalid watch basis')
        require(all(row[k] in WATCHES | {None} for k in ('startWatch', 'endWatch')), 'Unknown watch')
        require(row.get('clock', 'adventure') in {'adventure', 'local'}, 'Unknown clock')
        for start, end in row.get('sourceRanges', []):
            scene_map.source_bounds(bundle, scene_map.source(start, end), 'Supplementary watch evidence')
        dates = [date.fromisoformat(row[k]) for k in ('startDate', 'endDate') if row.get(k)]
        require(dates == sorted(dates), 'Reversed civil date range')
        primary.extend(row['markers'])
    require(Counter(primary) == Counter({ident: 1 for ident in all_times}), 'Missing, extra, or repeated primary time marker')
    location_data = sources['location-markers']
    places = location_data['places']
    markers = {m['id']: m for m in location_data['markers']}
    require(set(edit.get('placeLabels', {})) <= places.keys(), 'Unknown place in short labels')
    for row in edit['locations']:
        require(row['markers'] and set(row['markers']) <= markers.keys(), 'Unknown or missing location reference')
        cited = [markers[ident] for ident in row['markers']]
        require(row['places'] and set(row['places']) <= places.keys(), 'Choose locations from the place dictionary')
        actors = {actor for m in cited for actor in m['actors']}
        require(row['actors'] and set(row['actors']) <= actors, 'Choose actors named in the cited markers')
        require(row['kind'] in {'presence', 'approach', 'observation'}, 'Unknown location row kind')
        if row['kind'] == 'observation':
            require(all(m['type'] == 'observation' for m in cited), 'Use observation markers for observed places')
            require(any(m['place'] in row['places'] for m in cited), 'Observed location needs a matching target')
            if row.get('from'):
                require(all(m.get('observerPlace') == row['from'] for m in cited), 'Observer position differs')
        else:
            played = [m for m in cited if m.get('context') in (None, 'flashback')]
            if row['kind'] == 'approach':
                require(len(row['places']) == 1 and any(m.get('to') == row['places'][0]
                        and m.get('completion') == 'underway' for m in played), 'Approach needs an underway marker')
            else:
                visited = {m['place'] for m in played if m['type'] == 'presence'}
                for m in played:
                    if m['type'] != 'movement' or m['completion'] in {'planned', 'canceled'}:
                        continue
                    visited.add(m.get('from'))
                    visited.update(stop.get('place') for stop in m.get('route', []))
                    if m.get('completion') == 'arrived':
                        visited.add(m.get('to'))
                require(set(row['places']) <= visited, 'Physical locations need matching presence or travel evidence')
    entities = ids('entity-map', 'entities')
    seen = set()
    for row in edit['entities']:
        members = set(row['ids'])
        require(members and members <= entities and not seen & members, 'Invalid entity references')
        seen.update(members)
    stars = {e['id'] for e in sources['entity-map']['entities'] if e['importance'] == 'star'}
    require(stars <= seen, 'Missing star in the cast summary')
    records = sources['combat']['combats']
    require([v['id'] for v in records] == [v['id'] for v in edit['combats']], 'Missing or extra encounter')
    for combat, row in zip(records, edit['combats']):
        require([r['round'] for r in combat['rounds']] == list(range(1, len(row['rounds']) + 1)),
                f"Round coverage differs in {combat['id']}")
        require(bool(combat.get('openingActions')) == bool(row.get('opening')), 'Opening action coverage differs')


def table(headers, rows):
    def cell(value):
        return str(value).replace('|', r'\|').replace('\n', ' ')
    return '\n'.join('| ' + ' | '.join(map(cell, row)) + ' |'
                     for row in [headers, ['---'] * len(headers), *rows])


def duration(ms):
    minutes, sec = divmod(round(ms / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours}:{minutes:02}:{sec:02}'


def watch_name(row):
    first, last = row['startWatch'], row['endWatch']
    if first == last:
        return (first or 'open').title()
    return f'{(first or "open").title()} → {last or "open"}'


def marker_ids(markers):
    # Compress only consecutive IDs that are actually present.
    groups = []
    for ident in markers:
        match = re.fullmatch(r'([a-z]+)(\d+)', ident)
        if groups:
            prev = groups[-1][-1]
            if match and prev.startswith(match[1]) and int(prev[len(match[1]):]) + 1 == int(match[2]):
                groups[-1].append(ident)
                continue
        groups.append([ident])
    return ', '.join(g[0] if len(g) == 1 else f'{g[0]}–{g[-1]}' for g in groups)


def render(bundle, paths, sources, edit, output, totals, overlap):
    def link(path, label):
        return f'[{label}]({quote(os.path.relpath(path, output))})'
    data = bundle['data']
    lines = [f"# {data['campaign']} · Session {data['sessionNumber']}", '## Review flags']
    limits = [f"{k} — {v['limitations']}" for k, v in sources.items() if v.get('limitations')]
    flags = edit['flags'] + limits
    if totals is None:
        flags.append('Speaking time is unavailable because the session has no registered timed transcript.')
    lines.append('\n'.join(f'- {f}' for f in flags) or 'No open issues identified in this review.')
    lines.extend(['## In-world time', edit['dates']])
    rows = []
    for row in edit['watches']:
        text = row['summary']
        if row.get('scope'):
            text = f"**{row['scope']}** · {text}"
        watch = watch_name(row)
        if row.get('clock') == 'local':
            watch += ' (local)'
        rows.append([row['day'], watch, '—' if row['basis'] == 'open' else row['basis'],
                     text, marker_ids(row['markers'])])
    lines.append(table(['Day', 'Watch', 'Basis', 'Time evidence', 'Markers'], rows)
                 if rows else 'No supported time markers.')
    lines.append('## Locations')
    labels = {key: place['label'] for key, place in sources['location-markers']['places'].items()}
    labels.update(edit.get('placeLabels', {}))
    visits, observations = [], []
    for row in edit['locations']:
        names_of_actors = ['Party' if actor == 'party' else actor for actor in row['actors']]
        actors = ' and '.join(names_of_actors) if len(names_of_actors) == 2 else ', '.join(names_of_actors)
        names = [labels[place] for place in row['places']]
        refs = marker_ids(row['markers'])
        if row['kind'] == 'observation':
            if row.get('via'):
                actors += f" ({row['via']})"
            observations.append([' · '.join(names), actors, labels.get(row.get('from'), '—'), refs])
        else:
            location = ' → '.join(names)
            if row['kind'] == 'approach':
                location = 'Approach to ' + location
            visits.append([location, actors, refs])
    if visits:
        lines.append(table(['Location', 'Present', 'Markers'], visits))
    if observations:
        lines.append(table(['Observed location', 'Observer', 'From', 'Markers'], observations))
    if not visits and not observations:
        lines.append('No location markers.')
    entity_map = {e['id']: e for e in sources['entity-map']['entities']}
    kinds = Counter(e['importance'] for e in entity_map.values())
    lines.extend(['## Entities',
                  f"Stars {kinds['star']} · Supporting {kinds['supporting']} · Cameos {kinds['cameo']}"])
    rows = []
    for row in edit['entities']:
        members = [entity_map[ident] for ident in row['ids']]
        rows.append([', '.join(e['label'] for e in members), row['summary'], marker_ids(row['ids'])])
    if rows:
        lines.append(table(['Entity', 'Role in this session', 'IDs'], rows))
    lines.append('## Combat')
    if not edit['combats']:
        lines.append('No classified combat encounters.')
    for combat, row in zip(sources['combat']['combats'], edit['combats']):
        lines.append(f"### {combat['encounter']}")
        if row.get('opening'):
            lines.append(row['opening'])
        lines.append(table(['Round', 'What happened'], list(enumerate(row['rounds'], 1))))
        lines.append(row['ending'])
    lines.append('## Speaking time')
    if totals is None:
        lines.append('No timed utterance data available.')
    else:
        total = sum(totals.values())
        lines.extend([table(['Segment class', 'Speaking time (h:mm:ss)', 'Share'],
                      [[key.replace('_', ' ').capitalize(), duration(value),
                        f'{100 * value / total:.1f}%' if total else '—'] for key, value in totals.items()]
                      + [['**Total**', duration(total), '100%' if total else '—']]),
                      'Timed transcript utterances, counted once per source ID. Gaps between utterances are excluded.'])
        if overlap:
            lines.append(f'Utterances overlap for {overlap / 1000:.1f} seconds of cumulative speech beyond elapsed recording time.')
    lines.append('Sources · ' + ' · '.join([link(bundle['source'], 'Transcript'),
                 *[link(paths[k], k.replace('-', ' ').title()) for k in VERSIONS], '[Watch data](time-watches.json)']))
    return '\n\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path, help='Registered session YAML')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--prepare', action='store_true', help='Print an editorial draft bound to current inputs and outputs')
    mode.add_argument('--editorial', type=Path, help='Render a completed draft from --prepare')
    parser.add_argument('--input-dir', type=Path, help='Alternate directory of same-session extractions')
    parser.add_argument('--time-markers', type=Path, help='Select a separately produced time extraction')
    parser.add_argument('--output-dir', type=Path, help='Destination for isolated reviews')
    args = parser.parse_args()
    manifest = args.manifest.resolve()
    input_dir = (args.input_dir or manifest.parent).resolve()
    time_path = args.time_markers.resolve() if args.time_markers else None
    output = (args.output_dir or manifest.parent).resolve()
    if input_dir != manifest.parent or time_path and time_path != manifest.with_name(
            manifest.name.replace('-session.yaml', '-time-markers.json')):
        require(output != manifest.parent, 'Select a separate --output-dir for alternate extraction inputs')
    require(output == manifest.parent or not list(output.glob('*-session.yaml')),
            'Another registered session cannot be the output directory')
    bundle, paths, sources, fingerprints = read_sources(manifest, input_dir, time_path)

    with lock(bundle['root']):
        scene_map.check_inputs(bundle)
        for key, path in paths.items():
            require(file_hash(path) == fingerprints[key]['sha256'], f'{key} changed during review')
        previous = {name: current_hash(safe(output, name)) for name in OUTPUTS}
        if args.prepare:
            draft = dict(inputs=fingerprints, previous=previous, dates='', flags=[], watches=[],
                         locations=[], entities=[], combats=[])
            print(json.dumps(draft, ensure_ascii=False, indent=2))
            return
        edit = json.loads(args.editorial.read_bytes())
        require(edit.get('inputs') == fingerprints, 'Review inputs changed. Inspect them and prepare a new draft.')
        check_rows(edit, sources, bundle)
        totals, overlap = speaking_time(bundle, sources['segments']['segments'])
        watches = {'schemaVersion': '0.1-time-watches', 'sessionYaml': bundle['sessionYaml'],
                   'source': fingerprints['time-markers'],
                   'transcript': {'path': bundle['source'].relative_to(VAULT).as_posix(),
                                  'sha256': bundle['sourceSha256']},
                   'dateAssessment': edit['dates'], 'watches': edit['watches']}
        products = {'time-watches.json': scene_map.encoded(watches),
                    'structured-data-review.md': render(bundle, paths, sources, edit, output, totals, overlap).encode()}
        expected = edit.get('previous', {})
        require(expected.keys() == previous.keys(), 'Missing previous output snapshot')
        changed = []
        for name, data in products.items():
            if previous[name] == hashlib.sha256(data).hexdigest():
                continue  # Already applied, including a retry after an interrupted write.
            require(previous[name] == expected[name], f'{name} changed. Inspect it before regenerating the review.')
            changed.append(name)
        for name in changed:
            atomic(output, name, products[name])


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        sys.exit(f'Review could not be built: {error}')

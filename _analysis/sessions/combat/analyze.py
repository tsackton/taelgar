#!/usr/bin/env python3
"""Build reproducible combat tables, descriptive summaries, and figures.

Requires PyYAML and matplotlib. Run with --check to verify the text products
without writing files. Session artifacts are always read-only inputs.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date, timedelta
import hashlib
import io
import json
import os
from pathlib import Path
import statistics
import sys
import tempfile
from urllib.parse import quote

import yaml

sys.dont_write_bytecode = True
OUTPUT = Path(__file__).resolve().parent
VAULT = OUTPUT.parents[2]
sys.path.insert(0, str(VAULT / '.agents/skills/extract-session-structure/scripts'))
import render_review as review


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return path.resolve().relative_to(VAULT).as_posix()


def link(path, label=None):
    path = Path(path)
    target = os.path.relpath(path, OUTPUT)
    return f'[{label or path.name}]({quote(target)})'


def minutes(milliseconds):
    return round(milliseconds / 60_000, 6)


def session_level(config, number, positions=None, uid=None, at_end=False):
    override = config.get('session_overrides', {}).get(number)
    if override:
        return override['level']
    level = config['initial']
    for milestone in config.get('milestones', []):
        milestone_session = milestone['session']
        if milestone_session > number:
            break
        if milestone_session < number or at_end:
            level = milestone['level']
            continue
        if milestone.get('boundary') == 'start':
            level = milestone['level']
        elif uid and 'from_uid' in milestone:
            require(milestone['from_uid'] in positions,
                    f'Unknown advancement UID for session {number}')
            if positions[uid] >= positions[milestone['from_uid']]:
                level = milestone['level']
    return level


def format_for_session(campaign, number, manifest, data, metadata):
    rules = metadata['play_formats'].get(campaign, {})
    for gathering in rules.get('in_person', []):
        if number in gathering['sessions']:
            return 'in person', gathering['gathering'], rules['source']
    override = rules.get('overrides', {}).get(number)
    if override:
        return override['format'], '', override['evidence']

    # Source paths may refer to archived locations that no longer exist.
    # The recorded path remains evidence of how the recording was acquired.
    config_path = Path(data['sourceConfigPath'])
    config = yaml.safe_load(config_path.read_text()) if config_path.is_file() else {}
    paths = [str(config.get('sourcePath', '')), str(data.get('sourceAudioPath', '')),
             str(data.get('sourceInputPath', ''))]
    for source_path in paths:
        if '/zoom/' in source_path.lower() or Path(source_path).name.startswith('GMT'):
            return 'Zoom', '', source_path
    original = data.get('transcriptProcessing', {}).get('artifacts', {}).get('original')
    if original and Path(original['path']).name.startswith('GMT'):
        return 'Zoom', '', original['path']
    return 'unknown', '', relative(manifest)


def validate_binding(document, manifest, transcript, session_id):
    provenance = document['provenance']
    expected = {
        'sessionId': session_id,
        'sessionYaml': relative(manifest),
        'sessionYamlSha256': sha(manifest),
        'transcriptPath': relative(transcript),
        'transcriptSha256': sha(transcript),
    }
    for field, value in expected.items():
        require(provenance[field] == value, f'Stale {field} in {session_id}')


def timing_blocks(bundle, segments):
    artifacts = bundle['data']['transcriptProcessing']['artifacts']
    artifact = artifacts.get('cleaned') or artifacts['prepared']
    path = bundle['root'] / artifact['path']
    units = review.parse_units(path.read_text())
    bounds = [tuple(round(review.seconds(value) * 1000)
                    for value in unit['timing'].split('-')) for unit in units]
    blocks = []
    for segment in segments:
        start, end = (bundle['positions'][segment['source'][field]]
                      for field in ('startUid', 'endUid'))
        selected = bounds[start:end + 1]
        blocks.append((segment['id'], min(begin for begin, _ in selected),
                       max(finish for _, finish in selected)))
    return blocks, path


def collect(metadata):
    registry_path = VAULT / '_scripts/session_note_campaigns.json'
    registry = json.loads(registry_path.read_text())['campaigns']
    sessions, encounters = [], []
    roster_path = OUTPUT / 'enemy-rosters.yaml'
    roster_data = yaml.safe_load(roster_path.read_text())
    require(roster_data['schema_version'] == 1, 'Unsupported enemy-roster schema')
    rosters = roster_data['rosters']
    fingerprints = {relative(registry_path): sha(registry_path)}
    fingerprints[relative(OUTPUT / 'metadata.yaml')] = sha(OUTPUT / 'metadata.yaml')
    fingerprints[relative(roster_path)] = sha(roster_path)
    for module in (review, review.scene_map, review.scene_map.draft):
        module_path = Path(module.__file__)
        fingerprints[relative(module_path)] = sha(module_path)

    for campaign in metadata['campaign_keys']:
        identity = registry[campaign]
        root = VAULT / '_sessions' / identity['sessionRoot']
        for manifest in sorted(root.glob('*/cleaned/*-session.yaml')):
            data = yaml.safe_load(manifest.read_text())
            session_id = manifest.name.removesuffix('-session.yaml')
            number = data['sessionNumber']
            config = metadata['levels'][campaign]
            format_name, gathering, format_evidence = format_for_session(
                campaign, number, manifest, data, metadata)
            roster = [person['gameRole'] for person in data.get('participants', [])
                      if person.get('gameRole') and person['gameRole'] != 'DM']
            segment_path = manifest.with_name(f'{session_id}-segments.json')
            combat_path = manifest.with_name(f'{session_id}-combat.json')
            row = dict(
                campaign_key=campaign, campaign=identity['name'], session_id=session_id,
                session_number=number, real_world_date=str(data['realWorldDate']),
                source_type=data['sourceType'], play_format=format_name,
                gathering=gathering, play_format_evidence=format_evidence,
                listed_player_count=len(roster),
                split_adventure=number in config.get('split_sessions', []),
                level_at_start=session_level(config, number),
                level_at_end=session_level(config, number, at_end=True),
                extraction_status='unavailable', recording_minutes=None,
                classified_minutes=None, gameplay_minutes=None, combat_minutes=None,
                meta_discussion_minutes=None, table_talk_minutes=None,
                framing_minutes=None, unassigned_gap_minutes=None,
                combat_share_recording_pct=None, combat_share_classified_pct=None,
                recorded_combats=None, recorded_rounds=None, speed_sample_combats=None,
                source_limitations=metadata.get('session_qualifications', {}).get(session_id, ''),
                session_yaml=relative(manifest), session_yaml_sha256=sha(manifest),
                segments_path='', segments_sha256='', combat_path='', combat_sha256='',
                timed_transcript_path='', timed_transcript_sha256='',
                polished_transcript_path='', polished_transcript_sha256='',
            )
            fingerprints[relative(manifest)] = sha(manifest)
            config_path = Path(data['sourceConfigPath'])
            if config_path.is_file() and config_path.is_relative_to(VAULT):
                fingerprints[relative(config_path)] = sha(config_path)
            if not segment_path.is_file() or not combat_path.is_file():
                row['source_limitations'] = ' '.join(filter(None, [row['source_limitations'],
                    'No complete timed segment/combat pair. Combat count and time are unavailable.']))
                sessions.append(row)
                continue

            bundle = review.scene_map.load(manifest, allow_unknown_dates=True)
            segments = json.loads(segment_path.read_text())
            combats = json.loads(combat_path.read_text())
            require(segments['schemaVersion'] in review.SEGMENT_CLASSES,
                    f'Unsupported segments in {session_id}')
            require(combats['schemaVersion'] == '0.1-combat-draft',
                    f'Unsupported combats in {session_id}')
            for document in (segments, combats):
                validate_binding(document, manifest, bundle['source'], session_id)
            require(combats['provenance']['segments']['sha256'] == sha(segment_path),
                    f'Combat refers to a different classification in {session_id}')
            require(combats['provenance']['segments']['path'] == relative(segment_path),
                    f'Wrong classification path in {session_id}')
            require(combats['provenance']['segments']['schemaVersion'] == segments['schemaVersion'],
                    f'Wrong classification version in {session_id}')
            segment_lookup = {item['id']: item for item in segments['segments']}
            require(len(segment_lookup) == len(segments['segments']),
                    f'Duplicate segment IDs in {session_id}')
            combat_ids = [item['segmentId'] for item in combats['combats']]
            require(combat_ids == [item['id'] for item in segments['segments']
                                   if item['category'] == 'combat'],
                    f'Combat coverage differs from classification in {session_id}')
            timing = review.recording_time(bundle, segments['segments'], segments['schemaVersion'])
            require(timing['recording'] is not None, f'Unusable timing in {session_id}')
            blocks, timed_path = timing_blocks(bundle, segments['segments'])
            allocated = review.exclusive_time(blocks, [ident for ident, _, _ in blocks])
            row.update(
                extraction_status='recorded_source_complete',
                recording_minutes=minutes(timing['recording']),
                classified_minutes=minutes(sum(timing['elapsed'].values())),
                gameplay_minutes=minutes(sum(timing['elapsed'].get(category, 0)
                    for category in ('gameplay', 'exploration', 'social_interaction', 'planning'))),
                combat_minutes=minutes(timing['elapsed']['combat']),
                meta_discussion_minutes=minutes(timing['elapsed']['meta_discussion']),
                table_talk_minutes=minutes(timing['elapsed']['table_talk']),
                framing_minutes=minutes(timing['elapsed']['session_framing']),
                unassigned_gap_minutes=minutes(timing['recording'] - sum(timing['elapsed'].values())),
                combat_share_recording_pct=round(100 * timing['elapsed']['combat'] / timing['recording'], 6),
                combat_share_classified_pct=round(100 * timing['elapsed']['combat'] /
                                                  sum(timing['elapsed'].values()), 6),
                recorded_combats=len(combats['combats']),
                recorded_rounds=sum(len(item['rounds']) for item in combats['combats']),
                speed_sample_combats=0,
                segments_path=relative(segment_path), segments_sha256=sha(segment_path),
                combat_path=relative(combat_path), combat_sha256=sha(combat_path),
                timed_transcript_path=relative(timed_path), timed_transcript_sha256=sha(timed_path),
                polished_transcript_path=relative(bundle['source']),
                polished_transcript_sha256=sha(bundle['source']),
            )
            limitations = list(dict.fromkeys(filter(None, [row['source_limitations'],
                segments.get('limitations'), combats.get('limitations')])))
            row['source_limitations'] = ' '.join(limitations)
            if segments.get('limitations') or combats.get('limitations'):
                row['extraction_status'] = 'known_recording_omission'
            for path in (segment_path, combat_path, timed_path, bundle['source']):
                fingerprints[relative(path)] = sha(path)

            encounter_total = 0
            for combat in combats['combats']:
                roster_key = f'{session_id}/{combat["id"]}'
                require(roster_key in rosters, f'Missing enemy roster: {roster_key}')
                enemy_roster = rosters[roster_key]
                record_hash = hashlib.sha256(json.dumps(combat, ensure_ascii=False,
                    sort_keys=True, separators=(',', ':')).encode()).hexdigest()
                require(enemy_roster['source_record_sha256'] == record_hash,
                        f'Combat record changed. Reinspect enemy roster: {roster_key}')
                require(enemy_roster['source_combat'] == relative(combat_path),
                        f'Enemy roster refers to a different source: {roster_key}')
                require(enemy_roster['enemies'] or enemy_roster.get('other_opposition'),
                        f'Empty enemy/opposition annotation: {roster_key}')
                require([item['round'] for item in combat['rounds']] ==
                        list(range(1, len(combat['rounds']) + 1)),
                        f'Nonconsecutive rounds in {session_id}/{combat["id"]}')
                segment = segment_lookup[combat['segmentId']]
                source = segment['source']
                level = session_level(config, number, bundle['positions'], source['startUid'])
                end_level = session_level(config, number, bundle['positions'], source['endUid'])
                require(level == end_level, f'Level changes inside {session_id}/{combat["id"]}')
                qualification = metadata['encounter_qualifications'].get(f'{session_id}/{combat["id"]}', {})
                elapsed = allocated[combat['segmentId']]
                encounter_total += elapsed
                rounds = len(combat['rounds'])
                actors = {entry['actor'] for cycle in combat['rounds']
                          for entry in cycle['entries'] if entry['kind'] == 'turn'}
                pc_actors = sorted(set(roster) & actors)
                include_speed = qualification.get('include_speed', True) and rounds > 0
                row['speed_sample_combats'] += include_speed
                note = ' '.join(filter(None, [qualification.get('reason'), combat.get('note'),
                                               segment.get('note')]))
                encounters.append(dict(
                    campaign_key=campaign, campaign=identity['name'], session_id=session_id,
                    session_number=number, real_world_date=row['real_world_date'],
                    encounter_id=combat['id'], segment_id=combat['segmentId'],
                    encounter=combat['encounter'], level=level, play_format=format_name,
                    enemy_list=' | '.join(enemy_roster['enemies']),
                    other_opposition=' | '.join(enemy_roster.get('other_opposition', [])),
                    enemy_roster_note=enemy_roster.get('note', ''),
                    enemy_source_record_sha256=record_hash,
                    gathering=gathering, listed_player_count=len(roster),
                    pc_regular_turn_count=len(pc_actors), pc_regular_turn_actors=' | '.join(pc_actors),
                    four_or_five_pcs=len(pc_actors) in (4, 5),
                    split_adventure=row['split_adventure'],
                    encounter_kind=qualification.get('kind', 'combat'),
                    include_in_speed_summary=include_speed,
                    elapsed_minutes=minutes(elapsed), recorded_rounds=rounds,
                    minutes_per_round=round(elapsed / 60_000 / rounds, 6) if rounds else None,
                    minutes_per_round_per_pc=round(elapsed / 60_000 / rounds / len(pc_actors), 6)
                        if rounds and pc_actors else None,
                    start_uid=source['startUid'], end_uid=source['endUid'],
                    qualification=note, ending=combat['ending']['summary'],
                    source_limitations=row['source_limitations'],
                    combat_path=relative(combat_path), combat_sha256=sha(combat_path),
                    segments_path=relative(segment_path), segments_sha256=sha(segment_path),
                    timed_transcript_path=relative(timed_path), timed_transcript_sha256=sha(timed_path),
                    polished_transcript_path=relative(bundle['source']),
                    polished_transcript_sha256=sha(bundle['source']),
                ))
            require(encounter_total == timing['elapsed']['combat'],
                    f'Encounter times do not add up in {session_id}')
            sessions.append(row)
    expected_rosters = {f'{row["session_id"]}/{row["encounter_id"]}' for row in encounters}
    require(set(rosters) == expected_rosters,
            f'Enemy-roster coverage differs from encounter table: {set(rosters) ^ expected_rosters}')
    return sessions, encounters, fingerprints


def csv_text(rows):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def summary(rows):
    if not rows:
        return None
    return dict(
        n=len(rows), sessions=len({row['session_id'] for row in rows}),
        minutes=statistics.median(row['elapsed_minutes'] for row in rows),
        rounds=statistics.median(row['recorded_rounds'] for row in rows),
        pace=statistics.median(row['minutes_per_round'] for row in rows),
        pooled=sum(row['elapsed_minutes'] for row in rows) /
               sum(row['recorded_rounds'] for row in rows),
    )


def summary_cells(rows):
    result = summary(rows)
    if result is None:
        return ['0', '0', '—', '—', '—', '—']
    return [str(result['n']), str(result['sessions']), f'{result["minutes"]:.1f}',
            f'{result["rounds"]:.1f}', f'{result["pace"]:.1f}', f'{result["pooled"]:.1f}']


def table(headers, rows):
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(headers) + ' |',
                      '| ' + ' | '.join(['---'] * len(headers)) + ' |'] +
                     ['| ' + ' | '.join(cell(value) for value in row) + ' |' for row in rows])


def combat_table(encounters, metadata):
    lines = ['---', 'tags: [meta, status/check/ai]', '---', '# Combat table with enemy rosters', '',
        f'{len(encounters)} recorded encounters across five campaigns. '
        'This includes solo and smaller-party encounters as well as the four-or-five-PC subset. '
        'Dragonets is excluded. Each session link opens the source combat extraction.', '',
        'Enemy lists are draft annotations derived from existing combat records. '
        'Names and descriptive forms follow the played source. Counts appear only where '
        'supported, and labels can overlap when the record uses several descriptions for one '
        'actor. A repeated enemy in successive encounters remains on each encounter row. '
        'Summoned enemies and minions are included. Allied NPCs, party summons and constructs '
        'are omitted from enemy lists. Changes of allegiance are explained in the roster notes.', '',
        'Time is total elapsed recording time, including internal pauses and discussion. '
        'The PC count includes roster characters with a recorded regular turn. The normalized column '
        'divides elapsed minutes by recorded rounds and that PC count. It is blank when no '
        'PC acts. Friendly duels, PC conflicts and environmental opposition are labeled '
        'explicitly. The observed fight and extended-action-cycle encounter remain in this '
        'full table and carry their existing qualifications in the analysis data.', '',
        f'The filterable data is in {link(OUTPUT / "encounters.csv")}. '
        f'Enemy annotations and source-record fingerprints are in '
        f'{link(OUTPUT / "enemy-rosters.yaml")}.', '',
        'Dunmari sessions 96, 107 and 135 and Mawar episode 1 lack timed combat extractions. '
        'Labyrinths session 2 has a known missing recording interval containing an additional '
        'fight. This table covers the surviving extracted encounters.', '']
    for campaign in metadata['campaign_keys']:
        rows = [row for row in encounters if row['campaign_key'] == campaign]
        name = 'Dunmari Frontier' if campaign == 'dunmar-frontier' else rows[0]['campaign']
        lines += [f'## {name}', '']
        cells = []
        for row in rows:
            total_seconds = round(row['elapsed_minutes'] * 60)
            hours, remainder = divmod(total_seconds, 3600)
            minute, second = divmod(remainder, 60)
            duration = f'{hours}:{minute:02}:{second:02}'
            source = link(VAULT / row['combat_path'],
                          f'{row["session_number"]} · {row["encounter_id"]}')
            opposition = row['enemy_list']
            if row['other_opposition']:
                other = f'Other opposition / objective: {row["other_opposition"]}'
                opposition = '<br>'.join(filter(None, [opposition, other]))
            normalized = row['minutes_per_round_per_pc']
            cells.append([source, row['encounter'], opposition.replace(' | ', '<br>'),
                          row['level'], row['pc_regular_turn_count'], duration,
                          row['recorded_rounds'], f'{normalized:.2f}' if normalized is not None else '—'])
        lines += [table(['Session / fight', 'Encounter', 'Enemies / opposition', 'Level', 'PCs',
                         'Elapsed', 'Rounds', 'Minutes/round/PC'], cells), '']
        notes = [row for row in rows if row['enemy_roster_note']]
        if notes:
            lines += ['### Roster notes', '']
            lines.extend(f'- Session {row["session_number"]} {row["encounter_id"]} · '
                         f'{row["enemy_roster_note"]}' for row in notes)
            lines.append('')
    return '\n'.join(lines)


def matched_groups(encounters, metadata):
    eligible = [row for row in encounters if row['campaign_key'] == 'dunmar-frontier'
                and row['include_in_speed_summary'] and not row['split_adventure']]
    results = []
    window = timedelta(days=metadata['matched_comparison']['days_either_side'])
    for gathering in metadata['play_formats']['dunmar-frontier']['in_person']:
        name = gathering['gathering']
        local = [row for row in eligible if row['gathering'] == name]
        if not local:
            continue
        first = min(date.fromisoformat(row['real_world_date']) for row in local)
        last = max(date.fromisoformat(row['real_world_date']) for row in local)
        strata = {(row['level'], row['pc_regular_turn_count']) for row in local}
        for level, count in sorted(strata):
            person = [row for row in local if row['level'] == level
                      and row['pc_regular_turn_count'] == count]
            zoom = [row for row in eligible if row['play_format'] == 'Zoom'
                    and row['level'] == level and row['pc_regular_turn_count'] == count
                    and first - window <= date.fromisoformat(row['real_world_date']) <= last + window]
            results.append((name, level, count, person, zoom))
    return results


def make_figures(sessions, encounters, matches):
    os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'taelgar-combat-matplotlib'))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'axes.titleweight': 'bold', 'figure.facecolor': 'white',
                         'axes.grid': True, 'grid.alpha': 0.16, 'savefig.dpi': 170})
    rng = np.random.default_rng(116)
    blue, orange = '#285e7d', '#c26d36'
    selected = [row for row in encounters if row['campaign_key'] == 'dunmar-frontier'
                and row['include_in_speed_summary']]

    def save(fig, name):
        fig.savefig(OUTPUT / 'figures' / name, bbox_inches='tight')
        plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(12, 3.7))
    for ax, field, label, bins in zip(axes,
            ['elapsed_minutes', 'recorded_rounds', 'minutes_per_round'],
            ['Minutes per encounter', 'Recorded rounds', 'Minutes per recorded round'],
            [18, np.arange(0.5, max(row['recorded_rounds'] for row in selected) + 1.5), 16]):
        values = [row[field] for row in selected]
        ax.hist(values, bins=bins, color=blue, alpha=0.85)
        ax.axvline(statistics.median(values), color=orange, linewidth=2,
                   label=f'Median {statistics.median(values):.1f}')
        ax.set(xlabel=label, ylabel='Encounters')
        ax.legend(frameon=False)
    fig.suptitle(f'Dunmari Frontier · {len(selected)} comparable recorded encounters')
    fig.tight_layout()
    save(fig, 'combat-distributions.png')

    fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    for ax, field, label in zip(axes,
            ['elapsed_minutes', 'recorded_rounds', 'minutes_per_round'],
            ['Minutes per encounter', 'Recorded rounds', 'Minutes per round']):
        for format_name, color in [('Zoom', blue), ('in person', orange)]:
            rows = [row for row in selected if row['play_format'] == format_name]
            ax.scatter([date.fromisoformat(row['real_world_date']) for row in rows],
                       [row[field] for row in rows], s=25, alpha=0.75, c=color, label=format_name)
        ax.set_ylabel(label)
        ax.set_ylim(bottom=0)
    axes[0].legend(frameon=False, loc='upper left')
    axes[0].set_title('Dunmari Frontier · encounters over time')
    axes[-1].xaxis.set_major_locator(mdates.YearLocator())
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    fig.tight_layout()
    save(fig, 'combat-over-time.png')

    fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    levels = sorted({row['level'] for row in selected})
    for ax, field, label in zip(axes,
            ['elapsed_minutes', 'recorded_rounds', 'minutes_per_round'],
            ['Minutes per encounter', 'Recorded rounds', 'Minutes per round']):
        for format_name, color in [('Zoom', blue), ('in person', orange)]:
            rows = [row for row in selected if row['play_format'] == format_name]
            x = np.array([row['level'] for row in rows], dtype=float) + rng.uniform(-0.18, 0.18, len(rows))
            ax.scatter(x, [row[field] for row in rows], c=color, s=23, alpha=0.65, label=format_name)
        ax.plot(levels, [statistics.median(row[field] for row in selected if row['level'] == level)
                        for level in levels], c='#333333', marker='_', markersize=12, linewidth=1.3,
                label='Level median')
        ax.set(ylabel=label, ylim=(0, None))
    counts = {level: sum(row['level'] == level for row in selected) for level in levels}
    axes[0].set_title('Dunmari Frontier · level and encounter timing')
    axes[0].legend(frameon=False, ncol=3)
    axes[-1].set_xticks(levels, [f'{level}\n(n={counts[level]})' for level in levels])
    axes[-1].set_xlabel('Encounter level · counts include the level-8 Riswynn adventure')
    fig.tight_layout()
    save(fig, 'combat-by-level.png')

    full_party = [row for row in selected if row['pc_regular_turn_count'] in (4, 5)]
    bands = [('1–4', 1, 4), ('5–10', 5, 10), ('11–16', 11, 16), ('17–20', 17, 20)]
    medians, pooled, labels = [], [], []
    band_rng = np.random.default_rng(2026)
    fig, ax = plt.subplots(figsize=(10, 5.7))
    for index, (label, low, high) in enumerate(bands):
        rows = [row for row in full_party if low <= row['level'] <= high]
        normalized = [row['elapsed_minutes'] / row['recorded_rounds'] /
                      row['pc_regular_turn_count'] for row in rows]
        medians.append(statistics.median(normalized))
        pooled.append(sum(row['elapsed_minutes'] for row in rows) /
                      sum(row['recorded_rounds'] * row['pc_regular_turn_count'] for row in rows))
        labels.append(f'Levels {label}\n{len(rows)} fights')
        ax.scatter(index + band_rng.uniform(-0.16, 0.16, len(rows)), normalized,
                   color='#81919a', alpha=0.45, s=26, edgecolors='none',
                   label='Individual fights' if index == 0 else None)
    x = np.arange(len(bands))
    ax.plot(x, medians, color=blue, marker='D', markersize=7, linewidth=2.2,
            label='Median encounter', zorder=4)
    ax.plot(x, pooled, color=orange, marker='s', markersize=6, linewidth=1.8,
            linestyle='--', label='Pooled across rounds × PCs', zorder=3)
    for index, value in enumerate(medians):
        ax.annotate(f'{value:.2f}', (index, value), xytext=(0, -19),
                    textcoords='offset points', ha='center', color=blue,
                    fontweight='bold', fontsize=11)
    fig.suptitle('Combat time per round per PC', fontsize=16, fontweight='bold', y=0.98)
    ax.set_title(f'Dunmari Frontier · {len(full_party)} fights with four or five PCs',
                 fontsize=11, fontweight='normal', pad=13)
    ax.set_xticks(x, labels)
    ax.set(xlabel='Character level band', ylabel='Elapsed minutes ÷ rounds ÷ PCs',
           ylim=(0, None), xlim=(-0.4, 3.4))
    ax.legend(frameon=False, loc='upper left')
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    save(fig, 'full-party-normalized-by-level.png')

    timed = [row for row in sessions if row['campaign_key'] == 'dunmar-frontier'
             and row['recording_minutes'] is not None]
    fig, axes = plt.subplots(2, 1, figsize=(12, 6.8), sharex=True)
    ordered = sorted(timed, key=lambda row: (row['real_world_date'], row['session_number']))
    for ax, field, label in zip(axes,
            ['recording_minutes', 'combat_share_recording_pct'],
            ['Recorded minutes', 'Recorded time in combat (%)']):
        for format_name, color in [('Zoom', blue), ('in person', orange)]:
            rows = [row for row in ordered if row['play_format'] == format_name]
            ax.scatter([date.fromisoformat(row['real_world_date']) for row in rows],
                       [row[field] for row in rows], c=color, s=23, alpha=0.65, label=format_name)
        # Nine-session centered median keeps the amount of play in each window explicit.
        medians = [statistics.median(row[field] for row in ordered[max(0, i-4):i+5])
                   for i in range(len(ordered))]
        ax.plot([date.fromisoformat(row['real_world_date']) for row in ordered], medians,
                c='#333333', linewidth=1.5, label='Centered 9-session median')
        ax.set(ylabel=label, ylim=(0, None))
    axes[0].set_title('Dunmari Frontier · recorded session length and combat share')
    axes[0].legend(frameon=False, ncol=3)
    axes[-1].xaxis.set_major_locator(mdates.YearLocator())
    axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    fig.tight_layout()
    save(fig, 'session-time.png')

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), gridspec_kw={'width_ratios': [1.4, 1]})
    campaign_order = ['dunmar-frontier', 'mawar-adventures', 'into-the-chasm',
                      'labyrinths-of-the-lost', 'lost-in-the-feywild']
    names = ['Dunmari Frontier', 'Mawar', 'Into the Chasm', 'Labyrinths', 'Lost in the Feywild']
    for y, (key, name) in enumerate(zip(campaign_order, names)):
        rows = [row for row in encounters if row['campaign_key'] == key
                and row['include_in_speed_summary']]
        axes[0].scatter([row['minutes_per_round'] for row in rows],
                        y + rng.uniform(-0.14, 0.14, len(rows)), color=blue, alpha=0.55, s=23)
        axes[0].scatter(statistics.median(row['minutes_per_round'] for row in rows),
                        y, marker='|', s=260, color=orange, zorder=5)
    axes[0].set_yticks(range(5), names)
    axes[0].invert_yaxis()
    axes[0].set(xlabel='Minutes per recorded round', title='Individual campaigns')
    for y, (name, level, count, person, zoom) in enumerate(matches):
        for rows, shift, color in [(person, -0.12, orange), (zoom, 0.12, blue)]:
            if rows:
                axes[1].scatter([row['minutes_per_round'] for row in rows],
                                y + shift + rng.uniform(-0.035, 0.035, len(rows)),
                                c=color, s=24, alpha=0.75)
    axes[1].set_yticks(range(len(matches)), [f'{name}\nL{level}, {count} PCs'
                                           for name, level, count, _, _ in matches])
    axes[1].invert_yaxis()
    axes[1].set(xlabel='Minutes per recorded round', title='Gatherings and nearby Zoom fights')
    axes[1].scatter([], [], c=orange, label='in person')
    axes[1].scatter([], [], c=blue, label='Zoom')
    axes[1].legend(frameon=False, loc='lower right')
    fig.tight_layout()
    save(fig, 'campaign-and-format.png')


def make_report(sessions, encounters, metadata, matches):
    eligible = [row for row in encounters if row['include_in_speed_summary']]
    dunmari = [row for row in eligible if row['campaign_key'] == 'dunmar-frontier']
    timed = [row for row in sessions if row['recording_minutes'] is not None]
    dsessions = [row for row in timed if row['campaign_key'] == 'dunmar-frontier']
    overall = summary(dunmari)
    pace_quartiles = statistics.quantiles([row['minutes_per_round'] for row in dunmari],
                                          n=4, method='inclusive')
    headers = ['Group', 'Fights', 'Sessions', 'Median minutes/fight', 'Median rounds',
               'Median minutes/round', 'Pooled minutes/round']
    lines = ['---', 'tags: [meta, status/check/ai]', '---', '# Initial combat analysis', '',
        f'Built from current session artifacts using metadata decisions dated {metadata["analysis_date"]}.', '',
        f'Dunmari Frontier has {len(dsessions)} timed sessions and '
        f'{sum(row["recorded_combats"] for row in dsessions)} recorded combat segments. '
        f'The comparable speed sample contains {len(dunmari)} encounters. '
        f'Its median encounter takes **{overall["minutes"]:.1f} minutes** across '
        f'**{overall["rounds"]:.1f} recorded rounds**. The median encounter averages '
        f'**{overall["pace"]:.1f} minutes per round**. Pooling all elapsed minutes and recorded '
        f'rounds gives **{overall["pooled"]:.1f} minutes per round**. The middle half of '
        f'encounters fall between {pace_quartiles[0]:.1f} and {pace_quartiles[2]:.1f} '
        'minutes per recorded round.', '',
        '## Coverage and definitions', '',
        f'The tables cover {len(sessions)} registered sessions in five campaigns, with '
        f'{len(timed)} timed sessions and {len(encounters)} recorded combat segments. '
        'Dragonets is excluded at the user’s request. A missing combat extraction has blank '
        'counts and times. A complete extraction with no combat has zero counts and combat time.', '',
        'A session’s recorded length is the extent from the earliest timestamp to the latest '
        'timestamp. Combat duration is elapsed time inside each classified combat segment, '
        'including setup, tactical discussion, rules, interruptions and internal pauses. '
        'Overlapping milliseconds belong to the earliest source block, following the existing '
        'review renderer. Gaps between segment blocks are reported separately. '
        '`combat_share_recording_pct` uses the recording extent as denominator. '
        '`combat_share_classified_pct` uses the sum of classified block durations.', '',
        'Rounds are the cycles recorded by the combat extractor. Final cycles can be partial, '
        'and narration sometimes compresses an ending. These measurements describe average '
        'time per recorded cycle. They do not locate or time individual round boundaries. '
        'The main speed summaries exclude the remotely watched fight and the colossus encounter '
        'with ten-minute action cycles in session 104. Both remain in encounter counts and '
        'session combat-time totals. Environmental challenges, brief standoffs, direct PC '
        'conflict, the compelled-PC intervention '
        'and the evacuation remain included and have explicit `encounter_kind` labels.', '',
        'All comparisons are descriptive. Level changes alongside real-world date, party '
        'composition, enemy design, rules and table experience. Encounters within a session or '
        'a gathering share conditions. No independent-sample significance test or causal '
        'level or format effect is asserted.', '',
        '## Campaign comparisons', '']
    coverage_rows = []
    summary_rows = []
    for key in metadata['campaign_keys']:
        ss = [row for row in sessions if row['campaign_key'] == key]
        ts = [row for row in ss if row['recording_minutes'] is not None]
        ee = [row for row in eligible if row['campaign_key'] == key]
        name = 'Dunmari Frontier' if key == 'dunmar-frontier' else ss[0]['campaign']
        combat_count = sum(row['recorded_combats'] for row in ts)
        combat_share = 100 * sum(row['combat_minutes'] for row in ts) / sum(row['recording_minutes'] for row in ts)
        coverage_rows.append([name, len(ss), len(ts), combat_count,
                              sum(row['recorded_combats'] == 0 for row in ts),
                              f'{statistics.median(row["recording_minutes"] for row in ts):.1f}',
                              f'{combat_share:.1f}%'])
        summary_rows.append([name] + summary_cells(ee))
    lines += [table(['Campaign', 'Registered', 'Timed', 'Recorded fights', 'Timed sessions without combat',
                     'Median recorded minutes', 'Pooled recorded combat share'], coverage_rows), '',
              table(headers, summary_rows), '',
        'The campaign rows retain differences in level, DM, party size and adventure premise. '
        'Into the Chasm and Lost in the Feywild have different DMs from the Dunmari, Mawar and '
        'Labyrinths games. Mawar and Into the Chasm are level 6 throughout. Labyrinths advances '
        'from level 2 to 3 during its first session. Lost in the Feywild is level 3. '
        'Labyrinths session 2 has an acknowledged recording omission containing an additional fight. '
        'Its totals and the campaign comparison describe surviving recorded play.', '',
        '![Campaign and gathering comparisons](figures/campaign-and-format.png)', '',
        '## Combat length, rounds and speed', '',
        '![Encounter distributions](figures/combat-distributions.png)', '',
        'The separate duration and round measurements help distinguish an encounter that takes '
        'more rounds from an encounter that spends longer on each round. Median minutes per '
        'round gives each encounter one observation. Pooled minutes per round weights the '
        'result by recorded rounds.', '',
        '## Level and elapsed campaign time', '',
        table(headers, [[f'Level {level}'] + summary_cells([row for row in dunmari if row['level'] == level])
                        for level in sorted({row['level'] for row in dunmari})]), '',
        '![Encounter timing by level](figures/combat-by-level.png)', '',
        '![Encounter timing across campaign dates](figures/combat-over-time.png)', '']
    bands = [('Levels 1–4', 1, 4), ('Levels 5–10', 5, 10),
             ('Levels 11–16', 11, 16), ('Levels 17–20', 17, 20)]
    lines += [table(headers, [[label] + summary_cells([row for row in dunmari if low <= row['level'] <= high])
                              for label, low, high in bands]), '']
    full_party = [row for row in dunmari if row['pc_regular_turn_count'] in (4, 5)]
    normalized_rows = []
    for label, low, high in bands:
        rows = [row for row in full_party if low <= row['level'] <= high]
        values = [row['elapsed_minutes'] / row['recorded_rounds'] /
                  row['pc_regular_turn_count'] for row in rows]
        pooled = sum(row['elapsed_minutes'] for row in rows) / sum(
            row['recorded_rounds'] * row['pc_regular_turn_count'] for row in rows)
        normalized_rows.append([label, len(rows), f'{statistics.median(values):.2f}', f'{pooled:.2f}'])
    lines += ['![Full-party combat normalized by rounds and PCs](figures/full-party-normalized-by-level.png)', '',
        table(['Level band, four or five PCs', 'Fights', 'Median minutes/round/PC',
               'Pooled minutes/round/PC'], normalized_rows), '',
        'The full-party graph includes four or five roster PCs taking recorded regular turns, '
        'including guest parties. Each gray point is one encounter’s elapsed minutes divided '
        'by its recorded rounds and PC count. The blue line gives each encounter equal weight. '
        'The dashed orange line divides total elapsed minutes by the sum of rounds × PCs. '
        'Elapsed time includes enemies, summons, discussion and pauses throughout the encounter.', '']
    early = summary([row for row in dunmari if row['level'] <= 4])
    late = summary([row for row in dunmari if row['level'] >= 17])
    lines += [f'Levels 1–4 have a median encounter duration of {early["minutes"]:.1f} minutes, '
              f'{early["rounds"]:.1f} rounds and {early["pace"]:.1f} minutes per round. '
              f'Levels 17–20 have corresponding medians of {late["minutes"]:.1f} minutes, '
              f'{late["rounds"]:.1f} rounds and {late["pace"]:.1f} minutes per round. '
              f'The ratio of median minutes per round is {late["pace"] / early["pace"]:.2f}. '
              'The figures show the within-level spread and the concentration of in-person '
              'play at particular levels. The median round count is three in both the lowest '
              'and highest bands. The level relationship has substantial variation, including '
              'a lower median pace in levels 17–20 than in levels 11–16. No timed level-19 '
              'combat is available in the current archive.', '']
    control_rows = []
    for label, low, high in bands:
        rows = [row for row in dunmari if low <= row['level'] <= high
                and row['play_format'] == 'Zoom' and row['pc_regular_turn_count'] == 4]
        result = summary(rows)
        control_rows.append([label, len(rows), f'{result["pace"]:.1f}' if result else '—'])
    lines += [table(['Level band, Zoom with four roster PCs taking turns', 'Fights',
                     'Median minutes/round'], control_rows), '',
        'Restricting to Zoom encounters with four roster PCs taking recorded turns produces '
        'a similar broad increase. This restriction accounts for two measured differences '
        'between encounters. Enemy composition, summons, objectives and incomplete or '
        'compressed turn reporting still vary.', '',
        'The level-8 group includes Riswynn and her level-8 guests in sessions 56 and 58. '
        'Other split-adventure PCs and guests are level 10. Session 49’s fight is level 8, '
        'following the user’s clarification about Kenzo’s early level-9 benefit. '
        'Session 2’s first fight is level 1 and its second is level 2. Session 116’s '
        'Fausto fight is level 15 and its Apollyon fight is level 16. '
        'The dated advancement list places level 15 after the Eldest in session 106. '
        'Session 107’s note repeats that milestone. The session 106 fight remains level 14.', '',
        '## In person and Zoom', '',
        table(headers, [[name] + summary_cells([row for row in dunmari if row['play_format'] == name])
                        for name in ['Zoom', 'in person']]), '',
        'The pooled format comparison combines different levels and party configurations. '
        'The following comparison uses Zoom fights within 180 days of each gathering, at '
        'the same level and with the same number of roster PCs explicitly taking regular '
        'turns. Split adventures are excluded. Counts of roster PCs taking turns are '
        'observations from action entries. They can omit PCs who do not take a recorded '
        'regular turn and exclude allied NPCs and summons.', '',
        table(['Gathering', 'Level', 'Roster PCs taking turns', 'In-person fights', 'Zoom fights',
               'In-person median min/round', 'Zoom median min/round', 'In-person / Zoom'],
              [[name, level, count, len(person), len(zoom),
                f'{summary(person)["pace"]:.1f}', f'{summary(zoom)["pace"]:.1f}' if zoom else '—',
                f'{summary(person)["pace"] / summary(zoom)["pace"]:.2f}' if zoom else '—']
               for name, level, count, person, zoom in matches]), '',
        'The level-9 Cape 2022 and level-20 Nantucket 2025 fights have no same-level Zoom '
        'comparison in this archive. Cape 2023 and Colorado 2024 supply the overlapping '
        'conditions. Treat each gathering as one shared playing context when interpreting '
        'the multiple encounters. The table reports every available matching stratum, '
        'including ones without a Zoom counterpart. The two matched four-PC strata have '
        'in-person medians about 9% and 18% above their Zoom comparison medians. Each Zoom '
        'comparison contains only two fights. This archive therefore supplies little '
        'precision for a general format effect.', '',
        '## Session totals and changes over time', '',
        '![Session length and combat share](figures/session-time.png)', '']
    year_rows = []
    for year in sorted({row['real_world_date'][:4] for row in dsessions}):
        ss = [row for row in dsessions if row['real_world_date'].startswith(year)]
        share = 100 * sum(row['combat_minutes'] for row in ss) / sum(row['recording_minutes'] for row in ss)
        ee = [row for row in dunmari if row['real_world_date'].startswith(year)]
        year_rows.append([year, len(ss), sum(row['recorded_combats'] for row in ss),
                          f'{statistics.median(row["recording_minutes"] for row in ss):.1f}',
                          f'{share:.1f}%', sum(row['recorded_combats'] == 0 for row in ss),
                          f'{summary(ee)["pace"]:.1f}' if ee else '—'])
    lines += [table(['Year', 'Timed sessions', 'Recorded fights', 'Median recorded minutes',
                     'Pooled combat share', 'Sessions without recorded combat',
                     'Median minutes/round'], year_rows), '',
        'Yearly median recorded session length stays between roughly 208 and 239 minutes. '
        'Combat share varies much more. In 2023, 14 of 23 timed sessions have no recorded '
        'combat and pooled combat share is 12.6%. In 2025, pooled combat share reaches 29.3%, '
        'including the long final gathering. These are differences in the recorded time '
        'budget across campaign phases.', '',
        'The plotted trend is a centered nine-session median, with shorter windows at the '
        'ends. Calendar-year summaries have unequal numbers and lengths of sessions. '
        'The short split adventures and long in-person gatherings remain visible in the '
        'individual-session points. A short timestamp extent alone cannot establish whether '
        'the recording covered the complete real-world meeting.', '',
        '## Qualifications and source checks', '',
        table(['Session / encounter', 'Treatment'],
              [[key, value['reason']] for key, value in metadata['encounter_qualifications'].items()]), '',
        'All present segment and combat inputs were checked against the current manifest and '
        'polished transcript hashes. The existing loader and recording-time implementation '
        'verify UID coverage, whole-turn boundaries and recording timestamps. Each encounter '
        'has a matching combat segment and consecutive recorded round numbers. The sum of '
        'encounter durations matches session combat time exactly before CSV rounding. '
        'Source hashes in both tables allow later analysis to identify changed inputs.', '',
        f'The initial source audit checked start and end passages for '
        f'{len(metadata["source_audit"]["reviewed_encounters"])} encounters, including the '
        'shortest exchanges, longest fights, largest minutes-per-round values and ordinary '
        'comparison cases. The brief PC strike and bandit intimidation are supported by '
        'initiative and resolved actions. The longest fight, Kadmos at the palace, continues '
        'until the explicit end of initiative. Large late-game fights retain continuous '
        'phases or an immediate rescue inside their existing boundaries. All 156 recording '
        'extents and combat totals also matched the current per-session reviews within one '
        'second of displayed rounding. This audit checks boundary plausibility and timing. '
        'It retains the existing round reconstruction.', '',
        'Dunmari sessions 96 and 107 have narrative sources, and session 135 has raw notes. '
        'Mawar episode 1 has a narrative source. Their missing timed extractions are retained '
        'as unavailable session rows. Session 135’s Impossible Tower battle therefore contributes '
        'no timed encounter to this report. Labyrinths session 2 carries its recording-omission '
        'qualification on both session and encounter rows.', '',
        'Session 116’s continuous timing repair was present before this analysis began. '
        'Its registered source offsets the second Zoom recording by 4:07:01.760. '
        'No additional offset is applied by this script.', '',
        '## Reproduce and inspect', '',
        'Run `python analyze.py` from this directory with PyYAML and matplotlib installed. '
        'Run `python analyze.py --check` to recompute and compare the CSV and report text '
        'without writing files. The script verifies that inputs remain unchanged during '
        'the calculation. Plotting uses a fixed jitter seed.', '',
        'The analysis uses the repository’s existing transcript loader and recording-time '
        'functions. Output columns preserve source paths and SHA-256 fingerprints. '
        'Level milestones, human clarifications, play-format evidence and encounter '
        'qualifications are maintained in `metadata.yaml`. Enemy rosters are draft '
        'analysis annotations in `enemy-rosters.yaml`, derived from the existing combat '
        'records with checks for allies, summons, changing sides and overlapping actor labels. '
        'Each annotation is bound to the exact semantic combat record. A changed record '
        'requires reinspection of its roster.', '',
        f'The full {link(OUTPUT / "combat-table.md", "combat table with enemy lists")} '
        'includes all recorded encounters, with PC count, elapsed time, rounds and '
        'minutes per round per PC. `four_or_five_pcs` in the CSV selects the subset used '
        'in the normalized full-party graph.', '',
        f'Inputs and outputs are available in {link(OUTPUT / "sessions.csv")}, '
        f'{link(OUTPUT / "encounters.csv")}, {link(OUTPUT / "metadata.yaml")} and '
        f'{link(OUTPUT / "analyze.py")}. The timing implementation is '
        f'{link(VAULT / ".agents/skills/extract-session-structure/scripts/render_review.py")}.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify existing text outputs without writing')
    args = parser.parse_args()
    metadata = yaml.safe_load((OUTPUT / 'metadata.yaml').read_text())
    sessions, encounters, fingerprints = collect(metadata)
    matches = matched_groups(encounters, metadata)
    products = {'sessions.csv': csv_text(sessions), 'encounters.csv': csv_text(encounters),
                'report.md': make_report(sessions, encounters, metadata, matches),
                'combat-table.md': combat_table(encounters, metadata)}
    for path, fingerprint in fingerprints.items():
        require(sha(VAULT / path) == fingerprint, f'Input changed during analysis: {path}')
    for name, text in products.items():
        path = OUTPUT / name
        if args.check:
            require(path.is_file() and path.read_text() == text, f'Outdated analysis output: {name}')
        else:
            path.write_text(text)
    if not args.check:
        (OUTPUT / 'figures').mkdir(exist_ok=True)
        make_figures(sessions, encounters, matches)
    print(f'{"Verified" if args.check else "Built"} {len(sessions)} session rows, '
          f'{len(encounters)} encounters and {len(fingerprints)} source fingerprints.')


if __name__ == '__main__':
    main()

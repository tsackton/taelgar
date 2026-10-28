#!/usr/bin/env python3
"""Validate a frozen interaction extraction and render its evidence for review."""
import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data, vault):
    def path_for(value):
        path = (vault / value).resolve()
        require(path.is_relative_to(vault.resolve()), f"Path outside vault: {value}")
        require(path.is_file(), f"Missing file: {value}")
        return path

    require(data['schema_version'] == 3, 'Unsupported schema version; v3 requires typed entities, typed scenes and quote lists')
    require(data['campaign'] and data['session'], 'Missing campaign/session')
    require(type(data['segmentation_revision']) is int and data['segmentation_revision'] > 0,
            'Invalid segmentation revision')
    require(data['source']['kind'] in {'transcript', 'notes'}, 'Invalid source kind')
    for source in [data['source'], *data['supporting_sources']]:
        require(hashlib.sha256(path_for(source['path']).read_bytes()).hexdigest() == source['sha256'],
                f"Source hash changed: {source['path']}")
    if data['source']['kind'] == 'notes':
        require(data['source']['original'] in data['supporting_sources'], 'Missing original notes evidence')
    rows = {}
    for line, text in enumerate(path_for(data['source']['path']).read_text().splitlines(), 1):
        match = re.match(r'^\[(u\d+)(?:\s*\|\s*(.*?))?\]\s?(.*)$', text)
        if match:
            uid, attribution, words = match.groups()
            require(uid not in rows, f'Duplicate source UID: {uid}')
            rows[uid] = {'line': line, 'attribution': attribution or '', 'text': words}
    require(rows, 'No source UIDs found')
    ids = list(rows)
    positions = {uid: index for index, uid in enumerate(ids)}

    def span(item):
        start, end = item['startUid'], item['endUid']
        require(start in positions and end in positions, f'Missing UID: {start}–{end}')
        a, b = positions[start], positions[end]
        require(a <= b, f'Reversed range: {start}–{end}')
        return ids[a:b + 1]

    scenes = {}
    covered = []
    last_end = -1
    for scene in data['scenes']:
        index = scene['index']
        require(type(index) is int and index == len(scenes) + 1, 'Scene indexes must be sequential integers')
        selected = span(scene)
        require(positions[selected[0]] > last_end, 'Scenes out of source order')
        last_end = positions[selected[-1]]
        covered.extend(selected)
        require(scene['boundary'] and scene['location'], f'Missing boundary/location: {index}')
        require(scene.get('type') in {'conversation', 'exploration', 'combat', 'travel'}, 'Invalid or missing scene type')
        day = scene['date']
        require(day['basis'] and day['evidence'], f'Missing date basis: {index}')
        require((day['start'] is None) == (day['end'] is None), 'Date bounds must both be known or unknown')
        if day['start'] is not None:
            require(date.fromisoformat(day['start']) <= date.fromisoformat(day['end']), 'Invalid date order')
        scenes[index] = scene
    for excluded in data['excluded_ranges']:
        require(excluded['reason'], 'Missing exclusion reason')
        covered.extend(span(excluded))
    require(len(covered) == len(set(covered)), 'Overlapping source coverage')
    require(set(covered) == set(ids), 'Incomplete source coverage')
    entities = {}
    for entity in data['entities']:
        require(entity['id'] not in entities, 'Duplicate entity ID')
        require(entity['label'] and entity['basis'], 'Missing entity label/eligibility basis')
        require(entity.get('kind') in {'npc', 'item'}, 'Invalid entity kind')
        eligible = {'named', 'individual'} if entity['kind'] == 'npc' else {'named', 'distinctive'}
        require(entity['eligibility'] in eligible, 'Invalid eligibility')
        if entity['note']:
            path_for(entity['note'])
        entities[entity['id']] = entity
    record_ids, introduced = set(), set()
    by_id, quote_owners = {}, {}
    def check_quote(quote, allowed, kinds):
        require(quote['kind'] in kinds, 'Invalid quote kind')
        require(set(span(quote)) <= allowed, 'Quote crosses interaction boundary')
        passage = ' '.join(rows[uid]['text'] for uid in span(quote))
        require(bool(quote['quote']) and quote['quote'] in passage, 'Quote is not verbatim source text')

    for record in data['interactions']:
        require(record['id'] not in record_ids, 'Duplicate record ID')
        record_ids.add(record['id'])
        by_id[record['id']] = record
        require(record['entity'] in entities, 'Broken entity join')
        require(record['scenes'] and record['scenes'] == sorted(set(record['scenes'])), 'Scene references must be ordered and unique')
        require(all(type(index) is int and index in scenes for index in record['scenes']), 'Broken scene join')
        require(record['interaction'] in {'interacted', 'observed', 'present', 'mentioned'}, 'Invalid interaction type')
        require(record['importance'] in {'star', 'supporting', 'cameo'}, 'Invalid importance')
        require(0 < len(record['overview'].split()) <= 35, 'Overview missing or longer than 35 words')
        require(not ({'location', 'date', 'other_npcs'} & record.keys()), 'Scene fields duplicated on record')
        require(record['transcript'], 'Missing complete interaction source bounds')
        scene_ids = set().union(*(set(span(scenes[index])) for index in record['scenes']))
        interaction_ids = []
        prior_end = -1
        for excerpt in record['transcript']:
            require(set(span(excerpt)) <= scene_ids, 'Excerpt crosses scene boundary')
            require(positions[excerpt['startUid']] > prior_end, 'Interaction source ranges overlap or are out of order')
            prior_end = positions[excerpt['endUid']]
            interaction_ids.extend(span(excerpt))
        interaction_ids = set(interaction_ids)
        require(all(interaction_ids & set(span(scenes[index])) for index in record['scenes']), 'Unrelated scene reference')
        if len(record['scenes']) > 1 or len(record['transcript']) > 1:
            require(record.get('continuity'), 'Missing encounter continuity explanation')
        if record['interaction'] == 'present':
            require(record.get('presence_basis'), 'Presence must be affirmatively evidenced')
        for excerpt in record.get('excerpts', []):
            require(set(span(excerpt)) <= interaction_ids, 'Highlight outside complete interaction bounds')
        require('npc' not in record and 'pull_quote' not in record, 'Legacy record fields in v3')
        for quote in record.get('quotes', []):
            require(quote.get('id') and quote['id'] not in quote_owners, 'Missing or duplicate quote ID')
            require(quote.get('attribution'), 'Missing quote attribution')
            entity = entities[record['entity']]
            if entity['kind'] == 'npc':
                require(quote.get('speaker') == record['entity'], 'Pull quote belongs to another NPC')
                kinds = {'dialogue', 'written'}
            else:
                kinds = {'description', 'dialogue', 'written'}
                if quote['kind'] == 'dialogue':
                    require(quote.get('speaker') and quote['speaker'] != record['entity'], 'Item dialogue must name the actual speaker')
                else:
                    require('speaker' in quote, 'Item source quote must explicitly identify speaker or use null')
            check_quote(quote, interaction_ids, kinds)
            quote_owners[quote['id']] = record['entity']
        if record.get('introduction'):
            intro = record['introduction']
            require(record['entity'] not in introduced, 'Repeated introduction for entity')
            introduced.add(record['entity'])
            check_quote(intro, scene_ids, {'description', 'dialogue'})
    require({record['entity'] for record in data['interactions']} == set(entities), 'Unused entity')
    for entity in entities.values():
        own = {record['id'] for record in data['interactions'] if record['entity'] == entity['id']}
        require(0 < len(entity['session_overview'].split()) <= 55, 'Missing or excessive session entity overview')
        require(set(entity['overview_records']) == own and len(entity['overview_records']) == len(own), 'Session overview must reference all and only this entity’s records')
        require(entity['quote_review'] in {'selected', 'no_suitable_dialogue', 'no_suitable_excerpt', 'uncertain_attribution', 'not_applicable'}, 'Missing quote review')
        featured = entity.get('featured_quote_ids', [])
        require(isinstance(featured, list) and len(featured) == len(set(featured)), 'Featured quotes must be unique IDs')
        require(all(quote_owners.get(q) == entity['id'] for q in featured), 'Featured quote must belong to this entity')
        has_quotes = any(by_id[r].get('quotes') for r in own)
        require((entity['quote_review'] == 'selected') == has_quotes, 'Quote review disagrees with selected quotes')
        require(bool(featured) == has_quotes, 'Select featured quotes for entities with quotes')
    # Prevent the same entity being accidentally indexed twice for an overlapping encounter.
    for entity in entities:
        occupied = set()
        for record in data['interactions']:
            if record['entity'] != entity:
                continue
            selected = set().union(*(set(span(item)) for item in record['transcript']))
            require(not occupied & selected, 'Overlapping duplicate entity interactions')
            occupied.update(selected)
    return rows, span


def render(data, vault, rows, span, excerpts=False):
    source_path = (vault / data['source']['path']).resolve()
    entities = {entity['id']: entity for entity in data['entities']}

    def link(item):
        a, b = item['startUid'], item['endUid']
        return f'[{a}–{b}](<{source_path}:{rows[a]["line"]}>)'

    counts = {kind: sum(e['kind'] == kind for e in entities.values()) for kind in ('npc', 'item')}
    out = [f'# {data["session"]}: campaign interaction extraction', '',
           f'{len(data["scenes"])} scenes · {counts["npc"]} NPCs · {counts["item"]} items · {len(data["interactions"])} records', '',
           f'Source: [{data["source"]["kind"]}](<{source_path}>) · segmentation revision {data["segmentation_revision"]}', '',
           '## Review notes', '']
    out.extend(f'- {note}' for note in data['review_notes'])
    out.extend(['', '## Scenes', '', '| Scene | Type | Location | Date/time | Source |', '| --- | --- | --- | --- | --- |'])
    for scene in data['scenes']:
        day = scene['date']
        when = day['start'] or 'unknown'
        if day['end'] != day['start']:
            when += f' to {day["end"]}'
        out.append(f'| {scene["index"]} | {scene["type"]} | {scene["location"]} | {when}; {day["time"] or "time unknown"} | {link(scene)} |')
    for entity in data['entities']:
        records = [record for record in data['interactions'] if record['entity'] == entity['id']]
        out.extend(['', f'## {entity["label"]} · {entity["kind"].upper()}', '', entity['session_overview'], ''])
        if entity['note']:
            out.extend([f'Identity: [{entity["canonical_name"]}](<{(vault / entity["note"]).resolve()}>)', ''])
        all_quotes = {q['id']: q for r in records for q in r.get('quotes', [])}
        featured = entity.get('featured_quote_ids', [])
        quote_label = 'Pull quote' if entity['kind'] == 'npc' else 'Source quote'
        def show_quote(quote):
            attribution = quote['attribution']
            out.extend([f'> {quote["quote"]}', '', f'{quote_label} ({quote["kind"]}): {link(quote)} — {attribution}', ''])
        for quote_id in featured:
            show_quote(all_quotes[quote_id])
        for record in records:
            label = ', '.join(str(index) for index in record['scenes'])
            out.extend([f'### Scenes {label} · {record["interaction"]} · {record["importance"]}', '', record['overview'], ''])
            if record.get('known_as'):
                out.extend([f'Known as: {record["known_as"]}', ''])
            for quote in record.get('quotes', []):
                if quote['id'] not in featured:
                    show_quote(quote)
            if excerpts and record.get('continuity'):
                out.extend([f'Continuity: {record["continuity"]}', ''])
            if excerpts and record.get('presence_basis'):
                out.extend([f'Presence evidence: {record["presence_basis"]}', ''])
            if record.get('introduction'):
                intro = record['introduction']
                out.extend([f'Introduction ({intro["kind"]}, {link(intro)}):', '', f'> {intro["quote"]}', ''])
            for excerpt in record['transcript']:
                out.extend([f'Complete interaction: {link(excerpt)}', ''])
            if record.get('excerpts'):
                out.extend(['Key passages: ' + ', '.join(link(item) for item in record['excerpts']), ''])
            if excerpts:
                for excerpt in record.get('excerpts', record['transcript']):
                    out.extend([f'Evidence excerpt: {link(excerpt)}', ''])
                    for uid in span(excerpt):
                        row = rows[uid]
                        out.append(f'> **{uid} {row["attribution"]}** {row["text"]}  ')
                    out.append('')
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--preview', type=Path)
    parser.add_argument('--excerpts', type=Path, help='Optional expanded evidence review with verbatim excerpts')
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    rows, span = validate(data, args.vault)
    if args.preview:
        args.preview.write_text(render(data, args.vault, rows, span))
    if args.excerpts:
        args.excerpts.write_text(render(data, args.vault, rows, span, excerpts=True))
    print(f'Validated {data["session"]}: {len(data["scenes"])} scenes, {len(data["entities"])} entities, {len(data["interactions"])} records')


if __name__ == '__main__':
    main()

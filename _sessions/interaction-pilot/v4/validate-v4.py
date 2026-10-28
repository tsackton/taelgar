#!/usr/bin/env python3
"""Validate a frozen interaction extraction and render its evidence for review."""
import argparse
import copy
import hashlib
import json
import re
from datetime import date
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def upgrade_v3(data):
    """Read historical v3 artifacts without rewriting them or their sources."""
    data = copy.deepcopy(data)
    if data['schema_version'] != 3:
        return data
    require(data['source']['kind'] == 'transcript', 'Regenerate legacy UID-marked notes using original note lines')
    data['schema_version'] = 4
    data['sources'] = [{**data.pop('source'), 'id': 'transcript'}]
    for scene in data['scenes']:
        scene['evidence'] = [{'source': 'transcript', 'startUid': scene.pop('startUid'), 'endUid': scene.pop('endUid')}]
    for item in data['excluded_ranges']:
        item['source'] = 'transcript'
    for record in data['interactions']:
        record['evidence'] = record.pop('transcript')
        for item in [*record['evidence'], *record.get('excerpts', []), *record.get('quotes', [])]:
            item['source'] = 'transcript'
        if record.get('introduction'):
            record['introduction']['source'] = 'transcript'
    return data


class Evidence:
    """Resolve source-qualified UID or exact note-text selectors against frozen files."""
    def __init__(self, sources, path_for):
        self.sources, self.rows, self.texts, self.lines, self.offsets = {}, {}, {}, {}, {}
        for source in sources:
            sid = source['id']
            require(sid and sid not in self.sources, 'Missing or duplicate source ID')
            require(source['kind'] in {'transcript', 'session_notes'}, 'Invalid source kind')
            self.sources[sid] = source
            text = path_for(source['path']).read_text()
            self.texts[sid] = text
            lines = text.splitlines(keepends=True)
            self.lines[sid] = lines
            offsets = [0]
            for line in lines:
                offsets.append(offsets[-1] + len(line))
            self.offsets[sid] = offsets
            rows = {}
            if source['kind'] == 'transcript':
                for line, text in enumerate(lines, 1):
                    match = re.match(r'^\[(u\d+)(?:\s*\|\s*(.*?))?\]\s?(.*)$', text.rstrip('\n'))
                    if match:
                        uid, attribution, words = match.groups()
                        require(uid not in rows, f'Duplicate source UID: {sid}:{uid}')
                        rows[uid] = {'line': line, 'attribution': attribution or '', 'text': words, 'position': len(rows)}
                require(rows, 'No source UIDs found')
            self.rows[sid] = rows

    def bounds(self, item):
        sid = item.get('source')
        require(sid in self.sources, 'Unknown evidence source')
        if self.sources[sid]['kind'] == 'transcript':
            require(not ({'startLine', 'endLine', 'text'} & item.keys()), 'Transcript range must use UIDs')
            rows = self.rows[sid]
            a, b = item.get('startUid'), item.get('endUid')
            require(a in rows and b in rows, f'Missing UID: {a}–{b}')
            start, end = rows[a]['position'], rows[b]['position'] + 1
            require(start < end, 'Reversed UID range')
            return sid, start, end
        require(not ({'startUid', 'endUid'} & item.keys()), 'Notes must use original lines, not fabricated UIDs')
        a, b = item.get('startLine'), item.get('endLine')
        require(type(a) is int and type(b) is int and 1 <= a <= b <= len(self.lines[sid]), 'Invalid note line range')
        text = item.get('text')
        passage = ''.join(self.lines[sid][a - 1:b])
        require(isinstance(text, str) and bool(text.strip()) and passage.count(text) == 1, 'Note selector must match exact, unambiguous source text')
        start = self.offsets[sid][a - 1] + passage.index(text)
        return sid, start, start + len(text)

    def span(self, item):
        sid, start, end = self.bounds(item)
        return {(sid, position) for position in range(start, end)}

    def passage(self, item):
        sid, start, end = self.bounds(item)
        if self.sources[sid]['kind'] == 'session_notes':
            return self.texts[sid][start:end]
        return ' '.join(row['text'] for row in list(self.rows[sid].values())[start:end])

    def is_transcript(self, item):
        require(item.get('source') in self.sources, 'Unknown evidence source')
        return self.sources[item['source']]['kind'] == 'transcript'


def validate(data, vault):
    data = upgrade_v3(data)
    def path_for(value):
        path = (vault / value).resolve()
        require(path.is_relative_to(vault.resolve()), f"Path outside vault: {value}")
        require(path.is_file(), f"Missing file: {value}")
        return path

    require(data['schema_version'] == 4, 'Unsupported schema version')
    require(data['campaign'] and data['session'], 'Missing campaign/session')
    require(type(data['segmentation_revision']) is int and data['segmentation_revision'] > 0, 'Invalid segmentation revision')
    require(data['sources'], 'Missing evidence sources')
    for source in [*data['sources'], *data['supporting_sources']]:
        require(hashlib.sha256(path_for(source['path']).read_bytes()).hexdigest() == source['sha256'], f"Source hash changed: {source['path']}")
    require(len({s['path'] for s in data['sources']}) == len(data['sources']), 'Duplicate source path')
    evidence = Evidence(data['sources'], path_for)
    span = evidence.span
    scenes, covered, last_end = {}, set(), {}
    for scene in data['scenes']:
        index = scene['index']
        require(type(index) is int and index == len(scenes) + 1, 'Scene indexes must be sequential integers')
        require(scene['evidence'], 'Missing scene evidence')
        for item in scene['evidence']:
            selected = span(item)
            if evidence.is_transcript(item):
                sid, start, end = evidence.bounds(item)
                require(start >= last_end.get(sid, 0), 'Scenes out of source order')
                last_end[sid] = end
                require(not covered & selected, 'Overlapping source coverage')
                covered.update(selected)
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
        require(evidence.is_transcript(excluded), 'Coverage exclusions apply only to transcripts')
        selected = span(excluded)
        require(not covered & selected, 'Overlapping source coverage')
        covered.update(selected)
    expected = {(sid, position) for sid, rows in evidence.rows.items() for position in range(len(rows))}
    require(covered == expected, 'Incomplete source coverage')
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
        passage = evidence.passage(quote)
        if not evidence.is_transcript(quote) and quote['kind'] == 'dialogue':
            require(quote.get('verification') == 'reported_in_notes', 'Note dialogue must be labeled reported_in_notes')
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
        require(record['evidence'], 'Missing complete interaction source bounds')
        scene_ids = set().union(*(span(item) for index in record['scenes'] for item in scenes[index]['evidence']))
        interaction_ids = []
        prior_end = {}
        for excerpt in record['evidence']:
            require(set(span(excerpt)) <= scene_ids, 'Excerpt crosses scene boundary')
            sid, start, end = evidence.bounds(excerpt)
            require(start >= prior_end.get(sid, 0), 'Interaction source ranges overlap or are out of order')
            prior_end[sid] = end
            interaction_ids.extend(span(excerpt))
        interaction_ids = set(interaction_ids)
        require(all(interaction_ids & set().union(*(span(item) for item in scenes[index]['evidence'])) for index in record['scenes']), 'Unrelated scene reference')
        if len(record['scenes']) > 1 or len(record['evidence']) > 1:
            require(record.get('continuity'), 'Missing encounter continuity explanation')
        if record['interaction'] == 'present':
            require(record.get('presence_basis'), 'Presence must be affirmatively evidenced')
        if record.get('perspective') is not None:
            require(record['perspective'] == 'session_record' and record['interaction'] == 'observed', 'Invalid observation perspective')
            require(all(not evidence.is_transcript(item) for item in record['evidence']) and record.get('observation_basis'), 'Documented observation requires note-only evidence and a basis')
        for excerpt in record.get('excerpts', []):
            require(set(span(excerpt)) <= interaction_ids, 'Highlight outside complete interaction bounds')
        require('npc' not in record and 'pull_quote' not in record, 'Legacy record fields')
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
            selected = set().union(*(span(item) for item in record['evidence'] if evidence.is_transcript(item)))
            # One paragraph can report separate events; note selectors need not partition prose.
            for previous in data['interactions']:
                if previous is record:
                    break
                if previous['entity'] == entity:
                    require(not (previous['scenes'] == record['scenes'] and previous['evidence'] == record['evidence']), 'Overlapping duplicate entity interactions')
            require(not occupied & selected, 'Overlapping duplicate entity interactions')
            occupied.update(selected)
    return evidence, span


def render(data, vault, rows, span, excerpts=False):
    data = upgrade_v3(data)
    evidence = rows
    entities = {entity['id']: entity for entity in data['entities']}

    def link(item):
        source = evidence.sources[item['source']]
        path = (vault / source['path']).resolve()
        if source['kind'] == 'transcript':
            a, b = item['startUid'], item['endUid']
            line = evidence.rows[item['source']][a]['line']
            label = f'Transcript {a}–{b}'
        else:
            line = item['startLine']
            label = f'Session note L{line}–L{item["endLine"]}'
        return f'[{label}](<{path}:{line}>)'

    counts = {kind: sum(e['kind'] == kind for e in entities.values()) for kind in ('npc', 'item')}
    out = [f'# {data["session"]}: campaign interaction extraction', '',
           f'{len(data["scenes"])} scenes · {counts["npc"]} NPCs · {counts["item"]} items · {len(data["interactions"])} records', '',
           'Sources: ' + ' · '.join(f'[{s["kind"]}](<{(vault / s["path"]).resolve()}>)' for s in data['sources']) + f' · segmentation revision {data["segmentation_revision"]}', '',
           '## Review notes', '']
    out.extend(f'- {note}' for note in data['review_notes'])
    out.extend(['', '## Scenes', '', '| Scene | Type | Location | Date/time | Source |', '| --- | --- | --- | --- | --- |'])
    for scene in data['scenes']:
        day = scene['date']
        when = day['start'] or 'unknown'
        if day['end'] != day['start']:
            when += f' to {day["end"]}'
        links = ', '.join(dict.fromkeys(link(item) for item in scene['evidence']))
        out.append(f'| {scene["index"]} | {scene["type"]} | {scene["location"]} | {when}; {day["time"] or "time unknown"} | {links} |')
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
            if quote.get('verification') == 'reported_in_notes':
                attribution = 'Reported in notes; not transcript-verified. ' + attribution
            out.extend([f'> {quote["quote"]}', '', f'{quote_label} ({quote["kind"]}): {link(quote)} — {attribution}', ''])
        for quote_id in featured:
            show_quote(all_quotes[quote_id])
        for record in records:
            label = ', '.join(str(index) for index in record['scenes'])
            out.extend([f'### Scenes {label} · {record["interaction"]} · {record["importance"]}', '', record['overview'], ''])
            if record.get('perspective') == 'session_record':
                out.extend(['Documented event; party witnessing is not established. ' + record['observation_basis'], ''])
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
                if intro.get('verification') == 'reported_in_notes':
                    out.extend(['Reported in notes; not transcript-verified.', ''])
            for excerpt in record['evidence']:
                out.extend([f'{"Complete interaction" if evidence.is_transcript(excerpt) else "Documented interaction"}: {link(excerpt)}', ''])
            if record.get('excerpts'):
                out.extend(['Key passages: ' + ', '.join(link(item) for item in record['excerpts']), ''])
            if excerpts:
                for excerpt in [*record.get('excerpts', record['evidence']), *(item for item in record['evidence'] if record.get('excerpts') and not evidence.is_transcript(item))]:
                    out.extend([f'Evidence excerpt: {link(excerpt)}', ''])
                    sid, start, end = evidence.bounds(excerpt)
                    if evidence.is_transcript(excerpt):
                        for uid, row in list(evidence.rows[sid].items())[start:end]:
                            out.append(f'> **{uid} {row["attribution"]}** {row["text"]}  ')
                    else:
                        out.extend('> ' + line for line in evidence.passage(excerpt).splitlines())
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

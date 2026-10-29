"""Canonical v5 structure, provenance validation, readiness and portable review rendering."""
import copy
import hashlib
import json
import os
import re
import subprocess
from functools import lru_cache
from html import escape
from pathlib import Path
from urllib.parse import quote
import jsonschema

SCHEMA = Path(__file__).resolve().parent.parent / 'references/session.schema.json'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def vault_path(vault, value):
    require(isinstance(value, str) and value and not Path(value).is_absolute(), 'Expected vault-relative path')
    path = (Path(vault) / value).resolve()
    require(path.is_relative_to(Path(vault).resolve()), 'Path escapes vault')
    components = [*Path(value).parts, *path.relative_to(Path(vault).resolve()).parts]
    require(not any(part.startswith('.') or part in {'_DM_', '_dm_notes'} for part in components), 'Private source/reference not permitted')
    require(path.is_file(), f'Missing vault file: {value}')
    return path

def ready(record):
    review = record.get('review', {})
    return review.get('confidence') == 'high' and review.get('status') in {'automatedReviewed', 'humanReviewed'}

def unique(items, key, label):
    result = {}
    for item in items:
        require(item[key] not in result, f'Duplicate {label}: {item[key]}')
        result[item[key]] = item
    return result

@lru_cache(maxsize=128)
def historical_source(vault, path, revision):
    require(re.fullmatch(r'[0-9a-f]{40}', revision), 'Source revision must be a full commit SHA')
    result = subprocess.run(['git', '-C', str(vault), 'show', f'{revision}:{path}'], capture_output=True)
    require(result.returncode == 0, f'Cannot read historical source: {path} at {revision}')
    return result.stdout

@lru_cache(maxsize=8)
def repository_url(vault):
    result = subprocess.run(['git', '-C', str(vault), 'remote', 'get-url', 'origin'], capture_output=True, text=True)
    match = re.fullmatch(r'(?:https://github.com/|git@github.com:)([\w.-]+/[\w.-]+?)(?:\.git)?', result.stdout.strip())
    require(match, 'Historical transcript links require a GitHub origin')
    return 'https://github.com/' + match[1]

def campaign_name(data, vault):
    path = Path(vault) / '_scripts/session_note_campaigns.json'
    campaigns = json.loads(path.read_text())['campaigns'].values() if path.exists() else []
    return next((c['name'] for c in campaigns if c['code'] == data['campaign']), data['campaign'])

def entity_anchor(entity_id):
    # Encoding bytes avoids collisions from punctuation or Unicode IDs.
    return 'entity-' + entity_id.encode('utf-8').hex()

def review_entities(data, excluded=None):
    excluded = excluded or {}
    entities = {e['id']: e for e in data.get('entities', [])}
    for eid, reason in excluded.items():
        require(eid in entities and entities[eid]['kind'] == 'item' and reason,
                'Display exclusions must name an existing item and give a reason')
    importance = {'star': 0, 'supporting': 1, 'cameo': 2}
    def order(e):
        rank = min((importance.get(r.get('importance'), 3) for r in data.get('interactions', []) if r['entity'] == e['id']), default=3)
        return ({'npc': 0, 'item': 1, 'organization': 2}[e['kind']], rank, e['label'].casefold())
    return sorted((e for e in entities.values() if e['id'] not in excluded), key=order)

class SourceCatalog:
    def __init__(self, data, vault, source_revision=None):
        self.vault = Path(vault)
        self.source_revision = source_revision
        self.sources = unique(data['sources'], 'id', 'source ID')
        self.rows = {}
        self.hashes = {}
        self.current_changed = []
        for sid, source in self.sources.items():
            path = vault_path(vault, source['path'])
            raw = historical_source(str(self.vault.resolve()), source['path'], source_revision) if source_revision else path.read_bytes()
            self.hashes[sid] = hashlib.sha256(raw).hexdigest()
            if source_revision and digest(path) != self.hashes[sid]:
                self.current_changed.append(source['path'])
            if source.get('sha256'):
                require(self.hashes[sid] == source['sha256'], f'Source hash changed: {source["path"]}')
            rows = {}
            for line, text in enumerate(raw.decode('utf-8').splitlines(), 1):
                m = re.match(r'^\[(u\d+)(?:\s*\|\s*(.*?))?\]\s?(.*)$', text)
                if m:
                    uid, speaker, text = m.groups()
                    require(uid not in rows, f'Duplicate source UID: {sid}:{uid}')
                    rows[uid] = dict(line=line, speaker=speaker or '', text=text, position=len(rows))
            require(rows, f'No transcript UIDs: {sid}')
            self.rows[sid] = rows

    def bounds(self, locator):
        require(locator['kind'] == 'transcript', 'Unsupported source kind')
        sid = locator['sourceId']
        require(sid in self.rows, f'Unknown source: {sid}')
        rows = self.rows[sid]
        a, b = locator['startUid'], locator['endUid']
        require(a in rows and b in rows, f'Missing source UID: {a}–{b}')
        start, end = rows[a]['position'], rows[b]['position']
        require(start <= end, 'Reversed source range')
        return sid, start, end

    def span(self, locator):
        sid, a, b = self.bounds(locator)
        return {(sid, i) for i in range(a, b + 1)}

    def passage(self, locator):
        sid, a, b = self.bounds(locator)
        return ' '.join(x['text'] for x in list(self.rows[sid].values())[a:b + 1])

    def link(self, locator, output):
        sid, _, _ = self.bounds(locator)
        line = self.rows[sid][locator['startUid']]['line']
        last = self.rows[sid][locator['endUid']]['line']
        path = self.vault / self.sources[sid]['path']
        target = quote(os.path.relpath(path, Path(output).parent), safe='/.-_')
        if self.source_revision:
            target = repository_url(str(self.vault.resolve())) + '/blob/' + self.source_revision + '/' + quote(self.sources[sid]['path'], safe='/.-_')
        anchor = f'L{line}' + (f'-L{last}' if last != line else '')
        return f'[{locator["startUid"]}–{locator["endUid"]}]({target}?plain=1#{anchor})'

def validate(data, vault, source_revision=None):
    jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=jsonschema.FormatChecker()).validate(data)
    catalog = SourceCatalog(data, vault, source_revision)
    for value in [*data['pcs'], *data.get('locations', [])]:
        vault_path(vault, value)
    def dates(record):
        if record.get('dateStart') and record.get('dateEnd'):
            require(record['dateStart'] <= record['dateEnd'], 'Reversed date interval')
    dates(data)
    scenes = unique(data.get('scenes', []), 'index', 'scene index')
    require(list(scenes) == sorted(scenes), 'Scene indexes must be ordered')
    coverage, ends = set(), {}
    for scene in scenes.values():
        sid, a, b = catalog.bounds(scene['source'])
        require(a > ends.get(sid, -1), 'Scenes overlap or are out of source order')
        ends[sid] = b
        coverage.update(catalog.span(scene['source']))
        if scene.get('location'):
            vault_path(vault, scene['location'])
        dates(scene)
        require(len(scene.get('aiSummary', '').split()) <= 25, 'Scene summary exceeds 25 words')
    entities = unique(data.get('entities', []), 'id', 'entity ID')
    for entity in entities.values():
        if entity.get('note'):
            vault_path(vault, entity['note'])
            require(entity['note'] not in data['pcs'] or entity['kind'] != 'npc', 'Participating PC included as NPC')
    records = unique(data.get('interactions', []), 'id', 'interaction ID')
    quotes = {}
    for record in records.values():
        require(record['entity'] in entities, 'Broken entity reference')
        require(record['scenes'] == sorted(record['scenes']), 'Interaction scene indexes out of order')
        require(all(i in scenes for i in record['scenes']), 'Broken scene reference')
        allowed = set().union(*(catalog.span(scenes[i]['source']) for i in record['scenes']))
        previous = {}
        for passage in record.get('passages', []):
            locator = passage['source']
            require(catalog.span(locator) <= allowed, 'Passage outside referenced scenes')
            sid, a, b = catalog.bounds(locator)
            require(a > previous.get(sid, -1), 'Passages overlap or are out of source order')
            previous[sid] = b
        for q in record.get('quotes', []):
            require(q['id'] not in quotes, 'Duplicate quote ID')
            require(catalog.span(q['source']) <= allowed, 'Quote outside referenced scenes')
            require(q['text'] in catalog.passage(q['source']), 'Quote is not verbatim transcript text')
            quotes[q['id']] = record['entity']
    for entity in entities.values():
        require(all(quotes.get(q) == entity['id'] for q in entity.get('aiSuggestedFeaturedQuotes', [])), 'Featured quote does not belong to entity')
    total = sum(len(x) for x in catalog.rows.values())
    return {'catalog': catalog, 'sourceUtterances': total, 'sceneUtterances': len(coverage),
            'unassignedUtterances': total - len(coverage), 'metadataReady': ready(data),
            'readyEntities': sum(ready(x) for x in entities.values()),
            'provisionalEntities': sum(not ready(x) for x in entities.values())}

def critical_queue(data):
    queue = []
    if not ready(data):
        queue.append({'target': 'session', 'review': data.get('review'), 'reason': 'Critical session metadata is provisional.'})
    for entity in data.get('entities', []):
        if not ready(entity):
            queue.append({'target': 'entity:' + entity['id'], 'label': entity['label'], 'review': entity.get('review'), 'reason': 'Entity identity/inclusion/vault match is provisional.'})
    return queue

def check_evidence(decision, catalog, vault):
    require(decision.get('reason') and decision.get('evidence'), 'Review requires reason and evidence')
    for locator in decision['evidence']:
        if 'vaultPath' in locator:
            vault_path(vault, locator['vaultPath'])
        else:
            catalog.bounds(locator)

def apply_review(data, report, vault, stage='automatedReviewed', source_revision=None):
    """Apply separately authored judgments; validation alone never creates judgments."""
    require(stage in {'automatedReviewed', 'humanReviewed'}, 'Invalid review stage')
    expected = hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    require(report.get('inputDigest') == expected, 'Stale review: candidate changed')
    require(report.get('reviewer') and report.get('decisions'), 'Missing reviewer/decisions')
    require(report.get('attempt') in {0, 1}, 'At most one targeted correction attempt')
    result = copy.deepcopy(data)
    catalog = validate(data, vault, source_revision)['catalog']
    targets = {'session': (result, 'review'), 'scenes': (result, 'sceneReview')}
    targets.update({'entity:' + e['id']: (e, 'review') for e in result.get('entities', [])})
    targets.update({'interaction:' + r['id']: (r, 'review') for r in result.get('interactions', [])})
    seen = set()
    for decision in report['decisions']:
        target = decision['target']
        require(target in targets and target not in seen, 'Unknown or duplicate review target')
        seen.add(target)
        check_evidence(decision, catalog, vault)
        record, key = targets[target]
        require(stage == 'humanReviewed' or record.get(key, {}).get('status') != 'humanReviewed', 'Automated review cannot overwrite human review')
        record[key] = {'confidence': decision['confidence'], 'status': stage}
    validate(result, vault, source_revision)
    return result

def render(data, vault, output, findings=None, source_revision=None, excluded=None, observations=None):
    checked = validate(data, vault, source_revision)
    cat = checked['catalog']
    findings, excluded = findings or {}, excluded or {}
    observations = observations or []
    entities = review_entities(data, excluded)
    records_by_entity = {e['id']: [r for r in data.get('interactions', []) if r['entity'] == e['id']] for e in data.get('entities', [])}
    kind_name = {'npc': 'NPC', 'item': 'Item', 'organization': 'Organization'}
    def state(record, key='review'):
        r = record.get(key, {})
        status = {'automatedReviewed': 'automated review', 'humanReviewed': 'human review', 'unreviewed': 'unreviewed'}.get(r.get('status'), 'unreviewed')
        return f'{r.get("confidence", "unknown")} confidence · {status}'
    def page(path):
        return '[' + escape(Path(path).stem, quote=False) + '](' + quote(os.path.relpath(Path(vault) / path, Path(output).parent), safe='/.-_') + ')'
    def cell(text):
        return str(text).replace('|', '\\|').replace('\n', ' ')
    def quote_lines(q):
        return ['> ' + escape(q['text'], quote=False).replace('\n', '\n> '), '', f'{q["type"]} · {cat.link(q["source"], output)}', '']
    def entity_link(e):
        return f'[{escape(e["label"], quote=False)}](#{entity_anchor(e["id"])})'
    navigation = []
    if (Path(output).parent.parent / 'sample.json').is_file():
        navigation.append('[All sessions](../README.md)')
    if (Path(output).parent / 'session.json').is_file():
        navigation.append('[Original session JSON](session.json)')
    lines = [f'# {campaign_name(data, vault)} · Session {data["session"]}', '',
             ' · '.join(navigation), '',
             f'**{len(entities)} entities** · {sum(not ready(e) for e in entities)} provisional · Played {data["realWorldDate"]}', '',
             'Start with the entity list. Each entry has its session overview, vault match and review notes; expand quotes or interactions for evidence.', '',
             f'Metadata: {state(data)} · ' + ('Ready for normal use' if ready(data) else '**Provisional critical metadata**'), '',
             '<details>', '<summary>Session dates, PCs, locations and metadata review</summary>', '',
             f'In-world span: {data.get("dateStart") or "unknown"} to {data.get("dateEnd") or "unknown"}', '',
             'PCs: ' + (', '.join(page(x) for x in data['pcs']) or '**No resolved PC pages; inspect the metadata review.**'), '',
             'Locations: ' + (', '.join(page(x) for x in data.get('locations', [])) or 'Not recorded'), '']
    if findings.get('session'):
        lines += ['Metadata review: ' + findings['session'], '']
    lines += ['</details>', '']
    if source_revision:
        lines += [f'Transcript links use the reviewed version at `{source_revision[:9]}`.', '']
        if cat.current_changed:
            lines += ['**The current transcript has changed since this extraction.** These cards show the original reviewed evidence; the extraction has not been refreshed.', '']
    lines += ['AI summaries are review aids. Confidence and review labels below are the saved assessments.', '',
              '## Entity list', '', '| Entity | Kind | Vault match | Review |', '| --- | --- | --- | --- |']
    for e in entities:
        match = page(e['note']) if e.get('note') else 'No linked page'
        status = state(e) + (' · **Provisional**' if not ready(e) else '')
        lines.append(f'| {cell(entity_link(e))} | {kind_name[e["kind"]]} | {cell(match)} | {status} |')
    if not entities:
        lines += ['', 'No entity records.']
    if excluded:
        lines += ['', f'{len(excluded)} item record(s) omitted under the selection rule; see [display exclusions](#display-exclusions).']
    covered_observations = set()
    for e in entities:
        records = records_by_entity[e['id']]
        all_quotes = {q['id']: q for r in records for q in r.get('quotes', [])}
        featured = e.get('aiSuggestedFeaturedQuotes', [])
        target = 'entity:' + e['id']
        own_targets = {target, *('interaction:' + r['id'] for r in records), *('quote:' + qid for qid in all_quotes)}
        notes = [(i, o) for i, o in enumerate(observations) if o['target'] in own_targets]
        covered_observations.update(i for i, _ in notes)
        lines += ['', f'<a id="{entity_anchor(e["id"])}"></a>', '', f'## {escape(e["label"], quote=False)}', '',
                  f'{kind_name[e["kind"]]} · **{state(e)}**' + (' · **Provisional entity**' if not ready(e) else ''), '',
                  'Vault match: ' + (page(e['note']) if e.get('note') else 'No linked page'), '',
                  e.get('aiSummary', '*No session overview recorded.*'), '']
        if not ready(e):
            lines += ['**Review question:** ' + findings.get(target, 'Entity inclusion, identity or vault match needs review.'), '']
        for _, note in notes:
            lines += ['**Audit observation:** ' + note['reason'], '']
        if featured:
            lines += ['<details>', f'<summary>Featured quotes ({len(featured)})</summary>', '']
            for qid in featured:
                lines += quote_lines(all_quotes[qid])
            lines += ['</details>', '']
        if ready(e) and findings.get(target):
            lines += ['<details>', '<summary>Review evidence</summary>', '', findings[target], '', '</details>', '']
        if records:
            lines += ['<details>', f'<summary>Interactions and source passages ({len(records)})</summary>', '']
            for r in records:
                scene_links = ', '.join(f'[{i}](#scene-{i})' for i in r['scenes'])
                lines += [f'### {r["interaction"].capitalize()} · {r.get("importance", "unrated")}', '',
                          r.get('aiSummary', '*No interaction overview recorded.*'), '',
                          f'Scenes: {scene_links} · {state(r)} · ID: `{r["id"]}`', '']
                if r.get('knownAs'):
                    lines += ['Known as: ' + r['knownAs'], '']
                for p in r.get('passages', []):
                    lines += [f'{p.get("relevance", "Passage").capitalize()}: {cat.link(p["source"], output)}' + (' — ' + p['aiSummary'] if p.get('aiSummary') else ''), '']
                if not r.get('passages'):
                    source_scenes = [s for s in data.get('scenes', []) if s['index'] in r['scenes']]
                    lines += ['Scene source: ' + ', '.join(cat.link(s['source'], output) for s in source_scenes), '']
                for q in r.get('quotes', []):
                    if q['id'] not in featured:
                        lines += quote_lines(q)
            lines += ['</details>', '']
        lines += ['[Back to entity list](#entity-list)', '']
    remaining = [o for i, o in enumerate(observations) if i not in covered_observations]
    if remaining:
        lines += ['## Other audit observations', '']
        lines += [f'- `{o["target"]}`: {o["reason"]}' for o in remaining] + ['']
    if excluded:
        lines += ['## Display exclusions', '', '<details>', '<summary>Items omitted under the selection rule</summary>', '',
                  'These entries remain in the original JSON and audit history. The review focuses on meaningful item discoveries, exchanges, destruction and plot relevance; ordinary treasure and routine gear use are omitted.', '']
        by_id = {e['id']: e for e in data.get('entities', [])}
        lines += [f'- **{by_id[eid]["label"]}** (`{eid}`): {reason}' for eid, reason in excluded.items()]
        lines += ['', '</details>', '']
    lines += ['## Scene reference', '', '<details>', f'<summary>Scene division and context ({len(data.get("scenes", []))} scenes)</summary>', '',
              f'Collection review: {state(data, "sceneReview")}', '',
              '| Scene | Type | Location | In-world time | AI summary | Source |', '| --- | --- | --- | --- | --- | --- |']
    for s in data.get('scenes', []):
        location = page(s['location']) if s.get('location') else 'unresolved'
        detail = s.get('locationDetail') or ''
        dates = [s[k] for k in ['dateStart', 'dateEnd'] if s.get(k)]
        when = '; '.join(x for x in [' – '.join(dict.fromkeys(dates)), s.get('time')] if x) or 'unspecified'
        lines.append(f'| <a id="scene-{s["index"]}"></a>{s["index"]} | {s.get("type", "")} | {cell(location + ("; " + detail if detail else ""))} | {cell(when)} | {cell(s.get("aiSummary", ""))} | {cat.link(s["source"], output)} |')
    lines += ['', '</details>', '']
    return '\n'.join(line.rstrip() for line in lines).rstrip() + '\n'

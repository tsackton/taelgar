"""Canonical v5 structure, provenance validation, readiness and portable review rendering."""
import copy
import hashlib
import json
import os
import re
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

class SourceCatalog:
    def __init__(self, data, vault):
        self.vault = Path(vault)
        self.sources = unique(data['sources'], 'id', 'source ID')
        self.rows = {}
        for sid, source in self.sources.items():
            path = vault_path(vault, source['path'])
            if source.get('sha256'):
                require(digest(path) == source['sha256'], f'Source hash changed: {source["path"]}')
            rows = {}
            for line, text in enumerate(path.read_text().splitlines(), 1):
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
        anchor = f'L{line}' + (f'-L{last}' if last != line else '')
        return f'[{locator["startUid"]}–{locator["endUid"]}]({target}?plain=1#{anchor})'

def validate(data, vault):
    jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=jsonschema.FormatChecker()).validate(data)
    catalog = SourceCatalog(data, vault)
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

def apply_review(data, report, vault, stage='automatedReviewed'):
    """Apply separately authored judgments; validation alone never creates judgments."""
    require(stage in {'automatedReviewed', 'humanReviewed'}, 'Invalid review stage')
    expected = hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    require(report.get('inputDigest') == expected, 'Stale review: candidate changed')
    require(report.get('reviewer') and report.get('decisions'), 'Missing reviewer/decisions')
    require(report.get('attempt') in {0, 1}, 'At most one targeted correction attempt')
    result = copy.deepcopy(data)
    catalog = validate(data, vault)['catalog']
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
    validate(result, vault)
    return result

def render(data, vault, output, findings=None):
    checked = validate(data, vault)
    cat = checked['catalog']
    def state(record, key='review'):
        r = record.get(key, {})
        return f'{r.get("confidence", "unknown")} / {r.get("status", "unreviewed")}'
    def page(path):
        return '[' + Path(path).stem + '](' + quote(os.path.relpath(Path(vault) / path, Path(output).parent), safe='/.-_') + ')'
    lines = [f'# {data["campaign"]} session {data["session"]}', '',
             f'Real-world date: {data["realWorldDate"]} · Critical metadata: **{state(data)}** · ' + ('Ready for normal use' if ready(data) else '**Provisional critical metadata**'), '',
             f'In-world span: {data.get("dateStart") or "unknown"} to {data.get("dateEnd") or "unknown"}', '',
             'PCs: ' + (', '.join(page(x) for x in data['pcs']) or '**No resolved PC pages; inspect the metadata review.**'), '',
             'Locations: ' + ', '.join(page(x) for x in data.get('locations', [])), '',
             'AI summaries are navigation/review aids, not source evidence or replacement narrative.', '',
             '## Scene division', '', f'Collection review: {state(data, "sceneReview")}', '',
             '| Scene | Type | Location | In-world time | AI summary | Source |', '| --- | --- | --- | --- | --- | --- |']
    for s in data.get('scenes', []):
        location = page(s['location']) if s.get('location') else 'unresolved'
        detail = s.get('locationDetail') or ''
        dates = [s[k] for k in ['dateStart', 'dateEnd'] if s.get(k)]
        when = '; '.join(x for x in [' – '.join(dict.fromkeys(dates)), s.get('time')] if x) or 'unspecified'
        summary = s.get('aiSummary', '').replace('|', '\\|')
        detail = detail.replace('|', '\\|').replace('\n', ' ')
        when = when.replace('|', '\\|').replace('\n', ' ')
        lines.append(f'| {s["index"]} | {s.get("type", "")} | {location}; {detail} | {when} | {summary} | {cat.link(s["source"], output)} |')
    for e in data.get('entities', []):
        records = [r for r in data.get('interactions', []) if r['entity'] == e['id']]
        lines += ['', f'## {e["label"]} · {e["kind"]}', '', f'Entity review: **{state(e)}** · ' + ('Ready for normal use' if ready(e) else '**Provisional entity**'), '']
        if e.get('note'):lines += [page(e['note']), '']
        if e.get('aiSummary'):lines += [e['aiSummary'], '']
        all_quotes = {q['id']: q for r in records for q in r.get('quotes', [])}
        featured = e.get('aiSuggestedFeaturedQuotes', [])
        for qid in featured:
            q = all_quotes[qid]
            lines += [f'> {q["text"]}', '', f'AI-suggested featured {q["type"]} quote · {cat.link(q["source"], output)}', '']
        for r in records:
            lines += [f'### {r["id"]} · {r["interaction"]} · {r.get("importance", "unrated")}', '',
                      f'Scenes: {", ".join(map(str,r["scenes"]))} · Review: {state(r)}', '']
            if r.get('knownAs'):lines += ['Known as: ' + r['knownAs'], '']
            if r.get('aiSummary'):lines += [r['aiSummary'], '']
            for p in r.get('passages', []):
                lines += [f'{p.get("relevance", "Passage")}: {cat.link(p["source"], output)}' + (' — ' + p['aiSummary'] if p.get('aiSummary') else ''), '']
            for q in r.get('quotes', []):
                if q['id'] not in featured:lines += [f'> {q["text"]}', '', f'{q["type"]} quote · {cat.link(q["source"], output)}', '']
    lines += ['## Critical review queue', '']
    queue = critical_queue(data)
    findings = findings or {}
    lines += [f'- `{q["target"]}`: {findings.get(q["target"], q["reason"])}' for q in queue] or ['No unresolved critical records.']
    return '\n'.join(lines) + '\n'

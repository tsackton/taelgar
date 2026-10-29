#!/usr/bin/env python3
"""Audit published trial executions and build a shareable review index; no model calls."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import quote
import yaml
from jsonschema import ValidationError
from session_model import apply_review, validate, render, critical_queue, check_evidence, campaign_name, entity_anchor, review_entities, ready, check_correction, vault_path


def read(path):
    return json.loads(Path(path).read_text())


def result_folder(vault, selection, results):
    """New runs live in session bundles; YAML owns the completed output pointer."""
    if 'inputs' in selection:
        manifest = vault_path(vault, selection['manifest'])
        metadata = yaml.safe_load(manifest.read_text())
        entry = metadata.get('interactionExtraction', {})
        if entry:
            relative = entry['sessionJson']
            if Path(relative).is_absolute():
                raise ValueError('Extraction pointer must be YAML-relative')
            target = manifest.parent / relative
            target = vault_path(vault, os.path.relpath(target, vault))
            if target.name != 'session.json':
                raise ValueError('Expected the completed session.json pointer')
            return target.parent
    return Path(results) / selection['id']


def audit_chain(folder, vault, selection=None, source_revision=None):
    """Replay the immutable trial reports; later edits need a new review candidate."""
    folder = Path(folder)
    if (folder / 'session-processing-data.json').is_file():
        from session_processing import audit_reviews, validate_processing
        data = read(folder / 'session.json')
        processing = read(folder / 'session-processing-data.json')
        if data.get('schemaVersion') == 6:
            if source_revision:
                raise ValueError('v6 inputs are bound by YAML and processing fingerprints, not the v5 snapshot option')
            catalog = validate(data, vault, processing=processing)['catalog']
            validate_processing(data, processing, vault, catalog, complete=True)
            if audit_reviews(processing, vault) != data:
                raise ValueError('Published session differs from its reviewed candidate chain')
            if selection is not None:
                source = catalog.sources[catalog.bundle['sourceId']]
                if selection['manifest'] != data['sessionYaml'] or selection['inputs'] != processing['inputs'] or selection['sha256'] != source['sha256']:
                    raise ValueError('Published execution does not match sampled YAML/source inputs')
            findings = {}
            for record in processing['reviews']:
                findings.update({d['target']: d['reason'] for d in record['report']['decisions']})
            return data, findings
    data = read(folder / 'extraction.json')
    reports = sorted(folder.glob('review-decisions-*.json'))
    if not reports or len(reports) > 2:
        raise ValueError('Expected initial review and at most one correction report')
    findings = {}
    for attempt, file in enumerate(reports):
        report = read(file)
        if file.name != f'review-decisions-{attempt}.json' or report.get('attempt') != attempt:
            raise ValueError('Review attempt sequence is incomplete or repeated')
        if attempt:
            corrected = read(folder / 'correction-candidate.json')
            check_correction(data, corrected, report, vault, source_revision)
            data = corrected
        data = apply_review(data, report, vault, source_revision=source_revision)
        findings.update({d['target']:d['reason'] for d in report['decisions']})
    if data != read(folder / 'session.json'):
        raise ValueError('Published session differs from its reviewed candidate chain')
    if selection is not None:
        if data['campaign'] != selection['campaign'] or data['session'] != selection['session']:
            raise ValueError('Published execution does not match sampled campaign/session')
        if len(data['sources']) != 1 or data['sources'][0]['path'] != selection['source']:
            raise ValueError('Published execution does not match sampled transcript')
        catalog = validate(data, vault, source_revision)['catalog']
        if catalog.hashes[data['sources'][0]['id']] != selection['sha256']:
            raise ValueError('Published transcript changed since sampling')
    execution = read(folder / 'execution.json')
    if execution.get('correctionAttempts') != len(reports) - 1:
        raise ValueError('Execution correction count differs from report chain')
    if not execution.get('fullTranscriptRead'):
        raise ValueError('No complete transcript-read attestation')
    for target in [data, *data.get('entities', [])]:
        if target.get('review', {}).get('status') not in {'automatedReviewed', 'humanReviewed'}:
            raise ValueError('Critical record has not received semantic review')
    return data, findings


def build(vault, sample, results, output, source_revision=None, exclusions=None):
    rows, directory = [], []
    exclusions = exclusions or {}
    if set(exclusions) - {s['id'] for s in sample['selected']}:
        raise ValueError('Display exclusions refer to an unsampled session')
    def link(path, label, anchor=''):
        return f'[{label}]({quote(os.path.relpath(path, Path(output).parent), safe="/.-_")}{anchor})'
    lines = [f'# Entity reviews · {len(sample["selected"])} sessions', '',
             'Choose a session to review its NPCs, significant items and organizations. Each entity has an overview, vault match, confidence, review notes and expandable quotes and interactions.', '',
             'Item selection focuses on meaningful discoveries, exchanges, destruction and plot relevance. Ordinary treasure, routine gear use and incidental objects are omitted. Original extraction JSON and review decisions are retained.', '']
    if (Path(results) / 'FINDINGS.md').exists():
        lines += [link(Path(results) / 'FINDINGS.md', 'Trial findings') + ' · [Model overview](../MODEL_OVERVIEW.md)', '']
    if source_revision:
        lines += [f'Transcript links and audit checks use the reviewed source snapshot at `{source_revision[:9]}`. Sessions whose current transcript has changed are marked below; their extraction has not been refreshed.', '']
    lines += ['| Session | NPCs | Items | Organizations | Provisional entities | Session metadata | Source |',
              '| --- | --- | --- | --- | --- | --- | --- |']
    for selection in sample['selected']:
        row = {'id':selection['id'], 'status':'pending'}
        try:
            folder = result_folder(vault, selection, results)
        except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
            row.update(status='invalid', error=str(error))
            rows.append(row)
            lines.append(f'| {selection["id"]} | — | — | — | — | Invalid YAML output pointer | {str(error).replace("|", "/")} |')
            continue
        if (folder / 'session.json').exists():
            try:
                data, findings = audit_chain(folder, vault, selection, source_revision)
                processing = read(folder / 'session-processing-data.json') if data.get('schemaVersion') == 6 else None
                checks = validate(data, vault, source_revision, processing)
                catalog = checks.pop('catalog')
                excluded = exclusions.get(selection['id'], {})
                entities = review_entities(data, excluded)
                observations = read(folder / 'independent-audit.json').get('findings', []) if (folder / 'independent-audit.json').exists() else []
                cards = render(data, vault, folder / 'review.md', findings, source_revision, excluded, observations, processing)
                if processing and (folder / 'review.md').exists() and (folder / 'review.md').read_text() != cards:
                    raise ValueError('Existing v6 review differs from generated output; preserve it and write a review candidate')
                (folder / 'review.md').write_text(cards)
                queue = critical_queue(data, processing)
                for item in queue:item['reason'] = findings.get(item['target'], item['reason'])
                (folder / 'queue.json').write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
                counts = [len(data.get(k, [])) for k in ['scenes','entities','interactions']]
                row.update(status='reviewed', counts=counts, checks=checks, criticalQueue=queue,
                           displayedEntities=len(entities), excludedEntities=excluded, currentSourceChanged=bool(catalog.current_changed))
                metadata = catalog.display_metadata() if processing else data
                title = f'{campaign_name(metadata, vault)} {metadata["session"]}'
                kind_counts = [sum(e['kind'] == k for e in entities) for k in ['npc','item','organization']]
                state = 'High · reviewed' if checks['metadataReady'] else data.get('review', {}).get('confidence', 'unknown').capitalize() + ' · provisional'
                source_state = '**Changed since review**' if catalog.current_changed else 'Unchanged'
                provisional = sum(not ready(e) for e in entities)
                lines.append(f'| {link(folder / "review.md", title, "#entity-list")} | {kind_counts[0]} | {kind_counts[1]} | {kind_counts[2]} | {provisional} | {state} | {source_state} |')
                directory += [f'### {link(folder / "review.md", title)}', '']
                for kind, label in [('npc', 'NPCs'), ('item', 'Items'), ('organization', 'Organizations')]:
                    names = [link(folder / 'review.md', e['label'].replace('|', '\\|'), '#' + entity_anchor(e['id'])) + (' **(?)**' if not ready(e) else '') for e in entities if e['kind'] == kind]
                    if names:directory += [f'**{label}:** ' + ' · '.join(names), '']
            except (ValueError, KeyError, OSError, ValidationError) as error:
                row.update(status='invalid', error=str(error))
                lines.append(f'| {selection["id"]} | — | — | — | — | Audit failed | {str(error).replace("|", "/")} |')
        else:
            lines.append(f'| {selection["id"]} | — | — | — | — | Pending | — |')
        rows.append(row)
    complete = all(r['status']=='reviewed' for r in rows)
    lines += ['', '## What to review', '',
              '- Are the right entities included, with the right vault matches?',
              '- Does each overview capture the entity’s role in the session?',
              '- Are the featured quotes useful, and are review questions easy to resolve?', '',
              '## Entity directory', '', '**(?)** marks a provisional entity. Names link directly to its review entry.', '', *directory,
              '<details>', '<summary>Sampling and validation details</summary>', '',
              f'Seed `{sample["seed"]}`; {len(sample["selected"])} sessions selected without replacement from {len(sample["population"])} available transcripts, across the available campaigns. Each file declares its schema version.', '',
              sample.get('method', ''), '',
              f'**{sum(r["status"]=="reviewed" for r in rows)}/{len(rows)} execution chains verified**' + (' against the reviewed transcript snapshot.' if source_revision else '.'), '',
              'Saved confidence and review states are unchanged. Passing the audit does not resolve provisional facts or constitute a new semantic review. Display exclusions are presentation choices; they do not rewrite the original extraction or its review history.', '',
              'Agents performed extraction and semantic review; Python validates and renders their records. Existing beats were optional review hints. This trial does not measure autonomous API cost or calibrated confidence.', '',
              '</details>', '']
    Path(output).write_text('\n'.join(lines))
    return {'seed':sample['seed'],'complete':complete,'sourceRevision':source_revision,'executions':rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault', type=Path, required=True)
    p.add_argument('--sample', type=Path, required=True)
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--status', type=Path)
    p.add_argument('--review-options', type=Path, help='Presentation-only sourceRevision and excludedEntities settings')
    p.add_argument('--require-complete', action='store_true')
    a = p.parse_args()
    options = read(a.review_options) if a.review_options else {}
    if set(options) - {'sourceRevision', 'excludedEntities'}:
        raise ValueError('Unknown review options')
    result = build(a.vault.resolve(), read(a.sample), a.results, a.output, options.get('sourceRevision'), options.get('excludedEntities'))
    if a.status:a.status.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'complete':result['complete'],'statuses':{r['id']:r['status'] for r in result['executions']}}))
    if a.require_complete and not result['complete']:raise SystemExit(1)


if __name__ == '__main__':main()

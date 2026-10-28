#!/usr/bin/env python3
"""Audit published trial executions and build a shareable review index; no model calls."""
import argparse
import json
import os
from pathlib import Path
from urllib.parse import quote
from jsonschema import ValidationError
from session_model import apply_review, validate, render, critical_queue, check_evidence, digest, vault_path


def read(path):
    return json.loads(Path(path).read_text())


def audit_chain(folder, vault, selection=None):
    """Replay the immutable trial reports; later edits need a new review candidate."""
    folder = Path(folder)
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
            for key in ['schemaVersion', 'campaign', 'session', 'sources']:
                if corrected[key] != data[key]:
                    raise ValueError(f'Correction changed execution identity/source: {key}')
            # Changed claims must be explicitly reassessed, not inherit old approval.
            targets = {d['target'] for d in report['decisions']}
            for key in ['review', 'sceneReview']:
                if corrected.get(key) != data.get(key):
                    raise ValueError('Correction cannot change review states directly')
            ignored = {'review', 'sceneReview', 'entities', 'interactions', 'scenes'}
            if {k:v for k,v in corrected.items() if k not in ignored} != {k:v for k,v in data.items() if k not in ignored}:
                if data.get('review', {}).get('status') == 'humanReviewed':
                    raise ValueError('Correction cannot overwrite human-reviewed metadata')
                if 'session' not in targets:raise ValueError('Metadata correction lacks session reassessment')
            if corrected.get('scenes') != data.get('scenes'):
                if data.get('sceneReview', {}).get('status') == 'humanReviewed':
                    raise ValueError('Correction cannot overwrite human-reviewed scenes')
                if 'scenes' not in targets:raise ValueError('Scene correction lacks collection reassessment')
            removed = set()
            for collection, prefix in [('entities', 'entity:'), ('interactions', 'interaction:')]:
                old = {r['id']:r for r in data.get(collection, [])}
                new = {r['id']:r for r in corrected.get(collection, [])}
                for rid, record in old.items():
                    if record.get('review', {}).get('status') == 'humanReviewed' and new.get(rid) != record:
                        raise ValueError(f'Correction cannot overwrite human-reviewed record: {prefix}{rid}')
                    if rid in new and record.get('review') != new[rid].get('review'):
                        raise ValueError('Correction cannot change review states directly')
                removed.update(prefix + rid for rid in old.keys() - new.keys())
                for rid, record in new.items():
                    if record != old.get(rid) and prefix + rid not in targets:
                        raise ValueError(f'Correction lacks reassessment: {prefix}{rid}')
            removals = report.get('removals', [])
            if len(removals) != len(removed) or {r['target'] for r in removals} != removed:
                raise ValueError('Removed records require explicit removal decisions')
            for removal in removals:
                check_evidence(removal, validate(data, vault)['catalog'], vault)
            data = corrected
        data = apply_review(data, report, vault)
        findings.update({d['target']:d['reason'] for d in report['decisions']})
    if data != read(folder / 'session.json'):
        raise ValueError('Published session differs from its reviewed candidate chain')
    if selection is not None:
        if data['campaign'] != selection['campaign'] or data['session'] != selection['session']:
            raise ValueError('Published execution does not match sampled campaign/session')
        if len(data['sources']) != 1 or data['sources'][0]['path'] != selection['source']:
            raise ValueError('Published execution does not match sampled transcript')
        if digest(vault_path(vault, data['sources'][0]['path'])) != selection['sha256']:
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


def build(vault, sample, results, output):
    rows = []
    def link(path, label):
        return f'[{label}]({quote(os.path.relpath(path, Path(output).parent), safe="/.-_")})'
    lines = [f'# {len(sample["selected"])}-session interaction trial', '',
             'Schema v5 · Agent extraction followed by a separate semantic review · Existing beats used only as optional review hints.', '',
             'This is a prototype of the extraction and review process, not an automatic promotion of all records into canon. Medium/low critical records remain provisional.', '',
             f'Seed: `{sample["seed"]}`. {len(sample["selected"])} sessions selected without replacement from {len(sample["population"])} available transcripts, with campaign variety guaranteed before filling remaining slots.', '',
             '| Session | Scenes / entities / interactions | Critical metadata | Provisional entities | Review |',
             '| --- | --- | --- | --- | --- |']
    if (Path(results) / 'FINDINGS.md').exists():
        lines[2:2] = [link(Path(results) / 'FINDINGS.md', 'Findings and suggested starting points') + ' · [Model overview](../MODEL_OVERVIEW.md)', '']
    for selection in sample['selected']:
        folder = Path(results) / selection['id']
        row = {'id':selection['id'], 'status':'pending'}
        if (folder / 'session.json').exists():
            try:
                data, findings = audit_chain(folder, vault, selection)
                checks = validate(data, vault); checks.pop('catalog')
                cards = render(data, vault, folder / 'review.md', findings)
                if (folder / 'independent-audit.json').exists():
                    audit = read(folder / 'independent-audit.json')
                    cards += '\n## Independent audit observations\n\n'
                    cards += '\n'.join(f'- `{f["target"]}`: {f["reason"]}' for f in audit.get('findings', [])) + '\n'
                (folder / 'review.md').write_text(cards)
                queue = critical_queue(data)
                for item in queue:item['reason'] = findings.get(item['target'], item['reason'])
                (folder / 'queue.json').write_text(json.dumps(queue, ensure_ascii=False, indent=2) + '\n')
                counts = [len(data.get(k, [])) for k in ['scenes','entities','interactions']]
                row.update(status='reviewed', counts=counts, checks=checks, criticalQueue=queue)
                state = 'Ready' if checks['metadataReady'] else data['review']['confidence'] + ' · provisional'
                lines.append(f'| {selection["id"]} | {" / ".join(map(str, counts))} | {state} | {checks["provisionalEntities"]} | {link(folder / "review.md", "Cards")} · {link(folder / "session.json", "JSON")} |')
            except (ValueError, KeyError, OSError, ValidationError) as error:
                row.update(status='invalid', error=str(error))
                lines.append(f'| {selection["id"]} | — | Audit failed | — | {str(error).replace("|", "/")} |')
        else:
            lines.append(f'| {selection["id"]} | — | Pending | — | — |')
        rows.append(row)
    complete = all(r['status']=='reviewed' for r in rows)
    lines += ['', f'Execution coverage: **{sum(r["status"]=="reviewed" for r in rows)}/{len(rows)} reviewed**. A reviewed execution may still have provisional critical facts.', '',
              '## What to critique', '',
              '- Are scenes divided usefully, and do conversations remain whole?',
              '- Are the selected NPCs, items and organizations useful without becoming exhaustive creature lists?',
              '- Do the quotes and short summaries make the source worth opening?',
              '- Are the unresolved critical questions specific enough for fast review?', '',
              'Each folder preserves the initial extraction, digest-bound review decisions, any one-round correction candidate, final session, execution evidence and unresolved queue. Links open the original source range. AI summaries are navigation aids.', '',
              'The Python commands prepare inputs, validate provenance, apply externally authored review judgments and render results. Agents perform semantic extraction and review; this trial does not measure autonomous API cost or calibrated confidence accuracy.', '']
    Path(output).write_text('\n'.join(lines))
    return {'seed':sample['seed'],'complete':complete,'executions':rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault', type=Path, required=True)
    p.add_argument('--sample', type=Path, required=True)
    p.add_argument('--results', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--status', type=Path)
    p.add_argument('--require-complete', action='store_true')
    a = p.parse_args()
    result = build(a.vault.resolve(), read(a.sample), a.results, a.output)
    if a.status:a.status.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'complete':result['complete'],'statuses':{r['id']:r['status'] for r in result['executions']}}))
    if a.require_complete and not result['complete']:raise SystemExit(1)


if __name__ == '__main__':main()

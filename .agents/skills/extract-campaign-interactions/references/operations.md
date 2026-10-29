# Operations

Dependencies: Python, `PyYAML`, `jsonschema`. Run from the vault root. The tools prepare/validate/render/apply separately authored review decisions; they do not call a model. Keep transcript context and the reusable name index outside the vault.

## Inspect and prepare

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . inspect --session-yaml _sessions/CAMPAIGN/SESSION/cleaned/PREFIX-session.yaml --output /tmp/bundle-inspection.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . index --output /tmp/vault-index.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . prepare --session-yaml _sessions/CAMPAIGN/SESSION/cleaned/PREFIX-session.yaml --index /tmp/vault-index.json --output /tmp/session-work
```

`inspect` reports registered source selection and proposed YAML path fixes. It never edits YAML. A primary path problem blocks preparation; review and fix its declaration in YAML within authorized scope before retrying. `prepare` prefers registered polished Markdown and retains comment UID mappings in the compact transcript. It creates `SESSION/draft.json` (v6), `session-processing-data.json`, `candidates.json` and `transcript.txt`. PC/name hits are review candidates, not automatic accepted attendance or entity matches. No beats are read.

For requested random batches:

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . sample --count 10 --seed 20261028 --output /tmp/sample.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . prepare --sample /tmp/sample.json --index /tmp/vault-index.json --output /tmp/session-work
```

Sampling records eligible sessions and exclusions, including missing source registration/path proposals. It samples across available campaigns without replacement. Older bundles without a YAML-registered cleaned transcript are not silently eligible. If too few qualify, inspect/fix declarations before requesting that sample size. `--resume` preserves existing work only for unchanged YAML/source fingerprints.

## Extract and review

Read the whole transcript, write scenes/entities/interactions into `draft.json`, and update processing `fullTranscriptRead`, `excludedBlocks`, `metadataFindings` and `stage: extracted`. Never write duplicated metadata/source paths into the draft or edit review history by hand. See [processing evidence](processing.md).

```sh
python .agents/skills/extract-campaign-interactions/scripts/validate.py --vault . --input /tmp/session-work/SESSION/draft.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . review-request --input /tmp/session-work/SESSION/draft.json --output /tmp/session-work/SESSION/review-request.json
```

The processing file defaults to the input's sibling `session-processing-data.json`; `--processing` selects it explicitly. Review requests include authoritative YAML context, entity evidence, exclusions and unexplained ranges. Existing beats/beat facts are optional noncanonical review hints. Only the review pass may inspect them.

A separately authored report uses:

```json
{
  "inputDigest": "candidate digest from request",
  "processingDigest": "processing digest from request",
  "reviewer": "actual reviewer/pass identifier",
  "attempt": 0,
  "decisions": [
    {"target":"session","confidence":"high","reason":"Evidence-based assessment of YAML consistency and locations.","evidence":[{"yamlField":"drStart"},{"kind":"transcript","sourceId":"transcriptProcessing.artifacts.polishedMarkdown","startUid":"u0001","endUid":"u0020"}]},
    {"target":"scenes","confidence":"high","reason":"Evidence-based assessment of division and exclusions.","evidence":[{"kind":"transcript","sourceId":"transcriptProcessing.artifacts.polishedMarkdown","startUid":"u0001","endUid":"u0020"}]}
  ]
}
```

Also assess each entity using `entity:ID`, and individual interactions when useful using `interaction:ID`. A clear conflicting transcript date becomes a critical processing finding, with both source and YAML evidence; metadata extensions/clarifications from YAML are not contradictions. If evidence/findings change, obtain a new request before applying the report.

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . apply-review --input /tmp/session-work/SESSION/draft.json --report /tmp/session-work/SESSION/review-decisions-0.json --output /tmp/session-work/SESSION/reviewed.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . render --input /tmp/session-work/SESSION/reviewed.json --output /tmp/session-work/SESSION/review.md --queue /tmp/session-work/SESSION/queue.json
```

The apply command appends candidate/evidence/report snapshots to the output directory's processing file. It refuses to overwrite an existing candidate or unrelated processing file. Use `--human` only to record an actual human review. Keep meaningful reasons for every assessment, especially provisional critical records. Review pages remain entity-first, with complete exclusions/reasons in their coverage section.

One correction/recheck is supported (`attempt: 1`). Write a corrected candidate preserving existing review flags, obtain a fresh request, then apply the new report. Removed entities/interactions require explicit `removals` entries with `target`, `reason` and `evidence`. Changed claims require reassessment. Do not reset history to evade the one-correction limit.

## Complete and register

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . complete --input /tmp/session-work/SESSION/reviewed.json --output _sessions/CAMPAIGN/SESSION/interactions
```

This validates source coverage, complete-read attestation and review replay, writes `session.json`, `session-processing-data.json` and `review.md`, then appends `interactionExtraction.sessionJson` and `interactionExtraction.processingData` to YAML. These pointers are YAML-directory-relative. Other YAML fields and formatting are preserved. No source-path or date repairs are applied automatically. Existing different outputs and pointers are protected. An unresolved critical finding does not prevent completion if it remains explicitly provisional after review.

For v6 batches, `batch.py` follows each sampled YAML's `interactionExtraction.sessionJson` pointer and replays its processing history. The batch directory contains navigation and run metadata, without another copy of canonical JSON. Existing different v6 review pages are protected. Historical v5 trials still use their original extraction/report chains under the results directory.

## Historical pilot review

The ten-session v5 pilot remains a historical trial and is not reinterpreted or migrated. Its presentation-only rebuild is still available:

```sh
python .agents/skills/extract-campaign-interactions/scripts/batch.py --vault . --sample _sessions/interaction-pilot/v5/sample.json --results _sessions/interaction-pilot/v5 --output _sessions/interaction-pilot/v5/README.md --status _sessions/interaction-pilot/v5/batch-status.json --review-options _sessions/interaction-pilot/v5/review-options.json --require-complete
```

Its explicit `sourceRevision` reads immutable historical source bytes and verifies saved hashes/quotes without changing current transcripts. Display-only `excludedEntities` omits specified items with reasons while preserving original JSON and complete critical queues. New extraction applies the item-selection rule at generation time. Historical v3 validation remains available; v4 is unsupported. No old file is automatically migrated.

Checks:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s .agents/skills/extract-campaign-interactions/scripts
```

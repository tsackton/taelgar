# Operations

Python dependencies: `PyYAML` and `jsonschema` (see `requirements.txt`). Commands below run from the vault root. Keep temporary context and the name index outside the vault. The tools perform deterministic support work; the extraction and semantic-review steps require an agent following the skill.

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . index --output /tmp/vault-index.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . sample --count 10 --seed 20261028 --output /tmp/sample.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . prepare --sample /tmp/sample.json --index /tmp/vault-index.json --output /tmp/session-work
```

`sample` records the population and exclusions, and selects without replacement across available transcript campaigns. `prepare` refuses to overwrite prior executions; it emits a metadata draft, name candidates and a compact full transcript. It does not load beats. Candidate names are not automatically converted into entities or interactions. Review unresolved PC matches in `candidates.json` against manifest/speaker evidence.

Add `--resume` to preparation to preserve existing executions from the same sample with unchanged source hashes. Failed preparations are reported individually while other sessions continue. Unknown/partial manifest dates are omitted and recorded as preparation issues; they are not converted into invented exact dates.

Read the full transcript and write the extraction into the draft. Validate and generate a separate review request:

```sh
python .agents/skills/extract-campaign-interactions/scripts/validate.py --vault . --input /tmp/session-work/SESSION/draft.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . review-request --input /tmp/session-work/SESSION/draft.json --output /tmp/session-work/SESSION/review-request.json
```

The request provides an input digest, critical metadata, entity evidence ranges and optional existing beat paths. The reviewer must independently examine actual evidence. Write a report shaped as:

```json
{
  "inputDigest": "digest from review request",
  "reviewer": "identifier of actual review pass",
  "attempt": 0,
  "decisions": [{
    "target": "entity:guide",
    "confidence": "high",
    "reason": "Evidence-based explanation of inclusion and match.",
    "evidence": [
      {"kind":"transcript","sourceId":"transcript-1","startUid":"u0001","endUid":"u0020"},
      {"vaultPath":"People/Guide.md"}
    ]
  }]
}
```

Targets are `session`, `scenes`, `entity:ID`, `interaction:ID`. `attempt: 0` is the first review; `attempt: 1` is the one targeted correction/recheck. Apply a review to a new candidate, not an existing accepted file:

```sh
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . apply-review --input /tmp/session-work/SESSION/draft.json --report /tmp/session-work/SESSION/review-decisions.json --output /tmp/session-work/SESSION/reviewed.json
python .agents/skills/extract-campaign-interactions/scripts/process.py --vault . render --input /tmp/session-work/SESSION/reviewed.json --output /tmp/session-work/SESSION/review.md --queue /tmp/session-work/SESSION/queue.json
```

A targeted correction changes the candidate and therefore its digest; obtain a fresh review request before reassessment. Retain snapshots and reports so one attempt cannot be quietly repeated. `--human` on apply-review is solely for recording an actual human decision. Automated review cannot overwrite human-reviewed targets. High confidence plus automated/human-reviewed status makes critical records ready; medium/low critical records remain in the queue. The CLI cannot prove a semantic review happened: reviewer evidence and execution provenance must be honest.

Render again in the final repository output directory so links are correct for sharing. Do not publish temporary full-transcript copies; link existing source files. Preserve the final `session.json`, readable review, decision evidence and execution findings per sampled session, plus a batch index and reproducible sample manifest. Never silently replace human-edited canonical data.

For published trials, use `extraction.json`, `review-decisions-0.json`, optional `correction-candidate.json` and `review-decisions-1.json`, then `session.json` and `execution.json`. The execution evidence records `fullTranscriptRead` and `correctionAttempts`. These files support this trial's audit; they do not dictate the eventual review UI or storage architecture.

```sh
python .agents/skills/extract-campaign-interactions/scripts/batch.py --vault . --sample /tmp/sample.json --results _sessions/interaction-pilot/v5 --output _sessions/interaction-pilot/v5/README.md --status _sessions/interaction-pilot/v5/batch-status.json --require-complete
```

The batch auditor replays review reports, binds each execution to the sampled campaign/session/source/hash, rejects stale/post-review edits and repeated or incomplete correction sequences, and requires reassessment of changed claims. Correction candidates must preserve the baseline review states; only review decisions can update them. Human-reviewed claims cannot be overwritten or removed by an automated correction. To remove a provisional entity/interaction, include a `removals` array in report 1 with the removed target, reason and source evidence for each removed record. This preserves the decision instead of silently clearing a queue by deleting its entries.

The audit continues across failed sessions and distinguishes reviewed executions from high-confidence critical facts. It renders actionable queue reasons from review decisions. For an individual rendering, add repeated `--report` arguments in chronological order to `process.py render` to show the same reasons.

Reviews open with an entity index, then entity overviews, vault matches and confidence. Provisional review reasons and independent audit observations appear beside the affected entity. Featured quotes and interactions expand on demand; scene context is linked from interactions and collected at the end. The batch index includes a directory linking directly to every displayed entity.

For a presentation-only rebuild of the published v5 pilot, use its explicit review options:

```sh
python .agents/skills/extract-campaign-interactions/scripts/batch.py --vault . --sample _sessions/interaction-pilot/v5/sample.json --results _sessions/interaction-pilot/v5 --output _sessions/interaction-pilot/v5/README.md --status _sessions/interaction-pilot/v5/batch-status.json --review-options _sessions/interaction-pilot/v5/review-options.json --require-complete
```

`sourceRevision` in that options file is a full Git commit SHA. It reads historical transcript bytes without checking out or overwriting sources, still checks the saved hashes and verbatim quotes, and links to that immutable GitHub version. Changed current transcripts are explicitly marked. Without this option, changed sources continue to fail validation. This audits the original evidence; it does not refresh the extraction or promote its confidence.

`excludedEntities` maps session IDs to item IDs and explicit reasons. This pilot uses it solely to omit two ordinary-treasure records from the display under the user's updated rule. The exclusions are disclosed in the review, while canonical JSON, review reports, and the complete critical queue stay intact. It is not a way to delete review decisions or silently clear uncertain records. New extractions should exclude ordinary treasure at extraction time.

This audit verifies the execution record, not the truth of an agent's judgments or the calibration of confidence. Agent review still has to happen. The stateless `apply-review` command only checks that an attempt is 0 or 1; use the batch audit and retain its input chain to check the execution-wide limit.

Checks:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s .agents/skills/extract-campaign-interactions/scripts
```

Historical v3 input is validated/rendered by the compatibility wrapper. Schema v4 is historical and unsupported by the active workflow. Neither is automatically migrated to v5.

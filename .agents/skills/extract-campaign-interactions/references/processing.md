# Session processing evidence

`session-processing-data.json` is the formal companion to schema-v6 `session.json`. It holds processing evidence without duplicating the YAML's canonical metadata or source registry. Its [schema](session-processing-data.schema.json) requires these fields:

| Field | Purpose |
| --- | --- |
| schemaVersion | Processing format version, currently 1; independent of session format version 6. |
| sessionYaml | The same vault-relative manifest reference as the extraction. |
| inputs | Semantic YAML digest and hashes keyed by YAML source identifiers; binds the exact reviewed inputs. |
| stage | prepared, extracted, reviewed or completed; not a claim that all facts are accepted. |
| fullTranscriptRead | Actual complete-read attestation by the extraction agent. Preparation defaults to false. |
| excludedBlocks | Ordered source ranges with a specific reason for each exclusion. An empty array explicitly records no exclusions. |
| metadataFindings | Date conflicts, path repair proposals, participation questions or useful clarifications, with evidence and severity/status. |
| reviews | Tool-appended review reports and candidate/evidence snapshots for replay, including any single correction attempt. |

The YAML digest ignores only `interactionExtraction`, so appending output pointers does not invalidate its own review. It hashes parsed metadata, not comments or formatting. Source fingerprints include the cleaned mapping source when polished text is selected. No report can be applied after those inputs change without a new execution/review.

## Exclusions and coverage

```json
{
  "source": {
    "kind": "transcript",
    "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
    "startUid": "u0001",
    "endUid": "u0012"
  },
  "reason": "Microphone setup and scheduling before play begins."
}
```

Every source UID must be in a scene or an explicitly excluded block before completion. Blocks cannot overlap scenes or each other. A reason is required; never exclude played material just because it contains no eligible entities. Minor chatter/interjections may stay within a scene, particularly when sharing a UID with meaningful speech. Do not manufacture scenes for non-play material solely to satisfy coverage.

The review request includes excluded blocks and unexplained ranges. The rendered review includes linked excluded ranges and reasons. A semantic `scenes` decision reviews this coverage together with the scene division. Validation checks coverage and provenance, not the truth of the reason.

## Metadata findings

Each finding has `id`, `kind` (dateConflict/pathIssue/participation/clarification), `severity` (critical/info), `status` (open/resolved), `reason`, and nonempty `evidence`. Optional `proposedChange` contains a YAML `field` and proposed `value`. Evidence uses transcript ranges, `{yamlField: "drEnd"}`, or `{vaultPath: "People/Name.md"}`.

A clear date contradiction must be critical and cite both transcript and YAML date evidence. Distinguish dates of the current action from flashbacks, hypothetical plans and characters' mistaken statements. A YAML span extending beyond recorded play or resolving an unstated date is not itself a contradiction. Do not manufacture transcript evidence for YAML-only context or generate interactions for unrecorded events.

Missing or incorrect primary transcript paths block preparation and produce concrete YAML proposals through `inspect`; do not mint replacement source paths in extraction JSON. Ancillary stale paths can be recorded as informational proposals while valid retained transcripts are used. Corrections to canonical metadata/source declarations remain proposed until separately authorized. The completion command only appends output pointers.

## Review history and completion

The reviewer receives an `inputDigest` for the candidate and `processingDigest` for the inputs, exclusions and findings. Reports must bind both and include `session` and `scenes` decisions plus all critical entity assessments needed for completion. Each decision needs confidence, reason and evidence. Machine validation is not semantic review.

`apply-review` records the actual reviewer, stage, attempt and output digest, together with the candidate and processing evidence assessed. These are historical snapshots, not separately editable authorities. One correction/recheck is allowed. Corrections preserve review flags until reassessed, protect human decisions, and require explicit removal decisions for omitted entities/interactions. The auditor replays this history instead of trusting a final success flag.

Completion requires full source accounting and semantic review of metadata, entities and scene coverage. A clearly flagged unresolved date conflict can complete with low/medium confidence and remain in the critical queue. It cannot receive high session confidence. Human-reviewed labels require an actual human decision.

The completer uses the transcript pipeline's bundle lock and atomic file writer. It writes derived files before appending YAML pointers and preserves other YAML text. It refuses different existing outputs or a pointer to a different extraction; reprocessing produces a candidate for an explicitly scoped replacement. No narrative recap, beats or transcript work directory is generated.

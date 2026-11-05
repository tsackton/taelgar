# Time assertion records — draft format 0.4

This format defines a single `time-markers.json` inventory whose core record is **source UID → inferred time or duration → evidence**. Preserve each temporal assertion separately. Additional structure exists only to interpret these records and assess YAML dates; never combine markers or compress the extracted evidence. It replaces the experimental time A/B pair for new extractions. It does not migrate old maps or define a chronological event database. Examples below are synthetic schema examples, not session evidence.

## File envelope

Required fields:

- `schemaVersion`: `0.4-time-markers-draft`.
- `provenance`: session ID, session YAML path/SHA-256, transcript path/SHA-256, and captured YAML start/end dates. Use the existing manifest's session identity. Source-local UIDs are not globally unique; session + transcript revision + UID identifies evidence.
- `markers`: source-ordered array of separate temporal assertions defined below; no marker-count or compression target.
- `yamlCheck`: the date assessment defined below.

Optional top-level `limitations` is a string describing concrete source or reading limitations that affect this extraction, such as an unread portion or missing source material. Identify the affected UID range when known and explain the impact. Omit generic disclaimers about source status, self-review, or lack of human approval. Reading the complete transcript remains an extraction requirement, not a `fullRead` field. Do not emit `review`, `readWindows`, or a review-status lifecycle.

Optional `boundaryUncertainties` retains unresolved opening/closing interpretations for later normalization. Omit absent optional fields and empty optional collections. Use null only where explicitly allowed; unknown is never zero. Do not add separate nodes, constraints, chronological projections, or exhaustive rejected-candidate collections.

The provenance keys are `sessionId`, `sessionYaml`, `sessionYamlSha256`, `transcriptPath`, `transcriptSha256`, and `yamlDates: {start, end}`. Dates are ISO strings or null when absent. Resolve the transcript through `transcriptProcessing.artifacts.polishedMarkdown` in the session YAML; the lookup key and transcript processing status are not output fields. A changed transcript or YAML hash requires reinspection. If supplementary sources are actually needed, record their paths/hashes and distinguish their evidence from the current transcript; do not silently import an adjacent session's chronology.

## Marker core

Every marker has:

| Field | Meaning |
| --- | --- |
| `id` | File-local stable reference such as `t01`; not a replacement transcript UID. |
| `source` | `{startUid, endUid}` identifying where this assertion occurs; inclusive, aligned to whole polished turns. Use the original transcript identifiers, not a newly minted UUID. A correction has its own marker at its own source position. This is not an exhaustive event-occupancy span. |
| `reading` | Inferred time or duration in plain language, separate from quotation; explicitly retain uncertainty when no value can be established. Add the structured fields below wherever supported. |
| `evidence` | Nonempty array of `{startUid, endUid, quote}`. Quotes are exact contiguous excerpts from the cited turns. Include question/answer and correction context when needed. Shared-UID turns retain their complete UID boundaries. |

Order markers by `source.startUid`, preserving assertion order within a shared UID. Every temporal assertion gets its own marker, including repetitions, confirmations, and immediate corrections. Multiple assertions within one polished turn retain the same whole-turn source boundaries but have separate IDs and assertion-specific quotations. Do not merge them because their date, interval, event, actor, or source UID is shared.

Supporting evidence can occur earlier or later: a question can clarify an answer, or a later date can support an explicitly labeled inference. That supporting citation does not replace the later assertion's own marker. A bare question with no temporal assertion need not become a marker. Preserve an original claim's value even when corrected; put the new value in a separate marker linked with `revises`. Markers may have only the core fields when the time/duration reading cannot be further structured honestly.

Examples of the required granularity:

| Source assertions | Required records |
| --- | --- |
| Opening “it is morning”; later “it is about ten now” | Two markers at their own source positions; the later clock does not date the opening to 10:00. |
| “You sleep for the night”; later “it is the morning of April 17” | Two markers; the morning marker establishes the reached date and confirms the overnight boundary. Do not count the same boundary twice. |
| “You travel for six days”; separately “it is April 23” | Separate duration and date markers. Do not invent six daily records for the single duration assertion. |
| “It is April 17—sorry, April 18” within one turn | Two markers sharing the turn's UID boundaries; the April 18 marker revises the April 17 marker. |
| “The trip took six days”; later “yes, six days” | Two markers; link `same_interval` when supported so the repeated duration is not added twice. |

## Optional time and duration fields

| Field | Shape and use |
| --- | --- |
| `time` | Time point object: any supported `date: {year, month, day}`, `clock: "HH:MM"` (24-hour local clock), `partOfDay` (e.g. `sunset`), or `relative` object; include `precision` and `basis` as below. Omit unknown date components. |
| `timeRange` | `{start, end}` using time point objects; either endpoint may be null if unknown. Use for an interval asserted as such, e.g. “from noon until sunset.” Never use it to merge separate start/end assertions or replace their markers with a reconstructed interval. |
| `duration` | Quantity object defined below; actual, estimated, or conventional basis must be explicit. |
| `dateBoundaries` | Nonnegative integer only when this marker establishes that many calendar transitions. Not inferred from rest mechanics or YAML end. Overlapping/same-interval markers are not additive. |
| `actors` | Explicit character/group labels when the claim is limited to those actors. Omitted means the shared current-play context, not proof that every character participated. |
| `context` | Omit for current play. Otherwise `flashback`, `reported`, `vision`, or `planned`. A retrospective statement about current-play elapsed time can remain current; statement tense alone does not determine context. |
| `completion` | For an action/interval whose status matters: `completed`, `begun`, `planned`, `interrupted`, or `uncertain`. Estimates are not completed intervals. |
| `note` | Material uncertainty or qualification not already expressed by the reading, structured fields, or basis. No generic extraction instructions. |

Use `reading` to state the interpretation and `basis` to explain support for a structured value. Add `note` only for a remaining material qualification; this applies to relationship notes too. Do not repeat explanations across fields. Keep all separate assertions and their evidence even when their values repeat.

A time point's `precision` is `exact` or `approximate`, relative to what the source establishes. `basis` is a concise string explaining stated, inferred, conventional, or YAML-derived components. For example, a spoken month/day plus YAML year must identify that mixed basis. Do not fill missing components merely because other markers have dates. Do not turn “sunset” into a numerical clock or interpret an ambiguous “six” as 18:00 without contextual support.

`relative` has `relation` (`before`, `after`, or `same_time`), `reference` (a marker ID when available), optional `anchor` (plain description when the reference is not a marker), and optional `offset` (quantity object). Require `reference` or `anchor`; a textual anchor does not mint an event node. For “previous evening,” retain `partOfDay: "evening"` and a relative anchor; do not pretend it is exactly 24 hours earlier. Reference an event boundary precisely in `anchor` when a referenced marker covers an interval.

A quantity has `unit` (`minute`, `hour`, or `day`), `precision` (`exact`, `approximate`, or `vague`), and `basis`. Specify either:

- `value`: a supported number;
- `min` and/or `max`: supported numerical bounds, with `minInclusive` / `maxInclusive` required for each supplied bound; or
- `text`: a vague quantity such as “a few days,” without invented numerical limits.

Examples: `{ "max": 1, "maxInclusive": false, "unit": "hour", "precision": "exact", "basis": "DM says less than an hour" }` preserves a strict bound. A short-rest duration uses `value: 1`, `unit: "hour"`, and `basis: "short-rest convention"`; it is not an independent clock measurement. Distinguish narrated elapsed time from forecasts in `basis` and action status. A corrected forecast can be retained as `context: "planned"` and `completion: "planned"`; evidence of later travel does not make the forecast exact elapsed time.

## Essential relationships only

Optional `relations` is an array of `{type, target}` with an optional `note`; `target` is another marker ID. The source marker's evidence must support the relationship, not merely the two durations independently.

| Type | Meaning from this marker to its target |
| --- | --- |
| `during` | This entire interval is contained within the target interval; adds no separate elapsed time outside it. |
| `overlaps` | Intervals overlap, but full containment is not established. |
| `same_interval` | Both describe the same interval; descriptions may differ or supply complementary evidence. |
| `revises` | This replaces the target's accepted claim. Retain the old marker/evidence; downstream consumers must not use it as an independent accepted advance. Unresolved contradictions are not revisions. |
| `returns_to` | Current narration resumes the context represented by the target after a flashback/vision; does not assert the identical clock time. |

Use one directional link rather than reciprocal duplicates. Do not emit routine before/after edges just to reconstruct chronology; use a time point's `relative` field when the source actually provides such a relation. Different actors do not prove concurrency. Containment and revisions must not cycle; same-interval links need not be transitively expanded.

For a flashback, retain the entry marker with `context: "flashback"` and the relative time when supported. An identifiable return marker uses `returns_to`; without an identifiable return, state the uncertainty. Use flashback context on time claims made inside the scene. A retcon inserting previously unnarrated action does not require `revises` unless it actually supersedes a prior claim. A self-correction always retains separate original and correcting markers, even within one turn. Relationships explain how assertions interact; they never authorize consolidation or deletion of their markers.

Example of actor-specific overlap (assuming `t06` records the supported study interval):

```json
{
  "id": "t07",
  "source": {"startUid": "u0200", "endUid": "u0200"},
  "reading": "Mira completed an hour-long short rest entirely during the study interval.",
  "actors": ["Mira"],
  "duration": {"value": 1, "unit": "hour", "precision": "exact", "basis": "explicit retrospective duration"},
  "completion": "completed",
  "relations": [{"type": "during", "target": "t06"}],
  "evidence": [{"startUid": "u0200", "endUid": "u0200", "quote": "Mira's completed short rest took one hour, entirely during your study."}]
}
```

## YAML date check

`yamlCheck` assesses current play, excluding retrospective scenes. It contains:

- `status`: exactly `matched`, `compatible`, or `conflict`.
- `dateAnchor`: explanation of independently spoken dates versus assumptions taken from YAML, including inherited years.
- `expectedDateBoundaries`: integer difference between valid YAML end/start, or null if unavailable.
- `supportedDateBoundaries`: exact total established for the assessed span, or null when incomplete/ambiguous. Partial counts belong in `explanation`, not this field as a false total.
- `evidence`: marker IDs supporting the assessment.
- `explanation`: concise reason, including missing coverage, contradictions, or applicable boundary uncertainty.

| Status | Required interpretation |
| --- | --- |
| `matched` | Completed extraction supports the whole YAML span without contradiction. A relative span may match conditional on the disclosed YAML start; this does not independently verify its absolute date. |
| `compatible` | No established contradiction, but missing days, uncertain boundaries, incomplete reading, missing YAML dates, or unresolved evidence prevent an exact match. A possible match is not a confirmed match. |
| `conflict` | Supported narration contradicts a YAML date or span under every reasonable evidence-supported boundary reading. A definite contradiction can be reported even if other coverage is incomplete; disclose the limitation. |

Test both narrated dates and elapsed span: matching the number of nights cannot override a contradictory explicit date. Do not sum durations across parallel groups, nested intervals, repetitions, revisions, or flashbacks. An exact span need not have every intervening day narrated individually: an explicit six-day montage can account for six boundaries. Conversely, “no overnight found” in incomplete or loosely framed material does not prove a zero-day span. Never use `drEnd` to supply missing days and then call the result a match. Missing clocks alone do not prevent matching a date span.

### Overnight boundaries and later normalization

YAML normally covers **current-play moments reached in narration**, excluding retrospective scenes. Going to bed ends on that evening's date. Explicitly waking after a completed overnight reaches the next date. Awarding long-rest benefits alone does not establish arrival at morning. Opening rest credit may refer to a night before current play begins. A long rest need not happen overnight at all.

Historical records used more than one boundary convention. Preserve reasonable alternatives rather than silently normalizing them. Each optional `boundaryUncertainties` entry has `boundary` (`start` or `end`), `evidence` (marker IDs), `reading`, and `alternatives` (array of `{reading, date?}`). Supply an ISO `date` only if supported, with its conditional basis in the reading; relative alternatives are sufficient otherwise. Preserve this record even if another independent issue makes the overall assessment `conflict`. With no other contradiction, an unresolved boundary that affects the YAML comparison normally yields `compatible`.

Adjacent sessions may share a morning date or end/start on successive evening/morning dates; neither pattern alone is an error. Cross-session normalization and YAML edits are deferred until separately requested. Do not read every neighboring transcript just to force an answer during this extraction.

## Verification and revision

Check actual JSON parsing; required fields and enum values; numeric bounds and valid date/clock components; unique marker IDs; existing relation and assessment targets; source order; exact quote membership; and full-turn UID boundaries. Review assertion coverage as well as validity: each distinct temporal assertion must retain its own source-positioned marker, including repeated, corrected, and separately stated endpoint claims. A quote retained only as supporting evidence in another marker does not satisfy this requirement. Verify that inferred values apply to the marker's own moment or interval, rather than silently importing another assertion's clock. Review relationship semantics and evidence, not just references; repeated or superseded markers must not inflate elapsed time. Confirm hashes still match, and distinguish complete source reading from semantic certainty. Disclose incomplete reading in `limitations`; it cannot produce `matched`. Check that notes contain material qualifications rather than repeated explanations or generic extraction rules. Preserve human decisions and IDs on revision; recheck the YAML assessment and affected relationships after changed evidence.

This draft specifies the checks but has no general-purpose extractor or schema validator yet. The existing A/B pilot builders are not validators for it. Do not claim their success validates a new-format extraction.

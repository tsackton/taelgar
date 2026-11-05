# Gameplay time markers — draft format 0.5

A marker records an established anchor, advance, or change of narrative time with the passage that supports it. Before turning a summary into a duration, identify the words that advance the scene or establish how long the played action took. The period a report covers can differ from time established for play. Source order lets a reader find the evidence. Gameplay can remain unplaced between markers. The session's played interval determines its YAML assessment.

## Calibration

| Passage | Expected markers |
| --- | --- |
| Dawn. The players plan. Two PCs shop and play out a lunch encounter. The DM later asks the third PC for a roll and summarizes what they learned “over the course of the day.” | Exactly two: dawn and the shoppers' lunch. Omit the planning and roll. Leave the rumor gathering unplaced relative to lunch. An explicit advance to dusk would add a marker. |
| Kenzo recognizes a mesa in the morning light after dreaming of it every night for a week. | Morning on the approach. The dream history supplies neither elapsed session time nor an alternative opening boundary. |
| Alesh describes her eight-hour ride in answer to a distance question. The DM places the meeting at about four. The party later marches for a day. | About four for the meeting, and the party's day of marching. Omit Alesh's previous ride. |
| “You search for a minute.” | One minute of elapsed search time. |
| Play opens on the morning of day 3. The table resolves business on days 1–2, then resumes the morning scene. | Opening anchor, earlier played interval, and return. Activities inside the resolved interval can share its marker. |
| “Two hours later — wait, thirty minutes later.” | One advance of thirty minutes with evidence for both statements. |
| A short rest is awarded after dinner for time already spent talking and eating. | Attach the rest credit to that interval. Count the time once. |
| The party travels six days and arrives April 23. Someone later confirms the journey took six days. | One travel interval can carry its endpoint date. Keep a separately established clock/date for a distinct later moment. |

## File envelope

Required fields:

- `schemaVersion`: `0.5-time-markers-draft`.
- `provenance`: session ID, session YAML path/SHA-256, transcript path/SHA-256, and captured YAML start/end dates. Use the existing manifest's session identity. Source-local UIDs are not globally unique; session + transcript revision + UID identifies evidence.
- `markers`: source-ordered array of accepted gameplay time markers, possibly empty.
- `yamlCheck`: the date assessment defined below.

Optional top-level `limitations` is a string describing concrete source or reading limitations that affect this extraction, such as an unread portion or missing source material. Identify the affected UID range when known and explain the impact. Omit generic disclaimers about source status, self-review, or lack of human approval. Reading the complete transcript remains an extraction requirement, not a `fullRead` field. Do not emit `review`, `readWindows`, or a review-status lifecycle.

Optional `boundaryUncertainties` retains unresolved opening/closing interpretations for later normalization. Omit absent optional fields and empty optional collections. Use null only where explicitly allowed; unknown is never zero. Do not add separate nodes, constraints, chronological projections, or exhaustive rejected-candidate collections.

The provenance keys are `sessionId`, `sessionYaml`, `sessionYamlSha256`, `transcriptPath`, `transcriptSha256`, and `yamlDates: {start, end}`. Dates are ISO strings or null when absent. Resolve the transcript through `transcriptProcessing.artifacts.polishedMarkdown` in the session YAML; the lookup key and transcript processing status are not output fields. A changed transcript or YAML hash requires reinspection. If supplementary sources are actually needed, record their paths/hashes and distinguish their evidence from the current transcript; do not silently import an adjacent session's chronology.

## Marker core

Every marker has:

| Field | Meaning |
| --- | --- |
| `id` | File-local stable reference such as `t01`; not a replacement transcript UID. |
| `source` | `{startUid, endUid}` identifying where the time of this event or interval is first established; inclusive, aligned to whole polished turns. Use the original transcript identifiers, not a newly minted UUID. Later supporting or correcting passages keep their own UIDs in evidence. This is not an exhaustive event-occupancy span. |
| `reading` | Inferred time or duration in plain language, identifying the session event or interval it dates, measures, or connects. Keep it separate from quotation and retain uncertainty when no value can be established. Add the structured fields below wherever supported. |
| `evidence` | Nonempty array of `{startUid, endUid, quote}`. Quotes are exact contiguous excerpts from the cited turns. Include question/answer and correction context when needed. Shared-UID turns retain their complete UID boundaries. |

Order by `source.startUid`, retaining source order within a shared UID. Cite the passage establishing the marker; add focused evidence from elsewhere for a revision, a return, or an inference. Give the accepted value in structured fields. For an unresolved disagreement, preserve the alternatives in the reading and evidence and omit a disputed numeric value. Separate records can share an anchor when they date distinct events.

## Optional time and duration fields

| Field | Shape and use |
| --- | --- |
| `time` | Time point object: any supported `date: {year, month, day}`, `clock: "HH:MM"` (24-hour local clock), `partOfDay` (e.g. `sunset`), or `relative` object; include `precision` and `basis` as below. Omit unknown date components. |
| `timeRange` | `{start, end}` using time point objects; either endpoint may be null if unknown. Use for an interval asserted as such, e.g. “from noon until sunset.” Keep each endpoint at the precision established for that event. |
| `duration` | Quantity object defined below; actual, estimated, or conventional basis must be explicit. |
| `dateBoundaries` | Nonnegative integer only when this marker establishes that many calendar transitions. Not inferred from rest mechanics or YAML end. Count each supported transition once. |
| `actors` | Explicit character/group labels when the claim is limited to those actors. Omitted means the shared current-play context, not proof that every character participated. |
| `context` | Omit for the shared adventure context. Use `flashback` or `vision` for a separately narrated frame when useful. Keep ordinary background and unfulfilled plans out of the inventory. |
| `completion` | For an action/interval whose status matters: `completed`, `begun`, `interrupted`, or `uncertain`. Estimates are not completed intervals. |
| `note` | Material uncertainty or qualification not already expressed by the reading, structured fields, or basis. No generic extraction instructions. |

Use `reading` to state the interpretation and `basis` to explain support for a structured value. Add `note` only for a remaining material qualification; this applies to relationship notes too. Do not repeat explanations across fields.

A time point's `precision` is `exact` or `approximate`, relative to what the source establishes. `basis` is a concise string explaining stated, inferred, conventional, or YAML-derived components. For example, a spoken month/day plus YAML year must identify that mixed basis. Do not fill missing components merely because other markers have dates. Do not turn “sunset” into a numerical clock or interpret an ambiguous “six” as 18:00 without contextual support.

`relative` has `relation` (`before`, `after`, or `same_time`), `reference` (a marker ID when available), optional `anchor` (plain description when the reference is not a marker), and optional `offset` (quantity object). Require `reference` or `anchor`; a textual anchor does not mint an event node. For “previous evening,” retain `partOfDay: "evening"` and a relative anchor; do not pretend it is exactly 24 hours earlier. Reference an event boundary precisely in `anchor` when a referenced marker covers an interval.

A quantity has `unit` (`minute`, `hour`, or `day`), `precision` (`exact`, `approximate`, or `vague`), and `basis`. Specify either:

- `value`: a supported number;
- `min` and/or `max`: supported numerical bounds, with `minInclusive` / `maxInclusive` required for each supplied bound; or
- `text`: a vague quantity such as “a few days,” without invented numerical limits.

Examples: `{ "max": 1, "maxInclusive": false, "unit": "hour", "precision": "exact", "basis": "DM says less than an hour" }` preserves a strict bound. A short-rest duration uses `value: 1`, `unit: "hour"`, and `basis: "short-rest convention"`; it is not an independent clock measurement. Distinguish narrated elapsed time from any supporting forecast in `basis` and action status. Evidence of later travel does not by itself make a forecast exact elapsed time; retain only an established timing constraint and label any inference.

## Essential relationships only

Optional `relations` is an array of `{type, target}` with an optional `note`; `target` is another marker ID. The source marker's evidence must support the relationship, not merely the two durations independently.

| Type | Meaning from this marker to its target |
| --- | --- |
| `during` | This entire interval is contained within the target interval; adds no separate elapsed time outside it. |
| `overlaps` | Intervals overlap, but full containment is not established. |
| `returns_to` | Current narration resumes the context represented by the target after a flashback/vision; does not assert the identical clock time. |

Use one directional link when the source establishes the relationship. `during` and `overlaps` can link distinct, actor-specific intervals. Mark a return only when play resumes an identifiable frame. Keep temporal corrections on the affected marker. A retrospective insertion may add a previously unplayed event while leaving earlier anchors valid. Different speakers, the placement of a roll, and source order alone establish no temporal relationship.

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

`yamlCheck` assesses the adventure interval covered by the session, including downtime, travel, and earlier events established through nonlinear narration. Explain which events belong to that interval; do not restrict it to events after the opening scene or derive it from the earliest/latest dates mentioned. Keep separate historical or vision frames from extending the adventure span without supporting evidence. It contains:

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

Test both narrated dates and elapsed span: matching the number of nights cannot override a contradictory explicit date. Do not double-count parallel groups, nested intervals, repetitions, revisions, or events recounted in flashbacks. Earlier adventure events established retrospectively can contribute to coverage without adding time after the opening scene. An exact span need not have every intervening day narrated individually: an explicit six-day montage can account for six boundaries. Missing coverage is not a contradiction, and “no overnight found” in incomplete or loosely framed material does not prove a zero-day span. Use `supportedDateBoundaries: null` for an incomplete or ambiguous total. Never use `drEnd` to supply missing days and then call the result a match. Missing clocks alone do not prevent matching a date span.

### Overnight boundaries and later normalization

Assess the session's covered adventure interval regardless of narration order. An earlier scene or downtime established later in the transcript can affect its start boundary. Going to bed ends on that evening's date. Explicitly waking after a completed overnight reaches the next date. Awarding long-rest benefits alone does not establish arrival at morning. Opening rest credit may refer to a night outside the covered session interval; establish its role rather than assuming inclusion or exclusion. A long rest need not happen overnight at all.

Historical records used more than one boundary convention. Preserve reasonable alternatives rather than silently normalizing them. Each optional `boundaryUncertainties` entry has `boundary` (`start` or `end`), `evidence` (marker IDs), `reading`, and `alternatives` (array of `{reading, date?}`). Supply an ISO `date` only if supported, with its conditional basis in the reading; relative alternatives are sufficient otherwise. Preserve this record even if another independent issue makes the overall assessment `conflict`. With no other contradiction, an unresolved boundary that affects the YAML comparison normally yields `compatible`.

Adjacent sessions may share a morning date or end/start on successive evening/morning dates; neither pattern alone is an error. Cross-session normalization and YAML edits are deferred until separately requested. Do not read every neighboring transcript just to force an answer during this extraction.

## Verification and revision

Verify that each entry recovers an established time, elapsed interval, or frame shift. Look for omitted advances and clear returns, unsupported ordering across actors, repeated credits for one interval, and background extending the YAML span. Inspect the original evidence for each correction and uncertain interpretation. Verify JSON shape, unique IDs, bound files and hashes, whole-turn ranges, exact quote membership, source order, allowed values, date and quantity bounds, and existing reference targets. Incomplete reading requires a limitation and precludes a matched assessment. The older experimental builders do not validate this format.

## Review table

Show every accepted marker in source order with its time or duration, a brief description of the played event and relevant actors, and its source UIDs. Show corrections as one accepted reading, with the correction citation where useful. Identify any material uncertainty in the YAML assessment.

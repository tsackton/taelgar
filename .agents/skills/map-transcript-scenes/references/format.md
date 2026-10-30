# Provisional scene map v1

One `cleaned/<stem>-scene-map.json` per selected session. This is a processing
artifact. It neither changes the canonical session YAML nor declares acceptance
of the final interaction data. No new source paths or copied session metadata.

| Field | Required | Meaning |
| --- | --- | --- |
| `schemaVersion` | Yes | `1`, the scene-map format, not the session.json version. |
| `sessionYaml` | Yes | Vault-relative path to the authoritative manifest. |
| `inputs` | Yes | Generated fingerprints described below. |
| `scenes` | Yes | Ordered played scenes; may be empty for a discussion-only recording. |
| `contextBlocks` | Yes | Ordered passages outside played scenes; may be empty. |
| `dateValidation` | For new/revised maps | Agent's session-level assessment of YAML dates against transcript evidence. |
| `splitConfidence` | For new/revised maps | One confidence rating and reason for the whole scene/context division. |
| `findings` | No | Material boundary, context, location, or date questions with source evidence. |

`inputs.sessionYamlDigest` hashes parsed YAML as sorted compact JSON (date values
serialized as ISO strings), ignoring only the final `interactionExtraction`
pointer. Formatting changes and appending that pointer do not stale the map.
`inputs.sources` maps the YAML artifact keys for polished text and, when registered,
cleaned UID text to their byte hashes. The optional reduction draft is a reading
view; validating it never makes it the source authority. Restoring its snips does
not change the map's original-source references. A changed canonical source or
semantic YAML context requires a new mapping/recheck, not editing stored hashes.

## Scenes

Each scene requires `index` (positive integer, unique and increasing in source
order) and `source`. It indexes a continuous stay at a meaningful place or movement
along a route, bounded by geographic or in-world temporal changes. Rooms, NPCs,
activity changes, and combat boundaries do not independently divide scenes.
Optional fields retain the existing schema's names:

- `type`: `conversation | exploration | combat | travel`; omit when no useful dominant activity exists. Never split a scene to make this uniform.
- `location`: verified vault-relative note path, or null.
- `locationDetail`: narrative subplace, or null.
- `dateStart`, `dateEnd`: supported ISO in-world dates, or null.
- `time`: supported narrative time such as “after dinner”, or null.
- `aiSummary`: at most 25 words of navigation/summary text.

Location and time context are strongly encouraged during authoring, although
they remain optional in the schema. `location` should meaningfully identify the
scene's setting; a broad containing region is not an automatic fallback.
`locationDetail` can stand alone when no suitable vault page exists. `time` can
use supported broad or relative wording, including estimates carried through
continuous play; exact hours need source evidence. Missing values do not block
validation or require a finding. See the skill's scene-context guidance for
matching and chronology decisions.

No separate title, participant list, entity records, interaction classifications,
or per-scene confidence metadata. Resolve scene dates against YAML and transcript
chronology rather than mechanically copying the session's aggregate endpoints.

```json
{
  "index": 1,
  "source": {
    "kind": "transcript",
    "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
    "startUid": "u0013",
    "endUid": "u0137"
  },
  "locationDetail": "Hunting camp on a mountain slope",
  "aiSummary": "An afternoon at the hunters' mountain camp, including conversation and preparations."
}
```

Ranges are inclusive, contiguous original UIDs in source order. The only supported
source kind is currently `transcript`. Boundaries must respect both complete UIDs
and complete polished turns; a turn combining UIDs cannot be divided between them.
Several turns sharing one UID stay together. No partial-UID alignment is invented.
The range may include unrelated chatter or a table break when play resumes the
same place/time span. Those passages stay inside the single range; no additional
range or overlapping context block is needed. Scene membership alone does not
classify every included passage as in-world action or dialogue.

## Context and findings

A context block requires `source`, `kind` (`recap | loreDiscussion | tableChatter`),
and `aiSummary` (at most 25 words explaining the passage's framing). These blocks
are not final extraction exclusions. Recap and lore material remain available to
entity mapping; even `tableChatter` is a provisional classification. Separate
context blocks cover material outside an ongoing place/time span. Interruptions,
including sustained unrelated chatter and table breaks, remain within the scene
when the same place/time span continues afterward; their length alone is not a
boundary.

The union of scenes and contextual blocks partitions the complete source without
gaps, overlaps, or duplicate coverage. Each collection is independently ordered;
the helper renders their merged source order. Context blocks do not consume scene
indexes. Empty `scenes` requires full coverage by contextual blocks, and vice versa.

A finding requires `kind` (`boundary | context | location | dateConflict`),
`source`, and `reason`. A `dateConflict` additionally requires `yamlFields`, a
nonempty list drawn from `drStart`, `drEnd`, `drStartTime`, `drEndTime`, and
`realWorldDate` (only with independent real-world evidence). Findings
may overlap scenes/context blocks; they annotate evidence rather than covering
additional source. They are questions/contradictions needing attention, not a
second review-status system. Unknown dictionary keys are rejected to catch typos.

The validator emits a critical finding for recorded `dateConflict` entries and a
warning for scene dates outside YAML's span. That warning is not proof of a clear
transcript conflict: inspect whether the scene is a flashback or the date was
assigned incorrectly. It does not reject a longer/clarifying YAML date span.

## Session date validation

This assessment is separate from scene coverage and individual scene dates.
`dateValidation` contains `result`, `reason` (brief explanation and limits), and
`evidence` (an array of existing transcript source references):

- `consistent`: the transcript timeline is compatible with YAML as its calendar
  anchor. Relative elapsed time and transitions suffice; an explicitly spoken
  calendar date is not required. This does not independently confirm every YAML
  value. Requires at least one source range.
- `conflict`: at least one clear discrepancy is recorded in `findings` as
  `dateConflict`. Requires at least one source range. Each conflict supplies its
  affected YAML fields and comparison/correction rationale. An unresolved
  conflict cannot coexist with a `consistent` assessment.
- `insufficientEvidence`: the source cannot meaningfully test the chronology or
  leaves a material timing question unresolved, without a clear contradiction.
  Identify the material uncertainty, such as ambiguous travel duration that could
  exceed the YAML span. An unstated calendar date alone does not qualify. Evidence
  may be empty if there is no usable timeline evidence.

An absent assessment on an older provisional map is reported as `notChecked`.
The reader can still display that map, but the writer requires an explicit
assessment for every new or revised map. `notChecked` cannot be authored as a
completed assessment. Date validation has no confidence score; overall split
confidence is recorded separately.

The assessment is authored by the mapping/review agent, never inferred from
successful mechanical validation. The validator checks its shape, evidence
ranges, and consistency with recorded conflicts; it cannot prove that all date
statements were read or that the temporal reasoning is correct. YAML values are
resolved for display, not copied into the map. Corrected YAML changes the input
digest and requires a fresh evidence-based date assessment.

## Overall split confidence

`splitConfidence` contains `rating: high | medium | low` and a nonempty, brief
`reason` for the session's overall scene/context division. It covers site/route
granularity, place/time boundaries, and contextual framing together, without
per-scene or per-field scores:

- `high`: the overall division is well supported, with only minor alternatives.
- `medium`: usable division with plausible alternative boundaries or context
  assignments needing selective review.
- `low`: material gaps or competing interpretations may substantially change
  the division and need broader review.

The mapping agent authors this after semantic review; successful structural
validation does not generate or establish the rating. Keep it independent of
calendar-date accuracy and location-note matching unless those uncertainties
affect the split. A few defensible extra scenes do not automatically reduce it.
For example:

```json
{
  "splitConfidence": {
    "rating": "medium",
    "reason": "The overnight boundaries are clear; treating the chapel and main house as separate sites is a plausible merge choice."
  }
}
```

New and revised saves require both fields. Legacy maps without the object remain
readable; validation and preview report `rating: notAssessed` without adding it
to the saved map or inferring confidence. `notAssessed` is a display fallback,
not an authorable rating. This is an additive version-1 field; no existing maps
are automatically migrated or re-rated.

## Reading, review, and downstream use

`inspect` reports input metadata and the current map hash without writing.
`show --start-uid ... --end-uid ... [--view auto|draft|polished]` prints readable
source windows. If a collapsed snip crosses a requested window, it displays
polished text for that window instead of misleadingly assigning the entire snip
to one scene. `validate` checks the default map or an explicit `--map PATH`.
`preview` leads with the date assessment, current YAML date values, source links,
and date discrepancies, followed by overall split confidence and its reason,
then the compact scene table and remaining findings. It
prints to stdout and persists no review document. The user-facing handoff follows
the skill's **Review presentation** section: one row per saved scene with place
and date/time context, even when some values are unknown; AI summaries are optional.
Date and time may share a column. For a session occurring on one supported date,
state that date above the table and show only times in the rows.
Do not compress multiple scenes into a narrative group or rely on tool output
alone to deliver the table. `save --proposal - --expect-input-digest DIGEST` validates and
writes the default map from stdin. Use the input digest from the initial `inspect`
to reject inputs changed since reading began. An existing file requires its actual
`--expect-sha256` value, including when revising after a changed input. The writer checks all inputs again under the
shared directory lock and protects sources, symlinks, and hard links.

Existing consumers can reuse these indexes/ranges and retain contextual framing.
They must inspect individual passages before inferring presence, quotations,
events, or exclusions; a scene can include multiple activities and unrelated table
discussion. Downstream NPC or interaction retrieval does not determine these
geographic and temporal boundaries. The [v7 session model](../../check-session-entities/references/pipeline-model.md)
and read-only projection preserve the records and give context blocks their own
indexes. No schema migration or downstream output generation is part of mapping.

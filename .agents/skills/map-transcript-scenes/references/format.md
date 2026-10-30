# Provisional scene map v2

One `cleaned/<stem>-scene-map.json` per selected session. This is a processing
artifact. It neither changes the canonical session YAML nor declares acceptance
of the final interaction data. No new source paths or copied session metadata.

| Field | Required | Meaning |
| --- | --- | --- |
| `schemaVersion` | Yes | `2`, the scene-map format, not the session.json version. |
| `sessionYaml` | Yes | Vault-relative path to the authoritative manifest. |
| `inputs` | Yes | Generated fingerprints described below. |
| `scenes` | Yes | Ordered played scenes; may be empty for a discussion-only recording. |
| `contextBlocks` | Yes | Ordered passages outside played scenes; may be empty. |
| `review` | Yes | Shared `{confidence, status}` for the overall scene/context division and source accounting. |
| `issues` | No | AI-generated concerns, each with a short description and optional transcript evidence. |

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
- `timeStart`, `timeEnd`: supported narrative times at the scene's beginning and
  ending, respectively, or null. Each endpoint is independently optional.
- `aiSummary`: at most 25 words of navigation/summary text.

Location and time context are strongly encouraged during authoring, although
they remain optional in the schema. `location` should meaningfully identify the
scene's setting; a broad containing region is not an automatic fallback.
`locationDetail` can stand alone when no suitable vault page exists. `timeStart`
and `timeEnd` can use supported broad or relative wording, including estimates
carried through continuous play; exact hours need source evidence. Leave an
unknown endpoint absent/null, even when the other is known. Missing values do not block
validation or require an issue. See the skill's scene-context guidance for
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

## Context

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

## AI issues

`issues` is an optional array for specific AI-generated concerns. Omit it, or use
an empty array, when there are no concerns to report. Its sole purpose is to
surface concerns and supporting evidence in a review workflow. Issue presence
does not fail validation or automatically change confidence or review status.
Each issue has:

| Field | Required? | Meaning |
| --- | --- | --- |
| `description` | Yes | Brief, nonempty, single-line explanation of the concern and what needs checking. |
| `evidence` | No | Nonempty array of original transcript `SourceRef` ranges supporting the concern. Omit when a whole-map concern cannot be localized. |

Issues can concern dates, uncertain boundaries, contextual framing, or location
matches. There is no required issue taxonomy, severity, separate date assessment,
or positive validation statement. For a date discrepancy, name the affected YAML
field and explain the source comparison in the description. Keep uncertainty
explicit; a concern does not establish a correction or authorize changing YAML.

Evidence may overlap scenes, context blocks, and other issues. It annotates a
concern rather than adding a coverage bucket. Source ranges still respect whole
turns/UIDs. Unknown keys are rejected. The helper checks shape and source ranges;
it does not author concerns, infer a successful date check, or certify their truth.
An absent issue list is not proof that all potential problems were checked.

Use YAML as the calendar anchor. Its span may extend beyond recorded action, and
an unspoken calendar date or unknown time endpoint alone is not a concern. Check
assigned dates outside the YAML span against source framing before raising an
issue; flashbacks or an incorrect assignment can explain the difference.

## Map review

`review` uses the shared structure, with exactly two required fields:

- `confidence`: `high | medium | low`, for the overall scene/context division and
  source accounting. High is well supported, medium has selective boundary/context
  questions, and low has material gaps or competing divisions.
- `status`: `unreviewed | automatedReviewed | humanReviewed`. Automated review
  requires a distinct semantic pass; human review requires an actual user decision
  on this map. Validation supplies neither.

There is no rating/reason pair or per-scene review field. Keep confidence separate
from date compatibility and note matching unless those uncertainties affect the
division. A few defensible extra scenes need not lower confidence. Review values
are caller attestations; write guards protect inputs and output versions, not
the truth of review claims.

Version 1 maps remain readable, including their legacy scene `time` and optional
`splitConfidence`. New scene records use only `timeStart` and `timeEnd`.
They have no shared review; validation reports `review: null` and preview says
“not recorded”. An old rating does not establish any review status. An intentional
revision must author the shared review after checking evidence and save as v2
with the normal input/output guards. Version 1's `findings` and `dateValidation`
remain readable; previews surface recorded concerns without positive date
assessments or rewriting the file. On revision, consolidate substantive concerns
into `issues` and discard obsolete pass statements. Recheck original speech to
assign separate time endpoints; do not copy or automatically split the old narrative time span.
Never invent values just to migrate a file.

## Reading, review, and downstream use

`inspect` reports input metadata and the current map hash without writing.
`show --start-uid ... --end-uid ... [--view auto|draft|polished]` prints readable
source windows. If a collapsed snip crosses a requested window, it displays
polished text for that window instead of misleadingly assigning the entire snip
to one scene. `validate` checks the default map or an explicit `--map PATH`.
`preview` leads with any AI-generated concerns and their evidence, then YAML
calendar context, map-review confidence/status, and the compact scene table. It
prints to stdout and persists no review document. The user-facing handoff follows
the skill's **Review presentation** section: one row per saved scene with place,
start, and end context, even when some values are unknown; AI summaries are optional.
Each endpoint can combine date and time. If every scene has the same supported
start/end date, state it above the table and show separate Start time / End time
columns. Legacy previews retain the unsplit text in a clearly labeled column.
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

---
name: map-transcript-scenes
description: Map where and when a session takes place from its YAML-registered polished transcript. Divide continuous source ranges by meaningful places and in-world time, preserve UID evidence, and check chronology against the session YAML.
---

# Map Transcript Scenes

Use after `process-transcript`, optionally with a `prepare-interaction-transcript`
draft as a reading view. This stage creates a geographic and temporal index and
checks the session YAML's dates. It does not extract entities, encounters,
interactions, quotes, beats, or recaps. Entity checking runs independently.

## Inputs and output

Follow repository branch/worktree instructions. Resolve one existing
`cleaned/<stem>-session.yaml`. Require valid `realWorldDate`, `drStart`, `drEnd`,
and a registered, locatable polished transcript with complete UID mappings.
Report proposed repairs without editing YAML or guessing another source.
Do not populate the map from beats or recaps; those can be later review hints.

Read [the format](references/format.md). Set `HELPER` to this skill's
`scripts/scene_map.py` and `YAML` to the manifest; substitute their actual paths:

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML show --start-uid u0001 --end-uid u0100
```

Retain the inspected `inputDigest` and existing `mapSha256` for saving. Artifact
paths are bundle-relative. `show` prefers a validated reduction draft when present;
use `--view polished` for original speech. Reading windows expand to whole turns
and UIDs. If a collapsed snip crosses a window, the helper shows polished text.
Report an invalid/stale draft and explicitly select polished view to continue;
do not repair the draft here.

The sole persistent output is `cleaned/<stem>-scene-map.json`. Sources, YAML,
drafts, existing processing files, and final outputs stay unchanged. The helper
uses the shared directory lock and a removed-after-use temporary file for atomic
writes. Do not persist another transcript, review document, or log by default.

## Divide by place and time

Read the entire draft or polished transcript. With a draft, reopen original speech
at every proposed boundary and wherever a snip might hide a place/time transition
or evidence for a claim. Labels are retrieval hints, never evidence. Routine
mechanics wholly inside an established scene need no second exhaustive reading.

A scene is one continuous source span covering a stay at a meaningful site or
movement along a route during a continuous interval of in-world time. Account
for **every UID exactly once** as a scene or contextual block, in source order:

- Split at distinct sites, substantial temporal discontinuities/rests, or separate
  visits after intervening activity elsewhere. Explain boundaries in place/time
  terms; do not target a scene count or token budget.
- Use site/route scale: a dungeon, tower, manor, or continuous journey. Rooms,
  floors, corridors, alleys, and positions on one road are subplace details.
  One city or vault link can still contain distinct sites and visits.
- Keep a continuous stay through conversations, NPC arrivals/departures, searches,
  demonstrations, and combat. Speaker, topic, activity, objective, or stakes alone
  creates no boundary. Brief detours within a site stay together; sustained cuts
  to another group's distinct location/time may need a separate scene.
- Keep a narrated journey together even across several days. Split out a sustained
  stop at a distinct site or a material time discontinuity. Tactical pauses,
  travel-method changes, and roadside events alone do not split a route. A pursuit
  can cross nearby streets, alleys, and fields before reaching a destination.
- Keep chatter and table breaks inside the scene if play resumes the same
  place/time span, regardless of interruption length. Snips and reading windows
  are not boundaries.
- Preserve source order for flashbacks and retroactively declared actions; do not
  reorder into chronology or mistake played flashbacks for recaps.
- Use contiguous inclusive UID ranges, respecting whole polished turns and shared
  UIDs. For a transition inside an indivisible group, choose the nearest defensible
  boundary and record an issue when the imprecision matters.

When a site/route boundary is genuinely ambiguous, modestly favor a few defensible
extra scenes that can later be merged. This tie-breaker never makes rooms, NPCs,
activities, or encounters independent boundaries. Downstream entity/interaction
retrieval does not determine granularity.

Use `contextBlocks` for material outside a continuing place/time span:
`recap` for previously played events, `loreDiscussion` for setting clarification,
postgame discussion or hypotheticals, and `tableChatter` for setup, scheduling,
and unrelated speech. Standalone mixed lore/chatter stays `loreDiscussion`.
Context blocks do not consume scene indexes or overlap scenes. An interruption
inside a continuing stay remains inside that scene.

These classifications are **not extraction exclusions**. In-character planning
belongs to its current place/time span but does not establish a proposed visit.
OOC wording alone does not make a context block, and scene membership does not
turn every included passage into played action or its speakers into participants.

## Locate and date scenes

Only `index` and `source` are required on a scene. Actively seek supported
location/date/time context while leaving unknowns absent/null. An optional dominant
activity `type` and an `aiSummary` of at most 25 words aid navigation; omit a mixed
activity label rather than splitting a scene to fit it.

For `location`, search filenames, names, and aliases and read the candidate note.
Choose a verified vault-relative `.md` path that meaningfully identifies the
setting. A fortress can cover a room within it, but not automatically a nearby
bridge or valley. Use a regional page only when the region meaningfully describes
the scene, not to fill the field. A mentioned place is not a visit. Use
`locationDetail` for subplaces or unmatched settings; it can stand alone. Do not
create notes or force broad links. Final aggregate location review is separate.

For `dateStart`, `dateEnd`, `timeStart`, and `timeEnd`, use YAML as the calendar
anchor and speech for explicit or defensible relative chronology. The time fields
describe the scene's beginning and ending independently; either may be absent/null.
Use text so relative or approximate endpoints remain possible. Carry supported
anchors through continuous play: “after breakfast”, “late morning”, or “afternoon to evening” can
help without an exact hour. Mark estimates as such and widen uncertain spans.
Never divide recording time into invented in-world times. Exact hours need evidence.
Do not copy one known endpoint to the other or mechanically split a legacy `time`
description. Reopen source evidence to assign endpoints; preserve unknowns.

A compatible single-day timeline can support one date on several scenes without
a spoken calendar date. In longer sessions, locate individual scenes by evidence;
do not stamp every scene with session endpoints or fill unexplained days. Preserve
recollections, mistaken claims, and uncertainty. Missing context alone needs no
issue and does not block saving.

## Record AI concerns

Use one optional `issues` array for specific AI-generated concerns about the map.
Its sole purpose is to surface those concerns to a reviewer. Display the concern
and supporting evidence in the review workflow; its presence does not fail
validation or automatically change confidence or review status.
Each entry has a short `description` and optional `evidence: SourceRef[]`. Include
source ranges whenever the concern can be localized; a whole-map concern may
omit them. Do not generate routine success statements, generic caveats, issue
categories, or a separate date-validation result. Omit the block when there are
no material concerns. See [the issue format](references/format.md#ai-issues).

While reading, compare current-date statements, overnight transitions, elapsed
journeys/stays, corrections, and the first/last played moments with YAML. Verify
material discrepancies in original speech, including relevant OOC/closing lore.
Historical/recap dates, future plans, snip labels, and recording timestamps do not
establish current in-world dates. For a date concern, identify the affected YAML
field and the actual comparison in its description. Preserve uncertainty and
propose a correction only when evidence supports it; do not edit YAML.

YAML remains the calendar anchor and may extend beyond recorded action. An
unspoken calendar date or missing scene endpoint alone needs no issue. Record
uncertain travel duration only when it materially questions the mapped timeline.
Question `realWorldDate` only with independent explicit real-world evidence.
Boundary, context, and location concerns use the same issue structure. These are
AI suggestions to inspect, not accepted corrections or extraction exclusions.

## Review and save

Perform a **distinct semantic pass** over both sides of every boundary and each
context block. Merge room/NPC/activity/combat-only splits. Check for lore in
closing chatter, recaps mistaken for visits, and plans mistaken for journeys.
Recheck location links and time anchors, removing forced links and distinguishing
estimates from explicit times. Record only material concerns in `issues`.

Use one map-level `review` with the shared fields `confidence: high | medium | low`
and `status: unreviewed | automatedReviewed | humanReviewed`. It covers the overall
scene/context division and source accounting, not individual scenes. High means
well supported with minor alternatives; medium means selective boundary/context
questions remain; low means material gaps or competing divisions need broader
review. Keep confidence separate from date compatibility and note matching unless
those uncertainties affect the division.

Start `unreviewed`; a distinct semantic pass permits `automatedReviewed`.
Use `humanReviewed` only for actual user review of this map's division, not approval
of YAML dates or the skill. Preserve existing human decisions and reset changed
decisions until rechecked. Validation never assigns confidence or review status.
There is no review `reason` field. Specific concerns belong in optional `issues`.

Author `scenes`, `contextBlocks`, `review`, and optional `issues` in a proposal,
preferably on stdin or in memory:

```bash
python3 -B HELPER --session-yaml YAML save --proposal - --expect-input-digest DIGEST
python3 -B HELPER --session-yaml YAML validate
python3 -B HELPER --session-yaml YAML preview
```

Use the initial inspection digest, not one regenerated to bypass changed inputs.
For an intentional revision, inspect/read the existing map, preserve unrelated
decisions, and add `--expect-sha256 HASH` with its inspected byte hash. New/revised
saves use version 2 and require map review; `issues` remains optional. Version 1
remains readable; missing review displays “not recorded”. Do not invent review
values or infer a status from an old split-confidence rating. The helper validates
and rechecks inputs under lock. Consumers
using scene/context indexes must bind to the map revision; entity UID references
remain independent. See [pipeline integration](../check-session-entities/references/pipeline-model.md).

## Present the review

Lead with any AI issues and their evidence, then map-review confidence and status.
In the **user-facing handoff**, include a compact table with **one row per saved
scene**, in source order. Show Scene, Place, Start, and End, combining each endpoint's
date and time or using separate columns.
Use location links and subplace detail when present, leaving unmatched settings
unlinked and unknown values as “Unknown” or an em dash. If every scene shares
one supported date, state it above the table and show Start time / End time in rows. AI
summaries, activity types, and source UIDs are optional columns.

Keep contextual blocks visibly distinct, interleaved or in a separate table.
Check row count/indexes against the saved map. Never collapse “Scenes 3–7” into
one row; split long tables into consecutive parts instead. Tool output or a JSON
link alone does not deliver the table. Finish with map path, substantive issues,
and review performed. Selective unresolved issues do not require approval of
every scene. Stop before other stages unless requested.

## Maintenance

Requires Python 3.9+ and PyYAML; tests use Python 3.10+.
Run `python3 -B -m unittest discover -s .agents/skills/map-transcript-scenes/tests -v`.

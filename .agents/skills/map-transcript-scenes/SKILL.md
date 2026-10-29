---
name: map-transcript-scenes
description: Map a YAML-registered polished session transcript into contiguous scenes and check timeline compatibility using YAML as the calendar anchor. Preserve UID evidence, distinguish contextual discussion, and surface date conflicts or material timeline uncertainty before later entity and interaction extraction.
---

# Map Transcript Scenes

Use after `process-transcript`, optionally after `prepare-interaction-transcript`.
This stage owns both scene division and the primary evidence-based check of the
session YAML's dates. Date validation is a required outcome of a run, even when
individual scene dates remain unknown. It does not extract entities, interactions,
quotes, beats, or narrative recaps. The Python helper checks structure and date
formats; an agent evaluates the transcript chronology and YAML agreement.

## Inputs and output

Read repository instructions and inspect the branch/worktree. Resolve one existing
`cleaned/<stem>-session.yaml`. Reuse the reduction skill's YAML/source reader;
require valid `realWorldDate`, `drStart`, `drEnd`, and a registered, locatable
polished transcript with complete UID mappings. Report proposed path/date repairs
without editing YAML or guessing another source. Do not read beats or recaps to
generate this map; they are optional evidence for a later review stage.

Set `HELPER` to this skill's `scripts/scene_map.py` and `YAML` to that manifest:

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML show --start-uid u0001 --end-uid u0100
```

`show` prefers a validated interactions draft if present, otherwise polished text.
Use `--view polished` to inspect original speech. Source labels display inclusive
UID ranges without repeating every character offset. Each displayed group ends
at a safe boundary between whole polished turns and whole UIDs. Requested reading
windows expand to those boundaries. The source file and all its mappings remain
unchanged. A stale or invalid draft must be reported; explicitly choose polished
view to continue from the canonical source, without repairing the draft here.

During a session run, the sole persistent output is
`cleaned/<stem>-scene-map.json`. It is provisional processing data, not a new
canonical session/source registry. Preserve all source files, the reduction draft,
YAML, existing processing files, and final extraction. The helper may create a
temporary file beside the map for an atomic write, removing it afterwards; it
uses the existing bundle directory lock. Do not save a second review document,
full transcript copy, or log. Render the compact table on demand.

This first version deliberately stays independently runnable on `main`. Its scene
records use the agreed interaction model's fields. A later integration should
adopt these records into shared processing/final output, not create a competing
second segmentation or quietly change the interaction branch's processing schema.
The [pipeline/model contract](../check-session-entities/references/pipeline-model.md)
defines the concrete v7 session model, including indexed contextual passages.
Assisted review and final interaction generation remain unfinished.

## Map the complete source

Read the entire draft or polished transcript. When using a draft, inspect original
source at each proposed boundary, including the edges of a collapsed combat snip.
Expand inside a snip if it could hide a transition or the evidence needed for a
location, time, or summary claim. Reopen complete polished turns around inline
snips when needed for context. Routine mechanical material wholly inside an
established scene does not need another exhaustive reading. Generated labels are
segmentation hints, never evidence of participants, dates, or outcomes; verify
such claims in the original before using them.

Divide source order into played scenes and contextual blocks, accounting for
every original UID exactly once. A short scene is fine; do not target a scene
count or word/token budget.

- Split meaningful location changes, time skips, departures/returns, and combat
  starts/ends. A narrated journey can be one travel scene across several days;
  split stops and distinct events actually played along the way.
- Keep one ongoing conversation together through topic changes, brief mechanics,
  table jokes, and interruptions. Keep a combat encounter together through turns,
  rounds, and brief dialogue. Neither a snip nor a reading-window boundary creates
  a scene boundary. Later interactions can span multiple scenes.
- Preserve source order even when players return to an earlier moment: a played
  flashback or retroactively declared action is still play, with its own source
  range if needed. Do not reorder it into chronology or confuse it with a recap.
- All ranges are contiguous, inclusive original UID ranges. Do not split a UID,
  invent IDs, or cut through a polished turn containing several UIDs. When a
  transition lies inside such a group, use the nearest defensible safe boundary
  and record a short `boundary` finding if the imprecision matters. Do not edit
  the transcript to make the model easier to fill.

Use separate `contextBlocks` for sustained passages outside played scenes:

- `recap`: recounting previously played events, not a new enactment.
- `loreDiscussion`: postgame clarification, setting discussion, hypothetical
  planning outside play, or references to another campaign. Preserve the framing
  in the short summary; this can be valuable evidence for later entity work.
- `tableChatter`: scheduling, setup, unrelated conversation, and other passages
  with no meaningful setting/play content.

These are accounted passages, **not blanket exclusions from later extraction**.
In-character planning is a conversation scene, even though its proposed events
have not happened. OOC wording alone does not make a contextual block. A brief
clarification inside a conversation stays with it; later entity extraction must
still distinguish a mention or hypothetical from participation. Do not fragment
a whole exchange to isolate every aside. For inseparable mixed contextual
material, retain it as `loreDiscussion`, not `tableChatter`.

## Minimal scene context

Require only `index` and `source` on each scene. Usually add `type` and an
`aiSummary` of at most 25 words; fragments are welcome. These are navigation aids,
not narrative replacements. Type is the dominant activity: `conversation`,
`exploration`, `combat`, or `travel`. Do not infer combat from discussion of a past
battle, or travel from a proposed trip.

Optional `location` is a verified vault-relative note path, including `.md`.
Search filenames/aliases and read the candidate before linking. Do not infer a
visit from a mentioned place. `locationDetail` is the narrative subplace, such as
“hunting camp on the mountain slope”; it can stand alone while the vault anchor
is unknown. Omit uncertain anchors rather than inventing notes or forcing matches.
Entity matching and a reviewed session location list belong to subsequent stages.

Optional `dateStart`, `dateEnd`, and `time` describe the played moment. Use explicit
source dates or defensible relative chronology. Do not stamp every scene with the
session start/end, equate recording time with game time, or fill unexplained days.
The YAML may extend beyond recorded play or clarify an unstated date. That is not
a contradiction. A clear conflicting date gets a `dateConflict` finding with the
source range, affected YAML fields, and a short explanation; do not change YAML
or rewrite speech. Preserve recollections, mistaken statements, and uncertain
timing as such. Unknown values can be omitted or null.

## Validate the session dates

**Use YAML as the calendar anchor.** Check whether the transcript's elapsed time,
transitions, or explicit dates give reason to question the YAML timeline. Relative
chronology can establish compatibility without a spoken calendar date. This is
a session-level check: populated scene dates alone do not demonstrate that the
transcript chronology has been reviewed.

1. While reading, identify explicit current dates, overnight transitions, elapsed
   travel/stays, corrections, and the first/last moments actually played. Check
   original polished wording for these anchors, including meaningful OOC and
   closing discussion. Do not use snip labels, historical anecdotes, future plans,
   recap dates, or recording timestamps as current in-world dates.
2. Reconcile the chronology, including relative intervals and returns to earlier
   moments. Check both session endpoints and any supported time-of-day values
   against `drStart`, `drEnd`, `drStartTime`, and `drEndTime`. Chronological
   constraints can expose a contradiction even when all populated scene dates
   lie within the YAML span. Leave ambiguous durations/endpoints unresolved.
3. Surface each clear disagreement as a critical `dateConflict`, citing source
   ranges and the affected YAML fields. Explain the YAML value versus the
   transcript evidence; include a proposed correction in the reason only when
   justified. A conflict identifies a discrepancy, not automatic authority to
   choose between a mistaken spoken date and mistaken metadata. Do not edit YAML.
4. Record one session-level `dateValidation` assessment: `consistent`, `conflict`,
   or `insufficientEvidence`, with a brief reason and source evidence. See the
   format for meanings. Absence of a conflict is not enough for `consistent`;
   there must be usable timeline evidence, such as afternoon-to-evening progression
   or a rest compatible with the YAML span. A spoken calendar date is not required.
   Missing assessments are visibly `notChecked`, never a pass.

A YAML span may extend beyond the recorded action or clarify dates unstated in
speech. Preserve that context; do not call the extension an error or truncate it
to the earliest/latest extracted scene. `consistent` means compatible with the
available evidence, not independent proof of every endpoint. If the transcript
cannot meaningfully test the timeline, or leaves a material duration/transition
uncertain (for example, travel that might exceed the YAML span), use
`insufficientEvidence` and identify that uncertainty. An unstated calendar date
alone is not insufficient evidence. A continuous afternoon ending around 7pm is
compatible with a single-day YAML span even if nobody names the day.

Calibration examples:

| Transcript evidence and YAML | Assessment |
| --- | --- |
| Continuous afternoon-to-evening play; YAML gives one day; no spoken date. | `consistent`: the observed timeline fits. |
| Travel might take several days, but its duration is unresolved; YAML gives one day. | `insufficientEvidence`: identify the uncertain travel interval. |
| The DM explicitly sets the current date to January 22; YAML gives January 25. | `conflict`: cite the discrepancy without choosing a correction. |

Keep the reason brief and focused on compatibility or the specific problem.
Do not turn an unspoken calendar date into a warning, a request for review, or
a requirement for independent confirmation of the YAML endpoints.

`realWorldDate` is checked for valid format at preflight; only flag
its value when independent, explicit real-world session-date evidence exists.
Never compare it with an in-world date or a relative recording timestamp.

Keep date findings independent of per-scene completeness: a clear date statement
can establish a conflict even when that scene's `dateStart` is omitted. Include
the date assessment in the distinct semantic review pass and lead the handoff
with it. Unresolved date questions do not block saving a provisional scene map,
but later stages must not promote that map to verified session chronology.

## Save, check, and inspect

Read [the format](references/format.md). Author a proposal containing `scenes`,
`contextBlocks`, `dateValidation`, and optionally `findings`. Prefer stdin or in-memory decisions;
the helper supplies source/YAML fingerprints and the manifest reference.

```bash
python3 -B HELPER --session-yaml YAML save --proposal - --expect-input-digest DIGEST
python3 -B HELPER --session-yaml YAML validate
python3 -B HELPER --session-yaml YAML preview
```

Use the `inputDigest` returned by `inspect` when the mapping began; the helper
refuses inputs changed since that inspection. `save` reads JSON on stdin when
given `-`. It validates the entire proposal before writing. Existing maps are
never silently replaced. Read the existing map, retain
unrelated decisions, and supply its inspected byte hash using
`--expect-sha256 HASH` for an intentional revision. Downstream consumers must bind
to the map hash: changed boundaries/indexes invalidate dependent references.

Perform a distinct semantic boundary pass: inspect both sides of every boundary,
check continuity of conversations and combat, and recheck every contextual block
against the original. Look especially for lore in closing chatter, recaps mistaken
for encounters, future plans mistaken for travel, and named places mentioned but
not visited. Review the scene division as a whole, not with per-scene confidence
scores. The validator proves source accounting and structure, not the truth of
scene assignments, dates, or summaries. Do not claim human or automated semantic
review from a passing validation command.

Hand off the date assessment and YAML discrepancies first, followed by the compact
table, map path, other substantive findings, and review actually performed.
Do not require routine human approval of every scene; unresolved
boundaries can remain findings for selective review. Do not run entity mapping or
final session generation unless requested.

## Maintenance checks

Run `python3 -B -m unittest discover -s .agents/skills/map-transcript-scenes/tests -v`.
Tests use synthetic bundles and exercise source accounting, combined/split UIDs,
draft lookup, stale inputs, safe writes, and date conflict reporting. Dependencies
are Python 3.9+ and PyYAML, shared with the existing transcript workflow.

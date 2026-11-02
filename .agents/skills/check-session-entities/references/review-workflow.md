# Entity review and feedback

Use with [the skill](../SKILL.md), [map format](format.md), and repository
`AGENTS.md`. The Obsidian Session review tab lists sessions with entity maps and
provides **Show entities map** and **Review entities**. The first is an editable
row per entity with UID source links and vault links; the second visits entities
that are **not human reviewed**, including high-confidence agent decisions.
Skipping navigates without changing review status. A session stays unreviewed
while any included entity is not `humanReviewed`.

## Durable review JSON

The decision store is `cleaned/<stem>-entities-review.json`, beside the map. It is
created on the first edit or comment, never merely by opening the reviewer. Map
edits immediately update `*-entity-map.json`; downstream readers see the actual
human changes without applying an overlay or importing an export. Entity removal
retains the complete old record in review history. Original sources and YAML stay
unchanged. This workflow does not delete existing maps or historical feedback.

Review JSON v1 has `purpose: session-entities-review`, `sessionYaml`, the current
map's byte `mapSha256`, an append-only `history`, and `feedback`:

- History events have stable `id`, timestamp `at`, `actor` (`human` or `agent`),
  `action`, session-local `entity` (or null for the whole map), optional-text
  `reason`, exact before/after map hashes, and `before`/`after` record snapshots.
  Map regeneration records complete before/after maps. The original confidence
  and actual correction remain available for calibration.
- Feedback records have stable `id`, timestamp, `author`, optional entity ID,
  exact reviewed `mapSha256`, reviewed entity `record` (null for a session comment),
  `comment`, and `status: open | resolved`. Resolution adds `resolution` and
  `resolvedBy`. Resolving feedback never supplies human approval.
- All feedback remains saved, including resolved comments and comments on removed
  entities. Human changes and reasons are calibration evidence even without a
  separate comment. A reason is optional; do not invent one from the correction.

The helper uses the shared session lock and an atomic write-ahead `transaction`
inside review JSON for two-file consistency. If interrupted, the next review
inspection completes that exact transaction only when the current map matches its
before or after hash. Conflicts stop for reconciliation. Do not manually remove
transaction data or rewrite hashes to suppress an error.

## Agent API

`scripts/entity_review.py` reads one JSON request from stdin and returns one JSON
response on stdout. Invoke it from the vault root with `python3 -B`; no shell or
model service runs inside the helper. Resolve the session YAML first. For example:

```json
{"command":"inspect","sessionYaml":"_sessions/demo/demo-001/cleaned/demo-001-session.yaml"}
```

Inspection returns the map, review history/feedback, session identity, UID-resolved
source links, and a token binding the current map bytes, review bytes, session
inputs, and inspected notes. Use that actual token verbatim for writes:

```json
{"command":"resolveFeedback","sessionYaml":"<resolved YAML>","token":{},"feedbackId":"f000001","resolution":"<what changed, supporting evidence, or why no change was appropriate>"}
```

`token: {}` above is only a placeholder. Reinspect after each write; use the token
returned by the latest response. A stale map, feedback file, source, YAML, or
consulted note rejects the write. `entityFeedback` records `comment` and optional
`entity`; `entityUpdate` applies a selected human edit/removal and its optional
`reason`. **Agents must not use entityUpdate to invent human actions.** Agent map
changes use the ordinary guarded `entity_map.py save` workflow below.

For a new vault link, inspect with `notes: ["People/Target.md"]` first. The helper
includes all existing chosen/candidate/evidence notes in that inspection. Evidence
uses `command: evidence`, `entity`, and inspected `mapSha256`, and resolves actual
whole-turn UIDs for transcript or prepared-narrative sources. Editor line numbers
are zero based and temporary; they are never provenance.

## Pick up feedback before mapping

Inspect existing same-session review JSON before revising its map. Discover review
JSONs alongside earlier same-campaign maps when using those maps as context.
Preserve entity IDs, human edits/removals, reasons, and open/resolved feedback.
Compare feedback's record snapshot and map hash with the current record and
intervening history. Old feedback must not silently replay onto a different
record. A removed entity's feedback remains valid evidence of the removal; do
not recreate it under another ID to bypass that decision.

Revisions still require reading the complete current registered source, consulting
full candidate/supporting notes, and the independent semantic pass. Prior maps and
feedback are leads and decisions, not independent source evidence or canon.

Save proposals using the standard helper with both inspected guards:

```bash
python3 -B .agents/skills/check-session-entities/scripts/entity_map.py --session-yaml SESSION_YAML save --proposal - --expect-input-digest INPUT_DIGEST --expect-sha256 MAP_SHA256
```

New maps omit `--expect-sha256`. Inspect every consulted note. Regeneration preserves
review history and rejects modifying/removing a whole human-reviewed record,
creating new human approvals, or recreating human-removed IDs. To reconsider a
human-reviewed record, have the human reopen that record as unreviewed in the
reviewer, then research and save the change. Unchanged human records stay intact.
When registered sources or consulted note evidence change, first retain the
human record’s other fields and reset its status to `unreviewed` through a guarded
save. The prior approval remains in history; changed evidence cannot inherit it.
Passing validation never supplies semantic review status.

## Recalibrate skill based on feedback

Treat this phrase as a request to improve the entity skill from recorded feedback:

1. Discover relevant review files (use the named session/campaign when supplied;
   otherwise inspect the available review JSONs). Read history as well as comments,
   including resolved feedback. Separate human corrections from agent regeneration.
2. Reconcile each example to its reviewed snapshot and intervening history. Identify
   the original judgment, original confidence, human correction, and stated reason.
   Distinguish session-specific facts from a reusable inclusion, identity, importance,
   evidence, or confidence rule. Do not infer a broad rule from an unexplained edit.
3. Update the skill and appropriate references with supported rules and concrete
   calibration examples. Preserve exceptions and uncertainty. Update `SKILLS.md`
   in the same change. This request does not authorize bulk reclassification of maps.
4. Report adopted rules and source review/event IDs; surface conflicting or ambiguous
   feedback as questions. Resolve a specific open comment only after its requested
   guidance change is actually implemented, with a recorded explanation. Human
   corrections in history remain append-only and are not erased or marked consumed.

## Resolve feedback with my help

Treat this phrase as an assisted pass through open feedback:

1. Inspect the selected session(s), sort open feedback by session and stable ID,
   and show one issue with the reviewed entity, exact human comment, relevant
   history, and focused UID passages/vault evidence.
2. Apply clear authorized corrections through guarded map saves. Ask a focused
   question for ambiguous identity/grouping, missing entities, or conflicting
   decisions. A comment is not approval of a guessed correction. Continue independent
   research while awaiting the answer.
3. Revalidate changes and preserve unchanged records. Changed agent records start
   unreviewed until the semantic pass; the agent never promotes them to human
   reviewed. A human decision on one field does not approve newly researched fields.
4. Resolve the feedback ID only after implementing and checking the agreed outcome;
   explain the change/evidence in `resolution`. Leave unanswered issues open.
   Report remaining issues and files changed. Never start later pipeline stages,
   commit, or push without corresponding authorization.

The Obsidian UI saves feedback for this handoff; it does not start an agent.

## Confidence-based calibration

An explicitly requested calibration sample can still select every medium/low
confidence decision plus four uniformly sampled high-confidence decisions per
session, including exclusions, unless another scope is requested. Freeze the
population, source hashes, random seed, and selected identities before presenting
one at a time; do not reroll after feedback. Exclusions are identified by exact
label and complete occurrence references, never mutable array positions. They
have no review-status field in the map schema. Only explicitly reviewed included
records receive `humanReviewed`. Completion of a sample does not make the whole
session human reviewed; the ordinary Obsidian queue still includes every included
entity lacking that status.

## Legacy feedback

The [October 30 export](../../../../_sessions/calibration/entity-mapping-feedback.json)
is historical: its corrections were already applied and its hashes refer to old
maps. Preserve it unchanged. Older exports with `mapSnapshots`, `decisions`, and
`recordReferences` require exact snapshot reconciliation before use. Exclusion
references may use an older single `source`; match them against the original
snapshot, never a later array position. Do not automatically import/replay them.
There is no migration from the old provisional `reviewState` queue; the current
map schema has no such field. Unsupported legacy maps need an intentional guarded
upgrade following the format reference, not silent schema normalization.

## Verify and deliver

Run the entity skill tests when helpers change and `git diff --check`. Test DOM
controls and a real browser preview for UI changes, including table/source/vault
links, every review status, skip, comments, removal, optional reasons, narrow
layout, and failure handling. Do not use actual session writes as tests. Report
changed files, checks, unresolved feedback, and whether a plugin build was installed.

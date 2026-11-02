# Entity review and feedback

Use with [the skill](../SKILL.md), [map format](format.md), and repository
`AGENTS.md`. The Obsidian Session review tab lists sessions with entity maps and
provides **Show entities map** and **Review entities**. The first is an editable
row per entity with inline type/status/role saves, explicit Accept, and reversible
Exclude/Include tables. Details loads source passages and active feedback; the second visits entities
that are **not human reviewed**, including high-confidence agent decisions.
Skipping navigates without changing review status. The queue's Exclude and next
requires a short exclusion reason, saves pending form edits into the archived
record, moves it to the map's excluded list, and advances. Include can restore it. A session stays unreviewed
while any included entity is not `humanReviewed`.

## Durable review JSON

The decision store is `cleaned/<stem>-entities-review.json`, beside the map. It is
created on the first edit, comment, or explicit source-change confirmation,
never merely by opening the reviewer. Map
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

## Included and excluded tables

The map screen has one navigation/reload/status bar and a session/date title.
Transcript and campaign session-note links appear only for existing files. Session
notes resolve through `_scripts/session_note_campaigns.json`, including aliases and
the registered `campaignRoot` / `notePattern`.

The optional entity `confidenceExplanation` contains the agent's one-sentence
explanation of medium/low confidence (and optionally high confidence). It appears
next to the queue badge or in the main map's Details popup. Legacy missing
explanations are identified as missing, never reconstructed by the reviewer.

Inline type, status, and role changes save immediately. Accept marks the row human
reviewed. Exclude asks for a reason of at most 40 words and moves the record into
the map's existing `{label, reason, occurrences}` exclusions array. The review
sidecar's optional `excludedRecords` retains the full entity paired with that
exact exclusion. The map schema remains v4. Include consumes the archived record
and restores its ID, note, flags, and passages as unreviewed, preserving feedback.
Notes needed for restoration must be inspected before the write. Original
exclusions without an archived record require explicit type and importance; the
helper allocates a fresh ID, avoiding current, archived, and historical IDs.

Agent regeneration must retain active human exclusions and cannot recreate their
archived IDs. Only a human Include action reopens such an inclusion decision.
Exclusion and inclusion use the same locked, recoverable transaction as other
edits. They never rewrite source passages, YAML, or canonical vault notes.

## Empty staging notes from the reviewer

The entity-by-entity screen keeps entity feedback but omits session feedback,
agent follow-up instructions, and history; those remain on the main map.
For an unlinked entity, Create staging note asks the human to confirm a name and
shows the target under `Worldbuilding/Staging/<campaign folder>/<name>.md`.
`entity_review_staging.py` reuses an existing short folder when it uniquely matches
the registered campaign name or aliases; otherwise it uses the canonical name.
It rejects unsafe filenames and vault-wide filename/name/alias collisions, then
creates the file exclusively with zero bytes. No template, frontmatter, status
metadata, or content is added: this action explicitly creates an empty note.

`createStagingNote` takes the current `token`, `entity`, human-chosen `name`, and
optional current `changes` limited to label/type (`kind`)/role (`importance`). It
saves those edits, links the empty file, and sets the entity unreviewed, preserving
source evidence. The helper checks inputs again before committing map/history.
Obsidian supplies a `noteIndex` snapshot of all Markdown paths and each cached
frontmatter name/alias list. The helper compares normalized identities in memory
and opens only notes missing cached metadata, avoiding a full vault reopen for
each creation. Calls without an index retain the complete file-based collision
scan. Target-path validation and exclusive creation remain the same.
A failure after file creation retains the note and reports its path. Interrupted
map/history writes recover through the existing transaction; never create a
second note or delete the preserved file as a convenience fix. A stale-token or
collision error before creation leaves all existing notes unchanged.

This is a human UI action, not permission for an agent to create guessed names or
empty stubs during an ordinary mapping run. Existing note-creation workflows keep
their own content, template, and approval requirements.

## Agent API

`scripts/entity_review.py` reads one JSON request from stdin and returns one JSON
response on stdout. Invoke it from the vault root with `python3 -B`; no shell or
model service runs inside the helper. Resolve the session YAML first. For example:

```json
{"command":"inspect","sessionYaml":"_sessions/demo/demo-001/cleaned/demo-001-session.yaml"}
```

Inspection returns the map, review history/feedback, session identity, UID-resolved
source links, and a token binding the current map bytes, review bytes, session
inputs, and inspected note paths. Vault-note contents are not hashed and their
edits do not stale a token. Use that actual token verbatim for writes:

```json
{"command":"resolveFeedback","sessionYaml":"<resolved YAML>","token":{},"feedbackId":"f000001","resolution":"<what changed, supporting evidence, or why no change was appropriate>"}
```

`token: {}` above is only a placeholder. Reinspect after each write; use the token
returned by the latest response. A stale map, feedback file, transcript, or YAML
rejects the write; vault-note content edits do not. `entityFeedback` records `comment` and optional
`entity`; `entityUpdate` applies a selected human edit/removal and its optional
`reason`. `entityUpdate` with `action: exclude` moves the entity using its
40-word-limited `reason` and can include the same pending `changes` as an edit.
Those fields and any new note target are validated before the record is moved;
the archive retains the edits and confidence explanation. `exclusionInclude` selects an `exclusionIndex` bound to
the current token, restoring an archived entity or requiring `kind` and
`importance` for an original exclusion. `evidence` accepts `exclusionIndex` with
the current `mapSha256` to read excluded passages. Inspection returns
`exclusionDetails` with restoration availability and note-inspection paths.
**Agents must not use entityUpdate, exclusionInclude, or createStagingNote to invent human actions.** Agent map
changes use the ordinary guarded `entity_map.py save` workflow below.

For a new vault link, inspect with `notes: ["People/Target.md"]` first. The helper
includes all existing chosen/candidate/evidence notes in that inspection. Evidence
uses `command: evidence`, `entity`, and inspected `mapSha256`, and resolves actual
whole-turn UIDs for transcript or prepared-narrative sources. Editor line numbers
are zero based and temporary; they are never provenance.

## Confirm changed transcript inputs

If the entity map's transcript/session inputs differ, `inspect` returns
`confirmationRequired: true`, `sourceChanges` (names and old/current SHAs),
`session`, and the current guarded `token`, without exposing an editable map.
Show the changes and ask whether to continue with the current transcript. After
explicit human confirmation, submit:

```json
{"command":"confirmSourceChanges","sessionYaml":"<resolved YAML>","token":{}}
```

Use the actual challenge token, never the placeholder above. The helper checks
the current source digest, map hash, and review hash, validates UID evidence, then
updates only the map's input fingerprints using the normal recoverable transaction.
It records a human `confirmSourceChanges` history event with whole before/after
maps, preserves entity decisions/statuses, and returns a fresh inspection. A stale
challenge must be inspected and confirmed again. Source files and YAML are not
rewritten. Agents must not submit this human action without explicit confirmation.

The CLI equivalent is `entity_map.py --session-yaml YAML confirm-sources
--expect-input-digest DIGEST --expect-sha256 HASH`, using the current values from
`entity_map.py inspect`. Ordinary reads/agent saves refuse a changed transcript
until it has been acknowledged. Legacy `inputs.vaultNotes` hashes are ignored on
read and omitted on the next guarded write. Note paths remain validated.

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
Vault-note content changes do not block processing or demote human decisions.
When registered transcript/session inputs change, obtain explicit human
confirmation of the current revision before continuing. Confirmation preserves
the existing decisions/statuses and records the old/current fingerprints; it
does not establish semantic review. Changed entity decisions still need actual
review. Passing validation never supplies semantic review status.

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

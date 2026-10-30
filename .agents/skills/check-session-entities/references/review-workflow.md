# Entity review and feedback handoff

Use with [the entity skill](../SKILL.md), [map format](format.md), and repository
`AGENTS.md`. Those own extraction, calibration, and field rules. This document
covers preparing a review and manually applying exported feedback. It does not
add an HTML renderer, automatic importer, or final interaction generator.

## Prepare from saved maps

1. Inspect branch/worktree and resolve the requested YAMLs. Preserve unrelated
   work; do not switch branches, commit, or push without authorization.
2. Follow the entity skill to read complete polished transcripts, inventory
   referents, and inspect/read candidate evidence. No scene map is required.
3. On revision, retain the old map byte hash and a before-image for comparison.
   Preserve stable entity IDs and accepted human decisions. Confidence, selection,
   identity grouping, and note matching are distinct judgments.
4. Use the guarded helper to save a complete proposal. Inspect every chosen,
   candidate, and supporting note, including unchanged records, and retain the
   full-set input digest. Additions to that evidence set require a new inspection
   and a check for changes to previously read notes.
5. Validate and perform the separate semantic pass required by the skill.

For an intentional revision, the save command needs both guards:

```bash
python3 -B .agents/skills/check-session-entities/scripts/entity_map.py --session-yaml SESSION_YAML save --proposal - --expect-input-digest INPUT_DIGEST --expect-sha256 MAP_SHA256
```

Substitute the actual manifest, initial input digest, and inspected old map hash;
provide proposal JSON on stdin. Omit `--expect-sha256` for a new output. Do not
edit map files directly or change fingerprints to bypass a stale-input error.

## Present a review

The supported general review is the helper's compact preview and on-demand
verbatim evidence:

```bash
python3 -B .agents/skills/check-session-entities/scripts/entity_map.py --session-yaml SESSION_YAML preview
python3 -B .agents/skills/check-session-entities/scripts/entity_map.py --session-yaml SESSION_YAML preview --entity e021
python3 -B .agents/skills/check-session-entities/scripts/entity_map.py --session-yaml SESSION_YAML preview --kind divine
```

Put uncertain/unreviewed decisions first and keep all inclusions and meaningful
exclusions accessible. Show session, stable entity ID, session label, kind, match/
candidates, confidence/status, and UID evidence. Later-identification
flags must remain visible at high confidence. Occurrence does not imply presence.

A saved reviewer is **additional user-requested work**. Render it from the saved
maps rather than extracting a second inventory. There is no committed general
HTML renderer or feedback-import command; the October 2026 calibration used
one-off tooling. Do not assume a pilot HTML file, ZIP, or generator exists in
another checkout. Helper previews are the supported fallback.

If building an offline HTML reviewer, provide:

- Session, kind, confidence, match, later-identification filters, and text search.
- Separate entity/exclusion views and expandable original UID passages.
- Entity actions: **Accept**, **Change / discuss**, **Exclude entity**.
- Exclusion actions: **Keep exclusion**, **Change / discuss**, **Include entity**.
- Per-record comments, per-session missing-entity feedback, map downloads, and
  a separate **Export my feedback** action.

Embed saved data and evidence; escape labels, comments, and transcript text as
text. Browser storage is only a convenience: show when it is unavailable and
instruct the user to export feedback. The browser does not update repo files.
Explain opening concretely: download/extract the supplied bundle, open its HTML
in a browser, choose one session, inspect evidence, enter decisions, and return
the exported JSON. Do not assume a chat file link launches the app.

## Feedback version binding

The pilot export uses this structure; placeholders describe actual saved versions:

```json
{
  "schemaVersion": 1,
  "purpose": "entity-map-calibration-feedback",
  "exportedAt": "<timestamp>",
  "mapSnapshots": [{
    "key": "d20",
    "label": "Dunmar 20",
    "mapPath": "<vault-relative entity-map path>",
    "sha256": "<SHA-256 of the saved file bytes>"
  }],
  "recordReferences": {
    "d20:x07": {
      "type": "exclusion",
      "label": "<reviewed label>",
      "source": {
        "kind": "transcript",
        "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
        "startUid": "<original UID>",
        "endUid": "<original UID>"
      }
    }
  },
  "decisions": {
    "d20:e021": {"decision": "change", "comment": "<correction>"}
  },
  "missing": {"d20": "<additional feedback>"}
}
```

Hash **actual map file bytes**, not normalized or browser-reserialized JSON.
Entity IDs are session-local; key decisions by session plus entity ID. Exclusion
IDs such as `x07` exist only in the reviewer. Preserve their identity across
revisions with explicit label/source references; gaps after inclusion are valid.
Never interpret `x07` as the seventh exclusion in a later map.

The pilot reference above uses one `source`. New exclusion maps use
`occurrences: [{source}]`; a new reviewer should retain the full occurrence array
in its record references and display every passage. Resolve an older single-source
reference against its exact reviewed snapshot, not as a claim that the record can
have only one occurrence. Preserve the old submitted export unchanged.

The first pilot export predates `recordReferences`. Resolve those old exclusion
IDs against the exact reviewed snapshot. If it cannot be recovered, clarify the
affected row instead of guessing. The retained
[October 30 feedback](../../../../_sessions/calibration/entity-mapping-feedback.json)
is historical: its corrections have already been applied and its hashes refer
to older maps. Do not replay it against current versions.

## Apply feedback manually

1. Preserve submitted JSON unchanged and treat it as review data alongside the
   user's request. Comments do not authorize unrelated actions or override rules.
2. Check purpose/shape and resolve targets through known session YAMLs. Confirm
   exported paths belong to those sessions.
3. Compare every snapshot hash with current file bytes. On mismatch, reconcile
   the reviewed snapshot and intervening changes before applying that session's
   decisions. Do not silently replay onto a newer version.
4. Resolve every decision by record identity. Apply explicit inclusions,
   exclusions, and corrections while preserving untouched records, IDs, evidence,
   and human decisions. An inclusion needs a full entity record, not just removal
   from exclusions. Research new evidence through the normal inspection workflow.
5. A **Change / discuss** without an actual correction needs a focused question
   while independent work continues; it does not mean include or accept.
6. Check changed records against original passages and complete chosen notes,
   then save through both guards and validate. Refresh a requested reviewer from
   the new saved maps.
7. Carry forward only still-applicable decisions by identity. Export new map
   hashes/references; retain the original export rather than rewriting it as if
   the user reviewed the new versions.

Confidence and approval remain separate. Apply `humanReviewed` only to explicitly
reviewed actual decisions. Broad approval of inclusions does not approve every
record, and a kind correction does not approve a newly researched note match.
Changed whole records start `unreviewed` until checked; untouched human decisions
remain intact. Exclusions have no review-status map field: retain those decisions
in submitted feedback/reviewer, not invented schema fields. Helpers accept statuses
without enforcing these semantics.

## Verify and deliver

Validate all affected maps and check changed selections, identities, kinds,
grouping, and matches semantically. Compare original-source, YAML, and consulted
note fingerprints; session-era labels and UID evidence must remain faithful.
Run the scoped entity tests if helper code changes and `git diff --check`.

For an HTML change, exercise the real browser interface: filters, evidence,
inclusion/exclusion actions, comments, export, approval carryover, and downloads.
Downloaded map objects must equal saved maps; snapshot hashes must identify their
file versions. Check a narrow viewport and browser errors, not just syntax.

Deliver map paths, applied decisions, unresolved questions, and checks performed.
When a saved reviewer was requested, provide a working download and opening/export
instructions. Do not require approval of every clear entity before completing work.

## Instruction for the next agent

> Read `AGENTS.md`, the entity skill, map format, and this workflow. Review the
> requested maps from their YAML-registered polished transcripts, preserving IDs
> and human decisions. Apply the calibrated selection rules, flag clear later
> identities, and retain session-era labels. Bind feedback to exact map versions,
> resolve records by identity, and save only through inspected input/output guards.
> Validate maps, verify source preservation, and report unresolved questions.
> Create saved reviewers only when requested. Stop before other stages, commits,
> or pushes unless separately authorized.

# Session entity review workflow for agent handoff

Use this workflow to prepare an entity review, collect human feedback, and apply
that feedback to the session maps. It covers the manual review process used for
the six-session calibration on October 30, 2026. The live
[entity skill](../SKILL.md) and [map format](format.md) define extraction behavior
and the accepted fields; read them together with the repository's `AGENTS.md`.

The deliverable is a checked entity map with reviewable evidence. A saved reviewer
is an additional, user-requested artifact. Entity checking reads the complete
YAML-registered polished transcript and does not require a scene map. Stop before
generating interactions or final `session.json` files.

## Start with the repository and original evidence

1. Inspect the branch and working tree. Preserve existing changes and follow the
   repository's authorization rules. Do not switch branches, commit, or push
   automatically.
2. Resolve the requested session YAML. It owns campaign identity, PC roles, dates,
   and transcript registration. Do not build a parallel manifest or PC list.
3. Record the original map hash, when a map exists, and the input fingerprints.
   Retain a before-image of the map for comparison while working. Preserve the
   YAML, transcripts, vault notes, and unrelated outputs.
4. Read the full polished transcript in order, using bounded windows that do not
   truncate output. Build the inventory from that transcript. Existing recaps and
   annotations can be later hints, not substitutes for reading it.
5. Search for candidate pages, inspect their fingerprints before reading them,
   and read the complete notes, including uncertainty and status comments. Keep
   private information out of the review.

Keep three decisions distinct: whether a referent belongs in the inventory, which
identity its occurrences share, and which vault page identifies it. An excluded
object may need inclusion without having a known note match. A clear identity can
have no page and still have high confidence.

## Apply the calibrated selection rules

| Case | Treatment |
| --- | --- |
| Distinct unnamed person | Include when individually identified, even only by a role such as Havdar's lieutenant. Dialogue is not required. |
| Divine identity unknown during play | Use the established divine kind when the identity is clear. Preserve what the session actually says. Delwath's patron is Yezali, a tanshi, and is therefore divine. |
| Clear identity supplied by later material | Choose the supported note, set `identifiedLater: true`, and explain the later name and basis in `reason`. Keep the session's `label` and `names`. |
| Ambiguous identity | Retain plausible `candidates`, an uncertainty reason, and appropriate confidence. A later-identification flag is not permission to force a weak match. |
| Brief concrete item lore | Include it. Recognition of an old elven blade qualifies even if its complete acquisition story is not transcribed. Routine attacks and numerical mechanics alone do not. |
| Distinct community or historical party | Can qualify as an organization without a spoken formal name. Examples include the peaceful desert orcs and the Heroes of the Great War. |
| Being associated with a monument | Check the associated being when its identity or lore is being discussed. Yerkir-Khor qualifies; a bare route label does not automatically identify a personal mention. |
| Party ladder in Dunmari Frontier | Treat as an NPC companion, even during equipment use. Keep the current ladder distinct from destroyed predecessors. This exception does not apply to other campaigns. |

A clear later match may have high confidence. The flag records where the
identification comes from; it does not assert that the characters knew the later
name or nature. Do not add later events to this session or replace its evidence.

For example, these are the identity fields of Dunmar 20's patron record:

```json
{
  "id": "e021",
  "kind": "divine",
  "label": "Delwath's unidentified patron",
  "note": "Gods and Religions/Gods/Tanshi/Meswati/Yezali.md",
  "identifiedLater": true
}
```

This is a field excerpt, not a complete proposal. The actual record also has
`occurrences`, `review`, and the required later-identification `reason`.

## Inspect and save through the helper

Run commands from the vault root. The following example uses Dunmar 20:

```bash
ENTITY_HELPER=.agents/skills/check-session-entities/scripts/entity_map.py
SESSION_YAML=_sessions/dunmar-frontier/dunmari-frontier-020/cleaned/dunmari-frontier-020-session.yaml

python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" inspect \
  --note 'Gods and Religions/Gods/Tanshi/Meswati/Yezali.md'

python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" show \
  --start-uid u0921 --end-uid u0940
```

Repeat `--note` for **every** chosen, candidate, and supporting page consulted for
the complete proposal, including unchanged records when revising an existing map.
Retain the returned `inputDigest` and `mapSha256`. Adding a note requires a new
inspection covering the full evidence set; check that previously read evidence
has not changed. Use `evidenceNotes` for consulted pages that are neither chosen
nor candidate targets.

Author the proposal in a temporary file. It contains `entities`, optionally
`exclusions` and `evidenceNotes`, without the helper-owned envelope. Preserve
existing entity IDs; append new IDs for additions. Every entity needs ordered,
non-overlapping evidence ranges respecting whole polished turns and UIDs.
`reason` is at most 40 words and is required for unlinked, uncertain, and
later-identified records. A record cannot have both a chosen `note` and
`candidates`.

For a new output, save using the inspected digest:

```bash
python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" save \
  --proposal /tmp/entity-proposal.json \
  --expect-input-digest '<inputDigest from inspection>'
```

For an intentional revision, also supply the inspected old output hash:

```bash
python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" save \
  --proposal /tmp/entity-proposal.json \
  --expect-input-digest '<inputDigest from inspection>' \
  --expect-sha256 '<mapSha256 from inspection>'
```

Replace the placeholders with the returned values. Do not bypass these guards by
writing the map directly. The helper checks source and note fingerprints, locks
the session directory, and writes atomically.

## Prepare an easy review

The durable helper supports compact previews and selected evidence:

```bash
python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" preview
python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" preview --entity e021
python3 -B "$ENTITY_HELPER" --session-yaml "$SESSION_YAML" preview --kind divine
```

When the user requests a saved reviewer, render it from the saved maps. Do not
independently extract a second inventory while preparing the display. Show
uncertain decisions first while keeping every inclusion and meaningful exclusion
accessible. For each record, show its session, stable entity ID, session label,
kind, chosen note or candidates, confidence, review status, rationale, and
expandable verbatim transcript passages with UID ranges. Display later-identity
flags even when confidence is high.

The calibration reviewer is a standalone HTML file. Its useful controls are:

- Session, entity kind, confidence, vault-match, and later-identification filters.
- Separate entity and exclusion views, text search, and links to notable decisions.
- Entity decisions: **Accept**, **Change / discuss**, and **Exclude entity**.
- Exclusion decisions: **Keep exclusion**, **Change / discuss**, and **Include entity**.
- A comment field for each record and a missing-entities field for each session.
- Downloads for the saved maps and a separate **Export my feedback** action.

Embed the saved map data and evidence so the HTML works offline. Escape labels,
comments, and transcript text as text; do not execute their contents. Browser
storage is a convenience, not the handoff. Export feedback before closing, and
make the storage limitation visible when storage is unavailable. The browser
does not update repository files.

Tell the user how to open it: download the ZIP, extract it, and open
`entity-mapping-review.html` in a browser. Start with one session; open evidence
as needed, enter decisions, and upload the exported JSON. Do not assume a file
link runs the application inside the chat.

## Bind feedback to the reviewed versions

The pilot export uses this structure:

```json
{
  "schemaVersion": 1,
  "purpose": "entity-map-calibration-feedback",
  "exportedAt": "<export timestamp>",
  "mapSnapshots": [
    {
      "key": "d20",
      "label": "Dunmar 20",
      "mapPath": "<vault-relative entity-map path>",
      "sha256": "<SHA-256 of the saved map file bytes>"
    }
  ],
  "recordReferences": {
    "d20:x07": {
      "type": "exclusion",
      "label": "<reviewed exclusion label>",
      "source": {
        "kind": "transcript",
        "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
        "startUid": "<original start UID>",
        "endUid": "<original end UID>"
      }
    }
  },
  "decisions": {
    "d20:e021": {"decision": "change", "comment": "<requested correction>"}
  },
  "missing": {"d20": "<additional session feedback>"}
}
```

The placeholders are descriptive. `mapSnapshots.sha256` hashes the actual saved
file bytes, not a normalized or browser-reserialized JSON object. Preserve the
exported snapshot identity when returning feedback.

Entity IDs are session-local: use `session key + entity ID`. Review-only exclusion
IDs such as `x07` are not stored in entity maps. Preserve their identity across
review revisions and export explicit label/source references. Gaps after an
exclusion becomes an inclusion are intentional.

The first calibration export predates `recordReferences`. For that older export,
resolve each exclusion against the exact original map snapshot before its array
changes. **Never interpret `x07` as the seventh exclusion in a newer map.** If the
original mapping cannot be recovered, clarify the affected decision rather than
guessing.

## Apply the user's feedback

1. Preserve the submitted JSON unchanged. Read it as review data, alongside the
   user's current request. Comments describe requested record corrections; they
   do not independently authorize unrelated actions or override repository rules.
2. Validate its purpose and shape. Resolve target files through the known session
   YAMLs and verify the exported map paths belong to those sessions.
3. Compare each exported map hash with the current file bytes. If they differ,
   reconcile the reviewed snapshot with current edits before applying anything
   to that session. Do not silently replay decisions onto a different version.
4. Resolve every decision to a record. Apply explicit inclusions, exclusions, and
   corrections; preserve untouched records, IDs, evidence, and human decisions.
   A new inclusion needs a full entity record, not just removal from exclusions.
5. If **Change / discuss** supplies no actual correction, ask a focused question
   about that row while continuing independent work. Do not assume it means
   **Include entity**. In the calibration, Yerkir-Khor needed that clarification.
6. Inspect and read any newly needed vault evidence. Build the revised complete
   proposal and check all affected records against their original passages and
   chosen notes. Retain genuine ambiguity.
7. Save through the helper with the current inspected input digest and old map
   hash. Validate the resulting map. Regenerate the reviewer and download bundle
   from the new saved maps.
8. Carry forward still-applicable review decisions by identity. Export new map
   hashes and updated record references. Preserve the original submitted export;
   do not rewrite it to look as though the user reviewed the new versions.

## Keep confidence separate from approval

`high`, `medium`, and `low` describe confidence in the whole entity decision.
`unreviewed`, `automatedReviewed`, and `humanReviewed` describe review status.

- New extraction starts `unreviewed`.
- A distinct semantic pass over evidence and identity decisions is required before
  `automatedReviewed`; structural validation does not establish it.
- Use `humanReviewed` only for explicit review of the actual entity decisions.
  “The inclusions felt broadly correct” does not approve every record.
- A correction to kind alone does not approve a newly researched note match.
  Retain the corrected kind, but leave the revised whole record unreviewed when
  other decisions have changed and have not been accepted.
- Changed decisions return to `unreviewed` until checked; untouched human decisions
  remain intact. The helper accepts caller-authored statuses and does not enforce
  these review semantics for the agent.
- Exclusions currently have no review-status field in the map schema. Preserve
  their human decisions in the submitted feedback and reviewer; do not invent
  unsupported map fields.

## Verify and deliver

Validate every affected map and perform a separate semantic check of changed
identities, kind, grouping, note matches, and exclusions. Confirm that original
UID evidence and session knowledge have not been rewritten. Compare source,
YAML, and consulted note fingerprints with the before-state.

When helper code changes, run its scoped suite:

```bash
python3 -B -m unittest discover \
  -s .agents/skills/check-session-entities/tests -v
git diff --check
```

For a changed HTML reviewer, exercise the actual interface in a browser: session
and identity filters, evidence expansion, inclusion/exclusion decisions, feedback
export, applicable approval carryover, and map downloads. Check that downloaded
map objects equal the saved maps and that their snapshot hashes refer to the
right file versions. Check a narrow viewport and browser errors. A JavaScript
syntax check alone is insufficient.

Deliver the map paths, a working download for the reviewer, a short account of
applied decisions and remaining questions, and the checks performed. Do not require
the user to accept every clear entity before finishing authorized work.

## Current calibration artifacts

At the end of the October 30 calibration:

| Session | Entities | Exclusions |
| --- | ---: | ---: |
| Dunmar 20 | 27 | 6 |
| Mawar 4 | 23 | 7 |
| Into the Chasm 1 | 18 | 8 |
| Lost in the Feywild 4 | 25 | 6 |
| Dunmar 70 | 32 | 9 |
| Dunmar 120 | 42 | 10 |

There are 167 entities, 46 exclusions, and 11 later-identification flags. The six
maps are beside their session YAMLs under `cleaned/`. The retained review files
in this workspace are:

- `_sessions/calibration/entity-mapping-review.html`: the updated offline reviewer.
- `_sessions/calibration/entity-mapping-feedback.json`: the user's original export,
  bound to the earlier map snapshots; its applicable corrections have already
  been applied. Do not replay it against the revised maps.
- `/workspace/entity-mapping-calibration.zip`: the updated reviewer, six maps, and
  original submitted feedback, plus this handoff document at its repository path.

The HTML is ignored by the repository's `*.html` rule, and the ZIP is outside the
repo. Pass the bundle explicitly when another agent needs those artifacts.
An agent in a different checkout also needs the updated skill and helper changes.
Check that checkout's Git state and helper capabilities before using the maps;
the handoff document alone does not establish which changes are present.

The Python helper is durable repository tooling. The HTML generator and the
feedback-application scripts used for this pilot lived in `/tmp`; there is no
committed general HTML renderer or feedback-import command. Do not assume those
temporary scripts exist in another environment. The self-contained HTML and this
contract can guide a replacement; the helper previews remain the supported
fallback. Final v7 projection keeps the entity core and omits processing-only
fields such as `identifiedLater`.

## Copyable instruction for the next agent

> Read `AGENTS.md`, `.agents/skills/check-session-entities/SKILL.md`, and
> `.agents/skills/check-session-entities/references/review-workflow.md`. Review the
> requested session maps from their YAML-registered polished transcripts, preserving
> existing IDs and human decisions. Use clear later identities with an explicit
> flag while retaining session-era labels. Produce or refresh the requested
> evidence-based review, apply only the supplied record decisions to the matching
> snapshots, and save through the guarded helper. Validate the maps, verify source
> preservation, and report unresolved questions. Stop before interactions, final
> session generation, commits, or pushes unless separately requested.

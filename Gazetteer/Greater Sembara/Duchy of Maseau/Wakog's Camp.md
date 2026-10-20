---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: null}
tags: [place, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: fortified camp
ancestry: orc
created: "1719-08"
destroyed: 1719-12-05
name: "Wakog's Camp"
whereabouts: Duchy of Maseau
dm_owner: none
dm_notes: color
POV: modern
---
# Wakog's Camp
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A temporary camp established by [[Wakog]] in the badlands between [[Cleenseau]] and [[Evis]]. It was destroyed by the [[Heroes of Cleenseau]] in late 1719.

%%^Metadata:names:v1%%
- {"name": "Wakog's Camp", "language": "unknown", "pronunciation": "WAH-kogz kamp", "status": "proposed", "notes": "Complete possessive-name proposal using the still-proposed WAH-kog in [[Wakog]], with English possessive z and ordinary camp. The personal name has initial stress, ah, hard g, and short o; its source language remains unknown."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of the temporary DR 1719 camp and its destruction; the exact destruction date in metadata requires reconciliation with the session chronology.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded the filename identity explicitly in name metadata.
- Added primary name metadata with a proposed pronunciation and its derivation.
- Added the required single-location map skeleton with its unknown locator left blank.
- Recorded the article POV and a persistent temporal-coverage interpretation.

### Validated judgments
- The camp’s founder and defeat are corroborated by [[Wakog]], [[Battle Against Wakog]], and [[Cleenseau - Session 05]]; the destruction-day discrepancy remains open.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement has no established world-map locator in the reviewed evidence. Supply the actual coordinate in the existing `locations` entry, keeping `map: world`; do not infer a hex from nearby places.

- [ ] **Warning — metadata.names_unresolved_status:** Review `WAH-kogz kamp` in `Metadata:names:v1`. Complete possessive-name proposal using the still-proposed WAH-kog in [[Wakog]], with English possessive z and ordinary camp. The personal name has initial stress, ah, hard g, and short o; its source language remains unknown. Accept or revise the complete reading; if accepted, copy it to frontmatter and mark the entry `documented`.

- [ ] **Warning — correctness.cross_note_conflict:** Frontmatter records `destroyed: 1719-12-05`, but the finalized [[Cleenseau - Session 05]] timeline dates scouting to December 5 and the camp attack, prisoner rescue, and victory to December 6; [[Battle Against Wakog]] and [[Wakog]] also use December 6. Confirm whether destruction denotes the decisive attack. If so, use `destroyed: 1719-12-06`; otherwise retain December 5 only with a source explaining the separate event. The existing “late 1719” body sentence does not resolve the one-day conflict.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. Shared campaign records do not establish information remaining only in private material. Retain `color` if useful material remains in memory or other off-vault sources; a human must decide any attestation change.

%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/stub, status/check/name, status/check/lint]
typeOf: road
name: North Road
whereabouts: Chardonian Empire
dm_owner: none
dm_notes: none
POV: 1740s
---
# The North Road
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% major road running north through the coastlands from Chardon %%

%%^Metadata:map:v1%%
locations:
  - {feature: Chardon, map: world, locator: }
  - {feature: , map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for North Road; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Validated judgments
- The missing-pronunciation check was dispositioned as not applicable because this is a plain-English descriptive title or an otherwise obvious ordinary label.

### Open findings
- [ ] **Warning — dm.notes_private_evidence_suspect:** Local-only evidence in [[Dunmar Notes]], [[History of Dunmar]], [[Copper Hills (OneNote)]] is not accounted for by an in-note SECRET link. Review whether `dm_notes: none` remains accurate; do not remove or change the field automatically.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks endpoint 1.locator, endpoint 2.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Warning — status.disposition:** Existing status `status/stub`, `status/check/name` remains in force. Its underlying name, cleanup, review, game-update, stub, or work-in-progress question requires human disposition; the lint did not alter it.
%%^End%%

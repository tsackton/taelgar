---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: canal
name: Mill Channel
whereabouts: North Bank
dm_owner: tim
dm_notes: none
POV: 1740s
---
# The Mill Channel
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Mill Channel is the largest of the canals and waterworks that connects the refineries of the [[Ragwater Basin]] to the [[Chasa]]. It cuts through the [[Bastion Quarter]], passing under the [[North Road|trade road]], and then exits the walls via the [[River Gate North (Chardon)|River Gate]]. From there, it loops west before veering south to reconnect with the [[Chasa]] downstream of the main port and the naval arsenal.

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chasa, map: world, locator: }
  - {role: outlet, feature: Chasa, map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Mill Channel; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.
- Applied high-confidence spelling, punctuation, title, or light-clarity corrections.

### Validated judgments
- The missing-pronunciation check was dispositioned as not applicable because this is a plain-English descriptive title or an otherwise obvious ordinary label.

### Open findings
- [ ] **Warning — dm.notes_private_evidence_suspect:** Local-only evidence in [[Chardon Timeline]], [[Session 125 - DM Notes]] is not accounted for by an in-note SECRET link. Review whether `dm_notes: none` remains accurate; do not remove or change the field automatically.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks source.locator, outlet.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

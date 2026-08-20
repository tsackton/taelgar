---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Kedron
whereabouts: Cedrano
dm_owner: tim
dm_notes: none
POV: 1740s
---
# Kedron
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Kedron is the principal river of the province of [[Cedrano]], flowing through the Kedron valley to the sea at [[Castrella]]. The valley is among the few inhabited stretches of Cedrano’s rugged interior.

%% 
some details about the Great Library Apporia arc impinge on Kedron geography but were never clearly worked out 
See:  [[GL - Session 62 - DM Notes]]  and [[Great Library Session Notes - Arc 5]]
%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Kedron; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Chardonian Greek-loan analogue: hard k, short e, and first-syllable stress. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Kedron, language: Chardonian, pronunciation: KEH-dron, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks source.locator, outlet.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Pergia
whereabouts: Portalia
dm_owner: tim
dm_notes: none
POV: 1740s
---
# Pergia
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Pergia is a small coastal city in [[Portalia]], near the southern entrance to the [[Old Chardon Canal]] on [[Emerald Bay]].

%% no details invented %%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: approximately the DR 1740s. Settlement Reference for Pergia; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Italian analogue: g before i read as j and first-syllable stress. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Pergia, language: Chardonian, pronunciation: PEHR-jah, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — dm.notes_private_evidence_suspect:** Local-only evidence in [[Session 47]] is not accounted for by an in-note SECRET link. Review whether `dm_notes: none` remains accurate; do not remove or change the field automatically.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

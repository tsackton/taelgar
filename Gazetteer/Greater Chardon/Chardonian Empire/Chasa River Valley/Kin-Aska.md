---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/cleanup/metadata, status/check/lint]
typeOf: settlement
typeOfAlias: city
campaignInfo: []
destroyed: 1
name: Kin-Aska
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Kin-Aska
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A former city in the [[Chasa]] river valley, destroyed during the [[Blood Years]] in the [[Battle of Kin-Aska]]. The present-day [[Arendum]] is largely built on the ruins of Kin-Aska.

%% confirm destroyed date with info on the wars in the west after the defeat of Cha'mutte %%
%% confirm pre-Great-War culture here with West Coast notes%%
%% clean up header formatting %%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: approximately the DR 1740s. Settlement Reference for Kin-Aska; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** The mixed Northros/Drankorian context does not establish one language; this is a cautious clear-vowel proposal. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Kin-Aska, language: unknown, pronunciation: kin-AHS-kah, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Warning — status.disposition:** Existing status `status/cleanup/metadata` remains in force. Its underlying name, cleanup, review, game-update, stub, or work-in-progress question requires human disposition; the lint did not alter it.
%%^End%%

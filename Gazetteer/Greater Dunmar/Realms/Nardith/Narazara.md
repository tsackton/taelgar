---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: Abandoned in}
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
ancestry: dwarven
destroyed: 1746
name: Narazara
whereabouts: Yuvanti Mountains
dm_owner: none
dm_notes: none
POV: modern
---
# Narazara
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small mountain village on the upper slopes of the [[Yuvanti Mountains]] that raised goats and sheep. In DR 1746, a sickness killed nearly all animals, and the village was abandoned. 

%%
[[Adrik]]'s home village
%%

%%^Metadata:names:v1%%
- {name: Narazara, language: unknown, pronunciation: "NAH-rah-zah-rah", notes: "Cautious spelling-based proposal: four syllables, open ah vowels, voiced z, and initial stress. The village is dwarven, but no source explicitly identifies the language or pronunciation of this name, so the Dwarvish analogue alone does not establish a name-language assignment.", status: proposed}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective summary of the village before and at its abandonment in DR 1746.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name metadata and a proposed pronunciation.
- Added the required single-location map skeleton, leaving the unknown locator blank.
- Added POV modern and temporal coverage notes for the retrospective account.

### Validated judgments
- The concise article adequately identifies the village, its livelihood, and the cause and year of its abandonment.
- [[Adrik]] independently supports the pestilence and abandonment; it attributes his suspicion of Morgana to Adrik rather than establishing her responsibility.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required world-map entry has no locator. Supply Narazara’s supported world-map position in `- {map: world, locator: }`; the upper slopes of the Yuvanti Mountains do not establish a hex coordinate.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed “NAH-rah-zah-rah” pronunciation in Metadata:names:v1, or replace it. This is a cautious spelling-based reading with four syllables, open ah vowels, voiced z, and initial stress. No source establishes the name’s language or exact pronunciation; its dwarven population alone does not identify the name’s language, so the Tolkien Dwarvish analogue is not treated as exact phonology. Copy an accepted primary pronunciation to frontmatter.
%%^End%%

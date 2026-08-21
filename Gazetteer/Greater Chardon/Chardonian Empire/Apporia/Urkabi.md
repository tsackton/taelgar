---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
displayDefaults: {endStatus: mysteriously vanished in}
tags: [place, status/gameupdate/gl, status/check/lint]
typeOf: settlement
typeOfAlias: village
ancestry: lizardfolk
destroyed: 1737
name: Urkabi
pronunciation: oor-KAH-bee
whereabouts: Portalia
dm_owner: tim
dm_notes: none
POV: "1748"
---
# Urkabi
*(oor-KAH-bee)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small lizardfolk village on the [[Apporia|Apporian Peninsula]], on the [[Zurrua]]. In DR 1737, all the inhabitants of the village, [[Samso|save one]], mysteriously vanished.  

%%
GL Arc 5: launch point for river travel toward Castrella.
[[Samso]]'s home village
Some details of disappearance are developed in [[Great Library Session Notes - Arc 5]] and [[GL - Session 62 - DM Notes|GL - Session 62 - DM Notes]]
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Urkabi", role: "primary", language: "Lizardling", pronunciation: "oor-KAH-bee", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: through DR 1748. Historical settlement snapshot after the disappearance and before the rescued villagers returned in DR 1752.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Validated judgments
- Shared nonpublic comments and Campaign:none material were reviewed; no additional public-safe candidate met the reporting threshold beyond any task below.
- Non-check status disposition: `status/gameupdate/gl` is not assessable pending the open temporal or coverage choice; no status was changed.

### Open findings

- [ ] **Warning — coverage.later_material_change:** Great Library Arc 5 records the rescued lizardfolk returning to Urkabi in DR 1752. Candidate: add a DR 1752 dated passage stating that rescued villagers returned to Urkabi.
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.

%%^End%%

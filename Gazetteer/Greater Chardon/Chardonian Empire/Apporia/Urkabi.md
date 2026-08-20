---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
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

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: through DR 1748. Historical settlement snapshot after the disappearance and before the rescued villagers returned in DR 1752."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Warning — status.disposition:** Existing status `status/gameupdate/gl` remains in force. Its underlying name, cleanup, review, game-update, stub, or work-in-progress question requires human disposition; the lint did not alter it.
- [ ] **Warning — coverage.later_invention:** Great Library Arc 5 records the rescued lizardfolk returning to Urkabi in DR 1752. Candidate: add a DR 1752 dated passage stating that rescued villagers returned to Urkabi.
%%^End%%

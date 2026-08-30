---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1693
gender: female
name: Elbeth
affiliations:
  - {org: Asineau Manor Guard, title: Guardsman}
whereabouts:
  - {type: home, location: Embry}
  - {type: home, location: Asineau}
knownTo: []
dm_owner: none
dm_notes: none
POV: 1710s
---
# Elbeth
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Elbeth, a younger woman, not quite 30. She came to the village from Embry with Lord Valbert, and no one in the village knows her that well. She is aloof and withdrawn most of the time. She has broken off three engagements with various men in the village, and is rumored to spend a lot of her free time watching the lizardfolk in Ganboa, and has been heard to express a desire to see fairies, or elves. Skilled with a sword, the best fighter of the three guards.

%%^Metadata:names:v1%%
- {name: Elbeth, language: Sembaran, pronunciation: el-BET, status: proposed, notes: "Proposed from the southern Sembaran French analogue, treating th as t with stress on the second syllable; an English-influenced EL-beth remains plausible."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1710s portrait of Elbeth as one of Lord Valbert's guards in Asineau; her later state after his flight is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added the explicit name and `knownTo: []`.
- Added persistent name metadata with a proposed pronunciation and recorded a late-1710s POV with its temporal limits.

### Validated judgments
- `Asineau Manor Guard` is clear descriptive relationship text; the absence of a same-named note does not make the affiliation invalid.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `Elbeth — el-BET` from the southern Sembaran French analogue, treating `th` as `t` with stress on the second syllable; an English-influenced `EL-beth` remains plausible. Review the alternatives. If `el-BET` is accepted, copy it to frontmatter and change the entry to `status: documented`; otherwise replace it with the chosen pronunciation while preserving the derivation.
%%^End%%

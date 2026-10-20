---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Houille
pronunciation: oo-yee
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: modern
---
# Houille
*(oo-yee)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village along the [[Auberonne]], south of [[Aslain]] and across the river from [[Peydon]].

%% This exists only to give a location for a minor NPC, [[Piers of Houille]], to have been from. Nothing exists about it otherwise %%

%%^Metadata:names:v1%%
- {"name": "Houille", "language": "unknown", "pronunciation": "oo-yee", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographic identification of the village; the article does not describe its changing market arrangements.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values.
- Added the explicit subject name already supplied by the filename and title.
- Added persistent primary name metadata, preserving existing accepted pronunciations and leaving newly composed pronunciations proposed.
- Recorded the supported article viewpoint and concise temporal-coverage metadata.
- Added the required typed settlement map block with its unsupported position left blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block has a blank `locator` because no supported world-map hex is established in the reviewed evidence. Supply the village's verified position in `- {map: world, locator: <verified hex>}`; the placeholder is a human task, not a coordinate proposal.
%%^End%%

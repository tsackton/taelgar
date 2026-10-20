---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Chaudi
whereabouts: Drankorian Hinterland
dm_owner: none
dm_notes: none
POV: modern
---
# Chaudi
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Chaudi is a large river that flows southwest from the [[Yuvanti Mountains]] to the western edge of the [[Sea of Storms]]. 

%% this is supposed to be a mysterious distant jungle river, known more in myth than fact. some versions of dunmar history have some Samraats claiming the territory between the Chaudi and the Shrev for Dunmar, but it has never been actually settled or controlled and it mostly wild jungle. nothing else about the Chaudi is invented %%

%%^Metadata:names:v1%%
- {"name": "Chaudi", "language": "unknown", "pronunciation": "CHOW-dee", "status": "proposed", "notes": "Cautious spelling proposal: ch as in church, au as ow in cow, final di as dee, and first-syllable stress. No source establishes the name language or an accepted reading; the regional Drankorian and Dunmari analogues do not by themselves identify this name’s origin."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Yuvanti Mountains, map: world, locator: }
  - {role: outlet, feature: Sea of Storms, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographic reference; the visible article identifies the river’s course without dating its formation or adopting the hidden historical possibilities.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Added persistent name metadata and a broadly modern article viewpoint with temporal coverage.
- Added the required typed waterway map entries, with source and outlet features from the visible article; coordinates remain blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both required map locators are blank. Supply verified world-map coordinates for the source and outlet in `Metadata:map:v1`; the prose supports their feature names but does not establish coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `CHOW-dee`: ch as in church, au as ow in cow, final di as dee, and first-syllable stress. This is a cautious spelling reading because no source establishes the name language or a name-specific rule; regional Drankorian and Dunmari guidance does not settle its origin. If accepted, copy `pronunciation: CHOW-dee` to frontmatter and mark the persistent entry `documented`; otherwise revise the proposal and its basis.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
%%^End%%

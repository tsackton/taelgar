---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Freccilia
pronunciation: FREH-chee-lah
whereabouts: Cymea
dm_owner: tim
dm_notes: color
POV: modern
---
# Freccilia
*(FREH-chee-lah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small rushing river in central Cymea, flowing north from the rocky foothills of the [[Mistfold Mountains]] until it joins the [[Ampogio]] south of the [[Plataca Hills]] and east of the [[Latazaro]].

%%^Campaign:dufr%%
The Freccilia is the location of the [[Elemental Forge]], which is located in a cave complex reached via an underground segment of the river. 
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Freccilia","language":"unknown","pronunciation":"FREH-chee-lah","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Mistfold Mountains, map: world, locator: }
  - {role: outlet, feature: Ampogio, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal anchor is established for the visible description.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name and persistent name metadata using the accepted pronunciation.
- Converted the equivalent `Campaign:DuFr` marker to canonical `Campaign:dufr`.
- Added broadly modern temporal metadata and the required source/outlet map skeleton, using the stated source and confluence features.

### Validated judgments
- The river’s course, upland character, and campaign-scoped relationship to the forge are sufficient for this bounded reference entry.
- Confirmed local DM source matches support the existing positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source in the [[Mistfold Mountains]] and outlet at the [[Ampogio]] confluence both lack verified world-map `locator` values. Supply each coordinate as a quoted string in the corresponding `Metadata:map:v1` entry; the prose establishes features but not exact hexes.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Edge of Echoes - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Edge of Echoes - Map Key]]
%%^End%%

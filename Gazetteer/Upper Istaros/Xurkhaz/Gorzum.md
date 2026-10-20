---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: oasis
name: Gorzum
pronunciation: gor-ZOOM
whereabouts: Xurkhaz
POV: modern
---
# Gorzum
*(gor-ZOOM)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Gorzum is a peaceful oasis in central [[Xurkhaz]].

%%^Metadata:names:v1%%
- {name: Gorzum, language: Free Orcish, pronunciation: gor-ZOOM, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern identification of the oasis and its central location in Xurkhaz; no narrower temporal state is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported temporal metadata and the required settlement map skeleton.

### Validated judgments
- [[Xurkhaz]] corroborates the central oasis identification. The documented name entry is preserved; the concise identification performs the note’s bounded reference role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed skeleton, but `locations[0].locator` is blank. Supply a verified world-map locator in `{map: world, locator: <verified locator>}`; no coordinate is established by the consulted text sources.
%%^End%%

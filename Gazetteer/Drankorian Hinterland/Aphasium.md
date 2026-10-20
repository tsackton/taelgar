---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
name: Aphasium
pronunciation: ah-FAH-see-um
whereabouts: Drankorian Empire
POV: modern
---
# Aphasium
*(ah-FAH-see-um)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Aphasium was a prosperous town in the [[Drankorian Empire]], not far from the capital.

%%^Metadata:names:v1%%
- {name: Aphasium, language: Drankorian, pronunciation: ah-FAH-see-um, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective identification of an ancient Drankorian town; the date of its prosperity and its later fate are not specified.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported temporal metadata and the required settlement map skeleton.

### Validated judgments
- The documented name and pronunciation are preserved. The short identification is sufficient for a minor ancient town; the sources do not establish a precise map position or later fate.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed skeleton, but `locations[0].locator` is blank. Supply a verified world-map locator in `{map: world, locator: <verified locator>}`; no coordinate is established by the consulted text sources.
%%^End%%

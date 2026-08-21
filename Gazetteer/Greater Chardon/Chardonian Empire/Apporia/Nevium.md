---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
population: 5300
name: Nevium
pronunciation: NEH-vee-oom
whereabouts:
  - {type: secondary, location: Apporia}
  - {type: primary, location: Portalia}
dm_owner: tim
dm_notes: important
POV: modern
---
# Nevium
*(NEH-vee-oom)*
>[!info]+ Information  
> pop. 5,300  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Nevium is a bustling port city and the provincial capital of [[Portalia]], built on pilings above the salt marshes along the [[Gulf of Chardon]] coast, about 10 miles east of the [[Old Chardon Canal]]. Completely destroyed in DR 1589 during the [[War of the Dark Rift]], Nevium was rebuilt in early DR 1600s and grew quickly into a thriving port after the [[Old Chardon Canal]] was reopened under Chardonian control in DR 1619. While the sheltered harbor and productive fishing grounds have supported settlements in the marshes around Nevium for a long time, the city itself largely dates to the first half of the DR 1600s. 

Nevium is a prosperous city. In addition to the productive fisheries, and alchemical ingredients and other marsh products, the city benefits tremendously from the nearby [[Old Chardon Canal]]. The [[Windcallers]], who guide ships through the canal, are based here. Nevium is also where tax revenues from canal transits are collected, which provide significant wealth to the city, and support a large official Chardonian governmental presence.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Nevium", role: "primary", language: "Chardonian", pronunciation: "NEH-vee-oom", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern portrait of prosperous Nevium after the canal reopened in DR 1619; the city's DR 1589 destruction and early-1600s rebuilding are historical background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Validated judgments
- Newer-source candidates were reviewed; no additional material change beyond the open coverage tasks below was identified.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.

%%^End%%

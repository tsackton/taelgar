---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Lunacosta
pronunciation: LOO-nah-koh-stah
whereabouts: Western Cymea
dm_owner: none
dm_notes: none
POV: modern
---
# Lunacosta
*(LOO-nah-koh-stah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Lunacosta is a coastal market town in [[Western Cymea]], located at the mouth of the [[Serrania River]] on the [[Western Gulf]]. Its harbor makes it a natural gathering point for river traffic and travelers moving between the coast and the roads inland.

The town is modest but active by local standards, with inns and markets that draw farmers, fishers, sailors, and visitors from the surrounding countryside.

%%^Metadata:names:v1%%
- {"name": "Lunacosta", "language": "unknown", "pronunciation": "LOO-nah-koh-stah", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and market-town function; incidental campaign visits do not require a narrower speaking position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, recorded the existing accepted pronunciation in primary name metadata, and added a broadly modern temporal frame.
- Added the required typed single-location map skeleton without inventing coordinates.

### Validated judgments
- The coastal market-town account and its harbor setting are supported by [[Serrania River]] and the shared [[Background - LL]]; incidental traveler captures do not require a campaign-history section here.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required world-map entry has a blank `locator`. Supply the verified world-map coordinate for Lunacosta in the existing `Metadata:map:v1` block. Its river-mouth location is established, but no coordinate is supplied by the reviewed text; do not guess one from regional geography.
%%^End%%

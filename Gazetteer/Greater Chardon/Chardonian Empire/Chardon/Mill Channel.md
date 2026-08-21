---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: canal
name: Mill Channel
whereabouts: North Bank
dm_owner: tim
dm_notes: none
POV: modern
---
# The Mill Channel
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Mill Channel is the largest of the canals and waterworks that connects the refineries of the [[Ragwater Basin]] to the [[Chasa]]. It cuts through the [[Bastion Quarter]], passing under the [[North Road|trade road]], and then exits the walls via the [[River Gate North (Chardon)|River Gate]]. From there, it loops west before veering south to reconnect with the [[Chasa]] downstream of the main port and the naval arsenal.

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chasa, map: world, locator: }
  - {role: outlet, feature: Chasa, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Mill Channel", role: "primary", language: "Common", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and industrial use of the channel; no construction date or later change to its route is described.
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

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: source.locator, outlet.locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.

%%^End%%

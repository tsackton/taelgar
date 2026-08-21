---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint, status/check/ai]
typeOf: waterway
typeOfAlias: brook
name: Cedar Brook
whereabouts:
  - {type: primary, location: Alta Tonaro}
  - {type: secondary, location: Yeraad Watershed, startFilter: r}
dm_owner: none
dm_notes: none
POV: modern
---
# Cedar Brook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small tributary of the [[Silverflood]], flowing north from the [[Chataan Mountains]].

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chataan Mountains, map: world, locator: }
  - {role: outlet, feature: Silverflood, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Cedar Brook", role: "primary", language: "Common", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography of Cedar Brook's course from the Chataan Mountains to the Silverflood. Chalyte mining resumes in the surrounding region in DR 1749 and dramatically changes Alta Tonaro, without any established change to the brook's course.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: source.locator, outlet.locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.

%%^End%%

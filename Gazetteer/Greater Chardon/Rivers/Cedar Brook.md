---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T17:36:36-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
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
- None.

### Validated judgments
- Cedar Brook is a plain Common descriptive name and does not require a pronunciation.
- The required `dm_notes` evidence review found no matching local sources. Newer [[Alta Tonaro]] material corroborates the brook's relationship to the Silverflood without establishing a change to its course.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet entries in `Metadata:map:v1` identify the [[Chataan Mountains]] and [[Silverflood]], but both `locator` values remain blank. Add the verified world-map hex for each endpoint when those coordinates are established.
%%^End%%

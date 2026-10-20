---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Holling Brook
whereabouts:
  - {type: primary, location: Sembara}
  - {type: secondary, location: Wistel-Enst Watershed}
POV: modern
---
# Holling Brook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Holling Brook is a small tributary of the [[Wistel]], joining the river between [[Gowerbourne]] and [[Wisford]]. It winds through pasture and hay meadows, shaded in places by willows, and spills across the low ground near its mouth during spring floods.

%%^Metadata:names:v1%%
- {name: Holling Brook, language: Common, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Wistel, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography; no narrower dated state is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded a broadly modern article POV and persistent temporal-coverage guidance.
- Added typed source/outlet map entries, leaving unestablished coordinates blank.

### Validated judgments
- The name has an obvious ordinary English reading and needs no pronunciation guide; this does not remove the name-block requirement.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet `locator` values remain blank in the required map block. The reviewed direct sources do not establish verified world-map coordinates. Fill each existing typed entry with its verified coordinate as a quoted string; retain its source/outlet role and do not infer a hex from the broader whereabouts.
%%^End%%

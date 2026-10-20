---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Kezhur
pronunciation: keh-ZHOOR
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
# Kezhur
*(keh-ZHOOR)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


The Kezhur is an eastern tributary of the [[Istaros]], joining it near the northern border of [[Xurkhaz]]. Its confluence marks the transition between the upper Istaros and the middle reach known as the Drogar.

%% not yet mapped - would enter Istaros around northern border of Xurkhaz%%

%% Naming discussion: [[2026-08-04 - Northern Forest Hills and River Names]] proposed these Orcish names for the unmapped river entering the Istaros from the east just north of Xurkhaz:
Sorkun (SOR-koon)
Kezhur (keh-ZHOOR)
Morzuk (MOR-zook)
No strong preference was expressed for the Xurkhaz names.
%%

%%^Metadata:names:v1%%
- {name: Kezhur, role: primary, language: Free Orcish, pronunciation: keh-ZHOOR, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Istaros, map: world, locator: }
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
- The existing documented Free Orcish name and pronunciation are preserved. The independent human `status/check/name` tag is preserved and is not used to infer a name-metadata defect.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet `locator` values remain blank in the required map block. The reviewed direct sources do not establish verified world-map coordinates. Fill each existing typed entry with its verified coordinate as a quoted string; retain its source/outlet role and do not infer a hex from the broader whereabouts.
%%^End%%

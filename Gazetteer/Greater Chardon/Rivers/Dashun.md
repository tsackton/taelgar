---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
tags: [place, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Dashun
pronunciation: DAH-shoon
whereabouts: Chardonian Empire
dm_owner: none
dm_notes: none
POV: 1700s
---
# Dashun
*(DAH-shoon)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A minor river in the [[Coastlands]], south of the [[Chasa]], flowing from the [[Chardon Hills]] to the [[Gulf of Chardon]].

%%^Metadata:names:v1%%
- {name: Dashun, role: primary, language: Old Northros, pronunciation: DAH-shoon, meaning: warm spring, derivedFrom: dāšûn, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chardon Hills, map: world, locator: 13.07.F16}
  - {role: outlet, feature: Gulf of Chardon, map: world, locator: 13.07.C18}
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: broadly the DR 1700s. The note describes a stable river course and does not depend on a campaign-era event or changing political condition."
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **suggestion — `status.name_review_disposition`:** The pronunciation, language, meaning, and source form are now documented, so `status/check/name` appears to have no remaining work. A human may remove `status/check/name`; the linter is not authorized to remove non-lint status tags.

### Applied changes

- Added the explicit name, `POV: 1700s`, current article/name metadata, and changed both `13.07.*` map locators from `unregistered` to the required `world` map.

### Validated

- The source and outlet coordinates now satisfy the world-hex rule, and the stable geographic description fits the broad DR 1700s viewpoint.
%%^End%%

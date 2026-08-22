---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T19:01:27-04:00"
lintVersion: "3.4"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Zurrua
pronunciation: TSOO-roo-ah
whereabouts: Portalia
dm_owner: none
dm_notes: none
POV: modern
---
# Zurrua
*(TSOO-roo-ah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% west of canal, unmapped, minor %%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Zurrua", role: "primary", language: "Chardonian", pronunciation: "TSOO-roo-ah", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern geographic reference; the Silver Tempests' DR 1748 journey downriver from Urkabi is a dated campaign event rather than the article's speaking point.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Reassessed the article viewpoint, changed `POV` from `1748` to `modern`, and revised `povNotes:v1`; the DR 1748 journey is a dated event rather than the speaking point of the otherwise broad geographic reference.

### Editorial assessment
**Underdeveloped**. The visible note has no public article text. Its central missing dimension is a basic account of the established geography: the Zurrua is a minor river in [[Portalia]], west of the [[Old Chardon Canal]], with [[Urkabi]] near its source. This is a source-grounded coverage gap; the river's explicitly minor role does not support a separate invention-based development finding. The unknown map endpoints are a separate metadata task.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Samso]] and [[Urkabi]] establish that the Zurrua is a minor river west of the [[Old Chardon Canal]], with the lizardfolk village of Urkabi near its source, while [[Great Library Session Notes - Arc 5]] records the [[Silver Tempests]] traveling downriver and camping along it in DR 1748. None of this appears in visible prose. Candidate: add "The Zurrua is a minor river in [[Portalia]], west of the [[Old Chardon Canal]], with the lizardfolk village of [[Urkabi]] near its source. In DR 1748, the [[Silver Tempests]] traveled downriver from Urkabi on a magically summoned boat and camped along the river."
- [ ] **Warning — metadata.map_location_missing:** The waterway map record has blank `source.locator` and `outlet.locator` values. Fill them only from an authoritative map; do not guess coordinates.

%%^End%%

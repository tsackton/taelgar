---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/cleanup/metadata, status/check/lint]
typeOf: settlement
typeOfAlias: city
destroyed: 1555
name: Kin-Aska
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: modern
---
# Kin-Aska
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% confirm destroyed date with info on the wars in the west after the defeat of Cha'mutte %%
%% confirm pre-Great-War culture here with West Coast notes%%
%% clean up header formatting %%

A former city in the [[Chasa]] river valley, destroyed during the [[Blood Years]] in the [[Battle of Kin-Aska]]. The present-day [[Arendum]] is largely built on the ruins of Kin-Aska.


%%^Metadata:names:v1%%
- {name: Kin-Aska, role: primary, language: unknown, pronunciation: kin-AHS-kah, status: proposed, notes: Cautious clear-vowel reading; the mixed Northros and Drankorian context does not establish one source language.}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the ancient city's destruction in DR 1555 and the present-day settlement of Arendum on its ruins.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.

### Validated judgments
- Shared nonpublic comments and Campaign:none material were reviewed; no additional public-safe candidate met the reporting threshold beyond any task below.
- Non-check status disposition: `status/cleanup/metadata` is not assessable because they record human editorial intent; no status was changed.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Kin-Aska — kin-AHS-kah` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T14:57:54-04:00"
lintVersion: "3.0"
tags: [place, status/cleanup/metadata, status/check/lint]
typeOf: settlement
typeOfAlias: city
campaignInfo: []
destroyed: 1
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

A former city in the [[Chasa]] river valley, destroyed during the [[Blood Years]] in the [[Battle of Kin-Aska]]. The present-day [[Arendum]] is largely built on the ruins of Kin-Aska.

%% confirm destroyed date with info on the wars in the west after the defeat of Cha'mutte %%
%% confirm pre-Great-War culture here with West Coast notes%%
%% clean up header formatting %%

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

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `kin-AHS-kah` as a cautious clear-vowel reading because the mixed Northros and Drankorian context does not establish one source language. If accepted, add `pronunciation: kin-AHS-kah` to frontmatter and change the entry to `status: documented`; otherwise revise the proposal.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map block has no locator. Fill the existing blank `locator` from the authoritative map; do not guess a coordinate.
%%^End%%

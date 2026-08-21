---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Erlona
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: 1748
---
# Erlona
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% incorporate notes from OneNote %%

Erlona is the capital of the Chasa Valley province, a rich and powerful province given the agricultural wealth of the valley. This far upriver, there is less wine, but the land is fertile pasture with many cattle and dairy farms.

%%SECRET[v2:c1ffae5c3746bb8f11e475b402da61e4]%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Erlona", role: "primary", language: "Chardonian", pronunciation: "ehr-LOH-nah", notes: "Italian analogue: open vowels and penultimate stress.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of Erlona as the prosperous provincial capital of the Chasa Valley; earlier and later civic conditions are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Validated judgments
- Newer-source candidates were reviewed; no additional material change beyond the open coverage tasks below was identified.
- Shared nonpublic comments and Campaign:none material were reviewed; no additional public-safe candidate met the reporting threshold beyond any task below.
- Non-check status disposition: `status/cleanup/text` is not assessable because they record human editorial intent; no status was changed.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** Session 50 establishes Erlona as a substantial city with a large coliseum; the visible prose still omits the confirmed landmark. Candidate: add a sentence identifying the large coliseum as a prominent landmark, while leaving unplayed details in private material.
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Erlona — ehr-LOH-nah` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Paisa
whereabouts:
  - {type: primary, location: Northern Provinces}
dm_owner: none
dm_notes: none
POV: modern
---
# Paisa
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village on the northwestern shore of [[Lake Valandros]]. 

%% Great Library

Birthplace of [[Scordith]], who lived here until age six before being sent to a monastery in the hills.

%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Paisa, language: unknown, pronunciation: PIE-sah, notes: cautious spelling-based reading; no language or name-specific pronunciation source was found, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the village's location and scale are not tied to a narrower date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added the required settlement map skeleton with its unknown locator left blank.
- Added a minimal name entry with a spelling-based pronunciation proposal.
- Added `POV: modern` and a persistent temporal-coverage note.

### Validated judgments
- The spelling-based pronunciation is only a proposal because no language or name-specific pronunciation source was found.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required world-map locator is blank. Replace the blank `locator` with Paisa's verified world-map coordinate.
- [ ] **Warning — metadata.names_unresolved_status:** `PIE-sah` is a cautious spelling-based proposal for Paisa. Accept it by adding `pronunciation: PIE-sah` to frontmatter and changing the name entry to `status: documented`, or replace it with the intended pronunciation and document that source.
- [ ] **Suggestion — editorial.public_material_candidate:** The Git-shared Great Library comment identifies Paisa as [[Scordith|Scordith's]] birthplace, and [[Scordith]] independently establishes the same fact. Add: “Paisa was the birthplace of [[Scordith]], who lived there until age six before being sent to a monastery in the hills.” Then remove the duplicated hidden sentence or retain only distinct campaign-source guidance.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/whereabouts, status/check/lint]
typeOf: settlement
typeOfAlias: village
campaignInfo:
  - {campaign: grli, type: visited, date: 1748-08-23, wParty: "<met:u> by <person> on <target> <current:Frq>"}
name: Suwi
whereabouts: Northwest Coast
dm_owner: none
dm_notes: none
POV: modern
---
# Suwi
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Visited by the [[Silver Tempests]] on August 23rd, 1748 in the [[Northwest Coast]] %%^End%%

%% needs a more specific whereabouts but the region is not well developed yet %%

A coastal village west of the [[Fiatara Mountains]] and near the [[Slate Sea]]. 

%%
GL Arc 4: staging point for investigation of nearby lake caverns and the aboleth [[Ithu’rax]].
See: [[Great Library Session Notes - Arc 4]]
Minimal details invented - was just the staging point for running a published adventure from Where Evil Lies
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Suwi, language: unknown, pronunciation: SOO-wee, notes: cautious spelling-based reading; no accepted pronunciation source was found, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the village's geography is not tied to a narrower date, while the campaign block records a DR 1748 visit.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Replaced the Great Library alias `GL` with canonical campaign code `grli` in `campaignInfo` and the campaign block.
- Added the required settlement map skeleton with its unknown locator left blank.
- Added a minimal name entry with a spelling-based pronunciation proposal.
- Added `POV: modern` and a persistent temporal-coverage note.

### Validated judgments
- `status/cleanup/whereabouts` is supported: the visible editorial comment says the broad regional whereabouts needs a more specific location once that geography is developed.
- The second shared comment is campaign/source guidance rather than a public reference account.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required world-map locator is blank. Replace the blank `locator` with Suwi's verified world-map coordinate.
- [ ] **Warning — metadata.names_unresolved_status:** `SOO-wee` is a cautious spelling-based proposal for Suwi, consistent with the unresolved proposal on [[Lake Suwi]]. Accept it by adding `pronunciation: SOO-wee` to frontmatter and changing the name entry to `status: documented`, or replace it with the intended pronunciation and document that source.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Zurrua
pronunciation: TSOO-roo-ah
whereabouts: Portalia
dm_owner: none
dm_notes: none
POV: 1748
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
Temporal coverage: a DR 1748 campaign reference, when the Silver Tempests traveled downriver from Urkabi; the note does not otherwise describe the river's state or continuity.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Validated judgments
- Shared nonpublic comments and Campaign:none material were reviewed; no additional public-safe candidate met the reporting threshold beyond any task below.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** Great Library Arc 5 establishes that the river passes Urkabi and was traveled downriver by the Silver Tempests in DR 1748, but the note has no visible article text. Candidate: add one sentence identifying the Zurrua as the river through Urkabi and noting the DR 1748 downstream journey only if campaign context is useful.
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: source.locator, outlet.locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.

%%^End%%

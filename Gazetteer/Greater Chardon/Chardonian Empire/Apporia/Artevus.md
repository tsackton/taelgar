---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
population: 850
name: Artevus
whereabouts: Portalia
dm_owner: tim
dm_notes: color
POV: modern
---
# Artevus
>[!info]+ Information  
> pop. 850  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Artevus is a small coastal town in northern [[Portalia]], primarily a minor market town for local fisherfolk. A relatively poor town, and somewhat dilapidated, Artevus is something of a sleepy backwater. 

The docks and the market square, with the nearby temple of the [[Mos Numena]], are the most notable local landmarks. A few quiet inns and taverns line the edge of the market square, near the docks, but are rarely busy.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Artevus", role: "primary", language: "Chardonian", pronunciation: "ar-TEH-woos", notes: "Classical Latin analogue: v read as w and penultimate stress.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern snapshot of Artevus as a poor, quiet fishing-market town; no founding date or later change in the town's condition is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Artevus — ar-TEH-woos` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

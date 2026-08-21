---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Arendum
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: 1748
---
# Arendum
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% substantial notes in OneNote from Cape / Elderwood adventure %%

Arendum is a substantial provincial town, with a frontier vibe. Built on the ruins of a former city-state, [[Kin-Aska]], which was a Chardonian satellite, a mixed Northlander/Drankorian culture with good relations with the nearby Deno'qai tribes in the forests, as well as the elves.


%% From Cape adventure briefing emails:
* The road is reasonably busy, and goes all the way to Arendum, about 500 miles east at the edge of the Chardonian Empire, on the eaves of the Elderwood.


Border town and timber capital of the Elderwood province. Built on the destroyed city-state of Kin-Aska, a pre-Great War settlement of mixed Drankorian and Northros population.

%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Arendum", role: "primary", language: "Chardonian", pronunciation: "ah-REN-doom", notes: "Latin analogue: penultimate stress and final um.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 frontier-town snapshot, with the present settlement described alongside the older ruins of Kin-Aska; earlier and later conditions in Arendum are not described.
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

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** Session 51 establishes that Arendum is organized around defense and has visible tension with nearby Deno'qai communities. Candidate: add a concise sentence about the defensive character and observed Chardonian-Deno'qai tension, attributed to the DR 1748 campaign snapshot.
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Arendum — ah-REN-doom` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

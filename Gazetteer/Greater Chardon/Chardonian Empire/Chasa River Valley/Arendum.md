---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T19:01:27-04:00"
lintVersion: "3.4"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Arendum
pronunciation: ah-REN-doom
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: 1748
---
# Arendum
*(ah-REN-doom)*
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
  - {map: world, locator: 12.08.C23}
%%^End%%

%%^Metadata:names:v1%%
- {name: "Arendum", role: "primary", language: "Chardonian", pronunciation: "ah-REN-doom", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 frontier-town snapshot, with the present settlement described alongside the older ruins of Kin-Aska; earlier and later conditions in Arendum are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Session 51 (DuFr)]] establishes that Arendum's gates and towers face the Elderwood and that friction with neighboring forest communities has produced a substantial imperial garrison, but the visible article gives only the town's river-trade setting. Candidate: add "Arendum's gates and towers face the Elderwood, reflecting its role as a fortified frontier town. Friction with neighboring forest communities has brought a substantial imperial garrison to the settlement."
- [x] **Warning — metadata.map_location_missing:** The settlement map record has a blank locator. Fill it only from the authoritative map; do not guess a coordinate.
- [x] **Warning — metadata.names_unresolved_status:** The persistent entry for Arendum remains status: proposed. Review the recorded pronunciation and linguistic analogue, then accept it in frontmatter or correct the persistent entry.
- [ ] **Suggestion — editorial.shared_material_redundant:** The shared briefing-email block repeats the town's visible trade, road, ferry, and frontier description. If the approximate five-hundred-mile distance from the imperial capital remains useful, adopt it only after source review; otherwise retain only the source pointer and remove duplicated summary prose.

%%^End%%

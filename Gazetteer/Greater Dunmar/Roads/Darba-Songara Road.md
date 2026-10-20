---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: road
name: Darba-Songara Road
whereabouts: Dunmar
dm_owner: tim
dm_notes: none
POV: modern
---
# The Darba-Songara Road
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The ancient [[Drankorian Empire|Drankorian]] road that leads north from [[Darba]], joining the [[Stoneway]] near [[Songara]].

%%^Metadata:names:v1%%
- {"name": "Darba-Songara Road", "language": "unknown", "pronunciation": "DAR-bah sohn-GAH-rah rohd", "status": "proposed", "notes": "The place-name components are Dunmari in context; no explicit pronunciation was found in [[Darba]] or [[Songara]]. The Hindi or other Indo-Iranian (Persian) analogue in [[Languages]] informs the proposal: open ah vowels in the place names, o as oh, voiced ng plus g, and ordinary d/b/s/r; DAR and GAH are provisional reading stresses. Road retains its ordinary English reading. Exact name language, vowel lengths and in-world stress are unestablished."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: , map: world, locator: }
  - {feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the ancient road and its route.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving existing values.
- Added the explicit name Darba-Songara Road and persistent name metadata with a proposed pronunciation.
- Added the required two-endpoint road map skeleton, leaving both unknown locators blank.
- Recorded a broadly modern reference POV and temporal coverage.

### Validated judgments
- The concise route description performs this connector note's reference role; its ancient origin does not require a historical POV.
- The road's recorded endpoint is its junction with the Stoneway near Songara; no coordinate or exact city-center endpoint has been inferred.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace **DAR-bah sohn-GAH-rah rohd** for the complete Darba-Songara Road name. [[Darba]] and [[Songara]] record no pronunciations. Their Dunmari context supplies the “Hindi or other Indo-Iranian (Persian)” analogue in [[Languages]]: the proposal uses open ah vowels, `o` as oh, voiced `ng` plus `g`, and ordinary `d/b/s/r`; DAR and GAH are provisional reading stresses, while Road uses its ordinary English reading. The exact source language, vowel lengths and in-world stress are unestablished. If accepted, set frontmatter `pronunciation: DAR-bah sohn-GAH-rah rohd` and change the name entry to `status: documented`; otherwise replace the proposal with the accepted form.
- [ ] **Warning — metadata.map_location_missing:** Both required endpoint locators remain blank. Supply verified world-map hexes for the Darba endpoint and the junction with [[Stoneway]] near [[Songara]] in the existing two `locations` entries. Keep `map: world` and fill each `locator` with its verified coordinate; do not substitute Songara's center for the nearby junction without evidence.
%%^End%%

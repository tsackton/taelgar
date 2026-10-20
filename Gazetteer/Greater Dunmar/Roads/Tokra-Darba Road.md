---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on", ltPlace: "on"}
tags: [place, status/check/lint]
typeOf: road
name: Tokra-Darba Road
whereabouts: Dunmar
dm_owner: tim
dm_notes: color
POV: modern
---
# The Tokra-Darba Road
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A Dunmari road that runs from the [[Melavan Caravanserai]], northwest of [[Tokra]], through the [[Copper Hills]], until it joins the [[Darba-Songara Road]] northeast of [[Darba]]. This road has seen better days: it is dusty and dry in the summer, and muddy during the monsoon. Nonetheless, for much of its length there are maintained way stations, and well-stocked caravanserai, spaced a day's journey apart. The only truly rough spot is the 60 miles or so where the road passes through the rocky outcroppings of the [[Copper Hills]], where there are no inns or way stations. 

%% notes from onenote: 
The Darba Road is really more of a marked track in the plains, and it is muddy and difficult at the moment, with the rains. It is not paved or anything, and frequently suffers from poor maintenance. 

The road is a minor road, dating from the Dharajun dynasty, pre-Great-War. It gets dusty in the hot summer and muddy in the monsoon.

also several points of interest in onenote that could be added
%%

%%^Metadata:names:v1%%
- {name: Tokra-Darba Road, language: unknown, pronunciation: "TOHK-rah DAHR-bah rohd", status: proposed, notes: "Tentative place-name components informed by the Hindi option of the Dunmari analogue in [[Languages]]: o as oh, a as ah, k-r kept distinct, and ordinary d/r/b consonants; English Road as rohd. Initial stress is a reading aid. The Persian alternative and exact in-world vowel lengths, consonant articulation, stress and source language are unestablished."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Melavan Caravanserai, map: world, locator: }
  - {feature: Darba-Songara Road, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern route, travel conditions and waystations; seasonal descriptions recur annually rather than describing one campaign journey.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added a persistent name entry with a proposed full pronunciation, a typed road-endpoint map block, and a broadly modern temporal viewpoint; normalized frontmatter formatting.

### Validated judgments
- The route and junctions are corroborated by [[Session 43 (DuFr)]] and [[Session 45 (DuFr)]]. Their routine encounters do not require a campaign log in the road reference.
- Confirmed local sources support the existing positive `dm_notes` attestation; its value is retained.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required road map block identifies the Melavan Caravanserai and Darba-Songara Road endpoints, but both `locator` values remain blank. Supply verified world-map positions for these two endpoints; the block uses unordered endpoints, and no hexes were inferred from travel times.
- [ ] **Warning — correctness.cross_note_conflict:** The final sentence gives about 60 miles without inns or waystations through the Copper Hills. [[Akela Inn]] instead describes the last stopping point before the Darba hinterlands 100 miles away, and [[Session 43 (DuFr)]] calls it the last caravanserai for “more than a hundred miles west.” Confirm the endpoints and reconcile the distance. If the same gap is intended, a candidate is: “Between the [[Akela Inn]] and the Darba hinterlands, travelers face more than a hundred miles without a caravanserai, including the rough crossing of the [[Copper Hills]].” If 60 miles describes only a shorter inner-hill stretch, distinguish that stretch from the full gap between stopping places rather than replacing one measure silently.
- [ ] **Warning — metadata.names_unresolved_status:** The name entry proposes **TOHK-rah DAHR-bah rohd**, informed by the Hindi option of the Dunmari analogue in [[Languages]] for the two place-name components: o as oh, a as ah, a distinct k-r cluster and ordinary d/r/b consonants; “Road” uses ordinary English. Initial stress is only a reading aid. Exact in-world vowel lengths, articulation, stress and source language, including the Persian alternative, remain unestablished. Confirm or replace the full form; if accepted, set it in frontmatter and change the entry to `status: documented`.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared “notes from onenote” comment contains the coherent historical sentence “The road is a minor road, dating from the Dharajun dynasty, pre-Great-War,” which is absent from the visible account. Decide whether to adopt: “The road dates from the [[Dharajun Dynasty]], before the [[Great War]].” This would supply the route’s historical origin; the shared comment is a proposal source, not proof of adoption. As a bounded split, remove the comment’s repeated dusty-summer/muddy-monsoon descriptions if the history is adopted, and retain only its distinct OneNote follow-up reminder as private editorial guidance.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Old Trade Road]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Road to Darba]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Vedmakov
whereabouts: Ursk
dm_owner: tim
dm_notes: color
POV: modern
---
# Vedmakov
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


Vedmakov stands at the headwaters of the [[Leis]] in interior [[Ursk]], a strategic hub on the overland route between the Ket basin and the western grainlands. Renowned—and feared—as the namesake seat of the [[Eyes of Vedmakov|Okolov]], the city exercises rigorous control over arcane practice and travel. Patrols on the roads and river approaches are disciplined and methodical; transit papers are routinely inspected, and contraband magic is confiscated without ceremony.

Topographically, Vedmakov sits amidst rolling farmland cut by river valleys that funnel trade east and west. Caravans bound for [[Yamgov]] often skirt the city rather than attempt entry, following maintained roads across tilled fields and low ridges. The city’s inner districts are said to house archives and administrative halls of the Okolov, though such places are seldom seen by foreign eyes.

%%
Meta/DM notes and campaign interactions:
- Referenced across travel notes in [[Session 95 (DuFr)|DuFr 95]] (road choice, patrols, bypassed en route to Yamgov); see also [[Philosopher's Information Concerning Ursk|Philosopher’s guidance]] (hopeless to infiltrate).
- Practical: road checks by Watchers; archival presence within the city; common to pass without entering when traveling west.
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Vedmakov", "language": "unknown", "pronunciation": "vyid-MAH-kuhf", "status": "proposed", "notes": "The Urskan context supplies the Russian analogue in [[Languages]]. Proposed soft v before e, reduced unstressed first and final vowels, tentative stress on mak, and final v devoiced to f. The exact in-world name language and stress are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern city geography and institutional role, supported around the DR 1749 journey; the campaign visit does not establish a narrower city-state transition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, made the filename-supplied name explicit, and added the required typed map skeleton with a blank locator.
- Added proposed primary name metadata and broadly modern temporal metadata.

### Validated judgments
- Confirmed local DM sources support the existing positive `dm_notes` attestation; private contents remain outside this report.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` single-location entry has an empty locator. Supply the settlement's verified world-map position as `- {map: world, locator: "<verified coordinate>"}`; the available prose does not establish a hex, so no coordinate was guessed.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `vyid-MAH-kuhf` in the persistent name entry. The Urskan cultural context supplies the Russian analogue in [[Languages]]: soft v before e, reduced unstressed vowels, a tentative stress on mak, and final v devoiced to f. These are analogue-informed choices; the name's actual language and stress remain unrecorded. If accepted, set `pronunciation: vyid-MAH-kuhf` and mark the entry `documented`.
- [ ] **Warning — correctness.unsupported_claim:** The visible text generalizes from one caravan journey to “Caravans bound for [[Yamgov]] often skirt the city” and asserts routine confiscation of contraband magic plus archives and administrative halls in the inner districts. [[Session 95 (DuFr)]] establishes the road, a transit-paper inspection, and the party passing without entry; [[Philosopher's Information Concerning Ursk]] warns against infiltration. Neither establishes the frequency of caravan bypasses, a confiscation policy, or the stated interior institutions. Verify these details, or replace only the unsupported clauses with: “Patrols inspect transit papers on the roads approaching Vedmakov. A maintained road connects the city with [[Yamgov]] to the west.” Do not infer a common merchant practice from the party's route.
- [ ] **Suggestion — editorial.shared_material_redundant:** The comment's `- Practical:` bullet repeats the visible patrol, archive, and bypass claims. Remove that bullet while retaining the first bullet's links to [[Session 95 (DuFr)]] and [[Philosopher's Information Concerning Ursk]] as a source pointer. Resolve the unsupported generalizations above before treating the repeated material as established.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 93 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

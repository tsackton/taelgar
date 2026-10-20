---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Sulmana
whereabouts: Elemental Plane of Air
dm_owner: none
dm_notes: none
POV: modern
---
# Sulmana
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A mysterious place on the [[Elemental Plane of Air]].

%%
the home of a djinn, [[Mehrangeesa]], but no canonical details invented
%%

%%^Metadata:names:v1%%
- {"name": "Sulmana", "language": "unknown", "pronunciation": "sul-MAH-nah", "notes": "Cautious spelling-based proposal: sul as in sulk, mah and nah with the vowel of father, and proposed second-syllable stress. No name-specific language, pronunciation, or stronger phonological rule is established.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographical reference to Sulmana on the Elemental Plane of Air; no narrower date or historical transition is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `typeOf: settlement` and `typeOfAlias: city`, supported by the Plane of Air and Mehrangeesa reference notes; normalized frontmatter.
- Added a proposed spelling-based pronunciation in persistent name metadata without changing accepted display values.
- Added broadly modern temporal metadata and the required settlement map skeleton with an unknown locator.

### Validated judgments
- The duplicate local timeline material adds nothing recoverable beyond the shared origin/release account; `dm_notes: none` is preserved.
- Later shared Arc 6 planning describes intended activity and does not establish a completed change to the city.

### Editorial assessment
**Underdeveloped**: the visible article identifies only a mysterious place, although shared reference sources already establish a djinni city, its conventional description, and Mehrangeesa's origin there. A short sourced city description is the missing central account; no invented city history or unrelated campaign log is needed.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Elemental Plane of Air]] identifies Sulmana as the City of Clouds, home of the Dukes of the Four Winds, and a reported great djinni city with domes of spun clouds. [[Mehrangeesa]] establishes a named inhabitant's origin. The visible “mysterious place” description omits that defining identity. Candidate: “Sulmana, the City of Clouds, is a city on the [[Elemental Plane of Air]] and the home of the Dukes of the Four Winds. Planar scholarship describes it as one of the great cities of the djinni, with towering domes built of spun clouds. [[Mehrangeesa]] is originally from Sulmana.” Preserve the reported character of the architectural description; the comment's old claim that no canonical details exist should be reconciled during adoption.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary entry proposes `sul-MAH-nah`: sul as in sulk, mah and nah with the vowel of father, and second-syllable stress. This is a cautious spelling reading; no name-specific language, pronunciation, or stronger phonological rule is established. Confirm or revise the proposal. If accepted, copy the complete pronunciation to frontmatter and mark the entry `documented`; no accepted pronunciation was overwritten.

- [ ] **Warning — metadata.map_location_missing:** The settlement profile requires a location entry, but the consulted sources supply no map locator for this extraplanar city. The standard skeleton retains a blank locator and makes no coordinate claim. Supply a supported map and locator, or explicitly decide how this off-world settlement should be represented; do not invent a Taelgar hex or treat the template's default `world` map as established geography.
%%^End%%

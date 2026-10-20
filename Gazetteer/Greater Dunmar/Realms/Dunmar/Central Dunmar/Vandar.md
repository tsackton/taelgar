---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: village
ancestry: Dunmari
name: Vandar
whereabouts: Copper Hills
dm_owner: tim
dm_notes: important
POV: 1748
---
# Vandar
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

An abandoned mining village in the [[Copper Hills]]. The village is set in the hills, on a bit of a rise. While most of the town is just ruins, the temple of the [[Dunmari Religion]], on a larger hill, is still mostly intact, albeit completely looted of any valuables. A short walk from the village is a flooded copper mine shaft. 

%%SECRET[v2:8d389e192ccd06f166b65cb7743f64f4]%%

%%^Metadata:names:v1%%
- {name: Vandar, role: primary, language: unknown, pronunciation: van-DAR, status: proposed, notes: "Regional proposal informed by the Persian option in the Dunmari guidance in [[Languages]]: retain v, n, and d, read both a vowels as the short a in cat, and stress the final syllable. A Hindi-oriented reading could instead reduce the vowels and favor the first syllable. The name's language and exact in-world phonology are not established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a pre-fire DR 1748 description of the abandoned village and its largely intact temple; a fire in the temple ruins is recorded on July 23rd, but the extent of lasting damage is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added a persistent name entry with a proposed pronunciation and its regional derivation.
- Added the required single-location map skeleton, leaving its unknown locator blank.
- Added `POV: 1748` and temporal coverage metadata identifying the visible description as a pre-fire snapshot.

### Validated judgments
- Confirmed local source identities support the positive `dm_notes` attestation; no private source content was added to this report.
- The SECRET block was reviewed and preserved; any recovery candidate remains in the private handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `van-DAR` in the name block. The Dunmari entry in [[Languages]] allows Hindi or Persian guidance; the preferred regional proposal follows its Persian option, retaining v, n, and d, reading both a vowels as the short a in “cat”, and stressing the last syllable. A Hindi-oriented alternative could reduce the vowels and favor initial stress. The name's language and exact in-world phonology remain unestablished. If accepted, copy the pronunciation to frontmatter and mark the entry `documented`; otherwise revise the proposal.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has no `locator`. Supply the established world-map position in `locations: [{map: world, locator: <confirmed locator>}]`; do not infer a world-map coordinate from an unidentified legacy map.
- [ ] **Warning — coverage.later_material_change:** The article describes the temple as largely intact, but [[Session 45 (DuFr)#Narrative]] records a fire starting in its ruins during the fighting on the night of July 23rd, DR 1748. The source does not establish that the temple or village was completely destroyed. Candidate addition: “On the night of July 23rd, DR 1748, a fire started in the temple ruins during a battle; the extent of lasting damage is not recorded.” Choose whether to update the account and its POV, defer the update with a human-selected game-update tag, or intentionally preserve the earlier snapshot. If retaining a broader article with a dated later layer, the smallest proposed layer is `%%^Date:1748-07-24%%`, that retrospective sentence, and `%%^End%%`; separately date the surviving pre-fire temple description rather than implying it remains current. No visibility block or non-lint status was changed automatically.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Copper Hills/Vandar (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
%%^End%%

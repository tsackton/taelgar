---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: fortified border town
name: Cassons
whereabouts: Duchy of Maseau
dm_owner: none
dm_notes: none
POV: modern
---
# Cassons
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The main town in southern [[Duchy of Maseau|Maseau]] is the border fort of Cassons. Once an important town on the road from [[Isingue]] to [[Embry]], it is a shadow of its former self and is dotted with ruins and abandoned buildings. It is a dry and dusty place, just far enough south to get choking ash storms in the summer, and the people eke out a meager living on the proceeds from trade along the [[Maseau - Dunmar Road]] and food shipments from [[Duchy of Maseau|Maseau]], designed to encourage a defense here. In the hinterlands of Cassons a small number of ranchers have established themselves along the ruins of the [[Great South Road]], and the forts of the Marcher Lords dot the ranchlands for several days' ride south.

%%^Metadata:names:v1%%
- {"name": "Cassons", "language": "unknown", "pronunciation": "kah-SOHN", "status": "proposed", "notes": "Proposed from the French analogues for southern Sembaran and northern Isinguese in [[Languages]], appropriate regional guidance for Maseau: hard c, a as ah, and final ons as a nasal oh sound without a pronounced s. The exact name language and nasal realization remain unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the undated frontier-town description includes older trade history but establishes no narrower present-day snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.
- Added the required settlement map skeleton, leaving its unknown locator blank.
- Corrected “or several days’ ride south” to “for several days’ ride south”.

### Validated judgments
- The small frontier-town account is proportionate to its role; travel and mobilization references do not require a campaign log in the article.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed single-location entry, but its `locator` is blank. Supply the verified world-map coordinate in that existing entry; the reviewed text and prepared evidence do not establish a coordinate, so none has been guessed.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `kah-SOHN`. The French analogues for southern Sembaran and northern Isinguese in [[Languages]] supply the strongest regional guidance for Maseau: hard c, a as ah, and final ons as a nasal oh sound without a pronounced s. The name language and exact nasal realization are unconfirmed. Confirm or replace the proposal; if accepted, copy the complete pronunciation to frontmatter and mark the existing entry `documented`.
%%^End%%

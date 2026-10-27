---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Aursenbourg
whereabouts: Refounded Alliance of Aurbez
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Aursenbourg is a walled market town where the [[Maseau - Dunmar Road]] crosses the [[Aursen]], centered on a sturdy stone bridge built over the river in DR 1732. Now a major market town for the region, a generation ago this was only a small village known as Aursen's Crossing, where regular ferry service would shuttle caravans and traders over the Aursen.

%%^Metadata:names:v1%%
- {"name": "Aursenbourg", "language": "unknown", "pronunciation": "or-sen-BOOR", "notes": "Proposed from the Isinguese cultural context and northern French analogue in [[Languages]]: au is rounded o, r remains audible in a reader-facing approximation, ou is oo, the final g of bourg is silent, and the final group is stressed. The name-specific source language is not established.", "status": "proposed"}
- {"name": "Aursen's Crossing", "role": "historical", "language": "unknown", "pronunciation": "OR-senz KROSS-ing", "notes": "The earlier village name is documented in this note. Proposed reading retains the Aursen component of the primary proposal, adds possessive z, and reads Crossing as ordinary English; this mixed displayed form does not establish its in-world source language.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the modern market town after the DR 1732 bridge replaced the ferry; the earlier village is described retrospectively.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit filename-derived name, persistent primary and historical name entries, temporal metadata, and the required map skeleton.

### Validated judgments
- [[Maseau - Dunmar Road]] corroborates the bridge’s construction in DR 1732 and its replacement of the ferry. The note adequately defines the town’s stable market and crossing role; the refugee crisis in [[Session 130 (DuFr)]] does not by itself establish a lasting change to that role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed skeleton, but `locations[0].locator` is blank. Supply a verified world-map locator in `{map: world, locator: <verified locator>}`; no coordinate is established by the consulted text sources.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm proposed `or-sen-BOOR` for Aursenbourg and `OR-senz KROSS-ing` for the documented earlier name Aursen’s Crossing. The Isinguese cultural setting and the northern French analogue in [[Languages]] motivate rounded o for au, oo for ou, a silent final g in bourg, and final group stress; the English possessive and Crossing are read as displayed. The exact source languages and in-world phonology remain unknown. Accept or revise each stored proposal, mark accepted entries documented, and copy the accepted primary pronunciation to frontmatter.

### DM evidence
- [[_DM_/Staging/Beatriz]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Aurbez NPC Charts]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
%%^End%%

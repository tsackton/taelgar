---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Fontwick
whereabouts: Stonewolds
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Fontwick is a small upland village on the edges of the [[Stonewolds]], a cluster of stone cottages gathered around a spring. Its folk tend sheep and some cattle on the rough grasses between rocky outcrops and cut timber from coppiced lots.

%%^Metadata:names:v1%%
- {"name": "Fontwick", "language": "unknown", "pronunciation": "FONT-wik", "status": "proposed", "notes": "[[Addermarch Village Names]] explicitly proposes FONT-wik in its French/English draft list. This remains provisional Worldbuilding guidance, not an accepted in-world pronunciation: font has the short English o and wick ends in k. The regional guidance in [[Languages]] permits both French and English influence; an entirely French treatment of font would instead nasalize its vowel."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography and institutions.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added primary name metadata and supported temporal POV metadata.
- Added the required typed map skeleton without inventing positions.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The typed map block has a blank world-map locator. Supply a verified locator from the map; the linter has not inferred a coordinate.

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry records proposed pronunciation `FONT-wik`. [[Addermarch Village Names]] explicitly proposes FONT-wik in its French/English draft list. This remains provisional Worldbuilding guidance, not an accepted in-world pronunciation: font has the short English o and wick ends in k. The regional guidance in [[Languages]] permits both French and English influence; an entirely French treatment of font would instead nasalize its vowel. Accept or revise it; if accepted, copy the pronunciation to frontmatter and mark the existing entry documented.
%%^End%%

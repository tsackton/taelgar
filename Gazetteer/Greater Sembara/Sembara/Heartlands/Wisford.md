---
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
campaignInfo: null
population: 8500
mapLocation: { x: 6484, y: 5338.5, hex: 12.11.D.06/5452, importance: local, symbol: square }
name: Wisford
pronunciation: Wis-ford
whereabouts: Duchy of Wisford
dm_owner: mike
dm_notes: color
POV: modern
---
```taelgar-header
```

The largest city in the [[Duchy of Wisford]] and the traditional seat of the Duke. It is a busy place at the intersection of the [[Great South Road]], the [[Tyrwinghan Road]], and the [[Wistel]], and more cosmopolitan than most Sembaran cities. It is divided into two sections, the North Bank and the South Bank, split by the [[Wistel]], and the ducal palace sits on a small island in the middle of the river, said to have been created as a gift from the gods many years ago.

%%^Metadata:names:v1%%
- {"name": "Wisford", "language": "unknown", "pronunciation": "Wis-ford", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern city layout, transport connections, and institutional ducal seat; the island-origin tradition is attributed rather than dated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “on an small island” to “on a small island.”
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded the existing accepted pronunciation in the primary name entry.
- Added the required single-location map skeleton with its unknown locator left blank.
- Recorded the article POV and a persistent temporal-coverage interpretation.

### Validated judgments
- The ducal-seat description and broad modern geography are compatible with [[Duchy of Wisford]] and [[Heartlands]]. Mike ownership makes the local DM-attestation evidence gate inapplicable.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement has no established world-map locator in the reviewed evidence. Supply the actual coordinate in the existing `locations` entry, keeping `map: world`; do not infer a hex from nearby places.

%%^End%%

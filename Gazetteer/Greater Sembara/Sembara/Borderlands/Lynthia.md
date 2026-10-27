---
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Lynthia
pronunciation: LIN-thee-ah
whereabouts:
  - {type: primary, location: Barony of Estrive}
  - {type: secondary, location: Lake Rin}
POV: modern
---
```taelgar-header
```

Lynthia is a growing market town on the southeastern shore of [[Lake Rin]], near the [[Enst]], in the [[Barony of Estrive]]. A twice-daily ferry connects it with [[Chantefleur]] on the opposite shore.

%%^Metadata:names:v1%%
- {name: Lynthia, language: Sembaran, pronunciation: LIN-thee-ah, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and ferry service, with no narrower snapshot established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the required settlement map skeleton, leaving its unknown locator blank.
- Added `POV: modern` and persistent temporal guidance.

### Validated judgments
- The existing documented name entry is preserved; [[Chantefleur]] corroborates the twice-daily ferry across [[Lake Rin]].

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed single-location entry, but its `locator` is blank. Supply the verified world-map coordinate in that existing entry; the reviewed text and prepared evidence do not establish a coordinate, so none has been guessed.
%%^End%%

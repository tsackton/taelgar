---
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
created: 1699
name: Aubrille
pronunciation: oh-BREE
whereabouts: Barony of Estrive
POV: modern
---
```taelgar-header
```

Aubrille is a village on the southern shore of [[Lake Rin]], near [[Lynthia]], in the [[Barony of Estrive]]. It is ruled by an energetic young lord.

%%^Metadata:names:v1%%
- {name: Aubrille, role: primary, language: Sembaran, pronunciation: oh-BREE, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern village geography after its DR 1699 foundation; the unnamed lord’s youth is not anchored to a dated tenure.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the typed settlement map block with its unknown locator left blank.
- Added modern POV and persistent temporal-coverage metadata.

### Validated judgments
- The documented Aubrille name entry and accepted pronunciation were preserved unchanged.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block is now present, but its `map: world` entry has a blank `locator`. Supply an established map coordinate for this settlement; the typed placeholder deliberately makes no location claim.

- [ ] **Warning — temporal.unanchored_state:** “It is ruled by an energetic young lord” is an undated changing state. [[Lake Rin]] repeats the same description without identifying the lord or anchoring a tenure, and `created: 1699` dates the village rather than the ruler. Establish a dated tenure before retaining the age claim, or adopt the geography-only candidate: “Aubrille is a village on the southern shore of [[Lake Rin]], near [[Lynthia]], in the [[Barony of Estrive]].” Preserve the undated age description as an editorial reminder if useful; do not invent a year or add a Date block automatically.
%%^End%%

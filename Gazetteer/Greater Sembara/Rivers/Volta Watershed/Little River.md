---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Little River
whereabouts:
  - {type: primary, location: Tollen}
  - {type: secondary, location: Volta Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Little River is a minor watercourse, now channeled into a canal, that flows through [[Brooklawn Inner]] before joining the [[Volta]]. Inside the city, the Little River is crossed by numerous bridges over the canal. Before it enters the city, it forms the boundary between [[Brooklawn Outer]] and [[Fairgate Outer]]; this is the center of the tannery and leatherworking districts of the city, and dyers’ sheds and other infrastructure dot the river's edge.

%%^Metadata:names:v1%%
- {"name": "Little River", "language": "Common"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "", "map": "world", "locator": ""}
  - {"role": "outlet", "feature": "Volta", "map": "world", "locator": ""}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and use; no narrower temporal reading position is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Added the required typed map entries; unsupported locator values remain blank.
- Corrected the declared objective grammar or typo without changing the factual account.

### Validated judgments
- The complete displayed name is ordinary English; no pronunciation guide is needed.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required river source and outlet entries in Metadata:map:v1 still have blank locator values. The reviewed sources establish identifying features but no verified world-map hexes for these positions. Supply each verified coordinate in its existing `locator` field, for example `locator: "<verified world hex>"`; retain the typed entries and do not infer a hex from a nearby place.
%%^End%%

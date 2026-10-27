---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: road
name: South Watch Road
whereabouts: Sembara
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

A new road, built during the reign of [[Cece I]] to connect [[Dunfry]] and the [[Army of the South|South Watch]] with [[Fellburn]] after the [[Third Hobgoblin War (Sembara)|hobgoblin wars]]. Most of the road runs through unsettled land, although several fortified garrison-houses dot the road to support soldiers and messengers travelling the road.

%%^Metadata:names:v1%%
- {"name": "South Watch Road", "language": "Common"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"feature": "Dunfry", "map": "world", "locator": ""}
  - {"feature": "Fellburn", "map": "world", "locator": ""}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern road and garrison use after construction during Cece I’s reign; the construction is historical background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Added the required typed map entries; unsupported locator values remain blank.

### Validated judgments
- The complete displayed name is ordinary English; no pronunciation guide is needed.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required road endpoint entries in Metadata:map:v1 still have blank locator values. The reviewed sources establish identifying features but no verified world-map hexes for these positions. Supply each verified coordinate in its existing `locator` field, for example `locator: "<verified world hex>"`; retain the typed entries and do not infer a hex from a nearby place.
%%^End%%

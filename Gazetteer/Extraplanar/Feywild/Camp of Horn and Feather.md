---
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
name: Camp of Horn and Feather
whereabouts: "Twilight's Edge"
POV: modern
---
```taelgar-header
```

The Camp of Horn and Feather is a lightly fortified fey encampment on a ridge at the western edge of [[Twilight's Edge]], on the border beside the [[Grey Mists]] and near [[Duskmire]]. Tents and a bonfire stand behind a wall, where the five fey siblings [[Thyron]], [[Kyron]], [[Myron]], [[Syron]], and [[Lyron]] camp with their animal companions.

The siblings keep watch over the border and hunt the surrounding lands. Watchfulness mingles with wild hospitality here: visitors may be challenged for their credentials, then drawn into feasting, tall tales, dances, and extravagant wagers around the bonfire.


%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Camp of Horn and Feather, language: Common, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference description of the border camp and its customary watch, hunting, and hospitality.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added a typed settlement map block and broadly modern temporal metadata.

### Validated judgments
- The existing documented Common name is preserved and needs no pronunciation. [[Cleenseau - Session 34]] supports the camp's identity and hospitality; its incidental visit and recovery do not need a campaign recap in this reference note.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** This camp is correctly classified as a settlement, so the adopted map profile requires a position. The new `Metadata:map:v1` block leaves its locator blank because neither the camp note nor [[Cleenseau - Session 34]] establishes a coordinate. Supply the supported locator in `locations: [{map: world, locator: "<supported locator>"}]`, or resolve the map representation for this Feywild site before replacing the blank; do not infer a Material Plane coordinate from approximate geography.
%%^End%%

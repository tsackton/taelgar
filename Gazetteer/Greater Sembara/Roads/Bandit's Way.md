---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: road
typeOfAlias: section
name: "Bandit's Way"
whereabouts:
  - {location: Great South Road, linkText: of}
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

Bandit's Way is the name for the stretch of the [[Great South Road]] that passes between [[Evis]] and [[Cleenseau]] through a hundred miles of rocky shrubland. The road used to be dotted with inns and waystations, but these have fallen into disrepair since the Great War. This stretch of road is dangerous and many ex-soldiers make a living escorting caravans between [[Cleenseau]] and [[Evis]], the northernmost settlement in [[Duchy of Maseau|Maseau]] along the Great South Road.

%%^Metadata:names:v1%%
- {name: "Bandit's Way", language: "Common", status: "inferred", notes: "Plain-English descriptive road name; no pronunciation guide is needed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: "Evis", map: world, locator: }
  - {feature: "Cleenseau", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern after the Great War; the article describes the road with its former inns and waystations in disrepair, without requiring a narrower campaign-era snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Corrected "ex-soliders" to "ex-soldiers" without changing meaning.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its Evis and Cleenseau endpoints locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.
%%^End%%

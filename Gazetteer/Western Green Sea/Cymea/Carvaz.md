---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Carvaz
pronunciation: kar-VAHZ
whereabouts: Cymea
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Carvaz is a river in [[Cymea]] and an eastern tributary of the [[Ampogio]]. 

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Ampogio, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Carvaz", "language": "unknown", "pronunciation": "kar-VAHZ", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography of the Carvaz and its tributary relationship to the Ampogio.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name metadata using the existing accepted pronunciation.
- Added the required two-ended map block, identifying the established outlet feature as Ampogio while leaving unsupported source and outlet coordinates blank.
- Recorded modern POV and persistent temporal interpretation.

### Validated judgments
- The one-sentence river entry identifies its region and eastern tributary relationship; [[Ampogio]] corroborates the confluence. No broader river history or generic geography is required for this connector.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required source.locator and outlet.locator remain blank. Supply the Carvaz source and Ampogio-confluence positions from an authoritative map. Keep `map: world` for coordinates in `13.07.F16` form, and retain the source/outlet roles; no coordinates were inferred from the prose.
%%^End%%

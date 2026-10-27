---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 174
name: Windlea
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

Windlea is a village on headwaters of the [[Leandre]], where it flows out of the [[Cleenseau Wood]] before joining the [[Auberonne]]. It is primarily known for an ancient temple of [[The Wanderer]] about a mile outside the town.

%%^Metadata:names:v1%%
- {"name": "Windlea", "language": "unknown", "pronunciation": "WIND-lee", "status": "proposed", "notes": "The English analogue for Sembaran in [[Languages]] supports wind as the ordinary short-i noun and lea as lee, with first-syllable stress. A WINE-dlee reading would require a different intended sense of wind, which is not established; retain this as a proposal. Exact in-world pronunciation remains unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern village geography and the nearby ancient temple; no narrower state or dated change is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Added a persistent primary name entry with a proposed pronunciation and its derivation; accepted frontmatter pronunciation is unchanged.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary entry proposes `WIND-lee`. The English analogue for Sembaran in [[Languages]] supports wind as the ordinary short-i noun and lea as lee, with first-syllable stress. A WINE-dlee reading would require a different intended sense of wind, which is not established; retain this as a proposal. This is an analogue-informed proposal, not established in-world phonology. Accept or revise it; if accepted, copy the complete pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%

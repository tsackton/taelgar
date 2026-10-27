---
lintedAt: "2026-10-20T06:59:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: road
typeOfAlias: street
name: Inkspell Lane
whereabouts: Southbridge
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Inkspell Lane is a street in [[Southbridge]] that forms the center of [[Tollen]]’s tattoo trade, lined with tattoo parlors and studios. Many of the most prosperous and skilled tattoo artists in the city, especially those who work with magical inks and [[Tollen Magical Tattoo|enchanted tattoos]], keep their shops along Inkspell Lane.

%%^Metadata:names:v1%%
- {"name":"Inkspell Lane","language":"unknown"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: , map: world, locator: }
  - {feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern Tollen tattoo trade and street use; no dated change to the lane is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added persistent name metadata, `POV: modern`, and temporal-coverage notes.
- Recorded the existing subject explicitly as `name: Inkspell Lane` and added the required two-endpoint road map skeleton.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both endpoint `locator` values in `Metadata:map:v1` are blank. Inkspell Lane is explicitly a street and uses the road profile. Supply two supported endpoint locators with `map: world`; optional `feature` labels may remain blank. [[Southbridge]] locates the lane within Tollen but supplies neither endpoint coordinate, so no coordinates were guessed.
%%^End%%

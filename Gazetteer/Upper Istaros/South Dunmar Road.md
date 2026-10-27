---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on"}
tags: [place, status/check/lint]
typeOf: road
name: South Dunmar Road
whereabouts: Upper Istaros
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A major trade road that departs from the [[Maseau - Dunmar Road]] just south of the [[Aursen]], crosses the [[Douren|Douren River]] at [[Heuren Gorge]], runs along western foothills of the [[Sentinel Range]] through Stoneborn settlements, past [[Raven's Hold]], and eventually to [[Karawa]].

%% who actually built this road left somewhat ambiguous. maybe Stoneborn? %%

%%^Metadata:names:v1%%
- {"name": "South Dunmar Road", "language": "unknown", "pronunciation": "south DUN-mar road", "status": "proposed", "notes": "Complete-name proposal combines ordinary English South and Road with the documented DUN-mar in [[Dunmar]]: initial stress, u as in sun, and the recorded mar syllable. The full road name's language and accepted pronunciation are not established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Maseau - Dunmar Road junction, map: world, locator: }
  - {feature: Karawa, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography of the road; its construction history remains unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting and recorded `POV: modern` with persistent temporal coverage.
- Quoted the existing display preposition `on` so YAML parsing preserves it as display text rather than a Boolean.
- Added the required two-endpoint road map skeleton, retaining blank world-map locators.
- Added a primary name entry with a proposed complete-name pronunciation based on the documented Dunmar component.
- Corrected the crossing phrase from “as Heuren Gorge” to “at Heuren Gorge”; [[Heuren Gorge]] and [[Douren]] independently identify that crossing.

### Validated judgments
- The road is a sufficient route connector; the uncertain builder remains an editorial question.
- Completed the required local evidence review; the human DM attestation is unchanged.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Supply verified world-map locators for both endpoints: the junction with [[Maseau - Dunmar Road]] and [[Karawa]]. The route description establishes these features, but not their world hexes. Leave each `map: world` in place and replace only the blank `locator` values with verified coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete-name pronunciation `south DUN-mar road`. [[Dunmar]] documents `DUN-mar`; the proposal preserves first-syllable stress, u as in “sun”, and the recorded mar syllable, and reads “South” and “Road” as ordinary English. The complete phrase is derived from the accepted component, not independently attested; its historical name language remains unknown. Accept or revise the name-block entry before copying an accepted primary pronunciation to frontmatter.
%%^End%%

---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on"}
tags: [place, status/check/lint]
typeOf: road
name: Great South Road
whereabouts: Greater Sembara
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

An ancient road that runs from [[Tollen]] through [[Embry]] to [[Cassons]], and then onward into the [[Plaguelands]]. It is said to still be in good repair as far south as [[Isingue]], and before the Great War, continued almost 2500 miles to [[Drankorian Empire|Drankor]] itself.

It is in remarkably good repair, and for much of its length it is paved with wide, smooth stones with drainage ditches on both sides. According to legend many of the stones in the road are a thousand years old, and have never cracked.

%%^Metadata:names:v1%%
- {"name":"Great South Road","language":"unknown"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Tollen, map: world, locator: }
  - {feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern surviving route and reported road condition, with the pre-Great-War continuation to Drankor treated as historical.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Quoted the display preposition `on` as a string so YAML readers preserve its intended text value.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries with supported endpoint features and left unknown positions blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for endpoint 1 and endpoint 2. Fill those blank values with confirmed coordinates, preserving recorded features and roles. The southern endpoint also needs a human decision between the surviving route and former Drankor continuation; Isingue is not a documented terminus.
%%^End%%

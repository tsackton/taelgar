---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Leandre
pronunciation: Leh-ahn-dray
whereabouts:
  - {type: primary, location: Barony of Aveil}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# The Leandre
*(Leh-ahn-dray)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small river that runs from the [[Cleenseau Wood]] to the [[Auberonne]] in the [[Barony of Aveil]]. It is not navigable, and tends to be rocky and shallow.

%%^Metadata:names:v1%%
- {"name": "Leandre", "language": "unknown", "pronunciation": "Leh-ahn-dray", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Cleenseau Wood, map: world, locator: }
  - {role: outlet, feature: Auberonne, map: world, locator: 12.10.H19}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal reading position is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter where needed and recorded the article’s broadly modern POV with persistent temporal coverage.
- Added an explicit subject name where absent and a persistent primary name entry preserving the existing accepted pronunciation.
- Added typed map metadata using unambiguous existing geographical evidence; unsupported locators remain blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source locator remains blank because the visible article and [[Barony of Aveil]] put the headwaters in [[Cleenseau Wood]], while the shared mapped-river register in [[Wistel-Enst Watershed]] labels the source “Aveil Ridge” at `12.10.H.07`. Resolve this source discrepancy before using `12.10.H07`; retain the supported outlet `12.10.H19`. Copy-ready source entry after verification: `{role: source, feature: <verified headwater feature>, map: world, locator: <verified locator>}`.
%%^End%%

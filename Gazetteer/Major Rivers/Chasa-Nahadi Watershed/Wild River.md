---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Wild River
whereabouts:
  - {type: primary, location: Erbalta Plains}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: tim
dm_notes: none
POV: modern
---
# The Wild River
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Wild River is a tributary of the [[Snake River]], cutting across the plains northeast of [[Voltara]].

%%^Metadata:names:v1%%
- {"name": "Wild River", "language": "unknown"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Snake River, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal reading position is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter where needed and recorded the article’s broadly modern POV with persistent temporal coverage.
- Added an explicit subject name where absent and a persistent primary name entry.
- Added typed map metadata using unambiguous existing geographical evidence; unsupported locators remain blank.
- Corrected the transposed whereabouts spelling `Erblata Plains` to `Erbalta Plains`, matching the region’s filename, name, and the [[Snake River]] account.

### Validated judgments
- The subject name is an ordinary English color word or plain-English river name; pronunciation is therefore omitted while the required name entry is retained.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Supply verified world-map locators in the existing typed `locations` entries; the reviewed evidence does not establish their positions. Preserve the endpoint roles and do not infer hexes from prose distances.
%%^End%%

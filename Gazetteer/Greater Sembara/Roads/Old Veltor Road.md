---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: road
name: Old Veltor Road
whereabouts: Barony of Aveil
POV: modern
---
# The Old Veltor Road
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Old Veltor Road is a maintained road along the [[Auberonne]], running from [[Rinburg]] to [[Veltor]]. The route is ancient, but the road underwent substantial repairs after the [[Third Hobgoblin War (Sembara)|hobgoblin wars]].

%%^Metadata:names:v1%%
- {name: Old Veltor Road, role: primary, language: Sembaran, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Rinburg, map: world, locator: }
  - {feature: Veltor, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern road alignment and maintained condition; the account recalls repairs after the hobgoblin wars without assigning an exact present-day snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded explicit identity where previously supplied by the filename.
- Added required typed map entries, leaving unsupported locators blank.
- Recorded POV: modern and concise temporal coverage in persistent metadata.

### Validated judgments
- Old Veltor Road is a transparent descriptive compound; [[Veltor]] records the component pronunciation Vel-tor, and no unresolved pronunciation component was established.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required Rinburg and Veltor map entries have blank locators. Supply verified world-map coordinates in the existing `Metadata:map:v1` entries; no endpoint coordinate for these positions was established, and none was inferred from regional geography.
%%^End%%

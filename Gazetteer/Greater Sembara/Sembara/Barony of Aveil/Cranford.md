---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
population: 654
name: Cranford
pronunciation: Cran-ford
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A bustling village which has grown rapidly since 1681 when a bridge was built over the [[Cranmere|Cranmère]]. It has a small unnamed inn which caters to travelers, and the temple of [[The Warlord]] that was destroyed in the [[Undead Attacks in Sembara]].

The most prominent building is the large manor house with an elaborate garden, but second in prominence is the tollhouse complex by the bridge.

%% Roleplaying vibe notes: small place, but bustling enough with travelers that it often feels like someone new is in town; tollhouse complex and the various officials and people of the tollhouse are important but not really made up; the kind of place that has markets every couple of days with some nearby merchants; has to be the kind of place someone might try to buy poison on the side, for example, but not so big that it wouldn't be noticed or that they'd get away it with %%

%%^Metadata:names:v1%%
- {"name":"Cranford","language":"unknown","pronunciation":"Cran-ford","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern, after the temple’s destruction during the Undead Attacks in Sembara; the bridge’s construction in DR 1681 is historical background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; recorded the explicit subject name and existing pronunciation in name metadata, and added a typed settlement map entry and modern temporal metadata.
- Corrected “the was” to “that was” and “a elaborate” to “an elaborate.”

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement’s `Metadata:map:v1` entry has a blank `locator`; the consulted sources do not establish its world-map hex. Supply the verified coordinate as a string in `  - {map: world, locator: "<verified world hex>"}`. Do not infer the position from a nearby river, settlement, or regional map.
%%^End%%

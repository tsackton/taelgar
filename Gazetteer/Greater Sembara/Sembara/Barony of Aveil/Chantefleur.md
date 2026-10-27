---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: fishing village
population: 390
name: Chantefleur
whereabouts: Lake Rin
POV: modern
---
```taelgar-header
```

Chantefleur is a fishing settlement on the north shore of [[Lake Rin]], near the mouth of the [[Auberonne]]. It has the lake's largest docks and a twice-daily ferry to [[Lynthia]].

%%^Metadata:names:v1%%
- {"name":"Chantefleur","language":"unknown","pronunciation":"shahnt-FLUHR","status":"proposed","notes":"Proposed from the French analogue for southern Sembaran place names in [[Languages]]: ch as sh, nasal an approximated ahn, t retained before fleur, and rounded eur approximated uhr with final-phrase stress. The name language and exact in-world phonology are not established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; describes the settlement, docks, and ferry service without a narrower supported date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added primary name metadata with a proposed pronunciation, a typed settlement map entry with its unknown locator left blank, and modern temporal metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed `shahnt-FLUHR` in the name block. It uses the French analogue applicable to southern Sembaran naming in [[Languages]]: `ch` becomes sh, nasal `an` is approximated ahn, the t is retained before fleur, and French rounded `eur` is approximated uhr with final-phrase stress. This is an analogue-informed proposal; the name’s language and exact in-world phonology are not established. If accepted, mark the entry `status: documented` and add `pronunciation: shahnt-FLUHR` to frontmatter.
- [ ] **Warning — metadata.map_location_missing:** The settlement’s `Metadata:map:v1` entry has a blank `locator`; the consulted sources do not establish its world-map hex. Supply the verified coordinate as a string in `  - {map: world, locator: "<verified world hex>"}`. Do not infer the position from a nearby river, settlement, or regional map.
%%^End%%

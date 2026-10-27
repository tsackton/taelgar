---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Snake River
whereabouts:
  - {type: primary, location: Erbalta Plains}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

The Snake River is a long, meandering river that flows east of [[Voltara]] through the grasslands of the [[Erbalta Plains]], forming one of the two great drainage branches of the northern [[Chasa-Nahadi Watershed]]. The Snake River marks the eastern extent of [[Greater Voltara]], and a small [[Chardonian Empire|Chardonian]] fort, the [[Snake River Fort]], guards the one easy crossing. 

Just north of [[Lake Valandros]] it joins the [[Zarnato]]. Major tributaries include the [[Kelvaros]] (draining [[Pykolon Lake]]) and the [[Wild River]].

%%^Metadata:names:v1%%
- {"name": "Snake River", "language": "Common"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "", "map": "world", "locator": ""}
  - {"role": "outlet", "feature": "Zarnato", "map": "world", "locator": ""}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and use; no narrower temporal reading position is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Recorded the existing subject explicitly in frontmatter name.
- Added the required typed map entries; unsupported locator values remain blank.

### Validated judgments
- The complete displayed name is ordinary English; no pronunciation guide is needed.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required river source and outlet entries in Metadata:map:v1 still have blank locator values. The reviewed sources establish identifying features but no verified world-map hexes for these positions. Supply each verified coordinate in its existing `locator` field, for example `locator: "<verified world hex>"`; retain the typed entries and do not infer a hex from a nearby place.
%%^End%%

---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Volta
aliases: [River Volta]
whereabouts:
  - {type: primary, location: Greater Sembara}
  - {type: secondary, location: Volta Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A major river that was historically a border between the [[Sembara|Sembaran]] and [[Zimkova|Zimkovan]] cultural influences. The upper reaches of the Volta in particular have always been a center of [[Kestavo|kestavan]] religious practice. 

 The height of navigation on the Volta is considerably upstream of Tollen, although there are few good anchorages upriver, and the [[Tollen Bridge]] blocks passage of the biggest ships.

%%^Metadata:names:v1%%
- {"name": "Volta", "language": "unknown", "pronunciation": "VOHL-tah", "status": "proposed", "notes": "Regional English reading using the northern Sembaran and Tollish analogues in [[Languages]]: initial v, oh before l, a pronounced ah, and initial stress. A southern French-style vohl-TAH is an alternative; neither the original name language nor its intended stress is established."}
- {"name": "River Volta", "language": "unknown", "pronunciation": "RIV-er VOHL-tah", "status": "proposed", "notes": "Complete alias proposal uses ordinary English River and the same regional analogue-derived proposal as Volta. Regional English reading using the northern Sembaran and Tollish analogues in [[Languages]]: initial v, oh before l, a pronounced ah, and initial stress. A southern French-style vohl-TAH is an alternative; neither the original name language nor its intended stress is established.", "role": "alias"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "", "map": "world", "locator": ""}
  - {"role": "outlet", "feature": "Gulf of Tollen", "map": "world", "locator": ""}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and use; no narrower temporal reading position is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Added the required typed map entries; unsupported locator values remain blank.
- Stored the unresolved pronunciation proposal persistently in the name block; accepted frontmatter pronunciations were preserved.

### Validated judgments
- The central missing dimension is established in the named public sources; the report does not invent the missing account.

### Editorial assessment
**Underdeveloped** — The central missing dimension is the geographical frame of this major regional river: the upper lake country, passage past Tollen, and outlet. A single sourced course sentence fills the identified reference gap; no invented source location or detailed route is required.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required river source and outlet entries in Metadata:map:v1 still have blank locator values. The reviewed sources establish identifying features but no verified world-map hexes for these positions. Supply each verified coordinate in its existing `locator` field, for example `locator: "<verified world hex>"`; retain the typed entries and do not infer a hex from a nearby place.

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `VOHL-tah` in Metadata:names:v1. The northern Sembaran and Tollish English analogues in [[Languages]] support initial v, oh before l, final ah, and initial stress. The southern French option could give vohl-TAH. The original name language and intended stress are unknown; also review the complete alias `RIV-er VOHL-tah`. Accept or revise the proposal, then copy the accepted primary pronunciation to frontmatter and mark the entry documented.

- [ ] **Warning — coverage.established_fact_missing:** The visible account describes cultural borders and navigation but does not identify the major river’s geographical course or outlet. [[Volta Watershed]] and [[Lake Kamchak]] place the lake country on its upper reaches; [[Greater Sembara]] and [[Gulf of Tollen]] establish its passage past Tollen and sea outlet. Add the bounded account: “The upper Volta includes [[Lake Kamchak]]; downstream, the river flows past [[Tollen]] into the [[Gulf of Tollen]].” No exact source or unsupported intervening route is implied.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%

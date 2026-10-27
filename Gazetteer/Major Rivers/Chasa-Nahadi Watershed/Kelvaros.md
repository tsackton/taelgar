---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Kelvaros
pronunciation: KEHL-va-ross
whereabouts:
  - {type: primary, location: Erbalta Plains}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Kelvaros is a small, swift-flowing river that drains [[Pykolon Lake]], south of [[Voltara]], flowing through the southern part of the [[Erbalta Plains]] to the [[Snake River]].

The name derives from the Drankorian word for "torrent".

%%^Metadata:names:v1%%
- {"name": "Kelvaros", "language": "Drankorian", "pronunciation": "KEHL-va-ross", "meaning": "torrent", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Pykolon Lake, map: world, locator: }
  - {role: outlet, feature: Snake River, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography; no narrower dated state is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded a broadly modern article POV and persistent temporal-coverage guidance.
- Added primary name metadata, preserving the accepted pronunciation and established etymology where present.
- Added typed source/outlet map entries, leaving unestablished coordinates blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet `locator` values remain blank in the required map block. The reviewed direct sources do not establish verified world-map coordinates. Fill each existing typed entry with its verified coordinate as a quoted string; retain its source/outlet role and do not infer a hex from the broader whereabouts.
%%^End%%

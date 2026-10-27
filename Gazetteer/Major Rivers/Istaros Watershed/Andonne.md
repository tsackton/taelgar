---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
campaignInfo: []
name: Andonne
whereabouts: Greater Sembara
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Andonne is formed by the confluence of the [[Masance]] and the [[Aursen]], and flows for almost 300 miles until it joins the [[Valmont]] at [[Lake Aeulian]]. The western quarter of the river runs swiftly with numerous rapids, until a particular sequence of rapids and waterfalls known as the Washbasin. Since the Great War, the river, east of the Washbasin, has been ash-choked and corrupted, and unsafe to drink.

%%^Metadata:names:v1%%
- {name: "Andonne", language: "unknown", pronunciation: "ahn-DON", status: "proposed", notes: "Southern Sembaran regional French analogue: nasalized initial an approximated by ahn, final -onne as on with a pronounced n and silent final e, and final phrase stress. The name language and exact in-world phonology are unknown."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: "Masance\u2013Aursen confluence", map: world, locator: }
  - {role: outlet, feature: "Lake Aeulian", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern after the Great War; the visible article describes the river with its eastern waters ash-choked and unsafe to drink, without asserting a later recovery.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Corrected "a particularly sequence" to "a particular sequence" without changing meaning.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** The southern Sembaran French analogue suggests nasalized initial an (approximated as ahn), -onne with a pronounced n and silent final e, and final phrase stress. The exact name language and in-world phonology are unknown. Candidate if accepted: set frontmatter `pronunciation: ahn-DON` and the matching persistent entry pronunciation to `ahn-DON` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Sukal
pronunciation: su-KAHL
whereabouts: Hara Watershed
dm_owner: none
dm_notes: color
POV: modern
---
# Sukal
*(su-KAHL)*
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Sukal is a meandering river that flows from the [[Copper Hills]] east, joining the [[Hara]] on the arid [[Sukal Plains]]. During the dry winter months, the Sukal is often little more than a trickle, but when the monsoon rains fall on the [[Darba Highlands]] it bursts to life.

%%^Metadata:names:v1%%
- {name: Sukal, language: unknown, pronunciation: su-KAHL, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Copper Hills, map: world, locator: }
  - {role: outlet, feature: Hara, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography and recurring seasonal flow; no narrower dated state is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added a documented name entry matching the accepted frontmatter pronunciation, a typed two-ended waterway map block, and a broadly modern temporal viewpoint; normalized frontmatter formatting.

### Validated judgments
- [[Copper Hills]], [[Hara]] and [[Hara Watershed]] corroborate the source, outlet and strongly seasonal flow. The short note performs its river-reference role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required waterway map block now identifies the Copper Hills source and Hara outlet, but both `locator` values remain blank. Supply the two verified world-map positions in `locations: [{role: source, feature: Copper Hills, map: world, locator: VERIFIED_SOURCE}, {role: outlet, feature: Hara, map: world, locator: VERIFIED_OUTLET}]`; the prose does not establish exact hexes, so none were guessed.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The existing `dm_notes: color` may refer to remembered or off-vault information. Confirm that it still applies, or make a separate human-authorized attestation correction; its value is preserved.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Dalinka
pronunciation: DAH-link-ah
whereabouts: Ursk
dm_owner: none
dm_notes: color
POV: modern
---
# Dalinka
*(DAH-link-ah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A river that flows from the [[Yengorza Mountains]] to the [[Green Sea]]. The Dalinka river valley is a fertile agricultural area, centered on the city of [[Yamgov]].

%%^Metadata:names:v1%%
- {name: Dalinka, language: unknown, pronunciation: DAH-link-ah, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Yengorza Mountains, map: world, locator: }
  - {role: outlet, feature: Green Sea, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography and agricultural use of the valley; no narrower speaking position is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added the explicit subject name, persistent name metadata, and broadly modern POV interpretation.
- Added typed river source and outlet map entries, with features taken from the article and position values left blank.

### Validated judgments
- The valley and headwaters account is consistent with [[Yamgov]] and [[Yengorza Mountains]].
- The recorded `DAH-link-ah` pronunciation is preserved as documented; the name language remains unknown.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet entries have blank `locator` values. Supply world-map positions for the Yengorza Mountains source and Green Sea outlet.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. Keep or revise the attestation after checking remembered information or other off-vault sources; no automatic change was made.
%%^End%%

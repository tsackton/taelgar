---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Valmont
aliases: [River Valmont]
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
# Valmont
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Valmont flows south from [[Addermarch]] and, with the [[Andonne]], is one of the primary inflows to [[Lake Aeulian]]. It largely passes through uninhabited land, and forms part of the border of the [[Darkwood]].

%%^Metadata:names:v1%%
- {"name":"Valmont","language":"unknown","pronunciation":"VAL-mont","status":"proposed","notes":"Preferred proposal using the English side of the Sembaran analogues in [[Languages]], regional guidance for Addermarch: short a, initial stress, and sounded final nt. A French-side alternative is val-MOHN, nasalizing the final vowel and omitting final consonants. The name language is unknown; human confirmation is required."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Westcliff, map: world, locator: }
  - {role: outlet, feature: Lake Aeulian, map: world, locator: 14.11.D01}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river course and its place in the upper Istaros network.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries; used the Lake Aeulian coordinate from [[Istaros]] for the outlet and left the Westcliff source locator blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `VAL-mont`. Preferred proposal using the English side of the Sembaran analogues in [[Languages]], regional guidance for Addermarch: short a, initial stress, and sounded final nt. A French-side alternative is val-MOHN, nasalizing the final vowel and omitting final consonants. The name language is unknown; human confirmation is required. Confirm or replace this full-name proposal; if accepted, copy it to frontmatter and mark the existing entry `documented`.

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for source. Fill those blank values with confirmed coordinates, preserving recorded features and roles.
%%^End%%

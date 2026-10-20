---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Rindle
whereabouts:
  - {type: primary, location: Sembara}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# The Rindle
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A tributary of the [[Wistel]], with a confluence west of [[Gowerbourne]].

%%^Metadata:names:v1%%
- {"name": "Rindle", "language": "unknown", "pronunciation": "RIN-dul", "status": "proposed", "notes": "The English-form local tributary names in [[Wistel]], including Ashwell Brook and Holling Brook, favor the English option in the Sembaran analogue in [[Languages]]: initial stress, short i as in pin, and dle as dul with an unstressed vowel. The source language and exact pronunciation remain unestablished."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Wisford, map: world, locator: "12.10.G.24"}
  - {role: outlet, feature: Wistel, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography; no narrower dated state is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded a broadly modern article POV and persistent temporal-coverage guidance.
- Added primary name metadata with a proposed pronunciation and its derivation.
- Added typed source/outlet map entries; recorded the explicit source hex from [[Wistel-Enst Watershed]] and left the uncertain border outlet blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** [[Wistel-Enst Watershed]] gives the source as `12.10.G.24` but places the outlet on the `12.11.A.02/A.06 border`; that does not select one verified outlet hex. Preserve that border evidence and choose the proper supported locator representation before filling the outlet.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `RIN-dul` in the persistent name block. The English-form local tributary names in [[Wistel]], including Ashwell Brook and Holling Brook, favor the English option in the Sembaran analogue in [[Languages]]: initial stress, short i as in pin, and dle as dul with an unstressed vowel. The source language and exact pronunciation remain unestablished. Accept or revise the proposal; if accepted, copy the complete value into frontmatter and mark the existing entry `documented`.
%%^End%%

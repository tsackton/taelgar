---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Velan
whereabouts:
  - {type: primary, location: Addermarch}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: tim
dm_notes: none
POV: modern
---
# The Velan
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Velan is a slow, calm river that rises near the lower faces of [[Westcliff]], swings north through open forest and orchards, and then bends south to meet the [[Aure]] not far from [[Adderfell]]. 

Seasonal rains and snowmelt swell the channel in late spring; in drier months the current slows over gravel bars frequented by herons. Generally unnavigable by all but the smallest river craft, the Velan is dotted with small mills and fords where hamlets have bridged or channeled the flow.

%%

This river is near the main action in Addermarch campaign and I have some future ideas for dungeons to set here but nothing well-formed yet

%%

%%^Metadata:names:v1%%
- {"name": "Velan", "language": "unknown", "pronunciation": "VEH-luhn", "status": "proposed", "notes": "Uses the English option of the Sembaran analogue, which [[Languages]] says is prevalent in Addermarch: initial stress, e as eh, and reduced final an as uhn. The name language is unestablished; a French-style veh-LAHN is an alternative."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "Westcliff", "map": "world", "locator": "13.11.A.17"}
  - {"role": "outlet", "feature": "Aure", "map": "world", "locator": "12.11.F.16"}
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
- Added typed river map entries with the positions explicitly recorded in the corresponding watershed map ledger.
- Stored the unresolved pronunciation proposal persistently in the name block; accepted frontmatter pronunciations were preserved.

### Validated judgments
- The shared comment is unresolved future adventure planning and remains separate from the public account.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `VEH-luhn` in Metadata:names:v1. Uses the English option of the Sembaran analogue, prevalent in Addermarch according to [[Languages]]: initial stress, e as eh, and reduced final an. A French-style veh-LAHN is an alternative; the original name language is unknown. Accept or revise the proposal, then copy the accepted primary pronunciation to frontmatter and mark the entry documented.
%%^End%%

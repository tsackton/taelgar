---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
destroyed: 1720-01-07
name: Eftly
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: 1720s
---
# Eftly
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small sheepherding village along the Great South Road between [[Rinburg]] and [[Dallet]], about 20 miles from [[Rinburg]]. It was depopulated during the [[Undead Attacks in Sembara]].

Before it was ruined, it used to be a common stopping spot on the road between [[Rinburg]] and [[Cleenseau]], and the villagers here would rent out sheep barns and haylofts to passing travelers. There was a temple to [[The Wildling]] here, but it collapsed in the aftermath of the [[Undead Attacks in Sembara]]. 

_Distances:_
* to [[Champimont]], 6 miles
* to [[Essenmer]], 9 miles
* to [[Rinburg]], 21 miles
* to [[Cleenseau]], 39 miles

%% There is some color  in [[The Destruction of Eftly]] %%

%%^Metadata:names:v1%%
- {"name": "Eftly", "language": "unknown", "pronunciation": "EFT-lee", "status": "proposed", "notes": "The English analogue for Sembaran in [[Languages]] supports short e, the written ft cluster, and final ly as lee, with first-syllable stress. No explicit pronunciation or stronger name-language rule was found. Exact in-world pronunciation remains unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the ruined village after the January DR 1720 undead attacks, with its former travel accommodations treated retrospectively; the temple’s later collapse is corroborated by the January 16 background scene.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Added a persistent primary name entry with a proposed pronunciation and its derivation; accepted frontmatter pronunciation is unchanged.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary entry proposes `EFT-lee`. The English analogue for Sembaran in [[Languages]] supports short e, the written ft cluster, and final ly as lee, with first-syllable stress. No explicit pronunciation or stronger name-language rule was found. This is an analogue-informed proposal, not established in-world phonology. Accept or revise it; if accepted, copy the complete pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%

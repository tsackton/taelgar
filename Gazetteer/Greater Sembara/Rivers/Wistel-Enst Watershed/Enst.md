---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on", defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Enst
aliases: [River Enst, Enst River]
whereabouts:
  - {type: primary, location: Sembara}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: mike
dm_notes: none
POV: modern
---
# The Enst
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A major river along the southern border of [[Sembara]]. It is rocky, cold, and wide for much of its length, and has traditionally been a major barrier to movement. It floods often, and is crossed by only two bridges east of the "Three Fingers", where it splits into the [[Enst (North Fork)|North Fork]], [[Enst (Middle Fork)|Middle Fork]], and [[Enst (South Fork)|South Fork]]: the ancient bridge in [[Cleenseau]], and a more recently constructed bridge just north of the confluence with the [[Aure]] at [[Eskbridge]].

It is navigable as far upriver as [[Rinburg]], and there is some riverboat traffic between [[Rinburg]], [[Fellburn]], and [[Eskbridge]], but it is not a river with a lot of boat traffic, unlike some of the other Sembaran rivers. There are few areas with adequate towpaths, and although it is wide and slow in places, the current is still strong enough that rowing or sailing upriver is not easy. Most of the traffic is makeshift boats escorting timber or ceramics to [[Fellburn]] or [[Eskbridge]]. 

The lower reaches of the Enst, in [[Ozabal|Ozabal Swamp]] tend to be marshy and treacherous, and there is little to no river traffic beyond [[Eskbridge]]. 

There are ferries at [[Rinburg]], [[Fellburn]], and [[Stavenford]], amongst other places.

%%^Metadata:names:v1%%
- {name: "Enst", language: "unknown", pronunciation: "ENST", status: "proposed", notes: "Inferred from the documented ENST-bayn in [[Enstbain]], retaining its short e and final nst cluster; the river name itself has no accepted recorded pronunciation."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: "Three Fingers", map: world, locator: }
  - {role: outlet, feature: "Ozabal", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Quoted the existing display text `on` in displayDefaults.linkText so YAML retains its intended string value instead of treating it as a boolean.
- Normalized frontmatter field order and collection formatting while preserving the other parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** The documented ENST-bayn in [[Enstbain]] supports short e and a pronounced final nst cluster. This is component evidence rather than a separately accepted pronunciation for the river. Candidate if accepted: set frontmatter `pronunciation: ENST` and the matching persistent entry pronunciation to `ENST` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

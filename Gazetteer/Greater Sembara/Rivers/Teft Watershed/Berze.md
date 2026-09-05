---
headerVersion: 2023.11.25
lintedAt: "2026-09-05T16:06:33-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Bērze
aliases: [Bērze]
whereabouts:
  - {type: primary, location: Zimkova}
  - {type: secondary, location: Teft Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Bērze
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A swift-flowing mountain river that joins the [[Teft]] just west of the [[Great Chasm]]. It flows south from the [[Sentinel Range|Sentinels]].

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Sentinel Range, map: world, locator: 10.10.D03}
  - {role: outlet, feature: Teft, map: world, locator: 10.10.E09}
%%^End%%

%%^Metadata:names:v1%%
- {name: Bērze, language: unknown, pronunciation: "BEHR-zeh", notes: "Proposed using the Latvian branch of the regional Zimkovan analogue in Languages: long ē, voiced z, final e, and initial stress. The exact name language and in-world sound system are not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added mapped source and outlet from [[Teft Watershed]], a proposed pronunciation, and modern temporal metadata; normalized frontmatter.

### Validated judgments
- The short note adequately identifies the river and its course. [[Teft Watershed]] supplies source `10.10.D.03` and outlet `10.10.E.09`, recorded in canonical locator notation; [[Vilna]] and [[Great Chasm]] corroborate the confluence.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** `BEHR-zeh` is proposed from the Latvian branch of the regional Zimkovan analogue in [[Languages]], preserving the long ē, voiced z, final e, and initial stress. The regional analogue does not establish the name’s in-world language. Accept with `pronunciation: BEHR-zeh` in frontmatter and `status: documented` in the name entry, or revise.
%%^End%%

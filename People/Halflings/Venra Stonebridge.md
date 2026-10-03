---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: Sembaran
born: 1643
gender: male
name: Venra Stonebridge
affiliations:
  - {org: Stonebridges, type: primary}
  - {place: The Crossroads Inn, title: Proprietor, start: 1}
whereabouts: Cleenseau
knownTo: []
dm_owner: none
dm_notes: none
POV: 1720
---
# Venra Stonebridge
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Halflings|halfling]] (he/him), of the [[Stonebridges]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

An elderly halfling and one of the owners of [[The Crossroads Inn]] in [[Cleenseau]] along with [[Willow Stonebridge]] and [[Marigold Stonebridge]]. Often called Grandmother Venra.

%%^Metadata:names:v1%%
- {name: "Venra Stonebridge", language: "unknown", pronunciation: "VEN-rah STOHN-brij", notes: "Preferred adaptation using the English branch of the Sembaran analogue in Languages: short e, pronounced n, two syllables with initial stress; the surname is an English compound. Southern French could instead yield nasalized vahn-RAH. The provisional Igbo halfling analogue does not establish this individual name language.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a Cleenseau campaign-era portrait around DR 1720 of an elderly co-proprietor of the Crossroads Inn; tenure boundaries are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added `knownTo: []`; shared inn ownership alone does not establish a party interaction.

### Validated judgments
- The co-proprietor role and contemporary household context support a DR 1720 portrait; the identity/title discrepancy remains unresolved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `VEN-rah STOHN-brij` in `Metadata:names:v1`. The preferred adaptation uses the English branch of the [[Languages]] Sembaran analogue: short e, pronounced n, initial stress and an English compound surname. A southern French reading could instead use nasalized vahn-RAH. The provisional halfling Igbo analogue does not establish this particular name’s language. These are analogue-informed proposals, not documented in-world phonology. On acceptance, set the entry to `status: documented` and copy the accepted primary pronunciation to frontmatter; no frontmatter pronunciation has been asserted.
- [ ] **Warning — correctness.internal_conflict:** Frontmatter says `gender: male` and the generated header uses he/him, but the visible article calls Venra “Grandmother Venra.” Neither [[Marigold Stonebridge]], [[Willow Stonebridge]], nor [[The Crossroads Inn]] settles the discrepancy. Confirm whether the title, gender, or pronouns are intentional. If the title is correct and female is intended, candidate `gender: female` plus the matching regenerated header; if male and he/him are intended with a conventional title, candidate “Often called Grandfather Venra.” An intentionally gender-independent title is also possible. No identity value has been inferred or changed.
%%^End%%

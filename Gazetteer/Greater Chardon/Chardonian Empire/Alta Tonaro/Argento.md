---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Argento
whereabouts:
  - {type: primary, location: Alta Tonaro}
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Argento
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Argento is the largest city, and provincial capital, of [[Alta Tonaro]]. Founded during the boom years of chalyte mining in the northern [[Chataan Mountains]], its fortunes have declined significantly over the past two generations. Now, its economy depends largely on a few productive silver mines.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: approximately the DR 1740s. Settlement Reference for Argento; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Italian analogue: soft g before e, final o, and penultimate stress. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Argento, language: Chardonian, pronunciation: ar-JEN-toh, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

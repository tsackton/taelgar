---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
population: 850
name: Artevus
whereabouts: Portalia
dm_owner: tim
dm_notes: color
POV: 1740s
---
# Artevus
>[!info]+ Information  
> pop. 850  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Artevus is a small coastal town in northern [[Portalia]], primarily a minor market town for local fisherfolk. A relatively poor town, and somewhat dilapidated, Artevus is something of a sleepy backwater. 

The docks and the market square, with the nearby temple of the [[Mos Numena]], are the most notable local landmarks. A few quiet inns and taverns line the edge of the market square, near the docks, but are rarely busy.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: approximately the DR 1740s. Settlement Reference for Artevus; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Classical Latin analogue: v read as w and penultimate stress. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Artevus, language: Chardonian, pronunciation: ar-TEH-woos, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

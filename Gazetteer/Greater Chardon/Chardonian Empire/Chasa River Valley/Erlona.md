---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Erlona
whereabouts: Chasa River Valley
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Erlona
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% incorporate notes from OneNote %%

Erlona is the capital of the Chasa Valley province, a rich and powerful province given the agricultural wealth of the valley. This far upriver, there is less wine, but the land is fertile pasture with many cattle and dairy farms.

%%SECRET[v2:c1ffae5c3746bb8f11e475b402da61e4]%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: approximately the DR 1740s. Settlement Reference for Erlona; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.
- Applied high-confidence spelling, punctuation, title, or light-clarity corrections.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Italian analogue: open vowels and penultimate stress. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Erlona, language: Chardonian, pronunciation: ehr-LOH-nah, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Warning — status.disposition:** Existing status `status/cleanup/text` remains in force. Its underlying name, cleanup, review, game-update, stub, or work-in-progress question requires human disposition; the lint did not alter it.
- [ ] **Warning — coverage.established_fact_missing:** Session 50 establishes Erlona as a substantial city with a large coliseum; the visible prose still omits the confirmed landmark. Candidate: add a sentence identifying the large coliseum as a prominent landmark, while leaving unplayed details in private material.
%%^End%%

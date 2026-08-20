---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Luminatia
whereabouts: Chardonian Empire
dm_owner: none
dm_notes: color
POV: "1748"
---
# Luminatia
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village near [[Lake Valandros]].

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: settlement reference
povNotes: "Accuracy range: DR 1748. Minimal settlement reference at the time of the Session 86 contact; broader history and later state are not established here."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Latin/Italian analogue: pure vowels and stress on na. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Luminatia, language: Chardonian, pronunciation: loo-mee-NAH-tee-ah, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Suggestion — dm.notes_no_local_evidence:** The positive `dm_notes` attestation has no matching local-only file. Confirm whether it represents off-vault or remembered information; retain it unless a human decides otherwise.
- [ ] **Warning — coverage.established_fact_missing:** Session 86 establishes an inn run by Livia and reduced traveler traffic in DR 1748. Candidate: add a minimal DR 1748 sentence noting the village's sole inn and reduced traffic; keep family details only if useful to the location article.
%%^End%%

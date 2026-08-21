---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
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

%%^Metadata:names:v1%%
- {name: "Luminatia", role: "primary", language: "Chardonian", pronunciation: "loo-mee-NAH-tee-ah", notes: "Latin/Italian analogue: pure vowels and stress on na.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: DR 1748. Minimal settlement reference at the time of the Session 86 contact; broader history and later state are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** Session 86 establishes an inn run by Livia and reduced traveler traffic in DR 1748. Candidate: add a minimal DR 1748 sentence noting the village's sole inn and reduced traffic; keep family details only if useful to the location article.
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only _DM_ notes found; verify dm_notes. The positive attestation may still represent remembered information or another off-vault source, so never remove it automatically.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Luminatia — loo-mee-NAH-tee-ah` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: inn
typeOfAlias: tavern
name: The Drunken Dolphin
whereabouts: Castrella
dm_owner: tim
dm_notes: color
POV: 1748
---
# The Drunken Dolphin
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A bustling sailor's tavern on the docks in [[Castrella]]. 

%%
popular, relatively high-quality food, less of a rowdy place, known for singers
%%

%%^Metadata:names:v1%%
- {name: "The Drunken Dolphin", role: "primary", language: "Common", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of the tavern during the Silver Tempests' information-gathering in Castrella; earlier and later operation are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Validated judgments
- Shared nonpublic comments and Campaign:none material were reviewed; no additional public-safe candidate met the reporting threshold beyond any task below.

### Open findings

- [ ] **Warning — consistency.cross_note:** Session 98 calls the Drunken Dolphin a rowdy sailor's tavern, while the note's hidden planning comment says it is less rowdy. Candidate: decide whether Session 98's played description or the later planning note governs the tavern's tone, then align the visible sentence.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only _DM_ notes found; verify dm_notes. The positive attestation may still represent remembered information or another off-vault source, so never remove it automatically.

%%^End%%

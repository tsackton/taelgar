---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: cured of lycanthropy, person: Riswynn, date: 1748-07-03}
born: null
gender: female
name: Avani
affiliations:
  - {org: Fraternity of the Empty Moon, start: "1748-04", end: 1748-07-03}
whereabouts: Tokra
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Dunmari Werewolf Woman
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Cured of lycanthropy by [[Riswynn]] on July 3rd, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

The unnamed woman who was cured of lycanthropy by [[Riswynn]], one of the few survivors of the [[Fraternity of the Empty Moon]].

%%^Metadata:names:v1%%
- {name: Avani, language: unknown, pronunciation: uh-VUH-nee, notes: "Proposed from the Hindi analogue for Dunmari in [[Languages]]: short a vowels as uh, v near v/w, and final i as ee; the stress guide is tentative, and the name's in-world language is not independently established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot after the cure of lycanthropy. The original qualification on the Fraternity of the Empty Moon affiliation's 1748-04 start is preserved: "start date an estimate".
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the existing campaignInfo and normalized frontmatter formatting.
- Preserved the inline YAML qualification “start date an estimate” in `povNotes`, explicitly tied to the Fraternity of the Empty Moon affiliation's 1748-04 start, so formatting does not discard it.
- Added a proposed pronunciation in persistent name metadata and recorded the DR 1748 viewpoint.

### Validated judgments
- The source review distinguishes this survivor from the identically named captain addressed in [[Archives Letter]].

### Open findings

- [ ] **Warning — metadata.identity_conflict:** The filename and `name: Avani` identify the woman, but the visible title is “Dunmari Werewolf Woman” and the body calls her “unnamed.” [[Session 39 (DuFr)]] links this woman to Avani but does not speak her name in the narrative. Confirm whether Avani is her adopted name or an editorial placeholder. If adopted, use `# Avani` and replace the body opening with “Avani is a Dunmari woman who was cured of lycanthropy by [[Riswynn]], one of the few survivors of the [[Fraternity of the Empty Moon]].” Do not conflate her with the captain in [[Archives Letter]].
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the proposed pronunciation `uh-VUH-nee`. The proposal uses the Hindi analogue for Dunmari in [[Languages]]: both written a vowels are rendered as short uh, v is near v/w, and final i is rendered ee; penultimate emphasis is a tentative reader aid, not an adopted in-world stress rule. No accepted pronunciation or independently established name language was found. If accepted, copy the pronunciation to frontmatter and mark the name entry documented.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No matching `_DM_` notes found; verify `dm_notes: color`. The mechanical candidates were a name list and a different person's correspondence, so neither validates this woman's attestation. Retain the field unless a human confirms a change; it may refer to off-vault information.
%%^End%%

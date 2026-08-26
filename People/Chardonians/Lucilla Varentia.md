---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/gameupdate/gl, status/check/lint]
species: human
ancestry: Chardonian
gender: female
title: Commander
campaignInfo:
  - {campaign: grli, type: met, date: 1747-11-18}
name: Lucilla Varentia
aliases: [Lucilla]
affiliations:
  - {type: leader, title: Commander, org: Varentia’s Camp}
whereabouts: Varentia’s Camp
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1747
---
# Commander Lucilla Varentia
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on November 18th, 1747 in [[Varentia's Camp]], the [[Northern Provinces]], the [[Chardonian Empire]] %%^End%%

%% need to fix afiliation and whereabouts when fort is named; need to update to 1752 or add POV tag %%

Commander Lucilla Varentia is an officer of the [[Chardonian Legion]] who commands a [[Varentia's Camp|frontier garrison]] east of [[Voltara]].


%%  Lucilla's age, earlier career, exact military formation, formal rank beyond commander, or other details are not established %%

%%^Metadata:names:v1%%
- {name: Lucilla Varentia, language: Chardonian, pronunciation: loo-KIL-lah vah-REN-tee-ah, notes: "The surname follows the documented pronunciation on [[Varentia's Camp]]; the given name uses the Latin side of the Chardonian Italian or Latin analogue in [[Languages]], with Italian loo-CHEEL-lah as an alternative.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 snapshot of Lucilla commanding the frontier garrison encountered by the Silver Tempests; her later position and history are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized the Great Library campaign code in `campaignInfo` and the campaign block, replaced the obsolete `Voltara Garrison 2` display alias with [[Varentia's Camp]], and added `knownTo: [grli]`.
- Added `Metadata:names:v1` with a proposed Chardonian pronunciation and added `POV: 1747` with persistent temporal coverage metadata.
- Canonicalized frontmatter ordering and collection formatting.

### Validated judgments
- The sole prepared local-only candidate is not a match for this subject, so it does not challenge `dm_notes: none`.
- `status/gameupdate/gl` is not assessable from current evidence: no source establishes Lucilla's later position, and a human must decide whether to preserve the DR 1747 snapshot or develop a later account.
- The visible note is sufficient for its present reference role.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new `Metadata:names:v1` entry proposes **loo-KIL-lah vah-REN-tee-ah**. The surname follows the documented pronunciation on [[Varentia's Camp]]; the given name uses a Latin reading under the Chardonian Italian-or-Latin analogue in [[Languages]], with Italian **loo-CHEEL-lah** as an alternative. Review the proposal; if accepted, add the preferred full pronunciation to frontmatter and change the entry to `status: documented`, or revise it.
- [ ] **Warning — status.questioned:** `status/cleanup/metadata` appears tied to the hidden reminder about naming the fort and adding a POV. The staged metadata now resolves the camp relationships and records the DR 1747 viewpoint. Remove the tag if no other metadata cleanup remains, or retain it with a new specific explanation.
- [ ] **Suggestion — editorial.shared_material_redundant:** The hidden reminder `need to fix afiliation and whereabouts when fort is named; need to update to 1752 or add POV tag` is now redundant with the resolved camp metadata and `POV: 1747`. Remove that comment; if a DR 1752 update is still intended, replace it with a specific source-backed editorial note.
%%^End%%

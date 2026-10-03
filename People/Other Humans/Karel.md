---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Urskan
gender: male
name: Karel
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Karel
>[!info]+ Biographical Info  
> An [[Ursk|Urskan]] [[Humans|human]] (he/him)

%% needs campaign info, whereabouts %%

Karel is a merchant who regularly travels between [[Zvervinka]] and [[Praznitsky]], bringing goods from the monster markets to the port for sale. 

%%^Metadata:names:v1%%
- {"name": "Karel", "language": "unknown", "pronunciation": "KAH-ryel", "status": "proposed", "notes": "Urskan context supplies the Russian analogue in [[Languages]]; proposed with hard k, open stressed a, and softened r before e. Initial stress is tentative rather than an established name-specific rule; the name's source language is unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Karel as an active merchant, corroborated by his caravan journey in DR 1749; the beginning and end of this trading career are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit `name: Karel` and `knownTo: [dufr]` from the party's journey with him in [[Session 95 (DuFr)]].
- Added persistent name metadata with a proposed pronunciation and a 1740s POV and temporal interpretation; normalized frontmatter.

### Validated judgments
- `status/cleanup/metadata` remains supported: the authored reminder requests campaign and whereabouts information, and historical location metadata remains unfinished. No permanent home has been inferred from ancestry.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace `KAH-ryel`. [[Languages]] supplies a Russian analogue for the Urskan context; this proposal uses hard `k`, open stressed `a`, and softened `r` before `e`. Initial stress and the exact source language are not established. If accepted, copy the pronunciation to frontmatter and mark the entry `documented`.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No confirmed `_DM_` notes found; verify `dm_notes: color`. Retain the attestation if useful information remains in another private source or in someone's head; only a human should change it.
- [ ] **Suggestion — metadata.requested_completion:** The comment “needs campaign info, whereabouts” remains partly unresolved. [[Session 95 (DuFr)]] dates the party's travel with Karel from Zvervinka on DR 1749-04-20 to Volya on DR 1749-04-23, without establishing his permanent home. To capture that bounded history, consider `campaignInfo: [{campaign: dufr, type: traveled with, date: 1749-04-20}]` and `whereabouts: [{type: away, start: 1749-04-20, end: 1749-04-23, location: traveling from Zvervinka to Volya}]`; then review the reminder and `status/cleanup/metadata` rather than inventing a home.
%%^End%%

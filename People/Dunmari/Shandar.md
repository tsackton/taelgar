---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo: []
born: null
gender: male
name: Shandar
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Shandar
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)

%% needs campaign info, born, whereabouts %%

%%^Campaign:dufr%%
An old Dunmari man who spent many years as [[Agata]]'s table, until [[Session 30 (DuFr)|freed]] by the Dunmar Fellowship. 
%%^End%%

%%SECRET[v2:93212a210e3fdd6686ee8e2a110f7801]%%

%%^Metadata:names:v1%%
- {name: Shandar, language: Dunmari, pronunciation: shahn-DAAR, notes: "Dunmari is inferred from the subject’s naming context. Hindi-informed proposal using Languages: sh + broad ah vowels + lightly tapped r; final stress and vowel lengths are tentative.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Shandar as an old man newly freed from Agata in June 1748; the visible note recalls his captivity but does not describe his later recovery or life.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting.
- Added `knownTo: [dufr]` from the existing campaign interaction evidence.
- Added a proposed name entry and supported `POV`/`povNotes` metadata.

### Validated judgments
- Matching local DM sources support the existing positive `dm_notes` attestation; its value was preserved.
- Reviewed the SECRET block and preserved its local-only contents.
- `status/cleanup/metadata`: not assessable. The comment requests birth, whereabouts, and campaign information; `knownTo` is now recorded, but the remaining intended scope and a birth date are not established. The tag was preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry for Shandar remains `status: proposed`. The proposed `shahn-DAAR` uses the Hindi side of the Dunmari analogue in [[Languages]] (Hindi or other Indo-Iranian, including Persian): sh as in ship, broad ah vowels, a lightly tapped r, and tentative final stress. Exact in-world vowel lengths and stress are unrecorded, so this remains a proposal. Confirm or revise the pronunciation and inferred name language; if accepted, copy `pronunciation: shahn-DAAR` to frontmatter and mark the entry `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%

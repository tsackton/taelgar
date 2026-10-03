---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: mentioned to, date: 1748-03-29, wParty: "<met:U> <person:U> on <target>"}
gender: male
name: Devana
whereabouts:
  - {type: home, location: Karawa Desert}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Devana
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Mentioned to the [[Dunmar Fellowship]] on March 29th, 1748 %%^End%%

%% need to decide how to track campaign info for people party heard of but never met%%

A Dunmari pastoralist.

%%^Date:1748%%

* (DR:: 1748-03-15) Devana's family was attacked by marauding axebeaks, supernaturally enraged by an ancient amulet from the Great War, which had been buried inactive for centuries until uncovered by [[Arcus]] in the [[Dunmari Fort (Gomat)|old Dunmari fort]] east of [[Gomat]]. One of his sons and nearly half his animals were killed in this attack (date is approx).

%%^End%%

%%SECRET[v2:036492c638abaccea3874a73df632ac6]%%

%%^Metadata:names:v1%%
- {name: Devana, language: Dunmari, pronunciation: deh-VAH-nah, notes: "Dunmari is inferred from the subject’s naming context. Hindi-informed proposal using Languages: deh + broad VAH + nah, with a light v/w consonant; vowel length and stress are tentative.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a pastoralist of the 1740s, with a separately dated account of the attack on his family in March 1748; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting.
- Canonicalized the equivalent `DuFr` campaign code to `dufr` in campaignInfo and the existing header block.
- Added `knownTo: [dufr]` from the existing campaign interaction evidence.
- Added a proposed name entry and supported `POV`/`povNotes` metadata.

### Validated judgments
- Matching local DM sources support the existing positive `dm_notes` attestation; its value was preserved.
- Reviewed the SECRET block and preserved its local-only contents.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry for Devana remains `status: proposed`. The proposed `deh-VAH-nah` uses the Hindi side of the Dunmari analogue in [[Languages]] (Hindi or other Indo-Iranian, including Persian): d and n as written, a light v/w sound, a steady e vowel rendered deh, broad ah vowels and tentative middle stress. The spelling does not settle vowel lengths or stress, so this remains a proposal. Confirm or revise the pronunciation and inferred name language; if accepted, copy `pronunciation: deh-VAH-nah` to frontmatter and mark the entry `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Clues in Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 2-3/Into the Wild Part 2]]
%%^End%%

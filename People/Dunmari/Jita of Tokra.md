---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-06}
born: 1713
gender: female
name: Jita
whereabouts:
  - {type: home, location: Varashan}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Jita
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 6th, 1748 in the [[Varashan]], [[Dunmar]] %%^End%%

A Dunmari herder living on the northern plains, north of Tokra. Niece of [[Saka]], and has generally taken charge of helping Saka around camp.

%%^Metadata:names:v1%%
- {name: Jita, language: unknown, pronunciation: JEE-tah, notes: "Proposal from the Dunmari cultural context and the Hindi analogue in Languages: j as in English judge, i as ee, dental t, and final a as ah; the long i and first-syllable emphasis are tentative because the spelling does not encode vowel length or stress.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Jita as Saka's niece and helper on the plains north of Tokra, anchored by the July 1748 encounter; her earlier and later circumstances are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` from the existing campaign interaction.
- Added persistent name metadata with a proposed pronunciation, plus `POV: 1740s` and its temporal interpretation.

### Validated judgments
- [[Session 40 (DuFr)]] corroborates Jita's defining role as Saka's niece and helper. This brief account is sufficient for that minor reference role; she is distinct from the historical ruler [[Jita]].

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `JEE-tah` in `Metadata:names:v1`. The Dunmari cultural context points to the Hindi or other Indo-Iranian (Persian) analogue in [[Languages]]; this proposal follows Hindi, with j as in “judge,” i as “ee,” dental t, and final a as “ah.” The spelling supplies no vowel-length or stress marks, so the long i and first-syllable emphasis are tentative; a short-i reading remains possible. Accept or revise the proposal, then copy an accepted pronunciation to frontmatter and mark the entry documented. The name's in-world source language remains unknown.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. It may represent remembered information or another off-vault source. Retain the attestation unless its owner decides no useful private information remains.
%%^End%%

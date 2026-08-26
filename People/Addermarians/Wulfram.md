---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Addermarian
campaignInfo:
  - {campaign: adma, type: discovered, date: 1715-04-28}
gender: male
died: 1715-03-29
name: Wulfram
affiliations:
  - {org: Torvaine Watch, title: temple steward, type: member}
whereabouts:
  - {type: home, location: Torvaine Watch}
knownTo: [adma]
dm_owner: none
dm_notes: none
POV: modern
---
# Wulfram
>[!info]+ Biographical Info  
> An Addermarian [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:adma%% Discovered by the [[Addermarch Mercenaries]] on April 28th, 1715 in [[Torvaine Watch]], the [[Torvaine Forest]], [[Addermarch]] %%^End%%

Wulfram was the temple steward of [[The Warlord]] at [[Torvaine Watch]], who urged the containment of the [[Serpentine Dagger]]. He tended the chapel and advised the garrison on matters of faith and honor. When the cursed dagger appeared, he urged it be locked away, but was killed in the confrontation created by the dagger's cursed influence.

%% DM (sources)

Letter: [[Session 2 - DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Wulfram, language: Addermarian, pronunciation: WULL-frum, notes: "Proposed from the English-dominant Addermarch analogue: initial W retained, short u in Wul-, and an unstressed final syllable.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account of Wulfram's service and death at Torvaine Watch in DR 1715; no other life periods are described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and temporal-POV metadata.
- Corrected a duplicated space in the final sentence.

### Validated judgments
- The shared source pointer was reviewed and retained.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The article identifies Wulfram as steward of [[The Warlord]], while its cited [[Session 2 - DM Notes]] says the Torvaine Watch chapel was dedicated to [[The Mother]]. Resolve which source controls. If the cited source is correct, use: Wulfram was the temple steward of [[The Mother]] at [[Torvaine Watch]].
- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation WULL-frum follows the English-dominant Addermarch analogue, retaining initial W, a short vowel in the first syllable, and an unstressed final syllable. Accept it by moving it to frontmatter and marking the name entry documented, or replace it with the intended pronunciation.
%%^End%%

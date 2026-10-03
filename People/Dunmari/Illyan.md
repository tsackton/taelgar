---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-02}
born: 1708
gender: male
name: Illyan
whereabouts:
  - {type: away, start: 1748-06-03, end: 1748-12-14, linkText: camped near, location: Tokra, format: "<name:q>"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Illyan
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 2nd, 1748 near [[Tokra]], in [[Dunmar]] %%^End%%

A commander in the army of [[Nayan Karnas]]. Stationed outside [[Tokra]] during the [[Summer Gnoll Raids of 1748]] and the [[Sibling War]]. Fought in the [[Battle of Tokra]]. 

%% Notes
Commander of Dunmari army. Has a ring to detect scrying and similar magic.
%%

%%^Metadata:names:v1%%
- {name: Illyan, language: Dunmari, pronunciation: il-YAHN, notes: "Dunmari is inferred from the subject’s naming context. Indo-Iranian-informed proposal using Languages: short il + y glide + broad YAHN; held l, vowel length and final stress are tentative.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of Illyan as an army commander during the fighting around Tokra, including the December battle; his later command and whereabouts are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting.
- Added `knownTo: [dufr]` from the existing campaign interaction evidence.
- Added a proposed name entry and supported `POV`/`povNotes` metadata.

### Validated judgments
- Matching local DM sources support the existing positive `dm_notes` attestation; its value was preserved.
- The visible command and Battle of Tokra service fit a DR 1748 viewpoint.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry for Illyan remains `status: proposed`. The proposed `il-YAHN` uses the Hindi or other Indo-Iranian (Persian) analogue for Dunmari in [[Languages]]: short initial i, a held l, y as a glide, broad ah, and tentative final stress. The spelling does not settle vowel length or stress, so this remains a proposal. Confirm or revise the pronunciation and inferred name language; if accepted, copy `pronunciation: il-YAHN` to frontmatter and mark the entry `status: documented`.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
%%^End%%

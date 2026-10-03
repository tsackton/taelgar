---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-01}
  - {campaign: dufr, type: last seen, date: 1748-07-09}
born: 1695
title: Chief Archivist
gender: male
name: Ardan
affiliations:
  - {type: leader, place: Archives, start: 1737}
whereabouts: Tokra
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Chief Archivist Ardan
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 1st, 1748 in [[Tokra]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

The middle-aged Dunmari Head Archivist at the [[Tokra]] [[Archives]]. Cautious to a fault and rather uninterested in administration, allowing many basic functions of the [[Archives]] to drift into disorganization and uselessness through lack of attention during his tenure. 
%%^Date:1748%%
As of mid-July 1748, he has allowed [[Govir]] to take over some of the administrative burden at the Archives, at the urging of [[Dunmar Fellowship]], and has secured funds for [[Govir]] to hire additional scribes and clerks. 
%%^End%%

%%SECRET[v2:9bb5b4ea7265e666fe346d2d020ab7a0]%%

%%^Metadata:names:v1%%
- {name: Ardan, language: Dunmari, pronunciation: ar-DAHN, status: proposed, notes: "Proposal using the Persian option of the Dunmari analogue in Languages: two syllables with plain r and d, broad final ah, and final stress. The name has no recorded pronunciation; the Hindi option could instead favor AR-dun, so vowel length and stress need confirmation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Ardan as the middle-aged Chief Archivist in Tokra, with a dated paragraph adding his July 1748 delegation of some administrative work to Govir; the prose does not establish how long that arrangement lasts.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` from the existing campaign interactions.
- Added a proposed name pronunciation and recorded `POV: 1740s` with temporal coverage guidance.

### Validated judgments
- The visible account gives a proportionate description of his role, management, and delegation to Govir. [[Session 35 (DuFr)]], [[Session 41 (DuFr)]], and [[Letter from Govir]] support that account without requiring a log of routine encounters.
- Confirmed local evidence supports the existing positive `dm_notes` attestation; the SECRET block was reviewed and preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed `ar-DAHN` in `Metadata:names:v1`. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue. The preferred Persian-informed reading uses two syllables, plain r and d, broad final ah, and final stress; a Hindi-informed `AR-dun` is also plausible. Neither stress nor vowel length is documented for this name. If accepted, set `pronunciation: ar-DAHN` in frontmatter and change the entry to `status: documented`; otherwise record the accepted reading.
- [ ] **Warning — temporal.date_scope:** The `Date:1748` block exposes the new administrative arrangement from the start of the year, although [[Session 41 (DuFr)]] places Ardan's agreement on July 9, 1748. Replace only its opening marker with `%%^Date:1748-07-09%%`, retaining the paragraph and closing marker. This visibility change requires human approval.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Lakan Monastery (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 38]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 39]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Archive Mysteries]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
%%^End%%

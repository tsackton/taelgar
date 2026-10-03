---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/text, status/check/lint]
species: human
ancestry: Sembaran
born: 1537
gender: male
died: 1561-01-17
title: King
name: Bertram II
affiliations:
  - {place: Sembara, title: High King, start: 1555}
  - {place: Ardlas, title: High King, start: 1555}
  - {place: Lavnoch, title: High King, start: 1555}
  - {place: Breva, title: High King, start: 1555}
  - {org: House of Sewick, type: primary}
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# King Bertram II
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Sewick]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

The eldest child of [[Reginald]], he was a ruler of Sembara in the 1550s. 

%% 
[[Bertram II]], after his step-grandmother’s death in 1559, gathers a small force of knights, and without the backing of the Royal Council or any great thought to supply chains, logistics, or military strategy, rides north to aid the barons of Lavnoch and Ardlas against the evil threat. He dies in battle in the deadly winter of 1560, when the tide of battle is turned but great losses were suffered.

Young irresponsible, never marries and dies young in battle

Integrate notes from sembara history here 

%%

%%^Metadata:names:v1%%
- {"name": "Bertram II", "role": "primary", "language": "Sembaran", "notes": "Sembaran regnal form inferred from the subject’s dynasty and realm; the ordinary personal name and regnal numeral need no pronunciation guide.", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective record of Bertram’s sixteenth-century rule and death; the shared draft and reign metadata retain chronology requiring human reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name block and article POV with a temporal-coverage note.
- Added knownTo: [], since no reviewed source establishes campaign knowledge.

### Validated judgments
- status/cleanup/text is supported: the defining campaign remains in a shared working draft, with a chronology requiring reconciliation.

### Editorial assessment
**Underdeveloped**. The visible note omits the northern campaign and battlefield death that define Bertram’s short reign, while the accession date disagrees across notes. Resolve that date and add one short campaign-and-succession paragraph; the shared draft’s characterization should remain tentative unless adopted.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — correctness.cross_note_conflict:** All four ruler affiliations begin in DR 1555, but [[Timeline of Sembaran History]] records Bertram’s coronation in winter DR 1552 and the end of Jane’s regency in winter DR 1553. The timeline separately warns that the highland political framework needs revision. Resolve the Sembaran accession first (candidate `start: 1552` if that chronology is retained), and review Ardlas, Lavnoch and Breva individually rather than applying one date to all four claims.
- [ ] **Warning — coverage.established_fact_missing:** [[Timeline of Sembaran History]] records Bertram riding north after [[Jane of Tollen]] died in DR 1559 and dying in the [[Sentinel Range War]] in DR 1561. The visible article records only parentage and a decade of rule. Copy-ready addition: “After [[Jane of Tollen]] died in DR 1559, Bertram rode north to aid [[Ardlas]]. He died in battle during the [[Sentinel Range War]], and [[Blanche I]] succeeded him in DR 1561.” The shared draft’s “winter of 1560” may name the winter spanning 1560–1561; clarify that wording when integrating the draft rather than silently changing the precise death metadata.
%%^End%%

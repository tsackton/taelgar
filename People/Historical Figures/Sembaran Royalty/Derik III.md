---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T13:33:35-04:00"
lintVersion: "3.4"
tags: [person, status/cleanup/metadata, status/review, testcase, status/check/lint]
species: human
ancestry: Sembaran
born: 1484
gender: male
title: King
died: 1549
name: Derik III
affiliations:
  - {org: Vostok, type: leader, title: Prince of the North, start: 1511, end: 1519}
  - {org: Sembara, type: leader, title: High King, start: 1519}
  - {org: Tyrwingha, type: leader, title: High King, start: 1519}
  - {org: Vostok, type: leader, title: High King, start: 1519}
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# King Derik III
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

%% the metadata / affiliations need to be updated to reflect current thinking about history; important figure with more details available so note could be expanded; note date of High Prince of the North is based on end of [[Vimfrost's War]], per that note %%

The king of Sembara during the [[Great War]]; of the [[House of Sewick]]. He reigned from his mother [[Charlotte I|Charlotte I's]] death in DR 1519 until his death, shortly after the end of the Great War, in DR 1549. 

He is known as one of the greatest kings in Sembaran history, a hero and legendary commander during the Great War, and the savior of his kingdom.

He had two sons ([[Reginald]] and [[Hugh of Wisenfold|Hugh]]) with his first wife, [[Sarabet]], and one son ([[Bertram I|Bertram]]) with his second wife, [[Jane of Tollen]]. 

Mostly due to the influence of his powerful second wife, [[Bertram I|Bertram]] succeeds him upon his death.

%%^Metadata:names:v1%%
- {name: Derik III, role: regnal, language: Sembaran, notes: "Sembaran regnal name; the ordinary reading of Derik and the regnal number does not require a separate pronunciation guide.", status: inferred}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective summary of Derik III's life and reign from DR 1484 to 1549; the visible account remains much less detailed than his historical importance.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Editorial assessment
**Underdeveloped**. The visible note identifies Derik III's reign, reputation, marriages, and succession, but it omits the established pre-reign campaign against [[Vimfrost]] that first demonstrates his regional importance, and the vault still lacks an adopted, concrete account of what his leadership during the [[Great War]] actually consisted of or how it shaped Sembara. The smallest useful scope is one source-grounded paragraph on Vimfrost's War and one bounded account of his Great War leadership and consequences once that material is invented or adopted.

### Applied changes
- Added required `knownTo: []`, persistent regnal-name metadata, and a modern retrospective temporal frame.

### Validated judgments
- `status/cleanup/metadata` is supported by the note's own unresolved metadata comment.
- `status/review` is supported by the same unresolved historical and metadata work.
- The shared comment is an editorial source pointer and planning note, not public canon.
- Generic local-only `_DM_` name matches do not justify changing `dm_notes: none`.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Vimfrost's War]] establishes a defining pre-reign achievement that the biography omits. Copy-ready addition: `Before taking the Sembaran throne, Derik III helped lead the allied forces of Sembara, Vostok, Kaldhalla, and their dwarven and stoneborn allies to defeat the dragon [[Vimfrost]]; the campaign also saw part of the ancient [[Grastenvakt|Gråstenvakt]] rediscovered and repaired.`
- [ ] **Suggestion — editorial.note_underdeveloped:** Develop a concrete account of Derik III's leadership during the [[Great War]] and its consequences for Sembara. The adopted [[Great War]] and [[Battle of Urlich Pass]] notes establish the conflict and its outcome but do not yet establish Derik III's specific actions, so this material requires human invention or adoption rather than a copy-ready factual insertion.
%%^End%%

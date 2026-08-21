---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T15:58:36-04:00"
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
**Underdeveloped**. The visible note identifies Derik III's reign, reputation, marriages, and succession, but it omits two established parts of his military career: the pre-reign campaign against [[Vimfrost]] and his death fighting near [[Valarin]] during the [[Bloodlust Wars]]. Separately, the vault still lacks an adopted, concrete account of what Derik III personally did during the [[Great War]] to earn his reputation as a legendary commander and savior. The smallest useful scope is a concise sourced addition covering the established prewar and postwar facts, plus one bounded account of his Great War command once that material is invented or adopted.

### Applied changes
- Added required `knownTo: []`, persistent regnal-name metadata, and a modern retrospective temporal frame.

### Validated judgments
- `status/cleanup/metadata` is supported by the note's own unresolved metadata comment.
- `status/review` is supported by the same unresolved historical and metadata work.
- The shared comment is an editorial source pointer and planning note, not public canon.
- Confirmed local-only matches are listed for review without disclosing their contents: [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]] and [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Northern Green Sea - DM Notes]]. Their presence does not by itself justify changing `dm_notes: none`.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Vimfrost's War]] establishes Derik III's defining pre-reign victory, while [[Hobgoblin Movements After Cha'Mutte]] and [[Timeline of Sembaran History]] place his death in fighting near [[Valarin]] during the [[Bloodlust Wars]], with the exact wider war chronology still under review. Copy-ready addition: `Before taking the Sembaran throne, Derik III helped lead the allied forces of Sembara, Vostok, Kaldhalla, and their dwarven and stoneborn allies to defeat the dragon [[Vimfrost]]; the campaign also saw part of the ancient [[Grastenvakt|Gråstenvakt]] rediscovered and repaired. In DR 1549, he was killed fighting the Iron Fang hobgoblins near [[Valarin]] during the [[Bloodlust Wars]].`
- [ ] **Suggestion — editorial.note_underdeveloped:** Develop the specific actions and command decisions during the [[Great War]] that earned Derik III his visible reputation as a legendary commander and savior. The adopted [[Great War]] and [[Battle of Urlich Pass]] notes establish the conflict, Sembaran participation, and the outcome, but not Derik III's individual role; the established prewar and postwar endpoints above do not supply this missing transition.
%%^End%%

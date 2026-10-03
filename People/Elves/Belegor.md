---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/check/lint]
species: elf
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-09-30, type: met}
born: 1468
ka: 36
gender: male
timelineDescriptor: Belegor
name: Belegor
pronunciation: beh-leh-GOR
whereabouts:
  - {type: home, start: "", end: 1712, location: Ainumarya}
  - {type: away, start: 1733-01-01, end: "", location: Elderwood}
  - {type: away, start: 1748-08-01, end: "", location: "Te'kula village"}
  - {type: away, start: 1748-09-30, end: "", location: "Te'kula village"}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Belegor
*(beh-leh-GOR)*
>[!info]+ Biographical Info
> An [[Elves|elf]] (he/him), ([[Elven Cycle of Generations|ka]] 36)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on September 30th, 1748 in [[Neshet|Te'kula village]], the [[Elderwood]], [[Ainumarya]] %%^End%%

Belegor is a solitary [[Elves|elf]] wanderer, who has travelled across the forests of the western region of Taelgar for many years, not wanting to hide in isolation as many of his generation chose after The [[Great War]].
## Overview

Belegor is an [[Elves|elf]] of the 36th ka, the generation that came of age during the [[Great War]]. He chose to wander in his later years, after fathering children, and is driven by a sense of wanderlust but also melancholy for what was lost. 
## Description

Belegor is a tall, ageless [[Elves|elf]], with medium length copper hair, pale skin, and green eyes. He wears elegant clothes in greens and yellows, with high collar and long, wide sleeves. Graceful.
## Events

- (DR:: 1748-06), Belegor met the green dragon [[Mezzar|Grimbaskal]], who was posing as an [[Elves|elf]], [[Mezzar]], at the time, in [[Elderwood|the Elderwood]]. 
- (DR:: 1748-07). Belegor fled from [[Mezzar|Grimbaskal]], realizing his deception. 
- (DR:: 1748-08). Belegor sought refuge in a [[Te'kula]] village, hidden in the Elderwood.  
- (DR:: 1748-09-11). Belegor and the [[Dunmar Fellowship]] meet in the hidden [[Te'kula]] village.

%%SECRET[v2:a6b7a7ec80f7df010d6371eb539d9532]%%

%%^Metadata:names:v1%%
- {name: Belegor, language: unknown, pronunciation: beh-leh-GOR, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of an elven wanderer taking refuge among the Te’kula, with selected earlier biography; the recorded meeting dates and the village stay after September require reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and temporal metadata; normalized frontmatter without changing the header version.
- Added `knownTo: [dufr]` from the existing campaign interaction.
- Corrected “not wanting hide” to “not wanting to hide”.

### Validated judgments
- Confirmed the positive `dm_notes` attestation from the matching local-source dossier; reviewed the SECRET block separately without promoting it.

### Open findings

- [ ] **Warning — correctness.conflicting_dates:** The campaign metadata and header say the Fellowship met Belegor on September 30, 1748, while Events says September 11. [[Session 52 (DuFr)]] explicitly dates dinner with Belegor to September 10. Reconcile all three locations together; the source-supported candidate is `{campaign: dufr, date: 1748-09-10, type: met}` and “September 10th, 1748” in the header and event. Preserve the source conflict until approved.
- [ ] **Warning — coverage.later_material_change:** The open-ended Te’kula-village whereabouts and final event leave Belegor in his refuge, but [[Session 52 (DuFr)]] records his departure on September 30 with Theba’s diplomatic mission after Grimbaskal’s defeat. Candidate: “After Grimbaskal’s defeat, Belegor left the Te’kula village with [[Theba]] on September 30, 1748, to visit the other Elderwood tribes.” Review both village whereabouts entries and end the refuge stay at the departure; do not invent a subsequent fixed residence. Decide whether to update the article and POV, defer under a human-selected game-update tag, or preserve an explicitly earlier snapshot.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
%%^End%%

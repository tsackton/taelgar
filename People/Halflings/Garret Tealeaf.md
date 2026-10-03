---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
campaignInfo:
  - {campaign: dufr, date: 1748-06-02, type: freed}
  - {campaign: dufr, date: 1748-07-09, type: last seen}
born: 1656
gender: male
name: Garret Tealeaf
aliases: [Garret]
affiliations:
  - {org: Tealeafs, type: primary}
whereabouts:
  - {type: home, end: 1737, prefix: roads of, location: Dunmar}
  - {type: away, start: 1737, end: 1748-06-07, location: "Agata's lair"}
  - {type: away, start: 1748-06-08, end: 1748-06-19, location: Karawa}
  - {type: away, start: 1748-06-20, end: 1748-06-29, location: traveling to Tokra}
  - {type: away, start: 1748-06-30, end: 1748-07-17, location: The Red Lily Inn}
  - {type: away, start: 1748-07-18, end: 1748-08-12, location: Tokra-Darba Road}
  - {type: away, start: 1748-08-13, location: Darba}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Garret Tealeaf
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him), of the [[Tealeafs]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Freed by the [[Dunmar Fellowship]] on June 2nd, 1748 in [[Agata's Lair]], the [[Garamjala Desert]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[The Red Lily Inn]], [[Tokra]], [[Dunmar]] %%^End%%

%% date of capture is approx %%

![[garret-tealeaf.jpg|right|300]]Garret Tealeaf grew up traveling the roads of Dunmar with the Tealeaf trading family, eventually becoming the patriarch of a group of 5 well-armed and defended caravans that regularly made the circuit from Chardon, east to [[Songara]], Tokra, and Karawa, before turning south across the Yuvanti Mountains to Nayahar, and then north along the coast to Darba, and back to Chardon. 
%%^Campaign:dufr%%
## Relationships

- [[Charmhearts]], occasional traveling companions after being freed from imprisonment in [[Agata's Lair]]. 
- [[Agata]], his captor and tormentor
- [[Seeker]], who freed him from his wooden puppet form
- [[Wellby]], who introduced him to the Charmhearts
- [[Oswalt Tealeaf]], a cousin
## Events
In DR 1737, the Tealeaf family fought off an orc attack from the [[Dustthorn Horde]], associated with [[Agata]]. In revenge, [[Agata]] herself attacked, killing a number of Tealeafs, and then capturing Garret, and using her magic to turn him into a wooden puppet, forced to serve her. She promised the surviving Tealeafs, including [[Oswalt Tealeaf]], that if they did not come east of the Hara River for 15 years, she would return Garret to them.

The [[Dunmar Fellowship]] saw a vision of this attack in the [[Soul Lantern Vision]]. 

Garret spent the next 11 years in servitude, as a wooden scarecrow, until he was rescued by the [[Dunmar Fellowship]]. Since then, he has slowly come back to himself, although he remains extremely nervous around magic, and especially any treasure claimed from Agata herself.

 - (DR:: 1737): Tealeaf clan fights off [[Dustthorn Horde]] orcs, but are then ambushed by [[Agata]]. [[Garret Tealeaf]] is captured.
  - (DR:: 1748-06-02):  [[Garret Tealeaf]] is freed from his imprisonment as a wooden scarecrow by [[Seeker]] and the [[Dunmar Fellowship]]. 
  
%%^End%%

%%^Metadata:names:v1%%
- {name: Garret Tealeaf, language: unknown, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait after Garret's rescue from Agata, with selected earlier trading history and captivity; later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter while preserving the approximate-capture-date comment verbatim below the complete header.
- Added `knownTo: [dufr]` and normalized the existing `DuFr` campaign aliases to `dufr` without changing their scope.
- Corrected two objective typos: “fought of” to “fought off” and “he reminds extremely nervous” to “he remains extremely nervous”.
- Added persistent name metadata and a DR 1748 temporal viewpoint; no name language was inferred.

### Validated judgments
- The existing account sufficiently identifies his trading role, captivity, rescue, and subsequent fear of magic; [[Session 30 (DuFr)]] and [[Session 33 (DuFr)]] corroborate those central events and their consequences.
- Garret Tealeaf is an obvious ordinary given name and English compound surname; pronunciation is omitted under the ordinary-name exception.
- The positive `dm_notes` attestation has confirmed local evidence; private contents remain outside this report.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** Reconcile the rescue date. This note's `campaignInfo`, header, and final timeline entry say June 2, 1748; [[Session 30 (DuFr)]] places the journey through Bas Udda on June 2–3 and the lair visit and rescue on June 4, with [[Session 31 (DuFr)]] opening that evening after Garret has been freed. No date was changed automatically. If the session chronology is adopted, use `{campaign: dufr, date: 1748-06-04, type: freed}`, replace “June 2nd, 1748” with “June 4th, 1748” in the header, and replace `(DR:: 1748-06-02)` with `(DR:: 1748-06-04)` in the rescue timeline entry. Otherwise, retain the date with an explicit explanation of the conflicting source chronology.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Kenzo, date: 1748-11-03, type: met}
  - {campaign: dufr, person: Kenzo, date: 1748-11-13, type: last seen}
born: null
activeYear: 1745
gender: male
name: Enari
whereabouts:
  - {type: home, location: Orekatu}
  - {type: away, start: 1748-11-01, end: 1748-11-04, location: Bedez}
  - {type: away, start: 1748-11-06, end: 1748-11-13, location: Azta Lekua}
  - {type: away, start: 1748-11-15, location: Bedez}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Enari
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Kenzo]] on November 3rd, 1748 in [[Bedez]], [[Orekatu]], the South Region %%^End%%  
>> %%^Campaign:dufr%% Last seen by [[Kenzo]] on November 13th, 1748 in [[Azta Lekua]], [[Orekatu]], the South Region %%^End%%

![[enari-portrait.png|right|400]]A well-muscled lizardfolk hunter and wanderer, who earned a reputation and honor traveling among the villages of the kingdom of [[Orekatu]]. 
%%^Campaign:dufr%%
Guided [[Kenzo]] and [[Izzarak]] to the [[Azta Lekua]], the [[Azta Lekua|Footprint of the Gods]], and returned to [[Bedez]] after they succeeded in their quest, to report to the elders of the kingdom. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Enari", "language": "unknown", "pronunciation": "eh-NAH-ree", "status": "proposed", "notes": "Basque-informed proposal using the Lizardling cultural analogue in Languages: e as eh, a as ah, i as ee, and a light single r. Penultimate stress is provisional; the exact source language of this personal name is not explicit."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of the Orekatu hunter and guide, with dated travel and campaign interactions in DR 1748; his later life is not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added knownTo: ["dufr"].
- Added persistent name and temporal-viewpoint metadata.

### Validated judgments
- The existing campaignInfo directly supports knownTo: [dufr].
- The concise hunter-and-guide account is proportionate to the role recorded in [[Session 59 (DuFr)]] and [[Session 64 (DuFr)]].
- Confirmed local-only sources support the positive dm_notes attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `eh-NAH-ree` for Enari. The proposal uses [[Languages]]’ Basque analogue for the Lizardling cultural context: eh/ah/ee vowels and a light single r, with provisional penultimate stress. The exact personal-name language and in-world stress are unrecorded, so the entry remains proposed. After acceptance, copy the pronunciation to frontmatter and mark the entry documented.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 1 - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 2 - Kenzo]]
%%^End%%

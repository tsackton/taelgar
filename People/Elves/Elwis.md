---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: elf
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1749-01-02, type: met}
born: 1634
ka: 37
gender: female
name: Elwis
pronunciation: EL-wiss
whereabouts:
  - {type: home, location: Orenlas}
  - {type: away, start: 1744-01-01, end: 1748-08-28, location: Green Sea}
  - {type: away, start: 1748-08-29, end: 9999, location: Tollen}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: modern
---
# Elwis
*(EL-wiss)*
>[!info]+ Biographical Info  
> An [[Elves|elf]] (she/her), ([[Elven Cycle of Generations|ka]] 37)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on January 2nd, 1749 in the [[Tollen|Free City of Tollen]] %%^End%%

Elwis is a female elf and painter from [[Orenlas]]. 

%%^Date:1744%%
She is spending her wandering years traveling around the [[Green Sea]], trying to make new art that hasn't been dreamed before in the history of her people. She has recently come to [[Tollen]], fascinated by the magical inks of the Dyer's Guild and seeking to use them in painting. 
%%^End%%

%%SECRET[v2:a63ff858568a0f60bf518ddd21422fef]%%

%%^Metadata:names:v1%%
- {"name": "Elwis", "language": "unknown", "pronunciation": "EL-wiss", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern identity as an elven painter; the dated passage describes her wandering from DR 1744 and her later arrival in Tollen, whose visibility boundary needs separation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and the campaignInfo code; added knownTo: [dufr].
- Recorded the accepted pronunciation in name metadata and added the article’s temporal interpretation.

### Validated judgments
- The available source record supports the bounded painter portrait. The positive dm_notes attestation is supported, and the SECRET block was reviewed without sharing its contents.

### Open findings

- [ ] **Warning — temporal.date_block_scope:** The existing Date:1744 block includes “She has recently come to [[Tollen]]”, while whereabouts dates her Tollen stay from 1748-08-29 and [[Session 84 (DuFr)]] places this portrait in January 1749. Keep the wandering sentence under Date:1744; put only the Tollen sentence in a separate Date:1748-08-29 block. Copy-ready Tollen sentence: “She has recently come to [[Tollen]], fascinated by the magical inks of the Dyer's Guild and seeking to use them in painting.” This requires human approval because it changes date-filtered visibility.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated meeting line still uses Campaign:DuFr. Replace only the marker value DuFr with the canonical code dufr from [[Campaign Registry]]; preserve the meeting text and date.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Orenlas - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
%%^End%%

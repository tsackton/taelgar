---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-19}
born: 1710
gender: male
name: Amar
affiliations:
  - {org: Akela Inn, title: Master, type: leader}
whereabouts:
  - {type: home, location: Hara River Valley}
  - {type: home, location: Akela Inn}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Amar
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 19th, 1748 in the [[Akela Inn]], on the [[Tokra-Darba Road]], in [[Dunmar]] %%^End%%

The innkeeper of the [[Akela Inn]], a fortified waystation and caravanserai on the road from [[Tokra]] to [[Darba]], near the [[Copper Hills]]. 

%%^Campaign:dufr%%
His story was heard by [[Kenzo]] of the [[Order of the Awakened Soul]] on 19 July 1748, and recorded: [[Amar's Story]].
%%^End%%

%%^Metadata:names:v1%%
- {name: Amar, language: Dunmari, pronunciation: "uh-mur", notes: "Proposed from the Dunmari analogue in [[Languages]], preferring Hindi-informed short a vowels as schwas, an ordinary m, and a lightly tapped r; neither syllable is strongly stressed. The written name does not establish exact in-world phonology.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Amar as keeper of the Akela Inn, anchored by the July 1748 encounter; his earlier life is linked through his collected story rather than narrated here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded meeting and normalized frontmatter.
- Normalized the existing campaign marker from `DuFr` to its registry-equivalent `dufr`.
- Added proposed name metadata and `POV: 1740s` with temporal guidance.

### Validated judgments
- [[Amar's Story]] supports the innkeeper's identity and family connection to the caravanserai; the present note remains a sufficient concise connector to that source.
- The two undated home entries validly distinguish his origin from his inn; they do not require invented move dates.
- Confirmed local source matches support the positive `dm_notes` attestation; unrelated matches were excluded.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `uh-mur` in `Metadata:names:v1` needs human acceptance. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue; the preferred Hindi-informed reading treats the two short `a` vowels as schwas, keeps `m`, and uses a lightly tapped `r`, without strong English-style stress. Exact in-world phonology is unrecorded. If accepted, set `pronunciation: uh-mur` in frontmatter and change the entry to `status: documented`; otherwise revise the proposal.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
%%^End%%

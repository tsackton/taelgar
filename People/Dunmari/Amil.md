---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo: []
born: 1731
gender: male
image: amil-small.jpg
name: Amil
affiliations: [Order of the Awakened Soul]
whereabouts:
  - {type: home, start: 1747, end: 1749-01-30, location: "Pava and Avaras' House"}
  - {type: away, start: 1749-01-30, end: 9999, location: Vindristjarna}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Amil
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% fix away whereabouts, campaign info %%

![[amil-final.jpg|right|400]]A young monk, in training as an apprentice of the [[Order of the Awakened Soul]]. Fit, tanned, and cheerful, even when undertaking challenging or unsettling tasks. Lives with his masters, [[Pava]] and [[Avaras]], on the edge of the [[Garamjala Desert]] in the blasted plains. 

%%SECRET[v2:dc51be15f3a73f26c2286c6622329ee6]%%
## Events
- (DR:: 1748-04-27) *(Amil)*: Arrives in Bas Udda to tend the unburied dead from the gnoll attacks
- (DR:: 1748-04-29) *(Amil)*: Meets [[Havdar]] and [[Dunmar Fellowship]], who aid him in his task. 
- (DR:: 1748-04-30) *(Amil)*: Leaves Bas Udda with The Dunmar Fellowship, traveling to his masters' house in the desert
- (DR:: 1748-05-02) *(Amil)*: Arrives at Pava and Avaras' House with The Dunmar Fellowship. 
- (DR:: 1748-05-17) *(Amil)*: At Pava and Avaras' House when [[Dunmar Fellowship]] spend the night

## Gallery
![[Amil-martial-arts.jpg|400]]

![[Amil-snow-forest.jpg|400]]

![[Amil-skyship-garden.jpg|400]]

%%^Metadata:names:v1%%
- {name: Amil, language: Dunmari, pronunciation: AH-mil, notes: "Proposed from the Dunmari Hindi/Indo-Iranian analogue in Languages: long open initial a, short i as in bit, plain m and l, with initial emphasis; a Persian-oriented reading could instead emphasize the final syllable. Vowel length and stress are not established for this name.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Amil as a young apprentice living with Pava and Avaras, with events from April and May of that year; the whereabouts metadata extends into 1749, but the visible account does not incorporate his later apprenticeship to Kenzo or his role aboard Vindristjarna.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added `knownTo: [dufr]`, supported by the existing events and [[Session 19 (DuFr)]].
- Normalized `image` to the filename `amil-small.jpg`; the asset exists, and the portrait embeds are unchanged.
- Added a primary name entry with a proposed pronunciation and its derivation.
- Recorded `POV: 1748` and the limits of the visible portrait in `povNotes`.

### Validated judgments
- The January 30, 1749 departure recorded in `whereabouts` agrees with [[Session 89 (DuFr)]]. The existing away entry already records Vindristjarna; no duplicate entry is needed.
- `status/cleanup/metadata`: not assessable. The reminder to fix whereabouts and campaign info does not specify the intended remaining changes. The tag and reminder are preserved for human disposition.
- Confirmed local DM sources support the positive `dm_notes` attestation. The local SECRET block was reviewed separately and preserved.

### Editorial assessment
**Underdeveloped**: the visible portrait omits Amil’s later role as Kenzo’s traveling apprentice and a member of Vindristjarna’s crew. His work with the ship’s Hall of Stories and martial training belongs to that same missing account. The sources establish the transition; a short update is sufficient, without a general biography or a log of routine appearances.

### Open findings
- [ ] **Warning — coverage.later_material_change:** The sentence beginning “Lives with his masters” and the April–May 1748 event list leave the article before its defining later relationship. [[Session 89 (DuFr)]] records Pava asking Kenzo to take Amil as an apprentice and Amil joining Vindristjarna on January 30, 1749; [[Session 124 (DuFr)]] still identifies him as Kenzo’s student. [[Vindristjarna Bastion Rules]] identifies his later work with the Hall of Stories and his ability to train unarmed combat. Choose whether to update the article and `POV`, defer the update with the appropriate game-update status, or intentionally preserve the 1748 snapshot. Copy-ready update: `Amil trained under [[Pava]] and [[Avaras]] at their home on the edge of the [[Garamjala Desert]]. On January 30, 1749, at Pava’s request, he joined [[Vindristjarna]] as [[Kenzo]]’s apprentice. Aboard the ship, he helps tend the Hall of Stories and can train others in unarmed combat.` If preserving the earlier portrait with later information layered beneath it, put only the dated departure sentence in a `%%^Date:1749-01-30%%` block ending with `%%^End%%`, and date-bound or rephrase the earlier residence sentence. The later Hall of Stories role has no established starting day. These visibility changes require human approval.
- [ ] **Warning — metadata.names_unresolved_status:** Review `AH-mil` in the name block. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue. The preferred Hindi-informed reading uses a long open initial a, short i as in “bit,” plain m and l, and initial emphasis; a Persian-oriented reading could instead emphasize the last syllable. The source does not establish this name’s exact vowel length or stress. Accept the proposal by setting `pronunciation: AH-mil` in frontmatter and changing the entry to `status: documented`, or supply the intended pronunciation.

### DM evidence
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Awakened Soul Monks]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 105 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 85 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 94 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: fey
gender: male
name: Count Vashan
aliases: [The Broken Mask]
whereabouts:
  - {type: home, end: 1, location: Amberglow}
  - {type: home, location: Sunwine Hall}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1749
---
# Count Vashan
>[!info]+ Biographical Info  
> A [[Fey|fey]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Count Vashan, who calls himself by the epithet "The Broken Mask", is a drunken hanger-on in the court of [[Lord Soven]]. He does not recall his origin any longer, and most have ceased to ask, leaving him to his forgetfulness. Persistent rumors claim that he was once a respected member of the [[Cloudspinner]]'s court, long ago.

%%^Campaign:dufr%%
In a brief moment of lucidity, Count Vashan spoke of how he was once a trusted advisor to the [[Cloudspinner]], but -- whether due to stupidity, or carelessness, or some hidden treachery in his heart, he no longer can recall -- he betrayed her, allowing [[Cha'mutte]] to surprise her in a moment of weakness. Now, he seeks to forget what he did, drowning his past in the wines of [[Sunwine Hall]].
%%^End%%


%%SECRET[v2:53cc35601e1b9f73af147795528ee796]%%

%%^Metadata:names:v1%%
- {name: Count Vashan, language: unknown, pronunciation: "kownt VAH-shahn", notes: "Cautious spelling-based proposal: ordinary English Count; Vashan with v as in vine, sh as in ship, broad ah vowels, and first-syllable stress. No established name language or explicit pronunciation was found.", status: proposed}
- {name: The Broken Mask, role: epithet, language: unknown, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 portrait of Vashan at Sunwine Hall, with an undated recollection of his service to and betrayal of the Cloudspinner; the duration of his residence and his subsequent state are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “betratyed” to “betrayed” in the existing Dunmar Frontier passage.
- Added the explicit name and knownTo: [dufr], normalized frontmatter ordering, and preserved both whereabouts entries and the DM attestations.
- Added persistent name metadata with a proposed pronunciation and the documented epithet; recorded a DR 1749 viewpoint with temporal coverage notes.

### Validated judgments
- [[Session 120 (DuFr)]] supports his presence at Sunwine Hall and his recollection of betraying the Cloudspinner. [[Session 121 (DuFr)]] and [[Session 122 (DuFr)]] add no later change to his personal state.
- Reviewed the local-only SECRET block; its contents remain outside this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation “kownt VAH-shahn” in Metadata:names:v1. No explicit pronunciation or established name language was found. This is a cautious spelling-based reading: ordinary English Count, v as in vine, sh as in ship, broad ah vowels, and stress on VAH. The general Sylvan guidance in [[Languages]] gives no specific analogue for this name. If accepted, copy `pronunciation: kownt VAH-shahn` to frontmatter and change the primary name entry to `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 119 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: fey
subspecies: hag
name: The Midnight Lady
aliases: [Night Witch]
whereabouts:
  - {type: home, location: Duskmire}
  - {type: away, start: "1720-01", end: 9999, location: Peydon}
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1720
---
# The Midnight Lady
>[!info]+ Biographical Info  
> A [[Fey|fey]] (hag)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A mysterious fey recently arrived in [[Peydon]]. Known by many in the village as the Night Witch. Her real name is Moriel.

%% Images

![[midnight-lady-true.jpg|left|400]]


![[midnight-lady-disguised.jpg|left|400]]

%%

%%^Metadata:names:v1%%
- {name: The Midnight Lady, role: primary, language: Common, status: inferred}
- {name: Night Witch, role: alias, language: Common, status: inferred}
- {name: Moriel, role: personal name, language: unknown, pronunciation: moh-ree-EL, notes: "Proposed cautious spelling-based reading with three syllables, long o, ee for i, and final stress. The Sylvan guidance in Languages supplies no definite analogue or name-specific phonology.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the early DR 1720 Peydon arrival and active hag portrait; the visible note has not incorporated her death on March 4, 1720, and must not be treated as a current account after that event.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and temporal metadata; normalized frontmatter without changing the header version.
- Added `knownTo: [clee]` from [[Cleenseau - Session 22]] and [[Cleenseau - Session 23]].

### Validated judgments
- The descriptive titles need no pronunciation. Moriel is independently represented as the personal name already given in the visible note.

### Editorial assessment
**Underdeveloped**: the arrival-only description omits the Midnight Lady’s defining control of Peydon through bargains and her established defeat and death. A short account of that rule and its end would fill the central gaps.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The description says only “A mysterious fey recently arrived”; [[Peydon]], [[Gareth's Story]], and [[Cleenseau - Session 22]] establish that her bargains gave her control over Peydon. Candidate: “The Midnight Lady, also called the Night Witch and known personally as Moriel, is a hag from [[Duskmire]] who gained control of [[Peydon]] through bargains made during the undead rising of DR 1720.” This identifies her defining role without importing unrevealed plans.
- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Session 23]] dates the Lady’s destruction to March 4, 1720, and [[Cleenseau - Session 24]] confirms the village’s release. The open-ended Peydon whereabouts and arrival-only prose remain misleading after that date. Propose a new `Date:1720-03-04` block containing only “The [[Heroes of Cleenseau]] destroyed her and her hidden refuge on March 4, 1720, ending her control of Peydon.” Review `died: 1720-03-04` and end the Peydon stay at that date together. Choose to update the article and POV, defer with a human-selected game-update tag, or intentionally retain the earlier snapshot; no visibility or life-cycle change was applied.
- [ ] **Warning — metadata.names_unresolved_status:** The new Moriel entry proposes `moh-ree-EL`: three syllables, long o, ee for i, and final stress. This is a cautious spelling-based proposal; [[Languages]] explicitly leaves the Sylvan analogue undetermined and supplies no exact phonology for the name. Confirm or replace the proposal in the name block. The plain-English primary and alternate titles require no pronunciation.
%%^End%%

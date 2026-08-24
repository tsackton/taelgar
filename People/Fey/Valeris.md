---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:02:51-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/dufr, status/check/lint]
species: satyr
gender: male
name: Valeris
whereabouts:
  - {type: home, end: 1749-06-07, location: Sunwine Hall}
  - {type: away, start: 1749-06-07, end: 1749-06-12, location: Emberwine}
  - {type: away, start: 1749-06-12, end: 1749-06-14, location: Amberglow}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Valeris
>[!info]+ Biographical Info  
> A [[Satyrs|satyr]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[valeris.jpg|right|300]]Valeris is a satyr, a musician and gambler, cursed to speak only the absolute truth, unable even to sugar coat his words with lies of omission. 

He is lean and rakish, with curling ram’s horns wrapped in gold rings, and half-buttoned silk shirt. His eyes twinkle with mischief he can no longer act on, and his mouth twitches constantly, but whether in irritation or the desperate effort to hold his tongue is hard to tell. 

%%
need to add details of his backstory / why he was cursed from session notes
%%

%%SECRET[v2:55600fbdf7bc3bced158b17f815cddcd]%%

%%^Metadata:names:v1%%
- {name: Valeris, language: Sylvan, pronunciation: vuh-LAIR-iss, notes: "Proposed from the spelling and the documented lyrical, partly Classical-Greek-inspired pattern for Sylvan names; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a June DR 1749 portrait spanning Valeris's time at Sunwine Hall and journey into Amberglow; the visible article does not include his decision on DR 1749-06-13 to remain there.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Updated `povNotes` to replace the obsolete claim that Valeris's later fate was unestablished with the established DR 1749-06-13 outcome boundary.

### Validated judgments
- `status/gameupdate/dufr` remains supported because the established outcome at the Prismwell is not represented in the visible article.
- The shared comment is a source pointer for the missing backstory.
- The SECRET block was reviewed for possible recovery without exposing its contents here.
- The DR 1749 viewpoint remains appropriate; the persistent temporal note now accurately identifies the visible article's omitted later outcome.

### Editorial assessment

**Underdeveloped**. The visible article identifies Valeris and his curse but omits the established cause of that defining curse and the established outcome of his journey through Amberglow. The smallest useful development is one concise backstory paragraph from [[Session 120 (DuFr)]] plus one dated outcome sentence from [[Session 123 (DuFr)]].

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Session 120 (DuFr)]] establishes that Valeris became unable to lie after telling a reality-altering story to undo an oath sworn by Yasara the Golden. This is the defining cause of the curse around which the visible article is organized. Copy-ready candidate: `Valeris's curse began when he told a story powerful enough to undo an oath sworn by Yasara the Golden. Reality accepted the tale, but thereafter Valeris could never speak a lie.`
- [ ] **Warning — coverage.later_material_change:** [[Session 123 (DuFr)]] establishes that on DR 1749-06-13 Valeris remained in Amberglow to help repair the realm and perhaps free himself from the curse. Choose whether to add this dated outcome, defer the update while retaining `status/gameupdate/dufr`, or intentionally preserve the earlier portrait. Copy-ready candidate if updating: `After [[Cloudspinner]] was freed at the [[Prismwell]] on DR 1749-06-13, Valeris remained in [[Amberglow]] to help repair the realm and perhaps free himself from his curse.`
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `Valeris — vuh-LAIR-iss` from the documented lyrical and partly Classical-Greek-inspired pattern for Sylvan names. Review the proposal; if accepted, copy it to frontmatter and change the entry to `status: documented`, or revise it while preserving its derivation.
%%^End%%

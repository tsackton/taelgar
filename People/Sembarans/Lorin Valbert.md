---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T23:46:56-04:00"
lintVersion: "3.4"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
gender: male
born: 1677
name: Lorin Valbert
affiliations:
  - {place: Manor of Asineau, start: 1715, end: 1720-01-13, title: Lord}
whereabouts:
  - {type: home, location: Embry, end: 1715}
  - {type: home, location: Asineau, end: 1720-01-13}
  - {type: away, location: Champimont, start: 1720-01-14, end: 1720-01-15}
  - {type: away, location: Rinburg, start: 1720-01-17, end: 1720-01-19}
  - {type: away, location: Borderlands, start: 1720-01-19, linkText: heading towards, wLastKnown: "Last known location (as of <lastknowndate>): <lastKnown:q>"}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1710s
---
# Lorin Valbert
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[lorin-valbet.png|right|320]]Lorin Valbert is the lord of [[Asineau]]. He is a cousin of the old lord, [[Lucas Asa]] ,via Lucas' biological father. Lorin did not expect to inherit a manorial lordship, and regards it as beneath his station, being a backwater far from the centers of power. 

He has a wife and two young children who often reside in [[Embry]].

%%^Campaign:clee%%
During the [[Battle Against Wakog]] he was notably unhelpful and did not wish to strip his manorial guard to aid the attack on [[Wakog|Wakog's]] camp. 
%%^End%%

%%^Date:1720%%
He fled his manor after the [[Undead Attacks in Sembara]], in part because he was convinced some of the misfortune of the Asa family was falling on him, and partly because he was scared and did not want to deal with the [[Undead Attacks in Sembara]].
%%^End%%

%%^Metadata:names:v1%%
- {name: Lorin Valbert, role: primary, language: Sembaran, pronunciation: loh-RAN val-BAIR, status: proposed, notes: "Southern Sembaran French analogue; tentative French-style vowels, softened final consonants, and phrase-final stress."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1710s portrait of Lorin as lord of Asineau, with a Date:1720 block recording his flight; his later fate is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added `knownTo: [clee]`, recorded `POV: 1710s` with persistent name and temporal-review metadata, and canonicalized the campaign block from `Clee` to `clee`.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** The persistent entry proposes `Lorin Valbert — loh-RAN val-BAIR` from the southern Sembaran French analogue. Review the proposal; if accepted, copy it to frontmatter and change the entry to `status: documented`, or revise the entry while preserving its derivation.
- [ ] **Warning — coverage.established_fact_missing:** [[Cleenseau - Session 11]] and [[Cleenseau - Session 12]] establish that [[Viepuck]] and [[Izgil]] deliberately deceived Lorin about a fey curse, that he renounced his claim to Asineau, and that the party recovered most of the manor's money and horses before helping him continue east. The existing Date:1720 passage attributes his flight only to fear and family misfortune, which materially obscures the party's role and the renunciation. Candidate replacement: `On January 11, DR 1720, [[Viepuck]] and [[Izgil]] deliberately convinced Lorin that the manor was cursed and that fey were pursuing him. Lorin fled the next morning and renounced his claim to Asineau. After [[Celyn]] and Viepuck caught him near [[Rinburg]], he returned most of the manor's money and horses before continuing east across the river.`

%%^End%%

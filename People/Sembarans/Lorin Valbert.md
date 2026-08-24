---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:02:51-04:00"
lintVersion: "3.5"
tags: [person, status/check/mike, status/check/lint]
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

![[lorin-valbet.png|right|320]]Lorin Valbert is the lord of [[Asineau]]. He is a cousin of the old lord, [[Lucas Asa]], via Lucas' biological father. Lorin did not expect to inherit a manorial lordship, and regards it as beneath his station, being a backwater far from the centers of power.

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
- Corrected the misplaced punctuation in `[[Lucas Asa]] ,via` to `[[Lucas Asa]], via`.

### Validated judgments
- The DR 1710s viewpoint remains coherent because the existing Date:1720 block isolates Lorin's later flight, although that dated account is materially incomplete.
- The newer Metadata Specification mention is an unchanged governance example and supplies no later lore about Lorin.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Session 11]] and [[Cleenseau - Session 12]] establish material DR 1720 consequences missing from the existing Date:1720 passage: [[Viepuck]] and [[Izgil]] deliberately deceived Lorin about a fey curse, Lorin renounced Asineau, and the party recovered most of the manor's money and horses before helping him continue east. Choose whether to expand the existing dated passage, defer the update with `status/gameupdate/clee`, or intentionally preserve a partial earlier account. Copy-ready replacement for the existing Date:1720 paragraph: `On January 11, DR 1720, [[Viepuck]] and [[Izgil]] convinced Lorin that the manor was cursed and that fey were pursuing him, building on his fear that the misfortune of the Asa family was falling on him amid the [[Undead Attacks in Sembara]]. Lorin fled the next morning and renounced his claim to Asineau. After [[Celyn]] and Viepuck caught him, he returned most of the manor's money and horses before continuing east across the river.`
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `Lorin Valbert — loh-RAN val-BAIR` from the southern Sembaran French analogue. Review the proposal; if accepted, copy it to frontmatter and change the entry to `status: documented`, or revise it while preserving its derivation.
%%^End%%

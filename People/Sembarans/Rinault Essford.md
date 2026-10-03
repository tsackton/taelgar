---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person]
species: human
ancestry: Sembaran
born: 1688
gender: male
title: Lord
name: Rinault Essford
pronunciation: ree-NOH ESS-ford
aliases: [Lord Rinault, Lord Rinault Essford, Rinault]
affiliations:
  - {org: Essfords, title: Heir, type: primary}
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1719
---
# Lord Rinault Essford
*(ree-NOH ESS-ford)*
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Essfords]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[Lord-Rinault-Essford.png|right|320]]The younger brother of [[Rosalind Essford|Rosalind]], he is considered rash and impulsive. He openly dreams of bigger adventures and grander scales for his ambitions, but few trust him.

He was briefly the acting lord of Cleenseau while Rosalind was traveling to Embry, but although he was not terrible, few see him as a viable heir.

%%^Campaign:none%%
The reasons for his lack of a wife and children are not clearly established, but have repeatedly been suggested to be something a bit magical or odd. He may have a curse or other magical affliction related to fatherhood.
%%^Campaign:none%%

%%^Campaign:clee%%
### Rinault's Childhood Stories
Before [[Cleenseau - Session 08]] Rinault shares some stories of his childhood:
- When Rinault was a bored teenager he sometimes took some buddies and went to smash stuff in the old ruins on the south side of the Enst. One night, he says, he swore he saw a skeleton arm move in the dirt. 
- He was fiercely forbidden from climbing around the hill or the basements of Essford Manor. He was always a rambunctious kid and often didn't follow the rules, but the one time he and two friends were "digging for buried treasure" in the side of the hill his father was apoplectic and he was confined to his room for a month afterwards. 
%%^End%%

%%^Campaign:none%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Rinault Essford", "language": "Sembaran", "pronunciation": "ree-NOH ESS-ford", "status": "documented", "notes": "The French strand of the Sembaran analogue in [[Languages]] gives Rinault an ee vowel and au as oh, with final lt silent; Essford is treated as an English-strand compound with short e and an audible ford. This mixed Sembaran adaptation remains proposed because no adopted pronunciation was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a portrait of Rinault from late 1719 with childhood recollections; his temporary authority during Rosalind’s absence is not yet described, nor is the impact of his father's death and Rosalind's search for an heir -- not him -- in summer 1720. 
%%^End%%
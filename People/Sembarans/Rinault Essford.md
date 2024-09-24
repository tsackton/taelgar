---
headerVersion: 2023.11.25
tags: [person, status/update]
name: Rinault Essford
born: 1688
species: human
ancestry: Sembaran
gender: male
aliases: [Lord Rinault, Lord Rinault Essford, Rinault]
title: Lord
whereabouts: Cleenseau
affiliations:
- {org: Essfords, title: Heir, type: primary }
dm_notes: color
dm_owner: mike
---
# Lord Rinault Essford
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Essfords]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[Lord-Rinault-Essford.png|right|320]]The younger brother of [[Rosalind Essford|Rosalind]] he is considered rash and impulse. He openly dreams of bigger adventures and grander scales for his ambitions, but few trust him.

%%^Campaign:Clee%%
### Rinault's Childhood Stories
Before [[Cleenseau - Session 08]] Rinault shares some stories of his childhood:
- When Renault was a bored teenager he sometimes took some buddies and went to smash stuff in the old ruins on the south side of the Enst. One night, he says, he swore he saw a skeleton arm move in the dirt. 
- He was fiercely forbidden from climbing around the hill or the basements of Essford Manor. He was always a rambunctious kid and often didn't follow the rules, but the one time he and two friends were "digging for buried treasure" in the side of the hill his father was apoplectic and he was confined to his room for a month afterwards. 
%%^End%%

%%^Campaign:None%%
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
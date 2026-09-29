---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person]
species: human
ancestry: Sembaran
born: 1698
gender: male
name: Matteo Ausson
whereabouts: Cleenseau
pronunciation: mah-TAY-oh ah-SOHN
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720s
---
# Matteo Ausson
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[matteo-ausson.png|right|320]]One of the sons of [[Arnaud Ausson]], something of a ne'er-do-well. Rumored to have been the lover of [[Rinault Essford|Rinault]] in the summer of 1719, and still hangs around [[Rinault Essford|Rinault]] and his cronies. Also rumored to have been involved in the death of his sister Lizette when he was 10, but no one knows the details. He is the first of his family to truly embrace his [[Sembara|Sembaran]] adopted homeland and is rarely interested in listening to his father's tales of home, although he is happy to spend his father's money.

Full of swagger and bravado on the outside, at least. 


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
- {name: Matteo Ausson, role: primary, language: Isinguese, pronunciation: mah-TAY-oh ah-SOHN, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of Matteo after the rumored events of DR 1719; earlier childhood is mentioned only through an unresolved rumor, and later life is not described.
%%^End%%
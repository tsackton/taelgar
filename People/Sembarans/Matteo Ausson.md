---
headerVersion: 2023.11.25
tags: [person]
ancestry: Sembaran
born: 1698
species: human
gender: male
whereabouts: Cleenseau
dm_plans: no
dm_notes: color
---
# Matteo Ausson
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[matteo-ausson.png|right|320]]One of the sons of [[Arnaud Ausson]], something of a ne'er-do-well. Rumored to have been the lover of [[Rinault Essford|Rinault]] in the summer of 1719, and still hangs around [[Rinault Essford|Rinault]] and his cronies. Also rumored to have been involved in the death of his sister Lizette when he was 10, but no one knows the details.

Full of swagger and bravado on the outside, at least.


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
---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person]
species: human
ancestry: Sembaran
born: 1675
gender: male
name: Ames Benthey
pronunciation: AYMS BEN-thee,
affiliations:
  - {org: "Lord's Guard of Cleenseau", title: Captain, type: leader}
  - {org: Essfords, title: Guard Captain}
  - {org: "Lord's Council of Cleenseau"}
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, start: 1720-01-04, end: 1720-01-19, location: travelling to Embry}
  - {type: away, start: 1720-01-20, end: 1720-02-20, location: Embry}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Ames Benthey
*(AYMS BEN-thee,)*
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[ames-benthey.png|right|320]]The captain of the household guard of [[Essford Manor]], part of the [[Lord's Guard of Cleenseau|Lord's Guard]] in [[Cleenseau]]. Likes to play dice with [[Celyn]]. Better at delegating than doing any actual work and enjoys his food. However, when push comes to shove, he is a competent fighter and captain. 






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
- {name: Ames Benthey, role: primary, language: Sembaran, pronunciation: AYMS BEN-thee, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Ames around his departure from Cleenseau for Embry; earlier and later career are not described.
%%^End%%
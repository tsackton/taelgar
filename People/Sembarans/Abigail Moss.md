---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person]
species: human
ancestry: Sembaran
born: 1698
gender: female
name: Abigail Moss
whereabouts: Taviose
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: 1720
---
# Abigail Moss
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[abilgail-moss.jpg|right|320]]Abigail is a somewhat shy farmer whose orchard was infected with the remains of the giant spiders that plagued [[Taviose]]. [[Robin of Abenfyrd|Robin]] was able to disinfect it with his lay on hands ability. Her family was killed in the spider attacks, and she has struggled to maintain the family orchard, which is mostly walnuts and chestnuts and hugs the edge of [[Cleenseau Wood]].

Her family holds the orchard and several buildings in [[Taviose]] as freeholders, and her two uncles are successful pig farmers.

%%^Campaign:clee%%
She has a potentially budding romance with [[Odo Cordwaner]], and a clear crush on [[Robin of Abenfyrd|Robin]]. 

In late April 1720, she came to [[Asineau]] with Odo and his younger brother [[Samuel Cordwaner|Samuel]]. An orchardkeeper and pig farmer, she had not yet settled on a role there.
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
- {name: "Abigail Moss", language: "Sembaran", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1719 and spring-1720 account of Abigail after the spider attacks, including her late-April arrival in Asineau; her eventual role there remains undecided.
%%^End%%

---
headerVersion: 2023.11.25
tags: [person]
name: Abigail Moss
born: 1698
species: human
ancestry: Sembaran
gender: female
whereabouts: Taviose
dm_notes: none
dm_owner: mike
---
# Abigail Moss
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[abilgail-moss.jpg|right|320]]Abigail is a somewhat shy farmer whose orchard was infected with the remains of the giant spiders that plagued [[Taviose]]. [[Robin of Abenfyrd|Robin]] was able to disinfect it with his lay on hands ability. Her family was killed in the spider attacks, and she has struggled to maintain the family orchard, which is mostly walnuts and chestnuts and hugs the edge of [[Cleenseau Wood]].

Her family holds the orchard and several buildings in [[Taviose]] as freeholders, and her two uncles are successful pig farmers.

%%^Campaign:Clee%%
She has a potentially budding romance with [[Odo Cordwaner]], and a clear crush on [[Robin of Abenfyrd|Robin]]. 
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
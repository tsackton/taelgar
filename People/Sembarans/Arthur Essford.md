---
headerVersion: 2023.11.25
tags: [person]
campaignInfo: [ {campaign: clee, date: 1720-01-03 }]
name: Arthur Essford
born: 1682
species: human
ancestry: Sembaran
gender: male
affiliations:
- {org: Bybets, type: primary }
- {org: Essfords, title: Lord Consort, start: 1706 }
whereabouts:
- {type: home, end: 1705, location: Ainwick}
- {type: home, start: 1706, location: Cleenseau}
- {type: away, start: 1720-01-04, end: 1720-01-19, location: travelling to Embry }
- {type: away, start: 1720-01-20, end: 9999, location: Embry }
dm_notes: color
dm_owner: mike
---
# Arthur Essford
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Bybets]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on January 3rd, 1720 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

![[arthur-bybet-portrait.png|right|320]]The husband of [[Rosalind Essford|Rosalind]] (whom he married in 1706), he wisely takes a back seat in local affairs. He hails from a prominent family in [[Ainwick]]. He is a aficionado of stories and songs and often frequents [[The Crossroads Inn]] to hear the latest news.

In the fall of 1719, he lost his three children during the [[Tragic Flood of the River Enst]] and his and [[Rosalind Essford|Rosalind's]] sadness over this has been profound. 

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
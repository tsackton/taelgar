---
headerVersion: 2023.11.25
tags: [person, status/gameupdate/active]
campaignInfo: [ { campaign: clee }]
name: Odo Cordwaner
born: 1700
species: human
ancestry: Sembaran
gender: male
affiliations:
- {org: Army Garrison of Cleenseau, end: 1719-11-05, title: Sergeant }
- {org: Lord's Guard of Cleenseau, start: 1719-11-16, title: Guardsman }
whereabouts:
- {type: home, location: Eftly }
- {type: home, location: Cleenseau, start: 1718 }
- {type: away, start: 1719-10-21, end: 1719-10-23, location: Taviose}
- {type: home, start: 1719-11-16, location: Taviose}
dm_owner: mike
dm_notes: color
---
# Odo Cordwaner
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[odo-cordwaner.png|right|320]] Until recently a sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]], he was discharged after failing to heed orders during the [[Festival of the Bridge]]. He allowed [[Francois the Bandit|François the Bandit]] access to the food area, despite specific warnings to be on the lookup.

Investigation determined that he was not malicious, but just careless. In the excitement of the festival, he failed to pay attention as he should have. He was discharged from the [[Army of the West]], but at the intervention of [[Robin of Abenfyrd|Robin]], was hired by the [[Essfords]] to provide a steady presence in [[Taviose]].

He has since developed a romantic attachment to [[Abigail Moss]], and has come to believe that his mistake was the hand of [[The Warlord]], setting him on a path to find his true calling (and setting the [[Heroes of Cleenseau]] on the path to become heroes).

His family is based in [[Eftly]], but he left home at 18 to join the army, being the youngest of five children and with no interest in farming.

%% See [[The Destruction of Eftly]] for some background information %%

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
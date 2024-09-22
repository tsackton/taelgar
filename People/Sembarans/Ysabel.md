---
headerVersion: 2023.11.25
tags: [person, status/update]
campaignInfo: [ { campaign: clee }]
name: Ysabel
born: 1688
died: 1720-01-06
species: human
ancestry: Sembaran
gender: female
affiliations: 
- { org: Lord's Guard of Cleenseau, title: Sheriff }
whereabouts:
- {type: home, location: Cleenseau}
---
# Ysabel
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[ysabel.png|right|420]] A striking and comely woman with a rough scar running from her eye to her neck. She is the sheriff of [[Cleenseau]] and leads a part of the [[Lord's Guard of Cleenseau|Lord's Guard]]. She has many opinions about her employers, in particular [[Rinault Essford]], and does not always successfully keep them to herself.


%% Needs significant updates from play, including the fact that she died in battle %%







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
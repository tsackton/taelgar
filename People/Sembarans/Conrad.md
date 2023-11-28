---
headerVersion: 2023.11.25
tags: [person]
campaignInfo: [{campaign: clee, type: met, person: Viepuck, date: 1719-10-23 }]
name: Conrad
born: 1699
species: human
ancestry: Sembaran
gender: male
whereabouts: Cleenseau
---
# Conrad
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:clee%% Met by [[Viepuck]] on October 23rd, 1719 in [[Cleenseau]], the [[Barony of Aveil]], [[Sembara]] %%^End%%

[[Anselm|Anselm's]] assistant at the [[Temple of the Warlord in Cleenseau|Temple of the Warlord]]. A young, rather shy man, who looks up to Anselm but has become fascinated by the [[Heroes of Cleenseau]]. He is the main organizer of the [[Temple of the Warlord in Cleenseau|temple's]] charity, and knows the people of [[Beggar's Way]] relatively well. He was one of the few people in [[Cleenseau]] who was sad to learn of [[Nicholas the Beggar|Nicholas the Beggar's]] death.


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
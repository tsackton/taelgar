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
dm_notes: none
dm_owner: yes
---
# Conrad
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:clee%% Met by [[Viepuck]] on October 23rd, 1719 in [[Cleenseau]], the [[Barony of Aveil]], [[Sembara]] %%^End%%

![[conrard-cleenseau.png|right|320]][[Anselm|Anselm's]] assistant at the [[Temple of the Warlord in Cleenseau|Temple of the Warlord]]. A young, rather shy man, who looks up to Anselm but has become fascinated by the [[Heroes of Cleenseau]]. He is the main organizer of the [[Temple of the Warlord in Cleenseau|temple's]] charity, and knows the people of [[Beggar's Way]] relatively well. 

%%^Campaign:Clee%%
He was one of the few people in [[Cleenseau]] who was sad to learn of [[Nicholas the Beggar|Nicholas the Beggar's]] death.

Since the [[Heroes of Cleenseau]] arrived in town, he has become somewhat of a confidant of [[Viepuck]]. He often stops by [[Essford Manor]] in the mornings to chat with [[Viepuck]] and is a good source of information about [[Anselm]] in particular. Conrad admires [[Anselm]] for his strength and position, but as he has grown closer to [[Viepuck]] has shared some tidbits: Anselm's disinterest in charity, a story of how he has tried to use various festivals to glorify himself as much as the Warlord, his desire for a better position - perhaps even lord, of one of the other manors, if not [[Essford Manor]].
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
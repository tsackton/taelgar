---
headerVersion: 2023.11.25
tags: [place, testcase]
name: Taviose
typeOfAlias: village
typeOf: settlement
whereabouts: Manor of Cleenseau
population: 30
pronunciation: Ta-vi-ose
dm_notes: color
dm_owner: mike
---
# Taviose
*(Ta-vi-ose)*
>[!info]+ Information
> pop. 30
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small hamlet in the [[Cleenseau Region]] on the edge of the [[Cleenseau Wood]], a mile and a half north of [[Cleenseau]] along a dirt track. The small hamlet is mostly woodcutters, charcoal makers, and pig farmers and is part of the manor of the Lord of Cleenseau. It consists of about a ten buildings, only one of which is notable: a large, two story stone building with three large oak trees carved on the lintel, the home to [[Perrin Voclain]].  It is said this was once holy to a *[[kestavo]]* of the wood, who has long since departed.

There is a small shrine to the Wildling attached to Perrin's house, with several ancient oak trees, which mostly serves as a burial plot for the hamlet. Perrin tends to this shrine.

%%^Date:1720%%
In the late fall of 1719, was the site of [[Cleenseau Spider Attacks|several]] [[Cleenseau Spider Attacks|spider attacks]] from giant spiders that came from the [[Cleenseau Wood]]. [[Perrin Voclain]] and the [[Heroes of Cleenseau]] were instrumental in saving the hamlet, which was abandoned for about a week in late 1719. Despite this, the town lost about of third of it's population. 

The ongoing corruption from these spiders later caused several orchards and timber groves to become corrupted and die, until healed by [[Robin of Abenfyrd|Robin]].
%%^End%%
### Notable Residents
* [[Perrin Voclain]], an acolyte of the Wildling and druid
* [[Brot Starsearcher]], an eccentric dwarf, and their wife [[Diesla Starsearcher]]
* [[Abigail Moss]] and her two uncles, pig and chestnut farmers, the sole survivors amongst the Moss family from the spider attacks
* [[Hugh Darrow]] and his father [[Remy Darrow]], charcoal makers
* [[Phillipa Northwood]], a woodcutter in the large Northwood family, the poorest of the inhabitants
* [[Odo Cordwaner]], recently appointed guardsman for the hamlet

%%^Campaign:None%%
### People in, or based in Taviose
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Alive", "Age"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, true, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file),  util.isAlive(b), util.s("<age> (<startdate>)", b.file)]))
```
%%^End%%
---
headerVersion: 2023.11.25
tags: [place/village, testcase]
campaignInfo: []
name: Taviose
typeOfAlias: village
typeOf: settlement
subTypeOf: 
partOf: Cleenseau
population: 30
pronunciation: Ta-vi-ose
---
# Taviose
*(Ta-vi-ose)*
>[!info]+ Information
> pop. 30
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small hamlet in the [[Cleenseau Region]] of about a dozen farms, on the edge of the [[Cleenseau Wood]], a mile and a half north of [[Cleenseau]] along a dirt track. The small hamlet is mostly woodcutters, charcoal makers, and pig farmers and is part of the manor of the Lord of Cleenseau. It consists of about a dozen buildings, only one of which is notable: a large, two story stone building with three large oak trees carved on the lintel, the home to [[Perrin Voclain]].  It is said this was once holy to a *[[kestavo]]* of the wood, who has long since departed.

%%^Date:1720%%
In the late fall of 1719, was the site of [[First Spider Attack on Tavoise|several]] [[Second Spider Attack on Tavoise|spider attacks]] from giant spiders that came from the [[Cleenseau Wood]]. [[Perrin Voclain]] and the [[Heroes of Cleenseau]] were instrumental in saving the town, which was abandoned for about a week in late 1719. Despite this, the town lost about of third of it's population.

The ongoing corruption from these spiders later caused several orchards and timber groves to become corrupted and die 
%%^End%%

%%^Campaign:None%%
### People in, or based in Taviose
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home", "Alive"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, true, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.isAlive(b.file, dv.current().pageTargetDate)]))
```

%%^End%%
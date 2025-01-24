---
headerVersion: 2023.11.25
tags: [place, status/check/tim]
typeOf: region
whereabouts: [{type: home, location: Taelgar, linkText: "in" }]
dm_owner: tim
dm_notes: important
---
# The Northern Sentinels
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

North

![[north-sentinels-map.png]]

## Major Features
Few have mapped this region, but some major features are known, if not named:

* [[Forest of Nightmares]]
* [[Blackwater Fens]]
* North Sentinel Range
* [[~Unnamed North Sentinel Pass~]]

## Civilizations and Cultures
There are few humans in this region, although the [[Northern Tribes|northern Deno'qai tribes]] make their home here. The dwarven kingdom of [[Fahnukan]] lies beneath the northern Sentinels, and [[Stoneborn|stoneborn]] are known in this region as well. 

Historically, this was the land of [[Pandar]] and one of the major bases of [[Cha'mutte|Cha'mutte's]] [[Hobgoblins|hobgoblin]] armies. The [[~Unnamed North Sentinel Pass~]] was an early route of migration for [[~Northerner~]] as they moved east before the [[The Downfall|Downfall]].
## Climate


%%^Campaign:None%%

*Area:* This region includes the far northern section of the Sentinels, the [[Forest of Nightmares]], [[Pandar]], and the [[Blackwater Fens]]. 

*Canonical Development and Constraints:* [[Pandar]] was canonically [[Cha'mutte]]'s primary permanent territory, and a large number of kenku enslaved by Cha'mutte lived here prior to the [[Great War]]. The history of the [[History of the Northern Deno'qai|northern Deno'qai]], including some details of the Great War era, and their current [[Northern Tribes|culture and territory]] is well developed. The [[Forest of Nightmares]], and the [[Blackwater Fens]], have some canonical details. Stoneborn, at least, canonically live in the [[Sentinel Range|Sentinels]] in this region. 

*Non-Canonical Development:* Some basic overview of the history of Pandar and Cha'mutte's activities exist, but these are largely brainstorming, or at best weakly canonical. No details of Stoneborn settlements exist, except their presence. 

*Blank Regions:* Much of this region is functionally a blank spot. In general, this region was dominated by [[Cha'mutte]] during the [[Great War]] and is best kept relatively empty as a setting for dark and dangerous things.

*Adventures:* The Delwath solo arc of the Dunmar Frontier campaign was set in the northern Deno'qai territory and the Forest of Nightmares; the black dragon arc of the Great Library campaign was set in the Blackwater Fens. 
### Places in North Sentinels
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%
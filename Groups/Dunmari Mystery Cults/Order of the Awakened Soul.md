---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <typeof:UA> of <deity:UA>"}
typeOf: mystery cult
ancestry: Dunmari
deity: Bhishma
dm_notes: important
dm_owner: tim
---
# The Order of the Awakened Soul
>[!info]+ Information  
> A [[Dunmar|Dunmari]] mystery cult of [[Bhishma]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

The mystery cult dedicated to the Dunmari god [[Bhishma]]. Dedicated to collecting the stories of the Dunmari, preserving the memories of the people of Dunmar, and making sure the  souls of the dead are not forgotten and lost. 

%%^Campaign:dufr%%
After the [[Great War]], the Order was one of the few who remained as much as they could in the [[Nashtkar]], as most Dunmari fled west. They made it their mission to find the many souls lost and wandering, unable to reach the [[Land of the Dead]], and help them find peace.

In the early 1700s, explorers and travelers from the Order reached as far as Drankor, and discovered [[Rai]], who spoke of the evil spreading from the wounds [[Cha'mutte]] left in the world. 

In DR 1718, the Order and Rai traveled together to [[Isingue]], and attempted to cleanse the land of the [[Seeds of Chaos]] left by [[Cha'mutte]]'s death, but [[Awakened Soul Disaster|failed]]. The few members of the Order that survived fled west, and scattered across [[Eastern Dunmar]] and [[Central Dunmar]], doing what they still could to tend the stories of the people. 

> [!warning]- Kenzo's conversation with Pava 
> 
> ### [[Kenzo]] and [[Pava]], [[Session 20 (DuFr)]]
> 
> [[Kenzo]] spoke with [[Pava]] to ask him what he knew of the Order of the Awakened Soul. During this conversation, he learned the following:
> 
> - The Order of the Awakened Soul was the pre-[[Great War]] name of the Mystai of [[Bhishma]]. When the order was founded in the years after [[Bhishma]] passed on from the mortal world and took up residence in the land of the gods, their mission was to tend to the soul of [[Dunmar]], and especially to see that the stories of the people of [[Dunmar]] were remembered, as [[Bhishma]] saw the people of the land as the heart and soul of the country. 
> - Since the [[Great War]], that name has fallen out of use, as the Mystai turned their focus to the dead, and from “awakening the soul of the country” to putting lost spirits to peaceful sleep.
> - The order is now all but dead, and few remember the time before the events 30 years ago during which many of the strongest of the Mystai died in an attempt at something, some ritual to cleanse the land. [[Pava]] and [[Avaras]] were still wanderers then, not yet promoted to masters.
> - The only master that [[Pava]] can think of who may still remember the times before is [[Saka]], an old woman who was a master before the attempted ritual but chose not to participate. He has not seen her in five years or more, but she always said that when she got too old to travel she was going to settle in the lands north and west of [[Tokra]], among the horse herders on the plains. So perhaps she is still there.
> - The Mystai of [[Bhishma]] are now few and far between. They do gather every few years for the Feast of [[Bhishma]], but [[Pava]] and [[Avaras]] did not attend the last gathering and don’t expect to make long journeys from their home anymore.

%%^End%%


%%SECRET[1]%%


%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
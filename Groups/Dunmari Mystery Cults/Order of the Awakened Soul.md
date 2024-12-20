---
headerVersion: 2023.11.25
tags: [organization]
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


%%SECRETS
## Summary

The mystery cult of Bhishma, the first ruler of Dunmar, the mother of Kotana and Shakun, the lover of Laka, and the spiritual founder of Dunmar.

Long associated with remembering the stories of the common folk and keeping the 'soul of Dunmar' true.

For generations they have wandered the blasted plains looking for souls that have lost their way, those who died a violent death and cannot rest. Some, who have faded away and whose soulls are lost, and yet nonetheless they try to remember them, to tell their stories and give some peace to Bhishma, to the mother of Dunmar, who mourns every Dunmari who dies forgotten.

For some time after the Great War, took on the task of trying to cleanse the land, with Rai's aid and encouragement, but failed.

They know [[Agata]], and hate her with a deep and abiding passion. But that is not their work and while there are lost souls to put to rest they cannot turn to other matters.

They know that something evil and undead has haunted Kharsan for generations, but seems to be getting stronger. It has been many, many years since it has been safe to venture to the monastery there.

## History

The Order of the Awakened Soul was founded early in the history of Dunmar, as the mystery cult of Bhishma, the mother of Dunmar. For a long time, they had a small presence, mostly associated with the Feast of Bhishma.

At some point, they started seeing it as their mission to collect stories and preserve the history of the Dunmari people, not the epic arc of history, which is more the Lakan tradition, but the stories of the people themselves. They evolved into an itinerant order, with monks who would wander and record the tales of families traveling on the plains.

In the run up to the Great War, they began speaking of great destruction to come, and a need to preserve the history of the people. They constructed a monastery on the banks of the Kharja, near where Bhishma is said to have prayed for a year to bring back Jeevali.

In this monastery the memories of the people and the story of the land was preserved. Until the Great War, when it was lost in the desert.

After the Great War, the monks of the Awakened Soul took on the task of stewarding the souls of the lost, the abandoned, wandering the blasted plains seeking the forgotten dead and learning what they could of them, telling their stories and helping their souls reach the afterlife.

Several generations ago, before the rise of Apollyon, some leaders of the order ventured to Drankor itself, where they met Rai, and took on the task of healing the land as well, the land that Jeevali restored for Dunmar and now was in the spiritual care of Bhishma.

This is no easy task, of course. About 30 years ago, many of the most powerful in the order, along with Rai, attempted to cleanse the land, but failed.

Since then, Rai has been missing and the order in a bit of disarray.

## Organization

Formally, organized by area, with particular monks having a 'territory', usually a master (or two) who then have a series of apprentices. Apprentices graduate to wanderers who travel among territories, learning the land and the organization, until a master passes on, when a wanderer is called to take their place.

Above the masters, a council of Supremes makes decisions -- but since the attempt and failure 30 years ago, most of the hidden knowledge of the council was lost, including the identity of Rai and the nature of the curse on the land.

Since then, many have despaired and there has been a renewed focus on the original mission, the stories of the people, and serving Bhishma. There is still a gathering of wanderers and some masters and the few remaining supremes every year at the Feast of Bhishma, where new apprentices are initiated, and wanderers are assigned to masters. Apprentices are sent out by their masters, and masters become supremes soley by the choice of Bhishma.
%%


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
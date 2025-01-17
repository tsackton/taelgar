---
tags: [organization, status/stub, status/check/mike, status/check/tim]
dm_owner: mike,tim
dm_notes: none
---

%% putting status/check/mike, status/check/tim as this needs a bit of joint work to write a centralized note. i have nothing in my dm notes except what is here%%

%% centralized notes from [[Fazoth de Brune|Fazoth]] backstory here

The de Brune family is a wealthy mercantile family, with a primary manor on the outskirts of Eskbridge, and extensive mercantile connections along the river valley, reaching into Addermarch even.  At least at the time of the Addermarch campaign, which is between 10-30 years after the Cleenseau campaign , the de Brunes are well known enough that people think, "oh, those de Brunes and associate the name with wealth." But they plausibly for example were just well-placed to grow after all the lich chaos, setting them up to go from a wealthy but minor player in 1720 to having a bigger, more famous role in 1730. 

Unknown to outsiders, the de Brune family also had a secret: they were powerful supporters and members of a secret cult connected to the archfey [[Lord Serenveil]]. The details of this cult are unclear, as is their positioning with respect to the main Ethlenn / Umbraeth conflict. But likely / presumably, Serenveil is either allied with Ethlenn, or something of a neutral arbiter. He is powerful enough to be a warlock patron, but minor enough to not have a large feywild domain of his own. Exactly why the de Brunes have this feywild connection is TBD and flexible. 

For my Addermarch game, this is really just a setup to give Nathaniel the secret backstory he wants, and to set up his archfey warlock subclass. For a while at least the larger story about the de Brunes will likely be somewhat irrelevant. 

[[Lord Serenveil]], Prince of the Vesperwind, Guardian of Twilight's Edge:

Tall, towering figure, long flowing silver hair, dark skin, dressed in robes that shift colors between deep purples, dusky blues, and silvery grays. Fiery eyes, like fading sunset. 

A few notes from Cleenseau game:
* The de Brune branch in Cleenseau is well known in the region as wealthy already; it is plausible they are fairly well known along the Enst in 1720 although perhaps not AS well known as they become

In general, the vibe should be that the de Brunes to have grown from reasonably wealthy and well-connected in 1705-1720 to famous and very rich in 1730-1745. I kind of like the trajectory of them being relatively "new rich" and upwardly mobile but not necessarily having very ancient wealth; this works for Nathaniel's backstory as he tends to play Fazoth more as "famous for being rich" than "rich because they are famous/old" 

In particular, in the late 1690s-early 1710s they were very much "workers" and managers, trading agents, factors, etc more than their own thing. faciliate others. but this lead to opportunities for growth and in the aftermath of the lich disaster they rapidly grew to prominence

Some important bits about one minor branch in [[Istarias]] page
%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
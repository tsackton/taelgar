---
tags: [organization, status/stub]
dm_owner: shared
---

%% centralized notes from [[Fazoth de Brune|Fazoth]] backstory here

The de Brune family is a wealthy mercantile family, with a primary manor on the outskirts of Eskbridge, and extensive mercantile connections along the river valley, reaching into Addermarch even.  At least at the time of the Addermarch campaign, which is between 10-30 years after the Cleenseau campaign , the de Brunes are well known enough that people think, "oh, those de Brunes and associate the name with wealth." But they plausibly for example were just well-placed to grow after all the lich chaos, setting them up to go from a wealthy but minor player in 1720 to having a bigger, more famous role in 1730. 

Unknown to outsiders, the de Brune family also had a secret: they were powerful supporters and members of a secret cult connected to the archfey [[Lord Serenveil]]. The details of this cult are unclear, as is their positioning with respect to the main Ethlenn / Umbraeth conflict. But likely / presumably, Serenveil is either allied with Ethlenn, or something of a neutral arbiter. He is powerful enough to be a warlock patron, but minor enough to not have a large feywild domain of his own. Exactly why the de Brunes have this feywild connection is TBD and flexible. 

For my Addermarch game, this is really just a setup to give Nathaniel the secret backstory he wants, and to set up his archfey warlock subclass. For a while at least the larger story about the de Brunes will likely be somewhat irrelevant. 

[[Lord Serenveil]], Prince of the Vesperwind, Guardian of Twilight's Edge:

Tall, towering figure, long flowing silver hair, dark skin, dressed in robes that shift colors between deep purples, dusky blues, and silvery grays. Fiery eyes, like fading sunset. 

A few notes from Cleenseau game:
* The de Brune branch in Cleenseau is well known in the region as wealthy already; it is plausible they are fairly well known along the Enst in 1720 although perhaps not AS well known as they become
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
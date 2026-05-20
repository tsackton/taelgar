---
headerVersion: 2023.11.25
tags: [group, status/check/mike]
dm_owner: mike,tim
dm_notes: none
typeOf: family
---
# The De Brunes
>[!info]+ Information  
> A family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The de Brunes are a wealthy mercantile family with roots in the [[Enst]] river valley, and a primary manor just outside [[Eskbridge]]. The family maintains outposts and connections along the Enst, including a longstanding presence in the [[Cleenseau Region]]. In recent years, de Brune business in the Cleenseau region has been shaped by [[Catherine de Brune]]’s investments and trade ties.

%%^Campaign:None%%
### Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%% 

Unknown to outsiders, the de Brune family also had a secret: they were powerful supporters and members of a secret cult connected to the archfey [[Lord Serenveil]]. The details of this cult are unclear, as is their positioning with respect to the main Ethlenn / Umbraeth conflict. But likely / presumably, Serenveil is either allied with Ethlenn, or something of a neutral arbiter. He is powerful enough to be a warlock patron, but minor enough to not have a large feywild domain of his own. Exactly why the de Brunes have this feywild connection is TBD and flexible. 

[[Lord Serenveil]], Prince of the Vesperwind, Guardian of Twilight's Edge:

Tall, towering figure, long flowing silver hair, dark skin, dressed in robes that shift colors between deep purples, dusky blues, and silvery grays. Fiery eyes, like fading sunset. 

Some important bits about one minor branch in [[Istarias]] page

---

A few notes from Cleenseau game:
* The de Brune branch in Cleenseau is well known in the region as wealthy already; it is plausible they are fairly well known along the Enst in 1720 although perhaps not AS well known as they become

Not sure if this is real anymore or not, given Addermarch game now set in 1715. My vote is mostly no, especially bullet #2. It still works if the timeline is pushed back a little, but they need to be wealthy in 1715 already. 

- In general, the vibe should be that the de Brunes to have grown from reasonably wealthy and well-connected in 1705-1720 to famous and very rich in 1730-1745. I kind of like the trajectory of them being relatively "new rich" and upwardly mobile but not necessarily having very ancient wealth; this works for Nathaniel's backstory as he tends to play Fazoth more as "famous for being rich" than "rich because they are famous/old" 

- In particular, in the late 1690s-early 1710s they were very much "workers" and managers, trading agents, factors, etc more than their own thing. faciliate others. but this lead to opportunities for growth and in the aftermath of the lich disaster they rapidly grew to prominence

%%
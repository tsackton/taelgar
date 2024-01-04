---
headerVersion: 2023.11.25
tags: [place, status/needswork]
name: Dunmar
whereabouts: Greater Dunmar
typeOf: realm
---
# Dunmar
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Dunmar is an ancient theocratic monarchy stretching more than 700 miles across the central lowlands of [[~Northern Continent~]], bordered by the coast of the [[Nevos Sea]] and the [[Myraeni Gap]] in the west, the [[Sentinel Range]] in the north, and the  barren wastelands of the [[Nashtkar]] and the [[Garamjala Desert]] in the east and south. Founded in DR 1173 by the great leader and first Samraat [[Bhishma]], who is now a goddess and a divine protector of her people, Dunmar survived the turmoil of the [[Great War]] and the upheavals of [[~Cha'mutte's Destruction~]], and now occupies a land much-changed from the fertile grasslands of its founding.

Dunmar was founded on the territory that was formerly the heartland of the [[Drankorian Empire]], but left largely, although not entirely, empty by the [[~Fall of Drankor~]]. The palace and administrative center of the [[Aatmaji Dynasty]], the founding dynasty of Dunmar, was [[Kharsan]] and the [[Kharja]] river valley. When the [[Aatmaji Dynasty]] was ended after a disastrous attempt to invade and cleanse [[Drankor]], after a short period of chaos, the political and cultural center of the country moved west under the [[Dharajun Dynasty]], to the city of [[Tokra]]. Dunmar reached its peak of power and influence during this time, thanks in part to its agricultural wealth (largely in horses and sheep) and overland trade network connecting the east and west. 

During the [[Great War]], however, Dunmar suffered terribly. The [[Dharajun Dynasty]] was destroyed, many Dunmari died in battle against [[Cha'mutte]]'s armies, and the eastern part of the country was destroyed. After [[Cha'mutte]]'s defeat, the land itself was reshape: the [[Garamjala Plateau]] and the [[Yuvanti Mountains]] rose violently and suddenly, shifting the course of the [[Istaros|Mahar]] and creating the [[Dunmari Basin]]. Yet the Dunmari survived, and built a new country in the changed land. 

Now, Dunmar is culturally divided by the [[Yuvanti Mountains]] and the [[Darba Highlands]]. To the east, the Dunmari who live in the dry, arid grasslands and deserts of the [[Dunmari Basin]] maintain a traditional nomadic way of live, moving with their herds of horses, sheep, and goats across the plains with the seasons, and gathering at temples and religious sites to mark the festivals and turnings of the year. To the west, the people living on the coastal plains and in the river valleys and rolling hills of highlands have adopted a much more sedentary lifestyle, with a much greater focus on permanent agriculture. 

Nonetheless, the Dunmari remain united by their worship of the [[Five Siblings]], the divinities that protect the people, and worship of these deities is a central part of all Dunmari culture and civic life. 
## Geography 

Dunmar is the largest and most significant populated realm in the [[Greater Dunmar]] region, covering nearly 400,000 square miles, although much of that territory is sparsely settled or uninhabited desert. 

### Climate


### Regions



## History



## Life in Dunmar




%%^Campaign:None%%
## Places in Dunmar
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Subtype"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter))
				.sort(f => util.s("<maintype>", f.file))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name:x> (<pronunciation>)", b.file), util.s("<home:1x>", b.file), util.s("<maintype>", b.file), util.s("<subtype>", b.file)]))
```

%%^End%%
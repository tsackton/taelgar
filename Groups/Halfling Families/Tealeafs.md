---
tags: [organization/family, status/unknown]
displayDefaults: {defArt: the}
campaignInfo: []
name: Tealeafs
typeOf: family
---

%%notes from Garret
The patriarch of a halfling trading family that would make a long circuit from Chardon east to Songara, Tokra, and Karawa before turning south, trading with the dwarves, and then crossing the mountains to Nayahar, then traveling along the coast and turning north again for Chardon. The Tealeafs were a large family, traveling often in 4-5 wagons, well armed and defended. Eleven years ago, as [[Agata]] was starting to build her [[Orcs|orc]] horde and gain the loyalty of those who would become the Dustthorn Horde, the [[Orcs]] attempted to raid the Tealeaf caravan, and were unexpectedly repulsed, suffering many causalities. In revenge, [[Agata]] attacked, killing about half the clan with AoE spells and then diving down on her giant fly to grapple and drag away Garret. She told the survivors that if they did not come east of the Hara River for 15 years, she would return Garret to them. Since then, the Tealeaf clan has shortened their route to turn south from Songara, trading at Darba and Nayahar then back to Chardon.
%%


%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file.frontmatter))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter)]))
```
%%^End%%
---
headerVersion: 2023.11.25
tags: [place]
name: Mawakel Peninsula
typeOf: region
whereabouts: West Coast Region
---
# The Mawakel Peninsula
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


The Mawakel Peninsula is a land of contrasts and challenge. The peninsula is cut off from the mainland by steep, rocky mountains, making coastal travel the primary means of access. The center of the peninsula is dominated by the swift-flowing [[Sulqat]] river. Little of the river is navigable by ship, but the salmon run on the [[Sulqat]] is a major source of food and wealth for the Mawar and most of the inland settlements on the peninsula are on this river. 

The [[Sulqat]] river valley in the center of the peninsula is separated from the coasts by steep hills dominated by dense, old growth pine forests. The coasts themselves are rocky and dominated by steep cliffs and narrow inlets. 

The western and northern side of the peninsula tend towards milder climates, with less snow in the winter, while the interior and eastern sides are colder and receive often heavy snowfalls, especially towards the higher elevations near the mountains.

%%^Campaign:None%%
### Cities in Mawakel Peninsula
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter) && (f.file.frontmatter.typeOf == "city" || f.file.frontmatter.typeOf == "village" || f.file.frontmatter.typeOf == "town" || f.file.frontmatter.typeOf == "hamlet"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name>", b.file), util.s("<home:1>", b.file), util.s("<maintype>", b.file), util.s("<population>", b.file)]))
```

%%^End%%
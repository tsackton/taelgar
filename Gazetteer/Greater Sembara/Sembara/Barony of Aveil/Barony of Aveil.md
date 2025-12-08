---
headerVersion: 2023.11.25
tags:
  - place
name: Barony of Aveil
typeOf: subdivision
whereabouts: Sembara
pronunciation: Ah-veh-eel
dm_notes: color
dm_owner: mike
typeOfAlias: barony
---
# The Barony of Aveil
*(Ah-veh-eel)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Barony of Aveil is one of the oldest baronies in Sembara, sitting between the [[Western Marches]], the powerful [[Duchy of Wisford]], and the sparsely settled [[Borderlands]]. The western third of the barony is dominated by the [[Cleenseau Wood]], and ancient old-growth forest. In the north, the [[Aveil Ridge]], a small escarpment, defines the northern quarter of the barony, and is home to the seat of the baron, [[Veltor]], a small fortified castle near the headwaters of the [[Auberonne]]. Two rivers run through the barony: the [[Auberonne]], which runs the length of the barony, and the [[Leandre]] which is smaller and flows from the [[Cleenseau Wood]] to the [[Auberonne]]. 

The borders of the barony are the height of land of the [[Aveil Ridge]] in the north, 12 miles from the course of the [[Auberonne]] in the east, the [[Enst]] in the south, and, for all practical purposes, the eastern edge of the [[Cleenseau Wood]].

The three largest settlements in the barony are [[Rinburg]], a free city on the [[Enst]], [[Cleenseau]], an important market town, also on the [[Enst]], and [[Aslain]], a market town at the confluence of the [[Auberonne]] and the [[Leandre]]. 

The barony is characterized by six major regions:

* the [[Cleenseau Region]] in the west is somewhat disconnected from the rest of the barony, there being no settlements for the fifteen miles between [[Dallet]] and [[Beury]]
* [[Rinburg]] and the [[Enst]], a land of sheep herders and fishing villages, all clustered along the [[Enst]] and the [[Great South Road]], including the market towns of [[Champimont]] and [[Dallet]]
* the [[Aveil Ridge]] in the north, a escarpment that rises about 2500' above the land, the source of the [[Auberonne]] and little-settled hilly land of secondary forest. The seat of the baron, [[Veltor]], is here
* the [[Auberonne]] valley, the richest farmland of the barony. [[Aslain]], one of the largest market towns in the barony, is here.
* the [[Cleenseau Wood]], and the small villages along its eaves, in particular near the [[Leandre]]
* the [[Madour Hills]], which separate the villages along the [[Enst]] from the more northern parts of the barony

Most of the settlement in the barony is along the eastern valleys and banks of the [[Auberonne]], where the farmland is better, and the sheep pastures along the [[Enst]]. 

## Map

![[Aveil.jpg|800]]

In general, despite its relatively ancient roots, [[Barony of Aveil|Aveil]] is a poor barony largely dominated by the powerful [[Duchy of Wisford]] to its west, save for the [[Cleenseau Region]], which tends to see itself as more independent and if anything, more aligned with the powerful [[Army of the West]]. [[Rinburg]], at the head of the navigation of the [[Enst]] is a wealthy and bustling market town, but as a free city, contributes little to the barony itself. Even the better farmland in the eastern [[Auberonne]] valley is not as rich as the heartlands of Sembara, and much of the land was pillaged by hobgoblins during the [[Third Hobgoblin War (Sembara)|hobgoblin wars]]. [[Veltor]] never fell, and the [[Aveil Ridge]], with its many caves, was a redoubt for Sembaran troops resisting the hobgoblins. There are several rich tin mines in the [[Aveil Ridge]], but they are controlled by the [[Duchy of Wisford]] and contribute little to the wealth of the barony.

There is a maintained road the length of the [[Auberonne]], from [[Rinburg]] to [[Veltor]], and the [[Aveil Road]] which runs north from the tin mines to the [[Wistel]].

### Cities in Barony of Aveil
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, true, true, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "settlement"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.s("<maintype>", b.file, dv.current().pageTargetDate), util.s("<population>", b.file, dv.current().pageTargetDate)]))
```

### Rivers and Landforms 
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "waterway" || f.file.frontmatter.typeOf == "landform"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^Campaign:None%%
### People in, or based in Barony of Aveil
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
---
headerVersion: 2023.11.25
tags: [place]
name: Istaros Watershed
typeOf: watershed
whereabouts:
- { type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
---
# The Istaros Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Istaros watershed is the vast river basin that gathers into the [[Istaros]] and its many tributaries, stretching from the [[Mostreve Hills]] to the [[Sea of Storms]]. For much of recorded history it has been a fertile crossroads, central first to vast elven realm of [[Alcarinque|Alcarinquë]], then to the [[Drankorian Empire]]; even after the [[Fall of Drankor]] the upper Istaros served as a crucial connection between [[Cymea]] and the [[Green Sea]], the [[Istabor Alliance]], and the [[Dunmar|Dunmari]]. 

Since the [[Great War]], much of the watershed has been defined by the scars and magical curses of [[Cha'mutte]]. The upper Istaros flows through the [[Plaguelands]], where the ruined city of [[Isingue]] lies near one of the watershed’s most storied confluences; beyond, it passes into the [[Desolation of Cha'mutte]] around the ruined city of [[Drankor]]. 


%%^Campaign:None%%
### Places in the Istaros Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

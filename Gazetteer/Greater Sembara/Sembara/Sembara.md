---
headerVersion: 2023.11.25
tags: [place, status/incomplete]
displayDefaults: { ruledBy: "Ruled by: <name> <((since )startDate())>"}
name: Sembara
typeOf: realm
whereabouts: Greater Sembara
dm_owner: shared
dm_notes: important
---
# Sembara
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Sembara is a large and properous realm in the [[Western Green Sea]] situated amongst five great rivers that pour down from the [[Sentinel Range|Sentinels]] to the [[Western Gulf]].  One of the few realms in the east to survive the Blood Years largely intact, Sembara is a hereditary monarchy with a large nobility and considerable prowess at arms. Sembara invests significantly in defensive fortifications in the [[Western Marches]], on the western (mountain) borders of the realm. These areas are under threat from hobgoblins, aberrations, and other incursions from the wilds, and the defense of these borders is a major concern for the ruling class. While most of the Sembaran population descends from the Drankorians who conquered the land, in the highlands traces of the original culture survive. And in Tyrwingha, ancient connections to the Archfey who once protected the realm still linger.


-   Inward agricultural focus. Sphere of influence pushing more west and interior than into the [[Western Gulf]] - limited or no real navy, small scale fishing but not a major part of the culture or economy (think China)
    
-   Trade devalued -- historical analog: ancient Rome, where wealth from land was much more significant than wealth from trade
    
-   Very fertile soil and rich agricultural harvests in the heart of Sembara drive the economy. Major exporter of foodstuffs and raw materials. Also higher population density than anywhere else between the good soil and the miracle that the heartland of Sembara has never been overrun by anything too bad since even before the Drankorians relatively gently took over
    
-   Landed barons and dukes dominate local politics
    
-   Very good relationship with halflings, who are the favored traders, and have formal rights of free passage and access to markets across Sembara.
    
-   Cooler relationship with dwarves -- not at all hostile, but dwarves are more aligned with the highland kingdoms, esp Ardlas and Lavnoch
    
-   Close relationship with lizardfolk, who have played an outsized role in Sembara’s history and establishment of [[House of Sewick]].
    
-   Elves very rare in Sembara, with little direct political contacts; largest Elven settlement nearby is the semi-mythical kingdom of [[Orenlas]] in the forests surrounding a supposedly enchanted lake south/southeast of Tyrwingha in the Cymea foothills.
    
-   Stoneborn are also very rare in Sembara; mostly in the high peaks north of Ulrich devastation; more common in Northlands than elsewhere, coming from the [[Vostok]] highlands


## Map

```leaflet 
id: region-map-sembara
image: [[[sembara-regions.png]]] 
bounds: 
- [0,0]
- [2468, 2308]
height: 900px
lat: 1200
long: 1200
minZoom: -1
maxZoom: 3
defaultZoom: 0
unit: miles 
scale: 0.5
```



%% Notes
The largest and most prosperous realm on the [[Western Gulf]] of the [[Green Sea]], Sembara is an old and traditional monarchy, situated amongst five great rivers that pour down from the high mountains to the sea. One of the few realms in the east to survive the Blood Years largely intact, Sembara is a hereditary monarchy with a large nobility and considerable prowess at arms. Sembara invests significantly in defensive fortifications in the Western Marches, on the western (mountain) borders of the realm. These areas are under threat from hobgoblins, aberrations, and other incursions from the wilds, and the defense of these borders is a major concern for the ruling class. To the south, a series of earls and other border lords watch the Southern Marches for incursions from the Plaguelands. While most of the Sembaran population descends from the Drankorians who conqueored the land, in the highlands traces of the original culture survive. And in Tyrwingha, ancient connections to the Archfey who once protected the realm still linger.
-   Inward agricultural focus. Sphere of influence pushing more west and interior than into the [[Western Gulf]] - limited or no real navy, small scale fishing but not a major part of the culture or economy (think China)
    
-   Trade devalued -- historical analog: ancient Rome, where wealth from land was much more significant than wealth from trade
    
-   Very fertile soil and rich agricultural harvests in the heart of Sembara drive the economy. Major exporter of foodstuffs and raw materials. Also higher population density than anywhere else between the good soil and the miracle that the heartland of Sembara has never been overrun by anything too bad since even before the Drankorians relatively gently took over
    
-   Landed barons and dukes dominate local politics
    
-   Very good relationship with halflings, who are the favored traders, and have formal rights of free passage and access to markets across Sembara.
    
-   Cooler relationship with dwarves -- not at all hostile, but dwarves are more aligned with the highland kingdoms, esp Ardlas and Lavnoch
    
-   Close relationship with lizardfolk, who have played an outsized role in Sembara’s history and establishment of [[House of Sewick]].
    
-   Elves very rare in Sembara, with little direct political contacts; largest Elven settlement nearby is the semi-mythical kingdom of [[Orenlas]] in the forests surrounding a supposedly enchanted lake south/southeast of Tyrwingha in the Cymea foothills.
    
-   Stoneborn are also very rare in Sembara; mostly in the high peaks north of Ulrich devastation; more common in Northlands than elsewhere, coming from the [[Vostok]] highlands
%%

%%^Campaign:None%%
### Cities in Sembara
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "settlement"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.s("<maintype>", b.file, dv.current().pageTargetDate), util.s("<population>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
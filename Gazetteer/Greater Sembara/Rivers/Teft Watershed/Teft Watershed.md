---
headerVersion: 2023.11.25
tags: [place]
name: Teft Watershed
typeOf: watershed
whereabouts:
- { type: home, location: Greater Sembara, linkText: in }
dm_owner: none
dm_notes: none
---
# The Teft Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Teft watershed drains northwestern [[Sembara]] into the [[Western Gulf]]. Its principal river, the [[Teft]], gathers swift mountain waters from the [[Sentinel Range|Sentinels]] before plunging through the [[Great Chasm]] on its way to the sea north of [[Embry]]. Few of the rivers in this watershed are navigable, and the Teft and its tributaries often function as barriers to movement and serve as borders. 

%%^Campaign:none%%

## DM notes

### Mapped rivers

Mapped rivers of the Teft Watershed:

[[Teft]]: 
source: 10.10.B18
end (ocean): 11.11.H.20

[[Berze]]:
source: 10.10.D.03
end (Teft): 10.10.E.09

[[Vilna]]:
source: 10.10.E.11
end (Teft): 10.10.E.09

[[Selgrava]]:
source (Breva): 10.10.G.23
end (Teft): 10.11.B.02

Unnamed 1:
source (Breva): 10.11.B.17
end (Teft): 10.11.B.16

Unnamed 2:
source (Breva): 10.11.E.11
end (Teft): 10.11.F.07

Unnamed 3:
source (Aine Hills): 11.11.D.01
end (Teft): 11.11.D.14

There is probably at least two missing rivers:

Approximately source (Braebin): 10.11.I.03, end (Teft): 11.11.H.05
Approximately source (Sembara): 11.11.E.14 end (Teft): 11.11.H.10

## Places in the Teft Watershed

```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

 %%

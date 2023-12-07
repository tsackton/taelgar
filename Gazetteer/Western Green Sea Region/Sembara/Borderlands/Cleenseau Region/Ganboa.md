---
headerVersion: 2023.11.25
tags: [place]
name: Ganboa
pronunciation: Gan-bo-a
partOf: Barony of Aveil
typeOf: settlement
ancestry: lizardfolk
typeOfAlias: village
population: 62
---
# Ganboa
*(Gan-bo-a)*
>[!info]+ Information
> pop. 62
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small lizardfolk village a few miles downstream on the Enst, known in [[Cleenseau Region]] as a good source of healing herbs. Several lizardfolk from Ganboa are regulars at the markets in [[Cleenseau]] and [[Beury]].  Ganboa is built on a cul-de-sac in the [[Enst]] where the banks become very marshy and the river splits and northly channel meanders through several large marshy flats. It is a small village of only about a two dozen huts, about half scattered across the semi-permanent marsh islands, and the other half along the banks of the river. 

A small community of fisherfolk in [[Asineau]] has been known to grumble about lizardfolk getting preferential fishing rights when times are lean, but relationships with the humans in the region as usually quite good.
### Notable Residents

* [[Erdu]], the spokesperson
* [[Unai]], a noted herbalist and healer, chiefly responsible Ganboa's reputation
* [[Koldo]], a reclusive druid who is well respected in the town but rarely talks to non-lizardfolk

%%^Campaign:None%%
### People in, or based in Ganboa
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
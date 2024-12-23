---
headerVersion: 2023.11.25
tags: [place]
name: Asineau
typeOf: settlement
typeOfAlias: fishing village
population: 311
whereabouts: Manor of Asineau
pronunciation: Ah-zee-noh
dm_notes: important
dm_owner: mike
---
# Asineau
*(Ah-zee-noh)*
>[!info]+ Information  
> pop. 311  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[asineau-image-2.png|right|320]] ![[asineau-docks.jpg|right|320]]A manorial fishing village on the banks of the Enst, two miles downriver of [[Auloutte]]. The village is small, about 50 houses, mostly clustered a hundred feet above the banks of the Enst in a rough line, anchored at one end by a humble temple of the Wyrdling and the other by the manor house. There are three wooden docks, and a sandy beach where small fishing rafts can pull out, just before the banks turn marshy. There is no blacksmith, folks walk the 2.5 miles to [[Beury]] if they need a horse shoed or a plow made. About half the inhabitants of Asineau fish, and there are occasional disagreements with the lizardfolk in [[Ganboa]] when the catch is small. Much of the farmland is middling, at best, rockier than other parts of the region.

A few hundred feet outside the village is a small mill and bakehouse. The large stone manor house dates from the early 1600s, and stands alongside the road. There is a stable building attached to it. 

![[asineau-wrydling-painting.jpg|right|320]]The temple to [[The Wyrdling]] here is known for a chaotic painting on the wall, and is said to have been standing in this spot for over 500 years. There are two local miracles celebrated in Asineau: the [[Miracle of the Hopeful Heat]] and the [[Miracle of the Guided Wanderers]]

## Notable Residents

* [[Lorin Valbert]], the lord, recently fled
* [[Isolde]], Lord Valbert's chief muscle and advisor, departed with her lord
* [[Connor]], [[Matias]] and [[Elbeth]], Lorin's guards and valets
* [[Susanna Northwoods]], his steward and secretary, and the wife of Bertram
* [[Bertram Northwoods]], the stablemaster
* [[Eleanor]], the steward of the temple
* [[El]], an acolyte of the Wyrdling, associated with the temple
* [[Thierry]], a boatbuilder and veteran of the [[Army of the West]]
* Jacques, Thierry's brother, and his husband Ari, fishermen
* [[Arnold the Miller]], a racist miller and baker, although no fan of Lorin's taxes
* Celia, a young stablehand of 11 or 12, scrawny but not malnourished, known as Sweet Little Hayhead to the horses

%%^Campaign:None%%
### People in, or based in Asineau
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
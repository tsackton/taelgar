---
headerVersion: 2023.11.25
tags: [place]
name: Auloutte
typeOf: settlement
typeOfAlias: fishing village
whereabouts: Manor of Cleenseau
population: 102
pronunciation: OO-loot
---
# Auloutte
*(OO-loot)*
>[!info]+ Information  
> pop. 102  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A poor fishing village on the banks of the [[Enst]], a short walk from [[Cleenseau]]. It is nestled on reclaimed marsh between the [[Great South Road]], [[Amance Brook]], and the [[Enst]]. About a mile downriver from Cleenseau, just before the road crosses the Amance, it is part of the [[Manor of Cleenseau]]. About a dozen boats fish for river trout in the spring and summer, from a makeshift dock rebuilt each April. The twenty houses here flood at times, save for the sturdy mill, built on the banks of the [[Amance Brook]], and the small temple of the Warlord built next to the mill. 

### Notable Residents
* [[Gideon Thorne]], a prominent fisherman and part-time steward of the small temple
* Lucien, a skilled fisherman, quite knowledgeable about the river currents, who fished [[Cedric]] from the river
* Marguerite, the toll collector and miller

%%^Campaign:None%%
### People in, or based in Auloutte
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
---
headerVersion: 2023.11.25
tags: [status/cleanup/text, organization]
typeOf: clan
displayDefaults: {defArt: "the" }
ancestry: dwarven
whereabouts: Barony of Aveil
dm_notes: none
dm_owner: none
---
# The Ferrystones
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A fairly prominent dwarven clan with longstanding ties to [[Rinburg]] and [[Aslain]], known since at least the [[Third Hobgoblin War (Sembara)|hobgoblin wars]] for their work building with recovered stones from ruins.

%% 
dwarven clan in Rinburg and Aslain,; have a small clanhouse in Aslain and larger buildings in Rinburg
important  / connected enough to have sent 2 of their members from Rinburg to Aslain to get news when there was little news of the north in Rinburg
from game intro:
- The Ferrystones, a dwarven clan, a group of whom are staying at the Resting Ox. They are important in Rinburg, and might have some useful information to share (and see Bolgrim and Kazak above)

Prominent enough that a clan member was brought in during an investigation into a ruined temple for their expertise in ruins
%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
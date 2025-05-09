---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: the}
campaignInfo: []
name: Gemcrafters
typeOf: clan
ancestry: dwarven
aliases: [Barzinduk]
whereabouts: Nidzahar
dm_notes: none
dm_owner: mike
---
# The Gemcrafters
>[!info]+ Information
> A [[Dwarves|dwarven]] clan
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

*in dwarvish, Barzinduk*

A wealthy merchant clan in [[Nidzahar]]. Their wealth largely dates from just after the Great War, as the family was relatively unscathed by those events.

%% 
The family made a deal of sorts with the [[Bahrazel]] during the Great War, for protection, and one of the family [[Izgil Moonseeker|Izgil]] has been claimed by the Bahrazel for mysterious purposes.
%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
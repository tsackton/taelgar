---
headerVersion: 2023.11.25
tags: [status/cleanup/text, group]
displayDefaults: {defArt: 'the'}
typeOf: family
ancestry: Sembaran
typeOfAlias: yeoman family
whereabouts: Cleenseau
dm_owner: none
dm_notes: none
---
# The Thornes of Cleenseau
>[!info]+ Information  
> A [[Sembara|Sembaran]] yeoman family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% The Thornes in the Cleenseau region have come up several times in various Cleenseau sessions as semi-prominent yeoman, sturdy, good allies to the PCs. I don't have any details made up but the family should have a "the Cottons in the Shire" vibe.  Not wealthy, but definitely hold some land themselves, likely at least partly [[Land Holding in Sembara|freehold]] %%

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
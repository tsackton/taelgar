---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {partOf: "", boxInfo: "", defArt: "the"}
typeOf: family
whereabouts: Cleenseau
aliases: [Essford]
dm_notes: none
dm_owner: mike
---
# The Essfords
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A minor landholding family in the [[Enst|Enst River Valley]]. The founder of the family, [[Reginald Essford]], came to prominence during the [[Third Hobgoblin War (Sembara)|hobgoblin wars]] for valor in battle as a member of [[Cece I|Cece I's]] [[Radiant Alliance]]. The Essfords have been well-loved in the [[Cleenseau Region]] for several generations now.

%% Some notes in [[Cleenseau History Notes]] and [[Reginald Essford]] and [[Wymar Essford]] %%

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

%%^Campaign:None%%
### Historical Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%
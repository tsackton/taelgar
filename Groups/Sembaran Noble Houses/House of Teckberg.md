---
headerVersion: 2023.11.25
tags: [organization]
typeOf: family
typeOfAlias: noble family
whereabouts: Sembara
dm_notes: none
dm_owner: none
---
# The House of Teckberg
>[!info]+ Information  
> A noble family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A cadet branch of the [[House of Sewick]]. 

%% Nothing canonically made up other than the family tree. Available to be used as a powerful noble family in Sembara %%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%
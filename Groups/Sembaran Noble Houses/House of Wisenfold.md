---
headerVersion: 2023.11.25
tags: [organization, status/check/mike]
typeOf: family
dm_notes: none
dm_owner: none
---
# The House of Wisenfold
>[!info]+ Information  
> A family  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% anything to add? %%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%
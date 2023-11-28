---
tags: [organization, status/notes, status/unknown]
displayDefaults: {defArt: ''}
name: The Cleansed
typeOf: cult
---

# The Cleansed

A mysterious secret society in [[Chardon]] of which [[Fausto]] is a member and seem to be dedicated in some way to Drankorian purity. 

%%SECRET[1]%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
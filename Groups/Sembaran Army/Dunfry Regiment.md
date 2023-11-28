---
headerVersion: 2023.11.20
displayDefaults: {partOf: '<typeof:A> of <partof>', boxInfo: ''}
tags: [organization, status/unknown]
typeOf: regiment
partOf: Army of the West
---
# The Dunfry Regiment
>[!info]+ Information
> a regiment of the [[Army of the West]], the [[Sembaran Army]], [[Sembara]]

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
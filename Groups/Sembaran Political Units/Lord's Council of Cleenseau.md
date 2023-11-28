---
tags: [organization, status/unknown]
displayDefaults: {startStatus: founded, startPrefix: founded, endPrefix: destroyed, endStatus: destroyed}
campaignInfo: []
name: Lord's Council of Cleenseau
typeOf: council
partOf: Cleenseau
---

The Lord's Council is an advisory group to the lord of [[Cleenseau]], currently [[Rosalind Essford]] for all practical purposes. 

It is advisory, but Rosalind convenes it before important decisions and respects the advice she receives. It consists of:

* [[Marigold Stonebridge]], the owner of [[The Crossroads Inn]], as an observer in the tradition of the Sembaran Royal Council
* [[Jonathon Henwyn]], the steward
* [[Ames Benthey]], the captain of the household guard 
* [[Annet Bybet]], the chamberlain
* [[Anselm]], the administrator of the Temple of the Warlord

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
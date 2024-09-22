---
tags: [organization, status/needswork/wip, status/tim, status/cleanup/header]
displayDefaults: {defArt: ""}
campaignInfo:
name:
typeOf: army
subTypeOf: warband
whereabouts: 
- {type: home, location: Eastern Dunmar}
- {type: away, start: 1748-09-30, end: 1748-12-13, prefix: camped, location: plains north of Tokra}
- {type: away, start: 1748-12-14, end: 1748-12-18, location: Tokra}
- {type: away, start: 1748-12-19, end: 1748-12-27, location: riding to Songara}
- {type: away, start: 1748-12-27, location: Songara}
---

%% fill in whereabouts %%
%% Tim: set a bunch of status flags; not sure how much info you have about these %%
# Havdar's Warband

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
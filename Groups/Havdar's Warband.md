---
headerVersion: 2023.11.25
tags: [organization, status/needswork/wip, status/check/tim, status/metadata/header]
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
# Havdar's Warband
>[!info]+ Information  
> A warband army  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


%% fill in whereabouts %%
%% Tim: set a bunch of status flags; not sure how much info you have about these %%

%%SECRET
Group of 30-40 Dunmari warriors that ride under [[Havdar]]'s command. Function like a household guard for [[Karawa]] and the eastern plains.

Recruited largely after the first gnoll attack on [[Bas Udda]], from a much smaller nucleus that rode with [[Havdar]] to protect the first refugees heading north to [[Karawa]].

Rode to [[Tokra]] guarding [[Karawa]] evacuation, then returned to [[Karawa]] to find [[Centaurs]] and gnolls.

Helped defeat gnoll remnants with [[Centaurs]], then established guard of [[Karawa]].

After learning from [[Alesh]] about [[Orcs]] and other things on the eastern plains, they headed out to investigate and fight. Fought off a band of 40 [[Orcs]] with some causalities, found nothing else west of the [[Kharja]] river, returned to [[Karawa]].

Now sworn into Nayan [[Sura]]'s service.

%%

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
---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: the}
campaignInfo: []
name: Charmhearts
aliases: [Charmheart]
typeOf: family
ancestry: halfling
dm_notes: color
dm_owner: tim
---
# The Charmhearts
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Charmhearts are a prominent family of [[Halflings|halfling]] overland traders. They trace their history to [[Sembara]], but for the past several generations they have made their living on long distance trade, bringing spices, furs, and dyed cloth from [[Sembara]] to [[Dunmar]], as well as sometimes apple brandy from [[Adderfell]]. 

Their traditional route brings them across the lower elevation eastern passes across the [[Sentinel Range]] on the road to [[Karawa]], often crossing as early as the middle of March, aiming to arrive in [[Karawa]] in time to trade at the [[Festival of Rebirth]], usually in early April. After a year circuiting [[Dunmar]], they return to [[Sembara]] via the high passes from [[Tokra]] in late spring when the snows melt. 

They are a serious trading family, and always travel prepared for danger, especially across the passes and the open frontier north of [[Karawa]]. 

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

%%^Date:1748%%
In 1748, the Charmhearts encountered trouble on the road from [[Ausson's Crossing]] to [[Karawa]]. Descending the passes on March 19, 1748, the Charmheart caravan stopped to rest and recover after the hard journey, at a well-used campsite near the old Dunmari fortress called Raven's Hold. [[Ander Charmheart]], a young and sometimes foolish member of the clan, went exploring, and was caught in a wave of demonic energy from a demon summoning. Driven mad, the Charmheart caravan was forced to deal with the situation in [[Karawa]]. 

The demon at Raven's Hold was later killed by [[Dunmar Fellowship]], but [[Ander Charmheart]] only slowly and partially recovered. What is more, during this time, gnoll raiders rampaged across [[Eastern Dunmar]], and little trading was possible. The Charmhearts made their way to [[Tokra]] with crowds of Dunmari refugees, but the sickness and war seriously disrupted their trading year, causing significant losses. Later, they left [[Tokra]] for [[Darba]], hoping for better luck. 
## Chronology
- (DR:: 1748-03-19): [[Ander Charmheart]] caught in wave of demonic corruption near [[Raven's Hold]]. 
- (DR:: 1748-03-28): Charmhearts arrive in [[Karawa]]
- (DR:: 1748-03-29): Meet [[Dunmar Fellowship]] in [[Karawa]] in the evening
- (DR:: 1748-04-13): Charmhearts reach [[Tokra]] with Dunmari refugees
- (DR:: 1748-06-30): Meet [[Wellby]] in [[Tokra]], receive gifts from him to help get them on their feet again. Introduced to [[Garret Tealeaf]]. 
- (DR:: 1748-07-18):  [[Garret Tealeaf]] and the Charmhearts leave [[Tokra]], planning on heading to [[Darba]] with trade goods and reconnecting with the Tealeafs, if possible.
- (DR:: 1748-08-13): Charmhearts and [[Garret Tealeaf]] arrive in [[Darba]].
%%^End%%

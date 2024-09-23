---
tags: [status/metadata/header, organization, status/cleanup/internal]
displayDefaults: {defArt: "the" }
dm_notes: none
dm_plans: yes
---

%% The merriweather family is an important halfling trading family in Aveil, especially plying the route along the [[Auberonne]] between Asalin and Rinburg. 

The family was involved in the exile of the old baron of aveil. (Reginald Rusebek) in that they found out about his embezzlement and he killed them to try to cover it up. It was the murder of several important halflings that led to his execution and his family scattering mostly volunteerly.

It is possible but not decided that this was all faked by the lich. If faked, the halflings did not know it was faked and are innocent dupes. Either way, they are, in 1720, reeling from a recent tragedy that killed 6-10 elders of the family, basically. 

From game intro:
- The Merriweather's, a halfling family in the area, who are apparently the family the old lord killed (Reginald Rusebek) to cover up his embezzlement. Fin (mentioned above) is one of them


%%

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
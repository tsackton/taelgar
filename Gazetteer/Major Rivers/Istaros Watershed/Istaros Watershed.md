---
headerVersion: 2023.11.25
tags: [place, status/stub, status/check/ai]
name: Istaros Watershed
typeOf: watershed
whereabouts:
- { type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: color
---
# The Istaros Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Istaros watershed is the vast river basin that gathers into the [[Istaros]] and its many tributaries, stretching from the [[Mostreve Hills]] to the [[Sea of Storms]]. For much of recorded history it has been a fertile crossroads, central first to the [[Drankorian Empire]] and later to realms that rose in the shadow of Drankor’s fall.

In the modern day, much of the watershed is defined by the scars of the [[First Plague]] and the [[Great War]]. Large stretches of the river system flow through the [[Desolation of Cha'mutte]] and the [[Plaguelands]], and the ruined city of [[Isingue]] lies near one of the watershed’s most storied confluences.

## Geography

The headwaters of the Istaros lie at [[Lake Aeulian]], fed by the [[Andonne]] and the [[Valmont]]. Downstream, the river is joined by major tributaries including the [[Thalurien|Thalúrien]] from the east and the [[Yandare|Yandarë]] from the mountains beyond [[Xurkhaz]].

## History

By the early centuries of the Drankorian reckoning, Drankor’s influence had spread along the entire river system, and the Istaros valley became one of the Empire’s great settled heartlands. After the fall of Drankor, the watershed remained a route of travel and settlement—until the wars and plagues of the Blood Years and the Great War left much of the interior cursed and abandoned.

%% AI note: Expanded from existing vault sources: [[Istaros]], [[Upper Istaros]], [[Desolation of Cha'mutte]], [[History of the Drankorian Empire]]. %%


%%^Campaign:None%%
### Places in the Istaros Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

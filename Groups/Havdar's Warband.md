---
headerVersion: 2023.11.25
tags: [group, status/cleanup/metadata]
displayDefaults: {defArt: ""}
typeOf: army
ancestry: Dunmari
typeOfAlias: warband
whereabouts: 
- {type: home, location: Eastern Dunmar, end: 1748}
- {type: home, location: Tokra, start: 1749}
- {type: away, start: 1748-09-30, end: 1748-12-13, prefix: camped, location: plains north of Tokra}
- {type: away, start: 1748-12-14, end: 1748-12-18, location: Tokra}
- {type: away, start: 1748-12-19, end: 1748-12-27, location: riding to Songara}
- {type: away, start: 1748-12-27, location: Songara}
dm_notes: none
dm_owner: tim
---
# Havdar's Warband
>[!info]+ Information  
> A [[Dunmar|Dunmari]] warband  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% metadata still needs a little cleanup w/r/t Siblings War, etc %%

Havdar’s Warband is the informal name for the group of about 30-40 Dunmari soldiers and riders who travel under the command of [[Havdar]], a prominent Dunmari soldier. In the early DR 1740s, this group was largely based out of [[Karawa]] and the surrounding area, functioning as a close knit group of riders and warriors handling threats on the border. During the [[Summer Gnoll Raids of 1748]], this group was extremely active in protecting the people of [[Eastern Dunmar]], and made a name for themselves.  

[[Havdar]] was an early supporter of [[Sura|Nayan Sura]] upon [[Session 31 (DuFr)|her return from magical imprisonment in DR 1748]], and over the course of the next two years grew to be one of her most trusted military commanders. During this time, Havdar's Warband grew into her elite guard, now based out of [[Tokra]]. 

## Notable members

- [[Aram]], a holy warrior of [[Aagir]] and the warband’s unofficial spiritual leader
- [[Camana]] (deceased), a warrior and scout associated with Havdar’s riders


%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

## DM Notes

Very loosely modeled on the group of soldiers that travels with Uhtred in the Last Kingdom (Netflix show)

Basic history:

- Group of 30-40 Dunmari warriors that ride under [[Havdar]]'s command. Function like a household guard for [[Karawa]] and the eastern plains.
- Expanded after the first gnoll attack on [[Bas Udda]], from a smaller nucleus that rode with [[Havdar]], to protect the first refugees heading north to [[Karawa]]. Rode to [[Tokra]] guarding [[Karawa]] evacuation, then returned to [[Karawa]] to find [[Centaurs]] and gnolls.
- Helped defeat gnoll remnants with [[Centaurs]], then established guard of [[Karawa]].
- After learning from [[Alesh]] about [[Orcs]] and other things on the eastern plains, they headed out to investigate and fight. Fought off a band of 40 [[Orcs]] with some causalities, found nothing else west of the [[Kharja]] river, returned to [[Karawa]]. Dunmar Fellowship traveled with them for some of this journey. 
- Havdar was early supporter of Sura, and his warband was sworn into her service almost immediately. 
- Over the course of the [[Sibling War]] grew into an elite household guard for Sura.

%%^End%%

---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {partOf: ""}
created: 843 
typeOf: clan
ancestry: orc
name: People of the Rainbow
whereabouts: 
- {type: home, end: 940, location: Amberglow} #end is +/- 10 years
- {type: home, start: 940, end: 1050, location: unknown} #start +/- 10 years
- {type: home, start: 1051, end: 1582, location: wandering and hiding}
- {type: home, start: 1583, location: Xurkhaz}
dm_notes: important
dm_owner: tim
---
# The People of the Rainbow
>[!info]+ Information
> An [[Orcs|orc]] clan
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The name for the [[Orcs]] of [[Xurkhaz]] who have lived free from [[Thark]]'s curse for many generations.
## History

The People of the Rainbow trace their origins to the Golden Age of the [[Drankorian Empire]], when their ancestors were freed from [[Thark]]'s chains by the gift of an archfey known as the [[Cloudspinner]]. In those days, the People of the Rainbow grew and prospered in the [[Feywild]] domain of [[Amberglow]], under the [[Cloudspinner]]'s protection, and safe from [[Thark]]'s reach. 

As they grew, the People of the Rainbow wished to free their brethren from [[Thark]]'s chains, so with the [[Cloudspinner]]'s blessing and the gift of the [[Cloak of Rainbows|Cloak of Rainbows]] to protect them, they ventured back to the material plane. 

However, rumors of the unchained [[Orcs]] and the [[Cloak of Rainbows|Cloak of Rainbows]] and its power grew in [[Drankorian Empire|Drankor]], and eventually attracted the attention of [[Apollyon|Apollyon]], the emperor, who attacked the People of the Rainbow, and stole the [[Cloak of Rainbows|Cloak of Rainbows]] for himself. 

For the next five hundred years, the People of the Rainbow lived a hunted existence, scattered in small groups trying to avoid the ever-watchful eyes of [[Thark]] and the violence of his servants. Until after the [[Great War]], when [[Uzgash]], the leader of a small tribe of orcs hiding in the [[Nashtkar]], discovered the long-lost [[Cloak of Rainbows|Cloak of Rainbows]] in a ruined Dunmari fort. Using the power of the cloak, he founded the kingdom of [[Xurkhaz]]. The People of the Rainbow have lived in [[Xurkhaz]] ever since, under the protection of the [[Cloak of Rainbows|Cloak of Rainbows]]. Over the years, as rumors of [[Xurkhaz]] spread, lost tribes of the People of the Rainbow hiding in distant places have begun to return when they can. 

Now, the People of the Rainbow are thriving in [[Xurkhaz]], and perhaps in other hidden pockets of the world. 
### Events
- (DR:: 917): [[Cloak of Rainbows]] is gifted to the People of the Rainbow by [[Cloudspinner]]
- (DR:: 930)-(DR_end:: 950): People of the Rainbow begin to drift out of the feywild, seeking to free their chained brethren
- (DR:: 1050): [[Apollyon]] attacked the People of the Rainbow and the [[Cloak of Rainbows|Cloak of Rainbows]] was lost.
- (DR:: 1582): [[Uzgash]] finds the [[Cloak of Rainbows|Cloak of Rainbows]] in a Dunmari fort in the [[Nashtkar]]
- (DR:: 1583): [[Xurkhaz]] is founded as the new homeland of the People of the Rainbow. 

%%SECRET[1]%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
---
headerVersion: 2023.11.25
excludePublish: ["clee"]
tags: [item]
typeOf: skyship
pronunciation: vin-dree-SHAR-na
displayDefaults: {linkText: on, ltItem: stored on}
whereabouts:
- {type: home, location: unknown storm giant}
- {type: home, location: dufr}
- {type: away, start: 1748-12-03, end: 1748-12-10, location: Uzgukhar}
- {type: away, start: 1748-12-28, end: 1749-01-04, location: Tollen} #check
- {type: away, start: 1749-01-15, end: 1749-01-16, location: Orenlas}
- {type: away, start: 1749-01-17, end: 1749-01-19, location: traveling to Xurkhaz}
- {type: away, start: 1749-01-20, end: 1749-01-24, location: Uzgukhar}
- {type: away, start: 1749-01-25, end: 1749-01-30, location: Nashtkar} #add session 90 travel
- {type: away, start: 1749-03-13, end: 1749-03-16, location: Vostok}
- {type: away, start: 1749-03-17, end: 1749-03-18, location: Sivnjo Mountains} #add travel
- {type: away, start: 1749-05-30, end: 9999, location: Garamjala Desert}
- {type: away, start: 1749-06-14, end: 9999, location: Gulf of Chardon}
rarity: unique
typeOfAlias: skyship
aliases: [Star on the Wind]
subTypeOf: magical
dm_owner: tim
dm_notes: important
---
# Vindristjarna
*(vin-dree-SHAR-na)*
>[!info]+ Information  
> (unique magical skyship)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[vindristjarna-v1.jpg]]

## History

Eons ago, lost in the dawn of time when the Firstborn walked the earth and the great empires of giants and dragons and other creatures of myth and legend  stretched across the world, great skyships of the storm giants sailed the skies. While a few may remain in distant hidden corners of the world, or travel the skies of other planes, many crashed or were destroyed.

One such skyship, the Star on the Wind, Vindristjarna (vin-dree-shar-na), crashed on what is now the Dunmari plains thousands of years ago. 

The ancient skyships of the storm giants are powered by [[Phasing Stones]], that connect to the dreamworld and allow one to imagine and project different physics, physics where stone can float. 

While the phasing stone that originally powered Vindristjarna is mostly destroyed, the ship is otherwise intact and could be made to fly with a new phasing stone. 

## Recovery and Repair

The [[Dunmar Fellowship]] restored Vindristjarna in the course of [[Session 74 (DuFr)|their adventures]], replacing the ruined phasing stone with a new one, [[Session 73 (DuFr)|recovered from Hralgar's ancient mountain home]]. 

Currently, the hull of the ship has been restored and repaired, and two stone decks constructed, creating three floors: a storage hold that is currently mostly unimproved, a lower deck, and an upper deck. 

The upper deck, occupying a total of 12,000 square feet (480 squares), is dominated by a large central courtyard, greenhouse, and garden, maintained by Kenzo. Around the railing of the upper deck is also a depiction of the travels of [[Dunmar Fellowship]], and especially the stories of the people they have met, recalling the [[Hall of Stories]] in the [[Monastery of Bhishma]]. 

Also constructed are a well-equipped galley and kitchen, a dining hall, a map room maintained by Wellby, a workshop and a games room maintained by Seeker and providing space for Faldrak to work, a sanctuary of the tanshi maintained by Delwath, and comfortable living quarters for ten hirelings or followers, as well as cabins for Riswynn, Delwath, Seeker, Kenzo, and Wellby, and a guest suite. 

## Mechanics

More detail about the mechanical effects of Vindristjarna can be found here:
- [[Vindristjarna Mechanics]]
- [[Vindristjarna Bastion Rules]]

%%^Campaign:none%%

*I don't think this will translate to mkdocs?*
## People

People currently on Vindristjarna, including those trapped in the [[Mirror of Soul Trapping]], are listed below. 

### On Vindristjarna
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation("Vindristjarna", f.file.frontmatter, dv.current().pageTargetDate))
				.where(f => !util.inOrHomeLocation("Mirror of Soul Trapping", f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> <pronunciation> (<pronouns>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

### In the Mirror
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation("Mirror of Soul Trapping", f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> <pronunciation> (<pronouns>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
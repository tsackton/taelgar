---
headerVersion: 2023.11.25
tags: [place, status/cleanup/text]
name: Darba
typeOf: city
whereabouts: Coastal Dunmar
dm_notes: important
dm_owner: tim
---
# Darba
>[!info]+ Information
> A city in [[Western Dunmar]], [[Dunmar]], the [[Greater Dunmar]]

%%needs some basic cleanup, plus collating various notes in Obsidian and OneNote%%

Darba is a walled city set on the rocky coast, perched above the flooded swamps of the Rudhan river. From a distance, the white walls of the old Drankorian fort that guards the harbor gleam in the sun, its six towers commanding a wide view across the bustling city. The old trade road follows the height of land north of the river, avoiding the flooded swamps of the delta in monsoon, approaching the old gates of the city, the ancient Drankorian wrought iron motifs of confronted lions framing the gate and visible even from a distance.

To the south of the walls, across the estuary, a shanty town of wooden dwellings and flooded, muddy streets stretches inland for some distance. Now, in the monsoon flood, small boats ply their trade back and forth along the river, many distinctive high-prowed Illorian poled boats. In the sheltered estuary, the masts of tall sailing ships can just be seen dancing on the waves at dock. Three and four masted, square rigged Chardonian trading caravels, small and fast Illorian lanteen-rigged ships, and the occasional junk-rigged sailing ship with unusual stiff sails from farther afield. The Dunmari are not know as shipbuilders, but the occasional single-masted Dunmari longship patrols the waters.

To the north, the waves lap against the sea wall, a thin beach of sand and rock exposed at low tide. A few distant ships ride at anchor here, and small fishing boats heading out to sea are a common sight.

A steady flow of traffic - dwarves with iron wares to trade, merchant caravans loaded with exotic goods heading south to [[Nayahar]], halfling traders taking goods overland to [[Songara]], lumber and food moving in and out of the city.

The land along the river is marshy and not much settled, but the floodplains are fertile farmland and you pass many communal pastures and fields, and the occasional small village, although even here the population is restless and many dwellings are not permanent.

The north bank is less marshy than the south, and there are several weirs and water mills that dot the landscape just inland of Darba, helping fuel in the industry of the city.

## History

- (DR:: 377): A Drankorian fort, to provide naval defenses for the western frontier of the Empire, is constructed at the mouth of the Rudhan river, in the location that will eventually grow to become the city of Darba. 
- (DR:: 1552): An Illorian captain, Chirce, claims sovreignity over Darba and the surrouding coastal plain
- (DR:: 1558): The Samraat Nayan Kundar drives the Illorian from Darba and reclaims the city 
- (DR:: 1644): A massive new public market is constructed in Darba by dwarven craftsfolk, commissioned by the Samraat to reflect the growing importance of Darba as a center of trade

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

%%SECRET[1]%%


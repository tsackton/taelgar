---
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [background, status/check/ai, status/check/lint]
name: The World of Taelgar
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

%% See [[Geography - Open Questions]] for some unresolved general questions about the world %%

The world of Taelgar is a globe, slightly bigger than Earth, with Earth-like seasons and climate and an Earth-like sun, [[Moon]], and [[Stars|stars]]. The main landmass stretches from the [[Endless Ocean]] in the west across more than 5,000 miles of mountains, forests, rivers, swamps, farmland, desolation and deserts to the mysterious [[Outer Ocean|east]].

Many mapmakers consider the mighty [[Sentinel Range]], whose highest peaks rise more than 20,000 feet into the air, the defining feature of the land. The [[Sentinel Range|Sentinel's]] 2,500 miles of mountains and foothills divide the world into three: 
* to the west, [[Chardon]], the great city of magic and learning, by the mouth of the mighty [[Chasa-Nahadi Watershed]], and the smaller [[Yeraad Watershed|Yeraad River]], to the south
* to the south, the great [[Hara Basin]], arid and windswept, cut off from the [[Nevos Sea]] by the [[Yuvanti Mountains]]
* to the east, the [[Greater Sembara|realms of Sembara, Tyrwingha, and Vostok]] on the shores of the [[Western Gulf]] of the [[Green Sea]]

The halflings navigating the [[Green Sea]] would tell a different tale, as they sailed the 3,000 miles of rugged coasts, mysterious islands, and northern forests. They would talk of the [[Northern Green Sea|northern forests]], the mysterious island of [[Irrla]], the volcanic [[Skaerhem]], and the [[Cymean Peninsula]], steeped in history. They would tell you that the familiar lands of [[Greater Sembara|Sembara and Tollen]] are just the beginning of a never-ending road, running through the waves and currents of the [[Green Sea]].

If you were lucky enough to find an ancient map from [[Drankorian Empire|Drankor]], the ruined and haunted center of a once-mighty empire, it would show you that the [[Istaros]], flowing for nearly 2,000 miles from the [[Mostreve Hills]] to the shores of the [[Sea of Storms]], was the lifeblood of fortune and empire. Today though, the river runs only through the fallen city of [[Isingue]], and many other places that were once fertile and beautiful, that are now cursed by [[Plaguelands|plague]] and [[Desolation of Cha'mutte|desolation]].

%%^Campaign:none%%
### Oceans and Boundaries
The known world is bounded by the [[Endless Ocean]] in the west and the [[Outer Ocean]] in the east. The lands to the north and south are intentionally vague and mysterious, to preserve blank spaces on the map for future adventures.
### Major Regions
To ease worldbuilding, Taelgar is divided up into 15 regions, listed approximately from northwest-southeast:

1. the [[Northwest Coast]], in the far northwest, home to the [[Mawakel Peninsula]]
2.  [[Greater Chardon]], home to the city of [[Chardon]] and much of its vast [[Chardonian Empire|empire]]
3.  [[Nevos and Apporia]], home to the islands of [[Illoria]] and the mysterious [[Apporia|Apporian Peninsula]]
4. the [[Northern Sentinels]], once the realm of [[Pandar]], homeland of [[Cha'mutte]], now a dangerous place with few permanent settlements
5. the [[Central Highlands]], home to the [[Sentinel Range]] and the great forests of [[Ainumarya]] and the [[Elderwood]]
6. [[Greater Dunmar]], the land of the [[Dunmar|Dunmari]], changed significantly since the [[Great War]]
7.  [[Greater Sembara]], the place of the old and stable realms of [[Sembara]] and [[Tyrwingha]], as well as the rivers and forests of [[Vostok]] and the famous port and trading city, the [[Tollen|Free City of Tollen]]
8. the [[Upper Istaros]], dominated by the [[Istaros]], once [[Isingue|rich farmlands]], now mostly cursed [[Plaguelands]] full of ash and danger, but with scattered [[Refounded Alliance of Aurbez|human]], [[Xurkhaz|orc]], and [[Orenlas|elf]] communities on the edges
9. the [[Drankorian Hinterland]], once the heartland of the [[Drankorian Empire]], now a place of [[Desolation of Cha'mutte|desolation]] and danger
10. the [[Northern Green Sea]], dominated by mighty northern forests, and home to the mysterious land of [[Ursk]]
11. the [[Western Green Sea]], where the [[Skaerhem|Skaer Islands]] are, as well as the [[Cymean Peninsula]] and other descendant civilizations of Drankor

```taelgar-map 
id: region-map-taelgar
image: [[world-map-regions-new.png]] 
bounds: 
- [0,0]
- [5156.7, 6636.233]
height: 600px  
lat: 3333
long: 3000
minZoom: -3
maxZoom: 2
defaultZoom: -2
unit: miles 
scale: 1
calibration:
  hexMiles: 24
  hexPixels: 20.166666666666668
  imageSize: [7200, 4536]
  imageSha256: 0240203fcb6588b34c4d4799e0af63a98f78c0b4c623efaa5444745923f07867
draw: false
darkMode: false
markerTag: location-source
```

Finally, there are four mostly uncharted regions, with little factual information:
12. the vast [[Eastern Green Sea]]
13. and the [[Great Desert|deserts]] and [[Orekatu|jungles]] of the [[Far South]]
14.  the islands and underwater civilizations of the [[Western Ocean|western Endless Ocean]]
15. the frozen [[Far North]]

### Major Features
A handful of major features are large, and cross regions. These are:
##### Mountain Ranges
* the [[Sentinel Range]]
##### Seas and Oceans
* the [[Green Sea]]
* the [[Endless Ocean]]
* the [[Outer Ocean]]
* the [[Nevos Sea]]
##### River Systems
- the [[Chasa-Nahadi Watershed]]
- the [[Istaros Watershed]]
- the [[Yeraad Watershed]]
##### Peninsulas and Islands
* the [[Apporia|Apporian Peninsula]]

%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography after the Great War, with older Drankorian maps and maritime traditions as historical context.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added a broadly modern POV and temporal-coverage interpretation.
- Corrected “am Earth-like” to “an Earth-like,” removed the duplicated “the,” supplied the article in “a never-ending road,” corrected “a ancient” to “an ancient,” and supplied the missing article in “now a dangerous place.”
- Corrected the private region inventory’s summary count from 13 to 15 to match its numbered entries; normalized the existing private-block marker from Campaign:None to Campaign:none without changing its payload or placement.

### Validated judgments
- This is a geographic overview rather than a name-bearing entity article, so no name block is needed. Its maritime and historical framing is intentional reference prose, not a style defect.
- The existing status/check/ai is preserved as independent human-review state. The source-pointer comment and the private regional inventory were reviewed; the latter retains its distinct worldbuilding and navigation purpose.

### Open findings

- [ ] **Warning — correctness.source_conflict:** The last public paragraph says the Istaros “runs only through the fallen city of [[Isingue]], and many other places ... now cursed,” which reads as if its whole course passes only ruined or cursed lands. [[Istaros#Middle Istaros|Istaros]] explicitly describes the inhabited river valley around [[Uzgukhar]] as one of the most densely settled parts of [[Xurkhaz]]. Qualify the overstatement while preserving the contrast with the old empire. Candidate replacement for the final sentence: “Today, much of its former imperial heartland around [[Isingue]] and [[Drankor]] is cursed by [[Plaguelands|plague]] and [[Desolation of Cha'mutte|desolation]], although the river also passes settled lands such as [[Xurkhaz]].” Keep the existing link to the river’s source and its historical importance; the whole river is not an abandoned landscape.

### DM evidence
- [[_DM_/Brainstorming/Misc Random Ideas]]
%%^End%%

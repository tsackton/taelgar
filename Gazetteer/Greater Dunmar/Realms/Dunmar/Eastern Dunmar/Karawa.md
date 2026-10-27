---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
typeOfAlias: town
mapLocation: { x: 5607.5, y: 6913.5, hex: 15.09.H.22/2350, importance: local, symbol: square }
name: Karawa
whereabouts: Eastern Dunmar
dm_owner: tim
dm_notes: important
POV: 1748
---
# Karawa
>[!info]+ Information
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%reorganize into a cleaner format%%

%% OneNote dumps here: [[Karawa - Design Note]] %%

A small Dunmari village. Houses of adobe / mud brick, except a few bigger or more important ones of sandstone. Colors browns and some ochre. Lots of awnings of variously colored cloth, lots of horses and goats. Much of the town was destroyed in gnoll attacks in the summer of 1748, but is in the process of being rebuilt. 
#### Locations

[[Temple of Shakun]]: one of the few buildings not destroyed during the gnoll attacks; set into the mesa itself.

[[Red Mesa]]: a massive red stone flat-topped mesa that looms over the village. 

[[Ikram's|The caravanserai]]: Largely destroyed in the gnoll attacks. A new caravanserai is under construction, larger and better fortified. 

The Oasis: The central feature of the town is a small oasis. Over the years a marble pool and short wall have been built around it, allowing water to be drawn off for various uses. The reliability and purity of the water here has established Karawa as a waypoint and gathering place for the Dunmari. Palm trees provide shade and shelter and make the oasis square a place where people linger. Fouled by gnolls, but now clear again. There has always been a holy spring here, a place that people said could show you glimpses of dreams and faraway visions of possible futures, guarded and protected by a small Mystery Cult dedicated to [[Shakun]].

The market square: On the northwestern edge of town, there is a large market square, which stands empty most of the year, filling to capacity only during the large markets after the [[Festival of Rebirth]], at least this is what you've been told. Beyond it, cleared scrublands and pastures serve as a temporary home for hundreds of herders who return for the [[Festival of Rebirth]], or so you've heard.

The Temple of [[Dunmari Religion]]: Although the [[Temple of Shakun]] is the larger draw in Karawa, a small temple to [[Dunmari Religion]] stands on the eastern side of town, facing a small public square. The temple itself is plain, but well-maintained. Damaged, but not destroyed, in the gnoll attacks, and has been rebuilt. 

The Council of Elders: Standing across a small public square from the Temple of [[Dunmari Religion]] is a circular, dome shaped building that is the main public building in Karawa. This space serves as the council chambers where the council of elders meets to deliberate, and the square in front is a place for public debate. Judgements are issued here by the council.

The village: The village itself is mostly small houses of adobe and mud, facing on narrow streets, with shade provided by colorful awnings. A few artisans and scattered shops line the streets facing the caravanserai, including a tea house which [[Delwath]] once lived above, and a blacksmith. Most of the small houses were burned and destroyed in the gnoll attacks, but many have been cleaned and are being rebuilt. 

The fields: To the southeast of town, some small scale agriculture provides a bit of extra food, beyond what the herds can provide and what can be traded with pastoralists passing through. Crops that require little water and lots of heat do best, although the oasis feeds irrigation channels here that allow crops to thrive. Dates and honey are a particular delicacy, being used to make wine and desserts.

![[karawa-map.png]]

%%SECRET[v2:0a7681f2297a60055c1b91ebc2cd3463]%%

%%^Metadata:names:v1%%
- {"name": "Karawa", "language": "unknown", "pronunciation": "kuh-RAH-wah", "notes": "Proposed Hindi-oriented reading from the Dunmari cultural context and [[Languages]]: reduced initial a, a tapped r, open ah vowels, and w near the v/w sound; penultimate prominence and vowel lengths are unconfirmed. The name language is not explicitly established.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a rebuilding-era DR 1748 snapshot after the gnoll attacks, with remnants of the pre-attack oasis description; completion of the new caravanserai in January DR 1749 is not incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and list formatting without changing the header version, classification, cleanup status, or human DM attestations.
- Corrected subject–verb agreement in “a marble pool and short wall have been built” and “irrigation channels here that allow crops to thrive” in the visible article.
- Added a persistent proposed name pronunciation, a typed settlement map entry with an unknown locator, and `POV: 1748` with the article's temporal limits.

### Validated judgments
- `status/cleanup/text` is supported by the author's reorganization reminder and the fragmentary opening description; the tag is preserved.
- “Summer of 1748” is compatible with the April attacks: [[Dunmari Festivals]] places Dunmari summer between the Festival of Rebirth and the Feast of Bhishma.
- Confirmed local evidence supports the positive `dm_notes: important` attestation. The SECRET block was reviewed; its contents and any recovery candidate remain outside this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `kuh-RAH-wah` for Karawa. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue; the proposal favors Hindi-style k, a tapped r, a v/w-like consonant, a reduced first a, and open ah vowels. Penultimate prominence is a reading aid, while a Persian-oriented final prominence is an alternative. The name's language, vowel lengths, and stress are not explicitly established. Accept or revise the proposal, then copy the accepted pronunciation to frontmatter and mark the entry `documented`.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has a blank `locator`. Supply Karawa's verified world-map coordinate in the existing `{map: world, locator: }` entry; the embedded village plan does not establish a world-map hex.
- [ ] **Warning — temporal.mixed_viewpoints:** The Oasis says “Palm trees provide shade and shelter,” while the rest of the article describes rebuilding after the attacks. [[Session 17 (DuFr)]] records the oasis shade trees chopped down or burned, and [[Scrying Delwath Oct 26]] shows new date palms only beginning to grow in late DR 1748. Clarify the pre-attack and rebuilding states. Copy-ready replacement for that sentence: “Before the gnoll attacks, palms shaded the oasis square. By late DR 1748, new date palms were beginning to grow after the burned trees had been cleared.” No visibility-changing block was applied.
- [ ] **Warning — coverage.later_material_change:** The caravanserai entry still says a new building “is under construction.” [[Ikram's#Events|Ikram's dated events]] records its completion on January 11th, DR 1749; [[Scrying Delwath Oct 26]] corroborates construction during the article's DR 1748 rebuilding phase. Decide whether to update the account and POV, defer with `status/gameupdate/dufr`, or intentionally retain the DR 1748 snapshot. If updating, the bounded replacement is: “[[Ikram's|The caravanserai]] was largely destroyed in the gnoll attacks. A larger, better-fortified replacement was completed on January 11th, DR 1749.” Alternatively, retain the existing reconstruction account and propose the dated completion as a separate layer: `%%^Date:1749-01-11%%` followed by “The new [[Ikram's|caravanserai]] is complete.” and `%%^End%%`; a human must authorize that visibility change. No game-update tag or Date block was changed automatically.

### DM evidence
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Meta/Map Notes]]
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Secret Worldbuilding/Mulitverse]]
- [[_DM_/Staging/NPC Ideas - Unused]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Candrosa (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Cintra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Bookkeeping]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Backstory developments]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Bas Udda (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Havdar's Band]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Session 19]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival of Rebirth (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Individual Scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 5 scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 6 scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Situation in Karawa After Raven's Hold]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/The Situation in the South]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 12]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 8]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 9]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Distances and Travel Time]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Journey North]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Session 7]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Tower/Session 14]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Character Intros]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Clues in Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Into the Wild - Part 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/The Attack and the Aftermath]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 2-3/Into the Wild Part 2]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 2-3/Return Trip]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/The Rampaging Beasts]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Magic Items]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Karawa (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Shakun Ritual]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Situation in Karawa - Shakun Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Notes - Shakun Heart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-0]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 28/Session 28]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Session 30]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime Timeline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Session 32]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Shakun's Heart Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Postscripts/Delwath (Postscript)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Leveling Up]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Backstory]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Brainstorming]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Character Notes - Dunmar Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Flowchart - Dunmar Arc 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Mystai of Shakun]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Overview - Dunmar Arc 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Secrets of Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/The Mystery of Shakun]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Dunmari Religion - Old Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Equipment Info DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Gnoll Warbands]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Karawa Area Map]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
%%^End%%

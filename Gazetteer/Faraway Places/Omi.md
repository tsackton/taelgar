---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: underwater city
ancestry: merfolk
name: Omi
whereabouts:
  - {type: home, location: Endless Ocean}
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

Omi is an important and ancient [[Merfolk|merfolk]] city in the western [[Endless Ocean]], in the deep waters west of [[Apporia]] and [[Tamaro Bay]]. Surface sailors know it chiefly through Apporian songs of the Jade Garden, but among the merfolk it is an important city of kelp forests, coral craft, manta rays, and communal memory watched over by the [[Sentient Ocean]]. 
## City of Kelp

Omi is built in and around a vast kelp forest. Its buildings are woven from living kelp, coral, shell, and stone, with roads and clearings winding through the undersea growth. Like other western merfolk settlements, Omi has little contact with surface peoples. The merfolk of Omi do not use a conventional land-dweller alphabet, but do record history and lore using pictograph glyphs, mosaics, and other visual signs.

The city is associated with a sacred kelp and coral garden mentioned in Apporian song as the Jade Garden. The [[Ballad of the Jade Garden]] places this garden west of [[Tamaro Bay]], where merfolk tend jade and grow names beneath the waves. [[Luminastra's Gift]] draws on the same rumors of merfolk who could grow names in a magical jade garden beneath the sea.

%%^Campaign:dufr%%
## The Garden of Names

The Jade Garden's true name was the Garden of Names. It was Omi's central sacred place: a living memorial where names, memories, and stories of those who had crossed through the ocean lived in kelp, coral, currents, and song. Its power was strengthened by a fragment of [[Jade Piece of Rai's Hand|Rai's jade hand]], which fell into Omi's kelp forests in DR 1718. Over the next five years, the merfolk learned to use the jade to channel the dreams of the [[Sentient Ocean]]. 

## Fall of Omi

In DR 1739, the merfolk warlock [[Buruli]] turned against Omi. Empowered by [[Gazankoa]], he seized the jade, corrupted the Garden of Names, and opened a portal to the [[Elemental Plane of Water]] in the heart of the city. Creatures and warriors from the Plane of Water flooded through the rift, threatening to spread beyond Omi into the wider seas.

The [[Sentient Ocean]] sealed Omi inside a protective barrier to stop the corruption from spreading. Many merfolk who had not joined Buruli were trapped inside, enslaved, killed, or dragged back through the portal. Buruli fled to the Plane of Water, leaving guards and a Herald of Gazankoa to hold the [[Material Plane]] side of the breach.

## Ruins and Rebuilding

When the [[Dunmar Fellowship]] reached Omi on (DR:: 1749-05-11), the city was ruined but not empty. They saw a long gash in the seafloor, dead kelp, bleached coral, collapsed coral buildings, a central civic ruin, a strange rippling pool, and guarded merfolk prisoners forced to work on the seafloor. Buruli's servants were excavating Omi for artifacts, pictographs, and mosaics connected to the origins and weaknesses of the [[Sentient Ocean]].

The [[Dunmar Fellowship]] defeated the Herald of Gazankoa, entered the [[Elemental Plane of Water]], rescued [[Milo Thistlefoot]], [[Tilly Brineheart]], and surviving members of the [[Stormdancer]] crew, and recovered the [[Jade Piece of Rai's Hand]] from Buruli on (DR:: 1749-05-12). 

The defeat of [[Buruli]] and recovery of the jade collapsed the portal in Omi. Since then, [[Merfolk]] have slowly returned and begun to rebuild and restore Omi to its former glory. 

%%^End%%

%%^Campaign:none%%
Relevant sources: [[Western Ocean]], [[Merfolk]], [[Ballad of the Jade Garden]], [[Luminastra's Gift]], [[Tamaro Bay]], [[Dorian Almare]], [[Jade Piece of Rai's Hand]], [[Visions of the Sentient Ocean]], [[Session 98 (DuFr)]], [[Session 99 (DuFr)]], [[Session 100 (DuFr)]], [[Session 101 (DuFr)]], [[Session 102 (DuFr)]], [[Milo's Story]], [[Stormdancer]], [[Elemental Plane of Water]], [[Gazankoa]], [[Rayna]], [[Mawar Adventures Episode 05]].
%%^End%%

%%^Metadata:names:v1%%
- {name: Omi, language: unknown, pronunciation: OH-mee, notes: "Proposed from the Merfolk naming guidance in [[Languages]], which has no fixed analogue but notes Classical or Japanese patterns with alternating consonant and vowel syllables: two syllables, pure o and i vowels, and a tentative first-syllable stress. No accepted pronunciation or exact source language is recorded.", status: proposed}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identity and geography, with the Dunmar Frontier passage recounting the DR 1739 fall and May DR 1749 liberation; the final rebuilding state is supported by a late-May DR 1749 vision and is not established for earlier dates.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name and a persistent primary-name entry with a proposed pronunciation.
- Added the required single-location map skeleton with its unknown locator left blank.
- Added broadly modern temporal metadata distinguishing the fall, liberation, and later rebuilding evidence.

### Validated judgments
- [[Visions of the Sentient Ocean]] and [[Session 100 (DuFr)]], [[Session 101 (DuFr)]], and [[Session 102 (DuFr)]] support the central garden, invasion, captive labor, and liberation account. [[Mawar Adventures Episode 05]] supplies later vision evidence for rebuilding.
- The Campaign:none block is a source list. Local evidence and in-note shared material were reviewed separately; no local source contents were incorporated into shared prose.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block now contains the single world-map entry, but its locator is unknown. Supply the verified world-map locator in the existing `locator` field; the ocean location and folk-song distance do not establish a hex coordinate.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `OH-mee` in the persistent name entry. [[Languages]] gives Merfolk no fixed real-world analogue, but notes Classical or Japanese naming patterns and alternating consonant/vowel syllables. The proposal uses two syllables with pure o and i vowels; first-syllable stress is tentative. Neither the precise name language nor an accepted pronunciation is recorded. If accepted, copy it to frontmatter and mark the entry documented.
- [ ] **Warning — correctness.cross_note_conflict:** The City of Kelp paragraph says Omi merfolk record history and lore through pictograph glyphs and mosaics, whereas [[Merfolk#At Home Underwater|Merfolk]] says they “have no writing.” [[Session 102 (DuFr)]] establishes pictographs and mosaics from excavations beneath Omi, but does not by itself identify all of those finds as contemporary merfolk record-keeping. Reconcile the narrow practice and the blanket species claim, preserving the archaeological evidence. A conservative candidate for the two record-keeping clauses in Omi is: “Pictographs and mosaics recovered from excavations beneath Omi depict strange forms and may preserve clues to the origins of the [[Sentient Ocean]]. Their relationship to present-day merfolk record-keeping is not established.” If Omi’s existing practice is independently confirmed, retain that exception and narrow the Merfolk statement instead.
- [ ] **Warning — correctness.cross_note_conflict:** The final paragraph asserts that Buruli’s defeat and recovery of the jade “collapsed the portal in Omi.” [[Elemental Plane of Water#Portals to the Plane of Water|Elemental Plane of Water]] calls the collapse presumed, and [[Session 102 (DuFr)]] records escape over the rainbow bridge without an observation of the Omi portal afterward. Resolve the certainty difference. Conservative candidate for the first sentence: “The portal in Omi was presumed to have collapsed after the defeat of [[Buruli]] and recovery of the [[Jade Piece of Rai's Hand|jade]].” Preserve the separate rebuilding evidence and do not infer an observed collapse from the jade’s removal alone.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Buruli Kingdom - Work Complex]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Kelp City Ruins]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 101 - DM Notes]]
%%^End%%

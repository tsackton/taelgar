---
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on", ltItem: stored on}
tags: [object, status/check/lint]
typeOf: skyship
subTypeOf: magical
typeOfAlias: skyship
rarity: unique
name: Vindristjarna
aliases: [Star on the Wind]
pronunciation: vin-dree-SHAR-na
whereabouts:
  - {type: home, location: unknown storm giant}
  - {type: home, location: dufr}
  - {type: away, start: 1748-12-03, end: 1748-12-10, location: Uzgukhar}
  - {type: away, start: 1748-12-28, end: 1749-01-04, location: Tollen}
  - {type: away, start: 1749-01-15, end: 1749-01-16, location: Orenlas}
  - {type: away, start: 1749-01-17, end: 1749-01-19, location: traveling to Xurkhaz}
  - {type: away, start: 1749-01-20, end: 1749-01-24, location: Uzgukhar}
  - {type: away, start: 1749-01-25, end: 1749-01-27, location: Nashtkar}
  - {type: away, start: 1749-01-28, end: 1749-01-29, location: "Pava and Avaras' House"}
  - {type: away, start: 1749-01-30, end: 1749-01-30, location: traveling to Copper Hills}
  - {type: away, start: 1749-03-13, end: 1749-03-16, location: Vostok}
  - {type: away, start: 1749-03-17, end: 1749-03-18, location: Sivnjo Mountains}
  - {type: away, start: 1749-05-30, end: 9999, location: Garamjala Desert}
  - {type: away, start: 1749-06-14, end: 9999, location: Gulf of Chardon}
knownTo: [dufr]
excludePublish: [clee]
dm_owner: tim
dm_notes: important
POV: 1749
---
```taelgar-header
```

%%
Whereabouts annotations:
- Tollen (1748-12-28 to 1749-01-04): check
- traveling to Copper Hills (1749-01-30): add session 90 travel
- Sivnjo Mountains (1749-03-17 to 1749-03-18): add travel
%%

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

%%^Metadata:names:v1%%
- {name: Vindristjarna, language: unknown, pronunciation: vin-dree-SHAR-na, status: documented}
- {name: Star on the Wind, role: alias, language: unknown, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 view of the restored and furnished ship, following the flight restoration of November 29, 1748; the History section also preserves its earlier unrepaired condition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit name and `knownTo: [dufr]`, supported by the ship's restoration and use by the Dunmar Fellowship.
- Normalized frontmatter formatting, quoting the existing `linkText` preposition as `"on"` to preserve its textual display meaning. With explicit user approval, moved the three YAML annotations into a hidden comment below the complete header, preserving their exact wording and associated whereabouts entries.
- Added documented name entries for Vindristjarna and Star on the Wind, preserving the accepted pronunciation; the source language remains unknown.
- Recorded `POV: 1749` and temporal coverage for the restored, furnished ship.

### Validated judgments
- The restoration in [[Session 74 (DuFr)]] and the refit in [[Interlude (Tollen Downtime)]] support the restored-ship reading. Detailed operating rules remain available through the existing mechanics links.
- Confirmed matching local DM evidence supports the existing positive `dm_notes` attestation; private contents are not reproduced here.
- Retained the shared nonpublic roster queries and their editorial note in their existing wrapper.

### Open findings

- [ ] **Warning — temporal.mixed_viewpoints:** The History sentence beginning “While the phasing stone that originally powered Vindristjarna is mostly destroyed” still describes a ship that could be made to fly, whereas Recovery and Repair says it was restored. [[Session 74 (DuFr)]] establishes the first flight on November 29, 1748. For an always-visible historical account, replace that sentence with: “Before the Dunmar Fellowship restored Vindristjarna, its original phasing stone was mostly destroyed, but the ship was otherwise intact and could be made to fly with a new phasing stone.” If date-filtered views are intended instead, propose the old-condition paragraph inside `%%^Date:1748-11-29b%%` / `%%^End%%` and only the opening restoration paragraph inside `%%^Date:1748-11-29%%` / `%%^End%%`; the furnished-deck description needs its own refit boundary. No visibility change has been applied.
- [ ] **Warning — correctness.cross_note_conflict:** Recovery and Repair gives “living quarters for ten hirelings or followers,” while [[Vindristjarna Bastion Rules#Basic Facilities, Lower Level]] specifies twelve hireling quarters. Confirm whether these describe different layouts. If the bastion layout is the intended current account, replace “ten hirelings or followers” with “twelve hirelings or followers”; otherwise date the earlier ten-person layout and reconcile the two descriptions.
- [ ] **Warning — metadata.whereabouts_conflict:** The final whereabouts entry starts the Gulf of Chardon stay on June 14, 1749, but [[Session 124 (DuFr)]] places the ship at Pava and Avaras' house through June 17, departing June 18 and entering the gulf on June 25. Candidate correction for that entry: `start: 1749-06-25`. Its `end: 9999` also presents this as an ongoing location, while [[Session 131 (DuFr)]] has the ship approaching Aurbez in August. Decide whether to update the later itinerary, defer with a human-applied `status/gameupdate/dufr`, or intentionally retain a clearly bounded earlier snapshot; do not infer a final departure date from a last-observed position.

### DM evidence
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/_Campaign 3/Dunmar Epliogue - Campaign 3 Timing]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Stormcaller Tower (OneNote)]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 0]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 105 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 106 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Arc Outline]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/chatGPT - Cloudspinner Arc]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chalyte Giant Adventure]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chalyte Giants Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Isingue Arc Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Limbo/Isingue - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Limbo/Nantucket Planning]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 130 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 132 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 133 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 134 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Stormcaller Tower - DM Version]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 66 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 67 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 79 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 85 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 94 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

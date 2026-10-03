---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-12-30, type: first met}
born: 1516
gender: male
image: faldrak-small.png
name: Faldrak Bronzehammer
aliases: [Faldrak]
affiliations:
  - {org: Bronzehammers, type: primary}
whereabouts:
  - {type: home, start: "", end: 1693-01-01, location: Fahnukan}
  - {type: away, start: 1693-01-01, end: "", location: Feywild}
  - {type: away, start: 1698-01-01, end: "", location: Feywild}
  - {type: home, start: 1727-01-02, end: 1749-01-04, location: Tollen}
  - {type: away, start: 1749-01-05, end: 1750, location: Vindristjarna}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Faldrak Bronzehammer
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of Bronzehammers  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% First met by the [[Dunmar Fellowship]] on December 30th, 1748 in the [[Tollen|Free City of Tollen]] %%^End%%

![[faldrak-portrait-1.png|right|400]]Faldrak Bronzehammer is an aged dwarf runecrafter and tinker, with a touch of Feywild whimsy.
## Overview
Faldrak Bronzehammer, with his eccentric blend of traditional dwarven craftsmanship and fey magic, has become a subject of both admiration and curiosity. Born in [[Fahnukan]], a strange northern dwarven kingdom, his life took an unexpected turn during an accidental sojourn in the [[Feywild]]. Although he emerged with peculiar behaviors, his enhanced craft bearing fey enchantments has left many in awe. 
## Description
Despite his aging exterior and graying, rune-braided beard, Faldrak's eyes sparkle with mischief. His wardrobe—a combination of dwarven armor and fey fabrics—reflects his diverse experiences. A small pouch, perpetually moving, is always by his side. He walks with a cane, which seems to be magical and multipurpose. 
## Events

- In DR 1748, during [[Pyravela]] in [[Tollen]], Faldrak attended the party hosted by The Dunmar Fellowship on [[Vindristjarna]], where he met and bonded with Seeker, requesting his aid in journeying to the [[Edge of Echoes]], a mysterious place where the boundaries between the planes (especially between Taelgar and the elemental planes) are thin. 

%%SECRET[v2:1da9cd38631c8b787cdfe27567301be9]%%

%%^Metadata:names:v1%%
- {name: Faldrak Bronzehammer, language: unknown, pronunciation: "FAHL-drahk BRONZ-ham-er", status: proposed, notes: "Faldrak follows the Dwarvish cultural context and the analogue in [[Languages]]: distinct consonants, both a vowels as ah, and provisional initial stress. Bronzehammer is read as the transparent English compound. The full name's source language and exact pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of an aged runecrafter, with earlier Feywild backstory and a dated introduction in Tollen; the visible account does not yet cover his subsequent role aboard Vindristjarna.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting without changing existing dates or affiliations.
- Added `knownTo: [dufr]` from the existing campaign interaction and the played record.
- Stored the existing lead image as `image: faldrak-small.png`, the filename form specified for that field; the asset exists and was not replaced.
- Added the primary name entry with a proposed pronunciation and an explicitly unknown full-name language.
- Recorded `POV: 1740s` and the limited temporal coverage of the visible portrait.

### Validated judgments
- The aged runecrafter portrait supports a late-1740s reading; the isolated dated introduction does not require a whole-note year. Later ship service and crafting are a separate coverage decision below.
- `status/cleanup/metadata` remains supported by the unresolved affiliation target and is preserved.
- Matching local evidence supports the existing positive `dm_notes` attestation. The SECRET block was independently reviewed; its content remains outside this report.

### Editorial assessment
**Underdeveloped**. The visible account stops at the introduction in Tollen and lacks Faldrak’s subsequent crew/captain role aboard Vindristjarna and the completed craft that defines his lasting partnership with Seeker. The smallest useful scope is a short account of those established roles and achievements, not a campaign log. No separate invented transition is needed: the recruitment bargain and later command are recorded in play.

### Open findings

- [ ] **Warning — relationship.unresolved:** `affiliations: {org: Bronzehammers, type: primary}` does not resolve to a vault note or established identity, and the header repeats that clan label. The name/alias and filename checks found no clan page. Confirm whether Bronzehammers is the intended clan identity and authorize a minimal clan note, or supply the correct existing affiliation target. Preserve the current value until that identity decision is made.
- [ ] **Warning — metadata.names_unresolved_status:** The new primary entry proposes `FAHL-drahk BRONZ-ham-er`. The Dwarvish analogue in [[Languages]] is the strongest available cultural guidance: the proposal keeps the written consonants distinct, reads both a vowels as ah, and provisionally stresses the first syllable; the transparent English surname is read BRONZ-ham-er. This is an analogue-informed proposal, not documented in-world phonology, and the full name’s language remains unknown. Accept or correct the complete pronunciation, then copy the accepted value to frontmatter and mark the entry documented.
- [ ] **Warning — coverage.later_material_change:** The visible account records only the DR 1748 introduction. [[Session 84 (DuFr)]] records his recruitment bargain, [[Session 87 (DuFr)]] and [[Elemental Forge Hoard]] establish his completed craft with Seeker, [[Faldrak's Journal Notes]] identifies the successful flight of Pebblepeep, and [[Session 94 (DuFr)]] explicitly leaves him in command on DR 1749-04-11. [[Dunmar Fellowship Associates]] accordingly identifies him as a skyship captain. The finalized Session 139 beat facts (`_sessions/dunmar-frontier/dunmari-frontier-139/cleaned/dunmar-frontier-139-beat-facts.json`, beats 004 and 009) establish completed communication rings and a still-planned planar refit. Choose whether to update the article and its temporal interpretation, defer with a human-selected game-update status, or deliberately retain the earlier portrait. Copy-ready bounded update: “In DR 1749, Faldrak joined the crew of [[Vindristjarna]] and took command while the [[Dunmar Fellowship]] traveled ashore. At the [[Elemental Forge]], he and [[Seeker]] constructed the ship’s planar prism and icicle turret, and Faldrak made his stone bird Pebblepeep fly. By November, they had made four rings from the rainbow prism that allowed the fellowship to exchange messages and return to Vindristjarna; further work to prepare the ship for planar travel remained a plan.” If date-filtered visibility is wanted, retain the current portrait and add only the new material in dated layers for the completed January craft, command attested on April 11, and November plans; do not silently apply those visibility changes or present the refit as completed.
- [ ] **Suggestion — editorial.reference_voice:** In `Overview`, “has become a subject of both admiration and curiosity” and “has left many in awe” repeat generalized praise without identifying an observer, an achievement, or a setting-specific consequence. Rewrite or remove those clauses during human review while preserving his Fahnukan origin, accidental Feywild sojourn, and the stated mixture of dwarven craftsmanship and fey enchantment. The concrete physical description need not be rewritten.

### DM evidence
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 105 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chalyte Giant Adventure]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Edge of Echoes - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 79 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 80 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 85 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 94 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

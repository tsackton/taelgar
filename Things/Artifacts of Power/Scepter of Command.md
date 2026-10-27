---
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
tags: [object, testcase, status/check/lint]
typeOf: scepter
rarity: unique
campaignInfo:
  - {campaign: dufr, type: destroyed, date: 1748-12-25}
created: 1053
destroyed: 1748-12-25
name: Scepter of Command
whereabouts:
  - {type: home, end: 1059, location: Apollyon}
  - {type: away, start: 1552, end: 1746, location: Kharsan, startFilter: ""}
  - {type: home, location: Fraternity of the Empty Moon, start: 1747, end: 1747-12-11}
  - {type: home, location: Agata, start: 1748-01-17, end: 1748-05-29}
  - {type: home, location: Dunmar Fellowship, start: 1748-05-29, end: 1748-12-24}
  - {type: away, location: Vetta, start: 1748-12-24, end: 1748-12-25}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

![[scepter-of-command.jpg|right|300]]%% needs to incorporate some secrets in to the note, as most have been revealed in game by now %%

This scepter is about a foot long and is constructed in silver, with loops of silver forming a ball at the head, set with diamonds that seem to catch the light. It feels very old, and yet doesn't seem tarnished or worn at all. 

It seems powerful, and like it wants to be used.

%%^Campaign:dufr%%
Seen in [[Mirror of the Past]]: [[Scepter of Command Vision]]

From the mirror, you learned this is of Drankorian origin, constructed by [[Apollyon]], an emperor of [[Drankor]] in a tall black tower on a perfectly circular island, and used to enhance his command of his armies. It was carried by the fire giant who destroyed [[Kharsan]], you presume [[Mavdyr]] who led an [[Orcs|orc]] horde to attack [[Tokra]] in 1552 by the Drankorian Reckoning, 7 years after the death of [[Cha'mutte]]. [[Agata]] apparently obtained it in trade with the [[Fraternity of the Empty Moon]], in exchange for a scroll that would summon (and presumably bind) a demon from the [[Abyss]] who had the power to create gnoll armies, as well as a [[Pandemonium Scroll|scroll]] with the power to enhance the essence of [[Pandemonium]]. 
%%^End%%

%%^Date:1748%%
## Destruction
The Scepter of Command was destroyed in 1748, by [[Dunmar Fellowship]]. It was immersed in the sacred waters on the island of [[Vetta|Vetta]] in the Skaer Islands for 24 hours during a full moon, and then shattered with the combined power of [[Kenzo]]'s staff and the might of [[Kaikkea]]'s waters. 
%%^End%%

%%SECRET[v2:ed02a62757915b63bead81777b966216]%%

%%^Metadata:names:v1%%
- {name: Scepter of Command, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the intact artifact, with earlier provenance and a destruction account dated DR 1748-12-25; the physical description refers to the scepter before its destruction.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added the explicit name and `knownTo: [dufr]`, supported by the existing campaign record and [[Session 81 (DuFr)]].
- Normalized the existing campaign codes to `dufr` without changing their scope.
- Added minimal name metadata; the plain-English title needs no pronunciation, and its in-world language remains unestablished.
- Added `POV: modern` and temporal guidance distinguishing the intact artifact's description from its dated destruction.

### Validated judgments
- Confirmed local evidence supports the existing positive `dm_notes` attestation. Private contents remain outside this report.
- Reviewed the local-only SECRET block separately; any useful recovery is confined to the private handoff.
- The existing destruction date and account agree with [[Session 81 (DuFr)]].

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The Fraternity's whereabouts entry ends on DR 1747-12-11, but [[Fraternity of the Empty Moon#Chronology]] identifies that date as the initial approach to Agata and dates the trade of the scepter to DR 1748-01-17. The target itself begins Agata's possession on that latter date. Confirm the custody boundary; if the reference chronology is adopted, replace the Fraternity entry with `{type: home, location: Fraternity of the Empty Moon, start: 1747, end: 1748-01-17}`. Preserve a distinct earlier transfer only if its source can be identified.
- [ ] **Warning — temporal.date_scope:** The `Destruction` section uses `%%^Date:1748%%`, so the destruction can appear before DR 1748-12-25; the campaign-scoped destruction statement in the header has no date boundary at all. The precise event date is established by the target's metadata and [[Session 81 (DuFr)]]. Proposal: change the section's opening marker to `%%^Date:1748-12-25%%` and date-scope the existing header statement while retaining its campaign restriction. Copy-ready header line: `>> %%^Campaign:dufr%% %%^Date:1748-12-25%% Destroyed by [[Dunmar Fellowship]] on December 25th, 1748 in [[Vetta]], [[Skaerhem]] %%^End%% %%^End%%`. These visibility changes require human approval and have not been applied.

### DM evidence
- [[_DM_/Timelines/Cloak of Rainbows Timeline]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Magic Items]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Shakun's Heart Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 38]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Summary]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Circular Island Overview - DM notes v2]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Seven Souls]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Temple of Apollyon]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Timeline for the End of Drankor]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Brainstorming - Scepter Arc]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Temple Key]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
%%^End%%

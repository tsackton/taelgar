---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed}
tags: [person, status/check/lint]
species: undead
subspecies: skeletal
campaignInfo:
  - {campaign: dufr, type: scryed, date: 1748-12-28}
  - {campaign: dufr, type: defeated, date: 1749-01-20}
born: null
died: 1749-01-20
gender: male
name: Grash
whereabouts:
  - {type: away, start: 1747, end: 1748-11-28, location: Kharsan}
  - {type: away, start: 1748-11-28, end: 1748-12-05, location: Garamjala}
  - {type: away, start: 1748-12-05, end: 1748-12-14, location: Xurkhaz}
  - {type: away, start: 1748-12-14, end: 9999, location: Uzgukhar}
knownTo: [dufr]
excludePublish: [clee]
dm_owner: tim
dm_notes: important
POV: modern
---
# Grash
>[!info]+ Biographical Info
> A skeletal [[Undead|undead]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Scryed by the [[Dunmar Fellowship]] on December 28th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%
>> %%^Campaign:DuFr%% Defeated by the [[Dunmar Fellowship]] on January 20th, 1749 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

![[image-grash-1.png|right|320]]Known as Grash the Undying, an undead warrior and commander of a large [[Orcs|orc]] army in Kharsan. He possessed the [[Ring of Undying]], and used it to create a large army of orcs and undead. 

Grash was rumored to once have been a knight from an unknown land, a warrior, skilled in battle, who sought glory in the [[Nashtkar]], and never returned. He became something of a rumor and legend, a haunted ghost to frighten children with. A knight of shadows who could cut wounds that would not heal with his glaive. A cursed warrior, who could summon chains of darkness to bind your heart and drag you closer to death. 

How he acquired the [[Ring of Undying]], and how he found himself in [[Apollyon|Apollyon]]'s service, are not known.

%%^Metadata:names:v1%%
- {name: Grash, language: unknown, pronunciation: GRASH, status: proposed, notes: "Cautious spelling-based proposal: one syllable, initial gr as in grasp, short a as in ash, and final sh as in ship. No name-specific pronunciation or source language is established in the reviewed evidence. The note also calls him Grash the Undying."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of Grash's command at Kharsan and rumored earlier life, with his defeat in DR 1749 recorded in the header; the present article does not recount the intervening War of the Cloak.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; canonicalized the existing campaignInfo codes to `dufr`.
- Added `knownTo: [dufr]` from the existing campaign interactions.
- Added a persistent name entry with a proposed spelling-based pronunciation, retaining the unknown source language.
- Added `POV: modern` and temporal coverage describing the retrospective article and its limits.

### Validated judgments
- The existing positive `dm_notes` attestation is supported by confirmed local evidence; its value is unchanged.
- The rumored early life and explicitly unknown origins remain uncertain. The established war and fate can be summarized without inventing how Grash acquired the ring or entered Apollyon's service.

### Editorial assessment
**Underdeveloped**: the page identifies Grash's Kharsan command and records a defeat date, but lacks the central account of his invasion of Xurkhaz for the Cloak of Rainbows, his siege of Uzgukhar, and the destruction of the ring and the undead army at his final defeat. One bounded paragraph can supply these established dimensions; the rumored early life need not be expanded.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The body ends with his unknown origins and never explains the defining war or why his defeat was final. [[War of the Cloak]] establishes the invasion to seize the cloak and the siege; [[Session 88 (DuFr)]] establishes Wellby's destruction of the ring, Delwath's killing of Grash, and the collapse of the undead sustained by the ring. Add the following bounded conclusion, with the proposed date block keeping the completed outcome from appearing before the battle. This changes prose and filtered visibility, so it remains a human adoption choice:

```markdown
%%^Date:1749-01-20%%
During the [[War of the Cloak]], Grash invaded [[Xurkhaz]] to seize the [[Cloak of Rainbows]] and besieged [[Uzgukhar]]. The [[Dunmar Fellowship]] defeated him at the [[Battle for Uzgukhar]] on January 20th, DR 1749: [[Wellby]] destroyed the [[Ring of Undying]], [[Delwath]] killed Grash, and the undead sustained by the ring collapsed.
%%^End%%
```

- [ ] **Warning — correctness.cross_note_conflict:** The first two whereabouts entries put the Kharsan-to-Garamjala transition on `1748-11-28`, while [[War of the Cloak#Events in the War]] explicitly dates Grash's departure from Kharsan to `1748-11-27`. Confirm which date governs before changing the recorded journey. If the war timeline is adopted, replace just those two entries with `{type: away, start: 1747, end: 1748-11-27, location: Kharsan}` and `{type: away, start: 1748-11-27, end: 1748-12-05, location: Garamjala}`. The same timeline dates the army's arrival at Uzgukhar to December 15, whereas Grash's whereabouts there begin December 14; verify whether his individual movement differed before adjusting that boundary.
- [ ] **Warning — metadata.names_unresolved_status:** The new primary name entry proposes `GRASH`: one syllable, initial `gr` as in grasp, short `a` as in ash, and final `sh` as in ship. No explicit name pronunciation or established source language was found in the reviewed evidence, so this is a cautious spelling-based proposal, not an adopted language rule. Accept or correct it; if accepted, use `pronunciation: GRASH` in frontmatter and change the persistent entry to `status: documented`.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Both generated interaction lines use `%%^Campaign:DuFr%%`. The registry resolves that alias to `dufr`; replace each opening marker with `%%^Campaign:dufr%%`, preserving the enclosed text and closing markers. The existing generated header is otherwise left unchanged.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Brainstorming - DM]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Grash (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Vola Forena (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan Palace/Palace]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Design Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan City Proper]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan Palace]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Mechanics]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Monastery of Bhishma/Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Stronghold Map]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 23 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/General Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Lair (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Centaur Camp]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 1 - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Postscripts/Postscripts]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Arc overview/Arc overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Events in Tokra]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 39]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Leveling Up]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Bhishma Monastery]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Apollyon Dopplegangers]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Grash Arc Overview]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Brainstorming - Scepter Arc]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Grash Statblock]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 100 - DM Notes]]
- [[_DM_/_Dunmari Frontier/assets/grash-battle-layout.excalidraw]]
%%^End%%

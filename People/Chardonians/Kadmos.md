---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed}
tags: [person, testcase, status/gameupdate/dufr, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-12-08, type: encountered}
born: 1711
gender: male
died: 1748-12-08
name: Kadmos
affiliations:
  - Society of the Open Scroll
  - {org: The Cleansed, title: Cultist}
whereabouts:
  - {type: home, start: "", end: "", location: Chardon}
  - {type: away, start: 1748-11-15, end: "", prefix: somewhere in, location: Dunmar}
  - {type: away, start: 1748-11-19, end: "", location: Garamjala Desert}
  - {type: away, start: 1748-12-08, end: 1748-12-08, location: Uzgukhar}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Kadmos
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Encountered by the [[Dunmar Fellowship]] on December 8th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

%%collate various notes for completeness -- mostly in Obsidian DM notes%%

![[kadmos-portrait.png|right|320]]A mysterious figure who doesn't speak unless necessary, the leader of this company, with [[Hektor]], [[Marcella]], [[Antonia]], and [[Casian]]. 

A tall Chardonian man, cloaked and hooded, wearing dark, travel-stained leather armor, without obvious weapons. A spellcaster, who took on an undead visage in combat and whose spirit seems touched by a darkness. 

A character of dubious morality, clearly willing and able to use enchantment magic to get what he wants, and happy to provoke a fight. 


%%SECRET[v2:127b5aa7c1542b5b132493a3563d442c]%%

%%^Metadata:names:v1%%
- {name: Kadmos, role: primary, language: Chardonian, pronunciation: KAD-mohs, notes: "Chardonian is established by his ancestry and origin in Chardon; pronunciation is proposed from the documented Chardonian Italian/Latin analogue with occasional Classical Greek forms, using the first-syllable stress and clear final -os of the Greek-form name", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Kadmos during his encounters with the Dunmar Fellowship and ending with his death on December 8; his earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from Kadmos's direct interactions with the Dunmar Fellowship in [[Session 43 (DuFr)]], [[Session 44 (DuFr)]], and [[Session 78 (DuFr)]].
- Normalized frontmatter ordering and collection formatting.
- Added persistent `Metadata:names:v1` metadata for Kadmos with established Chardonian language and an analogue-derived pronunciation proposal.
- Added `POV: 1748` and a `povNotes:v1` block identifying the visible article as a DR 1748 portrait.

### Validated judgments
- `status/gameupdate/dufr` is supported: [[Session 78 (DuFr)]] and [[Session 79 (DuFr)]] establish a later assault, defeat, and death that the visible article does not yet represent.
- `dm_notes: important` is supported by confirmed local `_DM_` matches; the finalizer records the exact source links without exposing private contents.
- The `SECRET` block was reviewed and remains local-only; a bounded public-recovery candidate is reserved for the private handoff.
- The shared comment was retained as an editorial source pointer.

### Editorial assessment
- **Underdeveloped**. The visible note is only a brief DR 1748 sketch of a recurring antagonist. It omits Kadmos's later alliance with Grash, leadership of the assault on Uzgukhar, defeat, and execution. The smallest useful development scope is one concise sourced paragraph covering that final arc and fate.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new `Metadata:names:v1` entry records Chardonian from Kadmos's ancestry and origin in Chardon and proposes `KAD-mohs` from the documented Chardonian Italian/Latin analogue with occasional Classical Greek forms, using first-syllable stress and a clear final `-os`. Review the proposal; if accepted, change the entry to `status: documented` and add `pronunciation: KAD-mohs` to frontmatter, or revise the pronunciation and derivation note.
- [ ] **Warning — coverage.later_material_change:** [[Session 69 (DuFr)]], [[Session 78 (DuFr)]], [[Session 79 (DuFr)]], and [[War of the Cloak]] establish a defining later arc absent from the article. Either add the following paragraph and retain `POV: 1748`, defer the update and retain `status/gameupdate/dufr`, or intentionally preserve the earlier portrait and remove that game-update tag: `By late DR 1748, Kadmos had joined [[Grash]]'s campaign against [[Xurkhaz]] and led an assault on [[Lubash]] in [[Uzgukhar]] to seize the [[Cloak of Rainbows]]. The [[Dunmar Fellowship]] defeated the attackers on December 8; after Kadmos and [[Casian]] nearly escaped with the cloak, [[Delwath]] counterspelled their final attempt, and Kadmos was captured and executed.`

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Finding Artifacts in Chardon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Session 62 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 46 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Postscripts/Postscripts]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Arc overview/Arc overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part I To Arendum/The Shadow Hunter]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/SESSION I]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Magic Items - Dunmar]]
- [[_DM_/_Dunmari Frontier/Equipment Info DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 134 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Grash Arc Overview]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
%%^End%%

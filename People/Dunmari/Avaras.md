---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T23:46:56-04:00"
lintVersion: "3.4"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, date: 1748-05-02, type: met}
born: 1676
gender: male
name: Avaras
affiliations: [Order of the Awakened Soul]
whereabouts:
  - {type: home, start: "", end: "", location: Karawa}
  - {type: home, start: 1717-01-01, end: "", location: "Pava and Avaras' House"}
  - {type: away, start: 1749-01-01, end: "", location: "Pava and Avaras' House"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Avaras
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% need to add campaign info, perhaps a bit more context %%

![[avaras-portrait.png|right|400]]Avaras is one of the few remaining masters of the [[Order of the Awakened Soul]]. He is an older man, with close-cropped gray hair and lined, weathered skin. He lives in the [[Garamjala Desert]] with his partner [[Pava]] and apprentice [[Amil]], leading an isolated existence, concerned with [[Pava]] and with what is left of the Order's mission.
%%SECERT 
**One-word key: contemplative
Demeanor: quiet, cautious, always thinking about Pava and to a lesser extent [[Amil]], close to animals**
%%
Avaras grew up on the plains near [[Karawa]]. He was a loner as a child, but drawn to the stories that the wandering monks of the [[Order of the Awakened Soul]] would tell, and drawn to the idea of gathering the history of the common people. 

### Life Events

* (DR:: 1693) Became an apprentice of the [[Order of the Awakened Soul]] at 17 and traveled around much of Eastern Dunmar 
* (DR:: 1711), when he went to the [[Monastery of Bhishma]], met [[Pava]], and was raised out of his apprenticeship. 
* (DR:: 1717), after the [[Awakened Soul Disaster]] took up residence in the desert with [[Pava]], to watch the comings and goings on the plains and rescue the lost and the desperate who come seeking treasure, glory, or death in the desert. 

It is a quiet life, with time for contemplation. With [[Pava]] and the occasional apprentice, he has sought out the many stories of lives lived on these lands that are forgotten, and sought to quiet the restless and forgotten dead who died in the chaos of the Great War and the Blood Years with no one to mark their lives. 

%%^Campaign:dufr%%
### Recent Happenings
* (DR:: 1747-08-19) Avaras and Pava found an elf, Delwath, wandering confused in the desert west of Kharsan, dying of thirst and delirious. They took him in, and removed his armor which seemed to be smoking with some kind of shadows. 
* (DR:: 1747-08-20) Delwath left in the night a few days later.
* (DR:: 1748-05-02) Delwath returned and [[Session 19 (DuFr)|met Avaras again]], with the [[Dunmar Fellowship]]

%%^End%%

%%^Metadata:names:v1%%
- {name: Avaras, role: primary, language: Dunmari, pronunciation: AH-vah-rahs, status: proposed, notes: The Dunmari Hindi and Indo-Iranian analogue supports this cautious reading; exact in-world phonology is not recorded.}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait with selected childhood and early-adult backstory; later DR 1749 developments involving Amil and the Dunmar Fellowship are not incorporated into the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the established Dunmar Frontier interaction to `campaignInfo` and `knownTo`; added `POV`, `povNotes`, and a persistent pronunciation proposal; normalized frontmatter and the campaign block code.
- Corrected `close cropped`, the `Recents Happenings` heading, and the tense of the DR 1748 reunion entry.
- Corrected Delwath's departure date from DR 1747-08-21 to DR 1747-08-20, following [[Delwath]].

### Validated judgments
- `status/cleanup/metadata` remains supported because the chronology and whereabouts metadata still require human resolution; no status was changed.
- Matching local-only sources support `dm_notes: important`; their contents are not reproduced here.

### Open findings
- [ ] **Error — correctness.cross_note_conflict:** The DR 1717 life-event entry and house `whereabouts.start` place Avaras's settlement after the [[Awakened Soul Disaster]], but [[Awakened Soul Disaster]] and [[Order of the Awakened Soul]] date that disaster to DR 1718. A copy-ready reconciliation is `* (DR:: 1718) After the [[Awakened Soul Disaster]], Avaras took up residence in the desert with [[Pava]], to watch the comings and goings on the plains and rescue the lost and the desperate who come seeking treasure, glory, or death in the desert.` and `start: 1718` for the house whereabouts; use a later start instead if the move was not immediate.
- [ ] **Warning — metadata.whereabouts_conflict:** The DR 1749 `away` entry points to the same `Pava and Avaras' House` as the ongoing home entry, while [[Session 124 (DuFr)]] places Avaras at that house in June 1749. Remove `- {type: away, start: 1749-01-01, end: "", location: "Pava and Avaras' House"}` if it is redundant, or replace its date and location with the intended journey.
- [ ] **Warning — coverage.later_material_change:** The visible account still says Avaras lives with his apprentice Amil. [[Session 89 (DuFr)]] establishes that Amil left with the Dunmar Fellowship on DR 1749-01-30 to travel as Kenzo's apprentice, and [[Session 124 (DuFr)]] shows Avaras still at the desert house in June 1749, approving of Kenzo's new spiritual mastery. Choose whether to update the article and `POV`, defer the update with the appropriate game-update status, or preserve the DR 1748 snapshot. Copy-ready update: `By DR 1749, Amil had left the house to travel as Kenzo's apprentice, while Avaras remained at his desert home with Pava. In June, Avaras observed Kenzo's new spiritual mastery with approval.`
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Avaras — AH-vah-rahs` (proposed). Dunmari's documented Hindi and Indo-Iranian analogue supports this cautious three-syllable reading, but exact in-world phonology and stress are not established. Accept it by adding `pronunciation: AH-vah-rahs` to frontmatter and changing the name entry to `status: documented`, or correct the proposal.
- [ ] **Warning — privacy.malformed_secret_marker:** The hidden roleplaying block begins with `%%SECERT`, which is not a recognized local-only `SECRET` marker and therefore remains a Git-shared ordinary comment. Change the opening marker to `%%SECRET[v2:1e5f13af3dfef8a8b312e0f42f9ca3f8]%%` if Git-shared DM guidance was intended.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Awakened Soul Monks]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Bas Udda (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
%%^End%%

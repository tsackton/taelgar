---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T12:50:50-04:00"
lintVersion: "3.5"
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

%%SECRET[v2:378312f41ce482bbb945db438546b86a]%%

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
- None.

### Validated judgments
- Reconfirmed `POV: 1748` and the existing `povNotes` description as an accurate temporal reading of the visible article; the later DR 1749 developments remain a separate open coverage decision.
- `status/cleanup/metadata` remains supported because the chronology and whereabouts metadata still require human resolution; no status was changed.

### Open findings
- [ ] **Error — correctness.cross_note_conflict:** The DR 1717 life-event entry says Avaras settled in the desert after the [[Awakened Soul Disaster]], but [[Awakened Soul Disaster]] and [[Order of the Awakened Soul]] date that event to DR 1718. If the move immediately followed the disaster, use `* (DR:: 1718) After the [[Awakened Soul Disaster]], Avaras took up residence in the desert with [[Pava]], to watch the comings and goings on the plains and rescue the lost and the desperate who come seeking treasure, glory, or death in the desert.` and change the house `whereabouts.start` to `1718`; otherwise retain the established move date and revise the sentence to separate it from the disaster.
- [ ] **Warning — metadata.whereabouts_conflict:** The DR 1749 `away` entry points to the same `Pava and Avaras' House` as the ongoing home entry, while [[Session 124 (DuFr)]] places Avaras at that house in June 1749. Remove `- {type: away, start: 1749-01-01, end: "", location: "Pava and Avaras' House"}` if it is redundant, or replace its date and location with the intended journey.
- [ ] **Warning — coverage.later_material_change:** The visible account still says Avaras lives with his apprentice Amil. [[Session 89 (DuFr)]] establishes that Amil left with the Dunmar Fellowship on DR 1749-01-30 to travel as Kenzo's apprentice, and [[Session 124 (DuFr)]] shows Avaras still at the desert house in June 1749, approving of Kenzo's new spiritual mastery. Choose whether to update the article and `POV`, defer the update with the appropriate game-update status, or preserve the DR 1748 snapshot. Copy-ready update: `By DR 1749, Amil had left the house to travel as Kenzo's apprentice, while Avaras remained at his desert home with Pava. In June, Avaras observed Kenzo's new spiritual mastery with approval.`
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Avaras — AH-vah-rahs` (`status: proposed`). The stored entry derives this cautious three-syllable reading from Dunmari's Hindi or other Indo-Iranian analogue and notes that exact in-world phonology is not recorded. Accept it by adding `pronunciation: AH-vah-rahs` to frontmatter and changing the name entry to `status: documented`, or correct the proposal.
- [ ] **Warning — privacy.malformed_secret_marker:** The roleplaying-guidance comment begins with `%%SECERT`, which is not the recognized local-only `SECRET` marker and is therefore Git-shared. Change the opening marker to `%%SECRET[v2:1e5f13af3dfef8a8b312e0f42f9ca3f8]%%` if Git-shared DM guidance was intended.
%%^End%%

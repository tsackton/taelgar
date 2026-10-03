---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/text, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo: []
born: null
died: 1748
gender: male
name: Hagrim of Morkalan
whereabouts:
  - {type: home, end: 1545, location: Ardith}
  - {type: home, end: 1570, location: Nardith}
  - {type: home, start: 1571, location: Morkalan}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Hagrim of Morkalan
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% needs significant refactoring, and add campaign info %%

![[hagrim-portrait.png|right|400]]A dwarf, once known as Hagrim Firebrand, who made a name for himself in the [[Great War]], but was unable to forget or move past the horrors he saw in battle against mind flayers and the aberrations of the deep, fighting under the halls of [[Ardith]]. Whether he was broken by battle or his mind was corrupted by those evils, he returned a changed man. 

He reluctantly left his retirement to help lead a group of warriors, including the young soldier [[Nora Silverspark]], on a rescue mission to find refugees in [[Ardith]], bringing the [[Chalice of the Runepriest]] to aid in the quest.

The rescue was somewhat successful, but on the return journey across [[Dunmar]], the [[Dwarves]] encountered the fire giant [[Odim Mavdyrson]], the son of [[Mavdyr]], who had fought and been defeated by an army of [[Dwarves]] and humans outside [[Tokra]] in the [[Fire War]]. Odim sought revenge for his father's defeat, and drove the [[Dwarves]] to take refuge in fortifications constructed [[Stoneborn Statue Dungeon|beneath the ancient Stoneborn Warrior statue]] on the plains north of [[Tokra]].

During the ensuing battle, [[Hagrim]] broke and turned on [[Nora Silverspark]], claiming she was about to betray him. As dwarf fought dwarf, Odim laughed in victory. As Hagrim died, his betrayal and anger, and possibly the corruption in his mind from the aberrations of the [[Great War]], created the [[Shadowfolds]] domain of [[Morkalan]] around him, trapping the surviving [[Dwarves]] in his nightmare. 


%%SECRET[v2:d8d6df76a8bcffcecbeef5a3bc739b0f]%%

%%^Metadata:names:v1%%
- {name: Hagrim of Morkalan, language: unknown, pronunciation: HAH-grim ov MOR-kah-lahn, notes: 'Proposed from the Tolkien Dwarvish analogue in [[Languages]] for the dwarven personal name: open a, short i, hard g, and sounded r; first-syllable stress is tentative. The domain name uses a cautious spelling-based reading; no adopted Morkalan pronunciation is recorded.', status: proposed}
- {name: Hagrim Firebrand, role: historical, language: unknown, notes: 'Name used before the creation of Morkalan, as recorded in this article and [[Chalice of the Runepriest]].', status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of Hagrim’s Great War service and the creation of Morkalan; the visible narrative stops before his later ghostly rule and final defeat in DR 1748.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo: [dufr]`, current and historical name metadata, and temporal metadata; normalized frontmatter.
- Corrected “solider” to “soldier,” “aid in the question” to “aid in the quest,” and one duplicated space in visible prose.

### Validated judgments
- The Great War history and the uncertainty over battle trauma or aberrant corruption are corroborated by [[Session 58 (DuFr)]] and remain qualified.
- `status/cleanup/text` is supported by the incomplete public account; `status/cleanup/metadata` is supported by the unresolved chronology. Both tags remain unchanged.
- Local sources support the positive `dm_notes` attestation. The `SECRET` block was reviewed and preserved; its recovery candidate is confined to the private handoff.

### Editorial assessment
**Underdeveloped** — The visible account explains Hagrim’s original fall but omits the ghostly identity and rule that define Hagrim of Morkalan and the established end of that rule. The smallest useful completion is one short account of his lost memories and rule, followed by his final defeat and the domain’s dissolution. These are established coverage gaps; no invented transition is required.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The public narrative ends at the domain’s creation and does not explain the ghostly identity behind the title. [[Session 58 (DuFr)]] and [[Morkalan]] establish that he called himself Morkalan and had relinquished his memories. Add, subject to the article’s chosen temporal treatment: “In his domain, Hagrim became a ghost who called himself Morkalan and no longer remembered his former life. He had freed himself of the memories of his past, which haunted the domain as spirits.” This supplies the central intervening state without promoting private encounter design.

- [ ] **Warning — coverage.later_material_change:** [[Session 58 (DuFr)]] records Hagrim’s final defeat on DR 1748-08-25, a defining fate absent from this account. Proposed addition: “On DR 1748-08-25, [[Riswynn]] and her companions defeated Hagrim’s ghost. Riswynn poured the waters of the [[Chalice of the Runepriest]] over his fading spirit and asked the [[Bahrazel]] to grant him redemption. His soul was sent to the gods for judgment, and Morkalan dissolved, freeing its surviving inhabitants.” The outcome of that judgment is not established. To preserve earlier filtered views, wrap only this addition in `%%^Date:1748-08-25%%` and its matching end marker. Choose whether to update the article and POV, defer under the appropriate game-update status, or intentionally retain the earlier account; no visibility block or status change was applied.

- [ ] **Warning — correctness.cross_note_conflict:** The whereabouts entry starts Hagrim’s home in Morkalan in DR 1571, but [[Chalice of the Runepriest#History of the Chalice]] dates the rescue expedition and Morkalan’s creation to DR 1575-09-19, corroborated by [[Morkalan]] and [[Dworic]]. If that chronology is adopted, replace the Morkalan entry with `{type: home, start: 1575-09-19, location: Morkalan}`. Separately clarify whether `died: 1748` intentionally records his ghost’s final defeat or should record his mortal death in 1575; both deaths must be distinguished in the account. No dates were changed automatically.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `HAH-grim ov MOR-kah-lahn` in `Metadata:names:v1`. [[Languages]] supplies Tolkien Dwarvish as the personal-name analogue: the proposal uses open a, short i, hard g and sounded r, with tentative initial stress. No adopted pronunciation of the domain name was found, so MOR-kah-lahn is a cautious spelling reading. If accepted, copy the full pronunciation to frontmatter and mark the primary entry `documented`; otherwise revise it.

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Hagrim of Morkalan]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Main Quest - Riswynn Solo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/NPCS of Morkalan/Delg Firebrand]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Session 2 - Riswynn]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/The Domain of Morkalan/Lost Camps]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/The Domain of Morkalan/The Ashfields]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/The Domain of Morkalan/The Domain of Morkalan]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Timelines - Solo Arcs]]
%%^End%%

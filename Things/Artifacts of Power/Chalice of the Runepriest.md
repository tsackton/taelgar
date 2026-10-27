---
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
displayDefaults: {wOrigin: "<start:u> in <startDate> <origin:3rq>", wCurrent: "Current location: <current:3r>", dCurrent: ""}
tags: [object, testcase, status/check/lint]
typeOf: chalice
ancestry: dwarven
created: 1547
rarity: unique
name: Chalice of the Runepriest
whereabouts:
  - {type: home, end: 1547, location: Bahrazel}
  - {type: away, start: 1548, end: 1570, location: Tharn Todor}
  - {type: away, start: 1570, end: 1748-10-04, location: lost}
  - {type: away, start: 1748-10-05, end: 9999, location: Tharn Todor}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

%%
Whereabouts dates:
dates are approx prior to 1748
%%

![[chalice-of-the-runepriest.png|right|400]]An elaborate rune-carved chalice of ambiguous origin, revered as a sacred national treasure by the dwarves of Nardith. It is rumored to have many powers, including the power to heal all wounds and illness and the power to magically provide food, water, and shelter to all who need it.

It was found when the [[Dwarves]] fleeing the destruction of the kingdom of [[Ardith]] at the end of the [[Great War]] reached the [[Yuvanti Mountains]], located in a chamber already carved and prepared deep beneath the ground, reminiscent of [[Heart of the Mountain]]. When it was first found, it flowed with salt water (some say, the tears of the [[Bahrazel]]; others a memory of the ocean that once covered the land). This became the site where [[Tharn Todor]] was constructed. 

## History of the Chalice
- (DR:: 1547): The Chalice of the Runepriest is discovered by dwarven refugees from [[Ardith]], while exploring the newly risen Yuvanti Mountains. 
- (DR:: 1575-03): The Chalice of the Runepriest is carried north by an expedition under the leadership of Hagrim Firebrand to search for survivors among the ruins of [[Ardith]]. 
- (DR:: 1575-05): The Chalice provides protection and healing for soldiers and refugees alike, and many hundreds of dwarves are rescued. 
- (DR:: 1575-08): The Chalice of the Runepriest sustains the refugees of [[Ardith]] and their rescuers on the long march south.
- (DR:: 1575-09-14): A fire giant, [[Odim Mavdyrson]], attacks dwarven refugees from [[Ardith]] and the warrior mission sent to find them, on the Dunmari [[Varashan|plains north of Tokra]]. The dwarves flee, constructing hasty fortifications around the [[Stoneborn Statue Dungeon]] on the Dunmari plains
- (DR:: 1575-09-19): [[Odim Mavdyrson]] attacks the fortifications, breaking through. The leader of the dwarves, Hagrim Firebrand, turns on his companions as Odim approaches, creating the Shadowfell domain of [[Morkalan]] in death, and dragging the surviving dwarves to this realm with him. The chalice is abandoned in the fortifications surrounding the [[Stoneborn Statue Dungeon]].
- (DR:: 1747-12-05) A group of Chardonian treasure hunters arrives at the ancient [[Stoneborn Statue Dungeon]] and finds a major cache of Dwarven relics hidden nearby, including the Chalice of the Runepriest. Two of them -- Vita, an archer, and Caius, a skirmisher -- are pulled into [[Morkalan]].
- (DR:: 1747-12-15): The Chalice of the Runepriest passes through [[Songara]], carried by Chardonian treasure hunters 
- (DR:: 1748-01-15): Rumors reach Riswynn Brawnanvil and other dwarves of [[Nardith]] in the Yuvanti Mountains that treasure hunters are seeking ancient artifacts among the ruins of [[Ardith]], including rumors that the Chalice of the Runepriest has been recovered.
- (DR:: 1748-02-04): The Chalice of the Runepriest arrives in Chardon
- (DR:: 1748-04-11): The Chalice of the Runepriest is purchased by [[Galen]] for his private study
- (DR:: 1748-08-23): Galen agrees to sell the Chalice of the Runepriest to Riswynn, a dwarf of Nardith
- (DR:: 1748-08-24): Riswynn purchases the Chalice of the Runepriest for 8000 gold pieces and a minor magic item, a Black Light Candle from [[Agata's Treasure]]. Riswynn attempts to use the chalice to teleport [[Dunmar Fellowship]] to safety, but is instead transported to the [[Heart of the Mountain]]
- (DR:: 1748-08-25): Riswynn and companions [[Session 56 (DuFr)|take the Chalice of the Runepriest into Morkalan]], where they use it to destroy [[Hagrim]] and the shadowfell domain of [[Morkalan]]
- (DR:: 1748-10-05): The Chalice of the Runepriest is returned to its rightful place in [[Tharn Todor]]

%%^Metadata:names:v1%%
- {name: Chalice of the Runepriest, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of the chalice, with dated history through its return to Tharn Todor in DR 1748; its origin remains uncertain, and the dated whereabouts and narrative chronology require reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- With explicit approval, moved the unchanged annotation “dates are approx prior to 1748” from YAML to a hidden comment below the complete header, labeled as referring to the whereabouts dates; normalized the now-safe frontmatter without changing its values.
- Added `knownTo: [dufr]`, supported by the artifact's recovery and use in [[Session 49 (DuFr)]], [[Session 56 (DuFr)]], and [[Session 58 (DuFr)]].
- Added primary name metadata and a broadly modern retrospective POV with its coverage limits.
- Corrected “A elaborate” to “An elaborate,” “fortifications surrounded” to “fortifications surrounding,” and “use it destroy” to “use it to destroy.”

### Validated judgments
- The description and dated history provide a sufficient account of the artifact's religious role, loss, recovery, and return; an invented explanation of its ambiguous origin is not required.
- The plain-English title needs no pronunciation; its in-world name language remains unestablished.
- [[Session 46 (DuFr)]] corroborates the discovery tradition; [[Session 49 (DuFr)]] corroborates the purchase and transportation; [[Session 58 (DuFr)]] records the redemption and return chronology.
- Confirmed local source clusters support the positive `dm_notes` attestation; no private contents have been placed in this report.

### Open findings

- [ ] **Warning — temporal.internal_conflict:** The whereabouts list places the chalice in Tharn Todor only through DR 1570 and marks it lost from 1570 through 1748-10-04. The article instead describes an expedition in 1575, loss on 1575-09-19, recovery on 1747-12-05, and subsequent possession in Chardon and by Riswynn. The annotation that pre-1748 dates are approximate does not resolve the confirmed 1748 custody conflict. Choose the governing chronology and rebuild the affected whereabouts intervals without changing the dated account silently. If the article's loss and recovery dates are accepted, the replacement lost interval is `{type: away, start: 1575-09-19, end: 1747-12-04, location: lost}`; the pre-loss and post-recovery intervals also require reconciliation. [[Session 49 (DuFr)]] independently establishes Riswynn's acquisition on 1748-08-24, and [[Session 58 (DuFr)]] establishes the return journey and arrival at Tharn Todor on 1748-10-05.

- [ ] **Warning — correctness.internal_conflict:** The opening calls the chalice's origin ambiguous, and the first dated entry records discovery in DR 1547, while `created: 1547` and the first `home` relationship to Bahrazel encode a definite creation date and divine maker under [[Metadata Specification#Whereabouts Specification]]. [[Session 46 (DuFr)]] supplies a discovery tradition, not an established manufacture date or maker. Confirm whether the metadata expresses separately adopted canon; if only the discovery is established, remove `created: 1547` and `{type: home, end: 1547, location: Bahrazel}` while retaining the discovery entry and qualified prose. No origin metadata was changed automatically.

- [ ] **Warning — correctness.cross_note_conflict:** The historical battle is dated DR 1575-09-19 here and supported by [[Dworic]]'s captivity chronology, but [[Hagrim]] starts his home in Morkalan in 1571, while [[Odim Mavdyrson]] dates his death in that same battle to 1590. Reconcile the linked references around one accepted chronology. If this article's 1575 date governs, the cross-note candidates are Hagrim's `{type: home, start: 1575-09-19, location: Morkalan}` and Odim's `died: 1575-09-19`; otherwise identify the evidence for revising this article's dated sequence. The linter has preserved every conflicting date.

- [ ] **Warning — correctness.cross_note_conflict:** This article places Hagrim's defeat and Morkalan's destruction on DR 1748-08-25, matching [[Session 58 (DuFr)]]'s defeat timeline; [[Morkalan]] instead has `destroyed: 1748-08-26`. Session 58 separately dates emergence onto the material plains to August 26. Confirm whether the realm ceased to exist at the defeat or at the later emergence. If the former, the candidate for the realm note is `destroyed: 1748-08-25`; if the latter, split this article's final confrontation and realm destruction into distinct dated statements. No date was selected automatically.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chalice of the Runepriest (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Main Quest - Riswynn Solo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Riswynn Solo Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Session 2 - Riswynn]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Riswynn (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 100 - DM Notes]]
%%^End%%

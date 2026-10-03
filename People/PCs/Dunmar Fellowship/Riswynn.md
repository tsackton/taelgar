---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: Nardith
campaignInfo: null
born: null
gender: female
player: Kate Sackton
name: Riswynn
affiliations:
  - {org: Dunmar Fellowship, type: primary}
  - {org: Brawnanvils, type: primary}
knownTo: [dufr]
dm_owner: player
dm_notes: important
POV: 1748
---
# Riswynn
>[!info]+ Biographical Info  
> A [[Nardith]] [[Dwarves|dwarf]] (she/her), of the [[Dunmar Fellowship]], and the [[Brawnanvils|Brawnanvil Clan]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

> [!image|right standard]
> ![[riswynn-intro-ikrams-courtyard.webp]]
> *Riswynn meets the Dunmar Fellowship at Ikram's.*
## Pre-Campaign Events
- (DR:: 1748-03-10): Riswynn leaves Tharn Todar, heading north for Raven's Hold
- (DR:: 1748-03-24): Riswynn leaves Askandi, heading for Karawa.
- (DR:: 1748-04-26): Riswynn arrives in Tokra.
- (DR:: 1748-04-30): Riswynn arrives in Askandi.
- (DR:: 1748-05-05): Riswynn arrives in Tharn Todor.

%%^Metadata:names:v1%%
- {"name": "Riswynn", "language": "unknown", "pronunciation": "RISS-win", "status": "proposed", "notes": "Riswynn appears in the [[Dwarves]] female-name list. The [[Languages]] analogue is Tolkien Dwarvish: the proposal uses an articulated r, voiceless s, and consonantal w. Short i-like vowels for i and y and first-syllable stress are tentative adaptations because no name-specific vowel or stress rule is recorded."}
- {"name": "Riswynn Brawnanvil", "role": "alias", "language": "unknown", "pronunciation": "RISS-win BRAWN-an-vil", "status": "proposed", "notes": "The full form is recorded in [[Session 6 (DuFr)]]. Riswynn follows the primary proposal; Brawnanvil follows the ordinary trade-tongue clan-name rendering described in [[Dwarves]], with English brawn and anvil. The complete form’s source language and accepted pronunciation are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a spring DR 1748 itinerary and portrait at the beginning of Riswynn’s travels with the Dunmar Fellowship; it does not describe her later achievements or continuing quests.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting without changing existing values.
- Added `knownTo: [dufr]` from the existing Fellowship affiliation and the introduction in [[Session 6 (DuFr)]].
- Added name metadata for Riswynn and the attested full form Riswynn Brawnanvil, with proposed pronunciations and their derivation.
- Recorded the article’s spring-1748 viewpoint and coverage limits in `POV` and `povNotes`.

### Validated judgments
- The principal missing dimensions are established in shared reference, campaign, and source records; incidental encounters and combat actions do not require a session-by-session biography.

### Editorial assessment
**Underdeveloped**. The visible article records affiliations and five spring-1748 travel entries, but omits Riswynn’s clerical vocation and purpose, her defining acts of restoration, and her later Crown stewardship and unfinished quest. These are established gaps, not a request to invent a biography; the smallest useful scope is a short identity paragraph and a few dated statements of lasting consequences.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Review `RISS-win` and `RISS-win BRAWN-an-vil` in `Metadata:names:v1`. [[Dwarves]] explicitly includes Riswynn in its female-name list and describes trade-tongue clan surnames; [[Session 6 (DuFr)]] establishes the full form. The [[Languages]] Tolkien Dwarvish analogue informs an articulated r, voiceless s, and consonantal w, while short i-like vowels and initial stress remain tentative because the analogue gives no exact rule for this spelling. The surname uses ordinary English brawn and anvil. Accept or revise the proposals; on acceptance, mark the entries documented and put the accepted primary pronunciation in frontmatter. The complete forms’ source language remains unknown.

- [ ] **Warning — coverage.established_fact_missing:** The article does not identify Riswynn’s clerical vocation or explain what drives her travels. [[Dunmar Fellowship]] identifies her as a dwarven cleric, [[Brawnanvils]] calls her a champion of the Bahrazel, and her own account in [[Visions of the Sentient Ocean]] connects her divine service to mending and restoring her people’s lost connections. A bounded opening is: “Riswynn Brawnanvil is a [[Nardith]] dwarf, a cleric and champion of the [[Bahrazel]], and a companion of the [[Dunmar Fellowship]]. She understands her service as the continuing work of mending: repairing what is broken and reconnecting her people with their past.” Keep this an account of her stated purpose, without inventing childhood, training, or a new explanation of her faith.

- [ ] **Warning — coverage.later_material_change:** The spring-1748 itinerary leaves out major established consequences of Riswynn’s later life. [[Session 58 (DuFr)]] records her redemption of Hagrim and resettlement of the freed dwarves; [[Session 116 (DuFr)]] and [[Session 117 (DuFr)]] record her Crown stewardship and intervention against the chalyte trade; the Epilogues section of [[dunmar-frontier-139-session-recap]] records her continuing planar quest and the orcs’ commemoration of her. Decide whether to update the article and its POV, defer with the appropriate `status/gameupdate/dufr`, or deliberately preserve the earlier article. Copy-ready dated additions, if updating: “In DR 1748, Riswynn used the [[Chalice of the Runepriest]] to redeem [[Hagrim]] and free the dwarves trapped in [[Morkalan]]. With [[Thror]], she guided the survivors to [[Tharn Todor]] and helped them rejoin dwarven society. In May DR 1749, she became bearer of the [[Crown of Purity]], using its influence to oppose the [[chalyte]] trade and support peace between [[Dunmar]] and [[Chardon]]. She subsequently departed for another plane with companions to pursue her unfinished work concerning [[Thark]]. Lubash’s thriving orc city honored her with statues.” The epilogue’s exact in-world date is unassigned: preserve that uncertainty and leave any new visibility-changing `Date:*` blocks for human approval.

- [ ] **Suggestion — correctness.name_spelling:** The March 10 itinerary entry says “Tharn Todar”, whereas the May 5 entry and the canonical [[Tharn Todor]] note use “Tharn Todor”. Correct the first place name after review: “- (DR:: 1748-03-10): Riswynn leaves Tharn Todor, heading north for Raven's Hold”. No itinerary dates or other names need to change for this correction.
%%^End%%

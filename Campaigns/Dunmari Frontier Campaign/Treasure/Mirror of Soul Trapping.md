---
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
displayDefaults: {ltPerson: trapped in}
tags: [object, status/check/lint]
typeOf: mirror
subTypeOf: magical
rarity: very rare
name: Mirror of Soul Trapping
whereabouts:
  - {type: home, location: unknown hobgoblin wizard, linkText: by an}
  - {type: home, location: dufr}
  - {type: away, start: 1748-06-08, end: 1748-06-08, location: Karawa}
  - {type: away, start: 1748-12-05, end: 1748-12-10, location: Uzgukhar}
  - {type: away, location: Vindristjarna}
knownTo: [dufr]
POV: 1749
---
```taelgar-header
```

%%need to decide if this is a one-off item, unique, or a representative of a class of items, and refactor text as appropriate; also maybe remove the game mechanics to a D&D Beyond link %%

![[mirror-of-soul-trapping-v1.jpg|right|400]]This 4’ heavy silvered mirror, weighing around 50 lb, is made of solid metal, polished to a silvered reflective surface on one side. The back side is etched in numerous strange languages, which [[Delwath]] understood to be incantations binding twelve extradimensional cells to the mirror.

An extradimensional cell is an infinite expanse filled with thick fog that reduces visibility to 10 feet. Creatures trapped in the mirror's cells don't age, and they don't need to eat, drink, or sleep. A creature trapped within a cell can escape using magic that permits planar travel. Otherwise, the creature is confined to the cell until freed. If the mirror is destroyed, all creatures trapped within are released.

Any creature that sees its reflection in the mirror while within 30 feet of it must make a DC 15 Charisma save or be trapped in one of the cells. This saving throw is made with advantage if the creature is aware of the nature of the mirror. 

%%^Campaign:dufr%%
Seen in [[Mirror of the Past]]: 

![[Mirror of Soul Trapping Vision]]
#### Command Words
The mirror can be controlled by command words, which must be spoken within 60 feet of the mirror to function, and require an action to invoke. You know five command words: 

1) When spoken, allows you to activate or deactivate the trapping function of the mirror. Learned in [[Session 32 (DuFr)]]. 
2) When spoken, allows you to release a creature contained in one cell which you identify by number. Learned via Identify when mirror was first discovered, in [[Session 30 (DuFr)]]. 
3) When spoken in combination with the name of a creature in the mirror, allows you to summon the named creature to the surface, which allows you to speak with them. The mirror must be inactive for this command to function. Learned in [[Session 32 (DuFr)]]. 
4) When spoken in combination with the number of a cell, allows you to summon the creature in that cell to the surface, which allows you to speak with them. The mirror must be inactive for this command to function. Learned in [[Session 49 (DuFr)]].
5) When spoken in combination with two cell numbers, allows you to open a portal between the two cells indicated by number. You currently do not know a way to close this portal. Learned in [[Session 49 (DuFr)]]. 

You sense there may be other command words, but further study or research on the item would be required to learn them.
#### Occupants
Current occupants of the mirror are:

1. [[Revaka]], a hobgoblin, trapped by [[Agata]] / [[Szoltar|Szoltár]], a hobgoblin soldier from the [[Iron Fang]], trapped in [[Session 130 (DuFr)]]
2. (removed when cells holding Revaka and Szoltar)
3. A wyvern, trapped in [[Session 43 (DuFr)]]. 
4. Kinzal mage and messenger, trapped in [[Session 96 (DuFr)]]
5. empty
6. (removed when the cells holding Valius and Vargus were merged)
7. [[Antonia]], trapped in [[Session 78 (DuFr)]]
8. empty
9. empty
10. empty
11. empty
12. empty

#### Former Occupants
- A poison troll, trapped in [[Session 45 (DuFr)]], was released in the [[Shadowkeep]] in [[Session 96 (DuFr)]].
#### Research Notes

[[Seeker]] and [[Delwath]]’s research in [[Karawa]], early June 1748:

[[Seeker]] and [[Delwath]] spend a day poking around at the mirror, studying it, trying to learn as much as possible about how it works.

The first clue comes from realizing that there are hidden letters, in Goblin, etched on the back of the mirror, that seem to be more bindings and enchantments that control the ways the extradimensional prison cells are accessed. You had already noted the scripts and enchantments that created the cells themselves, but this is new.

However, it takes a long time to figure out how to translate this into action. After some careful trials, you discover command words 1 and 3. 

You feel that this is not all the secrets of the mirror, but you have exhausted what you can learn by examination and trial alone, you would need to do research on magic mirrors, hobgoblin magic, extradimensional prisons, or similar topics to learn more.

[[Seeker]]’s research in [[Chardon]], August 1748. 

Reading the book that Ulfgar got for you from the [[Great Library]] on magical mirrors, their construction and use, you learn command words 4 and 5. 

%%^End%%

%%SECRET[v2:cdb45d349a56af3d4ffb10fd4b5465aa]%%

%%^Metadata:names:v1%%
- {name: Mirror of Soul Trapping, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 campaign inventory incorporating Session 130, with research notes from DR 1748; the occupant list mixes states from different sessions and is not a continuous history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added the explicit object name and `knownTo: [dufr]` from the existing campaign account.
- Added a minimal name entry; this plain-English descriptive title needs no pronunciation, and its in-world name language is unestablished.
- Added DR 1749 POV and temporal-coverage metadata for the inventory incorporating Session 130.
- Canonicalized the equivalent campaign marker `DuFr` to `dufr`.
- Corrected `solider` to `soldier` and `was released at in the` to `was released in the`.

### Validated judgments
- The SECRET block was reviewed separately and remains unchanged; its contents are excluded from this report.
- The header comment preserves unresolved editorial choices rather than a developed public account; it remains unchanged.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** Occupants row 1 says Revaka was trapped by Agata. [[Session 32 (DuFr)]] records Revaka's account that [[Cha'mutte]] imprisoned her, and the embedded [[Mirror of Soul Trapping Vision]] depicts the same event. Reconcile that attribution while retaining the separate information about Szoltár. Copy-ready replacement for the Revaka clause: `[[Revaka]], a hobgoblin trapped by [[Cha'mutte]]`. The conflicting attribution has been preserved for human review.
- [ ] **Warning — coverage.later_material_change:** The current list incorporates Szoltár's confinement and cell merger in [[Session 130 (DuFr)]], but row 3 still lists the wyvern: [[Session 120 (DuFr)]] records its release and taming at [[Sunwine Hall]] in early June 1749. Row 4 also asserts the Kinzal messenger remains confined, although [[Session 97 (DuFr)]] records a scribe's belief that he could have returned home using a return stone; that is reported uncertainty, not proof of escape. Reconcile these states before using this as a current inventory. For the established wyvern change, replace row 3 with `3. empty` and add under Former Occupants: `- A wyvern, trapped in [[Session 43 (DuFr)]], was released and tamed by [[Wellby]] at [[Sunwine Hall]] in [[Session 120 (DuFr)]].` For the unresolved mage, use `4. Occupancy unconfirmed: the Kinzal mage and messenger was trapped in [[Session 96 (DuFr)]], but a scribe suggested in [[Session 97 (DuFr)]] that he could have returned home using a return stone.` Human choice remains whether to update the inventory and its temporal frame, defer with `status/gameupdate/dufr`, or preserve an explicitly historical inventory. If keeping a broadly modern mechanics article, a dated inventory may be isolated with `%%^Date:1749-08-07%%` before the Occupants heading and `%%^End%%` after the revised list; adding that visibility-changing block requires human approval.
- [ ] **Suggestion — editorial.prose_clarity:** Occupants row 2, `(removed when cells holding Revaka and Szoltar)`, ends before stating what happened and leaves the numbering unclear. [[Session 130 (DuFr)]] records that Szoltár's cell was merged with Revaka's. Complete the existing explanation without renumbering the cells: `2. (merged with cell 1, joining [[Revaka]] and [[Szoltar|Szoltár]], in [[Session 130 (DuFr)]])`.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo: []
born: 1714
gender: male
died: null
name: Frankar
whereabouts:
  - {type: home, start: "", end: 1730, location: Darakan}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Frankar
>[!info]+ Biographical Info
> a [[Dwarves|dwarf]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% should add campaign info, maybe cleanup whereabouts to reflect Philosopher's guild information %%

A dwarf from the city of Darakan, in the kingdom of [[Khatridun]], fascinated with mechanical devices and runic magic. 
%%^Date:1730%%
Mysteriously vanished in a storm in DR 1730.  
%%^End%%
%%^Campaign:dufr%%
[[Seeker]]'s brother. [[Seeker]] told his story on [[Session 17 (DuFr)|April 16, 1748]], after surviving the storms caused by Hralgar around Stormcaller Tower. 

### Seeker's Story of Frankar

"I have a younger brother. Or had, I do not know for certain. Frankar was his name. We called him Frank. I was thinking of him in the storm. And all those days he spent hunting salamanders.  
  
A wonderful prodigy, as a child wise beyond his years, memorized the architectural histories, could draw a diagram of the great keep from memory, the pride of our parents.  
  
A talent in runic magic as well, once in a generation, fluent with the symbols, like a conductor of an orchestra but his musicians were the arches of stone.  
  
He became obsessed with being perfect. And obsessed, as well, with a game that he had invented. A dangerous game, a kind of divination, but without the gods I think, a way or so he thought, to know what lay ahead. So he could never fail in his tasks. It was a kind of machine, made of stone wheels, and bits of crystal and gemstone, animated by magic. But an evil machine. It was like the face of a great clock. And in it he would place a tiny white salamander, a blind creature, rare and elusive, you only find them deep underground. He was always hunting them.  

And the salamander would enter the clock at its center, and crawl about, sealed inside, seeking a way out. And around the face of the clock were 12 little passages. If the salamander went this one way out, it would be frozen. Another way, and it would be crushed between stones. Another way and a blade would slice it, or it would be suffocated in a jar, or shocked by lightning, and so on.  
  
And depending on the fate of the salamander, he would know his future. If the salamander was crushed, then some crushing weight would come. If it was stabbed, perhaps a heartbreak would come, or perhaps some great insight. Who knows if it really worked.  
  
The machine was a secret, you see. He hid it carefully from all of us.  We only learned about it one morning, the morning after the night of a great raging storm. We found the machine at the top of the keep, high above the mountain, all in pieces. And by careful study and reconstruction I determined what it was, and what it had been for. Or so we think. Frankar, my beloved little brother Frank, was gone- we do not know where he went, and we have not seen him since. The only clue he left us was a tiny white salamander, burned to a crisp."
%%^End%%

%%^Metadata:names:v1%%
- {name: Frankar, language: unknown, pronunciation: "FRAHN-kar", status: proposed, notes: "Pronunciation proposal informed by the Dwarvish naming analogue in Languages: open ah vowels, a hard k, audible r consonants, and initial stress. The name's language and exact in-world phonology are not established."}
- {name: Frank, role: nickname, language: unknown, status: documented, notes: "Seeker's quoted story records this family nickname."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern origin and interests, with a dated disappearance and Seeker's DR 1748 recollection; the article does not yet include later reports about Frankar's survival or whereabouts.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting without changing existing values.
- Added `knownTo: [dufr]` from the existing account of Seeker telling the party about Frankar, and canonicalized the equivalent campaign marker to `dufr`.
- Added persistent name metadata, including the documented nickname Frank and a proposed pronunciation for Frankar.
- Added `POV: modern` and a temporal-coverage note describing the durable reference frame and the dated recollection.

### Validated judgments
- The disappearance date and relationship to Seeker agree with [[Seeker]] and [[Session 17 (DuFr)]]. The quoted recollection remains an attributed historical account, not an assertion that later reports never occurred.
- `status/cleanup/metadata` remains supported: the authored reminder about whereabouts still requires a human decision in light of later reports. The tag is preserved.
- Confirmed local evidence supports the existing positive `dm_notes` attestation; its value is preserved. Private contents are not reproduced here.
- The ordinary comment is an unresolved editorial reminder, not a public prose candidate.

### Editorial assessment
**Underdeveloped**: the note omits later reported survival and whereabouts, a central dimension of its account of Frankar as Seeker's missing brother. Add the bounded, attributed later evidence below; do not invent the intervening history, resolve captivity, or turn a vision into a confirmed current location.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.later_material_change:** [[Session 84 (DuFr)]] records the Guild's statement that Frankar is alive; [[Philosopher's Information Concerning Frankar]], received in [[Session 85 (DuFr)]] on DR 1749-01-08, reports an earlier sighting in Bronzehall with Zephyra. The finalized Session 135 beat facts (`_sessions/dunmar-frontier/dunmari-frontier-135/cleaned/dunmari-frontier-135-beat-facts.json`, beat-003, DR 1749-09-16) additionally record a vision of Frankar with an unidentified efreeti approaching a flaming chalice. These materially change the missing-person account and should not be reduced to incidental campaign appearances. Human choice: adopt an attributed update and review the whereabouts metadata, defer it with the appropriate `status/gameupdate/dufr` state, or explicitly preserve the earlier account. Copy-ready candidate, to add inside the existing `Campaign:dufr` block after Seeker's story, with the first paragraph in a proposed `Date:1749-01-08` block and the second in a proposed `Date:1749-09-16` block (new date blocks require human approval):

  > The [[Ancient and Honorable Guild of Philosophers]] [[Philosopher's Information Concerning Frankar|reported]] that Frankar had been seen alive in [[Bronzehall]] on the [[Elemental Plane of Fire]], at least five years before DR 1749. He was traveling with the [[Efreeti|efreeti]] [[Zephyra]] toward the [[Cinder Wastes]], though whether he accompanied her willingly or as a captive was unknown. Some witnesses claimed they sought knowledge of the [[Oracle's Pyre]].

  > A later vision seen by [[Seeker]] showed Frankar with an unidentified efreeti approaching a great flaming chalice. The vision did not establish his current whereabouts or whether he was free.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the stored proposal `FRAHN-kar`. The Dwarvish naming analogue in [[Languages]] informs the open ah vowels, hard k, audible r consonants, and initial stress; these are proposed adaptations, not documented rules for this name. Its language remains `unknown` because dwarven identity alone does not establish the language of the name. If accepted, use `pronunciation: FRAHN-kar` in frontmatter and change the primary name entry to `status: documented`; the ordinary nickname Frank needs no pronunciation guide.

### DM evidence
- [[_DM_/Brainstorming/Short Adventure Ideas (2025-2026)]]
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Taelgar Interlude Planning]]
- [[_DM_/_Campaign 3/Dunmar Epliogue - Campaign 3 Timing]]
- [[_DM_/_Dunmari Frontier/Brainstorming - DM]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Arrival]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Solo Quests]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Session 0.75 Planning Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Arc Outline - The Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Arc Outline]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 79 - DM Notes]]
%%^End%%

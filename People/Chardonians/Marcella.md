---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/text, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, person: Delwath, date: 1748-10-23, type: scryed}
born: 1718
gender: female
name: Marcella
whereabouts:
  - {type: home, end: 1748-07-01, location: Chardon}
  - {type: away, start: 1748-10-23, location: "Ausson's Crossing", wLastKnown: ""}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Marcella
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Scryed by [[Delwath]] on October 23rd, 1748 in [[Ausson's Crossing]], [[Laicon]], the [[Refounded Alliance of Aurbez]] %%^End%%

%% #end is approx %%
%% need to fix whereabouts, campaign info, away dates %%
%% fix text to change session links %%
%% might resurface if dunmar group ever goes to Aurbez area %%

A nondescript Chardonian woman, short brown hair and a plain face. An archer, skilled with a bow, wears well-tended leather armor under a traveling cloak. 

Traveled uneasily with [[Kadmos]], [[Hektor]], [[Casian]], and [[Antonia]]. 

Felt forced to try to steal from party in [[Session 44 (DuFr)]], but when given the push by [[Wellby]] to flee for herself at the end of battle figures out how to make her escape. Disappears when [[Kadmos]] and company are fighting [[Kobolds]] in the [[Myraeni Gap]], heading for the Stoneborn and then Sembara. 

![[marcella.png|500]]

%%SECRET[v2:584534ea4bc260ef7a1dff1e40e1ff9f]%%

%%^Metadata:names:v1%%
- {name: Marcella, language: Chardonian, pronunciation: mar-KEL-lah, notes: "Proposed from Chardon's more Latinate Chardonian analogue: classical Latin keeps c hard before e and stresses the second syllable; Italian-influenced speech could give mar-CHEL-lah. Exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait centered on Marcella's uneasy service with Kadmos's company and her subsequent escape; her later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting, relocating the exact inline approximate-date comment below the header; added `knownTo: [dufr]`, persistent Chardonian name metadata, and DR 1748 POV metadata.

### Validated judgments
- [[Session 42 (DuFr)]] through [[Session 50 (DuFr)]] corroborate Marcella's uneasy service with Kadmos's company, her attempted theft, and her DR 1748 escape.
- [[Session 129 (DuFr)]] and [[Session 130 (DuFr)]] establish that Marcella later settled in the [[Refounded Alliance of Aurbez]] and found a steadier life among the [[Rangers]].
- The existing `status/cleanup/text` and `status/cleanup/metadata` tags remain supported by the visible prose and unresolved temporal metadata.
- Confirmed local-only sources support the positive `dm_notes: important` attestation, and the `SECRET` block was reviewed; private contents remain outside this shared report.

### Editorial assessment
- **Underdeveloped**: the visible article ends with Marcella's DR 1748 escape and omits her established DR 1749 life among the Rangers, her settlement in Aurbez, and her role rallying aid against the Iron Fang.

- Discussion research: multiple non-Staging Worldbuilding notes discuss this subject. Query `_scripts/worldbuilding_discussion_index.json` before developing the missing material.

### Open findings
- [ ] **Warning — coverage.later_material_change:** [[Scrying Delwath Tollen Downtime]], [[Session 129 (DuFr)]], and [[Session 130 (DuFr)]] establish that Marcella reached Aurbez, joined the Rangers, settled on the plateau, and helped rally aid against the Iron Fang in DR 1749. Choose whether to update the article and `POV` to 1749, defer the update and add `status/gameupdate/dufr`, or intentionally preserve the DR 1748 historical snapshot. For an update, add: `After escaping Kadmos with Wellby's aid, Marcella crossed the mountains into the Refounded Alliance of Aurbez and joined the Rangers. By DR 1749, she had settled on the Aurbez Plateau, where she helped patrol the Plaguelands and rallied aid against the approaching Iron Fang host.`
- [ ] **Warning — metadata.whereabouts_temporal_ambiguity:** The `1748-10-23` away entry identifies [[Ausson's Crossing]], and the generated campaign line repeats that exact place, but [[Scrying Delwath Oct 21]] establishes only that Delwath saw Marcella approaching an unrecognized inn complex at a crossroads during October 21–25. Verify a separate source for the exact date and location; otherwise replace the exact location and date with a bounded description supported by the scrying record.
- [ ] **Warning — editorial.prose_clarity:** The opening uses fragments and a long sentence whose shifting tense obscures the sequence from coerced theft to escape. Replace the three visible prose paragraphs with: `Marcella is a nondescript Chardonian woman with short brown hair and a plain face. A skilled archer, she wears well-tended leather armor beneath a traveling cloak. She traveled uneasily with [[Kadmos]], [[Hektor]], [[Casian]], and [[Antonia]]. Feeling compelled to steal from the Dunmar Fellowship in [[Session 44 (DuFr)]], Marcella later acted on [[Wellby]]'s encouragement to flee. She escaped while Kadmos and the others fought kobolds in the [[Myraeni Gap]], heading toward the Stoneborn and eventually Sembara.`
- [ ] **Warning — metadata.names_unresolved_status:** The new Marcella name entry records `mar-KEL-lah` as a proposed pronunciation. It follows Chardon's more Latinate Chardonian analogue by keeping `c` hard before `e` and stressing the second syllable; Italian-influenced `mar-CHEL-lah` remains plausible. Review the proposal; if accepted, change the entry to `status: documented` and add `pronunciation: mar-KEL-lah` to frontmatter.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Old Trade Road]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Empress of Chaos Adventure]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Isingue Arc Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Plaguelands Adventure]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 130 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 132 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 133 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 134 - DM Notes]]
%%^End%%

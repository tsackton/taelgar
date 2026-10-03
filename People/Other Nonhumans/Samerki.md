---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed, boxInfo: "<subspecies> (<species>), <pronouns>", wPast: ""}
tags: [person, status/check/lint]
species: giant
subspecies: oni
campaignInfo:
  - {campaign: dufr, type: killed, date: 1748-05-29}
born: null
gender: male
died: 1748-05-29
name: Samerki
whereabouts:
  - {type: home}
  - {type: home, location: Garamjala Desert}
  - {type: away, start: 1748-02-08, end: 1748-05-29, location: Shakun’s Wellspring}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1740s
---
# Samerki
>[!info]+ Biographical Info  
> oni ([[Giants|giant]]), he/him  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Killed by the [[Dunmar Fellowship]] on May 29th, 1748 in [[Shakun’s Wellspring]], the [[Red Mesa]], [[Eastern Dunmar]] %%^End%%

A servant of [[Agata]]. 

%%SECRET[v2:200f4d510da173340309a26554947e11]%%

%%^Metadata:names:v1%%
- {name: Samerki, language: unknown, pronunciation: SAH-mehr-kee, status: proposed, notes: "Analogue-informed proposal using the Old Norse guidance for Giant in Languages: initial stress, a as ah, e as eh, hard k, and final i as ee. The name's language, vowel lengths, and exact in-world pronunciation are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Samerki's service to Agata in the 1740s, with his death recorded in DR 1748; the beginning of that service is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter layout and the `campaignInfo` code to `dufr`.
- Added `knownTo: [dufr]` from the existing campaign interaction and [[Session 28 (DuFr)]].
- Added a primary name entry with a proposed pronunciation, keeping the name's language unknown.
- Added `POV: 1740s` and temporal coverage for the existing account.

### Validated judgments
- Confirmed local-only sources support the positive `dm_notes` attestation; their contents remain private.
- Reviewed the SECRET block without changing its contents or visibility.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `SAH-mehr-kee` in `Metadata:names:v1`. [[Languages]] supplies Old Norse as the Giant analogue; the proposal uses first-syllable stress, `a` as ah, `e` as eh, a hard `k`, and final `i` as ee. Samerki's name language and exact phonology are unrecorded, so the cultural analogue is guidance rather than proof and vowel lengths remain uncertain. Accept or revise the proposal, record an accepted primary form in frontmatter, and mark the entry documented only after human review.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing header uses `%%^Campaign:DuFr%%`. [[Campaign Registry]] requires the lowercase code. Replace only that opening marker with `%%^Campaign:dufr%%`, preserving the contents and closing marker; the generated campaign block is left unchanged for human review.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Cintra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Lair (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Magic Items]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 28/Session 28]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Shakun's Heart Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
%%^End%%

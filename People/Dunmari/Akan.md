---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, testcase/with-whereabouts, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-03-23}
born: 1693
gender: male
name: Akan
whereabouts:
  - {type: home, location: Karawa Desert}
  - {start: 1748-03-21, end: 1748-03-23, location: Gomat Oasis, type: away}
  - {type: away, start: 1748-03-27, end: 1748-04-07, location: Karawa}
  - {type: away, start: 1748-04-07, end: 1748-04-12, location: travelling to Tokra}
  - {type: away, start: 1748-04-13, end: 1748-06-07, location: Tokra}
  - {type: away, start: 1748-06-08, end: 1748-06-15, location: travelling to Karawa}
  - {type: away, start: 1748-06-15, end: 1748-06-22, location: Karawa}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Akan
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 23th, 1748 in the [[Gomat|Gomat Oasis]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%

A Dunmari sheep herder from the area outside [[Karawa]]. Pastoralist and nomad, typical of the Dunmari in the eastern region of the country.  

%% Testcase reason: a good example of a 'with' whereabout being useful to track e.g movement of the Karawa refugees%%

%%SECRET[v2:f6930a530df9b0de0e069d78a59136c5]%%

%%^Date:1748-06-22%%
## Chronology
- (DR:: 1748-03-22): Attacked with his extended family at the [[Gomat]] oasis by enraged giant lizards. One of the few survivors. 
- (DR:: 1748-03-23): Met the [[Dunmar Fellowship]] (who [[Session 2 (DuFr)|killed the lizards]]) while returning to camp to gather supplies for the ride to [[Karawa]]. They returned his sister's amulet to him (she was killed in the giant lizard attack), helped his family recover, and made a very favorable impression. 
- (DR:: 1748-03-27): Arrived in [[Karawa]] for the [[Festival of Rebirth]].
- (DR:: 1748-04-07): Leaves [[Karawa]] with Dunmari evacuation
- (DR:: 1748-04-13): Reaches [[Tokra]]
- (DR:: 1748-06-08): Leaves [[Tokra]] to return to [[Karawa]]
- (DR:: 1748-06-15): Returns to [[Karawa]] from [[Tokra]], for the [[Feast of Bhishma]]
- (DR:: 1748-06-22): Returns to nomadic lifestyle traveling north and east of [[Karawa]] with his extended family and his diminished sheep herds. 

%%^End%%

%%^Metadata:names:v1%%
- {name: "Akan", language: "Dunmari", pronunciation: "uh-KUN", notes: "Proposed from the Hindi branch of the Dunmari Indo-Iranian guidance in Languages: both written a vowels read as short uh, with plain k and n and tentative second-syllable stress; a Persian-influenced ah-KAHN is an alternative, not an established pronunciation.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of a nomadic herder, with a separately date-gated March–June 1748 chronology; the exact Gomat attack and meeting dates remain disputed between session records.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter layout, added `knownTo: [dufr]`, and repaired the unambiguous malformed whereabouts key `type away` to `type: away`; the associated Gomat dates remain unchanged.
- Added persistent name metadata with a proposed pronunciation and a 1740s article POV; the dated chronology and its existing visibility block remain intact.

### Validated judgments
- The occupation, home region, family losses, and return to pastoral life make the reference account sufficient. The detailed chronology also serves the note’s explicit testcase purpose.
- Confirmed support for the existing positive `dm_notes` attestation; reviewed the SECRET block separately.
- The generated header is preserved; its displayed date and ordinal should be regenerated together after the chronology decision below.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `uh-KUN` in the persistent name block. The Hindi branch of the Dunmari guidance in [[Languages]] supports short, reduced “uh” vowels with plain `k` and `n`; second-syllable stress is tentative. The documented Persian alternative would instead suggest `ah-KAHN`. Neither is an established in-world pronunciation. Accept one in frontmatter and mark the entry `documented`, or supply the intended reading.
- [ ] **Warning — correctness.cross_note_conflict:** The target’s chronology, Gomat whereabouts end, and campaign meeting metadata agree with [[Session 2 (DuFr)]]: attack on March 22 and meeting on March 23, 1748. [[Dunmar Frontier - Session 02]] instead dates the attack and lizard fight to March 23 and the meeting to March 24. Confirm which chronology governs; neither source record has been declared incorrect or edited. If adopting the latter chronology, use `campaignInfo: [{campaign: dufr, type: met, date: 1748-03-24}]`, change the Gomat entry’s `end` to `1748-03-24`, and change the first two chronology dates to `1748-03-23` and `1748-03-24`. Then regenerate the header as “March 24th, 1748.” If retaining the existing dates, preserve them and regenerate the header with the correct ordinal “March 23rd, 1748.”

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 2-3/Into the Wild Part 2]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: centaur
campaignInfo:
  - {campaign: dufr, date: 1748-12-30, type: met}
born: 1703
activeYear: 1733
gender: female
name: Aurelia
whereabouts:
  - {type: home, start: 1733, location: Tollen}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Aurelia
>[!info]+ Biographical Info  
> A [[Centaurs|centaur]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 in the [[Tollen|Free City of Tollen]] %%^End%%

Aurelia is a centaur woman, originally from a migrating tribe of centaurs, who settled in [[Tollen]] in the 1730s. 

%%^Metadata:names:v1%%
- {"name":"Aurelia","language":"unknown","pronunciation":"ow-REH-lee-ah","notes":"Proposed from the qualified classical Greek naming influence for Centaur in [[Languages]]: au is treated as the classical ow diphthong and the remaining vowels as eh, ee, and ah, with proposed second-syllable stress. Centaur names are diverse; this does not establish the language or exact stress of the name.","status":"proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Aurelia living in Tollen; the article places her move in the 1730s, while Session 82 (DuFr) reports twenty years of residence by late DR 1748, leaving that starting date unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added supported name/temporal metadata; pronunciations remain proposed pending human acceptance.
- Added knownTo: [dufr] and normalized the existing campaignInfo alias to dufr.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `ow-REH-lee-ah` in `Metadata:names:v1`. Proposed from the qualified classical Greek naming influence for Centaur in [[Languages]]: au is treated as the classical ow diphthong and the remaining vowels as eh, ee, and ah, with proposed second-syllable stress. Centaur names are diverse; this does not establish the language or exact stress of the name. If accepted, copy it to frontmatter `pronunciation` and mark the name entry `documented`.
- [ ] **Warning — chronology.cross_note_conflict:** The visible article says Aurelia settled in Tollen in the 1730s, with whereabouts.start and activeYear set to 1733. [[Session 82 (DuFr)]] says that by December 1748 she had lived there for twenty years, suggesting about DR 1728. Decide whether “twenty years” is rounded and the 1733 metadata should stand, or the move should be dated approximately 1728. If the latter is adopted, use “Aurelia is a centaur woman, originally from a migrating tribe, who settled in [[Tollen]] around DR 1728,” and review whereabouts.start and activeYear together. The existing values are preserved pending that choice.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header still uses `%%^Campaign:DuFr%%`. The registry resolves it to lowercase `dufr`; use `%%^Campaign:dufr%%` for that marker, preserving the enclosed text and closing marker. The current scope marker was preserved for review.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
%%^End%%

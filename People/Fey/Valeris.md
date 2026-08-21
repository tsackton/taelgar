---
subspecies: satyr
headerVersion: 2023.11.25
lintedAt: "2026-08-21T15:54:27-04:00"
lintVersion: "3.4"
tags: [person, status/gameupdate/dufr, status/check/lint]
species: fey
name: Valeris
whereabouts:
  - {type: home, end: 1749-06-07, location: Sunwine Hall}
  - {type: away, start: 1749-06-07, end: 1749-06-12, location: Emberwine}
  - {type: away, start: 1749-06-12, end: 1749-06-14, location: Amberglow}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Valeris
>[!info]+ Biographical Info  
> A [[Fey|fey]] (satyr)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[valeris.jpg|right|300]]Valeris is a satyr, a musician and gambler, cursed to speak only the absolute truth, unable even to sugar coat his words with lies of omission. 

He is lean and rakish, with curling ram’s horns wrapped in gold rings, and half-buttoned silk shirt. His eyes twinkle with mischief he can no longer act on, and his mouth twitches constantly, but whether in irritation or the desperate effort to hold his tongue is hard to tell. 

%%
need to add details of his backstory / why he was cursed from session notes
%%

%%SECRET[v2:55600fbdf7bc3bced158b17f815cddcd]%%

%%^Metadata:names:v1%%
- {name: Valeris, language: Sylvan, pronunciation: vuh-LAIR-iss, notes: "Proposed from the spelling and the documented lyrical, partly Classical-Greek-inspired pattern for Sylvan names; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a June DR 1749 portrait spanning Valeris's time at Sunwine Hall and journey into Amberglow; his later fate is not established.
%%^End%%

%%^Lint%%
### Editorial assessment
**Underdeveloped**. The visible article omits the established origin and price of Valeris's truth curse and his established June 1749 decision to remain in Amberglow. The smallest useful development is one concise backstory paragraph from `[[Session 120 (DuFr)]]` plus one dated outcome sentence from `[[Session 123 (DuFr)]]`.

### Validated judgments
- `status/gameupdate/dufr` is supported because the campaign established a later location and purpose not represented in the visible prose.
- The ordinary comment is a source pointer for the missing backstory.

### DM evidence review
Confirmed matching private notes; contents are not reproduced:
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 121 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 122 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]

### Open work
- [ ] **Warning — coverage.established_fact_missing:** `[[Session 120 (DuFr)]]` establishes the defining cause of the curse: Valeris told a reality-altering story to undo Yasara the Golden's oath, and the price was that he could never lie again. Add a bounded account such as: "Valeris's curse began when he told a story powerful enough to undo an oath sworn by Yasara the Golden. Reality accepted the tale, but thereafter Valeris could never speak a lie."
- [ ] **Warning — coverage.later_material_change:** `[[Session 123 (DuFr)]]` establishes that after traveling with the Dunmar Fellowship, Valeris remained in Amberglow to help repair the realm and perhaps free himself of the curse. Choose whether to add this as a dated outcome and update the temporal framing, defer it while retaining `status/gameupdate/dufr`, or intentionally preserve the earlier portrait.
- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `vuh-LAIR-iss`, derived from the documented lyrical and partly Classical-Greek-inspired pattern for Sylvan names. If accepted, copy it to frontmatter and change the name entry to `status: documented`.
- [ ] **Suggestion — frontmatter.deprecated_field:** `subspecies: satyr` is deprecated. Decide whether `satyr` is the primary classification (`species: satyr`) or display wording for the broader `species: fey` classification (`typeOfAlias: satyr`), then remove the deprecated field.
%%^End%%

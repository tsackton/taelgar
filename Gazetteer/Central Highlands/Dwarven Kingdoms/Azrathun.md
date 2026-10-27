---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: ruined city
name: Azrathûn
pronunciation: AZ-rah-thoon
whereabouts: Khatridun
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

Arzathûn was once among the greatest [[Dwarves|dwarven]] cities, but it was destroyed and abandoned in the aftermath of the [[Battle of Urlich Pass]] and the [[Great War]].

%%^Campaign:none%%

nothing invented except it was a huge city / capital of dwarvendom but was destroyed in the great war. tied to downfall of Khatridun as the center of dwarven life  located somewhere under the area destroyed near Urlich Pass after Cha'mutte's death

Two possible etymologies:

(1) From Dwarvish _azra_, “a foundation stone ceremonially laid at the beginning of a great work,” and _thûn_, “an inhabited great hall” or “seat of rule.” 

(2) A compressed form of _Azar-a-thûn_: “the hall beneath Azar's protection.”

Not decided which is correct. Option (1) makes the most sense if this is a pre-Riving or "created by Firstborn" city. Option (2) might be interesting if this was the great city and fortress built to protect against the evils of the depths in the years before the Downfall. 

%%^End%%

%%^Metadata:names:v1%%
- {name: Azrathûn, language: Dwarvish, pronunciation: AZ-rah-thoon, status: documented, notes: "The shared planning block preserves two undecided Dwarvish etymologies; neither meaning is adopted here."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective identification of the ruined city after the Great War; the exact destruction date and the city’s earlier history are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded the accepted name and pronunciation in persistent name metadata, preserving the undecided etymologies.
- Closed the unmatched quotation mark in the second proposed etymology without deciding between the alternatives.
- Added the required single-location map skeleton with an unknown locator.
- Added a modern retrospective POV and temporal-coverage interpretation.

### Validated judgments
- The compact ruined-city identification performs a bounded reference role. The optional capital-context addition is recorded separately for review.
- `status/check/name` is preserved independently of name metadata; the proposed etymologies remain undecided.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The settlement requires a known map locator, but no position is supplied in the note or the consulted kingdom sources. Fill `locator` in the new `Metadata:map:v1` entry after locating the ruin; do not infer a hex merely from proximity to [[Urlich Pass]].
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found in the prepared match set; verify `dm_notes: important`. The attestation may refer to memory or another off-vault source, so it has been preserved.
- [ ] **Warning — correctness.internal_conflict:** The visible sentence begins “Arzathûn,” while the title and accepted `name` use “Azrathûn,” and [[Dwarven Kingdoms]] links this city as [[Azrathun]]. Confirm the intended spelling. If the existing display name controls, replace only “Arzathûn” with “Azrathûn” in that sentence. No name choice was applied automatically.
%%^End%%

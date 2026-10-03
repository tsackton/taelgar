---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr}
born: null
gender: male
name: Kiran
whereabouts:
  - {type: home, location: plains north of Tokra}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Kiran
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% update campaign info, whereabouts %%

A member of a family of goat herders that wander across the upper reaches of the [[Hara]] river, north of Tokra. 
%%^Campaign:dufr%%
In 1748, met [[Dunmar Fellowship]], and his family was gifted a mechanical goat of a strange clockwork design by the dwarf [[Seeker]]. 
%%^End%%

%%^Metadata:names:v1%%
- {name: "Kiran", language: "Dunmari", pronunciation: "KIH-run", notes: "Proposed from the Hindi analogue for Dunmari in Languages: short i as in sit, a reduced to uh, a light tapped r, and n approximating the Hindi name's final retroflex nasal; first-syllable prominence is an English reading aid, not established in-world stress.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of a goat herder based north of Tokra; the campaign block separately records his family's encounter with the Dunmar Fellowship in DR 1748.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter layout, canonicalized the recognized `DuFr` campaign alias to `dufr`, and added `knownTo: [dufr]`.
- Added persistent name metadata with a proposed pronunciation and a 1740s POV with temporal coverage notes.

### Validated judgments
- The family occupation, home region, and distinctive clockwork-goat connection are sufficient for this minor person’s reference role. [[Session 40 (DuFr)]] confirms his campaign-era setting; its incidental conversation does not require a further recap here.
- `status/cleanup/metadata`: not assessable. The comment does not specify what further changes the author intended; valid free-text whereabouts and an undated campaignInfo entry have been preserved.
- Confirmed attributable local evidence supporting the positive `dm_notes` attestation; the generic name-table match was rejected.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `KIH-run` in the persistent name block. Using the Hindi analogue for Dunmari in [[Languages]], `i` is short as in “sit,” `a` is reduced to “uh,” `r` is lightly tapped, and the final nasal is approximated as `n`. The capitalization is an English reading aid, not an established in-world stress rule. Accept the pronunciation in frontmatter and mark the entry `documented`, or revise it.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
%%^End%%

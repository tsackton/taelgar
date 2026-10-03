---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
campaignInfo:
  - {campaign: dufr, person: Riswynn, date: 1748-08-25, type: met}
gender: male
name: Rurik
whereabouts:
  - {type: home, location: Bleakhold}
  - {type: away, start: 1748-08-26, end: 1748-10-04, location: Central Dunmar}
  - {type: home, start: 1748-10-04, location: Tharn Todor}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Rurik
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on August 25th, 1748 in [[Bleakhold]], [[Morkalan]], the [[Shadowfolds]] %%^End%%

Rurik is a dwarf, of indeterminate age, who remembers little of his life in [[Bleakhold]] except his close connection to his son, [[Tak]], who he cares for deeply and worries over constantly.

%%SECRET[v2:3338abd16635f892bf4590a38d7827b4]%%

%%^Metadata:names:v1%%
- {"name": "Rurik", "language": "unknown", "pronunciation": "ROO-rik", "notes": "Rurik appears among the dwarf names in Dwarves. Using the Tolkien Dwarvish analogue in Languages: u as oo, short i, sounded r and k, with tentative initial stress; exact in-world phonology is not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Rurik and his relationship with Tak; the dated whereabouts record the subsequent departure from Bleakhold and journey to Tharn Todor.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo`, a subject-name block, and article `POV`/`povNotes`; normalized frontmatter.
- Corrected the visible typo “indeterminant age” to “indeterminate age”.

### Validated judgments
- The local-only SECRET block was reviewed and preserved; its useful material is already present in shared evidence. The brief father-and-son portrait is sufficient.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `ROO-rik` in `Metadata:names:v1`. [[Dwarves]] lists Rurik among dwarf names. The Tolkien Dwarvish analogue in [[Languages]] informs u as oo, short i, sounded r and k, and tentative initial stress. This is an analogue-informed proposal, not an adopted in-world rule. If accepted, copy `pronunciation: ROO-rik` to frontmatter and change the entry to `status: documented`; otherwise amend the proposal.
- [ ] **Warning — temporal.cross_note_conflict:** The final `whereabouts` entry begins residence in Tharn Todor on `1748-10-04`, but the timeline in [[Session 58 (DuFr)]] dates the freed dwarves’ arrival to October 5. Confirm whether Rurik had a separate arrival or whether this is a one-day metadata error. If he arrived with the group, replace only that entry with `{type: home, start: 1748-10-05, location: Tharn Todor}`; do not duplicate it or infer a new travel interval.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The sole mechanical candidate is an unrelated list of potential names, not evidence about this dwarf. Preserve `dm_notes: color` unless the human confirms that no useful off-vault or remembered material remains.
%%^End%%

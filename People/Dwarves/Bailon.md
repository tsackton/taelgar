---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: female
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-09}
name: Bailon
whereabouts: Tharn Todor
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Bailon
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on May 9th, 1748 in [[Tharn Todor]], [[Nardith]], the [[Yuvanti Mountains]] %%^End%%

Bailon is a mine forewoman, working in the deep mines beneath [[Tharn Todor]]. 

%%^Metadata:names:v1%%
- {"name": "Bailon", "language": "unknown", "pronunciation": "BYE-lon", "notes": "Using the Tolkien Dwarvish analogue in Languages as broad guidance: ai as eye, a short o in lon, and initial stress; the exact in-world reading is unconfirmed.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of the mine forewoman at Tharn Todor, anchored by her DR 1748 appearance; the tenure of her position is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo`, a subject-name block, and article `POV`/`povNotes`; normalized frontmatter.
- Normalized the equivalent campaign alias `DuFr` to `dufr` in `campaignInfo` and the existing header block.

### Validated judgments
- The brief occupational description is sufficient for this minor person; [[Oskar in Tharn Todor]] corroborates her role without requiring a retelling of the rescue.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `BYE-lon` in `Metadata:names:v1`. The Tolkien Dwarvish analogue in [[Languages]] is the strongest available guidance: `ai` is read as eye, the final `o` is short, and stress is provisionally initial. This is an analogue-informed proposal, not an adopted in-world rule. If accepted, copy `pronunciation: BYE-lon` to frontmatter and change the entry to `status: documented`; otherwise amend the proposal.
%%^End%%

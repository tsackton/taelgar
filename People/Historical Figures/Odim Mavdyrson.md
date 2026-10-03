---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: giant
subspecies: fire giant
born: 1500
died: 1590
gender: male
name: Odim Mavdyrson
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Odim Mavdyrson
>[!info]+ Biographical Info  
> A [[Giants|giant]] ([[Giants|fire giant]]) (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`

%%  connected to the Fire War - Chalice of the Runepriest - Dwarves of Ardith historical context in the 1550s-1590s that needs to be collated and written %%

A fire giant, the son of [[Mavdyr]] (who was killed in the [[Fire War]]). Sought [[Dwarves]] for revenge; killed in the process but not before seeing [[Hagrim]] turn on [[Nora Silverspark|Nora]].

%%^Metadata:names:v1%%
- {"name": "Odim Mavdyrson", "language": "unknown", "pronunciation": "OH-dim MAHV-dür-son", "notes": "Proposed using the Old Norse analogue for Giant in [[Languages]]: initial stress in each name, sounded v and r, an open a, and y as rounded ee (ü). Vowel lengths are not marked in the spelling, so the English-readable rendering and exact name language remain uncertain.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of Odim’s revenge and death; the battle is dated DR 1575 in the chalice chronology, while this note records a conflicting death year of 1590.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and persistent name and temporal metadata; normalized frontmatter.

### Validated judgments
- [[Session 56 (DuFr)]] and [[Session 58 (DuFr)]] support the attack on the dwarves and Hagrim’s betrayal.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The target gives `died: 1590` and says Odim was killed in the conflict where Hagrim turned on Nora. [[Chalice of the Runepriest#History of the Chalice]] dates that attack and betrayal to DR 1575-09-19; [[Session 58 (DuFr)]] connects the same battle to Morkalan’s creation. Reconcile the death year and battle chronology. If the dated chalice chronology is adopted, the candidate field is `died: 1575-09-19`; otherwise document the basis for 1590. No date was changed.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation of Odim Mavdyrson: `OH-dim MAHV-dür-son`. The Old Norse analogue for Giant in [[Languages]] informs initial stress, sounded v/r, open a, and rounded ee for y (ü). The exact name language and unmarked vowel quantities are not recorded, so this remains a proposal. The proposal is preserved in `Metadata:names:v1`; if accepted, copy it to frontmatter and mark the entry `documented`, or revise it with its derivation.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The existing `dm_notes: important` may refer to memory or off-vault material. Confirm whether useful private information remains; keep the human attestation until that review.
%%^End%%

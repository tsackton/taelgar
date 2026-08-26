---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-08-22}
born: 1701
gender: male
name: Gnaeus
affiliations: [University of Chardon, "Sibyl's Hall"]
whereabouts:
  - {type: home, location: Arendum}
  - {type: home, location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Gnaeus
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% copy stuff from OneNote, I guess mostly not secrets anymore; update whereabouts to capture Elderwood time, add campaign info %%

A disgraced historian and scholar, expelled from the Faculty for using enchantment magic to aid his research, now making a poor living as a tutor. 

Wrote [[On the Lost People of the Forests]], describing travels in his youth among the Deno'qai of the [[Elderwood]]. 

%%SECRET[v2:cd80af0aa93653bae7a13d94ffbd012b]%%

%%^Metadata:names:v1%%
- {name: Gnaeus, language: Chardonian, pronunciation: GNYE-oos, notes: "Proposed from the Latin analogue for Chardonian: initial g and n are both sounded, ae as eye, and final us as oos; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Gnaeus as a disgraced tutor, with selected early-adult research history; the intervening and later years are not comprehensively described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` and a dated Dunmar Frontier `campaignInfo` entry from [[Session 49 (DuFr)]].
- Added persistent Chardonian name metadata with the proposed pronunciation `GNYE-oos`.
- Added `POV: 1748` and a persistent temporal-coverage note.

### Validated judgments
- Confirmed local-only sources support the positive `dm_notes: important` attestation; no private contents are reproduced here.
- Reviewed the existing `SECRET` block without changing or exposing it.
- `status/cleanup/metadata` remains supported because the undated Arendum and Chardon home entries do not yet distinguish Gnaeus's childhood home from his later residence.

### Open findings

- [ ] **Warning — correctness.unsupported_certainty:** The visible article says Gnaeus was `expelled from the Faculty`, but [[On the Lost People of the Forests]], [[Session 49 (DuFr)]], and [[Sibyl's Hall]] establish only that he was disgraced for using enchantment magic and later worked as a tutor or lecturer. Verify whether a separate source establishes expulsion. If not, use: `A disgraced historian and scholar, condemned for using enchantment magic in his research, now making a poor living as a tutor.`
- [ ] **Warning — metadata.whereabouts_temporal_ambiguity:** Both `whereabouts` entries are undated `type: home`. [[On the Lost People of the Forests]] establishes Arendum as Gnaeus's childhood home, while [[Session 49 (DuFr)]] and [[Sibyl's Hall]] place him tutoring in Chardon in DR 1748. Add supported bounds or choose an explicit relationship shape that distinguishes origin from later residence; do not infer a transition date solely from the book's DR 1725 creation date.
- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `GNYE-oos` from Chardonian's Latin analogue: initial g and n are both sounded, `ae` is read as `eye`, and final `us` as `oos`. Exact in-world phonology is not established. If accepted, mark the entry `status: documented` and copy `pronunciation: GNYE-oos` to frontmatter; otherwise revise the proposal and record the chosen basis.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Session 62 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Grimbaskal - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part I To Arendum/Part I To Arendum]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Baz'aku (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Part II Finding the Te'kula]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Notes from Kassi]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 96 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

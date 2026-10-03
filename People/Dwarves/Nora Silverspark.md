---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: passed on}
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo: []
born: null
died: 1748-11-23
gender: female
name: Nora Silverspark
aliases: [Nora]
affiliations:
  - {org: Silversparks, type: primary}
whereabouts:
  - {type: away}
knownTo: [dufr]
dm_owner: none
dm_notes: important
POV: 1748
---
# Nora Silverspark
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her), of the [[Silversparks|Silverspark Clan]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% need to copy notes from OneNote, clean up campaign info; significant dwarf in the late 1500s in the aftermath of the Great War %%

A dwarven warrior, once a ghost in [[Morkalan]] and now passed on. The first victim of [[Hagrim]]'s betrayal.

%%^Metadata:names:v1%%
- {name: "Nora Silverspark", language: "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective portrait after Nora’s spirit passed on in DR 1748, with an earlier death and period as a ghost; the exact release date in the existing metadata requires reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added `knownTo: [dufr]` from the documented interaction with Riswynn and her companions.

### Validated judgments
- `status/cleanup/metadata` is supported: the release-date discrepancy and unfinished campaign/location metadata still need human disposition. The tag is preserved.
- The complete name is an obvious ordinary given name and transparent compound surname; no pronunciation is required. Confirmed local evidence supports the positive `dm_notes` attestation.

### Editorial assessment
**Underdeveloped**. The visible note gives Nora’s victimhood and final fate but omits her defining role in the lost Ardith rescue expedition and the consequential role of her testimony in the release of Morkalan. A brief historical paragraph and a sentence explaining the release would supply this established account; no additional invented biography is required.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Silversparks]] and [[Dworic]] establish Nora’s defining rescue role, while [[Session 58 (DuFr)]] establishes her testimony and release. The current two-sentence account omits those central facts. Bounded candidate: “Nora was a decorated warrior of the [[Silversparks]] who helped lead the DR 1575 expedition to rescue dwarves stranded in [[Ardith]] after the [[Great War]]. She died after [[Hagrim]] turned on her during the return journey and remained a ghost in [[Morkalan]]. In DR 1748, her account of Hagrim’s past helped [[Riswynn]] and her companions free the realm. As her spirit passed on, she gave Riswynn the [[Silverspark Gauntlets]].”
- [ ] **Warning — correctness.cross_note_conflict:** The metadata records `died: 1748-11-23` with `endStatus: passed on`, but [[Session 58 (DuFr)]] places Nora’s fading and the party’s return to the mortal world in late August, with emergence dated 1748-08-26. Confirm whether this field denotes release or physical death. If it denotes release, candidate `died: 1748-08-26` after confirming the event boundary; if it denotes physical death, use the historical battle date only once confirmed and record the DR 1748 release separately. The present date is preserved.
- [ ] **Suggestion — temporal.date_block_proposal:** The undated words “now passed on” depend on the DR 1748 release. When the release date is confirmed, isolate only the release account in a `Date:*` block if this note must also serve earlier campaign views. Copy-ready year-level candidate: `%%^Date:1748%%` followed by “In DR 1748, Nora’s spirit passed on after the freeing of [[Morkalan]].” and `%%^End%%`; use the confirmed full date instead of the year when earlier DR 1748 views matter. No visibility change has been applied.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Hagrim of Morkalan]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Main Quest - Riswynn Solo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Session 2 - Riswynn]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/The Domain of Morkalan/The Domain of Morkalan]]
%%^End%%

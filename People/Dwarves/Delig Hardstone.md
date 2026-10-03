---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo: []
born: null
gender: male
name: Delig Hardstone
affiliations:
  - {type: primary, org: Hardstones}
whereabouts: Tokra
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Delig Hardstone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Hardstones]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Patriarch of the Hardstone clan, father to [[Dag Hardstone]].

%% One Note
Father/patriach of clan
%%

%%^Metadata:names:v1%%
- {"name": "Delig Hardstone", "language": "unknown", "pronunciation": "DEH-lig HARD-stohn", "notes": "The given-name reading follows the accepted DEH-lig in [[Delig Firebrand]]; Hardstone is read as the ordinary English compound. Application to this individual remains proposed; the name language is not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Delig as the Hardstone patriarch and father of Dag; earlier and later family states are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and collection formatting.
- Added the primary name entry and persistent temporal coverage metadata.
- Added `knownTo: [dufr]` from [[Session 36 (DuFr)]], recorded `POV: 1748`, and corrected “Patriach” to “Patriarch.”

### Validated judgments
- The visible note provides a sufficient brief identification of the clan patriarch and Dag’s father.
- The local evidence clusters support the positive `dm_notes` attestation; private contents remain excluded from this report.
- `status/cleanup/metadata`: not assessable beyond the metadata repairs made here; the tag may reflect additional human intent and is preserved.
- The brief One Note comment is retained as a provenance pointer, not an additional account requiring adoption.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name entry proposes **DEH-lig HARD-stohn**. The accepted given-name pronunciation in [[Delig Firebrand]] supplies DEH-lig (eh, short i, hard g, first-syllable stress); Hardstone is the ordinary English compound. This supports a proposal for this different person, not automatic acceptance. If accepted, copy the proposed pronunciation to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal and its derivation. The name language remains `unknown` pending evidence.
- [ ] **Warning — correctness.cross_note_conflict:** The family account needs a bounded human reconciliation: [[Seeker]]’s backstory calls Delig the brother of [[Fallthra Hardstone]], whereas [[Session 36 (DuFr)]] and [[Fallthra Hardstone]] identify him as her husband; this note identifies him as Dag’s father. Preserve the current statement until the relationship is confirmed. If the session account is the intended relationship, a candidate is: “Delig is the patriarch of the [[Hardstones]], husband of [[Fallthra Hardstone]], and father of [[Dag Hardstone]].” Reconcile the conflicting backstory separately rather than silently choosing a genealogy here.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
%%^End%%

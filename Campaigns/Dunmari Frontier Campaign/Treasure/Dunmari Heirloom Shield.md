---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:26:32-04:00"
lintVersion: "3.5"
tags: [object, status/check/lint]
typeOf: armor
subTypeOf: magic
typeOfAlias: shield
ancestry: Dunmari
rarity: uncommon
name: Dunmari Heirloom Shield
knownTo: [dufr]
POV: modern
---
# The Dunmari Heirloom Shield
>[!info]+ Information  
> (uncommon [[Dunmar|Dunmari]] magical armor)  
> `$=dv.view("_scripts/view/get_Affiliations")`

An elaborate shield from the [[Great War]] era, Dunmari design, found in [[Agata]]'s hut. Subsequently reinforced by [[Jasu]], the smith in [[Karawa]], with [[adamantine]] found in the [[Dwarven Outpost (Raven's Hold)|dwarven outpost]] near [[Raven's Hold]]. Destroyed in order to recover the [[Adamantine]] to construct the phasing stone harness on [[Vindristjarna]]. 

%%SECRET[v2:f45275c315116ba22755a85dcb17a397]%%

%%^Metadata:names:v1%%
- {"name": "Dunmari Heirloom Shield", "language": "unknown", "pronunciation": "DUN-mar-ee HAIR-loom sheeld", "notes": "The Dunmar base is recorded as DUN-mar in [[Dunmar]]. The proposed demonym adds ee without changing that stress; Heirloom Shield uses ordinary English pronunciation. The complete descriptive name has no established source language.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective of the shield's Great War origin, later recovery and reinforcement, and eventual destruction; the identity of the adamantine shield mentioned after the recorded conversion needs human review.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added knownTo: [dufr] from the established campaign interactions.
- Added an explicit name where missing, a primary name entry with a proposed complete pronunciation, and POV with persistent temporal coverage.

### Validated judgments
- The item's description and provenance perform its bounded reference role; no uninvented central dimension requires development.
- The local dm_notes attestation review is not applicable because dm_owner is absent; no human attestation was added or changed.
- Reviewed the local-only SECRET block; recovery is recorded only in the private structured handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `DUN-mar-ee HAIR-loom sheeld` in `Metadata:names:v1`. The Dunmar base is recorded as DUN-mar in [[Dunmar]]. The proposed demonym adds ee without changing that stress; Heirloom Shield uses ordinary English pronunciation. The complete descriptive name has no established source language. If accepted, set frontmatter `pronunciation: DUN-mar-ee HAIR-loom sheeld` and mark the entry `documented`; otherwise supply the preferred complete reading.
- [ ] **Warning — correctness.cross_note_conflict:** The article says the shield was destroyed for Vindristjarna's phasing-stone harness. [[Session 74 (DuFr)]] dates conversion of Delwath's shield to DR 1748-11-25, but [[Session 81 (DuFr)]] later describes him showing Umli an adamantine shield on DR 1748-12-17. The later passage does not identify that shield by name. Confirm whether it is another shield or a continuity error before changing the reference account; preserve both session records. If the existing destruction account is retained, a bounded clarification is: `The shield was converted into the [[adamantine]] harness for [[Vindristjarna]]'s phasing stone on [[Session 74 (DuFr)|November 25th, DR 1748]].` Apply that clarification only after resolving the later shield's identity.
%%^End%%

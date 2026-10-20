---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:26:32-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [object, status/check/lint]
typeOf: wondrous item
subTypeOf: magical
name: "Hralgar's Eyes"
knownTo: [dufr]
POV: modern
---
# Hralgar's Eyes
>[!info]+ Information  
> (magical wondrous item)
> `$=dv.view("_scripts/view/get_Affiliations")`

A pair of giant eyes, made of stone. These are two stone eyes, a bit smaller than a human head, and very heavy. They are exquisitely and realistically carved to resemble the eyes of a giant. 

%%^Campaign:dufr%%
These eyes were taken from the statue of Hralgar in [[Stormcaller Tower]], by [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]], on a mission funded by [[Fausto]] for the [[Society of the Open Scroll]], in DR 1748. They were kept in Fausto's tower in [[Chardon]] for several months, until they were [[Session 48 (DuFr)|recovered]] by the [[Dunmar Fellowship]]. Eventually, they were returned to [[Hralgar]] as [[Session 71 (DuFr)|part of the process of freeing him from his bonds]].
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Hralgar's Eyes", "language": "unknown", "pronunciation": "HRAL-garz eyez", "notes": "The Hralgar component is recorded as HRAL-gar in [[Hralgar]] and [[Hralgar's Eyes Vision]], with language Giant. The complete possessive reading adds z and ordinary English eyes; the complete descriptive name has no established source language.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective of the stone eyes, with campaign-scoped removal, recovery, and restoration to Hralgar in DR 1748; it does not assert continued existence as separate objects after their return.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added knownTo: [dufr] from the established campaign interactions.
- Added an explicit name where missing, a primary name entry with a proposed complete pronunciation, and POV with persistent temporal coverage.
- Corrected wonderous to wondrous, removed the stray in before until, and normalized the existing campaign code to dufr.

### Validated judgments
- The item's description and provenance perform its bounded reference role; no uninvented central dimension requires development.
- The local dm_notes attestation review is not applicable because dm_owner is absent; no human attestation was added or changed.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `HRAL-garz eyez` in `Metadata:names:v1`. The Hralgar component is recorded as HRAL-gar in [[Hralgar]] and [[Hralgar's Eyes Vision]], with language Giant. The complete possessive reading adds z and ordinary English eyes; the complete descriptive name has no established source language. If accepted, set frontmatter `pronunciation: HRAL-garz eyez` and mark the entry `documented`; otherwise supply the preferred complete reading.
- [ ] **Warning — correctness.source_attribution:** The link `[[Session 48 (DuFr)|recovered]]` points to the session in which the fellowship learned who held the eyes. [[Session 49 (DuFr)]] records their actual recovery on DR 1748-08-24. Replace only that citation with `[[Session 49 (DuFr)|recovered]]`; the existing event and prose can otherwise remain unchanged.
%%^End%%

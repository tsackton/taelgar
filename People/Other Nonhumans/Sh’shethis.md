---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: elemental
ancestry: null
campaignInfo:
  - {campaign: dufr, type: freed, date: 1749-01-08, wParty: "<met:u> from the <current:1> by <person> on <target>"}
born: null
gender: null
name: Sh’shethis
whereabouts:
  - {type: home, location: Elemental Plane of Air}
  - {type: away, start: 1000, end: 1749-01-08, location: Elemental Forge}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Sh’shethis
>[!info]+ Biographical Info
> an [[Elementals|elemental]]
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Freed from the [[Elemental Forge]] by the [[Dunmar Fellowship]] on January 8th, 1749 %%^End%%

%%check/cleanup whereabouts, campaign info, ancestry and related%%

A strange creature of elemental air who was bound to the Elemental Forge in the [[Edge of Echoes]] for over 1000 years. Freed in DR 1749 by [[Dunmar Fellowship]].

%%^Metadata:names:v1%%
- {"name": "Sh’shethis", "language": "unknown", "pronunciation": "shuh-SHEH-this", "notes": "Cautious spelling-based proposal: sh in each initial cluster, a short supporting uh before the apostrophe, eh in the stressed syllable, and final th as in thin. [[Languages]] gives no determined Primordial analogue, and no name-specific pronunciation is recorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account ending with the release on DR 1749-01-08; the start of imprisonment is uncertain. The preserved author comment on the Elemental Forge whereabouts start field is: “start date is unclear”.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and canonicalized equivalent campaign codes.
- Preserved the exact start-date comment and its association with the Elemental Forge whereabouts field in povNotes, enabling safe frontmatter formatting without changing the uncertain value.
- Added a proposed name pronunciation and a modern retrospective POV.

### Validated judgments
- The role, captivity, and release are sufficient for this bounded reference entry.
- `status/cleanup/metadata` is supported: the existing start-date value conflicts with the stated duration and still needs a human decision.
- The positive dm_notes attestation has a confirmed local source.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `shuh-SHEH-this` in the primary name entry. No adopted pronunciation was found, and [[Languages]] leaves Primordial analogues undetermined. This cautious proposal reads sh normally, supplies a short uh to make the initial cluster pronounceable, places stress on SHEH, and reads final th as in thin; the inserted vowel and stress especially need confirmation. If accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`; otherwise revise the proposal.

- [ ] **Warning — metadata.relationship_date_conflict:** The Elemental Forge whereabouts starts in DR 1000 and ends in DR 1749, about 749 years, while the prose says “over 1000 years.” The author explicitly marks the start date unclear; [[Session 86 (DuFr)]] establishes ancient Drankorian captivity without an exact binding date. Confirm the intended chronology. If the numeric start is only a placeholder, the copy-ready replacement is `{type: away, end: 1749-01-08, location: Elemental Forge}`; otherwise supply a supported start or revise the duration. The uncertain value and cleanup status are preserved pending that choice.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
%%^End%%

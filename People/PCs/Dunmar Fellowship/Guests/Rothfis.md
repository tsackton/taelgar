---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
displayDefaults: {aNoDate: "Traveled with <affiliations>"}
tags: [person, status/check/lint]
species: dwarf
ancestry: null
born: null
gender: null
player: Phil Grayson
name: Rothfis
affiliations:
  - {org: Dunmar Fellowship, title: Guest}
whereabouts: Chardon
knownTo: [dufr]
excludePublish: [clee]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Rothfis
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A dwarven monk, retired adventurer, and barkeep; owner of a bar in Chardon. Summoned to repay a debt he owed through marriage, from his now ex-wife's clan, the Ironcorns. Not happy about it.

%%^Metadata:names:v1%%
- {"name": "Rothfis", "language": "unknown", "pronunciation": "ROT-fiss", "notes": "No name-specific language or pronunciation is recorded. Proposal uses the Tolkien-Dwarvish cultural naming analogue in [[Languages]], with first-syllable stress, short o and i, and th adapted as an aspirated t; this is a tentative cultural analogy, not an adopted in-world sound rule.", "status": "proposed"}
- {"name": "Rothfis Stonefist", "role": "full name", "language": "unknown", "pronunciation": "ROT-fiss STOHN-fist", "notes": "The full form is recorded in [[Session 68 (DuFr)]]. Pronunciation combines the tentative Tolkien-Dwarvish-informed Rothfis proposal with the ordinary English reading of Stonefist; the name language remains unestablished.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait at the time of the summons to repay his debt; the article does not yet incorporate the recorded return home after the Morkalan expedition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting; preserved existing non-lint status tags and human DM attestations.
- Added `knownTo: [dufr]` from [[Session 56 (DuFr)]] and recorded the DR 1748 summons viewpoint.
- Added name metadata, including the fuller form Rothfis Stonefist from [[Session 68 (DuFr)]], with proposed pronunciations.
- Corrected “a debt he owned” to “a debt he owed” and removed the stray quotation mark from the affiliation title `Guest`.

### Validated judgments
- The brief profession, home, marriage connection, and summons identify this bounded guest character adequately.
- The reviewed local evidence supports the existing positive `dm_notes` attestation; no private source contents have been copied into this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `ROT-fiss` and `ROT-fiss STOHN-fist`. [[Languages]] supplies Tolkien Dwarvish as the cultural naming analogue: the proposals use short o and i, initial stress, and th tentatively adapted as an aspirated t; Stonefist takes its ordinary English reading. This is an analogue-informed proposal, not a recorded pronunciation or proof of the name's language. Accept or correct the proposals and copy an accepted primary pronunciation to frontmatter.

- [ ] **Warning — coverage.later_material_change:** The body ends at the summons, but [[Session 56 (DuFr)]] establishes the Bahrazel's expedition into Morkalan and [[Session 58 (DuFr)]] records Rothfis's return home on DR 1748-08-26 after Hagrim's redemption. This resolves the episode introduced by the note. Human choice: incorporate the outcome and retain an appropriate POV, defer it with a human-managed game-update tag, or explicitly preserve the summons-era snapshot. Smallest proposed addition, kept unapplied because it changes filtered visibility:

```markdown
%%^Date:1748-08-26%%
After joining [[Riswynn]] on the [[Bahrazel|Bahrazel's]] expedition into [[Morkalan]] and helping redeem [[Hagrim]], Rothfis returned home.
%%^End%%
```

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Main Quest - Riswynn Solo]]
%%^End%%

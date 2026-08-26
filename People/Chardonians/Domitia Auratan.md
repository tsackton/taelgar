---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
died: 1723
name: Domitia Auratan
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Domitia Auratan
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`

The mother of the current Magistros of Chardon, [[Mitus Verina Auratan]]. Died shortly after giving birth.

%%^Metadata:names:v1%%
- {name: Domitia Auratan, role: primary, language: Chardonian, pronunciation: doh-MIT-ee-ah aw-rah-TAHN, status: proposed, notes: "The first name is proposed from Chardon's Latinate Chardonian analogue; the Auratan pronunciation is documented in [[Chalyte Rumors from Tiberius]]."}
- {name: Auratan, role: dynastic name, language: Chardonian, pronunciation: aw-rah-TAHN, status: documented, notes: "Pronunciation documented in [[Chalyte Rumors from Tiberius]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Domitia's life through her death in DR 1723, described from a 1740s frame in which her son Mitus is Magistros.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit name and `knownTo: [dufr]`.
- Added persistent Chardonian name metadata, preserving the documented Auratan pronunciation and proposing a full-name pronunciation.
- Added `POV: 1740s` and a temporal coverage note distinguishing Domitia's life from the later frame in which Mitus is Magistros.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary full-name entry remains `status: proposed`. Chardon's more Latinate Chardonian analogue supports **doh-MIT-ee-ah** for Domitia, while [[Chalyte Rumors from Tiberius]] explicitly records **aw-rah-TAHN** for Auratan. Accept `doh-MIT-ee-ah aw-rah-TAHN` by copying it to frontmatter and changing the primary entry to `status: documented`, or replace the proposed first-name reading while preserving the documented surname pronunciation.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only `_DM_` note was found to support the positive `dm_notes: important` attestation. Verify whether the attestation reflects remembered or off-vault information; retain, revise, or remove it only by human decision.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-12-09, type: captured}
born: 1722
gender: male
name: Vargus
affiliations: [Chardonian Legion, Society of the Open Scroll]
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1748-12-09, end: 1749-06-19, location: Mirror of Soul Trapping}
  - {type: away, start: 1749-06-20, end: 9999, location: Tokra}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Vargus
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Captured by [[Dunmar Fellowship]] on December 9th, 1748 in the [[Mirror of Soul Trapping]], [[Uzgukhar]], [[Xurkhaz]] %%^End%%

%% whereabouts need updating; copy description and other details from DM notes%%

![[vargus.png|right|300]]Twin to Valius, Vargus was a formidable warrior in the Chardonian legion, turned mercenary and adventurer. He is now under the curse of the Cleansed and largely unaware of himself.

%%^Metadata:names:v1%%
- {name: Vargus, language: Chardonian, pronunciation: VAR-goos, notes: "Proposed from the Chardonian Latin analogue, with a hard g, broad initial a, and final u read as oo; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot after Vargus's capture in the Mirror of Soul Trapping; his established DR 1749 release and later whereabouts are not yet reflected in the visible prose.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` and canonicalized the Dunmar Frontier campaign code in `campaignInfo` and the campaign block.
- Corrected the whereabouts history to end Vargus's mirror imprisonment on DR 1749-06-19 and record his departure in Tokra on DR 1749-06-20.
- Corrected the objective missing article in `was formidable warrior`.
- Added persistent Chardonian name metadata with the proposed pronunciation `VAR-goos`.
- Added `POV: 1748` and a persistent temporal-coverage note describing the still-outdated visible frame.

### Validated judgments
- Confirmed matching local-only sources support the positive `dm_notes: important` attestation; private contents are not reproduced here.

### Editorial assessment
- **Underdeveloped**: The visible article's central account ends while Vargus is controlled by the Cleansed and omits his established DR 1749 release and departure with Valius to begin a quieter life in Tokra. The smallest useful development is a source-grounded account of his Legion and mercenary background, Fausto's control, capture, release, and new start.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Session 79 (DuFr)]] establishes that Fausto used the [[Crown of Purity]] on Vargus after he tried to leave Fausto's service, while [[Session 124 (DuFr)]] establishes that Vargus was freed from the Cleansed and the mirror in DR 1749 and left with Valius in Tokra. The visible article still says he is under the curse and unaware of himself. Human choice: update the article and move its POV to 1749; defer the update and add the appropriate `status/gameupdate/dufr` tag; or intentionally preserve the DR 1748 snapshot. Copy-ready update: `Vargus is the identical twin of [[Valius]] and a former warrior of the [[Chardonian Legion]]. After leaving the legion, the brothers worked as mercenaries and adventurers and later joined the [[Society of the Open Scroll]]. [[Fausto]] used the [[Crown of Purity]] to place Vargus under the control of [[The Cleansed]] after he tried to leave Fausto's service. The [[Dunmar Fellowship]] captured him in the [[Mirror of Soul Trapping]] in DR 1748. Freed from both the mirror and the Cleansed in DR 1749, Vargus and Valius departed together in [[Tokra]] to begin a quieter life in Dunmar.`
- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Chardonian Latin-analogue proposal `VAR-goos`; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
- [ ] **Warning — status.questioned:** The automatic lint changes resolved the concrete frontmatter-formatting and whereabouts defects associated with `status/cleanup/metadata`, but the linter cannot remove a non-check status. Remove `status/cleanup/metadata` if no additional human metadata cleanup is intended, or retain it and record the remaining scope.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Statblocks - Grash Battle]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
%%^End%%

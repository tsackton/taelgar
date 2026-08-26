---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/gameupdate/dufr, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-12-08, type: killed}
born: 1691
gender: female
died: 1748-12-08
name: Evelina
affiliations:
  - {org: The Cleansed, end: "9999"}
whereabouts:
  - {type: away, start: 1748-12-01, end: 1748-12-08, location: Uzgukhar}
  - {type: home, start: "", end: "", location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Evelina
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Killed by the [[Dunmar Fellowship]] on December 8th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

%% copy DM notes, update header%%

A sorcerer and a member of [[The Cleansed]].

%%^Metadata:names:v1%%
- {name: Evelina, language: Chardonian, pronunciation: eh-veh-LEE-nah, notes: "Proposed from the Italian and Latin analogue for Chardonian: the vowels are articulated and stress falls on the penultimate syllable; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of Evelina's final mission and death; her earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` and canonicalized the Dunmar Frontier code in `campaignInfo` and the campaign block.
- Added persistent Chardonian name metadata with the proposed pronunciation `eh-veh-LEE-nah`.
- Added `POV: 1748` and a persistent temporal-coverage note.

### Validated judgments
- Confirmed local-only evidence supports the positive `dm_notes` attestation.
- The existing `status/gameupdate/dufr` remains supported while the visible article omits Evelina's established final mission and fate.

### Editorial assessment
- **Underdeveloped**: the visible article identifies Evelina only as a sorcerer and member of The Cleansed; it lacks the central established account of her infiltration of Xurkhaz and her final attack with Kadmos.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Campaigns/Dunmari Frontier Campaign/Session Notes/Session 77 (DuFr)]] and [[Campaigns/Dunmari Frontier Campaign/Session Notes/Session 79 (DuFr)]] establish Evelina's defining role in the Xurkhaz infiltration and her death during Kadmos's attack, while the visible article supplies neither part of that account. Copy-ready candidate: "Evelina took part in a Chardonian expedition that infiltrated [[Xurkhaz]] under the guise of scholars seeking trade and knowledge exchange, spying on the orcs and the [[Cloak of Rainbows]]. She later joined [[Kadmos]]'s attack on the palace and was killed in battle on December 8th, 1748."
- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Italian- and Latin-analogue proposal `eh-veh-LEE-nah`; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Statblocks - Grash Battle]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
%%^End%%

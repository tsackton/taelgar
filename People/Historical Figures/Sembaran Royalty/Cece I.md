---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/review, status/check/lint]
species: human
ancestry: Sembaran
born: 1628
gender: female
title: Queen
died: 1713-09-12
name: Cece I
affiliations:
  - {place: Sembara, start: 1648-12-11}
  - {place: Tyrwingha, start: 1648-12-11}
  - {org: House of Sewick, type: primary}
knownTo: [clee, adma]
dm_owner: joint
dm_notes: important
POV: modern
---
# Queen Cece I
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her), of the [[House of Sewick]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% status/review -> central to recent Sembaran history, could use collating information from discord, backlinks, dm notes%%

Cece I reigned for 65 years, the longest reign in the annals of the kings and queens of Sembara. Her reign was one of peace, prosperity, and recovery. Sembara finally began to climb out of the devastation of the [[Great War]] and the [[Blood Years]], and for the first time in five generations the future of Sembara seemed to be brighter than its past.

She was unlucky with her children, however, and of her six children: Bertram, Derik, Elleth, [[Robert I]], Diana, and Mara, only [[Robert I]] did not predecease her. 

%% Children
		Bertram	 b. 1651  d. 1695
		Derik	 b. 1654  d. 1660
		Elleth	 b. 1658  d. 1662
		Robert I b. 1660  d. 1722
		Diana	 b. 1661  d. 1711
		Mara	 b. 1663  d. 1709

Some important stuff around the radiant alliance in discord 
%%

%%^Metadata:names:v1%%
- {"name": "Cece I", "role": "primary", "language": "Sembaran", "notes": "Sembaran regnal form inferred from the subject’s dynasty and realm; Cece is an ordinary English-readable personal-name form and the regnal numeral needs no separate pronunciation guide.", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of Cece’s completed reign and family losses; her historical death date remains unresolved across sources.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name block and article POV with a temporal-coverage note.
- Added knownTo: [clee, adma], supported by the campaign introductions.
- Corrected “annuals” to “annals” in the reign description.

### Validated judgments
- status/review remains supported by the explicitly requested historical collation and the unresolved date conflict.
- The children’s ledger is distinct supporting genealogical material; it does not need to be copied into the visible article to preserve its existing family-loss account.

### Editorial assessment
**Underdeveloped**. The account of peace and recovery omits Cece’s personal command of the Radiant Alliance, the military victory that enabled the recovery, and the division of the crowns after her death. Add one compact reign-and-succession paragraph and reconcile the exact death date.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Radiant Alliance]] and [[Third Hobgoblin War (Sembara)]] establish Cece’s personal military command and the campaign that enabled southern recovery; [[The Election of Elaine II]] establishes the ensuing split succession. These central acts are absent from the visible account. Copy-ready addition: “Cece assembled and personally commanded the [[Radiant Alliance]] during the [[Third Hobgoblin War (Sembara)]], beginning the reconquest of southern [[Sembara]]. Its campaigns ended in the defeat of the [[Shattered Ice Clan]] in DR 1653. After her death in DR 1713, [[Robert I]] succeeded her in Sembara, while the [[Oracle of the Riven|Oracles of Tyrwingha]] chose [[Elaine II]], separating the two crowns.”
- [ ] **Warning — correctness.cross_note_conflict:** The frontmatter records `died: 1713-09-12`, but [[The Election of Elaine II]] explicitly says Cece died on June 3rd, 1713, after months of illness. Preserve the current value pending a human decision; align the death date and election chronology together rather than treating election and death as interchangeable dates.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. Preserve `dm_notes: important` unless the human attestation changes; it may refer to remembered information or material outside this vault.
%%^End%%

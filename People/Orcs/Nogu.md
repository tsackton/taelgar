---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: orc
ancestry: null
campaignInfo:
  - {campaign: dufr, type: "freed from the [[Mirror of Soul Trapping]] into [[Lubash|Lubash's]] care", date: 1748-12-05, format: "<met:u> by <person> on [[Session 71 (DuFr)|<target>]] in <current:1>"}
born: 1662
gender: female
name: Nogu
affiliations:
  - {org: People of the Rainbow, type: primary}
whereabouts:
  - {type: home, location: Xurkhaz}
  - {type: away, location: Mirror of Soul Trapping, start: 1680, end: 1748-12-04}
knownTo: [dufr]
excludePublish: [clee]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Nogu
>[!info]+ Biographical Info  
> An [[Orcs|orc]] (she/her), of the [[People of the Rainbow]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% The freed from the [[Mirror of Soul Trapping]] into [[Lubash|Lubash's]] care by the [[Dunmar Fellowship]] on [[Session 71 (DuFr)|December 5th, 1748]] in [[Xurkhaz]] %%^End%%

An [[Orcs|orc]], trapped by [[Agata]] in the [[Mirror of Soul Trapping]] after refusing to reveal secrets of the [[Cloak of Rainbows]] and the [[People of the Rainbow]]. She is from [[Xurkhaz]], born in the 1660s, and spent around 60 years trapped before being finally freed into her people's care.

%%^Metadata:names:v1%%
- {name: "Nogu", language: "unknown", pronunciation: "noh-GOO", notes: "Proposed using the Turkic analogue in Languages for Orcish: plain n and hard g, pure rounded o/u vowels, and final stress as a cautious Turkish-like option within the broad Turkic guidance. The name language and exact in-world phonology are not recorded.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Nogu after her DR 1748 release, with earlier captivity summarized; her later life and whereabouts are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and the existing campaign marker, and added knownTo: [dufr], name metadata, and the DR 1748 viewpoint.
- Corrected “and spend around 60 years trapped” to “and spent around 60 years trapped.”

### Validated judgments
- The reference already records Nogu's defining captivity and release; Session 77 corroborates that account.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `noh-GOO` in `Metadata:names:v1`. [[Languages]] gives Orcish a broad Turkic analogue; the proposal uses plain n, hard g, pure rounded o/u vowels and final stress as a cautious Turkish-like option. The name language and exact in-world phonology remain unrecorded. If accepted, set `pronunciation: noh-GOO` in frontmatter and mark the entry documented.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. It may represent useful information in memory or another off-vault source, so the attestation is preserved.
- [ ] **Warning — metadata.campaign_source_mismatch:** The `campaignInfo.format` and generated header point the December 5, 1748 release to [[Session 71 (DuFr)]], which instead records events on November 23. [[Session 77 (DuFr)]] records the release into Lubash's care on December 5. Replace those two link targets with `Session 77 (DuFr)`, retaining their existing display aliases and the supported date.
%%^End%%

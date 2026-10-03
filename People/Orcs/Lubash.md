---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [status/cleanup/metadata, person, status/check/lint]
species: orc
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-12-10, type: met}
born: 1691
activeYear: 1735
gender: male
title: Chief
name: Lubash
affiliations:
  - People of the Rainbow
  - {org: Xurkhaz, type: leader, start: 1745}
whereabouts: Uzgukhar
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Chief Lubash
>[!info]+ Biographical Info
> An [[Orcs|orc]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met the [[Dunmar Fellowship]] on December 10th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

%%needs campaign info and whereabouts cleanup%%

Chief Lubash is the stern and protective ruler of [[Xurkhaz]], and by extension the [[People of the Rainbow]]. He is also the bearer of the [[Cloak of Rainbows]].  Lubash holds immense pride for his kingdom, [[Xurkhaz]], and resides in [[Uzgukhar]].
## Overview

Chief Lubash ascended to the throne of [[Xurkhaz]] three years prior. He took over rulership after a tragic event where his older brother, along with his brother's wife and child, were killed by marauding hill [[Giants]] during a royal tour. As a ruler, Lubash is marked by his intense pride in [[Xurkhaz]] and a deep-seated mistrust of gods.
## Description

Lubash has a pale green complexion and is bald. His features are striking, characterized by a long, stern face and a notably large nose.
## Relationships

- **[[Uzgul]]**: Lubash's nephew, the son of his younger sister, and his heir. Lubash is deeply protective of [[Uzgul]] since his sister passed away due to sickness when [[Uzgul]] was young.
- **[[Murook]]**: Lubash's chief general and confidante. 
- **[[Azogar]]**: Lubash's loremaster and confidante. 
## Events

- Came to power in DR 1745 after his older brother's family was killed by hill [[Giants]].
- In DR 1748-1749, led the [[Orcs]] of [[Xurkhaz]] in the war against [[Grash]], aided by [[Dunmar Fellowship]]

## Campaign Interactions
%%^Campaign:dufr%%
```dataviewjs
await dv.view("_scripts/view/get_CampaignInteractions")
```
%%^End%%


%%SECRET[v2:9941da82556eb5be71d78ea4e8875676]%%

%%^Metadata:names:v1%%
- {name: "Lubash", language: "unknown", pronunciation: "loo-BAHSH", notes: "Proposal using the Turkic analogue for Orcish in [[Languages]]: u is oo, a is ah, sh represents sh, and final-syllable stress is a cautious choice; the broad analogue does not establish exact in-world phonology or the source language of this name.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Lubash as ruler following his DR 1745 accession, with dated reference to the 1748–1749 war; the beginning of the visible account is his accession, not a complete earlier biography.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized `knownTo`, `campaignInfo`, and the two existing campaign markers from the registered alias `DuFr` to the equivalent canonical `dufr` code, preserving block boundaries and contents.
- Added a proposed name entry and late-1740s temporal metadata; normalized frontmatter formatting.

### Validated judgments
- The central identity, accession, relationships, and war role are already represented. The Session 139 epilogue corroborates his continuing rule and the recovery of his city; its memorial detail does not require a separate campaign log in this reference note.
- `status/cleanup/metadata` is supported by the remaining interaction-date question; the tag is preserved.
- The local evidence supports the positive `dm_notes` attestation. The SECRET block was reviewed, with any useful recovery confined to the private handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed `loo-BAHSH` in `Metadata:names:v1`. The Turkic analogue for Orcish in [[Languages]] motivates u as oo, a as ah, and sh as sh; final-syllable stress is a cautious choice. This broad analogue does not settle exact in-world phonology or the name language. Accept it by setting `pronunciation: loo-BAHSH` in frontmatter and changing the entry to `status: documented`, or supply the intended reading.
- [ ] **Warning — metadata.campaign_interaction_date:** `campaignInfo` and the generated header record meeting the Dunmar Fellowship on DR 1748-12-10, but [[Session 76 (DuFr)]] dates their introduction and audience with Lubash to DR 1748-12-05, followed by dinner in [[Session 77 (DuFr)]] on the same day. Verify which interaction the field intends. For the first meeting, use `campaignInfo: [{campaign: dufr, date: 1748-12-05, type: met}]` and regenerate the displayed header; retain December 10 only if a separate intended interaction can be sourced.
- [ ] **Warning — temporal.unanchored_relative_date:** “Chief Lubash ascended to the throne of Xurkhaz three years prior” has no reference date, while the note also includes events extending into 1749. The same note explicitly dates the accession to 1745 in its affiliation and Events section. Replace that opening sentence with: `Chief Lubash ascended to the throne of [[Xurkhaz]] in DR 1745.` This preserves the established date without making the prose depend on an unstated 1748 viewpoint.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
%%^End%%

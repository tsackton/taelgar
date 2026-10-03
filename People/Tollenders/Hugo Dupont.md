---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Isinguer
campaignInfo:
  - {campaign: dufr, date: 1748-12-29, type: met}
born: 1691
gender: male
name: Hugo Dupont
affiliations: [University of Tollen]
whereabouts:
  - {type: home, location: Tollen}
  - {type: away, start: "1748-12-29", end: "1748-12-29", location: Magus Street}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Hugo Dupont
>[!info]+ Biographical Info  
> An [[Istabor Alliance|Isinguer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 29th, 1748 in [[Magus Street]], the [[Tollen|Free City of Tollen]] %%^End%%

![[hugo-dupont-portrait.png|right|320]]Hugo Dupont is a scholar and theologian, and a lecturer at the university, known for his classes on comparative divinity and theological science, particularly a series of lectures and scholastic discourse on the nature of intercessionary prayer, and the intertwined divinities of the [[Mos Numena|Eight Divines]].

He is well-known in the Isinguese community, and also well connected across the non-human community, including with [[Caelynn]]. 

%%SECRET[v2:1985a4c422bf8892807ca3f1e189d0dc]%%

%%^Metadata:names:v1%%
- {"name": "Hugo Dupont", "language": "unknown", "pronunciation": "ü-GOH dü-POHN", "notes": "Proposed from the northern French option in the Isinguese analogue in [[Languages]], selected for this French-shaped name: silent h and final t, ü for the French rounded u (ee with rounded lips), o as oh, and a nasal final on. The spelling POHN approximates that nasal vowel; avoid a hard final n. Exact name language is unrecorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Hugo’s teaching and community connections in Tollen, supported by the late-1748 meeting; earlier career and later changes are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “is scholar” to “is a scholar.”
- Normalized safe frontmatter formatting and the campaignInfo code to `dufr`; added matching `knownTo`, proposed name metadata, and temporal metadata.

### Validated judgments
- [[Session 82 (DuFr)]] corroborates Hugo’s academic role; routine conversation and promises of letters do not require a reference-note campaign log.
- Matching local sources support the existing positive `dm_notes` attestation. The SECRET block was separately reviewed and preserved; no private contents are copied into this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `ü-GOH dü-POHN` from the northern French option in the Isinguese analogue in [[Languages]], selected for the French-shaped spelling: h and final t are silent, ü is the rounded French u (ee with rounded lips), o is oh, and the last on is nasal rather than a hard n. The precise name language is unrecorded; the Spanish option would produce a different reading. Confirm or revise the preferred French-informed proposal; if accepted, copy it to frontmatter and mark the entry `documented`.
- [ ] **Warning — correctness.cross_note_conflict:** The dated `whereabouts` entry and generated meeting line place the December 29, 1748 encounter on [[Magus Street]]. [[Session 82 (DuFr)]] places Sarah’s introduction of Hugo at Guy Marchand’s Isinguese party on [[Scrollwright Street]], before the party later visits Magus Street. Human review should reconcile these two locations. The source-supported candidate is `{type: away, start: '1748-12-29', end: '1748-12-29', location: Scrollwright Street}`, followed by regeneration of the meeting line. The existing home entry for Tollen does not need changing.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The header contains `%%^Campaign:DuFr%%`, while the registry’s authored code is lowercase `dufr`. Copy-ready marker: `%%^Campaign:dufr%%`; preserve the enclosed text and closing marker. The generated header is left for human refresh alongside the disputed meeting location.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Tollen DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
%%^End%%

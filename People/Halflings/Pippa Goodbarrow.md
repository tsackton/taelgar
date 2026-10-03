---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: female
name: Pippa Goodbarrow
affiliations:
  - {org: Goodbarrows, type: primary}
  - {place: "Summer's Breeze", title: Captain, type: leader, start: 1}
whereabouts: "Summer's Breeze"
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1740s
---
# Pippa Goodbarrow
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of Goodbarrows  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[pippa-greenbarrow-portrait.png|right|400]]Pippa is a cheerful halfling woman, with a warm, welcoming smile, often seen wearing a wide-brimmed hat. She has a love of good food, great ale, and great company, and attracts like-minded crew to her ship, the [[Summer's Breeze]]. 

She has no fixed route or typical path, but is welcome in every port along the [[Apporia|Apporian Peninsula]] for her genial nature, and her tendency to throw impromptu parties on deck.

%%SECRET[v2:31affff57645f243e2aae6cb594a1429]%%

%%^Metadata:names:v1%%
- {"name": "Pippa Goodbarrow", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Pippa as captain of the Summer’s Breeze, anchored by the DR 1749 voyage; no wider tenure is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit display name, `knownTo: [dufr]` from [[Session 98 (DuFr)]], a subject-name block, and article `POV`/`povNotes`; normalized frontmatter.
- Corrected “welcome is every port” to “welcome in every port”.

### Validated judgments
- The ordinary name and transparent English surname require no pronunciation proposal.
- The local-only SECRET block was reviewed and preserved; recovery material is confined to the private handoff.

### Open findings

- [ ] **Warning — relationship.unresolved:** The primary affiliation `{org: Goodbarrows, type: primary}` has no resolving family note or name/alias target. The note and [[Session 98 (DuFr)]] consistently call her Goodbarrow, so there is no supported replacement family name. Confirm the family identity and create the intended `Goodbarrows` target if appropriate, or explicitly remove the affiliation if it is unintended; do not substitute another similarly named family.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. Keep the current `dm_notes: color` until the human confirms whether useful information remains in memory or another off-vault source; the in-note SECRET block does not validate or invalidate this separate attestation.
%%^End%%

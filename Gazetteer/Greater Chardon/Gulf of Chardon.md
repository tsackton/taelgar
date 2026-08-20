---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
displayDefaults: {wSecondary: "Controlled by <secondary:1>"}
tags: [place, status/check/lint]
typeOf: marine feature
typeOfAlias: gulf
name: Gulf of Chardon
whereabouts:
  - {type: primary, location: Endless Ocean}
  - {type: secondary, location: Chardonian Empire}
dm_owner: tim
dm_notes: none
POV: 1740s
---
# The Gulf of Chardon
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Gulf of Chardon is the name for the sheltered body of water formed by the [[Apporia]] to the west and south, and the mainland to the east. 

Relatively sheltered from major storms, it is a well-traveled maritime highway, with numerous sailing ships, fishing boats, and naval vessels passing to and from [[Chardon]].  It is also rich in marine life and is a highly productive fishing area.

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Gulf of Chardon; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Latinate Chardonian reading for Chardon with English descriptive components. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Gulf of Chardon, language: Chardonian, pronunciation: gulf of KAR-dohn, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — dm.notes_private_evidence_suspect:** Local-only evidence in [[Peninsula NPC Notes]], [[Session 98 - DM Notes]] is not accounted for by an in-note SECRET link. Review whether `dm_notes: none` remains accurate; do not remove or change the field automatically.
%%^End%%

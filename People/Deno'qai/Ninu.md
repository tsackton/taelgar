---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo: []
born: 1703
gender: female
name: Ninu
affiliations:
  - {org: "Ko'zula", type: primary}
whereabouts:
  - {type: home, location: "Ko'zula village"}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Ninu
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (she/her), of the [[Ko'zula]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Chief of the largest of the [[Ko'zula]] villages; told [[Delwath]] the story of the [[Cha'mutte’s Shadow Armband|armbands of Cha’mutte]] and the lost tanshi.

She is in her late 40s/early 50s, with plenty of wrinkles and worry lines; her hair, which she wears loose and long, is still a dirty blonde, with hints of gray at the temples. She dresses in dyed buckskin, mostly reds and browns.

%%^Metadata:names:v1%%
- {name: "Ninu", language: "Deno'qai", pronunciation: "nee-NOO", notes: "Proposed from the Hebrew/Arabic analogue for Deno'qai in Languages: i as ee, u as oo, ordinary n, and tentative Hebrew-style final stress; an Arabic-style NEE-noo reading remains possible.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Ninu as chief, anchored by her meeting with Delwath; the stated age and birth year require reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter layout and added `knownTo: [dufr]`, supported by Ninu’s interaction with Delwath in [[Session 53 (DuFr)]].
- Added persistent name metadata with a proposed pronunciation and `POV: 1748` with temporal coverage notes; preserved the birth year and visible age wording pending review.

### Validated judgments
- The concise chief-and-storyteller account and physical description are sufficient for Ninu’s demonstrated reference role.
- `status/cleanup/metadata`: not assessable. The remaining intended cleanup is not fully specified; the tag is preserved.
- Reviewed the local evidence matches; no useful subject-level material remains to recover beyond the shared record.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `nee-NOO` in the persistent name block. The Hebrew/Arabic guidance for Deno'qai in [[Languages]] supports `i` as “ee,” `u` as “oo,” and ordinary `n`; final stress follows a tentative Hebrew-style reading. An Arabic-style `NEE-noo` is also plausible. No exact in-world stress rule is established. Accept a pronunciation in frontmatter and mark the entry `documented`, or revise the proposal.
- [ ] **Warning — temporal.internal_conflict:** The undated description says “late 40s/early 50s,” but `born: 1703` makes Ninu about 45 in the DR 1748 portrait anchored by [[Session 53 (DuFr)]]. Confirm which age evidence to retain. If the birth year is correct, a copy-ready opening is “She is in her mid-forties, with plenty of wrinkles and worry lines;”. If the age description is intended, confirm a different birth year rather than deriving an exact one from the approximate wording. Both original values have been preserved.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo: []
born: 1734
gender: male
name: Zevi
affiliations:
  - {org: "Ko'zula", type: primary}
whereabouts:
  - {type: home, start: "", end: "", location: "Ko'zula village"}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Zevi
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him), of the [[Ko'zula]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Guide who brought [[Delwath]] to the Ko’zula village and later to meet [[Aristaea]] and [[Iascaire]].

He is a younger boy, maybe 14 at most, learning the hunting trade.

%%^Metadata:names:v1%%
- {name: "Zevi", language: "unknown", pronunciation: "zeh-VEE", notes: "Proposed from the Hebrew side of the Deno'qai cultural guidance in [[Languages]]: short eh, voiced v, final ee, and final stress; the Arabic alternative does not supply an equally clear v reading. The name's language is not independently established.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an October DR 1748 portrait of Zevi as a boy of about fourteen learning to hunt and guiding Delwath; later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the established campaign interaction.
- Added a persistent primary-name entry with a proposed pronunciation; retained `language: unknown` because the name language is not independently documented.
- Added `POV: 1748` and a persistent explanation of the article’s temporal frame.
- Normalized frontmatter field order and collection formatting without changing existing values.

### Validated judgments
- Session 53 (DuFr) identifies this young Ko'zula guide separately from the Bek'eni warrior with the same name.
- Confirmed subject-specific local timeline evidence supports the positive `dm_notes` attestation.
- The legacy `status/cleanup/metadata` tag is not assessable as a statement of remaining human cleanup intent and is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary-name pronunciation `zeh-VEE` is a proposal. Proposed from the Hebrew side of the Deno'qai cultural guidance in [[Languages]]: short eh, voiced v, final ee, and final stress; the Arabic alternative does not supply an equally clear v reading. The name's language is not independently established. Accept it by setting the name entry to `status: documented` and adding `pronunciation: zeh-VEE` to frontmatter, or supply the preferred pronunciation; leave the proposal open until then.

### DM evidence
- [[_DM_/Timelines/Unified Timeline From OneNote]]
%%^End%%

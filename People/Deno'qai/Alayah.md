---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/cleanup/text, status/check/lint]
species: human
ancestry: "Deno'qai"
born: 1725
gender: female
name: Alayah
whereabouts:
  - {type: home, location: "Te'kula village"}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Alayah
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (she/her), of the [[Te'kula]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The young Godcaller of the [[Te'kula]] tribe in the Elderwood. Dreamed of [[Rai]] and [[Kenzo]]. 

Gave her [[Jade Piece of Rai's Hand]] to [[Kenzo]] after [[Dunmar Fellowship]] defeated the green dragon [[Mezzar|Grimbaskal]]. 

%%SECRET[v2:fb38ebd0d992dbf59c4c0d7a735eac4b]%%

%% Refactor: consider if this should be written to be less DuFr specific %%

%%^Metadata:names:v1%%
- {name: "Alayah", language: "unknown", pronunciation: "ah-LAH-yah", notes: "Proposed from the Arabic side of the Deno'qai cultural guidance in [[Languages]]: ah vowels, consonantal y, silent final h, and penultimate stress; Hebrew-style final stress is also possible. The name's language is not independently established.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of the young Te'kula Godcaller, including her completed transfer of the jade fragment after Grimbaskal's defeat; her later tenure is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the established campaign interaction.
- Added a persistent primary-name entry with a proposed pronunciation; retained `language: unknown` because the name language is not independently documented.
- Added `POV: 1748` and a persistent explanation of the article’s temporal frame.
- Normalized frontmatter field order and collection formatting without changing existing values.

### Validated judgments
- Session 52 (DuFr) and Jade Piece of Rai's Hand corroborate the Godcaller role and completed jade transfer.
- Confirmed subject-specific local evidence supports the positive `dm_notes` attestation. The SECRET block was reviewed separately.
- The legacy `status/cleanup/metadata` and `status/cleanup/text` tags are not assessable as statements of remaining human cleanup intent; both are preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary-name pronunciation `ah-LAH-yah` is a proposal. Proposed from the Arabic side of the Deno'qai cultural guidance in [[Languages]]: ah vowels, consonantal y, silent final h, and penultimate stress; Hebrew-style final stress is also possible. The name's language is not independently established. Accept it by setting the name entry to `status: documented` and adding `pronunciation: ah-LAH-yah` to frontmatter, or supply the preferred pronunciation; leave the proposal open until then.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Te'kula - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Te'kula Dream Notes]]
%%^End%%

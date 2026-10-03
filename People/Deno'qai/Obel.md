---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo: []
born: 1688
gender: male
name: Obel
affiliations:
  - {org: "Te'kula", type: primary}
whereabouts: "Te'kula village"
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Obel
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him), of the [[Te'kula]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

An old ranger of the [[Te'kula]] who volunteered to fight [[Mezzar|Grimbaskal]] with the party. Miraculously survived.

%%^Metadata:names:v1%%
- {name: Obel, language: unknown, pronunciation: oh-BELL, status: proposed, notes: "Proposed from the Hebrew side of the Deno'qai Hebrew/Arabic analogue in Languages: two syllables, clear o and e vowels, hard b, final l, and final stress. The name's language and exact in-world pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Obel as an older ranger after the fight with Grimbaskal; his earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]`, supported by [[Session 52 (DuFr)]].
- Added a proposed name entry and a DR 1748 temporal viewpoint with coverage notes; normalized frontmatter formatting.

### Validated judgments
- Confirmed subject-specific local sources supporting the existing positive `dm_notes` attestation; its value is unchanged.
- `status/cleanup/metadata`: not assessable beyond the current lint because the original cleanup scope is not recorded; preserved for human disposition.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry proposes **oh-BELL**. This uses the Hebrew side of the Deno'qai Hebrew/Arabic analogue in [[Languages]]: two clear o/e vowels, hard b, final l, and final stress. The Arabic alternative does not settle those written vowels or the stress, and no name-specific pronunciation or name language is established. Confirm or replace this proposal; if accepted, set `pronunciation: oh-BELL` in frontmatter and change the entry to `status: documented`.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: "killed by [[Mezzar|Grimbaskal]] on"}
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo:
  - {campaign: dufr, date: 1748-09-04, type: met}
born: null
gender: male
died: 1748-09-06
activeYear: 1745
name: Zevi
affiliations:
  - {org: "Bek'eni", type: primary}
whereabouts: Elderwood
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: modern
---
# Zevi
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him), of Be'k  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%needs campaign info%%

A scout and warrior of the [[Bek'eni]]. 

%%^Campaign:dufr%%
Part of the patrol that originally found the [[Dunmar Fellowship]] in the [[Elderwood]].  Accompanied the party back to the God tree to meet [[Mezzar]], and was killed by [[Mezzar|Grimbaskal]]'s breath weapon after [[Mezzar]] dropped his elven form.
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Zevi", "language": "Deno'qai", "pronunciation": "zeh-VEE", "notes": "Proposed from the Hebrew-leaning Deno'qai analogue in [[Languages]]: voiced z, short eh, final i as ee, and final-syllable stress; exact in-world pronunciation and the competing Arabic adaptation are not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account of Zevi as a Bek’eni scout and warrior and of his death in DR 1748; no later living state is implied.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded Dunmar Frontier interaction.
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata with a proposed pronunciation and recorded the article’s temporal viewpoint.
- Filled the existing empty `campaignInfo` with the meeting on DR 1748-09-04 documented in [[Session 51 (DuFr)]].
- Corrected “and killed by” to “and was killed by.”
- Normalized the existing campaign marker from `DuFr` to the registry’s canonical `dufr`; filtering behavior is identical.

### Validated judgments
- `status/cleanup/metadata` remains supported by the stale tribal label in the generated header. The editorial reminder about campaign information is retained; the missing interaction metadata has now been supplied.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry for Zevi proposes `zeh-VEE`. Proposed from the Hebrew-leaning Deno'qai analogue in [[Languages]]: voiced z, short eh, final i as ee, and final-syllable stress; exact in-world pronunciation and the competing Arabic adaptation are not established. Confirm or revise it; if accepted, use `pronunciation: zeh-VEE` in frontmatter and change the name entry to `status: documented`.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. The attestation may represent remembered or off-vault information; retain or change it only after human review.

- [ ] **Warning — correctness.internal_conflict:** The generated biography says “of Be'k,” while the affiliation, visible prose, [[Bek'eni]], and [[Session 51 (DuFr)]] identify the Bek’eni. No supporting Be'k form was found in People, Groups, Gazetteer, or campaign records. Regenerate or correct only that header clause to `of the [[Bek'eni]]`, preserving the other generated fields.
%%^End%%

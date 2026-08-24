---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:55:52-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
name: Suhaya
whereabouts: Mawar Confederacy
dm_owner: tim
dm_notes: color
POV: modern
---
# Suhaya
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Suhaya is the largest town at the mouth of the [[Sulqat]] River. It is a busy port for the [[Mawar Confederacy]], sustained by salmon runs and river trade to the interior.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Suhaya, language: unknown, pronunciation: soo-HAH-yah, notes: cautious spelling-based reading; no language or name-specific pronunciation source was found, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the town's port and river-trade role are not tied to a narrower date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Completed the two elliptical sentences without changing their meaning.
- Added the required single-location map block, leaving its unknown locator blank.
- Added persistent name metadata with a spelling-based pronunciation proposal.
- Recorded a broadly modern POV and its temporal interpretation.

### Validated judgments
- Preserved `dm_notes: color` as a human attestation; the linter does not adjudicate between positive attestation values.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Suhaya's required world-map locator remains blank. Supply the established coordinate in `- {map: world, locator: <hex>}`.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `soo-HAH-yah` only as a cautious spelling-based reading because no language or name-specific pronunciation source was found. Review the proposal; if accepted, add `pronunciation: soo-HAH-yah` to frontmatter and change the entry to `status: documented`, or replace it with the accepted form and derivation.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No matching local-only `_DM_` note was found for the positive `dm_notes: color` attestation. Verify whether useful information remains off-vault or in someone's head; preserve or change the attestation by human judgment.
%%^End%%

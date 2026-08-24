---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/gameupdate/gl, status/check/lint]
typeOf: building
subTypeOf: fortified frontier camp
name: Varentia’s Camp
whereabouts:
  - {type: primary, location: Northern Provinces}
dm_owner: tim
dm_notes: important
POV: 1747
---
# The Voltara Garrison 2
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A Chardonian frontier garrison east of [[Voltara]]. 

%%
## Campaign Notes (GL Arc 3)

Encountered by the party en route to the [[Sentinel Range]]. The [[Lucilla Varentia|camp commander]] received reports of orc activity from the party before they turned south to avoid further contact with imperial troops.


- DR 1747‑11‑18: Party passes the garrison camp and shares intelligence on an orc attack.

DM Notes: [[Garrison Camp - DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Varentia’s Camp, role: primary, language: unknown, pronunciation: vah-REN-tee-ahz KAMP, notes: "Proposed from a cautious spelling-based reading because no language or pronunciation source is established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 snapshot of the frontier garrison; its later name, command, and status are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal POV metadata.

### Validated judgments
- `status/check/name` was preserved as independent human-review state.
- `status/gameupdate/gl` was preserved as not assessable because the garrison's later name, command, and status are not established.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `vah-REN-tee-ahz KAMP` from a cautious spelling-based reading because no language or pronunciation source is established. Accept, revise, or reject it, and copy an accepted primary pronunciation to frontmatter.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only `_DM_` notes were found for the positive `dm_notes: important` attestation. Verify whether the attestation refers to off-vault or remembered material; do not remove it automatically.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [group, status/check/lint]
typeOf: magical bloodline
ancestry: Urskan
partOf: Rodnya
name: Rodnya Nivik
dm_owner: tim
dm_notes: important
POV: modern
---
# Rodnya Nivik
>[!info]+ Information  
> An [[Ursk|Urskan]] magical bloodline  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> Parent Organization: the [[Rodnya|Rodnye]]

The Rodnya Nivik is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Nivik is most closely associated with conjuration magic, and especially with teleportation.


%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Rodnya Nivik", "language": "unknown", "pronunciation": "rahd-NYAH NEE-vik", "status": "proposed", "notes": "Proposal using the Russian analogue for Urskan in [[Languages]]: Rodnya uses final stress and a softened n before ya; Nivik uses stressed ee and unstressed ih, softened consonants before i, and a hard final k. Initial stress in Nivik is provisional; no accepted pronunciation or exact name language is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of Nivik’s place among Ursk’s eight ruling rodnye and its conjuration and teleportation specialty.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved the header version and human attestations.
- Added the explicit subject name from the existing filename and article identity.
- Normalized the private Campaign:none sentinel casing after verifying equivalent export semantics; retained its contents and boundaries.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `rahd-NYAH NEE-vik` in the persistent name entry. Proposal using the Russian analogue for Urskan in [[Languages]]: Rodnya uses final stress and a softened n before ya; Nivik uses stressed ee and unstressed ih, softened consonants before i, and a hard final k. Initial stress in Nivik is provisional; no accepted pronunciation or exact name language is recorded. Accept the intended complete reading in frontmatter and mark the entry documented, or supply a revised reading with its basis.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The positive attestation may refer to remembered material or another off-vault source. Confirm whether useful unshared material remains; preserve `dm_notes: important` until that human review.
%%^End%%

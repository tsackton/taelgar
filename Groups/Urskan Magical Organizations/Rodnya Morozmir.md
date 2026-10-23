---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [group, status/check/lint]
typeOf: magical bloodline
ancestry: Urskan
partOf: Rodnya
name: Rodnya Morozmir
dm_owner: tim
dm_notes: important
POV: modern
---
# The Rodnya Morozmir
>[!info]+ Information  
> An organization  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Rodnya Morozmir is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Morozmir is based in the southeast of the country and is best known for defensive magic; it is often credited with involvement in the vast arcane wards that protect much of Ursk.


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
- {"name": "Rodnya Morozmir", "language": "unknown", "pronunciation": "rahd-NYAH muh-rahz-MEER", "status": "proposed", "notes": "Proposal using the Russian analogue for Urskan in [[Languages]]: Rodnya uses final stress and a softened n before ya; the two unstressed o vowels are reduced toward uh and ah, z remains voiced before m, and final mir is read meer with tentative final stress. No name-specific language, stress, or accepted pronunciation is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of Morozmir’s place among Ursk’s eight ruling rodnye, its southeastern base, and its reputation for defensive magic.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved the header version and human attestations.
- Added the explicit subject name from the existing filename and article identity.
- Normalized the private Campaign:none sentinel casing after verifying equivalent export semantics; retained its contents and boundaries.

### Validated judgments
- Confirmed local DM evidence supports the positive attestation; private contents remain outside this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `rahd-NYAH muh-rahz-MEER` in the persistent name entry. Proposal using the Russian analogue for Urskan in [[Languages]]: Rodnya uses final stress and a softened n before ya; the two unstressed o vowels are reduced toward uh and ah, z remains voiced before m, and final mir is read meer with tentative final stress. No name-specific language, stress, or accepted pronunciation is recorded. Accept the intended complete reading in frontmatter and mark the entry documented, or supply a revised reading with its basis.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%

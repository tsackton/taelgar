---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1698
gender: male
name: Matteo Ausson
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: none
dm_notes: color
POV: 1720s
---
# Matteo Ausson
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[matteo-ausson.png|right|320]]One of the sons of [[Arnaud Ausson]], something of a ne'er-do-well. Rumored to have been the lover of [[Rinault Essford|Rinault]] in the summer of 1719, and still hangs around [[Rinault Essford|Rinault]] and his cronies. Also rumored to have been involved in the death of his sister Lizette when he was 10, but no one knows the details.

Full of swagger and bravado on the outside, at least.


%%^Campaign:none%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Matteo Ausson, role: primary, language: Sembaran, pronunciation: mah-TAY-oh oh-SOHN, status: proposed, notes: "Proposed from the French-leaning southern Sembaran analogue: au as oh, ss as s, and final nasalized on approximated as OHN; exact in-world pronunciation is not documented."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of Matteo after the rumored events of DR 1719; earlier childhood is mentioned only through an unresolved rumor, and later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit `name: Matteo Ausson`.
- Added `knownTo: [clee]` from [[Cleenseau Campaign - Index of NPCs]], which identifies the page as an index of people known to the party.
- Normalized the private block sentinel to `Campaign:none`.
- Added a proposed Sembaran pronunciation record for Matteo Ausson.
- Added `POV: 1720s` and a temporal-coverage note.
- Reordered and normalized frontmatter to the canonical form.

### Validated judgments
- The `Campaign:none` block contains a relationship query rather than authored subject lore; it was retained without a public-adoption finding.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `mah-TAY-oh oh-SOHN` uses the French-leaning southern Sembaran analogue, reading `au` as `oh`, `ss` as `s`, and final nasalized `on` approximately as `OHN`; exact in-world phonology is not documented. Accept it, revise it, or leave the name entry proposed.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local `_DM_` note was found for Matteo Ausson. Verify the existing `dm_notes: color` attestation; it may represent remembered or off-vault information and must not be removed automatically.
%%^End%%

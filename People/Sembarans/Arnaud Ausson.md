---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Isinguer
gender: male
born: 1674
name: Arnaud Ausson
whereabouts:
  - {type: home, location: Laicon, end: 1698}
  - {type: home, location: Cleenseau, start: 1699}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720
---
# Arnaud Ausson
>[!info]+ Biographical Info  
> An [[Istabor Alliance|Isinguer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[arnaud-ausson.png|right|320]]A prominent merchant in [[Cleenseau]], his grandmother, [[Lizette Ausson]], traces her family to [[Isingue]] and he and his wife Alessia are the heart of a small community of Isinguen transplants in [[Cleenseau]]. He is well connected with the [[Refounded Alliance of Aurbez]] and well known to the merchant caravans that come from places like [[Laicon]] with recovered dwarven metals. 

He remains close to his aunt, [[Giselle Ausson]], who runs [[Ausson's Crossing]], an important inn in [[Laicon]].


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
- {name: Arnaud Ausson, role: primary, language: Isinguese, pronunciation: ar-NOH oh-SOHN, status: proposed, notes: "French-side Isinguese analogue documented in [[Languages]]; the proposed reading uses French-style vowels and softened final consonants, while exact in-world phonology remains undocumented."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Arnaud as a Cleenseau merchant and a central figure in its Isinguese community; earlier life and later fate are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added the explicit name, `knownTo: [clee]`, a DR 1720 `POV`, and persistent name and temporal metadata.
- Corrected `and important inn` to `an important inn`.
- Normalized the legacy `Campaign:None` marker to `Campaign:none`.

### Validated judgments
- The `Campaign:none` block is an operational relationship index rather than narrative material.
- No local-only `_DM_` evidence was found, consistent with `dm_notes: none`.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block retains the proposed Isinguese pronunciation `ar-NOH oh-SOHN`, using the French side of the Isinguese analogue in [[Languages]]. If accepted, add `pronunciation: ar-NOH oh-SOHN` to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal while preserving its derivation.
%%^End%%

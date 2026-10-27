---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/lint]
typeOf: family
ancestry: halfling
name: Sunmeadows
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

%% Jasmine's parents own [[The Green Leaf]] in [[Darba]], but what the rest of the family does, and whether they travel or are largely based in Darba,  is not invented. %%

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
- {"name": "Sunmeadows", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification of a halfling family; the visible article has no narrower temporal state, while the comment preserves undeveloped family background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and the article’s POV and temporal-coverage note.
- Normalized `Campaign:None` to `Campaign:none`; the current exporter casefolds both to the same private sentinel, preserving filtered visibility.

### Validated judgments
- The ordinary comment preserves a partly established family connection and explicit uninvented questions; the questions remain provisional. The plain-English compound family name needs no pronunciation.

### Editorial assessment
**Underdeveloped** — The public family entry lacks its one established setting-specific role: the multigenerational operation of The Green Leaf in Darba. One factual sentence supplies this central identification; no broader family culture or travel pattern needs inventing.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The visible article identifies only a halfling family, while [[The Green Leaf]] establishes that the Sunmeadows have run that Darba harbor inn for generations. [[Jasmine Sunmeadow]] also identifies Jasmine as the innkeepers’ daughter. Add: `The Sunmeadows are a halfling family who have run [[The Green Leaf]], a harbor inn in [[Darba]], for generations.` Keep the comment’s uninvented travel habits and wider-family questions as editorial material.

%%^End%%

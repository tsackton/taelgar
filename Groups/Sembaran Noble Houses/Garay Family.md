---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: family
typeOfAlias: merchant family
ancestry: Sembaran
name: Garay Family
whereabouts: Embry
dm_owner: none
dm_notes: none
POV: modern
---
# The Garay Family
>[!info]+ Information  
> A merchant family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A wealthy merchant family based in Embry, specializing in cloth.

%% Free to be used for other purposes, but note some of the details on Susanne's page %%

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Garay Family", "language": "unknown", "pronunciation": "gah-REH FAM-uh-lee", "status": "proposed", "notes": "A French-informed proposal for Garay in its southern Sembaran setting, using the analogue in [[Languages]]: hard g, open ah, final ay as eh, and emphasis on the final surname syllable. The surname reading also matches the still-proposed component in [[Susanne Garay]]; that proposal is not an accepted source pronunciation. Family has its ordinary English reading. The exact name language and stress remain unestablished."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern account of the family’s cloth trade in Embry; the visible article does not describe a particular generation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit family name, and recorded persistent name and modern temporal metadata.
- Normalized `Campaign:None` to `Campaign:none`; the current exporter treats them identically, and the generated member table is unchanged.

### Validated judgments
- The visible family entry is proportionate to its limited reference role; Susanne’s personal campaign history is not required here.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise the complete proposed pronunciation `gah-REH FAM-uh-lee`. A French-informed proposal for Garay in its southern Sembaran setting, using the analogue in [[Languages]]: hard g, open ah, final ay as eh, and emphasis on the final surname syllable. The surname reading also matches the still-proposed component in [[Susanne Garay]]; that proposal is not an accepted source pronunciation. Family has its ordinary English reading. The exact name language and stress remain unestablished. If accepted, copy it to frontmatter `pronunciation` and mark the name entry documented.
%%^End%%

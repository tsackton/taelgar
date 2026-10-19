---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: family
typeOfAlias: noble family
name: House of Teckberg
whereabouts: Sembara
dm_owner: none
dm_notes: none
POV: modern
---
# The House of Teckberg
>[!info]+ Information  
> A noble family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A cadet branch of the [[House of Sewick]]. 

%% Nothing canonically made up other than the family tree. Available to be used as a powerful noble family in Sembara %%

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "House of Teckberg", "language": "unknown", "pronunciation": "HOWSS uv TEK-berg", "status": "proposed", "notes": "Proposal favoring the English strand of the Sembaran analogue in [[Languages]] for the title and Teckberg: short e, ck as k, hard g and initial stress, with the ordinary English House of. A French-influenced tek-BEHR is another possible adaptation. Neither name language nor exact pronunciation is documented in [[Gyles of Teckberg]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification of the house as a cadet branch of the House of Sewick; its founding history is not developed in the visible article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and formatting; added supported primary name and temporal metadata.
- Canonicalized the private sentinel after verifying identical current and legacy export output.

### Validated judgments
- The cadet-branch identification performs a bounded genealogical reference role; the family-tree comment records limited development and does not establish an adopted account of political power.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `HOWSS uv TEK-berg` in the name block. This favors the English strand of the Sembaran analogue in [[Languages]]: ordinary House of, short e, ck as k, hard g and initial Teckberg stress. A French-influenced tek-BEHR is possible. [[Gyles of Teckberg]] supplies no accepted pronunciation; the name language and pronunciation remain unconfirmed. Accept or replace the proposal before copying the full value to frontmatter and marking the entry documented.
%%^End%%

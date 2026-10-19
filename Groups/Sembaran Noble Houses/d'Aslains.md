---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/lint]
typeOf: family
typeOfAlias: noble house
name: "d'Aslains"
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: important
POV: modern
---
# The D'Aslains
>[!info]+ Information  
> A noble house  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A longstanding noble family in the [[Barony of Aveil]] with an ancient history. One of the wealthiest families in the [[Auberonne]] river valley.

%%^Campaign:none%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "d'Aslains", "language": "unknown", "pronunciation": "dahz-LANE", "status": "proposed", "notes": "The Aslain component has the recorded pronunciation Ahz-lane in [[Aslain]]. The proposed family form adds the d prefix and treats the written plural s as silent under the southern Sembaran French analogue in [[Languages]]. The complete family-name pronunciation and its language are not explicitly attested."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the family’s longstanding wealth and association with Aveil and the Auberonne; no particular current officeholder is asserted.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; recorded the explicit filename identity, a proposed full-family pronunciation, and modern POV/povNotes.
- Standardized Campaign:none after confirming equivalent filtering semantics.

### Validated judgments
- The short noble-family reference is sufficient for its bounded role; the recorded Ahz-lane pronunciation of [[Aslain]] takes precedence over deriving that component afresh from a language analogue.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `dahz-LANE` in `Metadata:names:v1`. The Aslain component has the recorded pronunciation Ahz-lane in [[Aslain]]. The proposed family form adds the d prefix and treats the written plural s as silent under the southern Sembaran French analogue in [[Languages]]. The complete family-name pronunciation and its language are not explicitly attested. If accepted, copy the complete pronunciation to frontmatter and set the entry to `status: documented`; do not replace the recorded component pronunciation with an analogue-derived one.
%%^End%%

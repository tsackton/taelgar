---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [status/cleanup/text, group, status/check/lint]
typeOf: family
typeOfAlias: yeoman family
ancestry: Sembaran
name: Thornes of Cleenseau
whereabouts: Cleenseau
dm_owner: none
dm_notes: none
POV: modern
---
# The Thornes of Cleenseau
>[!info]+ Information  
> A [[Sembara|Sembaran]] yeoman family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% The Thornes in the Cleenseau region have come up several times in various Cleenseau sessions as semi-prominent yeoman, sturdy, good allies to the PCs. I don't have any details made up but the family should have a "the Cottons in the Shire" vibe.  Not wealthy, but definitely hold some land themselves, likely at least partly [[Land Holding in Sembara|freehold]] %%

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
- {"name": "Thornes of Cleenseau", "language": "Sembaran", "pronunciation": "thornz of Klen-sew", "status": "proposed", "notes": "Complete-form proposal from the recorded thorn surname pronunciation in [[Beatrix Thorne]] and Klen-sew in [[Cleenseau]], with ordinary voiced plural z and the word of. The component readings are source-given; the combined family form awaits confirmation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification of the family with Cleenseau; the hidden development note does not supply a dated family history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded the primary name and supported temporal viewpoint with persistent name and temporal metadata.
- Normalized frontmatter field order and collection formatting.
- Added the explicit subject name and canonicalized Campaign:None to the equivalent Campaign:none sentinel.

### Validated judgments
- status/cleanup/text is supported: the established local family context remains absent from public prose, while the note retains a development reminder.
- The hidden “Cottons in the Shire” analogy and likely freehold tenure are speculative guidance, not adopted family facts.

### Editorial assessment
**Underdeveloped** — The family’s established social and geographic context is missing from the visible account. A short paragraph locating its yeoman and fishing households is the smallest useful completion; a full genealogy or invented family history is unnecessary.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The visible page identifies only a yeoman family, while [[Gideon Thorne]] and [[Gabriel Thorne]] establish the family’s local households and social role. Add a short public account rather than leaving all context in the planning comment. Candidate: “The Thornes are a yeoman family of the [[Cleenseau]] region, with households in the town’s North Close and nearby [[Auloutte]]. [[Gideon Thorne]] is a prominent fisherman in Auloutte, while his son [[Gabriel Thorne]] is a yeoman in Cleenseau.” Avoid asserting the unsettled Jon–Gideon kinship or the comment’s merely likely freehold tenure.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed complete reading `thornz of Klen-sew`. The surname component `thorn` is recorded in [[Beatrix Thorne]], and [[Cleenseau]] explicitly records `Klen-sew`; the family plural adds ordinary voiced z. No analogue replaces these accepted components. If accepted, copy the complete pronunciation to frontmatter and mark its name entry documented; otherwise revise the combined form.
%%^End%%

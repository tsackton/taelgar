---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/lint]
typeOf: magical society
ancestry: Drankorian
name: Occulta Ludum
dm_owner: tim
dm_notes: important
POV: modern
---
# The Occulta Ludum
>[!info]+ Information  
> A [[Drankorian Empire|Drankorian]] magical society  
> `$=dv.view("_scripts/view/get_Affiliations")`

A magical society associated with the development of magic and especially with practical inventions of harnessing magical power. 

While they rejected the extremist claims of the [[Omnis Pura]] in the later years of the [[Drankorian Empire]], there is little evidence that has come down to current day that they actively opposed [[Omnis Pura]].

%%^Campaign:None%%
### Historical Members

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
- {"name": "Occulta Ludum", "language": "Drankorian", "pronunciation": "ok-KOOL-tah LOO-doom", "status": "documented", "notes": "Pronunciation of the society name is explicitly recorded within the documented title pronunciation in [[Enchiridion of the Occulta Ludum]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of the society and its role in the later Drankorian Empire; survival or activity after the empire's fall is not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting.
- Added documented name metadata using the society-name pronunciation recorded in [[Enchiridion of the Occulta Ludum]].
- Recorded the broadly modern retrospective viewpoint and its limitation concerning the society's later survival.

### Validated judgments
- The concise reference entry identifies the society's practical magical focus and its stance toward the Omnis Pura; [[Drankorian Empire]] corroborates that central account.
- Confirmed local DM matches support the existing positive `dm_notes` attestation.
- The noncanonical private block contains only the historical-members Dataview query; it was inspected and retained.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The historical-members query is wrapped in `%%^Campaign:None%%`; [[Campaign Registry]] defines the shared nonpublic sentinel as lowercase `none`. Proposed opening marker: `%%^Campaign:none%%`, retaining the query and closing marker exactly. Review the export behavior before applying this visibility-sensitive syntax change.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 15]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 16]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Tower Text]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Rescuing Hralgar]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 65 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Stormcaller Tower - DM Version]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Edge of Echoes - Map Key]]
%%^End%%

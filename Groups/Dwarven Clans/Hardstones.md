---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/lint]
typeOf: clan
ancestry: dwarven
name: Hardstone Clan
dm_owner: none
dm_notes: none
whereabouts: Tokra
POV: modern
---
# The Hardstone Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Hardstones are a prominent dwarven clan in Tokra, primarily known for their long-standing association with the [[Archives|Tokra Archives]]. The clan has traditionally worked at the archives, primarily as architects and generally managing the physical infrastructure of the building, settling in [[Tokra]] in the years after the [[Fire War]]. But they are also known, at times, to work some minor runic magic to protect scrolls and mend damage.

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```


%% One Note
Work at the archives, as architects, janitors, supers. Work some minor runic magic to protect scrolls, mend damage, and the like, as well as making magical runic imprints of particularly valuable material that can then be copied and sent to Nayahar or Darba or Chardon without risk of error.

Know Seeker, but have not yet met anyone else in the party.
%%

%%^Metadata:names:v1%%
- {"name": "Hardstone Clan", "language": "unknown", "notes": "[[Dwarves]] explains that dwarven clan names are often rendered in the trade tongue and presented in English; this ordinary English form needs no pronunciation guide."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference description of the clan’s continuing work at the Tokra Archives, with post-Fire-War settlement as historical background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added minimal name metadata and a broadly modern POV; normalized frontmatter.

### Validated judgments
- [[Dwarves]] supports treating the displayed clan name as an ordinary translated form needing no pronunciation guide. [[Seeker]], [[Session 36 (DuFr)]], and [[Session 41 (DuFr)]] corroborate the clan’s archive work; individual members’ campaign incidents do not require a clan chronicle.

### Open findings

- [ ] **Suggestion — editorial.shared_material_redundant:** The `One Note` comment repeats the visible account of archive maintenance and minor runic protection/repair, but adds distinct material about runic copying and an early meeting-state note. Split it rather than deleting it wholesale: remove the repeated work/protection/repair wording and retain the distinct guidance. The runic-copying detail is also established in [[Seeker]]’s travel backstory and can be adopted as this bounded public addition: “They also make magical runic imprints of valuable texts, allowing copies to be sent to [[Nayahar]], [[Darba]], or [[Chardon]] without transcription errors.” If that sentence is adopted, retain only any useful archival meeting-state reminder in the comment, labelled as predating [[Session 36 (DuFr)]]. This is a human proposal; no hidden content was promoted or reorganized.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
%%^End%%

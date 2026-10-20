---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Wistel
whereabouts:
  - {type: primary, location: Sembara}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Wistel
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A major river in [[Sembara]], the Wistel rises in the foothills of the [[Sentinel Range|Sentinels]] and flows east across the western marches before mingling with the [[Enst]] through the wetlands of [[Ozabal|Ozabal Swamp]]. From there the combined waters reach the [[Western Gulf]] of the [[Green Sea]]. 

Major tributaries include:
* West of [[Ainwick]], the [[Tarnslow]], which meanders north and west from the north edge of the  [[Cleenseau Wood]]
* From the [[Aine Hills]], numerous small brooks, the most prominent of which are the [[Wetherburn]] and the [[Mereburn]]
* the [[Bollin]], with a confluence near [[Ainwick]]
* West of [[Gowerbourne]], the [[Chemelle]] which flows south from the [[Aine Hills]], and the [[Rindle]], which flows north from Wisford
* Between [[Gowerbourne]] and [[Wisford]]: the [[Lanting]], and several small brooks, the most prominent of which are [[Holling Brook]] and [[Ashwell Brook]]
* East of [[Wisford]]: the [[Brunebeck]], which joins the Wistel at Wisford

%%^Metadata:names:v1%%
- {"name": "Wistel", "language": "unknown", "pronunciation": "WISS-tuhl", "status": "proposed", "notes": "Uses the English option of the Sembaran analogue in [[Languages]] and the spelling: initial w, short i, pronounced st, reduced final el, and initial stress. The southern French option could instead give wees-TELL, with a full ee and final stress. The name language and intended reading remain unestablished."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "Sentinel Range", "map": "world", "locator": "12.10.A02"}
  - {"role": "outlet", "feature": "Western Gulf", "map": "world", "locator": "12.11.G.10"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and use; no narrower temporal reading position is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Added typed river map entries with the positions explicitly recorded in the corresponding watershed map ledger.
- Stored the unresolved pronunciation proposal persistently in the name block; accepted frontmatter pronunciations were preserved.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `WISS-tuhl` in Metadata:names:v1. Uses the English option of the Sembaran analogue in [[Languages]]: initial w, short i, pronounced st, reduced final el, and initial stress. The southern French option could give wees-TELL with full ee and final stress; intended language and reading remain unknown. Accept or revise the proposal, then copy the accepted primary pronunciation to frontmatter and mark the entry documented.
%%^End%%

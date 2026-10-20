---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Thalúrien
aliases: [Thalúrien, Taloraine]
pronunciation: THAH-loo-ree-en
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
# Thalúrien
*(THAH-loo-ree-en)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Thalúrien flows south from [[Lathirion Lake]] before joining the [[Istaros]] near the ruins of [[Isingue]]. It is formed from three tributaries which all feed the lake: the [[Naithale|Naithalë]] to the west, the central [[Velasse|Velassë]], and the [[Silire|Silírë]] in the east. The Velassë flows from within [[Orenlas]] itself and is little known to outsiders. 

The Isinguese called it the Taloraine, and Isinguese poets would speak of the clarity and purity of its water. 

%%^Campaign:none%%
In ancient elvish lore, the Thalúrien was the water of purity, thought, and the sky - sacred to [[Elmerca]], and the Aistanë was the water of growth, and fertility, and the blessings of [[Aldanor]].  
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Thalúrien","language":"unknown","status":"documented","pronunciation":"THAH-loo-ree-en"}
- {"name":"Taloraine","role":"historical","language":"Isinguese","pronunciation":"tah-loh-REN","status":"proposed","notes":"The article records this as the Isinguese name. Pronunciation proposal uses the northern French strand of the Isinguese analogue in [[Languages]]: a as ah, o as oh, aine as en and silent final e, with final prominence. The southern Spanish option could give tah-loh-RAI-neh; neither establishes exact in-world phonology."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Lathirion Lake, map: world, locator: }
  - {role: outlet, feature: Istaros, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography, with the former Isinguese name and poetic associations presented as history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded explicit identity where previously supplied by the filename.
- Normalized the legacy capitalization of the reserved Campaign:none sentinel.
- Added persistent name metadata, preserving accepted pronunciations and keeping unaccepted readings proposed.
- Added required typed map entries, leaving unsupported locators blank.
- Recorded POV: modern and concise temporal coverage in persistent metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required source and outlet map entries have blank locators. Supply verified world-map coordinates in the existing `Metadata:map:v1` entries; no endpoint coordinate for these positions was established, and none was inferred from regional geography.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or correct `tah-loh-REN` for Taloraine. The article records this as the Isinguese name. Pronunciation proposal uses the northern French strand of the Isinguese analogue in [[Languages]]: a as ah, o as oh, aine as en and silent final e, with final prominence. The southern Spanish option could give tah-loh-RAI-neh; neither establishes exact in-world phonology. If accepted, mark this name entry `documented`; otherwise replace it with the intended pronunciation while preserving established name context.

- [ ] **Suggestion — editorial.public_material_candidate:** The Campaign:none paragraph beginning “In ancient elvish lore” preserves a coherent symbolic account that would add historical context to the river’s Isinguese poetry. It is shared nonpublic lore rather than established visible canon. Proposed public addition for human adoption: “In ancient Elvish lore, the Thalúrien was associated with purity, thought, and the sky, and was sacred to [[Elmerca]]; the [[Istaros|Aistanë]] was associated with growth, fertility, and the blessings of [[Aldanor]].” Retain or remove the corresponding hidden passage only as part of that human decision; no adoption or reorganization was applied.
%%^End%%

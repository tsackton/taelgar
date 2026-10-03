---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T18:00:33-04:00"
lintVersion: "3.5"
tags: [place, status/check/tim, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Tafolwern
pronunciation: Tav-ol-WERN
whereabouts: Tyrwingha
dm_owner: joint
dm_notes: none
POV: modern
---
# Tafolwern
*(Tav-ol-WERN)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Tafolwern is the capital and foremost cultural center of [[Tyrwingha]], with roughly 35,000 inhabitants. Its ornate architecture, carefully arranged parks, water features, and intricate public art reflect the influence of [[Archfey Ethlenn|Ethlenn’s]] court. Carvings and mosaics often imitate the flowing forms of Sylvan writing, sometimes without forming readable text.

The city draws traders and traveling performers from across Tyrwingha and beyond. Its wealthy households and earls are customers for the wines of the Tyrwinghan countryside. Tafolwern is also home to the [[Oracle of the Riven]], the council that elects Tyrwingha’s monarch, and to [[Twilight's Pool]], the principal crossing to [[Twilight's Grace]].

%% @check/tim : initial canonical draft - thoughts? %%

%% Sources:
- [[2024-05-09 - Discord Chat with Lilairen - Tyrwinghan Rivers Settlements and Demographics]]
- [[2024-07-15 - Discord Chat with Lilairen - Sylvan Writing Emotional Magic and Celyn's Reading]]
- [[Celyn Learning Languages]]
%%

%%^Metadata:names:v1%%
- {name: Tafolwern, language: Tyrwinghan, pronunciation: Tav-ol-WERN, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the city in the current campaign era without a narrower temporal limit.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `POV: modern` and a persistent temporal-coverage note.
- Normalized line endings to LF while preserving the header's Markdown hard breaks.

### Validated judgments
- The approved article provides a concise account of the city's capital and cultural roles, distinctive ornament, wine trade, and principal fey crossing. Its current reference frame does not require a narrower date.
- Preserved the documented Tyrwinghan name and accepted pronunciation, the human DM attestations, and Tim's review state.

### Open findings

- [ ] **Error — metadata.map_missing:** Settlements require a `Metadata:map:v1` block, but the reviewed sources do not establish Tafolwern's exact map locator. Supply its verified world-map hex, then add one `map: world` location entry with that nonblank `locator`. No empty map block was added, following the user's preference.
%%^End%%

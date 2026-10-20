---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Fat Brook
whereabouts:
  - {type: primary, location: Tollen}
  - {type: secondary, location: Volta Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Fat Brook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small river flowing south into the [[Volta]], through [[Tollen]], channeled and partially covered.

%% Name is a corruption of Vattenbrok, the original Skaer name meaning tidal waters.  %%

%%^Metadata:names:v1%%
- {"name":"Fat Brook","language":"unknown","notes":"The existing shared comment offers derivation from Skaer Vattenbrok (tidal waters); this naming context awaits human adoption in the public account."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Volta, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern urban river course and channel works; the dates of the channel works are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Recorded the existing subject name explicitly in frontmatter.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries with supported endpoint features and left unknown positions blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for source and outlet. Fill those blank values with confirmed coordinates, preserving recorded features and roles.

- [ ] **Suggestion — editorial.public_material_candidate:** The shared naming comment supplies a coherent etymology absent from the visible entry. Decide whether to adopt it as public canon. Copy-ready candidate: “Its name is a corruption of Vattenbrok, the original Skaer name meaning ‘tidal waters’.” If adopted, retain only distinct editorial guidance in the comment. The comment alone does not establish canonical adoption.
%%^End%%

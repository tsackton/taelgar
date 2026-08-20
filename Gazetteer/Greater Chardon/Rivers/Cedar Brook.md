---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Cedar Brook
whereabouts:
  - {type: primary, location: Alta Tonaro}
  - {type: secondary, location: Yeraad Watershed, startFilter: r}
dm_owner: none
dm_notes: none
POV: 1740s
---
# Cedar Brook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small tributary of the [[Silverflood]], flowing north from the [[Chataan Mountains]].

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chataan Mountains, map: world, locator: }
  - {role: outlet, feature: Silverflood, map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Cedar Brook; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Validated judgments
- The missing-pronunciation check was dispositioned as not applicable because this is a plain-English descriptive title or an otherwise obvious ordinary label.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks source.locator, outlet.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

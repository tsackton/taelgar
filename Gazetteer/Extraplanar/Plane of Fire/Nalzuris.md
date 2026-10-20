---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Nalzuris
aliases: [Golden City]
whereabouts: Elemental Plane of Fire
dm_owner: tim
dm_notes: none
POV: modern
---
# Nalzuris
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Nalzuris, sometimes translated as the Golden City, is a rumored city on the [[Elemental Plane of Fire]], home to many [[Efreeti|efreeti]] palaces and forges.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Nalzuris, language: unknown, pronunciation: nal-ZOOR-iss, status: proposed, notes: "Cautious spelling-based proposal: a as in pal, z pronounced normally, u as oo, final is as iss, and provisional middle-syllable stress. No accepted pronunciation or established language of the name was found."}
- {name: Golden City, role: translated, language: Common, status: documented, notes: the article records this as a translation used sometimes}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern rumored planar geography; the article does not establish a dated firsthand account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting without changing existing values.
- Added explicit subject-name metadata, a primary name entry, and the article POV with its temporal interpretation.
- Added the required typed settlement map skeleton with its locator left blank.

### Validated judgments
- The brief rumored-city entry is proportionate to its demonstrated role in [[Elemental Plane of Fire]]; it preserves uncertainty and does not need invented districts or government.
- Golden City is recorded as a translated form; the language of Nalzuris itself remains unknown rather than being inferred from its inhabitants.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now contains `{map: world, locator: }`. The consulted planar description explicitly lacks reliable maps and supplies no usable locator. A human must identify the appropriate supported map and position; fill that entry with a verified locator, and select the relevant planar map if one is available. Do not invent a world hex or treat the blank as a known coordinate.

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `nal-ZOOR-iss`. No accepted pronunciation, established name language, or name-specific phonology was found in the target or [[Elemental Plane of Fire]]. This is a cautious spelling-based reading: a as in “pal,” ordinary z, u as “oo,” final is as “iss,” and provisional middle-syllable stress. Confirm or revise it before marking the entry documented and copying an accepted primary pronunciation to frontmatter. Golden City remains the separately documented translated form.
%%^End%%

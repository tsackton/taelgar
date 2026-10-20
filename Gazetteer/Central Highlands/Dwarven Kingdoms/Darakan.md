---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
ancestry: dwarven
name: Darakan
whereabouts: Khatridun
dm_owner: tim
dm_notes: color
POV: modern
---
# Darakan
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% setting dm_owner: tim due to Seeker/Frankar connection %%

Darakan is set high in the mountains, split between the upper levels on the surface, and the lower levels belowground. It is famous for its fine marbleworks, especially the elaborate stonework marking the gates of the upper city, set high in a cliff face, and reached by a series of marble steps and arches. 

Home to clan Highkeep, including [[Seeker]] and [[Frankar]].

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Darakan, language: unknown, pronunciation: DAH-rah-kahn, status: proposed, notes: "Analogue-informed proposal using the Dwarvish naming guidance in Languages (Tolkien Dwarvish): three open a vowels, an articulated r, a hard k, and initial stress. The name's language and exact in-world phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography and marbleworking traditions; the Highkeep family connection records origin and clan membership rather than current residence.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting, and made the filename-derived name explicit as `name: Darakan`.
- Added the required settlement map skeleton with the unknown locator left blank.
- Added persistent name metadata with a proposed pronunciation, plus `POV: modern` and temporal coverage.

### Validated judgments
- The city's defining marblework and Highkeep connection are corroborated by [[Seeker]], [[Frankar]], and [[Khatridun]]. The family connection does not assert either brother's present residence.
- Confirmed local source matches support the existing positive `dm_notes` attestation; its value and the ownership reminder are preserved.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has one `map: world` entry, but its `locator` remains blank. Supply the verified world-map hex in that existing entry; the reviewed sources do not establish a coordinate. Preserve the typed entry rather than substituting an empty locations list.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent entry proposes `DAH-rah-kahn`, informed by the Dwarvish/Tolkien Dwarvish analogue in [[Languages]]: three open a vowels, an articulated r, hard k, and initial stress. This is a proposed adaptation; neither the name's language nor its exact in-world pronunciation is established. Accept or revise the stored proposal; if accepted, copy the primary pronunciation to frontmatter and set the entry to `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
%%^End%%

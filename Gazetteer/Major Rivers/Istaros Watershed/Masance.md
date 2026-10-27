---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Masance
aliases: [River Masance, Masance River]
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Masance flows south, and is rocky and shallow.

%% Pull in details from the Aurbez and other similar pages; lots of stuff made up for the Aussons mini series but it should all be scattered about in Obsidian %%

%%^Metadata:names:v1%%
- {"name": "Masance", "language": "unknown", "pronunciation": "mah-SAHNS", "status": "proposed", "notes": "Cautious spelling-based proposal: initial ma as mah, c before e as s, final e silent, and final-syllable stress. No reviewed source establishes the river name’s language or accepted pronunciation; the spelling admits other readings."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Andonne, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal reading position is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter where needed and recorded the article’s broadly modern POV with persistent temporal coverage.
- Added an explicit subject name where absent and a persistent primary name entry.
- Added typed map metadata using unambiguous existing geographical evidence; unsupported locators remain blank.
- Corrected “in obisidian” to “in Obsidian” (objective typo).

### Validated judgments
- `status/cleanup/text` remains supported by the explicit synthesis reminder and the established missing regional and crossing account; the tag is preserved. The travelogue corroborates the crossing hazards but its disputed dating is not adopted.

### Editorial assessment
**Underdeveloped**: the visible note lacks the river’s regional location and hydrological connection, and the seasonal flooding and crossing role that make it a defining feature of the Aurbez travel corridor. These are established coverage gaps, not a request for new lore. The smallest useful scope is one short geographical paragraph and one crossing paragraph sourced to the named canonical notes.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `mah-SAHNS` in `Metadata:names:v1`. Cautious spelling-based proposal: initial ma as mah, c before e as s, final e silent, and final-syllable stress. No reviewed source establishes the river name’s language or accepted pronunciation; the spelling admits other readings. If accepted, copy the accepted primary pronunciation to frontmatter and mark the entry `documented`; preserve uncertainty until that decision.

- [ ] **Warning — metadata.map_location_missing:** Supply verified world-map locators in the existing typed `locations` entries; the reviewed evidence does not establish their positions. Preserve the endpoint roles and do not infer hexes from prose distances.

- [ ] **Warning — coverage.established_fact_missing:** The visible sentence gives only southward flow and a rocky, shallow bed. [[Aurbez and the Andonne]] makes the Masance a principal settlement river along the Aurbez Plateau and describes frequent spring floods; [[Andonne]] establishes that it joins the [[Aursen]] to form that river; [[Maseau - Dunmar Road]] describes its shifting unbridged fords, seasonal town, and dangerous spring or thunderstorm floods. These defining connections and travel conditions are missing. Bounded replacement candidate: “The Masance flows south through [[Aurbez and the Andonne]], beside the eastern edge of the [[Aurbez Plateau]], and joins the [[Aursen]] to form the [[Andonne]]. Its bed is rocky and shallow, and spring snowmelt often floods the upper river. The [[Maseau - Dunmar Road]] crosses at shifting fords, where a small seasonal town appears in warmer months. There is no bridge; spring floods can delay crossings for days, and summer thunderstorms can bring sudden flash floods.” Keep the exact historical date of [[The Travelogue of Etienne of Cassons]] unresolved rather than using it to date this broadly modern account.
%%^End%%

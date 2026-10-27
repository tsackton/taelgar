---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/mike, status/check/lint]
typeOf: road
name: Maseau - Dunmar Road
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

It is 480 miles from [[Cassons]] to the high pass over the [[Sentinel Range]], and the road passes through three major areas on the journey. The first 140 miles run through the [[March of Andonne]], a land of small-scale ranchers and marcher lords. Clustered along the road are numerous fortified ranches, once the main defense from the [[Plaguelands]]. Today these ranches are open and have grown into small villages and markets, and the lords 50 miles or more to the south and east bear the brunt of whatever comes out of the [[Plaguelands]]. Travelers are advised to avoid sleeping on the roadside, but rarely is it needed as the ranches along the road have developed into waystops and places of refuge, earning a second income as inns and taverns.

After a week or more of travel, the first river crossing is reached, the crossing of the [[Masance]]. The river is wide and rocky, though shallow, and there is no bridge here, as the fords shift each year with the floods. During the spring floods, the crossing is dangerous and multi-day, or longer, waits for a safe crossing are common. In summer and autumn the crossing is usually quick as the snowmelt subsides – unless a thunderstorm brings a flash flood, always a danger in high summer. A small town springs up here in the warmer months with guides, conmen, adventurers, pickpockets, tinkers, and traders but it vanishes into the countryside each winter as the cold winds come and travelers mostly vanish. 

After crossing the Masance, the road begins to ascend into rocky scrubland, and the castles of the marcher lords of the [[March of Andonne]] quickly vanish. For the next 60 miles or so, the land is sparsely populated as the road rises towards the edge of the great escarpment that marks the [[Aurbez Plateau]]. This is difficult terrain: few people live in the hills and bandits can be a danger. 

Here, the road approaches the base of the [[Aurbez Plateau]] as it turns to follow a more southerly course. To the west, the land rises sharply to the [[Aurbez Plateau]], a very steep ride unsuitable for wagons. The higher elevation is slightly wetter and safer, and occasionally travelers see goat herders and shepherds tending flocks along the ridge. For the next 75 miles, the road runs beneath the plateau ridge, several thousand feet below the high ridge from which the plateau stretches. 

About 10 miles into this stretch of road, along the base of the escarpment, the road passes [[Laicon]] and the inn at [[Ausson's Crossing]], where a narrow mule track descends off the plateau. Metals from wildcat miners can often be purchased here. From [[Laicon]], the terrain gradually becomes more settled as the road rises to meet the [[Aursen]]. This land is dotted with stands of pine and aspen, near water, and grasses and dirt and scrubby vegetation elsewhere. The soil is poor, but along the rivers small scale irrigation allows for small farmsteads growing wheat and millet. 

At the crossing of the Aursen a major waterfall is visible just upriver, where the river cascades down 2000’ in just a few miles, as it falls off the Aurbez Plateau and continues its journey east. The growing market town of [[Aursenbourg]] sits at the crossing, where a stone bridge was constructed by the [[Refounded Alliance of Aurbez]] in DR 1732, replacing a ferry that once provided service to travelers for most of the year.

Shortly after the crossing of the Aursen is the crossroads where a small inn stands, and the road splits: west to [[Tokra]] or south to [[Karawa]] along the [[South Dunmar Road]]. The western road rises over the next few days as it ascends into the [[Sentinel Range|Sentinels]], and soon reaches the alpine valleys of the lower reaches of the [[Sentinel Range|Sentinels]]. The remaining stretch of the road crosses through this land, until the final ascent into the high passes. The land is still dry, but pine trees and aspens are not uncommon, and elk are seen and hunted in the summer and fall months. (They winter in the Triangle, usually). Snow is a danger in the fall and winter, and the road closes for a good part of the year. 

After another 120 miles through the mountain valleys, the road rises sharply over several days to the high pass itself, and then begins the descent into [[Dunmar]].

%%^Metadata:map:v1%%
locations:
  - {feature: Cassons, map: world, locator: }
  - {feature: high pass over the Sentinel Range, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Maseau - Dunmar Road", "role": "primary", "language": "unknown", "pronunciation": "mah-ZOH DUN-mar ROHD", "status": "proposed", "notes": "Complete-name proposal combines the accepted Maseau pronunciation in [[Duchy of Maseau]] and accepted Dunmar pronunciation in [[Dunmar]] with ordinary English Road. The complete compound itself is not recorded as an accepted pronunciation, and its name language is not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern route and travel conditions, including the stone bridge built in DR 1732; no finer undated snapshot is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.
- Added the required road map skeleton with the described endpoints; unknown locators remain blank.
- Removed two duplicated spaces and the duplicated final full stop in the route prose.

### Validated judgments
- The route, roadside settlements and bridge are corroborated by [[Aurbez and the Andonne]], [[Aursenbourg]], [[Laicon]] and [[South Dunmar Road]].
- `status/check/mike` is preserved as independent human-review state.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required road map block has its two unordered endpoints, but both `locator` values are blank. Supply verified world-map coordinates for Cassons and the high pass described in the article in the existing entries; no coordinate has been inferred.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the complete proposal `mah-ZOH DUN-mar ROHD`, assembled from the accepted component pronunciations in [[Duchy of Maseau]] (`mah-ZOH`) and [[Dunmar]] (`DUN-mar`), plus ordinary English Road. This uses direct recorded component pronunciations, not a new analogue derivation, but the complete compound is not yet adopted. If accepted, copy it to frontmatter and mark the existing entry `documented`; otherwise correct both together.
%%^End%%

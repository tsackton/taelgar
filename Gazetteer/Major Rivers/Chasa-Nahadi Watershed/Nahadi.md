---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Nahadi
aliases: [Nahadi River]
pronunciation: nah-HAH-dee
whereabouts:
  - {type: primary, location: Greater Chardon}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Nahadi
*(nah-HAH-dee)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Nahadi is a wide, slow moving river, meandering through a broad alluvial plain, that drains [[Lake Valandros]], and joins the [[Chasa]] near Chardon. Natural levees fringe the deep main channel, beyond which lie orderly patchworks of irrigated fields to the west and a rising mosaic of oak-pine foothills to the east.

The Nahadi is easily navigable along its entire length, and is a major trade connection and riverboat route in the [[Chardonian Empire]]. 

The name Nahadi derives from the old Northros word for "mighty river". 

%%^Campaign:none%%

### Nahadi River Valley - Overview - Raw ChatGPT Notes

**Climate (Köppen Csa – hot-summer Mediterranean)**  
Mild, rainy winters (mid-40s °F / 7 °C lows; 18 in / 450 mm of precipitation, most November – March) give way to long, bright summers that climb past 90 °F / 32 °C with scarcely a cloud from mid-June to early September. A dependable late-summer “wine wind” funnels up the valley each afternoon, moderating heat and clearing river mists before nightfall.

**Geography & Terrain**  
The Nahadi is a broad, unhurried river that braids and meanders through a 15- to 25-mile-wide alluvial plain. Natural levees fringe the main channel, beyond which lie orderly patchworks of irrigated fields to the west and a rising mosaic of oak-pine foothills to the east; oxbow lakes and reedy backwaters provide natural harbors for shallow-draft barges all along its course.

**Flora & Fauna**

- West Bank (cultivated): hedgerow willows, poplars, and field-margin pomegranates shelter hares, partridge, and stoats; the river itself teems with carp, catfish, and migratory lamprey.
- East Bank (wooded): down-valley mixed evergreen forests of holm oak, stone pine, and cedar give way upslope to stands of beech and silver fir; red deer, wild boar, and lynx roam beneath a spring canopy carpeted with cyclamen and asphodel.  
- Great white storks and grey herons stalk the flooded rice paddies, while summer nights resound with tree frogs and nightjars.

**Agriculture & Land Use (late-medieval / early-Renaissance techniques)**  
Irrigation ditches and simple norias lift water onto terraced vineyards (producing robust reds and sun-sweetened raisins), olive groves for oil, and rotations of durum wheat, chickpeas, and saffron. Flood-recession fields near the levees yield flax, melons, and indigo, and every village maintains communal mulberry orchards for sericulture. Upriver timber and resin from the eastern forests float downstream on rafts, exchanged at market ports for pottery, metalwork, and river fish dried in the valley’s constant summer breeze.

%%^End%%

%%^Metadata:names:v1%%
- {"name":"Nahadi","language":"Old Northros","pronunciation":"nah-HAH-dee","status":"documented","meaning":"mighty river"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Lake Valandros, map: world, locator: }
  - {role: outlet, feature: Metium, map: world, locator: 13.07.A24}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography, navigation, and trade role; the older name derivation is not dated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Recorded the existing subject name explicitly in frontmatter.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries; used the Metium confluence coordinate from [[Metium]] for the outlet and left the source locator blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for source. Fill those blank values with confirmed coordinates, preserving recorded features and roles.

- [ ] **Suggestion — editorial.shared_material_redundant:** The Geography & Terrain paragraph in the raw-notes Campaign:none block repeats the public natural-levees, western irrigated-fields, and eastern oak-pine-foothills sentence. Remove that duplicated sentence from the hidden paragraph; retain the distinct river-width, backwater, climate, agriculture, and fauna ideas as clearly unadopted planning. Do not promote those ideas into public prose.
%%^End%%

# Note Categorization
*last update: Dec 16th 2025*

Notes (pages) are categorized based on the combination of a descriptive tag, and a typeOf string. Both descriptive tags and typeOf strings are controlled vocabulary, and pages that do not have a canonical descriptive tag + typeOf combination will be flagged in queries in Data Cleaning. 

### Major Note Types

There are seven major categories of notes that are defined by descriptive tags and that are used by header code to generate specific headers. 

(1) Living Beings. This includes individual people, which are defined by the `#person` tag, powers (sometimes called divinities; see: [[Metaphysics of Creatures]] and [[Divinities and Powers - Discussion]]) which are defined with the `#power` tag, and notes about species or other types of creatures, defined by the `#creature` tag. (**Note: as of 12/16/12025, powers and creatures still use deity and species**).

(2) Places. These are, well, places, and use the `#place` tag. Places must have a typeOf, and have a controlled typeOf vocabulary, see below. 

(3) Events. These are specific events that have a start and end date (so this excludes things like timelines or holidays which recur each year). These use the `#event` tag. 

(4) Things. These are pages about specific things (Vindristjarna's Phasing Stone), general classes of things (Phasing Stones), materials (chalyte), books, vehicles, and generally any inanimate object that is not a place (structures, roads, walls all belong in places). There is some arbitrariness here, but generally if it moves, it's a Thing, if it doesn't move, it's a Place. Uses the `#thing` tag (**Note: as of 12/16/2025, things still use the older item tag**). 

(5) Groups. These are pages about groups of people. This can include lineages (such as dwarven clans, noble houses, or other family groups you are born into), cultures (ancestries and any other kind of ethnic or linguistic group), and organizations (anything you join, including magical groups such as thuhr as well as more typical groups like guilds and cults). There is some fuzziness here, but typically a realm that is defined by borders and physical control over space is a place, not a group, even it is fairly monolithic (though note that many ancestries have either a culture page or a realm page, but not both). Traditionally, the main page for a religion has been considered background, not groups, although religious orders are considered groups. Currently this is defined by the `#organization` and `#culture` tags, but this might change. 

(6) Sources. These are primary sources, either session notes (`#session-note`), or text written in a way that is intended to represent a handout or other kind of in-world game information (`#souce`). These currently have no automatic header generation. 

(7) Conceptual. These are pages that don't belong to any other group. These include world background pages (`#background`), which represent in-world information that is not any of the other defined types above (typically things like holidays, history, and overview pages about concepts such as [[Land Holding in Sembara]]). These also include pages with meta-information (timelines, map of content style information, game mechanics, and things like that). Meta pages (tagged with `#meta`) shouldn't contain in-world text themselves (though they can collate information from other notes). These currently have no automatic header generation. 

## Descriptive Tags
***Last update: 12/08/2025***

Every page should have a descriptive tag, excluding pages in meta directories (e.g., any starting with `_` and assets), the Campaign directory, or the Worldbuilding. 

The following descriptive tags are considered canonical. Note that while item pages often have subtags (e.g. `item/vehicle`), these are not consistently used and should be considered obsolete/depreciated, unless otherwise noted. 

* **person**: a specific individual
* **deity**: a specific page about a god or other deity
* **species**: a page about a specific type of creature. Can be used for broad types (humans) as well as more specific types (sea hags)
* **place**: a specific geographical place
* **event**: a page about a specific event
* **item**: a specific item, or a type of item, or a material. 
* **organization**: a specific group of people or other type of organization, including things like pantheons or families or clans.
* **culture**: a page describing a specific culture
* **session-note**: a page about a specific session
* **source**: a page containing the actual text or a paraphrase of actual in-world information, typically intended to be given to players as is. 
* **meta**: a page about pages, for example this page. Does not contain world information, but may contain information about world information. Can also be used for map of content-style pages that are outside the \_MoC folder, for example indexes of NPCs or indexes of events.
* **background**: a conceptual page that describes world background. This is still canonical information (or at least, potentially canonical, depending on the status tags) but it doesn't refer to a specific living being, place, group, thing, or event (i.e. Land Owning in Sembara or Climate Background). A good catch-all for otherwise unclear pages. Includes holidays, which should have a typeOf: holiday and (usually) a religion tag. 


There are three other tags that can be added to clarify the page but one of these items on its own is not sufficient to remove the page from the missing tags list:
* **pc**: a page describing a player character. Use a subtype for the campaign, i.e. pc/greatwar or pc/cleenseau
* **religion**: a page something about a specific religion. Use a subtype to define the type of religion. Also should be used for organization and deity pages that are part of this religion, i.e. religion/mosnumena should get all of the pages about the Mos Numena religion.
* **testcase**: this page makes use of complex Javascript features and is a good page for testing changes with

Pages that do not have any of these tags are listed here [[Missing Tags]].

See: [[Descriptive Tags - Discussion]] for discussion and proposals around tags. 

Descriptive tags are used to determine the page type, which is important for header generation. The page types that have meaningful header automation are `person`, `place`, `organization`, `event`, and `item`. See [[Display Control]] for more. 

## TypeOf
***Last update: 12/09/2025***

Certain descriptive tags require a secondary classification using typeOf (or the synonym species). The details of how typeOf is used depend on the descriptive tag, as outlined below. 

Currently, person, place, item, and organization require typeOfs; event can have them but usually doesn't. Currently, only place has a controlled vocabulary for typeOf. 

### Place TypeOfs

Place typeOf categories are organized into several broad groups. These are not tagged anywhere, but are meant to be small enough that it is feasible to write simple dataview queries or base filters to pull up all of a category. In the future this may be revised (e.g., an additional layer such as typeCategory might be added to frontmatter, potentially auto-populated). 

How ancestry, typeOfAlias,and subTypeOf might be used in association with typeOfs is discussed below. 
#### Communities
_Status: clean_

There are three place typeOf categories that generally relate to places where communities exist on a landscape. 

- **settlement** is used to describe any note about a current or former community of people; obvious examples are things like villages, towns, and cities, but transient settlements (a camp) and ruined settlements fit here too. There is no specific minimum size, but generally a single house would be considered a structure, not a settlement, and a building complex with a singular purpose (castle, monastery) would also generally be a structure, even if people make their home there. 
- **neighborhood** is used to describe subparts of a settlement; obvious examples are things like wards of Tollen or the North Bank of Chardon. Any note that describes a subdivision of a settlement that is larger than a single building or building complex should use the neighborhood typeOf. 
- **realm** is used to describe collections of settlements; this can be at any level of organization, from small groups like Sembaran manors or Addermanian shires, to intermediate-scale clusters (the Duchy of Wisford), to kingdoms (Sembara), to groups of realms (Dwarven Kingdoms of the Sentinels). Pages which focus on the physical landscape as opposed to the species landscape generally should use the region typeOf not the realm typeOf. Realms that have a magical existence (fey domains, etc), should use the extraplanar domain typeOf. 

Other frontmatter: 
- No other frontmatter is required for this group of typeOfs, though generally it will be desirable to at least include a typeofAlias for the header. 
- Typically the typeofAlias should be one of the suggested phrases below, possibly with one or more adjectives prepended. Descriptors are arbitrary, and the absence of a descriptor does not indicate lack of that feature (e.g. a city may still have walls even if it is not listed as a fortified city, and a town may still have a market even if it is not listed as a market town). 
	- settlement: village, town, and city are suggested
	- neighborhood: ward, precinct, district or similar are suggested for official administrative subdivisions; neighborhood (e.g. typeofAlias blank) or urban area for informal settlement parts
	- realm: kingdom, march, duchy, barony, shire, republic, empire or similar are suggested for singular realms; "group of x" is suggested for pages about groups of realms; and various terms like alliance or trading league are suggested for pages about in-world collections of realms (e.g., potentially Istabor Alliance). But see note on Geographic Regions, below. 
- subtypeOf is not used currently for any of these tags, though potentially some descriptors could get moved to subtype if it turns out to consistently be useful to filter or select on them.
- ancestry is encouraged to be used, but it is principally for display; typeOf: settlement and ancestry: dwarven does not consistently get all dwarven cities, for example, and should not generally be expected to. 

#### Geographic Regions
_Status: clean_

There are two typeOf categories that relate to geographic areas of the world. 

- **region**: is used to describe any geographic subdivision of the world. While the distinction between "realm" and "region" is a little arbitrary, region pages typically focus on physical geography, topography, climate, etc, instead of politics, law, economy. Generally pages that are clearly about collections of realms (cf [[Dwarven Kingdoms]]; [[Borderlands]]) should be realm, whereas pages that are ambiguous or lean more towards geography should be regions (cf [[Central Dunmar]]; [[Zimkova]]). But this is admittedly a judgement call. 
- **watershed**: is used specifically to describe watersheds, that is collections of rivers and drainage basins. Note this is not used strictly to refer to unique drainage basins, e.g. [[Tyrwinghan Watershed]] describes the drainage basins of several nearby rivers. 

Other frontmatter:
- No other frontmatter is required for this group of typeOfs, and typeofAliases are rarely used. Typically "region" or "watershed" is fine for display purposes. 
- subtypeOf and ancestry are not currently used for these pages and generally don't have a useful meaning here. 

---
#### Extraplanar
_Status: clean_

There are three typeOf categories that relate specifically to extraplanar features. 

- **plane**: is used to describe pages about planes as a whole (for example, [[Feywild]] or [[Material Plane]]); these should live in Cosmology, not Gazetteer, but otherwise are treated as locations. 
- **extraplanar domain**: is used to describe pages about planar regions where the character of the region is magically influenced by its ruler; the most obvious examples of these are fey realms like [[Twilight's Grace]] or [[Amberglow]], though others may exist and have not been invented yet. This would be an appropriate typeOf for a layer of the [[Abyss]], for example, if such things exist in Taeglar. 
- **planar link**: is used to describe pages about specific [[Planar Connections]], most commonly portals between the Feywild and the Material Plane. 

Other frontmatter:
- The `plane` typeOf generally does not need or expect other categorization frontmatter; because planar classification is intentionally left unclear, it is better to use whereabouts where multiple classifications are supported (e.g., see [[Feywild]] for an example). 
- The `extraplanar domain` typeOf often uses both whereabouts and ancestry to specify what type of extraplanar domain it is; fey realms, in particular, should always specify `ancestry: fey`. `typeOfAlias` is also typically expected: traditionally `realm` is used for fey domains and `domain` for [[Shadowfolds]] domains. 
- The `planar link` typeOf should use `typeOfAlias` to identify whether it is a weak point, a vortex, or a portal; see [[Planar Connections]] for details. 

---

#### Biomes

typeOf categories that relate to biomes / biological terrain

- wetlands
- forest
- plain
- desert


Unclear

Structures:
- inn
- building
- road
- holy site
- infrastructure

Water Features:
- waterway
- lake
- marine feature

Landforms:
- topographical feature
- island
- subterranean feature

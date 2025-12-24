# Note Categorization
*last update: Dec 24th 2025*

Notes (pages) are categorized based on the combination of a descriptive tag, and a typeOf string. Both descriptive tags and typeOf strings are controlled vocabulary, and pages that do not have a canonical descriptive tag + typeOf combination will be flagged in queries in Data Cleaning. 

There are 12 primary note categories, which are described below. These are not meant to exhaustively categorize every note in the vault; instead, they guide both Markdown templates / formatting, required/expecting metadata, and automatic header generation.

## Person
**Tag: `#person`**

Definition: a specific individual.

The person tag is used for all named sentient beings, except those who are sufficiently powerful to transcend normal mortality (these are powers, see below). Named pets, familiars, companions, beasts, and similar should be considered persons. 

The person note expects the following metadata:

Classification: species (required), ancestry, subspecies, gender
Other: pronouns (only use if different from gender), title, ka (for elves), ddbLink (for PCs or NPCs with character sheets)
Dates: born, died
Accepts whereabouts: yes
Accept affiliations: yes

Type-specific displayDefaults? Yes, defined in metadata.json
Type-specific header code for website? Yes, computed by outputs.js

### Classification Requirements

See: [[Person Categories]]

Species and ancestry metadata are loosely controlled vocabulary. While it is not predefined, any species used in a person note is expected to have a corresponding creature page, and any ancestry used is expected to have a corresponding ancestry page (though in some cases, a realm might stand in for an ancestry page). 

The usage of subspecies and speciesAlias are somewhat arbitrary. In general:
- species should be used if a page exists for the species
- subspecies should be used if a page exists for both the subspecies and the main species, or if a page theoretically could  exist, and the subspecies is NOT purely a cultural variant. Generally, if a creature has a partOf relationship to another creature, the subordinate page is a subspecies and the other page is the species. Note that in many cases what are currently used as subspecies should properly be ancestries. 
- speciesAlias should be used primarily to give a more meaningful header text for people with unknown species, or other complex situations where the display text and search text diverge. 

## Power
**Tag: `#power`**

Definition: a sentient being who has accreted so much soulstuff, either through their own powerful essence, or as a gift, as to transcend ordinary mortality. See more: [[Metaphysics of Creatures]], [[Divinities and Powers - Discussion]]. The fundamental trait of powers is that they are singular: while they might fall into some common types, they each have a unique origin story. 

The power tag is used for all kinds of divinities, as well as extraplanar powers. Note that this is not simply a place for named demons, for example. If something has a statblock and can be killed in normal combat, it is not a power, it is a person. 

Classification: typeOf (required), subTypeOf, gender
Other: pronouns (only use if different from gender), title
Dates: born, died
Accepts whereabouts: no
Accepts affiliations: yes; typically these would be either a religion, a pantheon, or a realm (e.g., an archfey might be the ruler of a fey domain, while The Mother might be a member of the Eight Divines and Mos Numena)

Type-specific displayDefaults? Yes, defined in metadata.json.
Type-specific header code for website? No. 

### Classification Requirements

See: [[Power Categories]]

Neither typeOf nor subTypeOf are currently controlled vocabulary. These should be used as makes sense, and following existing notes where logical. At some future date these might become controlled vocabulary. subTypeOf need not duplicate affiliations, so for example The Mother is probably typeOf: incorporeal god, subtypeOf blank, with affiliations with Eight Divines and Mos Numena. It is not obvious subTypeOf has any real use here. 

## Place
**Tag: `#place`**

Definition: a physical location in the word. 

The place tag is used for anything that has a (mostly) permanent location in the world. This includes geographic regions and natural features, as well as settlements, structures, and other constructed infrastructure. There is some fuzziness here with what is a place vs an ancestry, and what is a place vs an object. In general, if the subject of the note is defined by physical borders in the world, it is a place, even if the note content is largely about culture or politics. If it is stationary, it is a place even if it is constructed; only things that routinely move (ships, etc) should be treated as objects. 

Classification: typeOf (required), subTypeOf, typeOfAlias, subTypeOfAlias, ancestry
Dates: created, destroyed
Accepts whereabouts: yes, and places commonly use secondary whereabouts to account for multiple ways to categorize a location (e.g., geographic region vs political unit vs watershed)
Accepts affiliations: yes, but rarely; leader affiliations should be set on the person page, not the place page, and normal associations should be reserved for situations like a guildhall where it is useful to track group ownership of a structure. 

Type-specific displayDefaults? Yes, defined in metadata.json
Type-specific header code for website? Yes, computed by outputs.js

### Classification Requirements

Places use a controlled vocabulary for typeOf, which can be one of: settlement, realm, neighborhood, region, watershed, plane, extraplanar domain, planar link, wetlands, forest, plain, desert, inn, buliding, road, holy site, infrastructure, waterway, marine feature, lake, topographical feature, subterranean feature, or landform. 

Place typeOf categories are organized into several broad groups. These are not tagged anywhere, but are meant to be small enough that it is feasible to write simple dataview queries or base filters to pull up all of a category. In the future this may be revised (e.g., an additional layer such as typeCategory might be added to frontmatter, potentially auto-populated). 

**Note: water features, landforms, structures, and infrastructure may be revised***

See [[Place Categories]] for more details about how these are used in practice. 
#### Communities
*Generally related to places where communities exist on a landscape*

- **settlement** is used to describe any note about a current or former community of people; obvious examples are things like villages, towns, and cities, but transient settlements (a camp) and ruined settlements fit here too. There is no specific minimum size, but generally a single house would be considered a structure, not a settlement, and a building complex with a singular purpose (castle, monastery) would also generally be a structure, even if people make their home there. 
- **neighborhood** is used to describe subparts of a settlement; obvious examples are things like wards of Tollen or the North Bank of Chardon. Any note that describes a subdivision of a settlement that is larger than a single building or building complex should use the neighborhood typeOf. 
- **realm** is used to describe collections of settlements; this can be at any level of organization, from small groups like Sembaran manors or Addermanian shires, to intermediate-scale clusters (the Duchy of Wisford), to kingdoms (Sembara), to groups of realms (Dwarven Kingdoms of the Sentinels). Pages which focus on the physical landscape as opposed to the species landscape generally should use the region typeOf not the realm typeOf. Realms that have a magical existence (fey domains, etc), should use the extraplanar domain typeOf. 

#### Geographic Regions
_Generally related to geographic areas of the world._

- **region**: is used to describe any geographic subdivision of the world. While the distinction between "realm" and "region" is a little arbitrary, region pages typically focus on physical geography, topography, climate, etc, instead of politics, law, economy. Generally pages that are clearly about collections of realms (cf [[Dwarven Kingdoms]]; [[Borderlands]]) should be realm, whereas pages that are ambiguous or lean more towards geography should be regions (cf [[Central Dunmar]]; [[Zimkova]]). But this is admittedly a judgement call. 
- **watershed**: is used specifically to describe watersheds, that is collections of rivers and drainage basins. Note this is not used strictly to refer to unique drainage basins, e.g. [[Tyrwinghan Watershed]] describes the drainage basins of several nearby rivers. 

#### Extraplanar
_Related specifically to extraplanar features._

- **plane**: is used to describe pages about planes as a whole (for example, [[Feywild]] or [[Material Plane]]); these should live in Cosmology, not Gazetteer, but otherwise are treated as locations. 
- **extraplanar domain**: is used to describe pages about planar regions where the character of the region is magically influenced by its ruler; the most obvious examples of these are fey realms like [[Twilight's Grace]] or [[Amberglow]], though others may exist and have not been invented yet. This would be an appropriate typeOf for a layer of the [[Abyss]], for example, if such things exist in Taeglar. 
- **planar link**: is used to describe pages about specific [[Planar Connections]], most commonly portals between the Feywild and the Material Plane. This `typeOf` should use `typeOfAlias` to identify whether it is a weak point, a vortex, or a portal; see [[Planar Connections]] for details. 

#### Biomes
*Related to biomes and ecological terrain / ecoregions*

- **wetlands**: is used to describe pages about any kind of wetland, e.g. swamps, bogs, fens, marshes, and similar types of biomes. 
- **forest**: is used to describe pages about any kind of woodlands, from northern boreal forests to rain forests. 
- **grassland**: is used to describe pages about any kind of open, treeless terrain, from prairies to arid scrubland to high moors. 
- **desert**: is used to describe pages about any arid terrain with minimal rain and vegetation. 

#### Water Features
*Related to any kind of water feature, including rivers, lakes, and marine features.*

- **waterway** is used to describe any inland watercourse, whether artificial or nature, including navigable and unnavigable courses
- **lake** is used to describe any notable inland body of water
- **marine feature** is used to describe any oceanic feature, including any type of strait, channel, bay, gulf, as well as seas and oceans

#### Landforms
*Related to any kind of topographical or terrain features.*

- **topographic feature** is used to describe hills, mountains, chasms, valleys, and any other feature that involves significant topographic changes.
- **subterranean feature** is used to describe any underground feature, primarily caves
- **island** is used to describe any island feature

#### Structures
*Related to any kind of building.*

- **inn** is used for inns, taverns, and other places where adventurers commonly find themselves
- **holy site** is used for any building or other site associated with a religion
- **building** is used for all other structures

#### Infrastructure
*Related to other artificial, constructed features that aren't buildings*

- **road** is used for any kind of road or street
- **infrastructure** is used for all other kinds of infrastructure

## Event
**Tag: `#event`**

Definition: A defined event that has a start and end date and represents a description of something that happened at a fixed time. Anything time-related without a defined start and end should use the `#background` tag, most likely. 

The event note expects the following metadata:

Classification:  typeOf (required), ancestry, subTypeOf
Other: partOf
Dates: DR, DR_end
Accepts whereabouts: Yes, though typically only an undated home whereabouts makes sense.
Accept affiliations: No. Events should use partOf to indicate a sub-event within a larger category (e.g., a battle that is part of a war). 

Type-specific displayDefaults? Yes
Type-specific header code for website? Yes

### Classification Requirements

See: [[Event Categories]]

Neither typeOf nor subTypeOf are currently controlled vocabulary, though typeOf may become controlled at some point. These should be used as makes sense, and following existing notes where logical. To indicate sub-events within a larger event, use partOf. 

## Object
**Tag: `#object`**

Definition:

The object note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 

## Group
**Tag: `#group`**

Definition:

The group note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 

## Ancestry
**Tag: `#ancestry`**

Definition:

The ancestry note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 

## Creature
**Tag: `#creature`**

Definition:

The creature note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 

## Session Note
**Tag: `#session-note`**

Definition:

The session-note note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 

## Primary Source
**Tag: `#source`**

Definition:

The source note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 


## Background
**Tag: `#background`**

Definition:

The background note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 


## Meta
**Tag: `#meta`**

Definition:

The meta note expects the following metadata:

Classification: 
Other: 
Dates: 
Accepts whereabouts: 
Accept affiliations: 

Type-specific displayDefaults? 
Type-specific header code for website? 



## Descriptive Tags
***Last update: 12/08/2025***

Every page should have a descriptive tag, excluding pages in meta directories (e.g., any starting with `_` and assets), the Campaign directory, or the Worldbuilding. 

The following descriptive tags are considered canonical. Note that while item pages often have subtags (e.g. `item/vehicle`), these are not consistently used and should be considered obsolete/depreciated, unless otherwise noted. 

* **creature**: a page about a specific type of creature. Can be used for broad types (humans) as well as more specific types (sea hags)
* **object**: a specific item, or a type of item, or a material. 
---
* **organization**: a specific group of people or other type of organization, including things like pantheons or families or clans.
* **culture**: a page describing a specific culture
---
* **session-note**: a page about a specific session
* **source**: a page containing the actual text or a paraphrase of actual in-world information, typically intended to be given to players as is. 
---
* **meta**: a page about pages, for example this page. Does not contain world information, but may contain information about world information. Can also be used for map of content-style pages that are outside the \_MoC folder, for example indexes of NPCs or indexes of events.
* **background**: a conceptual page that describes world background. This is still canonical information (or at least, potentially canonical, depending on the status tags) but it doesn't refer to a specific living being, place, group, thing, or event (i.e. Land Owning in Sembara or Climate Background). A good catch-all for otherwise unclear pages. Includes holidays, which should have a typeOf: holiday and (usually) a religion tag. 

There are three other tags that can be added to clarify the page but one of these items on its own is not sufficient to remove the page from the missing tags list:
* **pc**: a page describing a player character. Use a subtype for the campaign, i.e. pc/greatwar or pc/cleenseau
* **religion**: a page something about a specific religion. Use a subtype to define the type of religion. Also should be used for organization and deity pages that are part of this religion, i.e. religion/mosnumena should get all of the pages about the Mos Numena religion.
* **testcase**: this page makes use of complex Javascript features and is a good page for testing changes with

Pages that do not have any of these tags are listed here [[Missing Tags]].

See: [[Descriptive Tags - Discussion]] for discussion and proposals around tags. 

Descriptive tags are used to determine the page type, which is important for header generation. The page types that have meaningful header automation are `person`, `place`, `organization`, `event`, and `object`. See [[Display Control]] for more. 

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

See: [[People Categories]]

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

Neither typeOf nor subTypeOf are currently controlled vocabulary, though typeOf may become controlled at some point. These should be used as makes sense, and following existing notes where logical. To indicate sub-events within a larger event, use partOf. PartOf should always point to another note.

## Object
**Tag: `#object`**

Definition: The object tag is used for any kind of physical object, including both specific objects (the Crown of Purity, Delwath's Shadow Breastplate), general classes of objects (Drankorian Message Stones), books, materials (chalyte), and vehicles (Vindristjarna, The Emerald Song). 

The object note expects the following metadata:

Classification: typeOf (required), subTypeOf, ancestry
Other: rarity, pcOwner, ddbLink
Dates: created, destroyed
Accepts whereabouts: Yes.
Accept affiliations: Yes.

Type-specific displayDefaults? Yes.
Type-specific header code for website? Yes.

### Classification Requirements

See: [[Object Categories]]

Objects probably should have a better controlled vocabulary for typeOf, and more consistent / clean use of whereabouts, but currently are a bit of a mess. See link above for current state. 

## Group
**Tag: `#group`**

Definition: The group tag is used for notes that contain information about specific groups of people. 

The group note expects the following metadata:

Classification: typeOf, subTypeOf, typeOfAlias, ancestry
Other: partOf
Dates: created, destroyed
Accepts whereabouts: Yes
Accept affiliations: Yes, but typically should only accept primary affiliations, often used for gods. Use partOf for sub-group relationships. 

Type-specific displayDefaults? Yes.
Type-specific header code for website? Yes.

### Classification Requirements

See: [[Group Categories]]

Groups probably should have a better controlled vocabulary for typeOf, and more consistent / clean use of other metadata, but currently are a bit of a mess. See link above for current state. 

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

Definition: Any note about either a general type of creature (e.g., `undead` or `elementals`) or a specific species (e.g., `elf`) uses the creature tag. 

The creature note expects the following metadata:

Classification: typeOf
Other: partOf
Dates: Not allowed.
Accepts whereabouts: Not allowed.
Accept affiliations: Not allowed.

Type-specific displayDefaults? No.
Type-specific header code for website? No.

### Classification Requirements

See: [[Creature Categories]]

Generally, creature notes have little or no frontmatter and no header. typeOf could be used for things like species, creature type, playable species, or similar, but this should grow organically as species are organized. "Subtype" pages (e.g., fire elementals as a subtype of elementals, or hags as a subtype of fey) should probably use partOf relationships. 

## Session Note
**Tag: `#session-note`**

Definition: The session-note tag is used exclusively for session notes. 

The session-note note expects the following metadata:

Classification: campaign
Other: sessionNumber, players, tagline, descTitle, name
Dates: DR, DR_end, realWorldDate
Accepts whereabouts: No.
Accept affiliations:  No.

Type-specific displayDefaults?  No, but should have one.
Type-specific header code for website? No, but should have one.

All metadata is required, and more may be added, see: [[session-manifest-schema.json]].

## Primary Source
**Tag: `#source`**

Definition: The primary source tag is used for notes that represent in-world text, meant to be shared directly with players (e.g., letters, handouts, journals). Notes that summarize in-world text generally should use background instead, but this is a judgement call. 

The source note does not currently expect additional metadata, and does not have a header.
## Background
**Tag: `#background`**

Definition: The background tag is used for world information that does not obviously fit into any of the above categories. This is still canonical information (or at least, potentially canonical, depending on the status tags) but it doesn't refer to a specific living being, place, group, thing, or event (i.e. Land Owning in Sembara or Climate Background). A good catch-all for otherwise unclear pages. 

While generally backgrounds do not expect metadata, and do not have type-specific displayDefaults or type-specific header code for the website, typeOf is occasionally used for more specific classification. 

See: [[Background Categories]]

## Meta
**Tag: `#meta`**

Definition: The meta tag is used for pages about pages, for example this page. Does not contain world information, but may contain information about world information. Can also be used for map of content-style pages that are outside the \_MoC folder, for example indexes of NPCs or indexes of events. Can also be used for pages about mechanics or other player-facing (as opposed to character-facing) details. 

The meta tag does not currently expect additional metadata, and does not have a header.


## Descriptive Tags
***Last update: 12/08/2025***

* **object**: a specific item, or a type of item, or a material. 
* **organization**: a specific group of people or other type of organization, including things like pantheons or families or clans.
* **culture**: a page describing a specific culture

There are three other tags that can be added to clarify the page but one of these items on its own is not sufficient to remove the page from the missing tags list:
* **religion**: a page something about a specific religion. Use a subtype to define the type of religion. Also should be used for organization and deity pages that are part of this religion, i.e. religion/mosnumena should get all of the pages about the Mos Numena religion.
* **testcase**: this page makes use of complex Javascript features and is a good page for testing changes with

Pages that do not have any of these tags are listed here [[Missing Tags]].

See: [[Descriptive Tags - Discussion]] for discussion and proposals around tags. 

Descriptive tags are used to determine the page type, which is important for header generation. The page types that have meaningful header automation are `person`, `place`, `organization`, `event`, and `object`. See [[Display Control]] for more. 

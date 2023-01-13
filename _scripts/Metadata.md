This note outlines all the metadata used by the header scripts and other associated scripts.

Note that core does not mean required (only type and name are really required), but without it there will be missing information in the header. Of course, some core items should be blank if they haven't happened yet (died, reignEnd, etc). 

| metadata key  | scripts (plugin)                                                         | optional/core?        | values                             | used for                                                                                                             |
| ------------- | ------------------------------------------------------------------------ | --------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| type          | all (eventually)                                                         | core                  | NPC, Building, Place, PC, Item, Ruler         | sets the expected yaml frontmatter, sets the header format. Additional types will be added over time.                |
| name          | generateHeader (templater)                                               | core                  | any string                         | sets the h1 text for the note in all headers                                                                         |
| species       | generateHeader (templater)                                               | core (NPC, Ruler)     | any string                         | sets the species displayed in the header                                                                             |
| ancestry      | generateHeader (templater)                                               | core (NPC, Ruler)     | any string                         | sets the ancestry displayed in the header                                                                            |
| pronouns      | metadataUtils (customJS), generateHeader (templater)                     | optional (NPC, Ruler) | any string                         | overrides default pronoun calculation in metadataUtils.get_Pronouns()                                                |
| gender        | metadataUtils (customJS), generateHeader (templater)                     | core (NPC, Ruler)     | male, female, nonbinary            | determines pronouns in NPC and Ruler headers                                                                         |
| born          | metadataUtils (customJS), get_PageDatedValue, get_RegnalValue (dataview) | core (NPC, Ruler)     | any year                           | calculate age in header, determine the year something started existing in metadataUtils.get_existYear                |
| created       | metadataUtils (customJS), get_PageDatedValue (dataview)                  | core (Item)           | any year                           | calculate age in header, determine the year something started existing in metadataUtils.get_existYear                |
| built         | metadataUtils (customJS), get_PageDatedValue (dataview)                  | core (Building)       | any year                           | calculate age in header, determine the year something started existing in metadataUtils.get_existYear                |
| died          | get_PageDatedValue, get_RegnalValue (dataview)                           | core (NPC, Ruler)     | any year                           | calculate death date and age at death in header                                                                      |
| destroyed     | get_PageDatedValue (dataview)                                            | core (Building, Item) | any year                           | calculate destruction date and age at destruction in header                                                          |
| preExistError | get_PageDatedValue (dataview)                                            | optional (any)        | any string                         | overrides default message to report when current year is before year born/created/built                              |
| startPrefix   | get_PageDatedValue (dataview)                                            | optional (any)        | any string                         | overrides default value associated with year of birth/creation in age string in header                               |
| endPrefix     | get_PageDatedValue (dataview)                                            | optional  (any)       | any string                         | overrides default value associated with year of death/destruction in age string in header                            |
| endStatus     | get_PageDatedValue (dataview)                                            | optional  (any)       | any string                         | overrides default "died at"/"destroyed at" string (use for petrified, burnt down, etc)                               |
| yearOverride  | get_PageDatedValue, get_RegnalValue (dataview)                           | optional (debugging)  | any year                           | use to override the Fantasy Calendar today date, mostly for debugging purposes                                       |
| reignStart    | get_RegnalValue (dataview)                                               | core (Ruler)          | any year                           | calculate reign start string and reign length in header                                                              |
| reignEnd      | get_RegnalValue (dataview)                                               | core (Ruler)          | any year                           | calculate reign end string and reign length in header. Redundant if equal to died.                                   |
| home          | generateHeader (templater), getLocation (templater)                      | core (NPC, Ruler)     | any string (parts comma-delimited) | sets the "Based in: " text in the header. Each comma-delimited piece will be linked if a file exists with that name. |
| homeRegion    | generateHeader (templater), getLocation (templater)                      | core (NPC, Ruler)     | any string                         | sets the last part of the "Based in: " text in the header. Usually a fairly big region, usually should be linkable.  |
| origin        | generateHeader (templater), getLocation (templater)                      | optional (NPC, Ruler) | any string                         | works like home but for origin, if relevant                                                                          |
| originRegion  | generateHeader (templater), getLocation (templater)                      | optional (NPC, Ruler) | any string                         | works like homeRegion, but for originRegion, if relevant                                                             |
| tags          | none                                                                     | core                  | array of strings                   | tagging, see below                                                                                                   |
| affiliations  | none                                                                     | core (NPC, Ruler)     | array of strings                   | used to link affiliations to people                                                                                  |
| aliases       | none                                                                     | core                  | array of strings                   | used for aliases, to simplify auto-linked                                                                            |


Values that are not used by any scripts, and not currently really implemented, but might be useful:
- whereabouts: as discussed, a way to track location in time that would be more flexible than location / locationRegion fixed frontmatter
- currentOwner: for items, who has the thing now. although usually not relevant, this could also be done like whereabouts to track ownership over time. 
- maker: for items, who made it
- player, campaing: for PCs
- location, locationRegion: for buildings and placed, functioning like home/homeRegion for people
- population: for places
- pronunciation: for anything
- ddbLink: for items, a link to the mechanics of the item on D&D Beyond. Could also extend to PCs, species. 
- languages: for people, indicating the languages they know
- family: for people, used to track familial affiliations (dwarven clans, halfling families, possibly orc hordes and deno'qai tribes too)
- lastSeenBy: campaign-specific value of the date the NPC's location was last known by the party. Would be used to auto-populate a Current Location field based on campaign + date information.


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
| home          | generateHeader (templater), getLocation (templater)                      | obsolete (NPC, Ruler) | any string (parts comma-delimited) | sets the "Based in: " text in the header. Each comma-delimited piece will be linked if a file exists with that name. |
| homeRegion    | generateHeader (templater), getLocation (templater)                      | obsolete (NPC, Ruler) | any string                         | sets the last part of the "Based in: " text in the header. Usually a fairly big region, usually should be linkable.  |
| origin        | generateHeader (templater), getLocation (templater)                      | obsolete (NPC, Ruler) | any string                         | works like home but for origin, if relevant                                                                          |
| originRegion  | generateHeader (templater), getLocation (templater)                      | obsolete (NPC, Ruler) | any string                         | works like homeRegion, but for originRegion, if relevant                                                             |
| tags          | none                                                                     | core                  | array of strings                   | tagging, see below                                                                                                   |
| affiliations  | none                                                                     | core (NPC, Ruler)     | array of strings                   | used to link affiliations to people                                                                                  |
| aliases       | none                                                                     | core                  | array of strings                   | used for aliases, to simplify auto-linked                                                                            |
| maker         | generateHeader (templater)                                               | core (Item)           | string                             | used to set the maker of an item |
| owner         | generateHeader (templater)                                               | core (Item)           | string                             | used to set the owner of an item |
| dbbLink       | generateHeader (templater)                                               | core (Item)           | url                                | used to set the mechanics link for an item |
| gpValue       | generateHeader (templater)                                               | core (Item)           | number                             | used to set the GP Value of an item |
| gpValueMin    | generateHeader (templater)                                               | optional (Item)       | number                             | if the GP Value is not set, will be used as a floor on the item value |
| gpValueMax    | generateHeader (templater)                                               | optional (Item)       | number                             | if the GP Value is not set, will be used as a ceiling on the item value |
Values that are not used by any scripts, and not currently really implemented, but might be useful:
- whereabouts: as discussed, a way to track location in time that would be more flexible than location / locationRegion fixed frontmatter
- currentOwner: for items, who has the thing now. although usually not relevant, this could also be done like whereabouts to track ownership over time. 
- player, campaign: for PCs
- location, locationRegion: for buildings and places, functioning like home/homeRegion for people
- population: for places
- pronunciation: for anything
- ddbLink: for items, a link to the mechanics of the item on D&D Beyond. Could also extend to PCs, species. 
- languages: for people, indicating the languages they know
- family: for people, used to track familial affiliations (dwarven clans, halfling families, possibly orc hordes and deno'qai tribes too)
- lastSeenBy: campaign-specific value of the date the NPC's location was last known by the party. Would be used to auto-populate a Current Location field based on campaign + date information.



# Instructions for ChatGPT

I'd like your help creating Markdown pages for NPCs in my D&D campaign. I will give you information about NPCs, and I want you to follow the instructions below to generate yaml frontmatter for the markdown page.

## NPC YAML Format Instructions

### Required Fields:

- `type`: Always set to `NPC`.
    
- `name`: The name of the NPC.
    
- `species`: The species of the NPC.
    
- `ancestry`: An optional field indicating the NPC's lineage or heritage. If not provided, leave it blank.
    
- `gender`: Can be `male`, `female`, `enby`, or any other specified gender.
    
- `born`: The year the NPC was born. Use context to determine if not directly provided.
    
- `died`: The year the NPC died. If the NPC is still alive, this should be blank.
    
- `title`: The title of the NPC, e.g., "Lord." If not provided, leave it blank.
    
- `family`: The family name of the NPC. If not provided, leave it blank.
    
- `affiliations`: Groups the NPC is associated with. Use as a list.
    
- `aliases`: Other names or nicknames for the NPC. Use as a list.
    
- `tags`: Specific identifiers or categories for the NPC. Use as a list. 
    

### Location Tracking:

- `lastSeenByParty`: Tracks the last known location of the NPC relative to the party.
    
    - `date`: Date format is "YYYY-MM-DD."
        
    - `prefix`: Always set to `DuFr`.
        
- `whereabouts`: Tracks the NPC's location over time. Use the following types:
    
    - `origin`: Where the NPC was born (date should be Jan 1 of birth year).
        
    - `home`: Where the NPC is based (date should be Jan 2 of birth year unless specified otherwise).
        
    - `excursion`: Represents trips (only include if mentioned).
        

### Presentation:

- Enclose the YAML block with `---` at the start and end.
    
- After the YAML block, provide a concise markdown description (1-2 sentences) summarizing the NPC.

Template:
```
---
type: NPC
name: 
species: 
ancestry: 
gender: 
born: 
died: 
title: 
family: 
affiliations: 
  - 
aliases: 
  - 
tags: 
  - 
lastSeenByParty: 
  - { date: YYYY-MM-DD, prefix: DuFr }
whereabouts: 
  - { date: YYYY-01-01, place: "", region: "", type: origin }
  - { date: YYYY-01-02, place: "", region: "", type: home }
---

```



### Reformat Note Instructions

I am going to give you potentially messy markdown text describing NPCs in my D&D campaign. When I tell you to reformat note, I want you to follow these instructions. 

**Reformat Note Instructions:**

1. If the note I give you includes any kind of yaml frontmatter or code, delete that.
2. Start with a **1-2 sentence brief introduction** to the NPC. Do not use bold here. 
3. Create an **## Overview** section that has up to a paragraph of text. This should be copied or restructured from the provided text, focusing on turning it into coherent and grammatically correct sentences.
4. Provide a **## Description** section, which should consist of a few sentences describing the NPC's physical appearance or their usual surroundings.
5. Add a **## Relationships** section as a bullet-point list of inferred relationships with other NPCs or organizations from the text.
6. Create an **## Events** section that offers a summary of events inferred to have happened to or involving the NPC.
7. Add a **## Rumors and Information** section as a bullet-pointed list of rumors, information, or other details about the NPC that player characters might know.
8. Construct an **## Roleplaying Notes** section when applicable, delivering a bullet-point list of roleplaying tips for a DM running the NPC based on the provided details.
9. Conclude with a **## Secrets** section that contains DM-only information. This will generally be based on information enclosed in `%%SECRET[1]%%` tags in the provided markdown.


Try to include as much of the text in the note as possible, just moving it to the appropriate section and deleting redundancy. If there's insufficient information, the **## Relationships**, **## Events**, **## Rumors and Information**, **## Roleplaying Notes**, and **## Secrets** sections can be omitted. However, do your best to fill these in, even if you have to invent a few details. 

Please don't include any addition sections. However, if the information I provide cannot be reasonably moved to one of the sections listed above, you can include a final ## Other Notes section at the end.


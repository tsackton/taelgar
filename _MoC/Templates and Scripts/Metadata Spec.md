<<<<<<< HEAD
# Metadata conventions
=======
Metadata conventions:

- Metadata entries use camelCase when possible. Because fantasy calendar uses kebab/dash case for fc-date, dates use dash case.
- Required metadata is always displayed in a file, even if it is null. Optional metadata should only be displayed if it is 




The following metadata is used:
>>>>>>> 0ca5ae4 (medata clean, _MOC_ work)

- Metadata entries use camelCase when possible. Because fantasy calendar uses kebab/dash case for fc-date, dates use dash case.
- Required metadata is always displayed in a file, even if it is null. Optional metadata should only be displayed if it has a non-null value.
- Metadata defaults can be defined as null, {guess}, or a fixed value. Metadata with a {guess} default should have a function implemented to attempt to derive a value based on file properties (path, name, etc)
- Metadata is defined by type; each type has different metadata, and required flags and defaults can vary as well. 
- The formal metadata spec consists of a set of json files and a file that defines which metadata files are combined in order to create the input metadata for each type. Each json file consists of an entry for each metadata, with the following:
  ```yaml
  key : {required : logical, default : some value or null }
  ```

## Updating metadata

- As metadata standards have changed, some old tags exist. In general, these conversions are handled only by Python update code, and can probably be ignored in templater and javascript code (but they are listed in the table as needed).
- Whereabouts requires special handling to conform to standard, which is implemented in Python update code. Templater and javascript code can assume whereabouts meets current standards. 

# Metadata Used

## Defined Types

The following types of notes are defined and have specific metadata. 

**People**:
- type: Ruler
- type: NPC
- type: PC
- type: Organization

Most people are NPCs. Rulers are NPCs that add metadata about regnal years, and have alternate info boxes. PCs add information about players, and might have alternate info boxes, but are not fully implemented. 

Organizations are a special class that represents a collection of people (a family, a clan, a secret society, an adventuring party, etc). Beyond founded / disbanded dates, if they exist, it is not clear there is anything useful to track with organizations. Primarily, these exist to allow people to be tagged to specific groups. 

**Locations**:
- type: Building
- type: Place
- type: Settlement

Places are a generic location, such as forests, rivers, mountains, kingdoms, roads, oceans. Places can have partOf relationships (one place can be part of another place). Buildings are a special type of place used to represent specific structures that, generally speaking, cannot have sublocations (buildings can be partOf another place, but nothing can be partOf a building). For example, the Monastery of Bhishma would be a place, but the Hall of Stories would be a building. Settlements are a special type of place used to represent specific named settlements, generally towns, villages, or cities, and often have additional metadata needs, such as population information.

Might consider additional location types: 
- something that tags specific civilizations / political units / cultures, however defined, that could be used for example to get all the Sembaran places. might be overkill and/or easier to just use nested partOf tags. Absent this, however, it is not obvious what to do with cultural descriptors or political organizations. 
- something that tags specific geographic regions with fixed boundaries on the map, similar to current gazetteer folder structure; could be used for queries to get all the defined places in a particular region of the word, but might not have a lot of value beyond the folder structure (although could be used to generate e.g. dynamic MOC pages, and could have more granulate organization with multiple levels, and could allow features such as rivers to exist in multiple regions)
- could also consider breaking places up, considering geographic features (rivers, forests, oceans, lakes) separately from human features (roads, mostly)

**Things:**
- type: Item

Items represent physical things in the world. One challege is how to handle unique items ("Chalice of the Runepriest") vs non-unique items (books, common magic items, etc). Also not obvious if it makes sense to have just one type of thing, or if we need separate metadata for various kinds of things. Lean no, but uncertain. 

**Events:**
- type: Event
- type: Holiday

Events are anything that occurs in time. Holidays are a special type of event that is expected to be recurring. 

**Meta:**
- type: Timeline
- type: Session

Meta are things that are used for notes that collect game information, and generally don't have metadata representing in-game information. Timelines are collections of events; Sessions are notes containing session notes and other session information. 

Timelines could alternately be in events as a way to represent notes with sequential historical information, e.g. "Timeline of Sembaran History"

**Other:**
 - type: Other

This is used to indicate "this file has metadata that is not in part of the universal metadata definition and shouldn't be modified by metadata cleanup scripts."

Other things that could use tags, maybe: 
- Religions
- Gods
- Other Planes
- Species
## Metadata By Type
### Common Metadata

All notes share this metadata.

| Name            | Description                                                                                          | Required | Default                             |
| --------------- | ---------------------------------------------------------------------------------------------------- | -------- | ----------------------------------- |
| type            | one of Ruler, PC, NPC, Item, Place, Building, Organization, Event, Holiday, Timeline, Session, Other | yes      | guess from folder location, or none |
| tags            | tbd                                                                                                  | yes      | none                                |
| name            | the name, set mostly when the name and filename are different                                   | no       | none                                |
| pageTargetDate  | used to override the current date for a page                                                         | no       | none                                |
| aliases         | alternate names - used by Obsidian                                                                   | no       | none                                |
| pronunciation   | the phonetic pronunciation of the page                                                               | no       | none                                |
| displayDefaults | dictionary of strings, used to hold display defaults for header generation                           | yes      | depends on type                                    |

displayDefaults generically is the following:
```yaml
displayDefaults : { startStatus : "created", startPrefix: "created", endStatus : "destroyed", endPrefix: "destroyed", preExistError : "**(doesn't exist yet)**"}
```
### People Metadata

| Name            | Description                                                                                                        | Required         | Default |
| --------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------- | ------- |
| reignEnd        | [[Formatting#Dates\|any date]] (type: Ruler only)                                                                  | yes: Rulers only | died    |
| reignStart      | [[Formatting#Dates\|any date]] (type: Ruler only)                                                                  | yes: Rulers only | none    |
| died            | [[Formatting#Dates\|any date]]                                                                                     | yes: Rulers only | none    |
| player          | indicates real world player (type: PC only)                                                                        | yes: PCs only    | none    |
| ka              | the ka of the elf (species: elf only)                                                                              | yes: Elves only  | none    |
| species         | string - links to page with matching speciesDescriptor                                                             | yes              | none    |
| ancestry        | string - links to page with matching cultureDescriptor                                                             | yes              | none    |
| gender          | male, female, nonbinary - used to calculate pronouns                                                               | yes              | none    |
| born            | [[Formatting#Dates\|any date]]                                                                                     | yes              | none (for elves, autocalculate from ka?)   |
| ddbLink         | link to page on D&D beyond (type: PC only)                                                                         | no               | none    |
| lastSeenByParty | See [[Whereabouts and Last Seen By Party]]                                                                         | no               | none    |
| whereabouts     | See [[Whereabouts and Location Specification]]                                                                     | no               | none    |
| title           | a title like Lord, Sir, etc. Used in header generation                                                             | no               | none    |
| family          | a single value; used for noble house, clan, etc. Expected to be used in dataview queries                           | no               | none    |
| affiliations    | list of string; any organizations or groups the person is associated with. Expected to be used in dataview queries | no               | none    |
| pronouns        | string - overrides pronoun calculation                                                                             | no               | none    |

displayDefaults for people is the following:
```yaml
displayDefaults : { startStatus : "born", startPrefix: "b.", endStatus : "died", endPrefix: "d.", preExistError : "**(Not born yet)**"}
```
### Organization Metadata
| Name      | Description                                             | Required | Default |
| --------- | ------------------------------------------------------- | -------- | ------- |
| created   | Date. Used to define when an organization was founded   | no       | none    |
| destroyed | Date. Used to define when an organization was disbanded | no       | none    |

displayDefaults for organization is the following:
```yaml
displayDefaults : { startStatus : "founded", startPrefix: "founded", endStatus : "disbanded", endPrefix: "disbanded", preExistError : "**(Not founded yet)**"}
```

=== EDIT LINE ===
### Places Metadata
| Name                  | Description        |
|--------|---------------| 
| created | Date. Used to define when a place was created or founded |
| destroyed | Date. Used to define when a place ceased to exist in a meaningful way |
| coordinates | Leaflet location coordinates |
| population | The exact or general population. Expected to be used in header generation |
| politicalUnit | The political unit the place belongs to. Expected to be used in dataview queries and header generation |

### Buildings or Locations in Towns

| Name                  | Description        |
|--------|---------------| 
| created | Date. Used to define when an item was created |
| destroyed | Date. Used to define when an item was destroyed |
| owner | who (or what group) owns an item, if known/relevant |
| place | the town or region the building is in |
| endStatus | string. optional. changes the text from destroyed, i.e. set to burnt down |
| endPrefix | string. optional, changes the text from destroyed i.e. from built 1700 - destroyed 1720 |
| startPrefix | string. optional changes the text from built i.e. in from built 1700|

### Items Metadata

| Name        | Description                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------- |
| created     | Date. Used to define when an item was created                                                   |
| destroyed   | Date. Used to define when an item was destroyed                                                 |
| magical     | true/yes or false/no - used to define if an item is magic                                       |
| maker       | Who made an item, if known/relevant                                                             |
| owner       | who (or what group) owns an item, if known/relevant                                             |
| ddbLink     | link to page on D&D beyond for item                                                             |
| endStatus   | string. optional. changes the text from destroyed, i.e. set to thrown into volcano              |
| endPrefix   | string. optional, changes the text from destroyed i.e. from created 1700 - destroyed 1720       |
| startPrefix | string. optioa. changes the text from created i.e. in from created 1700                         |
| unique      | True/False. set to True if this describes a unique item, False if this describes a generic item |

### Other

| Name                  | Description        |
|--------|---------------| 
| fc-date      | Used to tag an item to the Fantasy Calendar. Use for holidays only, do not use for one-off events |
| fc-end |  Used to tag the end date of something to Fantasy Calendar when it is multi-day |
| fc-display-name |  Used to change how something is displayed in Fantasy Calendar |
|name | the name; optional, set mostly when the name and filename are different |
| pageTargetDate | used to override the current date for a page |
| aliases | alternate names - used by Obsidian | 
| DR | used to define a date for an event | 
| DR_end | used to define the end date of an event |
| speciesDescriptor | used to tag a page as being the source of a species |
| cultureDescriptor | used to tag a page as being the source of a culture |

### Session Notes

| Name                  | Description        |
|--------|---------------| 
| sessionNumber      | Index of the session |
| realWorldDate |  Real-world date of a session |
| players | a list of who played in a session, if desired. Use character names |


### Obsolete Tags
* yearOverride - replaced by pageTargetDate
* campaign - replaced by affiliations
* home, homeRegion, location, locationRegion, origin, originRegion - replaced by whereabouts
* fc-calendar and fc-category: no longer used/needed, only holidays tagged to calendar
* taelgar-date: replaced with DR
* taelgar-date-end: replaced with DR_end
* realDate: replaced with realWorldDate
* subtype: no clear value; replace with nothing
* currentOwner: replaced with owner
* dbbLink: replace with ddbLink (d d beyond link)
* tag: typo for tags; replace with tags
* built: replace with created
* sessionStartTime, sessionEndDate, sessionEndTime: replace with realWorldDate or DR and DR_end
* summary: replace with text in body or a heading



 






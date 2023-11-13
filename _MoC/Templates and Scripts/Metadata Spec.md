Metadata conventions:

- Metadata entries use camelCase when possible. Because fantasy calendar uses kebab/dash case for fc-date, dates use dash case.
- Required metadata is always displayed in a file, even if it is null. Optional metadata should only be displayed if it is 




The following metadata is used:


### Common Metadata

| Name                  | Description        |
|--------|---------------| 
| type      | one of Ruler, PC, NPC, Item, Place, Building |
| tags |  tbd |
|name | the name; optional, set mostly when the name and filename are different |
| pageTargetDate | used to override the current date for a page |
| aliases | alternate names - used by Obsidian | 
| pronouciation | the phonetic pronouciation of the page |

### People Metadata

| Name                  | Description        |
|--------|---------------| 
| born      | [[Formatting#Dates\|any date]] |
| died | [[Formatting#Dates\|any date]] |
| reignStart | [[Formatting#Dates\|any date]] (type: Ruler only) |
| reignEnd | [[Formatting#Dates\|any date]] (type: Ruler only; defaults to died) |
| gender | male, female, nonbinary - used to calculate pronouns |
| pronouns | string - overrides pronoun calculation | 
| ancestry | string - links to page with matching cultureDescriptor | 
| species | string - links to page with matching speciesDescriptor | 
| affiliations | list of string; any organizations or groups the person is associated with. Expected to be used in dataview queries |
 | family | a single value; used for noble house, clan, etc. Expected to be used in dataview queries |
| title | a title like Lord, Sir, etc. Used in header generation |
| whereabouts | See [[Whereabouts and Location Specification]] | 
| lastSeenByParty | See [[Whereabouts and Last Seen By Party]] |
| player | For PCs only; indicates real world player |
| ka | elves only. the ka of the elf |
| endStatus | string. optional. changes the text from died, i.e. set to killed by orcs instead of generically died |
| ddbLink | link to page on D&D beyond for PC; PCs only |
| endPrefix | string. optional, changes the text from d. i.e. from b. 1700 - d. 1720 |
| startPrefix | string. optioa. changes the text from b. i.e. in from b. 1700|

### Places
| Name                  | Description        |
|--------|---------------| 
| created | Date. Used to define when an item was created |
| destroyed | Date. Used to define when an item was destroyed |
| location | Leaflet location coordinates |
| population | The exact or general population. Expected to be used in header generation |
| politicalUnit | The political unit the place belongs to. Expected to be used in dataview queries and header generation |
### Items

| Name                  | Description        |
|--------|---------------| 
| created | Date. Used to define when an item was created |
| destroyed | Date. Used to define when an item was destroyed |
| magical     | true/yes or false/no - used to define if an item is magic |
| maker | Who made an item, if known/relevant |
| owner | who (or what group) owns an item, if known/relevant |
| ddbLink | link to page on D&D beyond for item |
| endStatus | string. optional. changes the text from destroyed, i.e. set to thrown into volcano |
| endPrefix | string. optional, changes the text from destroyed i.e. from created 1700 - destroyed 1720 |
| startPrefix | string. optioa. changes the text from created i.e. in from created 1700|

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



 






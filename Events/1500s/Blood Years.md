---
headerVersion: 2023.11.25
tags: [event]
name: Blood Years
DR: 1545
DR_end: 1600
dm_notes: none
dm_owner: none
---
# The Blood Years
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`

An informal name for the roughly fifty year period after the [[Great War]], marked by continued conflict in the many parts of the world.

## Major Events of the Blood Years


```dataviewjs
await dv.view("_scripts/view/get_EventsTable", { yearStart: 1545, yearEnd: 1600, pageFilter: "#event-source",includeAll: false } )
```


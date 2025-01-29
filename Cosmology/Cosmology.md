---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Cosmology


## Open Tasks



## File Organization



## Staging

These are staging pages linked to notes in the Cosmology directory. 
```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC
```

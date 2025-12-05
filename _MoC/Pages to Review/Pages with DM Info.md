# Pages with DM Info

These are pages that are complete status-wise, but have DM information not on the page in question. If pages have status tags indicating `stub`, `update`, `check`, `needswork` they are not included here, but if the only status is `cleanup` or `metadata` they are included. 
## Important DM Information, Tim

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner = "tim" 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Color DM Information, Tim
```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner = "tim" 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```


## Important DM Information, Mike

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner = "mike" 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```


## Color DM Information, Mike

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner = "mike" 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Important DM Information, Neither Mike nor Tim

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_owner as DM, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner != "mike" AND dm_owner != "tim" AND dm_owner != "player"
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```


## Color DM Information, Neither Mike nor Tim

These should hopefully have notes about where the color information comes from. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_owner as DM, length(file.inlinks) as Backlinks
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner != "mike" AND dm_owner != "tim" AND dm_owner != "player"
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

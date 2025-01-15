These are pages that are complete status-wise, but have DM information not on the page in question. If pages have status tags indicating `stub`, `update`, `check`, `needswork` they are not included here, but if the only status is `cleanup` or `metadata` they are included. 
## Important DM Information, Tim

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner = "tim" 
sort file.path
```

## Color DM Information, Tim

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner = "tim" 
sort file.path
```


## Important DM Information, Mike

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner = "mike" 
sort file.path
```


## Color DM Information, Mike

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner = "mike" 
sort file.path
```

## Important DM Information, Neither Mike nor Tim

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_owner as DM
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "important" AND dm_owner != "mike" AND dm_owner != "tim" AND dm_owner != "player"
sort file.path
```


## Color DM Information, Neither Mike nor Tim

These should hopefully have notes about where the color information comes from. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_owner as DM
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !#status/needswork AND !#status/stub AND !#status/check AND !#status/update
WHERE dm_notes = "color" AND dm_owner != "mike" AND dm_owner != "tim" 
sort file.path
```

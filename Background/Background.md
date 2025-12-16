---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Background

This directory generally should contain **meta** pages almost exclusively. Not intended to be published, but rather intended to be a place to store canonical information that informs worldbuliding but is not directly player-facing. 

## Note Categories

Excludes missing tags, which should be caught by [[Missing Tags]]

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "Type",
  split(Combo, "\\|")[2] AS "SubType",
split(Combo, "\\|")[3] AS "Ancestry",
  length(rows) AS "Count"

FROM "Background" 
FLATTEN file.tags AS tag
WHERE !startswith(tag, "#status")
GROUP BY (tag + "|" + default(typeof, "none") + "|" + default(subtypeof, "none") + "|" + default(ancestry, "none")) AS Combo
SORT Combo ASC

```

## Note Ownership

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "DM Owner",
  length(rows) AS "Count"

FROM "Background" 
GROUP BY (default(dm_owner, "missing") + "|" + default(dm_notes, "missing")) AS Combo
SORT Combo ASC

```

### Nonstandard DM Owner

Pages that have dm_owner not in: tim, mike, joint, player, none

```dataview
list from "Background"
where dm_owner != "tim" and dm_owner != "mike" and dm_owner != "joint" and dm_owner != "none"
```

### Selected DM Owner

selected:: tim

```dataview
list from "Background"
where dm_owner = this.selected
```

## Note Status

lastChecked:: 2025-12-01

```dataview
list from "Background" and !"Background/Background.md" where file.mtime > this.lastChecked
```


### Status: Needs Work

Includes stubs and active

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/", "") AS Status
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


### Status: Check

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

### Status: Cleanup

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Publishable Pages

Pages with no publish exclusions. 

```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM "Background"
WHERE !excludePublish
SORT length(file.inlinks) DESC

```

Pages with non-"all" publish exclusions

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    exPub as "Publish Exclusions"
FROM "Background"
WHERE !contains(excludePublish, "all") and excludePublish
FLATTEN excludePublish as exPub
SORT length(file.inlinks) DESC

```

## Unnamed In-Links

Pages that link to a background page and are currently unnamed. 
```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM ""
WHERE 
    startswith(file.name, "~") AND
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Background")))
SORT length(file.inlinks) DESC

```

## Staging

These are staging pages linked to pages in the Background directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Background")))
SORT length(file.inlinks) DESC
```


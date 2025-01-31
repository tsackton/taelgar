---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Background

This directory generally should contain **meta** pages almost exclusively. Not intended to be published, but rather intended to be a place to store canonical information that informs worldbuliding but is not directly player-facing. 

## Tagging

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


## Needs Work

Cosmology pages that are stubs or need work.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/", "") AS Status
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


## Check

Cosmology pages that need checking. 

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

## Cleanup

Pages that need cleanup.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Background"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Publish Exclusions

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    pubEx as "Publish Exclusions"
FROM "Background"
WHERE excludePublish
FLATTEN excludePublish as pubEx
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

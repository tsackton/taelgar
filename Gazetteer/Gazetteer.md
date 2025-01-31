---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Gazetteer

This directory contains **character-facing**, **meta**, and **in-world** pages about the places on Taelgar.

## Tagging

```dataview
TABLE WITHOUT ID
split(Combo, "\\|")[0] as "Region",
  split(Combo, "\\|")[1] AS "Descriptive Tag",
  length(rows) AS "Count"

FROM "Gazetteer" 
FLATTEN file.tags AS tag 
WHERE !startswith(tag, "#status")
GROUP BY (default(split(file.folder, "/")[1], "Root") + "|" + tag) AS Combo
SORT Combo ASC

```



## Needs Work

Gazetteer pages that are stubs or need work.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/", "") AS Status
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


## Check

Gazetteer pages that need checking. 

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

## Cleanup

Gazetteer pages that need cleanup.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Publish Exclusions

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    pubEx as "Publish Exclusions"
FROM "Gazetteer"
WHERE excludePublish
FLATTEN excludePublish as pubEx
SORT length(file.inlinks) DESC

```

## Unnamed In-Links

Pages that link to a cosmology page and are currently unnamed. 
```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM ""
WHERE 
    startswith(file.name, "~") AND
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Gazetteer")))
SORT length(file.inlinks) DESC

```

## Staging

These are staging pages linked to pages in the Gazetteer directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Gazetteer")))
SORT length(file.inlinks) DESC
```

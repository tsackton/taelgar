---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Cosmology

This directory contains **in-world** pages about the planes and related concepts. Could be published as is, or selectively, or not at all, as desired.  

## Tagging

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "Type",
  split(Combo, "\\|")[2] AS "SubType",
    split(Combo, "\\|")[3] AS "Ancestry",
  length(rows) AS "Count"

FROM "Cosmology" 
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
FROM "Cosmology"
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
FROM "Cosmology"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

## Cleanup

Cosmology pages that need cleanup.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Cosmology"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Staging

These are staging pages linked to pages in the Cosmology directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC
```

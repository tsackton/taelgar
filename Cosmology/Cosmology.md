---
lintedAt: "2026-08-25T23:38:37-04:00"
lintVersion: "3.5"
tags: [meta]
name: Cosmology
noPublish: true
dm_owner: none
dm_notes: none
POV: modern
---
# Cosmology

This directory contains **in-world** pages about the planes and related concepts. Could be published as is, or selectively, or not at all, as desired.  

Open Questions:
- [[Cosmology - Open Questions]]

## Tagging Information

Excludes missing tags, which should be caught by [[Missing Tags]]

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

## DM Frontmatter Info

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "DM Owner",
  split(Combo, "\\|")[1] AS "DM Notes",
  length(rows) AS "Count"

FROM "Cosmology" 
GROUP BY (default(dm_owner, "missing") + "|" + default(dm_notes, "missing")) AS Combo
SORT Combo ASC

```

### DM Notes: Cleanup

Pages that have anything except none in dm_notes

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    dm_notes AS Notes
FROM "Cosmology"
WHERE dm_notes != "none" or !dm_notes
SORT dm_notes
```


### Nonstandard DM Owner

Pages that have dm_owner not in: tim, mike, joint, player, none

```dataview
TABLE WITHOUT ID
  file.link AS "File",
  length(file.inlinks) AS "Backlinks",
  dm_owner AS "Owner"
FROM "Cosmology"
WHERE typeof(dm_owner) != "string"
   OR !regexmatch(
     "^\\s*(tim|mike|joint|player|none)\\s*(,\\s*(tim|mike|joint|player|none)\\s*)*$",
     lower(string(dm_owner))
   )
```


## Pages with Status Tags
### Status: Needs Work

Includes stubs and active

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/", "") AS Status
FROM "Cosmology"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


### Status: Check

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Cosmology"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

### Status: Cleanup

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Cosmology"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Publish Exclusion Pages

Pages with publish exclusions. 

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    exPub as "Publish Exclusion"
FROM "Cosmology"
WHERE excludePublish
FLATTEN excludePublish as exPub
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
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC

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

%%^povNotes:v1%%
Temporal coverage: broadly modern; this maintenance page describes the current organization and review views for the Cosmology directory.
%%^End%%

---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
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

```dataviewjs
// Define the list of allowed owners
const allowedOwners = ["tim", "mike", "joint", "player", "none"];

// Fetch all pages from the "Background" directory
const pages = dv.pages('"Cosmology"');

// Filter pages where dm_owner contains any owner not in allowedOwners
const filteredPages = pages.filter(page => {
    // Ensure dm_owner exists and is a non-empty string
    if (!page.dm_owner || typeof page.dm_owner !== "string") {
        return true; // Exclude pages without dm_owner or with dm_owner not as a string
    }

    // Split the dm_owner string into an array, trimming whitespace
    const owners = page.dm_owner.split(",").map(owner => owner.trim().toLowerCase());

    // Check if any owner is not in the allowedOwners list
    return owners.some(owner => !allowedOwners.includes(owner));
});

// Create the table with File, Backlinks, and Owner columns
dv.table(
    ["File", "Backlinks", "Owner"],
    filteredPages.map(page => [
        page.file.link,                // Clickable link to the file
        page.file.inlinks.length,      // Number of backlinks
        page.dm_owner                   // Owner(s) as the original string
    ])
);
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

Pages that link to a background page and are currently unnamed. 
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

These are staging pages linked to pages in the Background directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC
```

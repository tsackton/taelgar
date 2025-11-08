---
headerVersion: 2023.11.25
tags: [meta]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
# Creatures

This directory contains **in-world**, **character-facing**, **player-facing**, and **meta** pages about the species of Taelgar. Player-facing pages should be kept in the Species\Mechanics folder, as should any "rules-heavy" meta pages.

Important Meta and Background Pages:
- [[Metaphysics of Creatures]] (dm background; overarching metaphysics)
- [[Creature Rules in Taelgar]] (dm meta; typology for interactions with D&D rules)
- [[Playable Species of Taelgar]] (player meta; playable species)
- [[Creatures of Taelgar]] (player background; character-facing encylopedia)

Subdirectories:
- **Bestiary**: catch-all for notes on creatures that are (a) native to the Material Plane, and (b) not species. This includes things like "common transformations" (undead, lycanthropes), as well as any others notes on ecology or anything else of non-species creatures. May be further subdivided if needed; a *Mechanics* subdirectory could be a better place for statblocks than Worldbuliding. 
- **Extraplanar**: notes on both creatures and species that are native to the Inner or Outer Planes (anything except Fey and Material Plane natives). May be further subdivided into *Species*, *Inner Planes*, *Outer Planes* as needed, for is not for now.
- **Fey**: notes on natives of the Feywild, both species and creatures.
- **Mechanics**: Player-facing meta pages on playable species (in the D&D rules sense). 
- **Species**: Character-facing encyclopedia pages on all species, whether playable or not. 

## Tagging Information

Excludes missing tags, which should be caught by [[Missing Tags]]

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "Type",
  split(Combo, "\\|")[2] AS "SubType",
  length(rows) AS "Count"

FROM "Creatures" 
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

FROM "Creatures" 
GROUP BY (default(dm_owner, "missing") + "|" + default(dm_notes, "missing")) AS Combo
SORT Combo ASC

```

### DM Notes: Cleanup

Pages that have anything except none in dm_notes

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    dm_notes AS Notes
FROM "Creatures"
WHERE dm_notes != "none" or !dm_notes
SORT dm_notes
```


### Nonstandard DM Owner

Pages that have dm_owner not in: tim, mike, joint, player, none

```dataviewjs
// Define the list of allowed owners
const allowedOwners = ["tim", "mike", "joint", "player", "none"];

// Fetch all pages from the "Background" directory
const pages = dv.pages('"Creatures"');

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
FROM "Creatures"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


### Status: Check

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Creatures"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

### Status: Cleanup

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Creatures"
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
FROM "Creatures"
WHERE excludePublish
FLATTEN excludePublish as exPub
SORT length(file.inlinks) DESC

```

## Unnamed In-Links

Pages that link to a page and are currently unnamed. 
```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM ""
WHERE 
    startswith(file.name, "~") AND
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Creatures")))
SORT length(file.inlinks) DESC

```

## Staging

These are staging pages linked to pages in this directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Creatures")))
SORT length(file.inlinks) DESC
```

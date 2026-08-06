---
tags: [meta]
---
# Tentative Notes

The `Worldbuilding/Tentative` directory contains candidate note subjects whose existence, boundaries, continuity, or value as standalone notes remains unresolved. `tentativeReason` is deliberately freeform and should briefly record why each note is here.

## Unclassified

```dataview
TABLE length(file.inlinks) AS "All backlinks"
FROM "Worldbuilding/Tentative"
WHERE !tentativeReason
SORT file.name ASC
```

## All Tentative Notes

```dataview
TABLE
  tentativeReason AS "Reason",
  length(file.inlinks) AS "All backlinks",
  length(filter(
    file.inlinks,
    (b) =>
      !contains(meta(b).path, "Worldbuilding/")
      AND !contains(meta(b).path, "Campaigns/")
      AND !contains(meta(b).path, "_sessions/")
      AND !contains(meta(b).path, "_DM_/")
      AND !contains(meta(b).path, "_dm_notes/")
  )) AS "Reference backlinks",
  length(filter(
    file.inlinks,
    (b) => contains(meta(b).path, "Campaigns/")
  )) AS "Campaign backlinks",
  choice(contains(file.name, "~"), "yes", "") AS "Temporary name"
FROM "Worldbuilding/Tentative"
SORT tentativeReason, length(file.inlinks) DESC, file.name ASC
```

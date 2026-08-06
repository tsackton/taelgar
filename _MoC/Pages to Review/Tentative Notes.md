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

General rules and notes about Tentative.

The Tentative folder collects notes that are useful for various reasons but (a) might not exist in world (including unused concepts from campaigns), (b) might not make sense to retain as a separate note, or (c) exist as spaces on the map but don't have enough context to decide if they should be one note or several. 

Category (a) is fairly obvious, but includes two distinct things: brainstorming ideas (typically, "unclear if this exists") or things that were invented for a game but were not used or were used in a non-canon game ("unused concept"). 

Category (b) includes merge candidates (e.g. do we need a Duchy of Brovna and a Marches of Brovna note), and possibly mythical people or places that might be best contained to the source note. 

Category (c) is the trickiest but generally captures blank spaces on the map that are ill defined, mountains on the map without much invention where it is not obvious if one, two, or more notes is best, and river systems either unmapped or without defined hydronomy. This is often a catch all for "it is hard to make up a name for this because not sufficient information has been invented". 

Referencing notes in Tentative:

Generally, nothing in category (a) should be linked from a published reference note, except in comments/discussion. Things from category (c) are often referenced in region notes, which is okay but should be checked. 

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
  filter(
    file.inlinks,
    (b) =>
      !contains(meta(b).path, "Worldbuilding/")
      AND !contains(meta(b).path, "Campaigns/")
      AND !contains(meta(b).path, "_sessions/")
      AND !contains(meta(b).path, "_DM_/")
      AND !contains(meta(b).path, "_dm_notes/")
      AND !contains(b.excludePublish, "all")
  ) AS "Published reference links",
  length(filter(
    file.inlinks,
    (b) => contains(meta(b).path, "Campaigns/")
  )) AS "Campaign backlinks",
  choice(contains(file.name, "~"), "yes", "") AS "Temporary name"
FROM "Worldbuilding/Tentative"
SORT tentativeReason, length(file.inlinks) DESC, file.name ASC
```

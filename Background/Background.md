---
headerVersion: 2023.11.25
lintedAt: "2026-11-12T19:02:10-05:00"
lintVersion: "3.5"
tags: [meta, status/check/lint]
noPublish: true
name: Background
dm_owner: none
dm_notes: none
POV: undated
---
# Background

This directory generally should contain **meta** pages almost exclusively. Not intended to be published, but rather intended to be a place to store canonical information that informs worldbuilding but is not directly player-facing.

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

lastChecked:: 2020-12-01
### Modified Files with No Status Tags

All files modified after last checked date, that lack status tags. 

```dataview
list from "Background" and !"Background/Background.md" 
where file.mtime > this.lastChecked and !contains(file.etags, "status")
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

%%^povNotes:v1%%
Temporal coverage: the directory guide describes vault organization and has no in-world reading date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded the page title as its explicit name and its out-of-world viewpoint as undated.
- Corrected “worldbuliding” to “worldbuilding.”

### Validated judgments
- [[Vault Organization]] confirms the stated purpose of the Background directory.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** “Nonstandard DM Owner” lists only five valid owners and will flag four values accepted by [[Note Status]]. Update its description to “Pages with a missing or unrecognized DM owner” and its filter to `where !contains(["tim", "mike", "joint", "player", "none", "schwartz", "kong", "eric", "isaac"], dm_owner)`.
- [ ] **Warning — correctness.internal_conflict:** The “Publishable Pages” queries ignore `noPublish`. The first table therefore includes this guide, which sets `noPublish: true` and explicitly disclaims publication. Add `!noPublish AND` before the existing condition in each of the two publication queries so a page marked as unpublished appears in neither list.
%%^End%%

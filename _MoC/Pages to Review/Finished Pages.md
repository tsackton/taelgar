# Pages without Status Tags

Pages without status/stub, status/check, status/needswork, or status/update, and with dm_info = none, are complete (although might need metadata updates or rewrites).

## Not People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
FROM !"Campaigns" AND !"Worldbuilding" AND !"People" AND !#status/stub AND !#status/check AND !#status/needswork AND !#status/update AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets" 
WHERE dm_notes = "none"
SORT file.path
```

## People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
FROM "People" AND !#status/stub AND !#status/check AND !#status/needswork AND !#status/update
WHERE dm_notes = "none"
SORT file.path
```

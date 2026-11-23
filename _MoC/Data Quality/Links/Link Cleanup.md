# Linked Pages

This tracks pages that are in directories that imply tentative/non-public but are linked outside those directories. Generally speaking these notes should either be moved to a more appropriate place (e.g., Worldbuilding/Staging if just a marker), or should be de-linked.

### World Building - Brainstorming

```dataview
TABLE WITHOUT ID file.link AS "File", external AS "External Backlinks"
FROM "Worldbuilding/Brainstorming"
FLATTEN list(filter(file.inlinks, (source) =>
  !startswith(meta(source).path, "Worldbuilding/") AND
  !startswith(meta(source).path, "_DM_/")
)) AS external
WHERE length(external) > 0
```


### World Building - Tentative

```dataview
TABLE WITHOUT ID file.link AS "File", external AS "External Backlinks"
FROM "Worldbuilding/Tentative"
FLATTEN list(filter(file.inlinks, (source) =>
  !startswith(meta(source).path, "Worldbuilding/") AND
  !startswith(meta(source).path, "_DM_/") AND
  !startswith(meta(source).path, "_dm_notes/")
)) AS external
WHERE length(external) > 0
```

##  DM Notes

```dataview
TABLE WITHOUT ID file.link AS "File", external AS "External Backlinks"
FROM "_DM_"
FLATTEN list(filter(file.inlinks, (source) =>
  !startswith(meta(source).path, "_DM_/")
)) AS external
WHERE length(external) > 0
```

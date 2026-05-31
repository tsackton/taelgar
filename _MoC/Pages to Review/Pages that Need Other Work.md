## Work In Progress

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/wip AND !"_templates"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Review


```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/review
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Text Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup/text and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Image Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup/image and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Map Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup/map and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Metadata Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup/metadata and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Tagged Whereabouts Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup/whereabouts and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```
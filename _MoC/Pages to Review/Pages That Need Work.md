# Pages That Need Work


## Needswork

These are incorrect pages that might have dubiously canonical information, that need revisiting.

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/needswork 
FLATTEN length(file.inlinks) AS BacklinkCount
SORT BacklinkCount DESC
```


## Incomplete

These are pages missing key information; see comment for what is missing.


```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/incomplete  
FLATTEN length(file.inlinks) AS BacklinkCount
SORT BacklinkCount DESC
```

## WIP

In process reformating or other in-progress updates.

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/wip  AND!"_MoC"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/") ASC, BacklinkCount DESC
```
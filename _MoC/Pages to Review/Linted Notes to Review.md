## Linted, Other Status

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status and !#status/check/tim and !#status/check/lint and !#status/check/mike
WHERE lintedAt
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Linted, Check Tim

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/tim  and !#status/check/lint
WHERE lintedAt
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```



## Linted, Check Mike

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/mike  and !#status/check/lint
WHERE lintedAt
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```


## Linted Clean

Set `lintedCleanAfter` to the ISO 8601 date and time after which cleanly linted notes should appear. The default preserves all existing results.

lintedCleanAfter:: 2026-08-19T22:19:45-04:00

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM !#status
WHERE lintedAt AND date(lintedAt) > date(this.lintedCleanAfter)
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

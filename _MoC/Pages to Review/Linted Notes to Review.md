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

## Linted, DM notes or DM info remains

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, dm_notes as "DM Notes", dm_owner as "DM Owner"
FROM !#status/check/lint
WHERE lintVersion = "3.0" and (dm_notes != "none" or dm_owner != "none") and (dm_notes)
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

lintedCleanAfter:: 2026-08-20T18:06:45-04:00

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, lintVersion
FROM !#status/check/lint
WHERE lintedAt AND date(lintedAt) > date(this.lintedCleanAfter)
SORT join(split(file.path, "/", 2), "/")
```

## All Current Version Linted

currentLintVersion:: "3.1"

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, lintVersion, date(lintedAt)
WHERE lintVersion and lintVersion = this.currentLintVersion
SORT date(lintedAt)
```

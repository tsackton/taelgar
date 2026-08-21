
### Need Lint Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/lint
WHERE lintVersion = "3.2"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```


## Linted Clean

Set `lintedCleanAfter` to the ISO 8601 date and time after which cleanly linted notes should appear. The default preserves all existing results.

lintedCleanAfter:: 2026-08-20T18:06:45-04:00

```dataview
TABLE
    join(split(file.path, "/", 2), "/") as Folder,
    lintVersion,
    choice(
	    typeof(POV) = "duration",
	    durationformat(choice(typeof(POV) = "duration", POV, null), "s's'"),
	    string(POV)
	) as POV
FROM !#status/check/lint
WHERE lintedAt AND date(lintedAt) > date(this.lintedCleanAfter)
SORT POV
```

## All Linted


```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder,
    lintVersion,  date(lintedAt) as "Linted At",
    choice(
	    typeof(POV) = "duration",
	    durationformat(choice(typeof(POV) = "duration", POV, null), "s's'"),
	    string(POV)
	) as POV,
    choice(
        contains(file.etags, "#status/check/lint"),
        "No",
        "Yes"
    ) as "Clean?"
WHERE lintedAt
SORT date(lintedAt)
```



## Linted Clean, DM Owner or DM Notes Remain

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, dm_notes as "DM Notes", dm_owner as "DM Owner"
FROM !#status/check/lint
WHERE lintVersion and (dm_notes != "none" or dm_owner != "none") and (dm_notes)
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

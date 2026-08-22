currentLinterVersion:: "3.4"
lintedCleanAfter:: 2026-08-21T18:00:45-04:00
lintedAfter:: 2026-08-21T18:00:45-04:00

### Need Lint Cleanup

Has the lint status tag and the current linter version. 

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/lint and !#status/check/mike
WHERE lintVersion = this.currentLinterVersion
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/")
```

### Need Lint Cleanup - Mike

Has the lint status tag and the current linter version. 

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/lint and #status/check/mike
WHERE lintVersion = this.currentLinterVersion
FLATTEN length(file.inlinks) AS BacklinkCount
SORT BacklinkCount DESC
```

## Recent Runs

All linted notes after the lintedAfter time above. 

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
WHERE lintedAt AND date(lintedAt) > date(this.lintedAfter)
SORT POV
```

## Linted Clean

All linted notes with no status tag, current version, and linted after the lintedCleanAfter date. 


```dataview
TABLE
    join(split(file.path, "/", 2), "/") as Folder,
    lintVersion,
    choice(
	    typeof(POV) = "duration",
	    durationformat(choice(typeof(POV) = "duration", POV, null), "s's'"),
	    string(POV)
	) as POV, pronunciation
FROM !#status/check/lint
WHERE lintedAt AND date(lintedAt) > date(this.lintedCleanAfter) AND lintVersion = this.currentLinterVersion
SORT POV, pronunciation
```


## Linted Clean, DM Owner or DM Notes Remain

All linted notes with no status tag, current version, linted after the lintedCleanAfter date, and not none for either dm owner or dm notes. 

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, dm_notes as "DM Notes", dm_owner as "DM Owner"
FROM !#status/check/lint
WHERE (dm_notes != "none" or dm_owner != "none") and (dm_notes) and lintVersion = this.currentLinterVersion and date(lintedAt) > date(this.lintedCleanAfter)
FLATTEN length(file.inlinks) AS BacklinkCount
SORT dm_owner, dm_notes, join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Linted Clean, DM Owner None

All linted notes with no status tag, current version, linted after the lintedCleanAfter date, and none for dm owner.

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, dm_notes as "DM Notes", dm_owner as "DM Owner"
FROM !#status/check/lint
WHERE (dm_owner = "none") and (dm_owner) and lintVersion = this.currentLinterVersion and date(lintedAt) > date(this.lintedCleanAfter)
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

## Linted Clean, DM Notes None

All linted notes with no status tag, current version, linted after the lintedCleanAfter date, and none for dm notes.

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, dm_notes as "DM Notes", dm_owner as "DM Owner"
FROM !#status/check/lint
WHERE (dm_notes = "none") and (dm_notes) and lintVersion = this.currentLinterVersion and date(lintedAt) > date(this.lintedCleanAfter)
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

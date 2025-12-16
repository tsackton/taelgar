# Pages That Need Review

These are pages that need checking of some kind. Usually this is just a simple review. Pages that need extensive work should be tagged needswork, cleanup, or something else as appropriate. 

## Review

### Needs AI Cleanup

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/ai and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```

### Check: Mike
```dataview
list from #status/check/mike and !#status/check/tim
```

### Check: Tim
```dataview
list from #status/check/tim and !#status/check/mike
```

### Check: Mike & Tim
```dataview
list from #status/check/tim and #status/check/mike
```

## Errors

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/check/errors and !"Worldbuilding" and !"_DM_"
FLATTEN length(file.inlinks) AS BacklinkCount
SORT BacklinkCount DESC, join(split(file.path, "/", 2), "/")
```
## Names

### Needs Name Confirmation
```dataview
list from #status/check/name and !"Worldbuilding"
where !contains(file.name, "~")
sort file.name
```
### Needs Official Name
```dataview
list from !"Worldbuilding"
where contains(file.name, "~")
sort file.name
```

## Minor Checks

### Needs Facts Checked
```dataview
list from #status/check/minor 
```

### Other Checking Needed (See Note for Details)
```dataview
list from #status/check and !#status/check/tim and !#status/check/name and !#status/check/mike and !#status/check/minor and !#status/check/ai and !#status/check/errors
```


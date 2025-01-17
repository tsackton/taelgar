## Stubs

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status",
  dm_notes as "notes",
  dm_owner as "owner"
FROM #status/stub 
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT directory, dm_owner, dm_notes
```

## No Owner, Important

Excluding stubs

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM !"#status/stub"
WHERE dm_notes = "important" and dm_owner = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT directory, Status
```

## No Owner, Color

Excluding stubs

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM !"#status/stub"
WHERE dm_notes = "color" and dm_owner = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT directory, Status
```

## Shared Notes

### All

All shared notes

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  dm_notes as notes,
  dm_owner as owner,
  Status AS "status"
FROM ""
WHERE contains(dm_owner, "shared") or contains(dm_owner, ",")
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT dm_owner, directory, dm_notes, Status
```
### Mike & Tim

All notes tagged "mike,tim". These are notes that are actively involved in multiple campaigns, but generally are not things we are primarily developing jointly. To the extent possible, should try to keep as much development on the Obsidian page as possible. 

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  dm_notes as notes,
  Status AS "status"
FROM ""
WHERE contains(dm_owner, "mike") and contains(dm_owner, "tim") and !contains(dm_owner, "shared")
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT directory, dm_notes, Status
```
### Shared and Private Notes
```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  dm_notes as notes,
  dm_owner as owner,
  Status AS "status"
FROM ""
WHERE contains(dm_owner, "shared") and (contains(dm_owner, "mike") or contains(dm_owner, "tim"))
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT dm_owner, directory, dm_notes, Status
```

### Only Shared Notes

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  dm_notes as notes,
  Status AS "status"
FROM ""
WHERE contains(dm_owner, "shared") and (!contains(dm_owner, "mike") and !contains(dm_owner, "tim"))
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 1), "/") as "directory"
SORT directory, dm_notes, Status
```

## No Owner or Notes

### Gazetteer
```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Gazetteer"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### People

Groups, People

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "People" OR "Groups"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### History Related

History, Events

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Events" OR "History"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### Meta

Species, Cosmology, Time

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Time" OR "Species" OR "Cosomology"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### Sources

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Primary Sources"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### Things
```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Things"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```

### Worldbuilding

```dataview
TABLE WITHOUT ID
  directory AS "directory",
  file.link AS "page",
  Status AS "status"
FROM "Worldbuilding"
WHERE dm_owner = "none" and dm_notes = "none"
FLATTEN choice(
    length(filter(file.etags, (t) => startswith(t, "#status/stub"))) > 0,
    "stub",
    choice(
      length(filter(file.etags, (t) => startswith(t, "#status/needswork"))) > 0,
      "needs work",
      choice(
        length(filter(file.etags, (t) => startswith(t, "#status/check"))) > 0,
        "check",
        choice(
          length(filter(file.etags, (t) => startswith(t, "#status/active"))) > 0,
          "active",
          "complete"
        )
      )
    )
  ) AS "Status"
FLATTEN join(split(file.path, "/", 2), "/") as "directory"
SORT Status, directory
```
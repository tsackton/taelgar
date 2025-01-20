## Overall

```dataview
TABLE WITHOUT ID
  split(GroupKey, "\\|")[1] AS "dm_owner",
  split(GroupKey, "\\|")[0] AS "dm_notes",
  length(rows) AS "count"
FROM !"_DM_" AND !"_MoC" AND !"_scripts" AND !"_templates" AND !"assets" AND !"Campaigns" AND !"Worldbuilding"
GROUP BY (
  default(dm_notes, "missing")
  + "|" 
  + default(dm_owner, "missing")
) AS GroupKey
SORT split(GroupKey, "\\|")[1], split(GroupKey, "\\|")[0]
```


## By Status Tag

```dataview
TABLE WITHOUT ID
  split(GroupKey, "\\|")[2] AS "status",
  split(GroupKey, "\\|")[1] AS "dm_owner",
  split(GroupKey, "\\|")[0] AS "dm_notes",
  length(rows) AS "count"
FROM !"_DM_" AND !"_MoC" AND !"_scripts" AND !"_templates" AND !"assets" AND !"Campaigns" AND !"Worldbuilding"
GROUP BY (
  default(dm_notes, "missing")
  + "|" 
  + default(dm_owner, "missing")
  + "|" 
  + (
    choice(
      length(filter(file.etags, (tag) => startswith(tag, "#status/stub"))) > 0, 
      "stub",
      choice(
        length(filter(file.etags, (tag) => startswith(tag, "#status/needswork"))) > 0, 
        "needs work",
        choice(
          length(filter(file.etags, (tag) => startswith(tag, "#status/check"))) > 0, 
          "check",
          choice(
            length(filter(file.etags, (tag) => startswith(tag, "#status/active"))) > 0, 
            "active",
            "complete"
          )
        )
      )
    )
  )
) AS GroupKey
SORT split(GroupKey, "\\|")[2] ASC, split(GroupKey, "\\|")[1] ASC, split(GroupKey, "\\|")[0] ASC

```


## By Directory

```dataview
TABLE WITHOUT ID
  split(GroupKey, "\\|")[0] AS "directory",
  split(GroupKey, "\\|")[2] AS "dm_owner",
  split(GroupKey, "\\|")[1] AS "dm_notes",
  length(rows) AS "count"
FROM !"_DM_" AND !"_MoC" AND !"_scripts" AND !"_templates" AND !"assets" and !"Worldbuilding"
GROUP BY (
  join(split(file.path, "/", 1), "/")
  + "|" 
  + default(dm_notes, "missing")
  + "|" 
  + default(dm_owner, "missing")
) AS GroupKey
SORT split(GroupKey, "\\|")[0] ASC, split(GroupKey, "\\|")[2], split(GroupKey, "\\|")[1]

```

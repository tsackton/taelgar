# TypeOf Details


Counts of TypeOf details for various descriptive tags

## People

People don't use typeOf, instead use species and ancestry.

See [[Person Details]]

## Groups

Includes organization, culture

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#organization",
    "#culture"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#organization",
    "#culture"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Missing, With Status, Excluding Stubs

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  Status AS "Status"
FROM (#organization OR #culture) AND !#status/stub
WHERE !typeof
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#organization",
    "#culture"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```

## Places

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#place"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#place"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Missing, With Status, Excluding Stubs

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  Status AS "Status"
FROM #place AND !"Worldbuilding/Brainstorming" AND !"Worldbuilding/Tentative"
WHERE !typeof and !"#status/stub"
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#place"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```

## Items

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#item"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#item"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Missing, With Status, Excluding Stubs

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  Status AS "Status"
FROM #item AND !#status/stub
WHERE !typeof
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#item"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```


## Time

Includes events, holidays, timeline

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#event",
    "#timeline",
    "#holiday"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#event",
    "#timeline",
    "#holiday"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Missing, With Status, Excluding Stubs

Event only for now
```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  Status AS "Status"
FROM #event AND !#status/stub
WHERE !typeof
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#event"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```


## Meta

Includes deity, species, background, meta.

These generally don't have typeOf.

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#deity",
    "#species",
    "#background",
    "#meta"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#deity",
    "#species",
    "#background",
    "#meta"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Has TypeOf, With Status

Since these generally don't have typeOf, worth looking at those that do.

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  typeof as "TypeOf",
  Status AS "Status"
FROM #background OR #deity OR #species OR #meta
WHERE typeof
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#background",
    "#deity",
    "#species",
    "#meta"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```


## Primary Sources

session notes and sources.

These generally don't have typeOf.

### Counts
```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#source",
    "#session-note"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#source",
    "#session-note"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```

### Has TypeOf, With Status

Since these generally don't have typeOf, worth looking at those that do.

```dataview
TABLE WITHOUT ID
  file.link AS "Page",
  Descriptive AS "Descriptive Tag",
  typeof as "TypeOf",
  Status AS "Status"
FROM #source OR #session-note 
WHERE typeof
FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#source",
    "#session-note"
  ], tag)
) AS Descriptive
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
SORT Status ASC, Descriptive ASC
```



## All 

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Descriptive Tag",
  split(Combo, "\\|")[1] AS "TypeOf Value",
  length(rows) AS "Count"

FROM "" 
WHERE any(
  file.tags,
  (tag) => contains([
    "#person",
    "#place",
    "#organization",
    "#item",
    "#deity",
    "#species",
    "#background",
    "#event",
    "#session-note",
    "#timeline",
    "#holiday",
    "#meta",
    "#source",
    "#culture"
  ], tag)
)

FLATTEN filter(
  file.tags,
  (tag) => contains([
    "#person",
    "#place",
    "#organization",
    "#item",
    "#deity",
    "#species",
    "#background",
    "#event",
    "#session-note",
    "#timeline",
    "#holiday",
    "#meta",
    "#source",
    "#culture"
  ], tag)
) AS Descriptive

GROUP BY (Descriptive + "|" + default(typeof, "missing")) AS Combo

SORT Combo ASC

```
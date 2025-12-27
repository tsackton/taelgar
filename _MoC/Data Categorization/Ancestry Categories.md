## Ancestry TypeOfs

```dataview
TABLE WITHOUT ID
  typeOf as "Type",
  length(rows) as "Count"
FROM #ancestry  and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOf
SORT length(rows) DESC
```
### Has TypeOf
```dataview
LIST
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and typeOf
```

## Ancestry PartOfs
```dataview
TABLE WITHOUT ID
  partOf as "Part Of",
  length(rows) as "Count"
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY partOf
SORT length(rows) DESC
```

### Has PartOf
```dataview
LIST
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and partOf
```

## Ancestry SubTypes
```dataview
TABLE WITHOUT ID
  subTypeOf as "Subtype",
  length(rows) as "Count"
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY subTypeOf
SORT length(rows) DESC
```

### Has SubTypeOf
```dataview
LIST
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and subTypeOf
```

## Ancestry Ancestries

```dataview
TABLE WITHOUT ID
  ancestry as "Ancestry",
  length(rows) as "Count"
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY ancestry
SORT length(rows) DESC
```

### Has Ancestry
```dataview
LIST
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and ancestry
```


## Ancestry TypeOf Alias

```dataview
TABLE WITHOUT ID
  typeOfAlias as "Alias",
  length(rows) as "Count"
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOfAlias
SORT length(rows) DESC
```

### Has TypeOf Alias
```dataview
LIST
FROM #ancestry and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and typeofAlias
```


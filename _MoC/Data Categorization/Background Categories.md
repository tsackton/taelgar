## Background TypeOfs

```dataview
TABLE WITHOUT ID
  typeOf as "Type",
  length(rows) as "Count"
FROM #background and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOf
SORT length(rows) DESC
```

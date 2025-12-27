## Creature TypeOfs

```dataview
TABLE WITHOUT ID
  typeOf as "Creature Type",
  length(rows) as "Count"
FROM #creature and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOf
SORT length(rows) DESC
```

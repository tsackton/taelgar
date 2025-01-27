# Linked Worldbuilding Pages

These are worldbuliding notes that ARE linked

```dataview
TABLE length(file.inlinks) as Backlinks
FROM "Worldbuilding" and !"Worldbuilding/Staging"
WHERE length(file.inlinks)>0 SORT length(file.inlinks) desc
```

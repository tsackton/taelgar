```dataview
TABLE length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
sort length(file.inlinks) desc
```

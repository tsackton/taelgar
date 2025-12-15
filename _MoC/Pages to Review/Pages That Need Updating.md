# Pages That Need Updating


All pages tagged with gameupdate tags, indicating they need to be updated to reflect game events. 

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/gameupdate and !#status/gameupdate/clee and !#status/gameupdate/dufr and !#status/gameupdate/chasm and !#status/gameupdate/gl and !#status/gameupdate/adma    
FLATTEN length(file.inlinks) AS BacklinkCount
SORT join(split(file.path, "/", 2), "/"), BacklinkCount DESC
```


# Pages without Status Tags
This should be pages considered "finished".

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder 
FROM !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates"
SORT join(split(file.path, "/", 2),"/")
```


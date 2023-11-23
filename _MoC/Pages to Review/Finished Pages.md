# Pages without Status Tags
This should be pages considered "finished".

```dataview
TABLE split(file.path,"/",1)[0] as Folder from !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates"
SORT split(file.path,"/",1)[0] 
```


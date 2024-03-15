# Pages without Status Tags
This should be pages considered "finished".

## Outside Worldbuilding and Campaigns

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, headerVersion
FROM !"Campaigns" AND !"Worldbuilding" AND !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets"
SORT file.path
```

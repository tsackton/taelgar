# Pages without Status Tags
This should be pages considered "finished".

# Outside Worldbuilding and Campaigns, Not People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, headerVersion
FROM !"Campaigns" AND !"Worldbuilding" AND !"People" AND !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets"
SORT file.path
```


# People
(these still need to be double-checked)
confirmed completed: Chardonians, Deno'qai, Dunmari, Dwarves, Elves, PCs

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, headerVersion
FROM !"Campaigns" AND !"Worldbuilding" AND "People" AND !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets"
SORT file.path
```

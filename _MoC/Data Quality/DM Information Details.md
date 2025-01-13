
```dataview
TABLE dm_owner as DM, dm_notes as Notes, join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets" AND !"Worldbuilding"
where ((dm_notes != "none" AND dm_owner !="none") OR (dm_notes = "none" AND dm_owner !="none") OR (dm_owner = "none" AND dm_notes != "none")) AND dm_notes AND dm_owner
sort dm_notes, dm_owner
```


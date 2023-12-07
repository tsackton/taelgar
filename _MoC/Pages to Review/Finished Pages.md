# Pages without Status Tags
This should be pages considered "finished".

## Outside Worldbuilding and Campaigns

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, headerVersion
FROM !"Campaigns" AND !"Worldbuilding" AND !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates"
SORT join(split(file.path, "/", 2),"/")
```

## Worldbuilding

```dataview
TABLE split(file.path, "/", 2)[1] as Folder 
FROM "Worldbuilding" AND !#status
SORT join(split(file.path, "/", 2),"/")
```

## Campaigns

```dataview
TABLE split(file.path, "/", 3)[1] as Campaign, split(file.path, "/", 3)[2] as Folder
FROM "Campaigns" AND !#status
SORT join(split(file.path, "/", 3),"/")
```
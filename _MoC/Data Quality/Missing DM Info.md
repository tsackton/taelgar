# All Excluding Worldbuilding

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets" AND!"Worldbuilding"
where !dm_owner or !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

## People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "People" 
where !dm_owner or !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

## Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Gazetteer"
where !dm_owner or !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Worldbuilding

DM frontmatter for worldbuilding pages is not critical, but can be helpful so worth setting where possible. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM "Worldbuilding" AND !"Worldbuilding/High School Notes"
where !dm_owner or !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```
# No Status, Need DM Info

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !#status AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets" AND !"Worldbuilding"
where ((dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_owner != "mike" and dm_owner != "shared" and dm_owner != "tim" and dm_owner != "none" and dm_owner != "open")) 
sort length(file.inlinks) desc, join(split(file.path, "/", 2),"/")
```

# People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "People" 
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_owner != "mike" and dm_owner != "shared" and dm_owner != "tim" and dm_owner != "none" and dm_owner != "open")
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Gazetteer"
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_owner != "mike" and dm_owner != "shared" and dm_owner != "tim" and dm_owner != "none" and dm_owner != "open")
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Groups

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Groups"
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_owner != "mike" and dm_owner != "shared" and dm_owner != "tim" and dm_owner != "none" and dm_owner != "open")
sort file.path, Backlinks
```

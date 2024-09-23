# People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "People" 
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_plans != "no" and dm_plans != "yes")
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Gazetteer"
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_plans != "no" and dm_plans != "yes")
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Groups

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Groups"
where (dm_notes != "none" and dm_notes != "important" and dm_notes != "color") or (dm_plans != "no" and dm_plans != "yes")
sort file.path, Backlinks
```

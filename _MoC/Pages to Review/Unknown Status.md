# People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "People" AND #status/unknown 
sort file.path, Backlinks
```

# Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Gazetteer" AND #status/unknown 
sort length(file.inlinks) desc, file.path
```

# Other

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"Gazetteer" AND !"People" AND !"Campaigns" AND #status/unknown 
sort file.path, Backlinks
```



# Campaigns
(these should mostly just be deleted)

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Campaigns" AND #status/unknown 
sort file.path
```

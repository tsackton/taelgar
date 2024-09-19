# People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "People" AND #status/needswork/blankslate 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from "Gazetteer" AND #status/needswork/blankslate 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Other (except Campaigns)

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from !"Gazetteer" AND !"People" AND !"Campaigns" AND #status/needswork/blankslate 
sort file.path, Backlinks
```

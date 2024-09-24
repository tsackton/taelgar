# Needs Text  - People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks, filter(file.etags, (x) => startswith(x, "#status") & !endswith(x, "unknown")) as Status
from "People" AND #status/needswork 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

# Needs Text  - Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks, filter(file.etags, (x) => startswith(x, "#status") & !endswith(x, "unknown")) as Status
from "Gazetteer" AND #status/needswork 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

# Needs Text  - Other

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks, filter(file.etags, (x) => startswith(x, "#status") & !endswith(x, "unknown")) as Status
from !"People" AND !"Gazetteer" AND #status/needswork 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

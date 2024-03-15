# Needs Images

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, filter(file.etags, (x) => startswith(x, "#status")) as Status
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/image 
```

# Needs Text 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, filter(file.etags, (x) => startswith(x, "#status") & !endswith(x, "unknown")) as Status
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/needswork 
sort join(split(file.path, "/", 2),"/"), Status, file.path
```

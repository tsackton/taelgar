# Needs Images

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, filter(file.etags, (x) => startswith(x, "#status")) as Status
from !#status/unknown AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/images 
```

# Needs Text

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, filter(file.etags, (x) => startswith(x, "#status")) as Status
from !#status/unknown AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/needswork 
sort filter(file.etags, (x) => startswith(x, "#status/needswork")), join(split(file.path, "/", 2),"/")
```

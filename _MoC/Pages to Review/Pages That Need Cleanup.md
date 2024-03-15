# Needs Header Information Cleanup

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/cleanup/header
sort file.path
```

# Stubs

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/stub  
sort file.path
```


# Needs Reformatting

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/cleanup/reformat
sort file.path
```

# Needs Refactoring

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/cleanup/refactor 
sort file.path
```

# Other Cleanup

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/cleanup AND !#status/cleanup/header AND !#status/cleanup/refactor AND !#status/cleanup/reformat
sort file.path
```

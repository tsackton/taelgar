# Needs Header Information Cleanup

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/metadata/header
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
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/cleanup
sort file.path
```

# Needs Refactoring

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/metadata/refactor 
sort file.path
```


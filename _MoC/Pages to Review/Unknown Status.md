
```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder
from !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status/unknown 
sort file.path
```

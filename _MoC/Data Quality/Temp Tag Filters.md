
```dataview
TABLE split(file.path,"/",1)[0] as Folder
from #item
where (
!contains(tags, "equipment") and 
!contains(tags, "other") and
!contains(tags, "vehicle")
)
```

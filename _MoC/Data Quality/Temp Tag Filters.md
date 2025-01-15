
```dataview
TABLE split(file.path,"/",1)[0] as Folder
from #religion 
where (
!contains(tags, "fivesiblings") and 
!contains(tags, "dwarven") and
!contains(tags, "halflings") and
!contains(tags, "kestavo") and
!contains(tags, "mosnumena") and
!contains(tags, "skaer") and
!contains(tags, "tanshi") 
)
```

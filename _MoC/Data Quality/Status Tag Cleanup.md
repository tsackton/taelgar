```dataview
TABLE split(file.path,"/",1)[0] as Folder, length(file.inlinks) as Backlinks
from #status/check 
where (
!contains(tags, "mike") and 
!contains(tags, "tim") and 
!contains(tags, "minor") and 
!contains(tags, "name") and 
!contains(tags, "whereabouts") 
)
SORT split(file.path,"/",1)[0], length(file.inlinks) DESC
```

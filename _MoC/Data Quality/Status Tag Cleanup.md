```dataview
TABLE split(file.path,"/",1)[0] as Folder, length(file.inlinks) as Backlinks
from #status/cleanup 
where (
!contains(tags, "map") and 
!contains(tags, "chronology") and 
!contains(tags, "external") and 
!contains(tags, "metadata") and 
!contains(tags, "image") and  
!contains(tags, "internal") and 
!contains(tags, "map") and 
!contains(tags, "refactor") and
!contains(tags, "text") and
!contains(tags, "whereabouts") 
)
SORT split(file.path,"/",1)[0], length(file.inlinks) DESC
```

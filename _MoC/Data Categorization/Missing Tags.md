# Pages outside DM/Campaign/MOC with no "well-defined tag"

See [[Note Categorization]] for the list of well-known tags. When changing that list, please update the data-query here.

```dataview
TABLE split(file.path,"/",1)[0] as Folder, length(file.inlinks) as Backlinks
from !"_DM_" and !"Campaigns" and !"_dm_notes" and !"_MoC" and !"assets" and !"_templates" and !"Worldbuilding" and !"_sessions" and !"AGENTS.md"
where (
!contains(tags, "object") and 
!contains(tags, "background") and 
!contains(tags, "person") and 
!contains(tags, "power") and 
!contains(tags, "place") and  
!contains(tags, "creature") and 
!contains(tags, "meta") and 
!contains(tags, "organization") and 
!contains(tags, "session-note") and
!contains(tags, "event") and 
!contains(tags, "source") and 
!contains(tags, "culture")
)
SORT split(file.path,"/",1)[0], length(file.inlinks) DESC
```


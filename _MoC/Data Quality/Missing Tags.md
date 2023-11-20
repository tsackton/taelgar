# Pages outside DM/Campaign/MOC with no "well-defined tag"

```dataview
TABLE split(file.path,"/",1)[0] as Folder, length(file.inlinks) as Backlinks
from !"_DM_" and !"Campaigns" and !"_MoC" and !"assets" and !"_templates" and !"Worldbuilding"
where (!contains(tags, "item") and !contains(tags, "person") and !contains(tags, "place") and !contains(tags, "event-source") and !contains(tags, "organization") and !contains(tags, "session-note") and !contains(tags, "event") and !contains(tags, "timeline"))
SORT split(file.path,"/",1)[0], length(file.inlinks) DESC
```

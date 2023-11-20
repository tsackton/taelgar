# Pages outside DM/Campaign/MOC with no "well-defined tag"

Note the following tags are considered well defined: item, background, person, deity, religion, place, species, meta, organization, session-note, event, timeline, holiday

```dataview
TABLE split(file.path,"/",1)[0] as Folder, length(file.inlinks) as Backlinks
from !"_DM_" and !"Campaigns" and !"_MoC" and !"assets" and !"_templates" and !"Worldbuilding" and  !"Primary Sources"
where (!contains(tags, "item") and !contains(tags, "background") and !contains(tags, "person") and !contains(tags, "deity") and !contains(tags, "religion") and !contains(tags, "place") and  !contains(tags, "species") and !contains(tags, "meta") and !contains(tags, "organization") and !contains(tags, "session-note") and !contains(tags, "event") and !contains(tags, "timeline") and !contains(tags, "holiday"))
SORT split(file.path,"/",1)[0], length(file.inlinks) DESC
```

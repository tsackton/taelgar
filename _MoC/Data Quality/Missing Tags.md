# Pages outside DM/Campaign/MOC with no "well-defined tag"

```dataview
list from !"_DM_" and !"Campaigns" and !"_MoC" and !"assets" where (!contains(tags, "item") and !contains(tags, "person") and !contains(tags, "place") and !contains(tags, "event-source") and !contains(tags, "organization") and !contains(tags, "session-note") and !contains(tags, "event") and !contains(tags, "timeline"))
```

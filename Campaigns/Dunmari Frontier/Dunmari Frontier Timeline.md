---
tags: [timeline, status/unknown]
campaignInfo:
name: Dunmari Frontier Timeline
timelineDescriptor: Dunmari Frontier Campaign
---

# Timeline of the Dunmari Frontier Campaign

##  Nayan 190 (DR 1747-1748)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and ((events.DR.year = 1747 and events.DR.month >1) or (events.DR.year = 1747 and events.DR.month = 1 and events.DR.day >= 23) or (events.DR.year = 1748 and events.DR.month = 1 and events.DR.day < 23)) sort events.DR
```
## Nayan 191 (DR 1748-1749)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and ((events.DR.year = 1748 and events.DR.month >1) or (events.DR.year = 1748 and events.DR.month = 1 and events.DR.day >= 23) or (events.DR.year = 1749 and events.DR.month = 1 and events.DR.day < 23)) sort events.DR
```

## Nayan 192 (DR 1749-1750)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and ((events.DR.year = 1749 and events.DR.month >1) or (events.DR.year = 1749 and events.DR.month = 1 and events.DR.day >= 23) or (events.DR.year = 1750 and events.DR.month = 1 and events.DR.day < 23)) sort events.DR
```

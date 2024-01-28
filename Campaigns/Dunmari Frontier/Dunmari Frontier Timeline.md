---
tags: [timeline, status/unknown]
campaignInfo:
name: Dunmari Frontier Timeline
timelineDescriptor: Dunmari Frontier Campaign
---

# Timeline of the Dunmari Frontier Campaign

## 190 Nayan (DR 1747)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and events.DR.year = 1747 sort events.DR
```
## 191 Nayan (DR 1748-1749)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and (events.DR.year = 1748 or (events.DR.year = 1749 and events.DR.month = 1 and events.DR.day < 23)) sort events.DR
```

## 192 Nayan (DR 1749-1750)
```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Dunmari Frontier/Session Notes" OR "People/PCs/Dunmar Fellowship" OR "Events/1700s/War of the Cloak" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR and (events.DR.year = 1749 and (events.DR.month >1 or (events.DR.month = 1 and events.DR.day >= 23))) sort events.DR
```

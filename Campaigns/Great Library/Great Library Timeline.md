---
headerVersion: 2023.11.25
tags: [timeline]
name: Great Library Campaign Timeline
---
# Great Library Campaign Timeline

```dataview
LIST WITHOUT ID events.text FROM "Campaigns/Great Library" OR "People/PCs/Silver Tempests" OR "Events/1700s/Grumella's War" flatten file.lists as events where !contains(events.recharge, "mirror") and events.DR sort events.DR
```

---
headerVersion: 2023.11.25
tags: [timeline]
name: Great Library Campaign Timeline
---
# Great Library Campaign Timeline

```dataview
LIST WITHOUT ID events.text
FROM  "Campaigns/Great Library Campaign"
   OR "People/PCs/Silver Tempests"
   OR "Events/1700s/Grumella's War"

FLATTEN file.lists AS events
FLATTEN
  choice(
        typeof(events.DR) = "date",               
        events.DR,
        date(                                      
             string(events.DR) +
             choice(length(string(events.DR)) = 4, "-01-01",
                   choice(length(string(events.DR)) = 7, "-01", ""))
        )
  ) AS fullDate

WHERE !contains(events.recharge, "mirror") AND events.DR
SORT fullDate

```


# Recently Created Files (most recent 100 in last 14 days)

```dataview 
TABLE dateformat(file.ctime, "MM.dd.yyyy - HH:mm") AS "Created" FROM !"_MoC" and !"_DM_" WHERE file.ctime > (date(now) - dur(14 days)) SORT file.ctime DESC LIMIT 100
```

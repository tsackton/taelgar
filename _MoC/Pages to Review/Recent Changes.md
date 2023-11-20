# Recently Modified (last 14 days, most recent 100)

```dataview 
TABLE dateformat(file.mtime, "MM.dd.yyyy - HH:mm") AS "Last modified" FROM !"_MoC" and !"_DM_" WHERE file.mtime > (date(now) - dur(14 days)) SORT file.mtime DESC LIMIT 100
```

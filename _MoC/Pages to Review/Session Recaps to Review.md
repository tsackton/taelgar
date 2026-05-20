```dataview
TABLE join(split(file.path, "/", 2), "/") as Campaign
FROM #status/recap-review
SORT join(split(file.path, "/", 2), "/")
```

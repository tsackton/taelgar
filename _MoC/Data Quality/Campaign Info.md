This is a big messy, ideally want to pull people linked in session notes but who don't have campaignInfo. Serves as a useful check for now. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM "People"
where !campaignInfo
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

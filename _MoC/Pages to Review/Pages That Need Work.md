# Pages That Need Work

These are incorrect pages that might have dubiously canonical information, that need revisiting.

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks, 
      replace(filter(file.etags, (x) => startswith(x, "#status/needswork"))[0], "#status/needswork/", "") as Status
FROM #status/needswork 
FLATTEN length(file.inlinks) AS BacklinkCount FLATTEN replace(default(filter(file.etags, (x) => startswith(x, "#status/needswork"))[0], ""), "#status/needswork/", "") AS StatusValue 
SORT StatusValue ASC, BacklinkCount DESC
```

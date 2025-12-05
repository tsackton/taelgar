# Pages That Need Cleanup

These are pages that need some kind of cleanup, either metadata, text, image, or maps. 

## All Cleanup

(sorted by backlinks)

```dataview
TABLE join(split(file.path, "/", 2), "/") as Folder, 
      length(file.inlinks) as Backlinks
FROM #status/cleanup 
FLATTEN length(file.inlinks) AS BacklinkCount
SORT BacklinkCount DESC
```

## Need Metadata Fixes

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/cleanup/metadata OR #status/cleanup/whereabouts OR #status/cleanup/campaigninfo  
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```
## Need Text Rewrites

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/cleanup/text or #status/cleanup/gameupdate or #status/cleanup/incomplete
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Need Maps 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/cleanup/map
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Need Images 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/cleanup/image
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Other Cleanup


```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/cleanup 
where !contains(tags, "image") and
!contains(tags, "map") and
!contains(tags, "metadata") and
!contains(tags, "text") and
!contains(tags, "whereabouts") and
!contains(tags, "campaigninfo")
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

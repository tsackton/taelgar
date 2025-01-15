# Pages That Need Finishing

These are pages that are not finished, or that need updating.

## Update

Pages that are out of date due to ongoing campaign events. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/update
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```


## Stubs

Pages that have not been finished

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

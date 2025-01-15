# Pages That Need Work

These are incorrect pages that might have dubiously canonical information, that need revisiting. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks, filter(file.etags, (x) => startswith(x, "#status/needswork") & !endswith(x, "unknown")) as Status
from #status/needswork 
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```
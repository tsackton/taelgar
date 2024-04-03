```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/needswork/external  
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```
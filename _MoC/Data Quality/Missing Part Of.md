# Missing Part Of

```dataview
TABLE length(file.inlinks) as Backlinks
from #place where !partOf 
SORT length(file.inlinks) DESC
```
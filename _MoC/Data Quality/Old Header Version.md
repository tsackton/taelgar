# Contains all data files that have a valid type but not current header

```dataview
TABLE length(file.inlinks) as Backlinks
from #person or #item or #place or #organization and -#status/stub 
where headerVersion != "2023.11.25"
sort length(file.inlinks) desc
```

```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["canal", "river", "gulf", "ocean", "sea", "bay", "brook", "lake", "strait", "waterway"], typeOf)
sort typeOf, subTypeOf, ancestry
```

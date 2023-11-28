```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["region", "plane", "ward"], typeOf)
sort typeOf, subTypeOf, ancestry
```

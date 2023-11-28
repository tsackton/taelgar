```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["city", "village", "town", "hamlet"], typeOf) 
sort typeOf, subTypeOf, ancestry
```

```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["road", "street", "pass"], typeOf) 
sort typeOf, subTypeOf, ancestry
```

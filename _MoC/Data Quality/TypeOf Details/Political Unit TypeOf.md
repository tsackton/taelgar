```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["duchy", "barony", "realm", "march"], typeOf) sort typeOf, subTypeOf, ancestry
```

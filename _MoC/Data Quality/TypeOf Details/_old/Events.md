```dataview
table typeOf, subTypeOf, ancestry, partOf, tags from #event or (#event-source and !#place and !#person and !#item) or #holiday where typeOf or subTypeOf or ancestry or partOf
sort typeOf, subTypeOf, ancestry
```

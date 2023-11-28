```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["orphanage", "holy site", "monastery", "tower", "building", "temple", "inn", "manor", "university", "house", "gate", "guildhall", "fort"], typeOf)
sort typeOf, subTypeOf, ancestry
```

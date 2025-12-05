```dataview
table typeOf, subTypeOf, ancestry, tags from #place where contains(["plains", "oasis", "swamp", "canyon", "island", "archipelago", "desert", "forest", "line of hills", "hill", "mountain", "mountain range", "landform"], typeOf) 
sort typeOf, subTypeOf, ancestry
```

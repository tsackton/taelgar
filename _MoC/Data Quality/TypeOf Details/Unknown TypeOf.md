```dataview
table typeOf, subTypeOf, ancestry, tags from #place where (
!contains(["plane", "region", "ward"], typeOf) and
!contains(["road", "street", "pass"], typeOf) and
!contains(["canal", "river", "gulf", "ocean", "sea", "bay", "brook", "lake", "strait"], typeOf) and 
!contains(["duchy", "barony", "realm", "march"], typeOf) and 
!contains(["city", "village", "town", "hamlet", "settlement"], typeOf) and
!contains(["plains", "oasis", "swamp", "canyon", "island", "archipelago", "desert", "forest", "line of hills", "hill", "mountain", "mountain range"], typeOf) and
!contains(["fort", "orphanage", "holy site", "monastery", "tower", "building", "temple", "inn", "manor", "university", "house", "gate", "guildhall"], typeOf)) and typeOf sort typeOf, subTypeOf, ancestry
```


All the things in a place. This gets everything that is a place in the current file

```
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter))
				.map(b => [util.getName(b.file.name), b.typeOf]))
```

All things in a place, that are known to a party. The two bools are: 
* allowTags: if true assumes a person tagged (prefix/x) is known to the party as long as x isn't unaware, unknown, or unsorted
* allowSessionNotes: if true, assumes a person is known to the party if the person appears in backlinks from session notes

Note that session notes depends on configuring the sessionNotePath in the metadata.json for the prefix.

```
```dataviewjs
const { util } = customJS
dv.table(["Person"], 
			dv.pages("#person")
				.where(f => util.inLocation("Sembara", f.file.frontmatter, false) && util.isKnownToParty(f.file.name, f.file.frontmatter, "clee", true, true))
				.map(b => [util.getName(b.file.name)]))
```

All the things in or from a place, with their current location, and whether they are known to the party

```
````dataviewjs
const { util } = customJS
dv.table(["Person", "Current", "Known to Clee"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation("Sembara", f.file.frontmatter, false))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter), util.isKnownToParty(b.file.name, b.file.frontmatter, "clee", true, true)]))
```
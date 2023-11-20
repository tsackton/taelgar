# People who might need typeOf updates

This lists all of the people (a) do not have an uptodate status tag, and (b) have either no species or (c) neither a subspecies nor an ancestry not (d) affiliations
Its meant to catch dwarves without clans, halflings without families, etc 

```dataview
table species, subspecies, ancestry from #person where (!species or (!subspecies and !ancestry)) and !contains(tags, "status/uptodate") and !affiliations sort species, subspecies, ancestry
```
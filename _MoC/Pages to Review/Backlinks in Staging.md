The `Staging` directory in `Worldbuilding` is used as a place to put notes that describe something that canonically exists, but is not ready to be incorporated into the main directory structure for whatever reason. 

Major uses include:
- A place to put canonical places that are not yet named, e.g. (`~Name~` pages)
- A place to put named pages that canonically exist, but do not yet have frontmatter
- A place to put named pages that canonically exist, but might not be worth additional invention (e.g., named scholars made up as a source of in-world information).

Places that are not backlinked from any canonical page should go in `Brainstorming` or `Tentative`, not `Staging`.

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns"))) as "Has Campaign Backlink"
FROM "Worldbuilding/Staging"
SORT any(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns"))) DESC, length(file.inlinks) DESC
```


## Staging Linked to Specific Directory

Currently: Cosmology

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC
```

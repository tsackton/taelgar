# Missing Notes and Owner

## Main Pages

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets" AND!"Worldbuilding" AND!"_dm_notes"
where !dm_owner and !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

## Worldbuilding

DM frontmatter for worldbuilding pages is not critical, but can be helpful so worth setting where possible. 

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
FROM "Worldbuilding/Brainstorming" OR "Worldbuilding/Tentative"
where !dm_owner and !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Missing Notes, Has Owner

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_owner as Owner, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets"
where dm_owner and !dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```

# Missing Owner, Has Notes

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, dm_notes as Notes, length(file.inlinks) as Backlinks
FROM !"Campaigns" AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND !"assets"
where !dm_owner and dm_notes
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) desc
```



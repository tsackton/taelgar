```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, tags as Tags from !#status/unknown AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status sort join(split(file.path, "/", 2),"/")
```

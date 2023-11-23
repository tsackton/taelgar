```dataview
table split(file.path,"/",1)[0] as Folder, tags as Tags from !#status/unknown AND !"_MoC" AND !"_DM_" AND !"_scripts" AND !"_templates" AND #status sort split(file.path,"/",1)[0]
```
## Linted Notes with Status Tags

currentLinterVersion:: "3.4"

```dataview
TABLE
    Status AS "Status Tag",
    join(split(file.path, "/", 1), "/") AS Folder
FROM !#status/check/lint
WHERE lintVersion = this.currentLinterVersion
FLATTEN filter(file.etags, (tag) => startswith(tag, "#status/")) AS Status
SORT Status ASC, file.name ASC
```

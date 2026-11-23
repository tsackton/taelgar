# `taelgar-relationship`

This Obsidian block shows the direct relationships of the person, organization, or place note containing it. The graph follows the active campaign date. Enable **Settings → Taelgarverse → Enable relationship explorer** to render the block.

An empty block renders a diagram. Set `mode: list` for a grouped list with links to related notes and expandable source details where available.

````markdown
```taelgar-relationship
mode: list
```
````

People and organizations show social relationships. Places show containment, routes, and current or last-known locations. The graph goes one step out from the source note, including when that note is transcluded.

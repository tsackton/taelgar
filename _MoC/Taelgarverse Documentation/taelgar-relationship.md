# `taelgar-relationship`

This Obsidian block shows the direct relationships of the person, organization, or place note containing it. The graph follows the active campaign date. Enable **Settings → Taelgarverse → Enable relationship explorer** to render the block.

An empty block renders a diagram. Set `mode: list` for a grouped list with links to related notes and expandable source details where available.

````markdown
```taelgar-relationship
mode: list
```
````

People and organizations show social relationships. Places show containment, routes, and current or last-known locations. The graph goes one step out from the source note, including when that note is transcluded.

## Tables

Taelgarverse 3.3.0 adds `mode: table`. This example shows only people and renames the name column.

````markdown
```taelgar-relationship
mode: table
types: [person]
columns: [name, info, lastKnown, alive]
columnHeadings: {name: Person}
sortBy: [type, name]
```
````

| Option | Behavior |
| --- | --- |
| `types` | A nonempty list of distinct values drawn from `person`, `object`, `group`, and `place`. Defaults to `[person, object]`. Add `group` for organizations or `place` for places connected by the graph. |
| `columns` | Defaults to `[name, info, lastKnown, alive]`. Use the applicable [[taelgar-index#Table columns|index columns]] for the selected types, plus `kind`, `info`, and `alive`. |
| `columnHeadings` | Map displayed column keys to custom labels. |
| `sortBy` | Give an ordered list of column keys, including hidden columns if useful. The default groups rows by `kind` in the order of `types`, then sorts by name. `type` sorts by displayed main type, such as species or `typeOf`. |

Table mode includes one row per directly connected note. For people and objects, explicit prose links can count in either direction. Frontmatter, comments, fenced code, and embeds do not contribute prose links. Dated passages and structured relationships follow the graph’s active date. `alive` shows Yes or No for people and is blank for other types. `lastKnown` can show a place even when `types` excludes place rows.

Use `mode: table` for the former CustomJS relationship tables. Set `types: [person, group, object]` to include the same note types as the old person, organization, and item filter. The native graph selects rows, so the results can differ from the old link filter.

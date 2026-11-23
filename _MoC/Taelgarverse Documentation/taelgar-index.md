# `taelgar-index`

Put a `taelgar-index` block in a note to list subjects connected to it by location or affiliation. Taelgarverse 3.0.0 renders the block in Obsidian and on the website using the reader’s selected date. The note containing the block is the default target.

## Residents of a place

Paste this beneath a Residents heading. It lists people whose home is this place or somewhere inside it.

````markdown
```taelgar-index
type: whereabouts
from: person
via: home
mode: table
heading: false
```
````

For people present on the selected date, use `via: current`. An active secondary location also counts. Use `via: lastKnown` to fall back to the geography on the day of the last sighting. Only the recorded home qualifies for the first step of `via: home`. Set `recursive: false` to match direct locations only.

To list places instead, use `from: place`. For example, adding this filter selects waterways and lakes. List values mean *any of these*. Additional fields must *all* match. Use the spelling, case, and YAML value type from the subject’s frontmatter.

```yaml
where:
  typeOf: [waterway, lake]
```

## Members and leaders

For a current roster, use `type: affiliation` and `from: person`. The following table instead lists everyone who led the target through the selected date, including former leaders.

````markdown
```taelgar-index
type: affiliation
from: person
affiliationType: leader
scope: ever
mode: table
columns: [name, roles, joined, left]
sortBy: [joined, name]
```
````

Affiliations include `affiliations` and `leaderOf`. Omit `affiliationType` to include every relationship type, or supply a value or list such as `[member, primary]`. Membership is direct by default. Set `recursive: true` to include members of groups connected to the target through `partOf`.

## Shared options

| Option | How to use it |
| --- | --- |
| `from` | Required. Choose `person`, `place`, `object`, `group`, `power`, `event`, `ancestry`, or `creature`. |
| `target` | Supply a visible note name, alias, or path to look up a different target. Quote a wikilink, for example `target: "[[Greater Sembara]]"`. |
| `scope` | `current` uses the selected date for subjects alive or in existence then. `historical` also includes ended subjects, evaluated at death or destruction. `ever` matches any qualifying day during the subject’s lifetime through the selected date. |
| `mode`, `heading`, `show` | The default is a card grid with a heading on both hosts. Use `mode: table`, `heading: false`, or `show: website` / `show: obsidian` as needed. |
| `columns`, `sortBy` | In table mode, give either option an ordered list. Sorting is ascending and can use a hidden column. Places default to type then name. Other subjects default to name. |

All tables can show `name`, `type`, `home`, and `currentLocation`. People add `info`, `born`, and `died`. Other subjects add `created` and `destroyed`, and places also have `region` and `population`. Affiliation tables add `roles`, `joined`, and `left`. Each subject appears once. For multiple qualifying terms, `roles` collects their titles and the dates describe the most recent qualifying term.

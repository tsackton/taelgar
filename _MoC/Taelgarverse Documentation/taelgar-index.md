# `taelgar-index`

Use `taelgar-index` to list subjects by location, affiliation, or frontmatter. Obsidian and the website evaluate the index at the selected in-world date. Location and affiliation indexes default to the note containing the block.

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

The whereabouts target `Taelgar` also matches the geographic root when there is no note with that name. Set `target: Taelgar`, `via: home`, and `recursive: false` to list places directly based in Taelgar, as in the [[Gazetteer#Regions of Taelgar|Gazetteer’s regions table]]. With `recursive: true`, places can also match through visible containing locations.

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

## Catalogs

A catalog lists notes of the selected kind that match a nonempty `where` mapping. It ignores `target`. `scope: current` lists subjects in existence at the selected date. `historical` and `ever` also include subjects whose existence ended by that date.

````markdown
```taelgar-index
type: catalog
from: place
where: {typeOf: plane}
mode: table
heading: Planes of the Multiverse
columns: [name, origin]
columnHeadings: {name: Plane, origin: Planar Group}
sortBy: [origin, name]
```
````

## Shared options

| Option | How to use it |
| --- | --- |
| `type` | Required. Choose `whereabouts`, `affiliation`, or `catalog`. |
| `from` | Required. Choose `person`, `place`, `object`, `group`, `power`, `event`, `ancestry`, or `creature`. |
| `via` | Required for `whereabouts`. Choose `home`, `current`, or `lastKnown`. |
| `affiliationType` | Optional for `affiliation`. Give one relationship type or a list of alternatives. |
| `target` | Supply a visible note name, alias, or path. Quote a wikilink, for example `target: "[[Greater Sembara]]"`. Whereabouts also accepts `Taelgar`. Catalogs ignore this option. |
| `recursive` | Defaults to `true` for whereabouts and `false` for affiliation. Use `false` for direct matches. |
| `where` | Matches top-level frontmatter values exactly, including case and YAML type. A list gives alternatives for one field. All specified fields must match. Catalogs require at least one field. |
| `scope` | `current` is the default. It uses the selected date for subjects alive or in existence then. `historical` also includes ended subjects, evaluated at death or destruction. `ever` matches any qualifying day during the subject’s lifetime through the selected date. |
| `mode` | `grid` displays cards and is the default. Use `table` for configurable columns. |
| `heading` | `true` adds the default H2. Supply nonempty text for a custom H2 or use `false` to hide it. |
| `show` | `both` is the default. Use `website` or `obsidian` for one host. |
| `columns`, `sortBy` | Table-only ordered lists of distinct column keys. Sorting is ascending, with missing values last. Sort keys can be hidden. Places sort by type then name by default. Other subjects sort by name. |
| `columnHeadings` | Table-only mapping from displayed column keys to new labels. Continue to use the original keys in `columns` and `sortBy`. |

## Table columns

All tables can show `name`, `type`, `home`, `currentLocation`, `lastKnown`, `origin`, and `status`. People add `info`, `born`, and `died`. Other subjects add `created` and `destroyed`. Places also have `region` and `population`. The default columns are `[name, info, currentLocation, home]` for people and `[name, type]` for other subjects.

- `currentLocation` uses the selected date. `lastKnown` uses the current location when known, or the last known location and its date when available. You can display `lastKnown` with any index type or `via` setting.
- `origin` displays the home recorded at birth or creation, using DR 1 if neither date is recorded.
- Affiliation tables add `roles`, `joined`, and `left`. Each subject appears once. `roles` collects qualifying titles, and `joined` and `left` describe the most recent qualifying term.

### Editorial status

The `status` column shows one bucket from the note’s current YAML tags, regardless of the in-world date. The first matching rule wins.

| Bucket | Rule |
| --- | --- |
| Stub | `status/stub` is present. |
| AI review | `status/check/ai` is present. |
| Lint | `status/check/lint` is the only `status/*` tag. |
| Needs work | `status/review`, `status/wip`, `status/check/errors` or one of its subtags, or any other unmapped `status/*` tag is present. |
| Check | `status/check` or another check subtag is present. The exact AI and lint tags and the errors family use the rules above. |
| Updates pending | `status/gameupdate` or one of its subtags is present. |
| Complete | The note has no `status/*` tags. |

With `sortBy: [status]`, the order is Stub, Needs work, Check, Lint, AI review, Updates pending, Complete.

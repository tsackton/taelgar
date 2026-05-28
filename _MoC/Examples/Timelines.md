# Timeline and Event Table Examples

Timeline tables are generated with the `_scripts/view/get_EventsTable` DataviewJS view. The view reads dated event pages and dated inline list items, then renders a Markdown table in Obsidian.

The view skips top-level folders beginning with `_` and the top-level `Worldbuilding` folder. It also excludes the current page from its own table, so a page like [[Blood Years]] does not list itself when it contains an event table.

## Basic Event Table

Use `yearStart` and `yearEnd` to select the date window.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1546,
  yearEnd: 1600,
  includeAll: false
})
```
````

If `yearEnd` is omitted, the table only covers `yearStart`.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1549
})
```
````

## Event Page Dates

Event pages are included when their frontmatter has `DR`. A page can also have `DR_end` for a ranged event.

```yaml
---
DR: 1542
DR_end: 1545
---
```

Ranged events render as one row, not separate start and end rows. They are included when any part of the event overlaps the requested date window. For example, an event with `DR: 1542` and `DR_end: 1545` appears in a `1545` table because it overlaps that year.

Event page names are linked and formatted as titles in the event text, such as `[[Conclave War|The Conclave War]]`.

## Timeline List Items

Inline timeline events come from list items with a `DR` field.

```markdown
- (DR:: 1549), fall: The [[Bloodlust Wars]] ends
```

This renders with the date qualifier in the date column:

| DR | Event | Source |
| -- | ----- | ------ |
| DR 1549, fall | The [[Bloodlust Wars]] ends | Timeline of Sembaran History |

Inline ranges use `DR_end`.

```markdown
- (DR:: 1749-06-15) - (DR_end:: 1749-06-17): The delegation meets in Tollen.
```

The row keeps the true start and end dates and appears when the interval overlaps the requested table window.

## Source Filters

Use `pageFilter` to restrict which notes Dataview scans.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1,
  yearEnd: 2000,
  pageFilter: "outgoing([[Timeline of Sembaran History]])"
})
```
````

Folder names in Dataview source strings should be quoted.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1,
  yearEnd: 2000,
  pageFilter: "#event-source and \"Campaigns\""
})
```
````

You can also pass a page predicate with `where`.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1546,
  yearEnd: 1600,
  where: page => page.tags?.includes("event")
})
```
````

## Generated Events

By default, the table focuses on explicit event pages and inline timeline events. Generated events are opt-in rows derived from other metadata on scanned pages. They still respect `yearStart`, `yearEnd`, `pageFilter`, `where`, the hard-coded folder skips, and current-page exclusion.

`includeAll` enables every generated row family unless a specific option is set to `false`.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1549,
  yearEnd: 1600,
  includeAll: true
})
```
````

You can also enable only the generated row families you want.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1549,
  yearEnd: 1600,
  includeCreate: true,
  includeEnd: true,
  includeRegnal: true,
  includeTravel: true,
  includePartyMeetings: true
})
```
````

Or start from `includeAll` and turn one family off.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1549,
  yearEnd: 1600,
  includeAll: true,
  includeTravel: false
})
```
````

The generated subject names are linked and title-formatted where possible.

| Option | Default | Generated rows |
| ------ | ------- | -------------- |
| `includeAll` | `false` | Sets all generated row families to true unless a specific option overrides it |
| `includeCreate` | `includeAll` | Page start rows from `born`, `created`, or a non-event `DR` date |
| `includeEnd` | `includeAll` | Page end rows from `died`, `destroyed`, or a non-event `DR_end` date |
| `includeRegnal` | `includeAll` | Ruler reign rows from regnal metadata |
| `includeTravel` | `includeAll` | Arrival, residence, move, and departure rows from `whereabouts` |
| `includePartyMeetings` | `includeAll` | Campaign meeting rows from `campaignInfo` |

### `includeCreate`

Creates one row when the page's start date is inside the requested window. The start date comes from `born`, `created`, or from `DR` on non-event pages. Explicit event pages with `DR` are excluded from generated start/end handling because they already produce their own event row.

The row text uses the page display defaults from `NameManager`, such as `startStatus`, and adds the origin location from `whereabouts` when available.

Example output:

| Date | Event |
| ---- | ----- |
| DR 1549 | [[Example Person]] was born in [[Example Place]] |

### `includeEnd`

Creates one row when the page's end date is inside the requested window. The end date comes from `died`, `destroyed`, or from `DR_end` on non-event pages.

The row text uses the page display defaults from `NameManager`, such as `endStatus`, and adds the last known location from `whereabouts` when available.

Example output:

| Date | Event |
| ---- | ----- |
| DR 1549 | [[Example Person]] died in [[Example Place]] |

### `includeRegnal`

Creates ruler reign rows when the page has `reignStart`. The view asks `DateManager.getRegnalDates` for the start and end dates.

The start row renders as `was crowned`. The end row renders as `reign ended`. If the reign end date is the same as the page end date, the reign-end row is omitted when `includeEnd` is also enabled, which avoids duplicate death/end rows.

Example output:

| Date | Event |
| ---- | ----- |
| DR 1549 | [[Example Ruler]] was crowned |
| DR 1580 | [[Example Ruler]] reign ended |

### `includeTravel`

Creates travel rows from `whereabouts` entries with `start` and/or `end` dates.

| Whereabouts data | Generated text |
| ---------------- | -------------- |
| Entry has `start` and `type: home` | `<name> moved to <location>` |
| Entry has `start` and also has an `end` | `<name> arrived at <location>` |
| Entry has `start` only | `<name> was at <location>` |
| Entry has `end` | `<name> left <location>` |

Example frontmatter:

```yaml
whereabouts:
  - {type: home, location: Tollen, start: 1549}
  - {location: Valarin, start: 1552, end: 1553}
```

Example output:

| Date | Event |
| ---- | ----- |
| DR 1549 | [[Example Person]] moved to [[Tollen]] |
| DR 1552 | [[Example Person]] arrived at [[Valarin]] |
| DR 1553 | [[Example Person]] left [[Valarin]] |

### `includePartyMeetings`

Creates campaign meeting rows from `campaignInfo` entries that have both `campaign` and `date`. The row text is formatted through the existing party-meeting helper, using entry-level `wParty` or `format` when present, otherwise the page display default.

Example frontmatter:

```yaml
campaignInfo:
  - {campaign: DuFr, date: 1549, type: met}
```

Example output:

| Date | Event |
| ---- | ----- |
| DR 1549 | [[Example Person]] met the party |

Generated event rows are point-in-time rows. They are included when their generated date falls inside the requested window; explicit `DR` / `DR_end` event ranges use interval overlap instead.

## Custom Columns

Pass `header` and `map` to customize the rendered table.

````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {
  yearStart: 1546,
  yearEnd: 1600,
  header: ["Date", "Event", "Ends", "Source"],
  map: e => [
    e.date,
    e.text,
    e.isRange ? e.dateEnd : "",
    dv.fileLink(e.file)
  ]
})
```
````

Rows include these fields for custom maps:

| Field | Meaning |
| ----- | ------- |
| `date` | Display date, including qualifiers such as `fall` |
| `dateStart` | Display start date without the source text |
| `dateEnd` | Display end date for ranged events |
| `startDate` | Parsed start date object |
| `endDate` | Parsed end date object |
| `isRange` | True when the row has a real interval |
| `year` | Numeric start year |
| `sort` | Start sort key |
| `sortEnd` | End sort key |
| `text` | Rendered event text |
| `rawText` | Original source text when available |
| `file` | Source file path |
| `dateQualifier` | Parsed qualifier such as `summer` or `fall` |

## Plain Dataview Examples

Plain Dataview can still be useful for ad hoc checks. This lists dated list events whose text mentions the current file name.

````
```dataview
LIST WITHOUT ID events.text
FROM #event-source
FLATTEN file.lists AS events
WHERE contains(events.text, this.file.name)
SORT events.DR
```
````

## Notes

Date qualifiers such as `spring`, `summer`, `fall`, and `winter` are used as a sorting hint within a year. This is intentionally heuristic and is meant to keep common seasonal timeline entries in a readable order.

The event table view is designed for event and timeline display. It can preserve common wiki links in list items, but it is not a general prose parser.

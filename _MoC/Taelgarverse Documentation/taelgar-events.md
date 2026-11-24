# `taelgar-events`

Use `taelgar-events` to render a chronological table with **Date**, **Event**, and **File** columns. It is available in Taelgarverse for Obsidian 3.3.0 and on the website.

This example includes authored dates from event notes and from people known to the Dunmar Fellowship. It also includes dated lifecycle entries from those sources.

````markdown
```taelgar-events
yearStart: 1546
yearEnd: 1600
includeLifecycle: true
sources:
  - {type: event}
  - {type: person, knownTo: dufr}
```
````

## Block options

| Option | Behavior |
| --- | --- |
| `yearStart` | Required. Use a DR year or a quoted `YYYY-MM-DD` date. A year starts on January 1. |
| `yearEnd` | Defaults to `yearStart`. A year ends on December 31. Both bounds are inclusive. |
| `includeLifecycle` | Include dated starts and ends, such as births, deaths, foundings, and destructions. Defaults to `false`. |
| `includeTravel` | Include dated arrivals, moves, visits, and departures from `whereabouts`. Defaults to `false`. |
| `heading` | Add an **Events** H2 with `true`. Defaults to `false`. |
| `show` | `both` is the default. Use `website` or `obsidian` for one host. |
| `sources` | A list of source selectors. Omit it to include every eligible source. `sources: []` selects none. |
| `excludeSources` | A list of selectors whose matches are excluded. |

## Source selectors

Each list entry is a mapping. Every field within an entry must match the same source note. A match to any entry in `sources` includes that note. A match to any entry in `excludeSources` excludes it. Selectors apply to the note storing the date.

| Field | Matches |
| --- | --- |
| `folder` | A vault-relative folder and its descendants. |
| `note` | A note name, path, or quoted wikilink. |
| `type` | The source note’s descriptive tag, such as `event`, `person`, `place`, or `session-note`. Use the canonical type names from [[Note Categorization]]. |
| `knownTo` | A campaign from the source note’s authored `knownTo` list. |
| `campaign` | The campaign recorded in the source note’s `campaign` field. |

Use a registered campaign ID such as `dufr` or `clee` for `knownTo` and `campaign`. For example, `sources: [{folder: Campaigns, type: session-note, campaign: clee}]` selects Cleenseau session notes in the Campaigns folder.

## Dates and visibility

Authored events come from frontmatter `DR` and from Markdown list items with an inline `DR::` field. Use `DR_end` or a date string with `to` to record a range. A range appears once when it overlaps the requested window. Year and month precision is preserved in the date label.

```markdown
- (DR:: 1549), fall: The [[Bloodlust Wars]] end.
- (DR:: 1749-06-15) (DR_end:: 1749-06-17): The delegation meets in Tollen.
```

Recognized qualifiers such as `fall:` and `morning:` appear in the date label and help order events. Double parentheses around an inline date field record uncertainty.

The block skips its own source note and notes under `Worldbuilding`, underscore-prefixed folders, or dot-prefixed folders. Obsidian uses the whole requested date window, including local date and campaign variants. The website applies publication and reader-context visibility. It shows an event range or partial date once its latest possible date is within the reader’s context.

## Migrating an old timeline

The `get_EventsTable` DataviewJS view has been retired. When migrating a saved query, copy its `yearStart` and `yearEnd`. To carry over births, deaths, and travel from `includeAll: true`, set `includeLifecycle: true` and `includeTravel: true`. Generation of party-meeting rows from `campaignInfo` was specific to the old view.

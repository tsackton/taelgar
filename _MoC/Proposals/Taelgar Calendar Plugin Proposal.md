---
tags: [meta, status/check/ai]
---
# Taelgar Calendar Plugin Proposal

> [!info] Proposal
> Prepared October 19, 2026. This is a design and implementation plan for a new Obsidian plugin. Implementation has not started. The data structures, defaults, and milestones below are proposed; saving this note does not adopt new calendar lore or authorize implementation.

## Objective

Build a calendar for Taelgar that combines a familiar month view with a historical timeline. It should be useful both for running a campaign and for looking across centuries of world history. Events should stay attached to their source notes, and different calendars should describe the same underlying days.

Required capabilities:

- Recurring events on fixed dates, ordinal weekdays, lunar phases, solar events, and combinations of these: May 15 every year; the first Saturday of June; the first new moon after the winter solstice.
- Single-day and multi-day events, with sensible treatment of long events. A year-long event should not occupy every day in a month grid.
- Zoom from multiple centuries through decades and years to a month.
- Moon phase display and solar-event markers.
- Alternative calendar structures and year reckonings.
- Session spans from their in-world start and end dates.

The recommended approach is a standalone plugin with an independent date engine. Use Fantasy Calendar as a compatibility reference and migration source. Evaluate Calendarium for reusable ideas before building, but avoid making the core date model depend on another plugin's mutable internal state.

## Existing implementation and sources

The initial inspection covered the installed Fantasy Calendar 3.0.0 manifest, compiled implementation, active `data.json`, Taelgar date utilities, and representative notes. This was not a complete calendar or holiday audit.

| Source | Relevant behavior or evidence |
| --- | --- |
| `.obsidian/plugins/fantasy-calendar/manifest.json` | Installed version 3.0.0. |
| `.obsidian/plugins/fantasy-calendar/data.json` | Taelgar uses 365 days, familiar month lengths, no leap days, seven weekdays, and one moon with cycle 29.5 and offset 4. Solar markers are March 21, June 21, September 21, and December 21. These are existing operational settings, not a new canon decision. |
| `.obsidian/plugins/fantasy-calendar/main.js` | Date and span matching, simple recurrence with omitted date components, day intervals, month/year views, and moon graphics. Moon display rounds the cycle into a set of phase labels. |
| `_scripts/customJS/dataUtil.js` | `DateManager` provides DR calculations, date normalization, and current-date access through Fantasy Calendar with a Calendarium fallback. It also contains CY display logic that must be checked against adopted lore. |
| [[Metadata Specification#Date Formats]] | Dates may have year, month, or day precision; `0001` and `9999` can be sentinel values. |
| [[Calendar Eras]] | Different new-year boundaries and year-counting systems, including DR, CY, dynastic years, regnal years, and named years. |
| [[Aagirvala]] | First full moon after the autumnal equinox; existing `fc-date` records one 1748 occurrence. |
| [[Feast of Bhishma]] | Existing unresolved differences between recurrence descriptions and between stored dates and the session record. Migration must retain those conflicts for review. |
| [[Session 43 (DuFr)]] | Example session span: July 19–23, 1748 DR, with a separate real-world play date. |
| [[Summer of Red Storms]] | Example month-precision endpoints. |

The saved calendar includes duplicate events, stale note paths, and an invalid parsed date. Rebuild note-derived events from their sources rather than treating the saved event array as authoritative. Separately preserve events that exist only in plugin storage until reviewed.

The original [Fantasy Calendar repository](https://github.com/fantasycalendar/obsidian-fantasy-calendar) is archived and marked unmaintained. Its documented features include spans, intervals, simple recurrence, note links, and configurable calendars. [Calendarium](https://github.com/javalent/calendarium) is another implementation reference; its suitability for this design has not been established.

## User experience

Provide a full-width Obsidian tab and a compact sidebar view. Both use the same selection, filters, event queries, and date engine.

- **Toolbar:** previous/next period, jump to date, zoom level, calendar system, and campaign-date shortcut.
- **Layer controls:** historical events, sessions by campaign, holidays by tradition or region, and astronomy. Saved filter presets are useful for campaign play and historical research.
- **Main display:** month grid at close range, timeline at broader scales.
- **Details panel:** selected day or event, source note preview/link, alternative date labels, recurrence explanation, and relevant uncertainty.

| Scale | Default display |
| --- | --- |
| Multiple centuries | Long periods, major events, and clusters of smaller dated events. |
| Century and decade | Duration bars, milestones, and progressively more detail. |
| Year | Twelve-month overview, campaign activity, significant spans, and optional festivals. |
| Month | Event bars across days, session spans, moon icons, solar markers, and overflow counts. |
| Selected day | Agenda and details, including continuing events. |

Zoom around the selected day rather than resetting to the beginning of a period. Preserve date selection and filters when changing the calendar system. Allow keyboard navigation, accessible labels for moon icons, and explicit controls as an alternative to scrolling or dragging. Color should not be the only way to distinguish campaigns or event types.

Browsing a historical date does not change the campaign's current date. Keep three states distinct: the browsed date, a campaign's configured date, and the active date used by existing vault scripts. Changing the latter requires an explicit action.

### Long events and uncertain dates

Use a display policy rather than repeating every overlapping event in every day cell:

- Short spans appear as bars, clipped at the viewport boundary with continuation indicators.
- Long background spans move into a collapsed **Ongoing during this month** list.
- Starts and ends occurring in the visible month remain available as milestone markers.
- Per-event overrides can force normal display, background display, or visibility at a chosen scale.
- Sessions have a separate default so a long travel session remains discoverable even if historical background is collapsed.

Initial candidate: month-view background treatment for events lasting at least 90 days, plus explicitly marked background events. Tune this against real notes; the threshold is not an adopted requirement. A year-long event must be hidden from ordinary day lanes by default but accessible through the ongoing list and search.

Do not confuse duration with date precision. An event known only to have occurred in 1555 has an uncertain position within that year; it is not a 365-day event. Show such points in an undated-within-period list or with an uncertainty band. A span with imprecise endpoints has uncertain boundaries, not fabricated exact start/end dates.

## Date and calendar engine

Use a continuous integer day count internally, with an explicitly chosen epoch. The epoch is an engineering coordinate and should not establish a creation date as lore. Optional fractions of a day support phase crossings; ordinary vault dates remain day-level.

Do not use JavaScript `Date` as the in-world calendar engine. DR has no Gregorian leap years; machine timezone and daylight-saving changes must not affect results. Real-world session dates use a separate civil-date adapter.

Each calendar adapter should provide equivalent operations to:

```typescript
validate(date): ValidationResult
toDay(date): AbsoluteDay
fromDay(day): CalendarDate
periodBounds(period): { start: AbsoluteDay; endExclusive: AbsoluteDay }
weekday(day): WeekdayId | null
format(date, options): string
```

Calendar definitions need stable IDs, month/cycle structures, weekday IDs and labels, year-boundary rules, intercalary behavior, and a mapping to absolute days. Public authored month numbers should be one-based; convert the legacy plugin's zero-based internal months only at its adapter boundary.

Support signed day counts internally. Before exposing early historical dates, decide year-zero and pre-DR notation explicitly. Do not infer these from the host date library. Sentinel `0001` and `9999` values in legacy metadata must be interpreted by the relevant metadata adapter, not rendered as literal calendar events.

### Precision and endpoints

Retain the authored value and precision alongside normalized bounds. Proposed date value:

```typescript
type DateValue = {
  calendar: string;
  year: number;
  month?: number;
  day?: number;
  precision: "year" | "month" | "day";
  original: string | number;
};
```

For exact spans, display inclusive end dates to the user and convert to half-open intervals internally: July 19–23 becomes `[July 19, July 24)`. This makes overlap queries and clipping consistent. Store earliest/latest possible endpoint bounds for imprecise spans. Distinguish missing end, explicit blank end, and explicit end; preserve source semantics instead of treating every blank as a single day or an event continuing forever.

The existing `DateManager` normalizes numeric years and year strings differently and uses particular start/end defaults for month strings. Do not silently carry those defaults into calendar placement or globally change them while adding the plugin. Audit consumers and use explicit adapters, with tests and a separate migration decision for legacy behavior.

### Alternative reckonings

Different year labels and genuinely different month/week structures should share the same underlying clock:

- DR starts January 1.
- CY starts March 17; the approximate year offset in [[Calendar Eras]] is insufficient for exact conversion around that boundary. Verify an exact epoch correspondence before shipping conversion.
- Dunmari dynastic years start January 23 and need a dynasty table.
- Sembaran regnal years need monarch and coronation boundaries.
- Named years need a lookup table, with missing names left unknown.
- A structurally different calendar may have intercalary days outside the weekday cycle.

[[Dwarven Calendar - Ideas]], [[Elven Calendar - Ideas]], and [[Hkar Calendar - Ideas]] remain development sources. Existing code is not evidence that every structural detail in those ideas has been adopted. Implement confirmed mappings first; label experimental definitions and leave unsupported conversions unavailable.

Recurrence is evaluated in the event's calendar, then displayed in the viewer's calendar. Switching the viewer must not change which absolute days an event occupies.

## Astronomy

Start with the existing operational model: a 29.5-day lunar cycle and fixed solar dates. Preserve the legacy offset only after verifying its epoch and direction against actual legacy calculations.

Separate continuous lunar phase from the icon displayed for a day. For an adopted anchor `t0` and cycle `P`, phase is the positive fractional part of `(t - t0) / P`. New/full moon occurrences come from phase crossings, not from whichever dates round to a “new moon” or “full moon” icon.

Define and test the convention assigning fractional crossings to dates. For the first version, use one configured world-day boundary; do not introduce Earth timezones. Day/night observance language can be retained as descriptive timing until a more detailed time model is adopted. Distinguish “strictly after this date” from “at or after this instant”; the recurrence editor must state the chosen policy.

Solar events should have stable identifiers such as `winter-solstice`, independent of display names. Initially they are configured annual anchors. Latitude-dependent sunrise/sunset, eclipses, weather simulation, and a physical orbital model are outside the first implementation.

## Event model and recurrence

Keep authored event definitions separate from computed occurrences. Each definition has a stable identity, source reference, title, kind, date/span or recurrence, optional duration, filters, and presentation preferences. Each occurrence points back to that definition and records its original anchor, calculated span, exception status, and explanation.

One note may eventually contain several event definitions. Use a stable per-note event key for identity; do not generate a new identity on each scan or deduplicate unrelated events merely because their titles and dates match. Note-derived events should be unique by source and event key. Recurring occurrence identity should use the definition plus original recurrence anchor, so moving an occurrence does not create a duplicate.

Proposed recurrence operations:

| Operation | Example |
| --- | --- |
| Fixed month/day | May 15 every year. |
| Day of every month | The 15th of each month. |
| Ordinal weekday | First Starday of June; last Moonday of each month. |
| Day interval | Every 10 days from a specified anchor. |
| Lunar phase | Every new moon, or first full moon within a specified month. |
| Solar anchor | Winter solstice each year. |
| Relative occurrence | First new moon after winter solstice. |
| Offset and duration | Begin one day before the chosen phase and last two days. |
| Named-event dependency | Third new moon after another festival. |

Use a small declarative rule tree. Avoid arbitrary executable expressions in note metadata. The rule schema should define calendar, annual/monthly scope, ordinal, comparison policy, date offset, duration, validity bounds, and exceptions. Validate impossible dates, unsupported rules, missing anchors, and cyclic event dependencies. For an absent fifth weekday, propose skipping that month's occurrence rather than moving it silently; show this policy in the editor.

Illustrative metadata, not an adopted field specification:

```yaml
calendarEvents:
  - id: winter-observance
    kind: holiday
    calendar: dr
    recurrence:
      type: annual-relative
      anchor: {type: solar, event: winter-solstice}
      select: {type: lunar, moon: taelgar-moon, phase: new, ordinal: 1, relation: strictly-after-day}
      offsetDays: 0
    durationDays: 1
    display: {placement: auto}
```

The editor should produce a readable sentence and preview the next several occurrences, with the anchor and calculation steps. Annual rules anchored in December must retain occurrences that fall in January of the following year. Query neighboring anchor periods and account for offset/duration when finding overlapping occurrences.

Exceptions should support cancellation and replacement of one occurrence. The original rule remains intact. An occurrence documented in a session may be an exception or evidence of a wrong rule; the software should report that conflict rather than change recorded play automatically.

## Vault integration and ownership

Notes remain authoritative for events. Versioned configuration holds calendar definitions and astronomy settings; runtime caches are disposable. Personal view state and filters should not cause frequent edits to shared event notes or shared configuration.

| Input | Adapter behavior |
| --- | --- |
| Event notes: `DR`, `DR_end` | Points or spans with preserved precision and endpoint semantics. |
| Session notes: `DR`, `DR_end` | Campaign-colored session spans; show session number, title, and source link. |
| `realWorldDate` | Details or separate real-world view, never an inferred conversion to DR. |
| Legacy `fc-date`, `fc-end`, `fc-category`, `fc-display-name` | Compatible legacy events, including omitted components used for recurrence. |
| Proposed `calendarEvents` | Explicit definitions and composable recurrence. |
| Session-processing artifacts | Optional future adapter; default to final session notes to avoid duplicate representations. |

Resolve campaign identity through the live campaign registry, currently `_scripts/session_note_campaigns.json`. Recheck its location before implementation; another proposal's future registry path is not an implemented dependency. Use canonical codes internally and preserve intentional display labels.

For a logical event with both explicit new metadata and a legacy representation, select one adapter by documented precedence and report disagreements. Proposed priority: explicit event definition, then note-type-specific DR fields, then legacy FC fields. Allow intentionally separate event definitions only through distinct IDs.

Do not scan arbitrary prose or comments for dates by default. Opt-in inline timeline parsing can be added later with source-line provenance. Likewise, births/deaths, affiliations, and whereabouts should be separate optional layers rather than flooding the initial calendar.

Observe explicit folder scope and source visibility. Exclude `_sessions`, test fixtures, Worldbuilding drafts, and private DM folders from the default published-note index. A local DM layer can be enabled deliberately. Campaign/date filters are convenience features, not publication access controls; a future website export needs its own safe source selection.

## Architecture and performance

Proposed components:

1. **Core:** pure TypeScript date values, calendar adapters, interval operations, astronomy, recurrence, validation, and explanations. No Obsidian or browser globals.
2. **Vault adapters:** metadata parsing, campaign resolution, source identity, legacy import, and diagnostics.
3. **Index and queries:** normalized definitions, interval search, recurrence expansion, cache invalidation, and aggregation.
4. **Views:** month grid, timeline, agenda/details, filtering, and calendar switching.
5. **Editor:** readable rule builder, previews, exceptions, and controlled note updates. Added after the read-only viewer.
6. **Compatibility API:** explicit access to dates, queries, current-date state, and change notifications for existing scripts.

Possible source modules are `core/calendars`, `core/astronomy`, `core/recurrence`, `adapters/vault`, `index`, `views`, and `api`. Choose the source repository and build/deploy process before creating them; only compiled plugin outputs belong in the installed plugin directory unless local engineering conventions say otherwise.

Index Obsidian metadata at startup and update only changed notes. Handle deletion and rename notifications without creating stale duplicate records. Cache occurrences by definition revision, calendar/astronomy revision, and requested window. Query overlap, not just start dates. Expand recurring rules only near the visible interval, including a sufficient lookback for duration and offsets.

At century scale, suppress or summarize ordinary recurring holidays before expansion. Cluster dense points and virtualize timeline rows. Filters should run before expensive expansion where possible. Use a worker only if measurement shows indexing or expansion blocks interaction; do not make worker infrastructure a prerequisite for the first viewer.

Choose the rendering library after a small proof that it accepts arbitrary day coordinates and non-Gregorian month layouts. A library that assumes Gregorian `Date` values is a poor core dependency. A custom month grid plus an SVG or canvas timeline is a reasonable starting option. Keep accessible event lists alongside any canvas rendering.

### Current-date compatibility

`DateManager.getTargetDateForPage()` currently checks an override date, then a page-specific date, then the external calendar API. Preserve those priorities. Provide a small Taelgar calendar API and update the relevant integration in a separate reviewed change; avoid impersonating the entire Fantasy Calendar API.

Setting the active in-world date should emit a documented change event and trigger the affected headers/queries to refresh through supported mechanisms. Merely navigating the calendar should emit only view-state changes. Replacing the plugin must not unexpectedly change the dates used by existing notes or website materialization.

## Migration

1. Inventory current settings, plugin-only events, note-derived events, duplicate identities, missing note targets, invalid dates, and affected API consumers. Preserve a baseline snapshot before any migration writes.
2. Rebuild note-derived events from note metadata. Keep plugin-only events in a reviewable import list; do not delete legacy data.
3. Translate straightforward fixed-date recurrence mechanically. Lunar rules described only in prose need reviewed structured definitions. Do not infer that one stored occurrence is an annual fixed-date holiday.
4. Compare weekdays, displayed moon phases, exact dates, spans, and representative historical ranges with the legacy calendar. Explain intentional differences between rounded icon matching and phase-crossing recurrence.
5. Run the new viewer alongside the old plugin in read-only mode. Resolve mismatches and adopt the necessary astronomical/calendar anchors.
6. Change current-date integration only after parity checks. Disable the old plugin after the replacement is accepted; retain a recoverable configuration snapshot. Do not run two authoritative current-date writers.

Imports must be repeatable without duplication. Preview changed notes and imported definitions before writes. No global metadata renaming or broad note cleanup is required to deliver the initial viewer.

## Delivery stages and acceptance criteria

| Stage | Deliverable | Acceptance |
| --- | --- | --- |
| 0. Adopt foundations | Repository choice, date conventions, baseline fixtures, reviewed anchors | Required decisions below are settled or explicitly isolated as provisional; no silent canon choices. |
| 1. Date engine | DR arithmetic, precision, intervals, astronomy, adapter interfaces | Round trips and boundary tests pass; output is independent of host timezone. |
| 2. Read-only month view | Existing events, sessions, astronomy, layers, details, long-event treatment | Session 43 spans July 19–23; year-long events leave day lanes; unknown endpoints and coarse dates remain visibly uncertain. |
| 3. Recurrence | Rule engine, editor previews, exceptions, reviewed holiday migration | Fixed dates, ordinal weekdays, lunar/solar combinations, offsets, and cross-year occurrences work without duplicates. |
| 4. Zoom and calendars | Year/decade/century views, clustering, approved alternative adapters | Selection survives zoom/calendar changes; broad views remain usable; conversion preserves absolute days. |
| 5. Editing and cutover | Note-backed event creation/editing, current-date compatibility, legacy retirement | Writes preserve unrelated metadata/prose; existing date-sensitive notes keep working; rollback is documented. |

The first useful user-facing milestone is Stage 2. Later features are part of the intended scope, not prerequisites for reviewing the month-view design. Website integration, timed appointment scheduling, notifications, sunrise/sunset, and weather generation remain separate possible extensions.

### Test plan

- Date round trips at month/year boundaries, years below 100, signed day counts, and the chosen year-zero convention. Reject invalid dates rather than rolling them into another month.
- Numeric versus quoted year input; month/day precision; sentinel years; missing versus explicit blank ends; exact one-day and cross-year spans.
- Inclusive displayed ends versus exclusive internal ends. Multi-day events beginning before the viewport still appear when they overlap it.
- Weekday alignment over multiple years, ordinal and last weekdays, absent fifth weekdays, and intercalary days that do not advance the week.
- Lunar crossings at day boundaries, strictly-after versus inclusive rules, offsets into previous periods, and December anchors producing January events.
- Exceptions retain original occurrence identity; dependent festivals reject cycles; a rule change invalidates affected caches.
- Alternative-calendar round trips across March 17, January 23, and adopted coronation boundaries; unmapped names/eras remain unknown.
- Metadata indexing after edits, deletions, and renames; rebuild consistency; repeatable imports; source precedence without accidental merging.
- Read-only views do not write to notes or change the active date. Editor writes preserve unrelated sections and frontmatter.
- Month and century views on a representative full-vault dataset. Set performance budgets after measuring the baseline; do not invent a supported maximum from a small fixture.
- Manual Obsidian review of keyboard navigation, dense days, long bars, narrow panes, dark/light themes, source previews, and current-date refresh behavior.

Use real vault examples as regression fixtures only after their relevant dates are confirmed. Preserve the Feast of Bhishma disagreement as an expected diagnostic rather than encoding one disputed answer as correct.

## Decisions needed before implementation

1. Source repository, plugin identifier, UI framework, and build/deploy convention.
2. Exact absolute-day epoch, DR weekday anchor, early-year notation, and supported historical range.
3. Lunar anchor and phase-to-day policy, including whether a ritual's night belongs to the preceding or following civil date.
4. Which alternative reckonings and structural calendars are sufficiently established for the first release.
5. Final event metadata schema, editor storage location for events without notes, and precedence for conflicting representations.
6. Default layers and long-event thresholds, and how much historical importance should be authored versus inferred from scale/duration.
7. Global versus per-campaign current-date settings and the explicit mechanism for selecting the active date used by existing scripts.

When resuming, first reread this proposal, the applicable engineering instructions, the active plugin settings, and the current date utilities. Recheck the source inventory, then resolve the foundations and build the read-only engine/view milestone. Do not start by migrating holiday notes or replacing the installed plugin.

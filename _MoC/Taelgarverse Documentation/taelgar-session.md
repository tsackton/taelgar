# `taelgar-session`

Use the singular `taelgar-session` fence to show a campaign’s play history in Obsidian or on the Taelgarverse website. The history draws on numbered session notes, arc headings, registered bundles, and entries on the campaign index.

## Define a history and reuse it

Put at most one session fence on the registered campaign index. An empty fence there derives the history from the vault. On other notes, supply the lowercase ID from the [[_MoC/Campaign Registry|Campaign Registry]]. Display options apply to that copy. For example, this view shows only Addermarch adventures and solos alongside selected campaign summary fields.

````markdown
```taelgar-session
campaign: adma
kinds: [adventure, solo]
columns: [session, account, played, dr]
summary: [count, played, dr]
```
````

## Display options

| Option | Behavior |
| --- | --- |
| `campaign` | Lowercase registered ID. Required off the registered index. On a registered index, omit it or use that index’s own ID. |
| `kinds` | One kind or a list from `adventure`, `solo`, `inter-session`, and `meeting`. Filters the rows. The campaign summary still covers the campaign as a whole. |
| `columns` | The default is `[session, account, played, dr]`. `session` gives the number or event label, `account` links to the account using its session title where available, `played` gives real-world dates, and `dr` gives in-world dates. Add `title` for a separate title column. |
| `characters`, `participants`, `people` | Values for `columns` that add expandable details. `characters` shows the in-world cast and companions. `participants` shows who attended, including the DM where recorded. `people` combines the two and shows differences. Choosing both `characters` and `participants` also gives the combined view. |
| `evidence`, `note` | Values for `columns` that add expandable sources and date differences, or an authored note. |
| `summary` | Omit or use `true` for the default summary (`count`, `played`, `dr`) alongside the history. Use `false` for the history alone, `only` for the default summary alone, or a list drawn from `first`, `latest`, `count`, `played`, and `dr` to choose fields alongside the history. |

The summary’s `count` counts adventures and solos. `first` and `latest` refer to session numbers. `played` and `dr` give the real-world and in-world spans. Exact endpoints can also show elapsed time.

## Correct or add particular sessions

Put `overrides` and `estimate` in the session fence on the registered campaign index. A fence embedded elsewhere reads those definitions from the index.

| Override field | Behavior |
| --- | --- |
| `number` or `id` | Identify each entry with one of these fields. Quote a point number such as `"12.10"` to preserve its full identifier. An unnumbered event uses a lowercase hyphenated `id` and `kind: meeting` or `kind: inter-session`. |
| `kind`, `title` | Set the entry’s category or descriptive title. |
| `played` or `date` | Give the real-world date using either field. A list records separate sittings of one session. |
| `dr`, `drEnd` | Set the in-world start and end. The preferred dated session note ordinarily supplies `DR` and `DR_end`. Other numbered notes, bundle manifests, and recaps can supply dates when that note has none. |
| `attendance` | Replaces the session’s attendance list. Each entry requires `player` and can give the `character` played and `role: player` or `role: dm`. |
| `characters`, `companions` | Replace the respective lists of characters present in the story. These fields are independent of the attendance list. |
| `account`, `evidence`, `note` | `account` can link to a note, heading, or block. `evidence` accepts text or a list of citations. `note` records an explanation for the row. |

This excerpt from [[Dunmari Frontier Index#Play history|Dunmar’s play history]] records an unnumbered meeting, a solo with attendance, and an uncertain date window. Add entries under the existing `overrides` list when an index already has a session fence.

````markdown
```taelgar-session
overrides:
  - id: session-zero-meeting
    kind: meeting
    title: Session 0 organizing meeting
    date: "2020-04-17"
  - number: "29.1"
    kind: solo
    played: "2021-09-05"
    attendance:
      - player: David Kong
        character: Kenzo
  - number: "31.1"
    kind: inter-session
    played:
      from: "2021-09-24"
      through: "2021-10-07"
      qualifier: possible window
```
````

For dates, use a quoted value such as `"2021-12-05"`, an `on` mapping for a qualified date, `from` and `through` for a window, or `label` for a description such as a season. Use `alternatives` with at least two date entries for an unresolved discrepancy. Date mappings can carry `qualifier` and `evidence`. See [[Great Library Index#Play history|Great Library’s play history]] for examples of inferred dates and sessions with multiple sittings.

### Attendance and character presence

The preferred session note’s nonempty `players` field supplies the in-world cast. Other numbered notes or the recap’s `PCs` header can supply cast when needed. Recorded attendance comes from session speaker statistics, with participant metadata helping identify speakers and roles. For older sessions without those records, the original cast and usual player assignments can supply inferred attendance. An `attendance` override replaces that derived list. A `characters` override updates the in-world cast while preserving the source evidence used for attendance.

Use `attendance: []` or `characters: []` for a known empty list. Use `attendance: null` or `characters: null` when the corresponding information is unknown.

### Estimate a campaign-wide history

Use `estimate` for a historical count or date span that the sources support at campaign scale. It accepts a nonnegative integer `count`, optional `first` and `latest` session numbers, `played` and `dr` date spans, and `note` and `evidence`. It supplies summary information without creating session rows. This example is drawn from [[Great War Index#Play history|Great War’s play history]].

````markdown
```taelgar-session
summary: only
estimate:
  count: 110
  first: "1"
  latest: "110"
  played:
    label: Fall 1993 to late spring or early summer 1997
  dr:
    from: "1544"
    through: "1545"
    qualifier: approximate start year
```
````

Use [[taelgar-roster]] for the corresponding players, characters, and appearance links.

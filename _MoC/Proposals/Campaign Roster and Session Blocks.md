# Campaign Roster and Session Blocks

> [!info] Design proposal · 22 November 2026
> Two proposed Taelgarverse blocks would show who played in a campaign and when they played. The campaign indexes already contain the reviewed rosters and play histories in ordinary Markdown. Both blocks are awaiting implementation. The November 2026 migration provides the baseline for comparing their output.

## What the reader sees

On a campaign index, **Roster** would show one row per player, their characters, and an expandable list of documented sessions. **Play history** would show the adventures in order, with local play dates, in-world dates where known, and a link to the best available account. Selecting a session from a roster row would lead to the same session that appears in the history.

Other notes could reuse either view. A campaign introduction might show just the characters and a short list of recaps. The DM could open the index to see guest players, inter-session correspondence, or the basis for a reconstructed date. Correcting a fact once should update both pages.

## Where to edit a fact

| Fact | Where it belongs |
| --- | --- |
| The usual player of a PC, and that character’s party affiliations | The PC note. The index’s `partyPage` identifies the campaign’s party. A former member still belongs in a historical roster. |
| A player’s role in this game, a guest from another party, or a character who has no PC page | The campaign index, when the ordinary sources need a qualification or supply no entry. A historical or non-main game can keep its entire roster here. |
| A session’s account, dates, and participants | The session note, arc heading, or registered bundle where they are documented. An index can supply a correction, a missing sitting, or an entire historical session. |
| Session-specific attendance | Record it with the session. Both the sessions view and the roster’s appearance links read that evidence. A substitute at one sitting leaves the PC’s usual player intact. |
| Estimates, disputes, and research citations | Keep the qualification and source with the fact. Detailed reconstructions and private correspondence can stay in their existing nonpublic sections of the index. |

The lowercase ID in `_sessions/campaign-registry.json` identifies the owning index. Each block type would have one defining block on that page. An empty defining block asks for the ordinary derived view. Elsewhere, `campaign: grli` means “read Great Library’s definition and render it here.” Display options apply only to that occurrence. The renderer should flag overrides entered on a secondary page or two competing definitions on the index. See [[_MoC/Campaign Registry|Campaign Registry]].

## `taelgar-roster`

Start with PC notes whose affiliation resolves to the registered party, and read each PC’s `player`. Apply the index entries one field at a time. A linked character brings its usual player from the PC note. A player-only entry can add someone whose character is unknown or change the campaign role of someone already present. An unlinked character name can carry a short description. Preserve draft assignments and manual judgments when migrating them.

For example, the following YAML could go inside the roster block on [[Great Library Index]]. These three entries illustrate the syntax and cover only part of that roster.

```yaml
overrides:
  - player: Abigail Raiche
    role: other
  - character: "[[Oskar]]"
    kind: guest
  - character: "[[Stoneclaw]]"
    kind: companion
```

Abigail’s pairing with [[Scordith]] already comes from the PC note. Her entry adds her campaign role. Oskar and Stoneclaw bring Nathaniel Sackton into this roster through their existing PC notes. A roster built entirely on the index uses the same entries. In [[Plaguelands Index]], for instance, Mike Sackton can have a player row with a note about his uncertain character assignment.

Keep player role and character kind as separate filters. David Kong was a core Dunmar player, played Kenzo as a party member, and also played Mikasa as a guest. A block on another page could show only the main characters of core players with the following settings.

```yaml
campaign: dufr
playerRole: core
characterKind: member
columns: [character]
```

This would include Kenzo and omit Mikasa. A single character column should render as a simple list. The full index view could group both characters under David. The rule for inferring `core` or `other` from ordinary affiliations still needs calibration against the reviewed roster. Attendance frequency alone does not establish either role.

## `taelgar-sessions`

Start from the campaign’s session notes and registered bundles. Join records by campaign and complete session number, using the registered parent directory and folder suffix for bundle identity. Keep point numbers as strings so `"12.1"` and `"12.10"` stay distinct. A Great Library arc note can contribute several sessions through its headings. A raw-only folder is a lead. Count a session as played once a source documents play.

The proposed index syntax uses the same `overrides` list for a missing detail or a complete historical entry. For example, the Dunmar review identifies December 5 as the local evening of session 35. It also identifies David Kong as the sole player in the solo numbered 29.1. Each entry supplies only the fields that need adding or correcting.

```yaml
overrides:
  - number: "35"
    played: "2021-12-05"
    note: "Local evening of play. The session note and manifest give the December 6 UTC date."
  - number: "29.1"
    kind: solo
    attendance:
      - player: David Kong
```

The reviewed correction would supply the displayed date while retaining the source discrepancy. Where two sources disagree and the review leaves the matter open, show the alternatives and their evidence. A qualification such as *inferred*, *possible window*, or *year only* should travel with the date wherever it is displayed. For an adventure played in two sittings, retain both dates under one session. A campaign-wide estimate can stand on its own, as it does in [[Great War Index]].

For attendance, session-note `players` names PCs. A manifest’s `participants` can pair a real person with a `gameRole`, including the DM. Keep DM participation, PC appearances, and companions distinguishable. An explicit session-specific pairing takes precedence over the usual PC pairing for that sitting. Match recognizable PC links and aliases within the campaign and surface ambiguous names for review. A missing attendance list leaves participation unknown. Both views count a documented appearance once when a note, bundle, and index describe the same session. See [[Metadata Specification]].

The Dragonets campaign page could request a compact list of played adventures.

```yaml
campaign: dragonets
kinds: [adventure, solo]
columns: [session, played, account]
```

A campaign summary could show the latest numbered session, the number of adventures played, and the first and latest documented dates. Calculate these from the full reviewed history. A compact list can show how many rows its filter selects. In Dunmar, “139” answers which numbered session came last, while “141” answers how many adventures were played. When only an estimate survives, carry the approximation through to the summary.

The full index could also show the title, DR start and end, participants, and evidence. The account link should open a finished session note or the relevant arc heading, then a prepared recap if available, then the corresponding index entry for a history recorded there. A source manifest can still be cited as evidence. Obsidian’s author view can link to private sources. A published view must select only material available to its audience before building rows, counts, or links.

## Pilot and migration

1. **Read the existing records first.** Implement a shared roster merge in `taelgarverse-core` and use the campaign registry to resolve both the index and its party. The vault’s `_scripts/view/pc_index.js` is a reference for affiliation handling. Compare derived rows to the November register tables and identify the exact overrides needed to reproduce reviewed decisions.
2. **Render the roster in an Obsidian test vault.** Register the native block and test Reading View, Live Preview, and a secondary campaign page. Use [[Addermarch Index]] for a roster derived entirely from PC notes, Great Library for partial overrides, and Plaguelands for a self-contained roster. Editing one PC or one index entry should refresh both displays.
3. **Add the shared session and attendance reader.** Reuse Core’s `src/session-bundles.mjs` and `src/vault-session-bundles.mjs`. Exercise both directions of navigation, the display filters, and the cases below. Check that unknown dates and attendance remain distinguishable from known empty values.
4. **Compare all 22 campaigns before replacing imported tables.** Account for each reviewed roster entry, session, qualification, source citation, and open question. Keep the research prose and stable source anchors when moving individual facts into blocks. Verify the published rendering before replacing a table used by a campaign homepage. [[Dragonets Campaign]] is a useful first example because it already has both a player table and a session list.

| Case | Pilot acceptance check |
| --- | --- |
| [[Dragonets Index]] | Heska has three documented sessions. Sessions 1 and 2 open their finished notes. Session 3 opens the bundle recap. The campaign page reads the same index roster. |
| [[Great Library Index]] | Session 0 counts as an adventure. Session 37 counts once with two inferred sittings. Session 68 opens the heading in Arc 6. |
| [[Dunmari Frontier Index]] | The latest ordinary session number is 139. Including two solo adventures gives 141 played adventures. The 31.1 correspondence window and the organizing meetings remain accessible separately. |
| [[Cleenseau Index]] | The reviewed snapshot shows 38 played sessions and four dated inter-session entries. The history can show both kinds and count them separately. |
| [[Plaguelands Index]] and [[Great War Index]] | Preserve 24 reconstructed Plaguelands sessions with their date qualifications. Show roughly 110 Great War sessions and seasonal endpoints without generating individual rows from the estimate. |
| [[Green Sea Index]] | Five proposed players can appear as a draft roster. A planned campaign produces no played-session count from those names. |

## Decisions for the pilot

- **Roster roles.** Which affiliations justify a default player role, and when should the display leave it unspecified?
- **Historical entry format.** Try editing a multi-sitting session, a date window, and an unnumbered meeting by hand. Choose readable YAML for dates, uncertainty, source anchors, and event identity before converting the long histories.
- **Default displays.** Check whether an expandable documented-session count works for Dunmar’s long roster. Choose which entry kinds appear by default in the full history and the compact campaign-page view.
- **Publication.** Decide which pages need website support in the first release and which fields those pages should expose. Obsidian is the proposed first implementation target.

# `taelgar-roster`

Use `taelgar-roster` to show a campaign’s players, characters, and documented session appearances in Obsidian or on the Taelgarverse website. The roster starts with PC notes affiliated with the registered index’s `partyPage`. It uses each PC’s `player` field and includes past affiliations.

## Define a roster and reuse it

Put at most one roster fence on the campaign’s registered index. An empty fence there uses the index’s campaign and derives the roster from vault data.

````markdown
```taelgar-roster
```
````

On another note, give the lowercase ID from the [[_MoC/Campaign Registry|Campaign Registry]]. Display options apply to that copy. The following example lists the member characters of core Addermarch players.

````markdown
```taelgar-roster
campaign: adma
playerRole: core
characterKind: member
columns: [character]
```
````

## Display options

| Option | Behavior |
| --- | --- |
| `campaign` | Lowercase registered ID. Required off the registered index. On a registered index, omit it or use that index’s own ID. |
| `playerRole` | A value or list drawn from `core` and `other`. Omit to include players whose role is unspecified as well. |
| `characterKind` | A value or list drawn from `member`, `guest`, `companion`, and `associated`. This filters characters independently of the player’s role. |
| `columns` | Choose `player`, `role`, `character`, `attendance`, or `note` in the order you want. Omit for the default grouped layout. A character-only view shows a single name or a list. Other explicit column selections use a table. |
| `characterPresence` | Defaults to `false`, so session links record who played the character. Set `true` to include documented cast presence in the same list, with labels when play and presence differ. Each session appears once per character. |

The default layout groups players by role when roles differ. It lists session links beside the character played, gives companions a separate expandable section, and lists one-off roles and substitutions under **Other appearances**. Use `characterPresence: true` with the default layout or include `attendance` (the **Documented play** column) when choosing a table.

````markdown
```taelgar-roster
campaign: dufr
columns: [player, character, attendance]
characterPresence: true
```
````

## Override roster data on the registered index

A player with a member character defaults to `core`. A player with a guest and only guest or companion characters defaults to `other`. Other combinations can leave the player’s role unspecified. The index’s `overrides` list can set the player’s role and the character’s kind independently.

| Override field | Behavior |
| --- | --- |
| `player` | Names the player. Use by itself to add a player without a recorded character or to update a player’s details. With `character`, it sets the player for that character in this campaign. |
| `character` | A quoted wikilink resolves to a PC note and can inherit its usual player. A plain name adds a character without requiring a note. Each entry needs `player` or `character`. |
| `role` | Sets the player’s role to `core` or `other`. Use `null` to leave it unspecified. |
| `kind`, `description` | Set the character’s kind or add a short description. Both require `character`. |
| `note`, `draft` | Add a note to the player’s row or mark the row as draft with `draft: true`. |

This excerpt from [[Great Library Index#Roster|Great Library’s roster]] changes one player’s role, adds a guest, and records a companion. Add the entries under the existing `overrides` list when the index already has a roster fence.

````markdown
```taelgar-roster
overrides:
  - player: Abigail Raiche
    role: other
  - character: "[[People/PCs/Other PCs/Oskar's Companions/Oskar.md]]"
    kind: guest
  - character: "[[People/PCs/Other PCs/Oskar's Companions/Stoneclaw.md]]"
    kind: companion
```
````

Record substitutions and attendance for a specific session in [[taelgar-session]]. The roster uses the same session record for its appearance links.

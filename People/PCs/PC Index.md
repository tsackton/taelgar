---
lintedAt: "2026-10-18T23:43:15-04:00"
lintVersion: "3.5"
tags: [meta]
excludePublish: ["all"]
name: PC Index
dm_owner: none
dm_notes: none
POV: undated
---
# PC Index

Characters grouped by player, with separate tables for **PCs** (regular and guest characters), **Companions**, and any roles still to classify. **Control** records who develops the character.

[[#PC review]] · [[#Companion review]] · [[#Roles to classify]] · [[PCs|Adventuring parties]]

> [!info]- How roles and links work
> Roles come only from adventuring-party affiliation metadata: `title: Guest` or `title: Companion`; `title: Regular`, `title: Member`, or no title means **Regular**. Other titles or missing party affiliations go under **Role to classify**. **Regular** includes former members and does not mean currently active. Party links require a recorded affiliation; campaign links can fall back to the note's collection. Role and control are independent.

## Abigail Raiche

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Abigail Raiche"});
```

## Bryn

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Bryn"});
```

## Chris Kelly

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Chris Kelly"});
```

## Dan Walters

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Dan Walters"});
```

## David Kong

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "David Kong"});
```

## David Schwartz

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "David Schwartz"});
```

## Duncan

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Duncan"});
```

## Dylan

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Dylan"});
```

## Eric Rosenbaum

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Eric Rosenbaum"});
```

## Gabe Raiche

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Gabe Raiche"});
```

## Isaac Sackton

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Isaac Sackton"});
```

## John Leeker

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "John Leeker"});
```

## Kate Sackton

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Kate Sackton"});
```

## Kiya Nicoll

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Kiya Nicoll"});
```

## Matt Rand

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Matt Rand"});
```

## Mi'sol

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Mi'sol"});
```

## Mike Sackton

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Mike Sackton"});
```

## Nathaniel Sackton

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Nathaniel Sackton"});
```

## Owen Bantham-Livermore

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Owen Bantham-Livermore"});
```

## Phil Grayson

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Phil Grayson"});
```

## Sara Smith

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Sara Smith"});
```

## Sasha Rosan

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Sasha Rosan"});
```

## Tim Sackton

```dataviewjs
await dv.view("_scripts/view/pc_index", {"player": "Tim Sackton"});
```

```dataviewjs
await dv.view("_scripts/view/pc_index", {"mode": "newPlayers"});
```

## PC review

Regular and guest PCs: check missing player names, campaign links, and ownership. Named DM owners, `joint`, and `none` are valid. Characters whose role is unclear appear under [[#Roles to classify]].

```dataviewjs
await dv.view("_scripts/view/pc_index", {"mode": "review", "category": "pcs"});
```

## Companion review

Companions have their own cleanup view. A missing player is informational here; pets, familiars, and summoned allies may intentionally have no player. Campaign links and ownership are checked separately from PCs.

```dataviewjs
await dv.view("_scripts/view/pc_index", {"mode": "review", "category": "companions"});
```

## Roles to classify

Missing party affiliations or ambiguous titles prevent these characters from being classified as PCs or companions. This view includes historical affiliations; a character can have a different role in another party.

```dataviewjs
await dv.view("_scripts/view/pc_index", {"mode": "roles"});
```

%%^povNotes:v1%%
Temporal coverage: an undated administrative index spanning campaigns; its role and control definitions supply no in-world modern, decade, or year reading position.
%%^End%%

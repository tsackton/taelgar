---
tags: [meta, status/check/ai]
---
# Temporal POV Metadata

> [!info] Adopted specification
> This note defines the temporal point-of-view metadata used by the Taelgar note linter. See [[Taelgar Note Linter]] for the complete review workflow.

## Purpose

Many Taelgar notes describe their subjects from an implicit point in the setting's history. A person may be described as young, a realm under a particular government, or a place before a campaign changes it. The prose does not always depend on an exact date, but it may stop making sense when moved far enough in time.

`POV` records the useful temporal viewpoint of the visible article:

```yaml
POV: 1750
```

This is the article's best single temporal reading position: the date or era from which its undated prose reads most coherently. It is an editorial anchor, not a validity interval, a summary of every dated fact, or a claim that the article has continuous coverage around that point. The field belongs at the very end of frontmatter, immediately after `dm_notes` when that field is present.

## Values

Use one scalar value whose precision communicates how closely the article's undated speaking position is tied to a point in time. Ordinary authored values are `modern`, a decade, a year, or `undated`.

### Modern

```yaml
POV: modern
```

`modern` means that no finer temporal anchor is useful within the current campaign era, broadly the DR 1700s. It is the ordinary value for material that works across modern play or whose finer placement does not matter. It deliberately replaces the former broad distinctions among `timeless`, `post-Great-War`, and `1700s`; any meaningful earlier or later limitation belongs in `povNotes`.

`modern` does not assert that every sentence is accurate throughout the entire era. A modern article may still have approximate, one-sided, event-bounded, or discontinuous coverage recorded in `povNotes`.

### Decade

```yaml
POV: 1740s
```

A decade captures a campaign era or rough life stage when the exact year does not matter. Typical campaign-era values include `1710s` for Addermarch, `1720s` for Cleenseau, and `1740s` for Dunmari Frontier material.

Use a decade when the rough era itself matters to the undated article, not merely because the article happens to mention an event in that decade.

### Year

```yaml
POV: 1750
```

A year means the undated article is a relatively narrow snapshot: a person's age or life stage, a current office or whereabouts, a campaign encounter, or a world state close to that year matters to how it reads. The year remains approximate unless the article or `povNotes` establishes a narrower boundary.

For example, `POV: 1750` can support describing [[Thomas Hawke]] as being in his early or mid-thirties. It would not support the same description in DR 1720 or DR 1770.

### Undated

```yaml
POV: undated
```

`undated` means that the note and its sources do not support a temporal reading position. It records an epistemic limitation: it does not mean that the subject is timeless, that the article is true at every date, or that its contents are stable. It also does not resolve incompatible undated states; those remain a temporal defect.

Use `undated` only after testing and rejecting `modern`, a decade, and a year under the decision sequence below. If later evidence establishes a reading position, replace `undated` during the next complete lint.

Century values, named eras, and `timeless` are legacy choices under linter 2.8. On re-lint, reconsider rather than mechanically replacing them: use `modern` when no finer current-era anchor matters, a decade or year when the article actually assumes one, or `undated` only when no temporal anchor is supported. No `POV` means no temporal classification has been recorded. A completed write-mode lint records a `POV` value.

## Choosing a value

Choose `POV` from the undated visible article frame. Ask: **if the reader had to stand at one date or era for the present-tense descriptions, ages, offices, relationships, political conditions, or physical state to read naturally, where would that be?** Test these values in order:

1. Use `modern` if the current DR 1700s campaign era is precise enough for the undated prose.
2. Otherwise, use a decade if a rough campaign era, city state, or life stage is precise enough but the current era as a whole is not.
3. Otherwise, use a year if a specific age, office, whereabouts, encounter, or changing world state supplies a narrower supported snapshot.
4. Use `undated` only if none of those reading positions is supported by the note or its sources.

Use the least precise value that still communicates the article's reading position. Do not choose `POV` from the oldest and newest dates mentioned, treat it as the midpoint of an accuracy range, or widen it merely because the article contains historical background. Likewise, one dated event does not narrow an otherwise broad article. `povNotes` carries the shape of temporal coverage, including any gaps or qualifications.

### Isolate narrower dated state

Choose the article POV after separating passages whose truth or visibility begins at a known date. A single dated event or later state should not force the entire note to use that year when the rest of the article has a broader speaking position.

Use `Date:X` around the smallest passage that should appear only on or after `X`. Keep durable identity, description, and history outside the block. The resulting `POV` describes that durable article frame, while the date block supplies the narrower layer.

For example, a character description with a generic 1740s speaking position can use `POV: 1740s` even if a final sentence about a DR 1747 encounter is wrapped in `%%^Date:1747%%`. A broadly modern power can use `POV: modern`, with a `%%^Date:1748-10-15%%` passage recording its later release. Use paired before/after blocks only when both states need to be stated explicitly.

## `povNotes`

`POV` is deliberately coarse. The persistent `povNotes:v1` block records the note-specific temporal coverage as plain text:

```markdown
%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of the subject in the same broad life stage; earlier and later life are not described.
%%^End%%
```

`povNotes` begins with `Temporal coverage:` and briefly explains how the article can be used away from its POV. It should record, when relevant:

- an approximate continuous range when the evidence supports one;
- events or developments that bound the article before or after;
- one-sided uncertainty when an exact boundary is not established;
- a narrow encounter, age, or life-stage snapshot;
- discontinuous coverage, such as childhood followed by current-day material with intervening decades omitted; and
- which periods are unknown rather than contradicted, or which later developments leave an intentionally historical snapshot valid as history.
- when `POV` is `undated`, that the available evidence does not support `modern`, a decade, or a year.

This is editorial guidance, not a second machine-readable date system. Do not invent an exact date merely to make a clean interval, infer continuity between separated facts, or treat the oldest and newest facts as complete coverage. Keep `povNotes` concise—normally one sentence and at most two when discontinuity or uncertainty needs explanation. Do not restate lifecycle dates, dated metadata, or every `Date:*` block unless they materially affect how the article should be read.

### Broad modern state with event bounds

Some modern states have approximate event-defined bounds even when no narrower single POV is useful:

```yaml
POV: modern
```

```markdown
%%^povNotes:v1%%
Temporal coverage: approximately DR 1715–1749, after the Riftstone Gorge Disaster and before the Dunmar Fellowship expedition.
%%^End%%
```

A Chardon neighborhood whose state is tied to a broader urban phase can use:

```yaml
POV: modern
```

```markdown
%%^povNotes:v1%%
Temporal coverage: approximately the late 1600s through early DR 1749; describes post-chalyte, pre-Dunmar Fellowship Chardon.
%%^End%%
```

### One-sided uncertainty

Do not invent a boundary when the article establishes only that earlier or later use needs care:

```yaml
POV: 1740s
```

```markdown
%%^povNotes:v1%%
Temporal coverage: the complete 17-ward layout is established for the 1740s. At earlier dates, some newer wards or outer subdivisions may not yet exist, but their settlement dates are not established.
%%^End%%
```

### Narrow and discontinuous people

A narrow character portrait uses the year of the visible life stage, even when a dated paragraph records an event within that portrait:

```yaml
POV: 1748
```

```markdown
%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Jumi as a very young child; earlier and later life are not described.
%%^End%%
```

When an article includes separated periods, describe the discontinuity instead of presenting a continuous range:

```yaml
POV: 1748
```

```markdown
%%^povNotes:v1%%
Temporal coverage: a DR 1748 present-day portrait with selected childhood and early-adult backstory; the intervening years are not comprehensively described.
%%^End%%
```

### Historical snapshots and records

An intentionally historical place description remains accurate as a historical snapshot even when later events change the place. A session note, Primary Source, or retrospective event account may describe older events from its own recorded or later speaking position. Choose `POV` from that speaking position, use `DR` and `DR_end` for the event chronology where applicable, and use `povNotes` to distinguish the record's temporal layers rather than forcing them into one continuous accuracy range.

### Unsupported temporal position

When neither the note nor its sources supports a reading position, record the limitation rather than defaulting to the current campaign era:

```yaml
POV: undated
```

```markdown
%%^povNotes:v1%%
Temporal coverage: undated; the available evidence does not support a modern, decade, or year reading position.
%%^End%%
```

## Relationship to other metadata

`POV` describes the viewpoint of the visible article. It remains separate from:

- `born`, `created`, `died`, and `destroyed`, which describe the subject's lifecycle;
- `DR` and `DR_end`, which date an event or session;
- `Date:*` blocks, which control individual passages;
- `pageTargetDate`, which controls date-sensitive queries and headers;
- campaign metadata, which records campaign identity, knowledge, or interactions;
- `lintedAt` and Git history, which record real-world review and editing history.

`POV` does not automatically set `pageTargetDate`.

## Linter behavior and legacy forms

The linter validates that `POV` is a nonempty scalar and that a completed lint records one. It also requires exactly one nonempty `%%^povNotes:v1%%` plain-text block. The contextual pass tests `modern`, a decade, and a year in that order before permitting `undated`, and judges whether `povNotes` honestly and concisely describes the article's coverage.

The contextual pass selects `POV` from the undated visible frame, then separately classifies coverage as broad, approximately bounded, narrow, one-sided uncertain, or discontinuous. It never infers continuity between separated facts or exact boundaries from uncertainty. It also checks whether a narrow dated passage has unnecessarily narrowed the whole-note POV. When a supported date block can isolate that passage without changing its meaning, the linter should propose or apply the copy-ready block and retain the broader article POV.

The searchable frontmatter field replaces two older note-level representations:

- inline `(POV:: ...)` annotations; and
- the legacy `Metadata:article` block, including its free-text `pov` key.

On every full re-lint, independently reassess both `POV` and `povNotes` against the current note and applicable evidence. Preserve the meaning of legacy temporal material, but treat the legacy article block's `povNotes` text as evidence rather than accepted final output: retain it unchanged only when the contextual review confirms that it remains accurate; otherwise rewrite it. Move the scalar viewpoint to `POV` and the explanation or qualification to the plain-text `povNotes:v1` block, discard `mode`, `profile`, and other obsolete keys, reconsider legacy broad values under the 2.8 vocabulary rather than blindly replacing them, and migrate useful existing `Accuracy range:` text into concise `Temporal coverage:` wording. Do not retain duplicate temporal labels after migration.

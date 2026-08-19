# Temporal POV Metadata

> [!info] Adopted specification
> This note defines the temporal point-of-view metadata used by the Taelgar note linter. See [[Taelgar Note Linter]] for the complete review workflow.

## Purpose

Many Taelgar notes describe their subjects from an implicit point in the setting's history. A person may be described as young, a realm under a particular government, or a place before a campaign changes it. The prose does not always depend on an exact date, but it may stop making sense when moved far enough in time.

`POV` records the useful temporal viewpoint of the visible article:

```yaml
POV: 1750
```

This is an editorial anchor, not a strict validity interval. The field belongs at the very end of frontmatter, immediately after `dm_notes` when that field is present.

## Values

Use one scalar value whose precision communicates how closely the article is tied to a point in time.

### Year

```yaml
POV: 1750
```

A year means roughly around that year. A difference of a few years is normally harmless unless the article makes an exact claim. An approximate five-year range is a useful intuition, not a deterministic rule.

For example, `POV: 1750` can support describing [[Thomas Hawke]] as being in his early or mid-thirties. It would not support the same description in DR 1720 or DR 1770.

### Decade

```yaml
POV: 1740s
```

A decade captures a campaign era or rough life stage when the exact year does not matter. Typical campaign-era values include `1710s` for Addermarch, `1720s` for Cleenseau, and `1740s` for Dunmari Frontier material.

Use a narrower year or dated passages if a change inside the decade materially changes the article.

### Century

```yaml
POV: 1700s
```

A century means the article remains serviceable across a broad historical span. This is expected to be uncommon. `1700s` is technically ambiguous with the first decade of the century; that ambiguity is acceptable. Use `povNotes` or a representative year when the distinction matters.

### Named era

```yaml
POV: post-Great-War
```

A named era means a major world-state boundary matters more than a campaign date. Clear values such as `post-Riving`, `post-Downfall`, `post-Fall-of-Drankor`, and `post-Great-War` may be used without a formal registry. `povNotes` should explain any ambiguity.

### Timeless

```yaml
POV: timeless
```

`timeless` means the note was reviewed and its purpose and ordinary claims are not meaningfully anchored to in-world chronology. It often fits meta, structural, or rules-oriented notes. It does not mean the subject is metaphysically eternal or that the note can never need revision.

No `POV` means no temporal classification has been recorded. `POV: timeless` means the question was considered and the note was deliberately classified as temporally insensitive. A completed write-mode lint therefore records a `POV` value.

## Choosing a value

Use the broadest description that remains honest about the visible article.

- Use a year when age, office, whereabouts, a recent event, or a changing world state places the prose near a particular time.
- Use a decade when rough campaign era or life stage matters but an individual year does not.
- Use a century only when the article genuinely remains useful across most of it.
- Use a named era when a major historical boundary is the important distinction.
- Use `timeless` only after deciding that in-world chronology is not material.

More precision is not automatically better. A broad value must not conceal an article that silently mixes incompatible viewpoints; use dated passages or revise the article when the distinction matters.

## `povNotes`

`POV` is deliberately coarse. The persistent `Metadata:article:v1` block records the note-specific explanation:

```yaml
%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: approximately DR 1748–1752. The exact year is not material, but the description assumes the subject is in the same broad life stage."
%%^End%%
```

`povNotes` should explain, when relevant:

- why the selected POV fits the article;
- the practical range of dates over which the article can be used;
- whether coverage becomes partial or uneven away from the main POV;
- which periods are unknown rather than contradicted; and
- which later developments do not invalidate an intentionally earlier snapshot.

The accuracy range is editorial guidance, not a second machine-readable date system. It may be approximate, asymmetric, or qualified in prose. When stating a range is useful, begin with `Accuracy range:` so it is easy to recognize and search.

### Minimal snapshots

Use `Accuracy range: minimal` when a note records only a momentary encounter or similarly narrow snapshot and the vault does not establish the subject before or after it. “Minimal” describes the evidence's temporal reach, not the note's quality or importance.

```yaml
POV: 1748
```

```yaml
%%^Metadata:article:v1%%
mode: encounter snapshot
povNotes: "Accuracy range: minimal. This is a snapshot of Alton Greenleaf at the DR 1748-07-18 encounter and his immediate eastward journey. Nothing is established about his earlier or later life."
%%^End%%
```

### Uneven coverage

Some notes cover a longer period but not uniformly. Describe that shape rather than pretending the article has one clean validity interval.

```yaml
POV: 1740s
```

```yaml
%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: uneven across the mid-1730s through DR 1749. The main portrait describes Fausto before his death in the late 1740s. A DR 1738 use must account for his age and the partial record of his adventuring and return to Chardon, while excluding later deeds and relationships. His childhood and origins are explicitly unknown, not available for extrapolation."
%%^End%%
```

### Historical snapshots and retrospective accounts

An intentionally historical place description remains accurate even when later events change the place:

```yaml
POV: 1748
```

```yaml
%%^Metadata:article:v1%%
mode: campaign reference
povNotes: "Accuracy range: DR 1747–1748. This describes Tempest Towers during the Silver Tempests' active use of it as a Voltara base. Later DR 1752 evidence suggests that access or control changed during the time skip, but does not make this deliberately historical snapshot incorrect."
%%^End%%
```

An event note may date earlier events while speaking from later knowledge:

```yaml
POV: 1750
```

```yaml
%%^Metadata:article:v1%%
mode: retrospective event synthesis
povNotes: "Accuracy range: DR 1750 and later, after Fausto's role and Apollyon's defeat had become known. The chronology covers DR 1743–1749, but its causal interpretation is intentionally retrospective and should not be exposed to an earlier viewpoint."
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

The linter validates that `POV` is a nonempty scalar and that a completed lint records one. The contextual pass judges whether its precision and `povNotes` are honest for the article.

The searchable frontmatter field replaces two older note-level representations:

- inline `(POV:: ...)` annotations; and
- the free-text `pov` key formerly used inside `Metadata:article:v1`.

On re-lint, preserve their meaning by moving the scalar viewpoint to `POV` and the explanation or qualification to `povNotes`. Do not retain duplicate temporal labels after migration.

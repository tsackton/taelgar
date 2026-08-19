---
tags: [meta, status/check/ai]
name: Temporal POV Metadata Proposal
---
# Temporal POV Metadata Proposal

> [!warning] Proposal
> This note proposes a model for article point-of-view metadata. It does not adopt a new frontmatter field, migrate existing `(POV:: ...)` annotations, change article metadata, or alter the Taelgar note linter.

## Purpose

Many Taelgar notes describe their subjects from an implicit point in the setting's history. A person may be described as young, a realm under a particular government, or a place before a campaign changes it. The prose does not always depend on an exact date, but it may stop making sense when moved far enough in time.

Proposed `POV` metadata records the useful temporal viewpoint of the visible article:

```yaml
POV: 1750
```

This is an editorial anchor, not a strict validity interval.

## Proposed values

Use one optional scalar frontmatter field. Its degree of precision communicates how closely the article is tied to a point in time.

### Year

```yaml
POV: 1750
```

A year means “roughly around this year.” A difference of a few years is normally harmless unless the article makes an exact claim.

For example, a DR 1750 POV for [[Thomas Hawke]] can support an ordinary description of him as being in his early or mid-thirties. The linter should not worry about a year or two of imprecision. The same description would not make sense in DR 1720, when he was a child, or DR 1770, when he would be in his fifties.

An approximate five-year range is a useful intuition, not a deterministic rule.

### Decade

```yaml
POV: 1740s
```

A decade captures a campaign era or rough life stage when the exact year does not matter. Likely examples include:

- Addermarch-era material: `POV: 1710s`;
- Cleenseau-era material: `POV: 1720s`;
- Dunmari-era material: `POV: 1740s`.

This suits descriptions such as “a young adult,” a long-held occupation, or a broad political situation. If the article depends on a change within the decade, it should use a year or explicit dated passages instead.

### Century

```yaml
POV: 1700s
```

A century means that the article remains serviceable across a very broad historical span. This will probably be uncommon. It may fit stable cultural, geographic, institutional, or historical-reference material.

`1700s` is technically ambiguous between the century and its first decade. That ambiguity is acceptable. In ordinary use it should mean the century; if the first decade matters, use a representative year or explain the intent in `povNotes`.

### Named era

```yaml
POV: post-Great-War
```

A named era means that a major world-state boundary matters more than a campaign-era date. Plausible values include:

- `post-Riving`;
- `post-Downfall`;
- `post-Fall-of-Drankor`;
- `post-Great-War`.

These do not need a formal era registry at the proposal stage. The value should use a clear, stable name that can be connected to [[Riving|the Riving]], [[The Downfall]], the [[Fall of Drankor]], the [[Great War]], or another well-established boundary. `povNotes` can explain any ambiguity.

A named era is initially an editorial description, not an instruction to a future website to hide or transform the article.

### Timeless

```yaml
POV: timeless
```

`timeless` means that the note was reviewed and its purpose and ordinary claims are not meaningfully anchored to in-world chronology. It will often fit meta, structural, or rules-oriented notes.

It does not mean that the subject is metaphysically eternal or that the note can never need revision.

The distinction from an absent field is useful:

- no `POV` means no temporal classification has been recorded;
- `POV: timeless` means the note was considered and deliberately classified as temporally insensitive.

## Choosing a value

Use the broadest description that remains honest about the article.

- Use a year when age, office, whereabouts, a recent event, or a changing world state places the prose near a particular time.
- Use a decade when rough campaign era or life stage matters but an individual year does not.
- Use a century only when the article genuinely remains useful across most of it.
- Use a named era when a major historical boundary is the important distinction.
- Use `timeless` only after deciding that in-world chronology is not material.

More precision is not automatically better. Conversely, a broad value should not be used to conceal an article that silently mixes incompatible viewpoints. Such a note needs dated passages or editorial revision.

## `povNotes`

`POV` is deliberately coarse. `povNotes` supplies the note-specific explanation needed to use it responsibly.

It should explain, when relevant:

- why the selected POV fits the article;
- the practical range of dates over which the article can be used;
- whether coverage becomes partial or uneven away from the main POV;
- which periods are simply unknown rather than contradicted;
- which later developments do not invalidate an intentionally earlier snapshot.

The accuracy range is editorial guidance, not a second machine-readable date system. It can be approximate, asymmetric, or qualified in prose. When stating it is useful, `povNotes` should begin with `Accuracy range:` so that the information is easy to recognize and search.

### Minimal snapshots

Use `Accuracy range: minimal` when the note records only a momentary encounter or similarly narrow snapshot and the vault does not establish the subject before or after it. “Minimal” describes the evidence's temporal reach, not the note's quality or importance.

For example:

```yaml
POV: 1748
```

```yaml
%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: minimal. This is a snapshot of Alton Greenleaf at the DR 1748-07-18 encounter and his immediate eastward journey. Nothing is established about his earlier or later life."
%%^End%%
```

This allows [[Alton Greenleaf]] to remain a useful, accurate encounter note without implying that his age, whereabouts, occupation, or later history have been invented.

### Uneven coverage

Some notes cover a longer period, but not uniformly. `povNotes` should describe that shape rather than pretending the article has one clean validity interval.

For example:

```yaml
POV: 1740s
```

```yaml
%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: uneven across the mid-1730s through DR 1749. The main portrait describes Fausto in the late 1740s. A DR 1738 use must account for his age and the partial record of his adventuring and return to Chardon, while excluding later deeds and relationships. His childhood and origins are explicitly unknown, not available for extrapolation."
%%^End%%
```

For [[Fausto]], this distinguishes three things that a single date cannot:

- the late-1740s period that supports the article's main present-tense portrait;
- the partially established facts that matter to a game set around DR 1738;
- his childhood and origins, which remain deliberately unknown rather than inaccurate or missing from an otherwise established account.

Other notes can use ordinary ranges such as `Accuracy range: approximately DR 1745–1752` when that is genuinely adequate. No controlled list beyond the recognizable `minimal` marker is proposed.

## Relationship to other metadata

`POV` describes the viewpoint of the article text. It remains separate from:

- `born`, `created`, `died`, and `destroyed`, which describe the subject's lifecycle;
- `DR` and `DR_end`, which date an event or session;
- `Date:*` blocks, which control individual passages;
- `pageTargetDate`, which controls date-sensitive queries and headers;
- campaign metadata, which records campaign identity, knowledge, or interactions;
- `lintedAt` and Git history, which record real-world review and editing history.

In particular, `POV` should not automatically set `pageTargetDate`.

## Relationship to article metadata

If `POV` is adopted in frontmatter, it should be the searchable temporal value. The article block would retain the explanation without repeating it:

```yaml
POV: 1748
```

```yaml
%%^Metadata:article:v1%%
mode: historical campaign reference
povNotes: "Accuracy range: DR 1747–1748. The visible article describes the Silver Tempests' manor before the Great Library time skip. Later DR 1752 evidence does not make that historical description incorrect."
%%^End%%
```

The current free-text `pov` key in `Metadata:article:v1` would eventually become unnecessary. `povNotes` would remain because it records the useful range, qualifications, and gaps that cannot be expressed by the scalar frontmatter value. Existing article blocks and inline POV annotations should not change unless this proposal is adopted.

## Possible future lint behavior

If adopted later, the linter could report:

- a missing POV where relative age or present-tense world state makes one useful;
- a clearly incompatible lifecycle or world state;
- a value that is much broader or more precise than the article supports;
- `timeless` on materially time-sensitive prose;
- missing or generic `povNotes` where the practical accuracy range needs explanation;
- newer invention elsewhere in the vault that has overtaken the stated POV;
- disagreement between `POV` and `povNotes`.

Small differences around a year value should remain human judgment, not deterministic errors.

No lint rules are adopted by this proposal.

## Existing inline annotations

Existing `(POV:: year)` annotations remain valid operational metadata unless this proposal is adopted. An eventual migration could copy the year into frontmatter and preserve the surrounding explanation as `povNotes`, but migration is outside this proposal.

## Open questions

1. Is an approximate five-year intuition useful, or should year tolerance remain entirely unstated?
2. Are the proposed named-era spellings clear enough for consistent use without a registry?
3. Does century-level POV have a real use case, or should it remain merely available?
4. Can reviewed in-world reference notes be `timeless`, or should that value be mainly for meta material?
5. Should `POV` remain capitalized to match the existing inline field?
6. Should a future Taelgarverse build treat `POV` only as a label and warning, or eventually use it more actively?
7. Is `Accuracy range: minimal` sufficient as the only standardized marker, leaving all other ranges as prose?

## Proposed decisions, not yet adopted

- Add one optional scalar `POV` frontmatter field.
- Allow a year, decade, century, named era, or `timeless` value.
- Accept some ambiguity in exchange for metadata that is easy to read and write.
- Treat years as approximate editorial anchors rather than exact validity dates.
- Keep campaign identity, dynamic display dates, lifecycle dates, lint time, and Git freshness separate.
- Use frontmatter for the searchable value and `povNotes` for the practical accuracy range, qualifications, and unknown periods.
- Use the lightweight marker `Accuracy range: minimal` for encounter-only snapshots without introducing a broader range taxonomy.
- Preserve existing inline POV annotations until a separate adoption and migration decision.

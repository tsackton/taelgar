# Name Metadata

`Metadata:names:v1` identifies the named in-world subject or work described by a note and records subject-specific facts about its names. It complements the ordinary `name`, `aliases`, and `pronunciation` frontmatter fields: frontmatter holds accepted display values, while the name block records language, meaning, derivation, alternate forms, and unresolved or proposed decisions.

Every note whose subject is a named in-world thing or work uses the block. Apply this rule semantically rather than by tag, folder, or title: notes about people, places, objects, groups, events, powers, creatures, ancestries or cultures, religions, primary-source works, and other named in-world subjects require it. A `background`-tagged note that actually describes a named in-world subject still requires the block.

Do not use the block on a meta or background page that organizes, analyzes, or summarizes information without itself describing an in-world subject. For example, `History of Sembara`, `Timeline of Tollen`, and `West Coast History Framework` do not receive blocks merely because their titles contain in-world names. When a qualifying subject has no established language or other name facts, use a minimal entry with its exact name and `language: unknown`; do not invent etymology. A plain-English or otherwise obvious name may omit pronunciation, but it does not omit the name block.

Evaluate each displayed name form separately. When a work title consists entirely of ordinary modern-English words and no contrary title-language evidence exists, infer `language: Common`; if the title is explicitly a translation, record that role. Do not apply this presumption to non-English, constructed, or transliterated forms: use the established language when unambiguous and otherwise use `language: unknown`. The title-form language does not establish the language of the work's text, and the work's ancestry, origin, or author is not sufficient evidence by itself.

## Linter review gate

[[Taelgar Note Linter]] defines `nameReviewVersion`, an independent minimum version for contextual name review. The linter reviews name-block applicability and searches for or derives pronunciation when a note has no valid `lintedAt`/`lintVersion` pair or its prior `lintVersion` is numerically lower than that threshold. A valid prior version at or above the threshold suppresses that contextual review during later lints. If a human changes the note's primary subject, removing its lint completion version forces a new review.

The gate never suppresses deterministic schema validation of an existing block. Entries with `status: proposed`, `disputed`, or `unresolved` remain deterministic human-review tasks even when contextual review is skipped; preserve them without recalculating or replacing them.

During ordinary lint, an existing entry with `status: documented` remains documented and every populated documented value remains unchanged. The linter may add a supported missing field, such as a pronunciation that was not previously recorded, but it never deletes, replaces, downgrades, or reinterprets an existing documented value. If another note describes a documented value differently, preserve the documented entry and open `metadata.names_documented_conflict` for human resolution rather than choosing between the sources.

The block belongs with other persistent metadata blocks at the end of the note, after article text and comments but before the replaceable lint report.

```yaml
%%^Metadata:names:v1%%
- {name: Istaros, language: unknown, derivedFrom: Aistanë, notes: likely corruption, status: inferred}
- {name: Aistanë, role: historical, language: Elvish, pronunciation: EYE-stah-neh, meaning: blessed water, status: documented}
%%^End%%
```

## Fields

Each entry requires:

- `name`: the exact displayed name form represented by the entry; and
- `language`: the in-world source language of that form, or `unknown` when the evidence does not establish one.

Optional fields are:

- `role`: how the form is used, such as `primary`, `historical`, `translated`, `alias`, `dynastic name`, or `name component`;
- `pronunciation`: an actual human-readable pronunciation of this form;
- `meaning`: an established translation or meaning;
- `derivedFrom`: another name form from which this form derives;
- `notes`: brief subject-specific context that does not fit another field; and
- `status`: epistemic status of the entry: `documented`, `inferred`, `proposed`, `disputed`, or `unresolved`.

The first entry is treated as primary unless another entry explicitly uses `role: primary`. Do not add empty optional fields. Use `language: unknown` rather than guessing. Do not copy reusable real-world language analogues or general phonological rules into every note; those belong in [[Languages]] or another shared language rule.

## Pronunciation workflow

An accepted primary pronunciation belongs in frontmatter so existing headers can display it. When creating a missing entry, a pronunciation matching frontmatter uses `status: documented`; no source note is needed because the note itself is the source. If a name-block entry has a pronunciation and frontmatter either has none or has a different value, identify the block value's source or derivation in `notes`. A proposed pronunciation belongs in the name block with `status: proposed` and records its derivation in `notes`; it remains unresolved until a human accepts it and copies it to frontmatter. Preserve an existing unresolved entry rather than recalculating it. Do not leave the only copy of a proposed pronunciation in a replaceable lint report. Every authored `pronunciation` value must be a pronunciation that a reader can say aloud.

Whenever the linter proposes a pronunciation, the lint report must explain its derivation. The explanation should identify the strongest available basis:

1. an explicit pronunciation in a canonical or human-authored source;
2. an adopted pronunciation or spelling rule for the language;
3. an established cultural naming pattern or real-world analogue documented in [[Languages]]; or
4. a cautious reading of the spelling when no stronger rule exists.

The report must distinguish these bases and state uncertainty. When [[Languages]] supplies a real-world analogue, the linter always uses it to generate an analogue-informed pronunciation: ask how the spelling would naturally be pronounced or adapted in that language, and explain the concrete consonant, digraph, vowel, and stress choices. A real-world analogue alone is not exact in-world phonology, so the result remains `proposed`; that uncertainty must never cause an unexplained fallback to English pronunciation. Use a merely spelling-based reading only when no stronger language rule, naming pattern, or analogue exists. If multiple documented analogues give materially different readings, identify a preferred proposal and explain the alternatives.

Plain-English titles, meta labels, and genuinely obvious ordinary names do not need a pronunciation. Represent that disposition by omitting the `pronunciation` field or entry key, not by writing sentinel values such as `title`, `obvious`, `meta`, or `inherited from <name>`. If a compound or possessive name needs help, record the complete pronounceable form; otherwise omit the key and leave any unresolved component as a lint finding.

## Editing the block

- Keep one dictionary per name form.
- Edit the existing entry when correcting evidence about the same form; do not append a second copy.
- Add an entry when the subject genuinely has another historical, translated, disputed, or alternate form.
- During ordinary lint, preserve `status: documented` and every populated value on that entry; add supported missing fields without rewriting existing ones. A targeted human-authorized correction may resolve a documented conflict outside the automatic lint workflow.
- Preserve established name-specific meaning, derivation, naming agent, and historical circumstance or timing in the appropriate fields or `notes`; a minimal entry omits unsupported or redundant fields but does not discard documented naming context.
- Preserve uncertainty with `status` and `notes`; do not resolve competing etymologies silently.
- Whenever a name-block entry has a pronunciation and frontmatter either has none or has a different value, use `notes` to record the block value's source or derivation. A matching frontmatter pronunciation needs no separate source note.
- When accepting a proposal, update its status, copy an accepted primary pronunciation to frontmatter, and resolve the corresponding lint item.
- Removing the lint report does not remove this block. It is persistent human-curated metadata.

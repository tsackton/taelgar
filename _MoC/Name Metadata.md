# Name Metadata

`Metadata:names:v1` records subject-specific facts about the names used on a note. It complements the ordinary `name`, `aliases`, and `pronunciation` frontmatter fields: frontmatter holds accepted display values, while the name block records language, meaning, derivation, alternate forms, and unresolved or proposed decisions.

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
- `pronunciation`: a human-readable pronunciation of this form;
- `meaning`: an established translation or meaning;
- `derivedFrom`: another name form from which this form derives;
- `notes`: brief subject-specific context that does not fit another field; and
- `status`: epistemic status of the entry: `documented`, `inferred`, `proposed`, `disputed`, or `unresolved`.

The first entry is treated as primary unless another entry explicitly uses `role: primary`. Do not add empty optional fields. Use `language: unknown` rather than guessing. Do not copy reusable real-world language analogues or general phonological rules into every note; those belong in [[Languages]] or another shared language rule.

## Pronunciation workflow

An accepted primary pronunciation belongs in frontmatter so existing headers can display it. A proposed pronunciation may appear in the name block with `status: proposed`, but it remains unresolved until a human accepts it and copies it to frontmatter.

Whenever the linter proposes a pronunciation, the lint report must explain its derivation. The explanation should identify the strongest available basis:

1. an explicit pronunciation in a canonical or human-authored source;
2. an adopted pronunciation or spelling rule for the language;
3. an established cultural naming pattern or real-world analogue documented in [[Languages]]; or
4. a cautious reading of the spelling when no stronger rule exists.

The report must distinguish these bases and state uncertainty. When [[Languages]] supplies a real-world analogue, the linter always uses it to generate an analogue-informed pronunciation: ask how the spelling would naturally be pronounced or adapted in that language, and explain the concrete consonant, digraph, vowel, and stress choices. A real-world analogue alone is not exact in-world phonology, so the result remains `proposed`; that uncertainty must never cause an unexplained fallback to English pronunciation. Use a merely spelling-based reading only when no stronger language rule, naming pattern, or analogue exists. If multiple documented analogues give materially different readings, identify a preferred proposal and explain the alternatives.

The literal values `obvious`, `title`, `meta`, and `inherited from <name>` record reviewed exceptions to a separate pronunciation. They should be used only when the reason is clear from the note and the referenced component has an accepted pronunciation where applicable.

## Editing the block

- Keep one dictionary per name form.
- Edit the existing entry when correcting evidence about the same form; do not append a second copy.
- Add an entry when the subject genuinely has another historical, translated, disputed, or alternate form.
- Preserve uncertainty with `status` and `notes`; do not resolve competing etymologies silently.
- When accepting a proposal, update its status, copy an accepted primary pronunciation to frontmatter, and resolve the corresponding lint item.
- Removing the lint report does not remove this block. It is persistent human-curated metadata.

---
name: prepare-interaction-transcript
description: Make a conservative in-world interaction draft from a session YAML and polished transcript. Preserve meaningful dialogue, lore, events and uncertainty; replace mechanics, routine combat and irrelevant chatter with short labelled snips, including small substitutions within turns. Retain every original UID span and verify all other wording unchanged. Only the new interactions-draft Markdown may be written.
---

# Prepare Interaction Transcript

Use for “make an in-world transcript,” “shrink this polished transcript for
interaction extraction,” or “prepare an interactions draft.” This is an
experimental derivative for later processing, not a replacement transcript,
recap, canonical account, or polished narrative.

## Hard boundary

During a session run, **the only file you may create or modify is
`cleaned/<stem>-interactions-draft.md`** in the selected bundle. All transcripts,
session YAML, beats, notes and existing processing files are read-only. No YAML
registration, logs, JSON plans, lock files, snapshots, temporary files or sidecars.
Use the helper with `python3 -B` to prevent Python cache writes. Read-only tools
and in-memory decisions are fine. Skill maintenance/tests are separate from a
session run; tests use synthetic bundles in temporary directories.

Use the provided helper for draft writes. It shares the transcript pipeline's
directory lock without creating a lock file. It refuses source changes, stale
drafts, symlinks, hard-linked drafts, unmarked edits, missing/duplicated spans and
accidental replacement of an existing draft. Never repair a blocked run by
editing an input or changing its fingerprint.

## Resolve and copy

Follow repository branch/worktree requirements. Resolve a supplied session to a
single existing `cleaned/<stem>-session.yaml`; ask only when selection is ambiguous.
Set `HELPER` to this skill's `scripts/interaction_draft.py` and `YAML` to that path.

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML init
```

`inspect` is read-only. It requires `sourceType: transcript`, known, valid
`realWorldDate`, `drStart`, and `drEnd`, and a locatable
`transcriptProcessing.artifacts.polishedMarkdown.path`. Artifact paths are
bundle-relative, following `process-transcript`. It checks registered hashes and
UID coverage; when the cleaned reference is registered, it also checks against
every cleaned unit. Without that reference it verifies the complete polished
source map, not completeness against earlier audio/ASR.

If dates or paths are absent/invalid, report the exact missing field or proposed
path correction and stop before creating a draft. Do not infer dates or silently
choose a transcript with a similar filename. YAML dates remain metadata context:
do not rewrite speech or manufacture chronology to fit them.

`init` copies all polished content into the new draft, adding an explicit derivative
heading and one comment with **version, session YAML path, and polished-source
hash**. No other processing metadata is stored. An existing draft is never replaced;
use `validate`, inspect its current snips, and resume. Do not treat an unchanged
copy as a completed experiment.

## Read and conservatively select

Read **the entire polished source**, in manageable overlapping portions if needed.
The helper's read-only `show --start N --end N` displays original turn numbers and
UIDs. Turn numbers are selectors tied to this exact source fingerprint; original
UIDs and offsets remain the enduring provenance. Current UIDs are `u0001`-style
identifiers, not newly generated UUIDs. Never renumber them.

Preserve, in original order and wording:

- NPC/PC speech, introductions, memorable lines, whole exchanges and replies needed
  to interpret them; keep speaker labels and meaningful emotional reactions.
- Lore, identities, affiliations, relationships, geography, dates, time skips,
  travel and location changes, clues, plans, decisions and actions—even when
  discussed in third person, as a rules question, or out of character.
- Questions and answers about how the world works; descriptions of meaningful
  creatures, magical properties, artifacts and discoveries; uncertainty, negation,
  corrections, conflicting claims and attribution. “We think Arcus is dead” must
  not become “Arcus died.”
- Distinctive combat developments: named participants, introductions, dialogue,
  surrender, capture, escape, death, significant injuries, transformation,
  discoveries, allegiances, important item changes, and aftermath. Preserve actual
  occurrence versus hypothetical tactics. Do not silently lose these in a summary.

Snip only clearly dispensable material: dice arithmetic, initiative bookkeeping,
turn sequencing, damage/hit-point accounting, repeated movement/range questions,
routine attacks and gear use, technical setup, scheduling, breaks, unrelated jokes.
“In-world” describes the information retained, not the grammatical style. Do not
rewrite retained words into character speech or repair names/ASR. If unsure, keep.

**Small substitutions inside mixed turns are encouraged.** Replace a clearly
mechanical phrase such as “I rolled a 12” with `((rolls))` while preserving the
question, answer, named entities, uncertainty and consequences around it. Work at
the smallest useful boundary; do not keep a long rules preamble merely because
the same turn contains lore. Keep meaningful out-of-character information exactly
as spoken. Do not automatically strip all uses of “roll,” numbers, or rules terms:
an in-character dice game, a date, an injury, or a magical property's limits may
matter. Search can locate candidates; an agent must classify each in context.

Polished turns can cover multiple UIDs or parts of one UID. Keep each turn's
existing UID comment unchanged. There is no additional source map inside a turn:
`((label))` marks a snip, and restoration recovers the entire polished turn.
Do not guess alignment to cleaned text. Keep ambiguous passages and
short replies whose meaning depends on neighbors. Never delete a hedge or a
negation and thereby strengthen the remaining claim.

## Replace selected spans

For a small cut, quote the exact words still present in the draft:

```bash
python3 -B HELPER --session-yaml YAML cut --turn 12 --text 'I rolled a 12.' --label rolls
python3 -B HELPER --session-yaml YAML restore --turn 12
```

The example assumes other meaningful speech remains in turn 12. `cut` preserves
the speaker and all text outside the selection and inserts `((rolls))`. No cut
offsets, removed words, or extra comments are stored. Labels are at most six words,
usually `((rolls))`, `((rules))`, or `((table chatter))`; labels themselves are
generated, not speech. Select punctuation that belongs to the removed phrase,
leave existing spacing outside the cut intact,
and inspect the resulting sentence. Do not rewrite the surviving words to make
them smoother. Prefer one contiguous cut over adjacent tiny cuts when all of
that material is dispensable; do not absorb meaningful connective text to merge.

If the same words occur more than once, pass `--occurrence 2` to select the second
occurrence in remaining speech (excluding generated labels). The helper rejects
cuts into existing labels, word fragments, speakers, uncertainty markers or
wikilinks. `restore --turn N` restores that complete original polished turn,
undoing all its inline snips together. Other turns remain as they are, even if
they share a UID. Do not use partial cuts to hide named combat events; preserve
their dialogue/context under the combat rules below.

Snip contiguous complete original turns with short double-parenthesized labels.
Each replacement retains their exact ordered UID/character spans. Those spans
identify the original turns: no separate snip record or turn range is stored.
The removed words remain in the polished source. Read both neighboring turns first.

```bash
python3 -B HELPER --session-yaml YAML snip --start 12 --end 15 --label 'dice rolls'
python3 -B HELPER --session-yaml YAML snip --start 81 --end 120 --label 'Combat against Grash and his allies.' --name Grash
python3 -B HELPER --session-yaml YAML snip --start 125 --end 150 --label 'combat continues against Grash' --name Grash
python3 -B HELPER --session-yaml YAML restore --turn 12
```

These numbers/names are illustrative. Supply actual selected ranges. All proper
names carrying setting information inside removed combat must survive in its
label or an untouched meaningful turn; use `--name` for names in a label. The
helper checks each supplied name against the source and label during that edit;
it does not save a name list or prove you identified all names. This needs semantic
review. Do not include unrelated player names from table chatter merely because
they are capitalized.

Use **one overview sentence per encounter**, at most 40 words, normally much
shorter. It should identify opponents, named foes and a supported consequential
outcome if that outcome is inside the replaced span. Never add an outcome from
later speech to an earlier snip or imply an uncertain outcome is established.
If useful dialogue or an event interrupts combat mechanics, leave it verbatim and
use short continuation labels (at most 12 words) for the remaining mechanics.
This preserves order and conversation while avoiding repeated summaries. Other
labels are at most 12 words, e.g. `((dice rolls))`, `((rules bookkeeping))`, `((scheduling))`.
An encounter can therefore contain several snips and retained passages but only
one generated overview. The agent checks this during semantic review; no encounter
IDs or overview flags are stored. Do not manufacture NPC/entity records at this stage.

When the selected turn is inside a snip covering several complete turns, `restore`
recovers that snip's entire original range. Snips can be restored independently,
in any order. For many snips, an in-memory Python caller may use the same helper
functions; never save a separate action plan or bypass its guards. Restore existing
inline cuts before replacing their whole turn, or restore a whole-turn snip before
editing inside it. The current experimental format is version 4; do not silently
overwrite drafts in an older format. Double parentheses are reserved for generated
labels; if the original source already contains that syntax, preflight stops and
reports the collision without editing any file.

## Verify and hand off

Perform a distinct second pass against **every removed range and its boundaries**,
including each inline cut and the complete edited turn.
Look especially for lore concealed in mechanics, new names, speech, world actions,
dates, place transitions, item events, and outcomes. Restore questionable ranges.
Check the complete draft for broken conversations and invented causal connections.
Neither smaller size nor complete UID coverage proves semantic preservation.

```bash
python3 -B HELPER --session-yaml YAML validate
```

Validation checks coverage, the polished-source hash, verbatim retained wording
around inline markers, and label syntax/length. It does not certify semantic
review or check one overview per encounter. Report the review performed in the
handoff; do not store review status, notes, timestamps, or a draft-body hash.
Confirm the original inputs remain unchanged and report the draft link,
reading-text reduction, source UID count, and material limitations. Readability
word counts exclude mapping comments; they are not model-token savings.

The YAML remains authoritative and is revalidated on every run. Valid YAML
updates do not invalidate an unchanged polished source. Input fingerprints used
to prevent changes during a write stay in memory; only the polished-source hash
is kept in the draft.

No sidecar state is written. In-place single-file writes avoid extra files but are
not crash-atomic; interrupted drafts fail validation. Report damage and recover
from the unchanged source plus inspected surviving snips; never silently reset
the draft or touch original references.

See [format and downstream integration](references/format.md) for the contract,
examples and suggested interaction-skill integration. Do not modify that skill or
register this experimental draft as the canonical transcript during this run.

## Maintenance verification

Requires Python 3.9+ and PyYAML, as does the existing transcript pipeline. Run
`python3 -B -m unittest discover -s .agents/skills/prepare-interaction-transcript/tests -v`
from the vault root. Synthetic tests cover input/date failures, exact coverage,
split UIDs, Unicode text, multiple cuts/whole-turn restoration, retained dialogue,
names, minimal metadata, source protection and the single-output boundary. A real
sample also needs the semantic passes above.

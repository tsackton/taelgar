---
name: prepare-interaction-transcript
description: Make a conservative interaction draft from a YAML-registered polished transcript. Preserve meaningful speech, lore, events, uncertainty, and every UID span; replace only clearly dispensable mechanics or chatter with labelled snips. Write only the derivative draft.
---

# Prepare Interaction Transcript

Use for “make an in-world transcript” or “shrink this polished transcript for
interaction extraction.” The draft is an optional reading view. Scene mapping
can use it; entity checking reads the polished transcript directly. It does not
replace the source or generate a recap or interactions.

## Inputs and boundary

Follow repository branch/worktree instructions. Resolve one existing
`cleaned/<stem>-session.yaml` and its registered polished transcript. Read
[the format](references/format.md) for metadata and restoration details.

During a session run, write **only `cleaned/<stem>-interactions-draft.md`** using
the helper. All other files are read-only. Do not create YAML registrations,
plans, logs, lock files, snapshots, temporary files, or sidecars. Use `python3 -B`
to prevent cache files. Maintenance tests are separate and use temporary bundles.

Set `HELPER` to this skill's `scripts/interaction_draft.py` and `YAML` to the
session manifest; substitute their actual paths in the commands below.

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML init
```

Preflight requires `sourceType: transcript`, valid `realWorldDate`, `drStart`,
`drEnd`, and a locatable `transcriptProcessing.artifacts.polishedMarkdown.path`.
Artifact paths are bundle-relative. It checks registered hashes and full polished
UID coverage, including agreement with registered cleaned text when available.
Without cleaned text, coverage is relative to the polished map, not earlier ASR.
Report missing/invalid fields and proposed repairs without changing inputs or
choosing a similar filename. YAML dates do not authorize rewriting speech.

`init` copies the polished text and adds a derivative heading and one metadata
comment. Never replace an existing draft: validate it and resume. Older formats,
changed sources, and source text containing reserved `((...))` syntax require
explicit resolution; do not silently migrate or reset them. An unchanged copy
is not a completed reduction.

## Select conservatively

Read the **entire polished transcript**, in overlapping portions if needed:

```bash
python3 -B HELPER --session-yaml YAML show --start 1 --end 100
```

Turn numbers select this exact source version; original UIDs and offsets remain
provenance. Keep their comments unchanged, including turns combining UIDs or
several turns sharing a UID. Never renumber or guess sub-turn source alignment.

Preserve original order and wording for:

- Meaningful NPC/PC speech, memorable lines, introductions, replies, reactions,
  and enough of each exchange to interpret it.
- Lore, identities, relationships, geography, dates, travel, time/location changes,
  clues, plans, decisions, actions, and meaningful creature/item properties.
- Uncertainty, attribution, negation, corrections, and conflicting claims. Keep
  world information even in third-person speech, rules questions, or OOC discussion.
- Distinctive combat events: named participants, dialogue, surrender, capture,
  escape, death, significant injuries, transformation, discoveries, allegiances,
  consequential item changes, and aftermath. Distinguish events from proposed tactics.

Snip only clearly dispensable dice arithmetic, initiative/turn bookkeeping,
routine attacks and gear use, repeated range questions, technical setup,
scheduling, breaks, or unrelated jokes. Nearby technical chatter does not make
an ambiguous line technical: “you're all just very still” might describe the
characters even after a frozen-call complaint. If unsure, keep it.

Small cuts inside mixed turns are encouraged. Remove the mechanical phrase while
keeping the lore, question/answer, names, and consequences exactly as spoken.
Do not automatically remove numbers or rules terms: dates, injuries, an in-world
dice game, and magical limitations can matter. Search locates candidates; the
agent classifies them in context. Never repair ASR or smooth retained wording.

## Cut and restore

Quote exact words still present in the draft:

```bash
python3 -B HELPER --session-yaml YAML cut --turn 12 --text 'I rolled a 12.' --label rolls
python3 -B HELPER --session-yaml YAML restore --turn 12
```

The cut must leave meaningful original speech. It preserves the speaker and
surrounding text, rejects word fragments and overlaps with uncertainty markers
or wikilinks, and inserts a generated label. Select the phrase's punctuation,
preserve spacing outside it, and inspect the result. Prefer one contiguous cut
when all intervening material is dispensable; never absorb meaningful words.
Use `--occurrence 2` for the second occurrence in retained speech, excluding labels.
Restoration recovers the **complete original turn**, undoing all its inline cuts.
A neighboring turn sharing a UID is unchanged.

For complete contiguous turns, read both neighbors before collapsing them:

```bash
python3 -B HELPER --session-yaml YAML snip --start 12 --end 15 --label 'dice rolls'
python3 -B HELPER --session-yaml YAML snip --start 81 --end 120 --label 'Combat against Grash and his allies.' --name Grash
python3 -B HELPER --session-yaml YAML restore --turn 81
```

Numbers and names are illustrative. A whole-turn snip inherits every exact source
span in order; removed words remain in the polished source. Restoring any contained
turn recovers the entire snip. Restore inline cuts before collapsing their whole
turn, and restore a whole-turn snip before editing inside it. Independent snips
can be restored in any order. An in-memory caller may batch helper operations;
do not save an action plan or bypass write guards.

Keep labels short and plain: inline labels at most six words, ordinary and
continuation labels at most 12, and **one combat overview sentence per encounter**
at most 40 words. Preserve useful dialogue/events verbatim between continuation
snips. The overview identifies opponents, setting-relevant proper names, and only
a supported outcome inside its range; do not import a later outcome or strengthen
uncertainty. Names must survive in the label or retained meaningful speech.
`--name` verifies each supplied name against source and label, but cannot prove
all names were noticed. Player names from unrelated chatter need not survive.
No encounter IDs, entity records, name lists, or review flags are stored.

## Verify and hand off

Make a **distinct second pass over every removed range and its boundaries**,
including complete turns with inline cuts. Look for concealed lore, names, speech,
world actions, dates, place transitions, item events, and outcomes. Restore a
questionable cut's complete turn or snip. Check the full draft for broken exchanges,
lost hedges/negation, invented causal connections, and repeated combat overviews.

```bash
python3 -B HELPER --session-yaml YAML validate
```

Validation checks source hashes, exact coverage/partitions, retained wording,
and label syntax. It cannot certify semantic preservation or one overview per
encounter. Confirm unchanged inputs and report the draft link, review performed,
reading-text reduction, UID count, and material limitations. Visible word reduction
excludes mapping comments and is not a model-token measurement.

Valid YAML updates are rechecked without staling an unchanged polished source.
Write guards reject concurrent edits, source changes, symlinks, and hard-linked
drafts. Single-file updates use the shared directory lock but are not crash-atomic.
If interrupted, report damage and recover from unchanged source and inspected
surviving snips; do not silently reset the draft or alter fingerprints.

## Maintenance

Requires Python 3.9+ and PyYAML; the tests use Python 3.10+.
Run from the vault root:
`python3 -B -m unittest discover -s .agents/skills/prepare-interaction-transcript/tests -v`.
A real sample still needs the semantic passes above.

---
name: automatic-transcript-cleanup
description: Resolve marked name and setting-term ASR errors in existing cleaned Taelgar session transcripts, with direct edits, a fixed review log, and selective undo. Use for one session or a bounded campaign batch; not initial transcript cleaning or prose reconstruction.
---

# Automatic Transcript Cleanup

Apply the **names-v1** pass to existing cleaned source transcripts. By default, make clear and well-supported likely name corrections directly and log every occurrence. Leave ambiguous identities, longer damaged phrases, and ordinary wording unchanged. This is a distinct stage after `transcript-cleaner`, not a rerun of its broad cleanup workflow.

Run from the vault root with Python 3.10+; the helper uses only the standard library on macOS/Linux. Set `--vault-root` when running elsewhere.

## Scope and authorization

- An instruction to run this skill on specified transcripts authorizes the described source edits and their logs. A request for a preview stays read-only. Do not interpret a question about the skill as authorization to run it.
- Accept session numbers, a session bundle, cleaned source paths, or one campaign directory and an explicit range/all. Resolve Dunmar/Dunmari Frontier to `_sessions/dunmar-frontier`; author the campaign name as **Dunmari Frontier**. Do not assume there are exactly 140 files or invent missing transcripts.
- Write only the selected cleaned source transcripts and this skill's logs beside them. Do not edit prepared sources, archival `sources/`, YAML configuration, canonical notes, existing cleanup reports, acceptance records, beats, facts, recaps, or polished transcripts. `_sessions` is status-tag exempt.
- Inspect branch and working-tree state before any writes; preserve existing local changes. Follow root branch rules. No automatic commits, staging, branch switches, or baseline commits. Git's existing diff may contain unrelated work and is not the rollback source.

## 1. Mandatory cheap gate

**Before reading transcript text, session configuration, glossary, prior reports, or evidence**, run:

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py scan \
  --transcript '_sessions/dunmar-frontier/dunmari-frontier-048/cleaned/dunmari-frontier-048-source-cleaned.md'
```

`scan` streams a byte search before decoding or parsing anything. If `status` is `skipped_no_markers`, stop that session immediately: do not read its full transcript, search its lore, or create a log. Report the helper's skip result. Unbalanced/nested/multiline markers are a structural blocker, not a zero-marker success. Legitimate `[[wikilinks]]` and `[laughs]` are not uncertainty markers.

For a campaign batch, begin with this cheap manifest instead:

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py batch \
  --campaign-root '_sessions/dunmar-frontier'
```

Restrict its rows to the user's requested scope. Preserve the complete queue across continuation turns. Process sessions in session-directory order; do not take a sample. Record missing, ambiguous, blocked, and skipped sessions explicitly. A blocked session does not stop independent sessions. Do not spawn agents unless the user authorizes delegation.

## 2. Inspect and group

For each marker-positive session:

1. Inspect its existing local diff and read the complete current cleaned transcript once, in bounded chunks if needed. The gate must have run first. Focus decisions on existing `{{...}}` spans; do not correct unmarked errors discovered incidentally.
2. Read its matching session YAML and any explicitly provided glossary. Current dialogue and participant roles establish what kind of referent is intended; reference notes establish spellings. Use prepared text only when useful; never use archived ASR in `sources/` as corrective authority.
3. Group candidate variants **within this session**, checking every occurrence. Repeated strings are separate decisions, even on the same line. Group by contextual referent, not merely phonetic resemblance: Grash and Uzgash must not be merged because both resemble `gash`.
4. Search likely canonical filenames, then names/aliases and variants. Read relevant notes and passages. Broaden only as needed to campaign records, primary sources, Worldbuilding, or DM notes. Do not turn development proposals, uncertain identities, or future revelations into facts that override the speaker's words.
5. Reuse established canonical spellings across a batch, with their source paths. Re-evaluate each ASR occurrence in context: never carry a global `garage -> Grash` substitution map from one session to another. New, plausible names need not be glossary matches.

Inventory IDs are `uNNNN:mN`, where `mN` is the **one-based ordinal of all markers on that original line**. Use IDs from the current scan, not remembered IDs from an earlier run. A changed transcript requires a fresh scan and plan.

## 3. Fixed decisions and constraints

Classify **every marker exactly once** using these actions:

| Action / confidence | Decision |
| --- | --- |
| `replace / high` | The referent, established form, and complete marked replacement are clear from context and evidence. |
| `replace / supported` | One contextual identity/form is strongly favored and supported by a source, but the recognition is less certain. Apply directly and label it for prioritized review. |
| `review / unresolved` | Competing identities, weak evidence, unclear replacement boundaries, possible deliberate wording/misremembering, or a name embedded in an otherwise unrecoverable phrase. Keep it unchanged and explain the specific uncertainty. |
| `leave / not_applicable` | Ordinary chatter, numbers, rules explanations, grammar, source-reading reconstruction, or other wording outside this pass. Keep unchanged; this is not automatically a human-review task. |

The reversible log supports **more evidence-backed replacements**, not guesses without a plausible unique referent. Do not reserve every imperfect phonetic match for a human: a unique role plus strong source support can justify `supported`. Record the reason and the competing readings considered where material. Keep this distinction stable across sessions.

Replace only **complete existing marked spans**, with plain name/term text. Eligible terms include people, places, gods, peoples, organizations, languages, titles, named items/features, and conventional item names such as message stone. Preserve possessives and sentence-initial capitalization where appropriate. An already correct name inside braces can be unmarked.

Never change headers, line count/order, speakers, timestamps, line endings, text outside the selected markers, links, annotations, tags, or unmarked punctuation. Never expand a replacement into adjacent words. Do not invent connective words, actions, numbers, chronology, or mechanics. Do not substitute the factually correct name merely because a speaker appears to have said the wrong one.

Examples of decision boundaries, **not preapproved substitutions**:

- A named skyship in `{{Vidya, Sharna}}` can become `Vindristjarna` when its role and source match.
- `{{Sura}}` can become `Sura` when the identity is clear.
- A likely Kylos Market reference inside `{{Since private pilot's market}}` stays wholly marked because the remaining wording is unclear.
- `{{Marcus}}` followed by another speaker saying `Alban` may be an actual spoken mistake; retain it.
- A written arrival script may establish the river as Chasa, but reconstructing `{{strategy that chaucer}}` as `stretch of the Chasa` belongs to a separate source-matching pass.
- A matching written letter can support a complete **name** replacement such as Rishi; it does not authorize repairing the letter's ordinary wording in this pass.

## 4. Plan, validate, and apply

Read [references/plan-and-audit.md](references/plan-and-audit.md) for the exact JSON schema, log fields, and undo/recovery commands. Author a temporary plan in the system temporary directory. Its fingerprint must come from `scan`; include every marker in a replacement, grouped name-review decision, or outside-scope group. Evidence entries are actual vault-relative source file paths. Avoid copying private source passages into shared reasons/logs; a source path, fingerprint, and non-spoiling name-resolution explanation suffice.

Run the same helper for a deterministic preview or direct application:

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py preview \
  --transcript 'PATH-TO-CLEANED-SOURCE' --plan '/tmp/name-pass-plan.json'

python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py apply \
  --transcript 'PATH-TO-CLEANED-SOURCE' --plan '/tmp/name-pass-plan.json'
```

Choose `apply` for an authorized cleanup invocation; do not pause for approval of each group/session. Choose `preview` when requested. Never bypass the helper by writing the transcript directly. It enforces whole-marker edits, complete accounting, input fingerprints, header preservation, exact line endings, and write-ahead audit creation. It rejects stale plans and structurally invalid edits.

The helper does **not** decide whether a proposed name is supported; that evidence judgment remains the agent's responsibility.

## 5. Verify, resume, and report

- Read each changed line with nearby context. Check the exact task diff against the journal's original lines, not just against Git HEAD. Review `supported` decisions particularly carefully. Correct a bad automatic decision with logged undo; do not erase its audit history.
- Confirm counts, marker balance, unchanged headers/order/line endings, and only whole-marker replacements. Run scoped `git diff --check` on task-touched paths, preserving unrelated/pre-existing findings. A prepared journal or error is not successful completion: run `recover` as documented before continuing that session.
- Use the helper's rendered report verbatim for per-session output and `review.md`; do not redesign headings, confidence labels, columns, or counting units. Source spans, not lines or deduplicated names, are the primary count. Marker-only removals are a subset of applied replacements, not an additional total.
- All marker-positive sessions receive a versioned log, including `reviewed_no_changes`; marker-free sessions receive none. The journal is the source of truth for regenerating display files and undo. Do not overwrite previous runs or rewrite older cleanup assessments to make them appear current.
- A batch row `reviewed_current` means the current transcript and recorded evidence match a completed names-v1 run. Skip it when **resuming the same batch**. A user-requested fresh review/recheck may inspect it again; new or previously unconsulted evidence can change a decision even if old fingerprints match. Marker changes, evidence changes, or a pass-version change require re-evaluation.
- At batch handoff, use `summary --manifest /tmp/name-pass-manifest.json --journals JOURNAL-PATH ...` (or `--campaign-root` instead of `--manifest`) to render the table below. Supply only journals completed during this invocation, one per session. A saved temporary manifest may be narrowed to the user's session range by filtering its `sessions` array before processing. The table lists skipped/missing/blocked sessions explicitly and links changed sessions' `review.md` logs. Do not compose a different table or label all retained markers human-review work. Do not claim zero markers means error-free ASR or that this constitutes audio verification.

| Session | Status | Markers before | High | Supported | Name review | Outside scope | Markers after | Log |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |

Use statuses `applied`, `reviewed_no_changes`, `reviewed_current`, `skipped_no_markers`, `missing_cleaned`, `ambiguous_cleaned`, `blocked`, or `recovery_required`. `ready` means pending work and cannot be reported as a completed batch. For a preview use `preview`. Use `—` for counts not computed, and a final `Total` row summing only supplied completed run journals; resumed rows are excluded from that total. In progress updates report completed/remaining sessions and actionable blockers, not invented completion percentages.

Existing cleanup acceptance and downstream artifacts may be stale after edits. Report that fact once; do not regenerate them or treat retained uncertainty as human-accepted without a separate request. Creating this skill alone never authorizes applying it to live transcripts.

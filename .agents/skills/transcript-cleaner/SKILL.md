---
name: transcript-cleaner
description: Clean prepared RPG session transcripts while preserving line IDs, speakers, timestamps, and order. Collect material ASR uncertainty for one conditional review after cleanup; provide an audio correction page only when requested.
---

# Transcript Cleaner

Run the commands below from the Taelgar vault root, using a Python environment with PyYAML installed.

Use this skill when working from a prepared session bundle:

- `session.yaml`
- `source.prepared.md`
- optional campaign glossary

The goal is to produce a corrected transcript that is still a transcript, not a recap.

## Allowed Inputs

Primary evidence:

- `session.yaml`
- the current `source.prepared.md`
- an optional glossary or dictionary explicitly provided for this cleanup run

Strictly ignore files in the bundle's `sources/` directory when making cleanup decisions.
Those files are archival inputs and may themselves contain transcription errors.
They are not valid evidence for corrections.

Secondary evidence is allowed, but subordinate to the primary evidence above.
This can include:

- prior cleaned transcripts
- prior cleanup reports
- earlier session outputs
- relevant notes elsewhere in the vault

Use secondary evidence only to support or confirm a correction, not to override what the current prepared transcript, `session.yaml`, and glossary/dictionary indicate.

## Rules

- Preserve every transcript header exactly.
  The full bracketed id line prefix must remain byte-for-byte identical, including `uNNNN`, timestamps, speaker/game role, separators, and ordering.
- Keep one input transcript line for one output transcript line.
- Only fix errors.
  Fix spelling, capitalization, punctuation, and minor grammatical errors caused by transcription.
  Do not prettify, summarize, tighten phrasing, smooth tone, or rewrite awkward wording unless it is clearly an ASR or transcription error.
- Safe fixes:
  punctuation, capitalization, spelling, obvious grammar noise from ASR, and clearly wrong fantasy terms when the correction is well-supported.
- Be more aggressive than a literal copy edit.
  If a phrase is semantically wrong, ungrammatical in context, or clearly an ASR near-miss for a protected name or glossary term, fix it directly instead of leaving it untouched.
- Do not anchor on the glossary or prior known errors.
  The glossary is supporting evidence, not the list of the only phrases worth correcting.
  You must actively look for new ASR mistakes, including phrases that are valid English but clearly wrong in context.
- The glossary is a list of canonical terms, not a list of known transcript errors.
  Its purpose is to tell you the correct forms of names and terms that exist in the campaign, not to enumerate all likely mistakes.
  Absence from the glossary can make a fantasy-looking term or name suspicious, but it is not sufficient by itself to force a correction.
  Use local transcript context first, then use the glossary to confirm likely canonical forms.
  Do not assume that every valid correction must map to a glossary entry, because some sessions introduce genuinely new entities.
- Treat participant game roles from `session.yaml` as protected names.
  Be extra careful with PCs and the DM name, especially when ASR drifts toward nearby English words.
- Watch for phonetic collisions between protected names and ordinary words.
  Examples:
  `Jrain` vs `brain` / `drain`
  `Finnan` vs `Finan` / `Finnen` / `Finn in`
- Use local conversational context aggressively for protected names.
  Turn-order language like `X's turn`, direct address, initiative chatter, and repeated nearby variants are strong evidence that a protected name is intended.
- If an unresolved error could change a name, event, decision, or the meaning of a substantive sentence, mark the questionable span with `[[...]]`.
- Leave unclear incidental table chatter, cross-talk, and short fragments verbatim when they do not affect the session record. Short lines are not automatically incidental: a brief name or decisive answer can matter.
- Apply `[[...]]` after checking:
  participant names from `session.yaml`, any provided glossary/dictionary, nearby lines, and repeated variants elsewhere in the session.
- Gather unresolved issues across all chunks. Never stop for ASR questions during cleanup; complete both passes before assessing the remaining uncertainty.
- Do not rely on a general impression of the chunk.
  You must inspect every transcript line individually for likely errors before deciding that it is clean.
- If you consult prior cleaned transcripts, prior session notes, or earlier cleanup artifacts, treat them as secondary evidence only.
  They may help confirm a likely correction, but they must not override stronger evidence from the current prepared transcript, `session.yaml`, or the glossary/dictionary.

## Workflow

1. Read `session.yaml` and `source.prepared.md`.
2. If a campaign glossary or dictionary is provided, load it once before cleaning any transcript chunks.
   Also derive a protected-name list from `session.yaml` participants before cleaning.
   Do not proceed as if the dictionary is unavailable if a path was provided but not read; stop and surface that failure.
   Do not load archival files from `sources/` as correction evidence.
   If you use secondary evidence from prior cleaned material or the broader vault, keep it clearly subordinate to the current transcript, `session.yaml`, and glossary/dictionary.
3. Clean the transcript in contiguous chunks.
   Keep a rolling session correction ledger so the same error is corrected consistently later in the session.
   Within each chunk, do this in order:
   1. do a line-by-line suspicion pass over every transcript line in the chunk
   2. for each line, explicitly check for:
      - protected names and possessives
      - fantasy-looking terms
      - ordinary English words that may be phonetic substitutions for names
      - malformed or semantically implausible phrases
      - repeated spelling drift from nearby lines
   3. mark each line mentally as:
      - clean
      - fixable with high confidence
      - materially uncertain, so it needs `[[...]]`
      - unclear incidental speech, which can remain verbatim
   4. resolve likely corrections using local context, participant names, glossary/dictionary, and repeated nearby variants
   5. only then write the cleaned chunk
4. Do a strict second pass over the cleaned transcript before finalizing it.
   This pass is specifically for finding missed mistakes, not for polishing prose.
   Re-check:
   - protected names and their possessive forms
   - turn-order language like `X's turn`
   - valid English words that may actually be ASR substitutions for names
   - repeated spelling drift within the same session
   - phrases that are grammatical but semantically wrong in context
5. After editing, run `scripts/report_cleanup_diff.py` to validate the cleaned transcript and generate:
   - `<prefix>-cleanup-report.json`
   - `<prefix>-session-corrections.yaml`
   - `<prefix>-human-transcript.md`
   - `<prefix>-cleanup-summary.md`
6. Fix header mismatches or line-count drift before proceeding. Unresolved markers are evidence of uncertainty, not structural validation failures. Assess their importance under Manual Review below.

## Chunking

- Prefer chunk sizes that preserve local conversational context.
- For long transcripts, use contiguous blocks with small local overlap in your reasoning, but the written output must still preserve the original one-line-per-unit structure.
- Do not reread the full transcript just to make a report. Use the diff script.
- Even when reasoning over a chunk, cleanup decisions should be made line by line.

## Glossary

- The glossary is optional.
- If provided, use it to normalize known PCs, NPCs, locations, organizations, items, and fantasy terms.
- Even without a glossary, participant game roles from `session.yaml` should still be treated as high-priority canonical names.
- If the glossary/dictionary is compact, load it in full once and keep it active for the whole transcript.
- Read the glossary as canonical reference material.
  It defines the right spellings and names for existing entities; it does not define the set of all possible transcript mistakes.
- Do not limit corrections to glossary matches.
  Many real transcript errors will be novel and must be caught from sentence meaning, turn context, and repeated same-session usage.
- Do not force unknown proper nouns to match the glossary.
- Novel entities are allowed. Preserve them if they are internally plausible.
- Do not treat archived bundle inputs as glossary material.
- Prior cleaned transcripts and related outputs may be useful secondary evidence, but they are not canonical by default.

## Manual Review

Assess the complete cleaned transcript once, after both cleanup passes. Judge importance and scale together; do not use a fixed error-count threshold. One unresolved identity may matter more than many unclear interjections. Material issues include uncertain names or entities, garbled full sentences, and one or several errors that obscure what happened or what a speaker meant. Ordinary table chatter and cross-talk can be tolerated.

In `interactive` mode (also the standalone default):

- If no material unresolved issues remain, continue automatically. Never ask whether a clean transcript, or one with only incidental noise, is acceptable.
- If material issues remain, the review is required. In chat, give the total affected lines and distinct issues, a compact list of unresolved lines with IDs and brief before/after context, and a judgment about their impact. Group repeated entities but retain occurrence IDs. For a large set, summarize each material issue group with representative context and link the complete inventory. Ask whether this level of uncertainty is tolerated or needs cleanup.
- Accepting uncertainty authorizes continuing with that uncertainty; it does not establish an uncertain name or event as fact. Record acceptance against the current transcript. Do not ask again on resume unless the relevant source changes or a new material issue is found.

In `auto` mode, report uncertainty and continue with omissions or qualified facts where reliable. Do not invent corrections or record human acceptance. Stop with a blocker report only if unresolved meaning prevents reliable downstream work.

Read [references/manual-review.md](references/manual-review.md) when markers remain, when recording acceptance, or when the user requests the audio review page. The cleanup report supplies context and a source fingerprint; the agent supplies the materiality judgment. Generate the page and clips only after the user requests them following the chat review. The page supports corrections, skipping one issue, and skipping remaining cleanup. Apply saved corrections, rerun structural validation, and continue when remaining material uncertainty has been accepted. A skipped issue remains unchanged.

## Detection Heuristics

When scanning each line, treat these as strong error signals:

- a protected name is missing where turn-order or direct-address context suggests it should appear
- a common English word appears where a PC/NPC name would make more sense
- a phrase is grammatical but does not make sense in the scene
- a fantasy-looking term differs slightly from a canonical glossary term
- the same unusual sound is rendered differently across nearby lines

Treat these as weaker signals that still deserve review:

- odd capitalization on a likely proper noun
- split-word variants like `Finn in`
- possessives that look almost right, like `Dray's` for `Jrain's`

## Diff Report

Generate the report with:

```bash
python .agents/skills/transcript-cleaner/scripts/report_cleanup_diff.py \
  --original /path/to/source.prepared.md \
  --cleaned /path/to/source.cleaned.md \
  --output-dir /path/to/cleanup-artifacts \
  --file-prefix addermarch-campaign-007
```

The script validates:

- exact header preservation
- line-count preservation
- changed lines
- unresolved `[[...]]` markers
- repeated replacement pairs derived from diffs
- a compact replacement summary printed to stdout
- a condensed human-readable transcript with adjacent speaker lines merged
- a markdown cleanup summary grouped by corrected term

Treat the script output as the canonical cleanup report rather than asking the model to narrate every change.

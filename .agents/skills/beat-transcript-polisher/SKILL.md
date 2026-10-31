---
name: beat-transcript-polisher
description: Extract recap-scoped excerpts from a finalized polished transcript and select pull quotes and audio highlights. Preserve polished wording, speakers, source spans, and existing recap highlight selections. Use after a session recap exists; this is not another transcript polishing pass.
---

# Transcript Excerpts and Highlights

This optional workflow keeps the existing `beat-transcript-polisher` invocation
and `cleaned/beat-transcripts/` filenames for compatibility. It copies reviewed
speech into recap excerpts and helps choose highlights. It is not part of default
`session-note-prep` and does not rerun cleanup, polishing, or prose-quality review.

## Inputs and ownership

- Resolve the full polished Markdown from the session YAML's
  `transcriptProcessing.artifacts.polishedMarkdown.path` (relative to the bundle).
  Use its finalized `Complete` or `Complete with retained uncertainty` version.
- `cleaned/<bundle-stem>-session-recap.md` owns recap IDs, titles, beat IDs, and
  source ranges. Ignore potentially stale `session-summary-context.json`.
- The polished transcript owns wording, corrected speakers, display substitutions,
  and `UID:start-end` character spans. Never rebuild speech from cleaned speaker
  headers or archival inputs. The helper reuses the existing polished parser.
- Existing `## Pull Quotes` and `## Audio Highlights` in the recap are the user's
  selected material. The highlights summary is a candidate pool, not authority
  to overwrite those selections.

## Extract excerpts

Run from the vault root with Python and PyYAML:

```bash
python -B .agents/skills/beat-transcript-polisher/scripts/manage_beat_transcripts.py \
  --transcript /path/to/cleaned/<bundle-stem>-transcript.md \
  --session-recap-md /path/to/cleaned/<bundle-stem>-session-recap.md \
  --output-dir /path/to/cleaned/beat-transcripts \
  --file-prefix <bundle-stem>
```

The helper creates missing `<bundle-stem>-<recap-id>-transcript.md` files,
updates recap `Polished Transcript` links and excerpt headings, and creates a
candidate summary if absent. Transcript bodies are copied exactly, including
speaker labels, paragraph breaks, source spans, `[garbled]`, `[cross-talk]`,
`{{uncertainty}}`, annotations, and wikilinks.

A recap boundary may cross a polished turn or a connected group of turns sharing
UIDs. Include the entire group; do not infer character cuts or split a sentence.
The excerpt records its actual `Source Range` and requested `Recap Source Range`,
and the helper reports the expansion. Adjacent excerpts can share this context.
It never changes the recap's own source boundaries.

For one block add `--recap-block-id recap-001`. For a beat request, select the
recap block containing that beat. Existing excerpts are preserved by default.
If an old excerpt differs, inspect its changes before using `--overwrite` to
refresh it from the finalized transcript. Do not silently discard unique manual
corrections; resolve useful corrections upstream first. `--overwrite` affects
excerpts only, never the candidate summary or selected highlights.

## Choose highlights

Read the extracted speech and fill
`cleaned/beat-transcripts/<bundle-stem>-transcript-highlights.md`. Preserve existing
candidate IDs and entries; add only missing beat sections when continuing work.
Do not confuse surrounding boundary context with the requested beat's content.

Prefer 2–3 strong quotes per beat when available, with varied speakers and moods.
Copy the polished wording and speaker, retaining uncertainty; do not rewrite a
quote to make it punchier. Use `None identified.` for a beat without a useful
quote. For audio, choose worthwhile speeches, narrations, exchanges, or table
moments: usually 2–5 across a session when the material supports them. No filler
candidates to satisfy a quota. Use `None identified.` when there are none.

Keep IDs unique across the candidate document and use actual source UIDs:

```markdown
## Pull Quotes

### beat-001 | Arrival

- Recap Block: recap-001
- Transcript: <bundle-stem>-recap-001-transcript.md
- Source Range: u0001 -> u0100
- Pull Quotes:
  - ID: quote-beat-001-001
    - Quote: "The maze remembers."
    - Speaker: Kalima
    - Source Lines: u0004-u0006

## Audio Monologue Candidates

- ID: audio-001
  - Source Lines: u0020-u0040
  - Speaker: DM
  - Summary: Holda tells his story.
  - Why Called Out: Central exposition.
```

The helper does not extract audio. Final session-note component generation uses
shared `_scripts/audio_tools.py` for selected clips. Listening questions can use
[process-transcript's audio-review mode](../process-transcript/references/audio-review.md)
without rerunning processing.

## Preserve selections

Normal runs and `--overwrite` do not sync candidate lists into the recap.
They preserve selected wording, speakers, order, titles, output filenames,
comments, removed candidates, and empty or deleted sections.

For a **new, unreviewed** recap only, after filling candidates, run the same
command with `--seed-highlights`. This explicitly copies candidates into missing
recap sections. Even this option leaves existing sections untouched, including
empty ones, and skips unfinished TODO entries. It must not be used to resurrect
a section the user removed. A missing section alone is not proof of first use.

For an existing reviewed recap, present new candidates in chat. Apply accepted
additions or changes directly and narrowly to the selected sections, preserving
all other choices. There is no automatic merge or replacement of the selected
list. In recap audio entries, use `Title` and `Output` (default `audio-NNN.m4a`),
with `ID`, `Speaker`, and `Source Lines`; pull quotes retain their candidate fields.
Explicit review answers need no second approval.

## Check and finish

The normal helper run checks excerpt text and source spans against the full
polished turns, recap links, metadata, candidate headings, and unique IDs. After
editing highlights, run once with `--validate-only`. It writes nothing. Review
candidate wording, speaker attribution, and UID ranges against the polished
passage. Retained uncertainty is reported, not reopened as a new review task;
`[[wikilinks]]` are not uncertainty markers.

If a new transcription problem is discovered, propose it in chat and apply an
approved fix to the full transcript through
[correct-transcript](../correct-transcript/SKILL.md), or the existing
process-transcript review if active. Refresh affected excerpts afterward.
Do not correct only the excerpt or initiate another full-session review.

Report excerpts created/refreshed, any expanded boundary context, proposed
highlights, and whether existing selections were preserved. This skill does not
render the final session note or commit changes automatically.

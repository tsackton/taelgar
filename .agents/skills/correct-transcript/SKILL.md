---
name: correct-transcript
description: Apply targeted later wording, uncertainty, display-label, and speaker corrections to an existing polished transcript while preserving source mappings. Supports several speakers within one turn. Use process-transcript for initial processing, ongoing human review, and optional audio-review pages.
---

# Correct Transcript

Use the maintained correction helper for specific fixes to finalized transcripts
or quality-complete portable reviews. Do not invent another replacement script,
edit hidden mappings by hand, or rebuild the whole session for a small correction.
An exact user correction authorizes that change; do not ask for the same approval
again. A request to inspect or propose changes remains read-only. Bring materially
uncertain wording or attribution to the user before applying it.

Ongoing process-transcript review stays in that skill. It may reuse this helper's
code without invoking another workflow or repeating these instructions.

## Ownership

- Wording changes go into cleaned UID text and its corresponding polished turns.
- Speaker corrections go **only into polished turns**, including multiple speakers
  within one UID. Original, prepared, and cleaned speaker headers stay unchanged.
- `[garbled]` and `[cross-talk]` are polished display substitutions; retain the
  underlying recognized text in cleaned sources. Use cross-talk only with evidence
  of overlapping speech. These labels must not silently hide meaningful speech.
- Confirmed uncertainty can be unmarked; retaining uncertainty does not confirm a
  reading. Preserve spoken errors, grammar, repetitions, and false starts.
- Polished Markdown owns corrected attribution. Do not write `speakerCorrections`
  to YAML or copy corrected labels back into the prepared/cleaned headers.

Read the entire affected exchange, its cleaned UID text, and relevant local
changes before choosing exact targets. Use vault evidence to support plausible
recognition, not to replace a spoken claim with what ought to have been said.
Follow repository branch and authorization rules. Do not commit automatically.

## Inspect, preview, apply

The code lives in the shared process-transcript implementation:
[transcript_corrections.py](../process-transcript/scripts/transcript_corrections.py).
It reuses the source parsers, coverage checks, locks, transactions, and finalization
helpers. Run with Python 3.9+ and PyYAML, with bytecode disabled.

Resolve the session with process-transcript's `resolve` command or a verified
bundle path. Set `HELPER` below to that script and `BUNDLE` to the session directory:

```bash
python3 -B HELPER --bundle BUNDLE inspect --uid u1975
```

Repeat `--uid` to inspect several UIDs. The result includes the input fingerprint,
cleaned text, complete intersecting polished turns, their **zero-based indexes**,
source character ranges, and pending review questions. Inspect neighboring UIDs
for conversational context. An index is valid only with this fingerprint and its
exact `before` text; do not reuse indexes from another version.

Read [the correction contract](references/corrections.md) before constructing a
plan. Supply the JSON object on stdin; do not persist another decision-state file:

```bash
python3 -B HELPER --bundle BUNDLE preview --plan -
python3 -B HELPER --bundle BUNDLE apply --plan -
```

Preview is read-only and is useful for a proposal requiring a decision. For an
already-authorized exact correction, apply the inspected plan directly and review
the returned diff/status once; a separate preview invocation is not required.
Otherwise present the concrete proposal and wait for the needed decision.

The helper automatically propagates exact, unique wording replacements. Supply
explicit revised polished turns when punctuation, repetition, or an existing
display label makes matching ambiguous. For a split, specify complete parts with
their exact source spans; never estimate source offsets from punctuated display
text or invent sub-turn timestamps. A replacement crossing an existing turn or
speaker boundary must be expressed as separate source edits with reviewed text.

For an open review, include only actual decisions using the report's issue IDs.
The helper preserves remaining questions and shifts their positions. It refuses
to overwrite decisions already entered into the report; apply those through
process-transcript first, or reconcile them explicitly. The review Markdown stays
the sole durable review state. An active unfinished processing queue belongs to
`process-transcript`, not this skill.

## Verification and completion

The helper validates source fingerprints, exact targets, speech preservation,
source coverage, speaker split partitions, and markers before writing. It rejects
unsupported polished-only word changes. Pure speaker changes preserve existing
display text exactly, including garbled labels. Read the changed passages after
application and run scoped `git diff --check`.

Finalized inputs remain finalized with updated fingerprints. A portable review
remains open while questions remain; when its last question is resolved, normal
finalization removes temporary review/processing files. Original and prepared
sources are never written. Cleanup, speakers, and display changes do not trigger
new scene, beat, recap, or annotation work. `downstreamToInspect` lists existing
derivatives that may need separate review, not automatic regeneration.

If a write or finalization is interrupted, run `HELPER --bundle BUNDLE recover`
with Python and `-B`. This uses shared recovery and retires only committed correction
snapshots; it preserves unrelated active work. Then inspect current inputs and
status before continuing. Never replace fingerprints merely to bypass a stale-input error.

Report what changed, any uncertainty retained, and whether the session is finalized.

## Maintenance

Run the correction regressions without touching live sessions:

```bash
PYTHONPATH=.agents/skills/process-transcript/scripts python3 -B -m unittest discover -s .agents/skills/process-transcript/tests -p 'test_corrections.py'
```

The full process-transcript behavioral suite also covers shared parsing, recovery,
finalization, and Markdown review. Keep correction behavior in the shared helper.

# Cleanup assessment and optional audio review

Use the prepared and cleaned transcript as text evidence. The optional page plays the original recording for human review; this does not permit consulting archived transcripts in `sources/` as correction evidence.

## Assess after the complete cleanup

Run `scripts/report_cleanup_diff.py` normally. Its `review` object contains `transcriptSha256`, one issue per marked line, two source lines before and after, counts, and default material classifications. Structural errors still block; unresolved markers do not change its successful exit status.

If there are markers, author `cleanup-artifacts/<prefix>-cleanup-assessment.json`:

```json
{
  "transcriptSha256": "copy the current report fingerprint",
  "judgment": "Brief overall assessment of the uncertainty's effect on the session record.",
  "issues": [
    {"uid": "u0042", "importance": "material", "reason": "Unclear name of the person receiving the letter."},
    {"uid": "u0108", "importance": "incidental", "reason": "Overlapping table chatter; no effect on the described action."}
  ]
}
```

List each marked line once. Unassessed markers default to material. The helper rejects stale assessments and nonexistent marked lines. Rerun the report with `--assessment-json` and, when it exists, `--decisions-json <prefix>-cleanup-decisions.json`. Use `review.pendingMaterialCount` to decide whether the interactive pause is needed. An incidental classification still needs contextual judgment; never classify by utterance length alone.

Show material unresolved text, IDs, brief context, and impact in chat. Ask whether the user tolerates the uncertainty or wants corrections. Do not create a page or extract clips merely because a pause is needed.

After an explicit tolerance decision, record it:

```bash
python .agents/skills/transcript-cleaner/scripts/review_cleanup.py accept \
  --cleaned /path/to/cleaned/<prefix>-source-cleaned.md \
  --assessment /path/to/cleanup-artifacts/<prefix>-cleanup-assessment.json \
  --decisions /path/to/cleanup-artifacts/<prefix>-cleanup-decisions.json \
  --reason 'The actual user decision accepting the remaining uncertainty'
```

This records skips without altering text. Use it only after human acceptance, never to simulate acceptance in auto mode. For a newly changed transcript, reassess it and use a new decision file if the old one no longer matches; preserve prior decisions as history.

## Build the page only when requested

Use a fresh local review directory beside the recordings, or a temporary directory. Keep extracted audio outside the vault. The small assessment and decision files may remain under `cleaned/cleanup-artifacts/`.

Verify that `session.yaml`'s `sourceAudioPath` uses the transcript's clock before using it. For older bundles, combined recordings, or offset clocks, provide `--audio-map` instead. Do not assume recordings share a clock or use a nearby file based only on its name.

```json
{
  "recordings": [
    {"startUid": "u0001", "endUid": "u0800", "audioPath": "/absolute/path/part1.m4a", "offsetSeconds": 0},
    {"startUid": "u0801", "endUid": "u1500", "audioPath": "/absolute/path/part2.m4a", "offsetSeconds": -3600}
  ]
}
```

Each reviewed UID must match exactly one range. Audio time equals transcript time plus `offsetSeconds`. Timestamp resets need separate mappings. Clip context is trimmed to the mapped recording segment. If the recording or mapping is unavailable, report that limitation and retain the chat review; do not fabricate a clip.

```bash
python .agents/skills/transcript-cleaner/scripts/review_cleanup.py prepare \
  --cleaned /path/to/cleaned/<prefix>-source-cleaned.md \
  --assessment /path/to/cleanup-artifacts/<prefix>-cleanup-assessment.json \
  --decisions /path/to/cleanup-artifacts/<prefix>-cleanup-decisions.json \
  --session /path/to/cleaned/<prefix>-session.yaml \
  --output /path/outside/vault/cleanup-review/review.json

python .agents/skills/transcript-cleaner/scripts/review_cleanup.py serve \
  --review /path/outside/vault/cleanup-review/review.json \
  --decisions /path/to/cleanup-artifacts/<prefix>-cleanup-decisions.json
```

For mapped recordings replace `--session` with `--audio-map /path/to/audio-map.json`. Open the printed localhost URL in the app browser. The page shows flagged text, surrounding lines, a clip, a correction field, and skip controls. It saves decisions locally; it does not rewrite the transcript while the user reviews it. On resume, reopen the existing page and decisions rather than overwriting them.

After the user finishes, apply saved corrections:

```bash
python .agents/skills/transcript-cleaner/scripts/review_cleanup.py apply \
  --review /path/outside/vault/cleanup-review/review.json \
  --decisions /path/to/cleanup-artifacts/<prefix>-cleanup-decisions.json
```

The helper rejects stale input, preserves header bytes and line endings, and saves a before-apply snapshot beside the decisions. It changes only corrected lines; skipped lines keep their uncertain text. Reassess the remaining markers against the new transcript fingerprint and rerun the diff report with the updated decisions. Preserve skipped decisions when reassessing; they count as accepted uncertainty. If partial review leaves material issues undecided, retain the existing pause. Do not proceed merely because the page was opened.

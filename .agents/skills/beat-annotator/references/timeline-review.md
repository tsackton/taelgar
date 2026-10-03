# Chronology review after annotation

Review actual passage of time in the cleaned source: session start, rests, waking, evenings, travel days, explicit dates, and meaningful time-of-day changes. A proposed rest, rules discussion, flashback, or repeated mention of the same rest does not advance the date. A long rest need not cross midnight. Infer only what the source supports, with YAML as a starting anchor rather than a reason to suppress conflicts.

Author `cleaned/<prefix>-timeline-evidence.json`:

```json
{
  "inferredStart": "1749-09-16",
  "inferredEnd": "1749-09-17",
  "transitions": [
    {"uid": "u0001", "label": "Session start", "date": "1749-09-16", "time": "evening", "basis": "inferred", "evidence": "Session YAML plus the opening description of dusk."},
    {"uid": "u0402", "label": "Next morning", "date": "1749-09-17", "time": "morning", "basis": "explicit", "evidence": "DM: After sleeping through the night, you set out at dawn."}
  ],
  "issues": [],
  "resolutions": {}
}
```

Use null dates and `basis: unknown` where justified. The first transition is always session start at the first source UID; cite the actual supporting passage in `evidence` when it occurs later. Include all supported later date/time transitions, even several within one beat or scene. `inferredEnd` is the date at the end of the source, not an invented extra day. Cite source UIDs in evidence text where a transition relies on multiple passages. For non-transcript input, use its prepared source UIDs and describe the note evidence.

Add semantic discrepancies needing resolution under `issues` as objects with `detail` and `evidence`. The helper checks values, ordering, beat/fact agreement, and YAML endpoints; it cannot identify the meaning of rests or judge whether all transitions were found. That remains the agent's job.

```bash
python .agents/skills/beat-annotator/scripts/review_timeline.py \
  --session /path/to/cleaned/<prefix>-session.yaml \
  --beats-json /path/to/cleaned/<prefix>-beats.json \
  --beat-facts-json /path/to/cleaned/<prefix>-beat-facts.json \
  --transcript /path/to/cleaned/<prefix>-source-cleaned.md \
  --evidence-json /path/to/cleaned/<prefix>-timeline-evidence.json \
  --output /path/to/cleaned/<prefix>-timeline-review.json
```

Exit 0 means no open discrepancy; exit 2 means the report was written with discrepancies to resolve; other failures are invalid input. No command here changes session YAML.

Fix obvious interpretation or annotation mistakes from the source. Send needed beat-date changes through `transcript-splitter`, then regenerate matching fact dates and rerun this review. Do not change beat boundaries just to make the date check pass. For a mechanically flagged sequence that the source actually explains, add a specific resolution keyed by the report's issue key:

```json
"resolutions": {
  "beat-003:sequence": {"by": "source", "reason": "u0410 explicitly says three uneventful days pass before this scene."}
}
```

Never resolve a genuine ambiguity merely to avoid a pause. A resolution with `by: human` must record an actual user decision. Remove stale resolutions when the underlying issue disappears.

In interactive mode, pause only for remaining discrepancies needing human judgment or YAML changes. Show the inferred sequence, source evidence, the current YAML values, and the proposed values. If `drEnd` is blank, propose the supported value here. If no end date is supportable, retain uncertainty and ask only when that uncertainty prevents a defensible chronology.

After approval, edit only the approved YAML date fields and refresh affected beats/facts before rerunning the report. Approval of scene grouping alone does not authorize YAML date changes. If the user deliberately keeps a discrepant or blank YAML value, record that explicit decision under its `yaml:drStart` or `yaml:drEnd` issue as a human resolution. Do not pretend the values agree.

In auto mode, perform the same review, repair narrow source-supported errors, and never edit YAML dates without approval. An unresolved discrepancy requiring human input is a blocker report, not permission to make up an answer. Clean chronology proceeds without a pause.

The review stores hashes of its session, beats, facts, cleaned source, and evidence. Regenerate it after any input changes. Scene review uses this same transition record to avoid inventing a second chronology.

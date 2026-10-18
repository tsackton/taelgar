# Recap Scene Proposal

Read this procedure in full before proposing scenes, recording approval, or checking scene approval on resume. Follow [the main skill](../SKILL.md) for modes, artifact paths, and human-owned recap protection. Run commands from the vault root.

Beats are evidence and navigation units; they are not automatically recap scenes. Before building the summary context, propose a smaller set of contiguous scene groups that reflects the session's actual playable situations.

Human guidance controls this stage:

- If the user gives exact beat groupings, preserve them unless they fail ordered coverage validation.
- If the user gives partial guidance, treat it as a constraint and propose the remaining boundaries around it.
- If the user gives no guidance, infer scenes from continuity of location, situation, immediate goal, and active cast.
- Do not target a fixed scene count or mechanically make one scene per beat.
- Do not merge across a genuine change of situation merely to make the recap shorter.
- Keep scene grouping independent from timeline grouping; one recap scene may cross a calendar-date boundary.

Draft `cleaned/<bundle-stem>-recap-scenes.json` with this shape:

```json
{
  "schemaVersion": "1.0",
  "scenes": [
    {
      "sceneId": "scene-001",
      "title": "A short scene title",
      "beatIds": ["beat-001", "beat-002"],
      "rationale": "Why these adjacent beats form one playable situation.",
      "overview": "A very brief description of the scene's action.",
      "transitionToNext": "The concrete change that starts the next scene."
    }
  ]
}
```

Validate it and render the proposal preview:

```bash
python .agents/skills/session-summary/scripts/manage_recap_scenes.py \
  --beats-json /path/to/cleaned/<bundle-stem>-beats.json \
  --beat-facts-json /path/to/cleaned/<bundle-stem>-beat-facts.json \
  --recap-scenes-json /path/to/cleaned/<bundle-stem>-recap-scenes.json \
  --transcript /path/to/cleaned/<bundle-stem>-source-cleaned.md \
  --timeline-review /path/to/cleaned/<bundle-stem>-timeline-review.json \
  --require-review-fields \
  --output-dir /path/to/cleaned \
  --file-prefix <bundle-stem>
```

The validator requires every beat exactly once, in original order, divided into contiguous groups with stable sequential scene IDs.

Mode handling:

- `auto`: validate the proposal, make one narrow repair if needed, then continue without pausing.
- `interactive`: present both tables below in chat and always wait for approval of the displayed proposal before generating summary context. Respect supplied groupings, but still show their timing, overview, transitions, and chronology for review.

At the interactive checkpoint, state the scene count, display these tables, link the preview, and ask for approval or revisions:

| Scene name | Beats covered | Time in play | Brief overview | Transition to next scene |
|---|---|---|---|---|

Use elapsed transcript timestamps, including pauses, for time in play. The helper computes the range and duration; never estimate from line counts. If timestamps are absent or reset within a scene, state that timing is unavailable unless a verified alignment has been supplied. The final scene's transition is `Session ends`. Keep the overview and transition reason brief; the transition should explain the actual boundary, not just repeat the next title.

| In-world date/time or transition | Beats | Scenes | Evidence |
|---|---|---|---|

Use the checked chronology record: session start followed by all supported date/time transitions, including those within a beat or scene. Cite source IDs and distinguish explicit, inferred, and unknown timing. The helper maps transition IDs to beats and scenes.

After explicit approval, rerun the same command with `--record-approval 'actual user decision'`. Before interactive summary generation or resume, rerun it with `--require-approval --validate-only`. Approval is bound to the proposal and current review inputs. A changed grouping, source, facts, or chronology requires a new displayed proposal and approval. Do not create an approval record in auto mode.

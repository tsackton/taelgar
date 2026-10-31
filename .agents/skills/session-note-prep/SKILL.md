---
name: session-note-prep
description: Run or resume a prepared Taelgar session bundle through source cleanup, beat annotation, chronology review, scene grouping, and session-recap.md. Use for the end-to-end recap pipeline, not initial transcription or source-bundle preparation.
---

# Session Note Prep

Run the commands below from the Taelgar vault root, using a Python environment with PyYAML installed.

Use this skill to run the existing session pipeline end to end on one prepared bundle.

This is an orchestration skill.
It does not replace the stage-specific rules in the component skills.
At each stage, load the next skill and follow its rules strictly:

- [`../process-transcript/SKILL.md`](../process-transcript/SKILL.md)
- [`../transcript-splitter/SKILL.md`](../transcript-splitter/SKILL.md)
- [`../beat-annotator/SKILL.md`](../beat-annotator/SKILL.md)
- [`../session-summary/SKILL.md`](../session-summary/SKILL.md)

Prefer loading only the stage you are currently executing, not every component in full up front.

## Required Inputs

Work from a prepared session bundle with:

- bundle root containing `cleaned/` and `sources/`
- `cleaned/<bundle-stem>-session.yaml`
- `cleaned/<bundle-stem>-source-prepared.md`
- optional glossary or dictionary explicitly provided for this run

Use `<bundle-stem>` as the canonical `file_prefix`.
Derive it from the session manifest filename by stripping the trailing `-session`.

In this vault, the cleaned transcript equivalent of `source.cleaned.md` should normally be:

- `cleaned/<bundle-stem>-source-cleaned.md`

Prefer these canonical downstream artifact paths in `cleaned/`:

- `<bundle-stem>-beats.json`
- `<bundle-stem>-beats-preview.md`
- `<bundle-stem>-beat-facts.json`
- `<bundle-stem>-beat-facts-preview.md`
- `<bundle-stem>-timeline-evidence.json`
- `<bundle-stem>-timeline-review.json`
- `<bundle-stem>-recap-scenes.json`
- `<bundle-stem>-recap-scenes-preview.md`
- `<bundle-stem>-scene-approval.json` (interactive mode)
- `<bundle-stem>-session-summary-context.json`
- `<bundle-stem>-session-recap.md`

Stage-specific helper artifacts may live in subdirectories under `cleaned/`, for example:

- `transcript-work/` (temporary; retired by process-transcript finalization)
- `annotation-context/`

Use these bundle paths in component commands rather than their illustrative output directories or prefixes. Keep beats, beat facts, chronology, scenes, summary context, and recap under `cleaned/`; let process-transcript own its temporary work and portable review Markdown, and use `cleaned/annotation-context/` for extracted beat context. Where a command accepts `--file-prefix`, pass `<bundle-stem>`; where it accepts a full output filename, use the corresponding canonical path above.

## Modes

If the user does not specify a mode, default to `interactive`.

### `auto`

- Run all stages in order.
- After each stage, run the stage's deterministic validator or helper for a quick validation pass.
- Make one narrow repair pass if the validator output is specific and easy to fix.
- Do not pause for user confirmation between stages.
- Do not ask for manual cleanup at checkpoint boundaries.
- Still assess ASR importance and chronology. Complete transcript cleanup and quality review before surfacing consequential ASR questions. If process-transcript requires human decisions, stop with its portable review Markdown; auto mode cannot fabricate acceptance or bypass finalization gates. Do not edit `drStart`/`drEnd` without approval. Stop if chronology requires a human decision.
- If a stage still has a hard blocker after the quick repair pass, stop the pipeline there and report the blocker clearly instead of pretending the next stage is reliable.

### `interactive`

- Run all stages in order.
- Complete transcript cleanup, polishing, and quality review before asking about ASR. Pause only for process-transcript's consequential unresolved choices; show exact wording, the complete exchange, and a concrete proposal or recommendation to retain uncertainty. Apply actual user decisions and finalize each session before continuing. No pending decisions means automatic continuation. Requested audio review is evidence for those decisions, not a separate acceptance-state workflow.
- Continue through beat splitting and annotation without routine approval pauses. After annotation, review chronology; pause only for discrepancies needing human input or proposed changes to session YAML dates.
- Always present the scene proposal and date/time transition tables in chat, then wait for approval of the displayed scene split before drafting the recap. An already existing valid scene file or a supplied grouping does not bypass this review. A recorded approval of this exact displayed proposal remains valid on resume.
- If the user edits an artifact during a checkpoint, reread it and rerun the validator before moving on.
- Do not insert an extra checkpoint after `session-summary` unless the user explicitly asks for one.

## Human-Edited Recap Boundary

Validation and repair apply to the skill's own generated recap only, before its initial handoff to the user.

Once the recap has been handed off and a human has edited, accepted, or deliberately removed any generated content or structure, the recap is human-owned:

- do not run `manage_session_recap.py` against it
- do not rebuild, normalize, or repair it because it would fail the generated-artifact schema
- do not restore missing subsections, metadata, wording, or formatting
- do not treat validation failure as evidence that a human edit is wrong

A human-owned recap is allowed to fail the pipeline validator. Later skills may read it as authoritative input, but may change it only within the scope of a new explicit user request. Revalidate or repair it only when the user explicitly asks to revalidate, rebuild, or fix the recap.

## Shared Rules

- Honor each component skill's evidence rules. Process-transcript may compare original and prepared references under its own contract; archived ASR wording is not independent corrective authority. Later annotation stages retain their own restrictions on `sources/`.
- Playing verified original recordings for a requested human ASR review is permitted. Use process-transcript's [optional audio page](../process-transcript/references/audio-review.md); its answers feed the same review and application step. Standalone later edits belong to [correct-transcript](../correct-transcript/SKILL.md).
- Never edit `drStart` or `drEnd` without approval of the specific proposed values. Scene approval is not approval to change YAML dates.
- Treat validated downstream artifacts as the handoff between stages.
- Do not silently weaken a stage's validation requirements just because this orchestrator is running the full pipeline.
- Before starting a stage, check whether its expected bundle artifact already exists.
- If an artifact already exists, validate it before trusting it.
- If an existing artifact validates cleanly and its upstream dependencies are still current, reuse it and skip regenerating that stage. Validation alone is not human acceptance. Check transcript completion status, chronology input hashes, and scene approval before bypassing their respective reviews.
- If an existing artifact fails validation, treat that stage as incomplete: repair or regenerate it, then continue forward.
- The human-edited recap boundary above overrides these existing-artifact rules for `session_recap_md` after handoff.
- Do not rerun completed stages just because this is a full-pipeline skill.
- Keep filenames stable across the run so later stages point at the current validated outputs.

## Workflow

1. Discover the bundle root and `cleaned/` directory.
2. Resolve:
   - `session_yaml = cleaned/<bundle-stem>-session.yaml`
   - `prepared_transcript = cleaned/<bundle-stem>-source-prepared.md`
   - `cleaned_transcript = cleaned/<bundle-stem>-source-cleaned.md`
   - `beats_json = cleaned/<bundle-stem>-beats.json`
   - `beat_facts_json = cleaned/<bundle-stem>-beat-facts.json`
   - `recap_scenes_json = cleaned/<bundle-stem>-recap-scenes.json`
   - `summary_context_json = cleaned/<bundle-stem>-session-summary-context.json`
   - `session_recap_md = cleaned/<bundle-stem>-session-recap.md`
3. Check which stage outputs are already present in `cleaned/`.
4. Validate and resume from the latest trustworthy stage instead of restarting automatically.
   Use this order:
   - if `session_recap_md` and `summary_context_json` exist and the recap is still an untouched agent-generated artifact in the current pre-handoff run, validate it; if `manage_session_recap.py` passes, the pipeline is already complete
   - if an existing recap predates the current run or has been handed off for human review, treat it as human-owned and do not validate or repair it without an explicit request
   - else if `recap_scenes_json` exists and validates, verify current chronology and, in interactive mode, use `manage_recap_scenes.py --require-approval` with the full review inputs before resuming at `session-summary`; without matching approval, show the proposal tables and wait
   - else if `beat_facts_json` exists and validates, resume at the chronology review, then recap-scene proposal
   - else if `beats_json` exists and `manage_beats.py` passes, resume at `beat-annotator`
   - else if `cleaned_transcript` exists, for transcript sources require process-transcript status to report `finalized: true` and `outputsCurrent: true` before resuming at `transcript-splitter`; otherwise resume Stage 1. For normalized non-transcript sources, reuse a structurally valid current cleaned source. Do not reopen unchanged accepted uncertainty
   - else start at transcript cleanup for `sourceType=transcript`, or source normalization for `sourceType=narrative|raw_notes`
5. Create helper directories only if needed, for example:
   - `cleaned/annotation-context/`

   Process-transcript creates and retires its own work directories; do not create a new legacy `cleanup-artifacts/` review state.
6. Run the remaining stages in order below. Before checking scene approval on resume, read [the scene-proposal procedure](references/scene-proposal.md).

## Stage 1: Upstream Source Cleanup Or Normalization

Produce `cleaned/<bundle-stem>-source-cleaned.md`. If it already exists and is trustworthy under the shared resume rules, reuse it.

For `sourceType=transcript`, load and follow [process-transcript](../process-transcript/SKILL.md). Inspect its status for this bundle first. Reuse current finalized references; otherwise resume or initialize from the existing session YAML and prepared source as that skill specifies. Preserve existing cleaned work through its import/resume rules rather than replacing it with a fresh copy of prepared text.

Complete cleanup, full-session polishing, quality review, required human decisions, and finalization. The retained products are original, prepared UID, cleaned UID, polished Markdown, and session YAML. The portable review Markdown is the sole durable decision state while review remains open; do not add the retired cleaner's assessment or acceptance JSON files. Present pending decisions with exact text, complete context, and the proposed reading or explicit unresolved disposition. Apply chat or audio answers within process-transcript's review; do not route the user through another skill, repeat cleanup, or ask for the same decision again.

Before source splitting, require process-transcript status to show `finalized: true` and `outputsCurrent: true`. Accepted uncertainty is compatible with completion and is not reopened. This Stage 1 requirement does not authorize retroactive processing of historical bundles already resumed from valid downstream products or human-owned recaps.

For `sourceType=narrative|raw_notes`, run:

```bash
python .agents/skills/session-note-prep/scripts/normalize_source.py \
  --session /path/to/cleaned/<bundle-stem>-session.yaml \
  --output-dir /path/to/cleaned \
  --file-prefix <bundle-stem>
```

Check sensible detected shape, useful primary units, preserved supplemental sources, and omitted duplicate sections recorded in the normalization report. Non-transcript normalization has no routine approval pause. Resolve obvious normalization failures or report a structural blocker; do not invent ASR review for note-based sources.

## Stage 2: Source Splitting

Load and follow [transcript-splitter](../transcript-splitter/SKILL.md) for drafting, validation, and preview generation, using this bundle's `cleaned_transcript`, `session_yaml`, and `beats_json` paths.

Validate existing beats and reuse them only under the shared resume rules. Otherwise complete the splitter's workflow and checks. In both modes, continue directly into annotation without a beat approval checkpoint. Carry chronology warnings forward to the review after annotation; do not invent dates or change YAML to satisfy a check.

## Stage 3: Beat Annotation

Load and follow [beat-annotator](../beat-annotator/SKILL.md) for context extraction, fact annotation, validation, and review. Use this bundle's `session_yaml`, `cleaned_transcript`, `beats_json`, and `beat_facts_json`; extract context into `cleaned/annotation-context/` and write facts and their preview into `cleaned/`.

Validate existing beat facts and reuse them only under the shared resume rules. Whether facts are reused or newly generated, perform the full-session chronology review before scene grouping. There is no general beat-facts approval checkpoint. Read and follow [the chronology procedure](../beat-annotator/references/timeline-review.md), producing the source-based transition record and current checked report.

Pause in interactive mode only for remaining discrepancies needing human input or proposed YAML date changes. A blank `drEnd` is an opportunity to propose the supported end date here. Show current/proposed values and evidence; apply date changes only after explicit approval. Repair source-supported mistakes upstream, refresh matching facts, and rerun the review. When chronology is consistent, continue automatically. In auto mode, unresolved discrepancies requiring human input stop the run with a blocker report.

## Stage 3.5: Recap Scene Proposal

Read and follow [the scene-proposal procedure](references/scene-proposal.md) in full. It owns grouping guidance, the scene JSON shape, validation, the two review tables, and approval recording and verification.

In interactive mode, display the scene proposal and date/time transition tables and obtain approval before generating summary context, even when the user supplied groupings or valid scene JSON already exists. On resume, reuse approval only when it matches the current proposal and review inputs; otherwise display the updated proposal and obtain approval. In auto mode, validate the grouping without creating a human approval record.

## Stage 4: Session Summary

Load and follow [session-summary](../session-summary/SKILL.md) for context building, recap scaffolding, drafting, and validation. Use this bundle's canonical paths and approved or auto-validated `recap_scenes_json`; do not use the standalone skill's legacy fallback without a scene map.

Require a current chronology review with no open issues and, in interactive mode, matching approval of the displayed scene proposal. Do not treat valid JSON as proof of either review. Follow the scene-proposal reference to verify approval before summary generation or resume.

If both `summary_context_json` and `session_recap_md` already exist, first apply the human-edited recap boundary above. Run `manage_session_recap.py` only when the recap is still an untouched agent-generated artifact in the current pre-handoff run. If it validates cleanly, skip this stage and treat the bundle as already complete. Otherwise, leave a human-owned recap unchanged unless the user explicitly requested rebuilding or validation.

The component skill owns the written-session-note lookup, daily timeline rules, and human-owned `Arc` and `Table Notes` fields. At handoff, surface those optional fields as values the user may fill in.

This stage completes the skill. Do not add an automatic pause after it in `interactive` mode unless the user asked for one.

## Completion Criteria

The run is complete when these files exist and pass their stage validations:

- `cleaned/<bundle-stem>-source-cleaned.md`
- `cleaned/<bundle-stem>-beats.json`
- `cleaned/<bundle-stem>-beat-facts.json`
- `cleaned/<bundle-stem>-timeline-review.json` with current inputs and no open discrepancies
- `cleaned/<bundle-stem>-recap-scenes.json`
- `cleaned/<bundle-stem>-session-summary-context.json`
- `cleaned/<bundle-stem>-session-recap.md`

For transcript sources processed through Stage 1 in this run, completion also requires current finalized process-transcript outputs, including the YAML-registered polished Markdown and completion fingerprints. Interactive completion requires consequential ASR decisions to have been resolved or explicitly retained, and the current displayed scene grouping to have been approved. Structural validation does not substitute for these decisions. The human-owned recap boundary still applies to completed historical runs; do not retroactively rebuild them to add new review artifacts.

If the run stops early, report:

- the last completed stage
- the blocking artifact path
- the validator error or unresolved review issue
- the next concrete action needed to continue

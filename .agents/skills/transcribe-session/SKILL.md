---
name: transcribe-session
description: Transcribe local RPG session recordings with ElevenLabs Scribe v2, then identify speakers with a local reference-based voice classifier and verified Scribe-ID fallback for short cues. Also inventory ordered chunks and alternate capture tracks. Use for first-pass session transcription and speaker attribution; stop before transcript cleanup or session-note preparation unless separately requested.
---

# Transcribe Session

Create a reproducible first-pass transcript from one local recording. Use the deterministic script in this skill; do not use older transcription helpers elsewhere in the repository.

## Required inputs

Resolve and verify:

- the exact local audio file;
- the campaign participant roster YAML;
- automatic speaker detection (the default), or an explicitly requested fixed
  speaker count;
- an optional UTF-8 keyterm file containing one reviewed campaign or world term per line;
- an explicit transcription workspace beside the original recording, normally
  `<recording-directory>/transcription/scribe-v2/`;
- whether the user has authorized uploading this exact recording to ElevenLabs.

Search campaign and session records before proposing world keyterms. Character and player names come from the participant roster. Treat keyterms only as transcription vocabulary: their presence does not establish canon. Do not scrape the whole vault into a keyterm list.

Let Scribe choose its speaker-ID count by default. The roster supplies vocabulary
and the physical identities the local classifier can assign; it does not set
Scribe's diarization count. Favor pure Scribe IDs over matching the roster count,
because pure IDs can support short-response attribution. Automatic detection does
not guarantee purity; assess that agreement after voice-classifier verification.

## Workspace boundary

Keep every transcription-stage artifact beside the original recording: raw service
JSON, VTTs, manifests, keyterms, speaker samples, embeddings, acoustic reviews,
audits, attribution layers, and reference banks. Never use any Taelgar vault
`_sessions` path as a transcription or speaker-review output directory. The scripts
enforce this boundary and refuse such output paths, including dry runs.

Only `prepare-session-source`, after its separate verification gate, may archive
the finalized identified VTT and its small control files into a vault `_sessions`
bundle. Do not create that bundle early as a convenient workspace.

## External-upload gate

An actual transcription sends the specified audio file and resolved keyterms to ElevenLabs. Before running it:

1. Run `scripts/transcribe_session.py` with `--dry-run`.
2. Show the user the exact audio path, byte size, output paths, expected speaker
   count (or automatic detection), and resolved keyterms.
3. Obtain explicit authorization to upload that file.
4. Add `--confirm-upload` only after authorization.

Authorization for one recording does not automatically authorize other recordings. A dry run never uploads audio and does not require an API key.

On an authorized run, the script first makes and deletes a disposable one-second local sample. If the available media backend cannot extract review clips from the recording, it stops before uploading.

## API key

Never place an API key in the vault, command arguments, generated artifacts, or chat output.

The script resolves the key in this order:

1. `ELEVENLABS_API_KEY` in the process environment;
2. legacy `ELEVEN_LABS_API` in the process environment;
3. either name in a user-supplied `--env-file` outside the vault.

The environment takes precedence over an env file. The env file parser accepts optional `export`, comments, and quoted values without expanding shell expressions. If no key is available, stop before uploading and explain how to set `ELEVENLABS_API_KEY` or pass `--env-file`. Do not inspect or print the key itself.

## Run the script

Use the system Python from the vault root:

```bash
python3 .agents/skills/transcribe-session/scripts/transcribe_session.py \
  "/absolute/path/to/Session-Audio.m4a" \
  --participants "/absolute/path/to/campaign-participants.yaml" \
  --keyterms "/absolute/path/to/campaign-keyterms.txt" \
  --output-dir "/absolute/path/to/transcription-output" \
  --language-code eng \
  --dry-run
```

For the authorized run, replace `--dry-run` with:

```text
--confirm-upload --env-file "/absolute/path/outside-the-vault/.env"
```

`--keyterms` is optional. Use repeatable `--keyterm` arguments only for a small
number of user-supplied additions. With neither speaker-count flag, the script
omits `num_speakers` from the external request. `--auto-speakers` remains an
optional explicit spelling of that default. Pass `--num-speakers N` only for an
explicitly requested fixed count, never merely because the roster has N people.
Use `--force` only after confirming replacement of existing output artifacts.

## Outputs

For `Session-Audio.m4a`, the output directory receives:

```text
Session-Audio.scribe-v2.json
Session-Audio.transcript.vtt
Session-Audio.transcription.json
Session-Audio.speaker-preview.md
Session-Audio.speaker-samples/
```

- Preserve the raw Scribe v2 JSON unchanged.
- Use the VTT as the transcript input for `prepare-session-source`.
- Use the manifest to establish the audio hash, request settings, resolved keyterms, response summary, sample metadata, and output hashes.
- Treat the speaker preview and linked audio excerpts as a diarization audit, not an identity map. The script selects up to three relatively long turns per Scribe ID and extracts short `.m4a` clips using `ffmpeg` or the skill's macOS AVFoundation pass-through helper. Preview samples alone do not justify a global participant mapping. After a verified model-assisted pass, however, a Scribe ID may supply short-cue labels when at least 80% of its durable model-classified cues agree on one participant.
- Never assume a speaker ID is stable across recordings, even when the device is unchanged.

## Speaker attribution

When the user wants participant names or the Scribe IDs are impure, read [references/speaker-attribution.md](references/speaker-attribution.md). The primary task is to classify each substantial audio segment against known people's reference voices. A pretrained ECAPA encoder supplies voice embeddings; reviewed clips supply participant profiles. This does not train a new neural network or assign one person globally to each Scribe ID. The number of participant profiles is independent of the number of Scribe IDs.

Scribe IDs help define segment boundaries. The local classifier assigns one identity per segment; it does not redo diarization or reliably recover a speaker change Scribe missed within a segment. After classifier verification, sufficiently pure Scribe IDs supply only the short-cue fallback described below.

Choose the reference strategy from recording conditions, not campaign identity alone. The bank fast path suits comparable recordings after transfer checks and goes directly to participant verification. A change from Zoom to room recordings, different microphones or speaker distances, or poor verification calls for local calibration and a blind model comparison. Keep concurrent captures separate and initially fit each recording independently.

Use `speaker_recalibrate.py` to recover recording-local reviews while preserving human corrections, prior predictions as comparison evidence, and compatible embedding caches. Prior banks and older identified transcripts can help propose clean anchors and cross-check local predictions; retain their paths, hashes, and disagreements. Anonymous older speaker numbers do not establish participant identities. Do not discard prior work or treat cross-microphone agreement as proof. Materialize local labels with an audited confidence policy; `speaker_model.py apply --compare-reference` keeps bank predictions separate from local assignments and permits weak matches to remain Unknown. See the reference for commands and gates.

When local calibration is needed, gather clean reference clips through acoustic microcluster review and refine only where reference coverage is missing. Verify ten time-spread model samples per person before deriving short-cue labels. After verification, assign short cues from a Scribe ID only when at least 80% of that ID's durable model-classified cues agree on one participant. This is agreement with classifier assignments, not an independently measured accuracy rate. Prefer per-cue model labels, then this qualified Scribe-ID fallback; do not use acoustic cluster labels as final identity evidence. A mixed cluster describes different voices across members, not overlap within every member. Preserve raw JSON and the Scribe-labelled VTT; caches, prior evidence, decisions, audits, model-assisted layers, reference banks, and identified VTTs are separate artifacts.

The identified VTT uses roster `gameRole` values such as `DM` and character names because those are the transcript labels consumed by `prepare-session-source`. Real participant names remain in the participant roster and are recovered there; do not replace that roster identity with the rendered role label.

After a successful run, report the output paths, sample count, response language and probability, detected speaker IDs, cue count, and any warnings. Do not infer real speaker identities without review.

## Multiple recordings

When a session has multiple files, read [references/recording-manifest.md](references/recording-manifest.md). Draft an authored YAML manifest beside the recordings only when the user asks to record the design. Keep sequential chunks from one capture in one ordered track and simultaneous device recordings in distinct tracks. Do not decide which track is primary without evidence or user direction.

Use `scripts/recording_manifest.py` to validate paths, sequence numbers, roles, alignments, hashes, durations, and calculated offsets. Validation without `--output` is read-only. The resolved inventory does not authorize uploading every listed file.

## Boundary

This skill transcribes one audio file at a time, can validate a multi-recording inventory, and can locally attribute already-transcribed utterances to roster participants through reviewed, refinable acoustic groups plus participant-level verification samples. It does not batch-upload a manifest, concatenate sequential chunks, align simultaneous device recordings, merge alternate transcripts, clean ASR errors, create source-prep configuration, or run the session-note pipeline. Continue into those operations only when separately requested and under the applicable skill.

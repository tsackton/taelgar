---
name: transcribe-session
description: Transcribe local RPG session recordings with ElevenLabs Scribe v2, using the campaign roster and reviewed setting keyterms, then audit or correct unreliable diarization through local cluster-level speaker review. Also inventory ordered chunks and alternate capture tracks. Use for first-pass session transcription and speaker attribution; stop before transcript cleanup or session-note preparation unless separately requested.
---

# Transcribe Session

Create a reproducible first-pass transcript from one local recording. Use the deterministic script in this skill; do not use older transcription helpers elsewhere in the repository.

## Required inputs

Resolve and verify:

- the exact local audio file;
- the campaign participant roster YAML;
- the expected number of speakers, normally inferred from that roster, or an
  explicit choice to let Scribe v2 detect the count automatically;
- an optional UTF-8 keyterm file containing one reviewed campaign or world term per line;
- an explicit transcription workspace beside the original recording, normally
  `<recording-directory>/transcription/scribe-v2/`;
- whether the user has authorized uploading this exact recording to ElevenLabs.

Search campaign and session records before proposing world keyterms. Character and player names come from the participant roster. Treat keyterms only as transcription vocabulary: their presence does not establish canon. Do not scrape the whole vault into a keyterm list.

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
number of user-supplied additions. Use `--num-speakers` only when the roster size
is not the correct expectation. Use `--auto-speakers` when the user explicitly
wants Scribe v2 to choose the count; this omits `num_speakers` from the external
request. Use `--force` only after confirming replacement of existing output
artifacts.

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

When the user wants participant names or the Scribe IDs are impure, read [references/speaker-attribution.md](references/speaker-attribution.md). For the first recording without a trusted reference bank, use local acoustic microcluster review rather than asking the user to label every utterance. Once verified reference clips exist, use the reference-bank fast path: embed durable cues, classify them from the bank, and ask for ten time-spread samples per person. After verification, assign short cues from a Scribe ID only when at least 80% of that ID's durable model-classified cues agree on one participant. Prefer per-cue model labels, then this qualified Scribe-ID fallback; do not use acoustic cluster labels as identity evidence. A mixed cluster means the cluster contains more than one voice across its members, not that every member is overlapping speech. Treat the bank as a seed rather than permanent truth because microphone and room conditions can change. Preserve the original raw JSON and Scribe-labelled VTT unchanged; embedding caches, attribution decisions, model-assisted and Scribe-fallback layers, verified reference clips, and the identified VTT are separate artifacts.

The identified VTT uses roster `gameRole` values such as `DM` and character names because those are the transcript labels consumed by `prepare-session-source`. Real participant names remain in the participant roster and are recovered there; do not replace that roster identity with the rendered role label.

After a successful run, report the output paths, sample count, response language and probability, detected speaker IDs, cue count, and any warnings. Do not infer real speaker identities without review.

## Multiple recordings

When a session has multiple files, read [references/recording-manifest.md](references/recording-manifest.md). Draft an authored YAML manifest beside the recordings only when the user asks to record the design. Keep sequential chunks from one capture in one ordered track and simultaneous device recordings in distinct tracks. Do not decide which track is primary without evidence or user direction.

Use `scripts/recording_manifest.py` to validate paths, sequence numbers, roles, alignments, hashes, durations, and calculated offsets. Validation without `--output` is read-only. The resolved inventory does not authorize uploading every listed file.

## Boundary

This skill transcribes one audio file at a time, can validate a multi-recording inventory, and can locally attribute already-transcribed utterances to roster participants through reviewed, refinable acoustic groups plus participant-level verification samples. It does not batch-upload a manifest, concatenate sequential chunks, align simultaneous device recordings, merge alternate transcripts, clean ASR errors, create source-prep configuration, or run the session-note pipeline. Continue into those operations only when separately requested and under the applicable skill.

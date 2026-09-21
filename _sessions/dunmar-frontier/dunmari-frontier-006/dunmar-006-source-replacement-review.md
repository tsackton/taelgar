# Session 006 source replacement — approved and completed

The user approved the replacement, and prepare-source completed successfully on 2026-09-11. All 3,951 prepared units were retained. Contextual cleanup is in progress; see the cleanup progress file for the reviewed range and unresolved phrases.

All six speakers have ten confirmed samples. This configuration replaces the legacy Zoom prepared source with the verified Scribe transcript. The campaign, roster, real-world date, and in-world date range are unchanged. Unknown speakers remain Unknown.

The old bundle, including the partial cleanup and your corrections, has been copied and hash-verified at:
`/Users/tim/Documents/RPGs/sessions/recordings/dunmar/zoom/Session 6/transcription/scribe-v2/source-prep-backups/dunmari-frontier-006-before-scribe/`

A read-only preflight passed: 3,951 prepared units with every transcript passage preserved. The expected warning is 117 Unknown speaker labels (2.96% of cues, 1.32% of transcribed speech).

## Complete source configuration

`/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmar-006-scribe-source-prep.yaml`

```yaml
sourcePath: /Users/tim/Documents/RPGs/sessions/recordings/dunmar/zoom/Session 6/transcription/scribe-v2/dunmari-frontier-006-identified.vtt
sourceAudioPath: /Users/tim/Documents/RPGs/sessions/recordings/dunmar/zoom/Session 6/dunmari-frontier-006-audio.m4a
sourceType: transcript
scope: session
outputDir: /Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier
campaign: Dunmari Frontier
sessionNumber: 6
realWorldDate: '2020-08-06'
drStart: '1748-04-04'
drEnd: '1748-04-06'
drStartTime: null
drEndTime: null
participantsPath: /Users/tim/Documents/RPGs/sessions/recordings/dunmar/zoom/Session 6/transcription/scribe-v2/dunmari-frontier-006-participants.yaml
supplementalSources: []
transcriptFormat: vtt
narrativeUnit: sentence
minSpeakerFraction: 0.01
```

## Complete speaker mapping

`/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmar-006-scribe-speaker-mappings.json`

```json
{
  "Kenzo": ["Kenzo"],
  "Wellby": ["Wellby"],
  "Delwath": ["Delwath"],
  "Seeker": ["Seeker"],
  "Riswynn": ["Riswynn"],
  "DM": ["DM"]
}
```

## Approved command executed

```sh
cd /Users/tim/RPGs/taelgar-utils
PYTHONDONTWRITEBYTECODE=1 /Users/tim/.local/miniforge3/envs/taelgar-utils/bin/python cli/session.py prepare-source \
  --config "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmar-006-scribe-source-prep.yaml" \
  --speaker-mappings "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmar-006-scribe-speaker-mappings.json" \
  --force
```

This command replaces only the existing session manifest, prepared source, and speaker statistics in the bundle's `cleaned/` directory, and archives the four new input/control files in `sources/`. The old archived Zoom files remain. Contextual cleanup is being regenerated from the new prepared source, preserving the earlier work in the verified backup.

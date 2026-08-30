# Session Recording Manifest

Use a recording manifest when one game session has sequential chunks, simultaneous recordings from different devices, or both. Keep the authored YAML beside the recordings. It is an inventory and timing model, not a transcript or a `_sessions` source bundle.

Keep the resolved JSON beside the authored manifest as well. The validator refuses
an output path under any vault `_sessions` tree.

## Schema

```yaml
schemaVersion: 1
campaign: Dunmar Frontier
sessionNumber: 135

tracks:
  - trackId: tim
    role: primary
    recordedBy: Tim Sackton
    parts:
      - sequence: 1
        path: raw_audio/Session135-Tim-Chunk-01.m4a
        gapBeforeSeconds: 0
      - sequence: 2
        path: raw_audio/Session135-Tim-Chunk-02.m4a
        gapBeforeSeconds: 0

  - trackId: kong
    role: alternate
    recordedBy: David Kong
    alignment:
      referenceTrackId: tim
      offsetSeconds:
    parts:
      - sequence: 1
        path: raw_audio/Session135-Kong-Chunk-01.m4a
        gapBeforeSeconds: 0
```

Paths may be absolute or relative to the authored manifest. The order of `parts` is authoritative and `sequence` must be consecutive from 1.
Unknown fields are rejected so a misspelled timing or role field cannot be silently ignored.

## Track roles

- `primary`: the selected session track; at most one track may be primary. Its timeline offset is zero.
- `alternate`: a simultaneous or substitute capture that is not the default transcript source.
- `candidate`: a capture whose eventual primary/alternate role has not been decided.

Do not label a track `primary` merely because its filename appears first. When no selection has been made, leave all plausible tracks as `candidate`.

## Timing

`gapBeforeSeconds` records a known gap between sequential parts of the same track. It must be zero on the first part.

For a simultaneous track, `alignment.referenceTrackId` identifies the comparison track. `alignment.offsetSeconds` is the start of this track relative to the reference:

- positive: this track begins later;
- negative: this track begins earlier;
- blank: alignment remains unresolved.

Do not invent an alignment offset. Resolve it later from reliable recording timestamps, audio correlation, or confirmed shared events.

Session-relative starts are calculated only when the reference chain reaches the primary track. A relative offset between candidate tracks remains useful inventory data, but it does not establish a session timeline until one track is selected as primary. Circular reference chains are invalid.

## Validation

Validate and print the normalized inventory without writing:

```bash
python3 .agents/skills/transcribe-session/scripts/recording_manifest.py \
  "/absolute/path/to/session-recordings.yaml"
```

Optionally write a resolved JSON inventory containing absolute paths, byte counts, hashes, probed durations, track-relative starts, and session-relative starts when alignment is known:

```bash
python3 .agents/skills/transcribe-session/scripts/recording_manifest.py \
  "/absolute/path/to/session-recordings.yaml" \
  --output "/absolute/path/to/session-recordings.resolved.json"
```

The normalized inventory does not combine audio or transcripts. Batch transcription, alignment, source selection, and final transcript merging remain later operations.

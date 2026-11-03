Session-pipeline JSON Schemas live here.

These schemas document source-preparation artifacts and retained legacy session artifacts:

- `session-manifest.schema.json`: `session.yaml` from `prepare-source`
- `speaker-stats.schema.json`: `speaker-stats.json` from `prepare-source`
- `normalized-transcript.schema.json`: `*.normalized.json` from `taelgar_utils.session.normalize`
- `cleanup-report.schema.json`: `<prefix>-cleanup-report.json` from `report_cleanup_diff.py`
- `session-corrections.schema.json`: `<prefix>-session-corrections.yaml` from `report_cleanup_diff.py`
- `beats.schema.json`: legacy `<prefix>-beats.json`
- `beat-facts.schema.json`: legacy `<prefix>-beat-facts.json`

The beat/recap authoring workflows have been retired. Their schemas remain to describe existing artifacts used by legacy consumers.

The YAML artifacts are listed here because JSON Schema can validate YAML data models too.

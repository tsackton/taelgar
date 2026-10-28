# Plan, audit, and rollback contract

`schemaVersion: 1` and `passVersion: names-v1` are required. Change these versions deliberately when changing the interpretation or decision/report contract; a later version must not silently accept incompatible plans or journals.

## Plan schema

Every field shown is required, including empty arrays/maps. Additional fields are rejected. A plan has exactly `schemaVersion`, `passVersion`, `transcriptSha256`, and `groups`. A group has exactly `id`, `action`, `confidence`, `reason`, `evidence`, `candidates`, `markerIds`, and `replacements`.

```json
{
  "schemaVersion": 1,
  "passVersion": "names-v1",
  "transcriptSha256": "COPY-FROM-CURRENT-SCAN",
  "groups": [
    {
      "id": "skyship",
      "action": "replace",
      "confidence": "supported",
      "reason": "The characters are boarding their named skyship; the reference note establishes its spelling.",
      "evidence": ["Things/Ships/Vindristjarna.md"],
      "candidates": [],
      "markerIds": [],
      "replacements": {
        "u0042:m1": "Vindristjarna",
        "u0109:m2": "Vindristjarna"
      }
    },
    {
      "id": "statue-subject",
      "action": "review",
      "confidence": "unresolved",
      "reason": "The founder is plausible, but the inspected sources do not identify this statue.",
      "evidence": ["People/Orcs/Uzgash.md"],
      "candidates": ["Uzgash"],
      "markerIds": ["u0200:m1"],
      "replacements": {}
    },
    {
      "id": "ordinary-wording",
      "action": "leave",
      "confidence": "not_applicable",
      "reason": "Ordinary wording and mechanics outside the name pass.",
      "evidence": [],
      "candidates": [],
      "markerIds": ["u0109:m1", "u0301:m1"],
      "replacements": {}
    }
  ]
}
```

- `id`: unique lowercase slug within this session. Separate groups if confidence differs between occurrences.
- `replacements`: exact current marker IDs to complete replacement strings. No braces, links, annotations, line breaks, control characters, or leading/trailing whitespace. Correct capitalization can differ by occurrence.
- `markerIds`: the review/leave occurrences; empty for replacement groups.
- `evidence`: existing vault-relative file paths. Required for replacement groups; optional otherwise. The helper captures exact source hashes. Archived bundle `sources/` files are rejected. A glossary or session config can be evidence; known facts in a transcript are subordinate to authoritative sources for preferred spelling. Naming judgment cannot be delegated to a string-matching script.
- Every current marker appears in exactly one group, including every duplicate on a line. The helper rejects omissions, duplicates, unknown IDs, stale transcript fingerprints, and unknown schema fields.
- `candidates` contains display-only possibilities for review, not instructions to apply them.
- No plan or report field may contain private DM excerpts. References to source paths are sufficient for provenance. The journal already preserves the original shared transcript lines needed for rollback.

## Files created by apply

For each marker-positive run, the helper creates:

```text
cleaned/cleanup-artifacts/automatic-transcript-cleanup/<UTC-time>-<unique-id>/
  journal.json
  review.md
  changes.diff
```

The parent `.lock` serializes this helper's mutating operations. Do not remove it while a run is active. It does not prevent Obsidian or an unrelated editor from changing the source; fingerprint rechecks reject detected conflicts.

`journal.json` is the rollback authority. It contains the exact original and resulting changed lines (including line endings), marker IDs and offsets, every old marked span/new string, confidence/reason/group, retained decisions, evidence paths/hashes, before/after transcript hashes, version, run identity, state, and reversion events. It captures the actual working file, including pre-existing user edits. It does not need a clean Git tree or a baseline commit.

`review.md` is the fixed marked log for human review. It retains the original `{{...}}` wording, so completed corrections remain inspectable. `changes.diff` is a display diff grouped by UID; it is not a repository-wide patch and is not the undo mechanism. Original replacement rows remain visible after undo, labeled reverted. Never remove rejected rows or their original values.

The journal is persisted before the transcript changes. Writes are atomic per file, with file/directory flushes. Multiple files do not form a filesystem-wide atomic transaction; pending states plus `recover` handle interruptions. A failure must be recovered, not reported as completed. New runs get new directories, preserving earlier evidence.

## Undo

Undo an entire run:

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo \
  --journal 'PATH-TO-RUN/journal.json'
```

Undo specific occurrences, including only one of two identical replacements:

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo \
  --journal 'PATH-TO-RUN/journal.json' \
  --marker-id 'u0042:m1' --marker-id 'u0109:m2'
```

Undo restores original braces and wording, records the decision, and regenerates review files. It preserves edits on other lines. If a selected line has since changed, the entire selected undo is refused without changing the transcript; inspect that conflict manually. This conservative refusal also applies when a later name pass changed another marker on the same line. Prefer reverting later runs first. Repeating an already completed undo is a no-op.

The counts in a run's report describe its original source plus its own recorded reversions. Other subsequent edits are excluded; use a fresh scan for actual current counts.

## Recovery and reports

```bash
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py recover \
  --journal 'PATH-TO-RUN/journal.json'

python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py report \
  --journal 'PATH-TO-RUN/journal.json'
```

Recovery never guesses new content or writes the transcript. If the current file matches a pending transaction's recorded before or after hash, it records whether the write completed and regenerates the display files. If neither matches, it refuses and preserves both the journal and source for inspection. This includes interrupted selective undo. A completed journal can also regenerate missing/stale display files via `recover`; `report` only prints without writing.

All commands support `--vault-root`. Paths must resolve inside that vault. Only cleaned source transcripts under `_sessions` are writable. Existing journals must live beside the transcript they describe. No Git commands are run by the helper.

## Format and resumption

The helper renders these sections, always in this order:

1. Session, status, pass version, fixed count table.
2. Applied replacements, one row per occurrence; original marker, replacement, group, confidence, reason, evidence, reversion status.
3. Name decisions left for review, grouped with all occurrence IDs and originals.
4. Outside this pass, grouped with all IDs, not mislabeled human-review requirements.
5. Reversion.
6. Provenance.
7. Downstream artifacts.

Do not have the agent compose a replacement log by hand. Structural format is deterministic; reasons and entity judgments remain source-dependent. Batch output uses the fixed table in `SKILL.md`. Keep semantic policy **names-v1** consistent across sessions and continuation turns.

Generate that batch table with `summary --manifest /tmp/name-pass-manifest.json --journals JOURNAL-PATH ...`. The manifest is the saved `batch` JSON, restricted to the requested scope when necessary. Alternatively use `--campaign-root` to build a fresh manifest. Supply only the completed run journals for the current invocation; resumed rows remain visible without duplicating their totals. A pending `ready` row means the requested batch is still incomplete.

The batch manifest reports marker-free, missing, ambiguous, blocked, ready, recovery-required, and already-reviewed-current files. `reviewed_current` checks the latest completed journal against current source/evidence hashes and this helper version; it is a resume hint for the same batch, not a claim that all future lore discoveries are irrelevant. A fresh review can revisit unchanged files. Do not reuse old marker ordinals after edits.

# Testing process-transcript

Run from the vault root, with bytecode writes disabled:

```bash
PYTHONPATH=.agents/skills/process-transcript/scripts python3 -B -m unittest discover -s .agents/skills/process-transcript/tests -p 'test*.py'
```

The real-bundle regression is opt-in. It copies each selected bundle into a new
temporary directory, normalizes only that copy, and compares all live file hashes
before and after. Run it together with the behavioral suite:

```bash
TRANSCRIPT_TEST_VAULT="$PWD" PYTHONPATH=.agents/skills/process-transcript/scripts python3 -B -m unittest discover -s .agents/skills/process-transcript/tests -p 'test*.py'
```

The behavioral suite checks incomplete-work gates, word preservation outside explicitly mapped display substitutions,
repetitions/false starts, uncertainty, annotations, numerical notation, character
coverage, speaker overlays including within-UID splits, cross-chunk continuity,
neighbor-review invalidation, human-decision invalidation, manual export changes,
resumption, interrupted writes, dependency conflicts, source-format adapters,
path/symlink restrictions, independent session locks, and removal/regeneration of
optional display/review views without losing retained references or pending review. Finalization tests cover permanent prepared-text retention, minimal remaining files, metadata/comment preservation, speaker overrides, review gates, edited references, interrupted retirement, symlinks, and idempotent completion without recreating state.
A child-process audit hook observes filesystem writes across an entire processing and finalization run and rejects any
write outside that session's bundle. Substitution tests cover intact surrounding
words, valid labels and spans, overlapping/invalid ranges, protected review markers
and annotations, cross-chunk joins, and finalization with unchanged source text.
Review tests require actual proposals and questions, exclude incidental queues,
and invalidate old work when the editorial policy changes.

Attribution-order regressions reproduce adjacent clean chunks alternately becoming
stale when unchanged overlays move within storage. Fingerprints must ignore that
ordering for clean, polish, and quality, while still changing for revised speakers,
spans, reasons, or evidence. Existing checkpoints need a separate read-only status
assessment under the fixed helper; tests must not silently replace their hashes.

## Initial evaluation, 2026-10-28

26 tests passed, including temporary-copy checks for seven bundles across the six
campaigns with transcript bundles:

| Copied bundle | UID units |
| --- | ---: |
| Dunmari Frontier 53 | 531 |
| Dunmari Frontier 139 | 5,642 |
| Dragonets 2 | 2,659 |
| Lost in the Feywild 4 | 2,542 |
| Into the Chasm 1 | 2,254 |
| Labyrinths of the Lost 1 | 2,113 |
| Mawar Adventures 2 | 3,597 |

Those checks preserved existing cleaned wording, archived input, stable headers,
and unrelated historical artifacts; inspected legacy excerpt candidates where
present; resumed idempotently; and confirmed unchanged live bundles. They do not
constitute a semantic cleanup of all seven sessions.

A separate full editorial pilot on the **temporary Session 53 copy** completed all
four cleanup, polish and quality jobs. It produced 202 readable turns with exact
coverage of all 531 source units and 295 quoted entity/time mentions. Three source
lines changed (two name-capitalization fixes and one contextual ASR repair); one
speaker correction was recorded without rewriting source headers. The separate
reading pass found and corrected punctuation/capitalization defects in initial
merges. The standalone HTML was visually inspected.

The first review incorrectly counted four fact/grammar-only flags as recognition
uncertainty. Following the user's scope correction, these were reassessed and
unmarked without changing any spoken words: a distance/direction claim, an awkward
geographical question, competing dates, and a grammatical phrase about sunrise.
These four removals are **flag reclassification, not ASR recovery**. The review
rules now explicitly exclude factual validation and awkward speech alone.

The corrected pilot retains nine material transcription issues in eight groups,
five incidental marked spans, and one incidental unmarked issue. It remains
`needs_manual_review`; no human acceptance was fabricated. All 531 unit word
sequences were unchanged during this reassessment. This is a fidelity/readability
pilot against the existing transcript, not verification against audio. Mechanical
checks cannot certify that an agent has correctly distinguished a recognition
problem from a spoken mistake; that remains an explicit editorial review task.

## Finalization evaluation, 2026-10-28

The expanded suite passed all 32 tests, including the seven copied-bundle checks.
A completed synthetic session retained exactly four transcript files and session
metadata; finalization preserved the prepared transcript byte-for-byte and kept
speaker overrides in metadata. Interrupted finalization resumed with the bundle
lock still effective after work-directory removal. The temporary Session 53 pilot
correctly refused finalization while its nine material issues remained pending;
its file hashes were unchanged. No live session was processed or finalized.

## Markdown review regression, 2026-10-28

The updated suite passes 53 tests, including the opt-in checks on temporary copies
of seven now-finalized live bundles. Those checks verify current retained hashes
and that initialization recreates no work state; live files remain unchanged.

New review regressions remove the original work directory and disposable exports,
then apply decisions using only the review Markdown and retained references. They
cover exact target boundaries and preserved suffix/neighbor speech, larger and
explicit context ranges, partial decisions with shifted offsets, retained
uncertainty, stale references, missing/unfaithful readable-turn updates, split
speaker bounds, garbled recovery, prohibited hiding of accepted words, confined
paths/writes, metadata-comment preservation, and interrupted application/recovery.
The runtime write audit now exercises bounded reopening, application, and
finalization as well as initial processing. The skill metadata validator passes.

Editorial policy 3 invalidates active work reviewed under the old free-form
proposal contract. Finalized references remain current; a new bounded review uses
their retained files. A portable Markdown handoff does not inherit the original
queue's lifetime or depend on its presence. These mechanical tests establish safe
application and recovery, not that a model finds every recognition error; the
editorial calibration examples in [review.md](review.md#editorial-calibration)
address that separate judgment.

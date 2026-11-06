# Dragonets 001 extraction validation

The eight package products are complete: time markers, location markers, entity map, interactions, segments, combat, structured-data review, and grouped time watches. This file records execution and validation evidence.

## Checkout and source scope

- Initial main commit: `a08c526f3a98c97a1f7eb2d786f5e9a515d49241`, fetched and pulled before reading package instructions.
- The four independent products were committed as `d66ac677b4128b7c670cba3fdbd16f1065ca8409`.
- Continuation started after fetching and pulling main at `c3df02368eb04d29fc0b0fc5c572e3131d2b81fb`. Applicable instructions and package files had not changed.
- The registered polished source was read completely in order: 1,158 turns covering all 2,203 UIDs. Shared-UID groups were preserved.
- The dedicated combat pass reread all of finalized segment s005, u1240–u1380, from original polished wording. It contains one nonlethal call-and-response encounter, two resolved rounds, and seven action/event entries.
- A distinct semantic pass reviewed all entity inclusions, exclusions, importance, identity evidence and vault matches. A second source pass checked each selected interaction range and its five-line neighbors, including every cut. No human-reviewed status was authored.
- No earlier Dragonets session exists to supply a prior entity map. Later-session maps and transcripts were not used to establish this session’s identities.

## Temporary date adapter

The manifest stores literal `unknown` for `drStart` and `drEnd`. The installed permissive source loader accepts null dates, but rejects those legacy strings. The continuation explicitly authorized an in-memory compatibility adapter.

The temporary adapter, `/tmp/dragonets001_adapter.py`, applies only to this exact session manifest, only when `allow_unknown_dates=True` and `for_draft=False`. During the installed `interaction_draft.load` call it substitutes that module’s YAML reader with a wrapper that maps only those two literal strings to None. It restores the module reference in a finally block. It then restores the returned bundle’s complete original manifest data before scene/entity helpers compute their input digests.

The manifest bytes are never rewritten. All other load arguments, installed source checks, UID checks, validators, source-change handling, concurrency guards, human-review protections and guarded writes are unchanged. The adapter checks the five protected files below before and after each adapted load and after command completion. Each registered artifact’s SHA is checked against its manifest registration. It asserts that the loader retains the original byte fingerprints. No date is invented; `realWorldDate` remains recording metadata.

The final check independently recomputed the canonical session-metadata digest from the original parsed manifest and compared it with the bundle and persisted entity map. The guarded entity input digest remained `a1f71704937fb5dae630f13d8f689e2acb2e9f0a0d4060a4374be011fb33e340`. A strict load with `allow_unknown_dates=False` was also checked and still rejects `unknown`, demonstrating that the ordinary strict validation path was not weakened.

| Protected bundle-relative file | Original and final SHA-256 |
| --- | --- |
| cleaned/dragonets-001-session.yaml | `6068525fceba05d6a9888e60b9d198c1839d433f32cdac49fbce14f7bb38731d` |
| sources/GMT20260918-010103_Recording.transcript.vtt | `dfb5aa90b305151ca96e1b9b3bd7bd672b8b717d65994f006ab6027574b31650` |
| cleaned/dragonets-001-source-prepared.md | `28fdf5fec740848bc6aa69e2f393fb9707a7f98191ebabf934f38594fccf611d` |
| cleaned/dragonets-001-source-cleaned.md | `54b423f16aea1878662c35495984a17b6fe339ab8a7ca4d088ab52fdd77edb20` |
| cleaned/dragonets-001-transcript.md | `273771a9ea93effe06e614f7847747925a8895c37398e75764e97a90d316532a` |

The adapter is temporary and is not installed or committed. The audit log is `/tmp/dragonets001-adapter-audit.jsonl`; the final machine-readable results are `/tmp/dragonets001-final-check-results.json`. Until registration is repaired separately, ordinary CLI loads still need the same narrowly scoped compatibility treatment.

## Commands requiring the adapter

These installed scripts ran through `python3 -B /tmp/dragonets001_adapter.py SCRIPT ...`:

- `.agents/skills/check-session-entities/scripts/entity_map.py`: `inspect` with every chosen/candidate/supporting note, guarded `save --proposal ... --expect-input-digest ...`, and `validate`.
- `.agents/skills/extract-entity-passages/scripts/interactions.py`: `context --session-yaml ... --start-uid ... --end-uid ...` for all 16 saved ranges, and `validate` on the saved interaction JSON.
- `.agents/skills/extract-session-structure/scripts/render_review.py`: `--prepare` and `--editorial`, using fresh input/output snapshots after the location qualifications changed.

The temporary interaction builder/reviewer and final checker also installed the same adapter before calling the unchanged helpers’ read-only APIs. The entity map itself was written only through its installed guarded save. The review and watch JSON were written only through the installed renderer.

## Validation results

- Entity validator: 33 entities, nine chosen note matches, two stars, five supporting entities, 26 cameos and 12 meaningful exclusions. The three medium-confidence entity decisions remain qualified.
- Interaction validator: 16 coherent exchanges, current source/map fingerprints, valid entity references, complete UID/span accounting, and exact deterministic before/after context.
- Verbatim checks: 371 unchanged retained turns, nine inline-cut turns checked with the owning `match_inline` helper, and 20 merged omission blocks. Retained wording, speaker labels and uncertainty markers are source-exact.
- Time/location/classification/combat checks: required fields and allowed values, original source hashes, exact quotations, whole/shared-UID boundaries, source order, unique IDs, quantity bounds, reference integrity, containment cycles, full segment coverage, and complete combat-segment coverage. The installed location checker and recording-time function passed.
- Review verification: all ten time markers appear exactly once in six watch rows; the vision’s night sky retains an open local civil watch. No calendar dates or overnight rest were supplied. Physical presence is separate from observations and the visionary journey. Played stops have separate rows. All seven star/supporting entities have individual rows, with no cameo promotion.
- The rendered review bytes were reproduced exactly from the saved editorial snapshot and linked inputs. The watch JSON’s source fingerprint matches the saved time-marker file.
- Package tests, without the adapter: `extract-session-structure` 36 passed; `extract-entity-passages` 15 passed; `check-session-entities` 85 passed. Total: 136 passed.

Recording endpoints are 00:00:09.090–03:04:45.200, an extent of 03:04:36.110. Segment elapsed time totals 03:04:32.928; speaking time totals 02:39:49.547. Gaps between segment spans total 3.182 seconds. One millisecond of overlapping utterance timestamps is counted once. Elapsed and speaking shares use their own totals; full audio-file duration is not established.

The four human actions retained in the [structured-data review](dragonets-001-structured-data-review.md) concern the scolding cloud’s inclusion, the distant object’s possible identity with the egg, the dying dragonet’s Dimitaur candidate, and the conflicting Bardic Inspiration statements. They are not automatically resolved by these checks.

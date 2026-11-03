# Full-read protocol and local format additions

This follow-up uses the two draft skills in the parent directory as extraction guidance. It keeps all new data, helper code and reviews here. The original five-session maps remain a separate pilot.

## Read procedure used

1. Draw two new eligible manifests without replacement, excluding the original five; save seed, complete eligible frame, selected source paths and hashes.
2. Freeze the keyword hit set before full reading. This is a candidate-selection baseline, not an independent semantic annotation.
3. Verify parser inventory accounts for every non-whitespace character in the transcript body, excluding only heading/source-map presentation. Read header/status separately. Polished paragraphs, uncertainty markers, speakers and shared UID turns stay intact.
4. Print bounded, unfiltered windows in source order. Read all text, including combat, lore and chatter. Record coverage only after the window has actually been inspected. Reread any truncated window; do not mark it complete just because it was requested.
5. Author sparse time and location evidence. Significant spatial thresholds and split actors matter; tactical five-foot movement usually does not. Nonadvancing lore/plan/table examples are included where they demonstrate a likely false positive, not as an exhaustive historical timeline.
6. Derive dates conditionally from YAML start and transcript-supported transitions. Keep YAML end as a claim to check. Compare current-span nights, literal boundary-prologue nights and planned rests separately.
7. Build ledger and graph views, validate exact evidence and referential consistency, then review the interpretations. Do not call structural validation a semantic gold standard.

## Local version 0.2 additions

The parent `format.md` remains the main contract. The follow-up uses `schemaVersion: 0.2-full-read-experiment` with these additions/clarifications:

- `review.coverage`: actual turn count, inspected windows and completion flag. The provenance block still owns source and YAML fingerprints. Coverage documents reading, not perfect extraction recall.
- Time audit: `openingBoundaryOvernights` and `literalNarrativeDateBoundariesIncludingOpening` may distinguish narrated boundary framing from the current action. `supportedDateBoundaries` continues to count only constraints included in the main span.
- Location B `reportedLocations`: reported past presence/routes retained without physical party visits.
- Location B `observations`: includes `observed_presence` for remotely witnessed NPCs. The observer and observed entity should be distinct actors in separate evidence rows when needed.
- Journey completion `accepted_compressed_return`: an explicitly accepted hand-wave establishing return, with no invented detailed route or room. Confidence can reflect the compression.
- Planned/canceled moves remain outside physical journeys/visits. Session 24’s departure next session and Session 39’s archives cancellation are examples.
- A spatial site can encompass a tower, its entrance and immediate camp when exact indoor occupancy is unclear. A separate interior child node is used for the witnessed chamber. This avoids falsely placing all combatants inside a building.
- `alternativeReadings`, `countGroup`, `concurrencyGroup` and notes preserve uncertainty and overlap. These are annotations, not an implemented interval solver.

All place IDs here are local labels. No source-independent identity reconciliation was attempted. The experiment does not publish canonical NPC whereabouts.

## Rebuild and limits

From the vault root:

```bash
python3 -B _sessions/time-location-testing/full-read/author_024.py
python3 -B _sessions/time-location-testing/full-read/author_039.py
python3 -B _sessions/time-location-testing/full-read/build.py
```

The authoring files contain manual semantic decisions. Running them or the renderer does **not** reread the transcripts, perform a new extraction, or justify updating full-read coverage. `build.py` consumes the existing coverage record, validates it against source turn counts and produces the eight JSON maps, two reviews, citation-selection comparison and validation result. Hash guards reject changed sources.

`inspect.py SESSION full FIRST LAST` displays complete source windows; `inventory` checks parser accounting. The sampling and frozen candidate baseline are records of this run, not generated on each rebuild.

Future independent calibration should compare two independently authored extractions against an adjudicated reference, tracking false positives as well as omissions. This experiment measures citation-selection coverage only. Expanding context recovered at least one cited turn for every authored marker at ±5 turns, but that does not establish complete semantic extraction. No process-time or token-cost benchmark was recorded, so no cost-efficiency claim is made.

---
name: extract-time-markers
description: Extract sparse in-world time markers from a registered polished session transcript, preserve UID evidence, reconstruct relative chronology, and compare elapsed date boundaries with session YAML. Does not assign every line a time or edit session dates.
---

# Extract time markers — experimental draft

This uninstalled prototype was developed from five Dunmari Frontier sessions. Read [the shared experimental contract](../../format.md) before authoring. The user's current instruction confines every generated file to `_sessions/time-location-testing`; do not install this skill or write into live bundles during the experiment.

Resolve the existing session YAML and its registered polished transcript. Record source/YAML fingerprints before reading. Preserve source-local UIDs and whole polished-turn mappings; session + source revision + UID identifies evidence. Do not substitute a recap or use recording runtime as world time.

Read the transcript in source order for date and clock anchors, time-of-day cues, completed rests, sleep/waking, explicit elapsed intervals, compressed journeys, and frame changes. Candidate searches help locate evidence but are not an exhaustive semantic review; include numeric clocks such as a bare “6:00.” Read surrounding speech to distinguish an accepted action from a plan, a spell's possible duration from time actually spent, and present play from history, visions, table conversation, or flashbacks. Be explicit about any limited reading scope.

Author a **time A evidence ledger** before deriving chronology. Keep exact quoted evidence separate from interpretation. Preserve self-corrections and materially conflicting statements. A later comment can confirm an earlier rest without creating another rest. Use the user's one-hour short-rest/eight-hour long-rest conventions as labeled assumptions; overnight does not equal exactly eight hours, and rest does not inherently advance the date.

Build **time B sparse chronology** with relative anchors and evidence-backed constraints. Reorder flashbacks only in this derived view; the ledger stays in source order. Carry dates forward only through supported continuity. Separate a spoken month/day from a YAML-supplied year. Keep vague quantities vague. Treat simultaneous study/rest, split-party errands, and umbrella montage descriptions as overlapping; do not sum nested intervals. Preserve local-clock changes on teleport without inventing geographic offsets.

Compare YAML start/end claims with the transcript independently. Count calendar boundaries, including those contained in a multi-day montage, and distinguish them from individually narrated nights. Report supported, compatible-relative, underdetermined, or conflicting evidence. Do not infer the missing nights from `drEnd` and then claim those nights validate it. If the main session day includes a prior-night retcon, explain the coverage convention rather than silently changing YAML.

Recheck each actual advance, both ends of jumps, final bedtime/departure framing, and any conflict in original speech. Verify source hashes, quotation membership, UID boundaries, and references. A structural check cannot certify semantic completeness. The five-session `build_review.py` is a pilot projection/validation tool, not a general extractor for arbitrary new sessions.

Deliver both JSON views and a table of date/time, claim, evidence, and UID, with the YAML audit and crucial uncertainties first. Keep unresolved observations useful without stopping over incidental wording. Preserve human corrections when revising; changed evidence requires rechecking dependent chronology. Do not edit YAML, transcripts, canonical dates, installed skills, or later timeline outputs unless separately requested.

---
name: extract-time-markers
description: Extract sparse markers for when gameplay happens, elapsed in-world time, and shifts in narrated time. Preserve transcript evidence, check session dates, and present a review table.
---

# Extract time markers

Create a marker when the table establishes **when something happens in play**, **how much in-world time passes**, or **a shift to an earlier or later point in play**. Identify the played event or interval each marker dates or measures. Leave the time of other gameplay open. A session can have few markers or none.

Read [the format and calibration examples](references/format.md). Resolve the existing session YAML and its registered polished transcript, fingerprint both, and read the complete transcript sequentially in manageable windows. Preserve whole polished-turn UID mappings. Reread truncated passages. Search can supplement this read. For comparison trials use a separate output directory and preserve existing runs. Otherwise use the bundle's `cleaned/<stem>-time-markers.json`.

## Decide from the surrounding play

- **Anchors and advances.** Keep a narrated dawn, an answer to “what time is it now?”, a minute actually spent searching, a night at camp, or days spent traveling. A short duration qualifies when the table establishes that it passed. Ordinary speech rhythms (“wait a minute”), visible gestures, and the sequence in which checks are rolled provide no timing by themselves.
- **Recollections and forecasts.** Ask what the time expression measures. An NPC's account of an eight-hour ride can explain the distance to an oasis. The time given for the roadside meeting anchors the conversation. Reaching an estimated destination later confirms arrival. Use the estimate for elapsed time only if the table also confirms how long the actual trip took. A PC's dream history can explain recognition on arrival. Exclude such background from both markers and the YAML span. An estimate or spell duration can support elapsed time when play independently establishes the relevant timing, for example when the full spell expires during scouting.
- **Nonlinear play.** Follow the table when it plays out or resolves earlier events. Mark an established shift and the identifiable return even without a clock reading. Preserve the anchor for the scene the table opens on. Keep a vision's local timing separate from elapsed adventure time.
- **Split parties.** Scope each marker to the actors it dates. A time established for one group supplies no timing for another. When the DM describes what a character learned “over the course of the day,” the day can be the scope of the answer. Omit the check and its outcome from the markers unless the table also establishes a clock, an elapsed interval, or a shift in play. “You spend the next day questioning people” advances play by a day. A cutoff at dusk or an explicit “two hours pass” can likewise supply a marker. Record overlap only from evidence such as “while you're scouting.” Leave the order open otherwise.
- **Repetitions and corrections.** Keep one accepted reading per anchor or advance. Attach useful confirmations and the original/corrected wording as evidence on that marker. Preserve unresolved alternatives locally when the table never settles a value. A later clock reading for a different moment, a new advance, or a return to an earlier narrative frame earns its own marker.
- **Rests.** Use the one-hour short-rest and eight-hour long-rest conventions as labeled assumptions for established rests. Credit awarded later for time already spent belongs to that interval. Establish waking, overnight passage, and completed rest from the narration. A proposed or interrupted rest establishes only the time actually supported.

## Verify and deliver

Check each marker against its original passage and actor scope. Ask what timing would be lost if it were removed. Revisit actual travel, rests, elapsed actions, local clock changes, corrections, and frame shifts, including those without a time word. Verify source hashes, source order, quotes, structured values, and references. Check every source and evidence range against whole shared-UID groups using the group boundaries in `map-transcript-scenes/scripts/scene_map.py`; consecutive turns sharing a UID form one group. A quote can stay short inside its full group range. Preserve human decisions and stable IDs when revising. Disclose any incomplete reading.

Assess YAML dates from accepted markers. State which date components come from YAML and which are independently spoken. Preserve genuinely open boundaries of played events. Use `compatible` for missing coverage and reserve `conflict` for an established contradiction. Never fill a missing day using the YAML end date.

Deliver the JSON, the YAML assessment, and a simple table with one row per marker showing time, the played event it anchors or measures, and source UIDs. Use source order for lookup. Keep YAML, transcripts, and canonical dates untouched.

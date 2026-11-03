# Time and location extraction experiments

**Follow-up completed:** [Full sequential reads of two new sessions, 24 and 39](full-read/README.md), with eight new maps and a comparison against keyword selection.

**Start with [the side-by-side review](review.html).** It contains both time versions and both location versions for all five sessions, with session selection, search, and expandable evidence. For Obsidian or Markdown, use the session reviews below.

My recommendation is **two separate extraction skills with shared evidence conventions**: a time-marker skill and a location-marker skill. Keep the evidence ledgers as the reviewable foundation, then derive the chronology and place/visit/route views. Time and place extraction should work independently; linking them should not require a scene map or a time assignment for every line.

These are exploratory, human-unreviewed artifacts. No session YAML, transcript, canonical note, installed skill, or repository skill catalog was changed.

## The five-session comparison

The sample was drawn without replacement from **136** Dunmari Frontier manifests with registered, existing polished transcripts. Python `random.Random(20261102).sample()` selected Sessions 17, 98, 41, 32, 109 from paths sorted before sampling. There were no redraws or deliberate substitutions. The complete sampling frame, seed, and source fingerprints are in [sample.json](sample.json). The seed makes this reproducible; it does not make five sessions representative of all transcript types.

| Session | Time result | Location test | Full tables |
| --- | --- | --- | --- |
| 17 | April 16 → 24: eight date boundaries supported. Two individually narrated nights and six boundaries within a travel montage. | Southbound journey, unnamed camps, town approach, temple council room, mirror observation. | [Review 17](session-017/review.md) |
| 32 | Earlier downtime is non-linear. Initiation → two festival days → departure gives three ordered boundaries; the full eleven-boundary YAML span remains unconfirmed. | Ritual and dream views separated from physical presence; temple room; separate westbound and northbound departures. | [Review 32](session-032/review.md) |
| 41 | July 6 → 8 → 9 → 10 is clear; Kassi likely July 11; final July 13 endpoint not independently stated. | Camp-to-city journey, two different inns, Archives, temple balcony, monastery/library. | [Review 41](session-041/review.md) |
| 98 | Two completed nights match YAML May 5 → 7. Absolute starting date still comes from YAML. Countdown says “three days,” possibly inclusive; retain that uncertainty. | Teleport, offshore route, shore scouting, split party, mobile ship, four parallel town errands. | [Review 98](session-098/review.md) |
| 109 | One current day, sunrise → 4 p.m. → 6 p.m. → sunset; compatible with May 19 → 19. Previous-evening retcon is separate. | Tower rooms and stairs, bypass via windows, return for rest, observed-but-unentered room, teleport home. | [Review 109](session-109/review.md) |

No YAML corrections are proposed from these experiments. “Compatible” means the observed relative sequence fits; it does not independently verify an unspoken civil date. An exact total in hours is not supported for any full session.

## Time A: evidence ledger

One row per useful statement or marker, in transcript order. Each has a kind, framing, actor, interpretation, and exact quotation with a whole-turn UID range. Clock/date readings, rests, time jumps, backward references, self-corrections, and selected misleading candidates remain inspectable.

**What works:** It is easy to correct an extraction without untangling a whole timeline. It also makes “planned,” “reported history,” “table time,” and “vision” explicit. A known day or clock is not propagated into every intervening utterance.

**What is awkward:** Multiple statements can describe the same interval. In Session 17, “six days,” “April 23,” and the rest inside the montage are related evidence, not three durations to add. A ledger alone does not answer the nights question cleanly. Long lore discussions generate many misleading search hits.

## Time B: chronology with constraints

A smaller set of chronological anchors, linked back to ledger evidence. Relations express same-day continuity, overnight boundaries, approximate elapsed intervals, before/after order, and overlapping activity. Civil dates carry their derivation separately from spoken time of day. Unknown dates stay null.

**What works:** It answers the YAML question and supports an eventual campaign timeline. Session 32 can put the earlier mirror discussion before initiation even though its UIDs are later. Session 109's rest during deciphering fits inside the two study hours. Session 41 can retain an unknown final date instead of copying `drEnd` into the last row.

**What is awkward:** Constraint authoring requires judgment. A vague “few days” should remain vague; converting it automatically to 2–4 days would manufacture a bound. This prototype records constraints and checks references/counts; it is **not a general interval-solving engine**.

**Recommendation:** Use A for extraction/review and B for the derived timeline/audit. They are distinct representations of the same reviewed evidence, not two independent extractions or two competing versions of truth. Changes to A should stale B unless B is rechecked.

## Location A: transition ledger

Ordered markers record presence, arrival, journey, threshold observation, remote observation, and plans. Each has the relevant actors and place or endpoints. Small sites and rooms are allowed when the speech distinguishes them. A narrated multi-day journey can remain one path.

**What works:** It is intuitive to read alongside a transcript and catches significant movement without partitioning the full text. Session 98 makes it clear that Delwath went to Martino’s house while the others approached the halfling ship. Session 109 records the return to the throne room for a rest.

**What is awkward:** A long room-by-room descent becomes repetitive. The same place recurs under different descriptive phrases. A flat table does not itself show which rooms belong to one tower, or distinguish a moving vessel from a port.

## Location B: places, visits, and route graph

Reusable place nodes have session-local IDs, typed parent relations, optional verified vault identities, and transcript evidence. Visits reference those nodes; journeys connect them with travel mode, actors, optional intermediate places, and completion status. Observations and plans are separate collections. Coordinates remain null.

**What works:** It supports both the eventual campaign map and place-specific retrieval. A tower can be inspected at building or room level; two returns to the same room remain separate visits. A ship is a mobile platform, with journeys and anchored-harbor context, not permanently “inside” one city. Routes begun at the end of Session 32 do not prove arrival at Tokra or the mountains.

**What is awkward:** Identity resolution costs more work than extracting movement. Topology is much better supported than metric geometry. “Here,” “this way,” and pointers at Roll20 often cannot be recovered from text. A parent may mean `within`, `approach_to`, `above_near`, or an inferred shared base; consumers must inspect `parentRelation` rather than assume every child is physically inside its parent.

**Recommendation:** Keep A as the source evidence. Derive B as the spatial product. Do not automatically create a canonical place note for every temporary camp, room, or viewpoint. Do not publish NPC whereabouts simply because an NPC is mentioned during a party visit; later entity work must establish actual presence with its own evidence.

## Alternatives considered

| Alternative | Decision | Why |
| --- | --- | --- |
| Extend the existing scene map | Useful comparison, not the main format | Its exhaustive UID partition and site-scale boundaries are different from sparse markers, room-level topology, and independent actor movement. |
| One combined time-and-place extraction skill | Possible later orchestration wrapper | Convenient single invocation, but chronology and spatial identity have different failure modes and should not depend on one another. |
| Flat time and place tables only | Keep as A views | Easiest review, weakest support for deduplication, overlapping events, repeated visits, and map topology. |
| Fully normalized event/interval/geometry database | Defer | More machinery than these five transcripts justify; precise temporal bounds and route geometry usually are unavailable. |
| Regex-only extraction | Reject as final extractor | Helpful candidate finder, but it confuses spell durations, plans, historical narratives, table breaks, and actual passage of time. It also missed a bare “6:00” until a supplementary scan. |

## Draft skills and shared contract

Two **uninstalled prototypes** are included:

- [Extract time markers](draft-skills/extract-time-markers/SKILL.md)
- [Extract location markers](draft-skills/extract-location-markers/SKILL.md)

[format.md](format.md) documents the experimental schemas, source identity, projection rules, and proposed review lifecycle. These drafts have been informed by the five worked examples and checked for structure. They have **not** been independently forward-tested on unseen sessions. The pilot builder is tied to this sample; it renders and validates manually authored annotations, not arbitrary transcripts automatically.

## Verification and limitations

The pilot contains **87 time markers and 84 location markers**, represented in **20 JSON maps**, plus five full Markdown reviews and the HTML comparison. [validation.json](validation.json) records successful exact-quotation/UID checks, source/YAML fingerprint checks, graph/reference checks, date-boundary arithmetic, and eight negative/regression checks. Source-range quotes retain polished wording, including uncertainty. The count of evidence references includes reuse between time and location; it is not a count of independent observations. [review-checks.json](review-checks.json) records offline checks of all ten session/view combinations, UID search, and context filtering. The HTML was not visually browser-tested: local-file navigation was blocked by the browser URL policy. The complete Markdown reviews remain available as a fallback.

The extraction method was an ordered candidate sweep over every polished turn, expanded full-turn context at selected decisions, a supplementary numeric-clock/spatial sweep, and a focused semantic pass over the resulting chronologies and movements. It was **not an exhaustive semantic read of every lore, combat, and chatter turn**. Completeness/recall has not been measured; these maps are reviewable prototypes, not finalized campaign records. One useful next calibration would be a full sequential read of an unseen session, followed by an independent comparison against candidate-led extraction.

The experiment avoids private DM design material as a source of played movement. Place notes were consulted for identity and context; modern descriptions do not overwrite session-era evidence. Examples: the upper anvil in Session 109 stays distinct from the lower magical forge, and its Sibyl temple is not linked to the similarly named building in Tollen. The Feast of Bhishma calendar has an unresolved date conflict, so it was not used to certify Session 32.

All generated files are inside this directory. Existing source and YAML hashes are checked on rebuild. [notes.md](notes.md) records decisions and discoveries as work progressed.

To rebuild the existing sample from its authored JSON, run from the vault root:

```bash
python3 -B _sessions/time-location-testing/build_review.py
```

The `author_*.py` files preserve the manual authoring decisions; running them rewrites their corresponding `authored.json`. `read_source.py` is a read-only inspection helper. `build_review.py` validates and projects the already-authored records. These are different operations: running the builder does not perform a new extraction.

## Suggested morning review

1. Open Session 17, compare Time A/B, and decide whether the sparse anchor density feels right.
2. Inspect Session 32’s flashback ordering and conditional calendar projection.
3. Inspect Session 98’s split-party rows and ship routes; these expose the main limits of a single party-location cursor.
4. Inspect Session 109’s room graph and overlapping rest/study. Decide whether this level of room detail is useful or should be optional.
5. Choose whether to adopt the recommended evidence-plus-derived-view approach before developing production helpers or installing skills.

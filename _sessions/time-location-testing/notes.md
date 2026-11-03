# Time and location experiment — working notes

## 2026-11-02 — Setup

User authorizes exploratory artifacts only under this directory. Existing session artifacts and YAML stay unchanged. Main branch; pre-existing Great Library Arc 6 edit and Rumplewick note are unrelated.

Read existing scene-mapping skill and schema, plus skill-creator guidance. Borrow provenance and evidence rules; do not borrow exhaustive scene partitioning, output path, or forced site-scale granularity. No repository skills are being installed.

Reproducible random sample: seed 20261102; sorted eligible YAML paths; five samples without replacement or redraw. Eligibility requires registered polished transcript. Full sampling frame in sample.json.

Compare time A: evidence ledger; time B: relative chronology with constraints and YAML audit. Compare location A: ordered place/movement ledger; location B: place hierarchy plus visits and route graph. All are provisional, source-grounded extractions.

## Source inspection and design findings

Random draw: 17, 98, 41, 32, 109 (136 eligible). All have registered polished sources; four retain transcription uncertainty. Stable identifiers are local `uNNNN` UIDs, not globally unique UUIDs: durable identity must combine session + source fingerprint + UID. Preserve full polished-turn mappings when a quotation spans several UIDs.

- 17: April 17 and April 23 anchors surround six elapsed travel days. April 24 is spoken on arrival. Two individually narrated overnight transitions plus six date boundaries inside a montage; do not demand eight separate sleep statements.
- 41: afternoon July 6 -> evening July 8 -> July 9 -> Renewal on July 10; Kassi follows. Speaker Lara returns “a few days before you leave.” July 13 endpoint remains unconfirmed; July 15 crafting deadline is future, not an arrival at that date.
- 32: opening initiation is the evening before the festival; later dialogue explicitly retcons to earlier downtime. Visions and mirror images must not advance present chronology or move the physical party. Festival calendar reference itself has unresolved June 17/18 discrepancy, so it is not a safe independent date anchor.
- 98: teleport switches local morning to pre-dawn with no elapsed day. Two completed overnight transitions; three named day slots are not three elapsed nights. Split party in Artevus and Castrella; ship moves independently of shore excursions. Closing 4 a.m. sailing is a plan.
- 109: dawn-to-sunset day; retrospectively played previous-evening scrying; short rest during deciphering overlaps study. 4:00 and 6:00 clock anchors. Initial candidate search missed bare “6:00,” so supplementary numeric-clock and spatial-vocabulary sweep is required.

Evidence collection: broad ordered temporal/spatial candidate sweep over every polished turn, then surrounding full-turn context for decisions and supplementary sweep. This is a pilot extraction, not an independently audited exhaustive read of every lore/combat/chatter turn. Preserve this limitation in the handoff and do not claim measured recall.

No elapsed time from recording timestamps. No fixed coordinates inferred from map gestures. No output claims of precise room floor numbering from DM design notes. Canonical notes are used only to resolve place identities/context; played movement comes from the transcript.

## Artifact construction and semantic review

Produced all four maps for each selected session: time A evidence ledger, time B chronology/constraints, location A transition ledger, location B places/visits/routes. Both versions use the same manually adjudicated evidence; they are schema/view alternatives, not independent extractions. Totals: 87 time markers; 84 location markers; 79 local place nodes.

Focused second pass rechecked source quotes and important frame/transition decisions. Additional context established the Red Lily visit in 41 (separate from Kirian’s), actual switch to Summer’s Breeze in 98, the 2–3-hour final Castrella Bay leg, the 6 p.m. endpoint and sunset teleport in 109, and the mirror workshop in 17. Preserved the 98 countdown’s “three days” as uncertain competing phrasing, rather than silently declaring it reconciled.

Graph review changes: visit tables sorted by evidence/source order; begun routes no longer imply arrivals; threshold/remote observations create no visits; parent relations explicitly distinguish containment, adjacency, approaches, and inferred shared base. Upper mundane anvil remains distinct from lower magical forge. Time B’s context list is named nonAdvancingInSourceOrder because a played flashback can still contribute to chronological coverage.

Drafted two uninstalled skills and shared format contract. Skill frontmatter/naming validators passed for both. No .agents skill or SKILLS.md changes; drafts stay in this experiment. The builder is deliberately a validator/renderer of manual annotations, not an automatic semantic extractor or general temporal constraint solver.

## Review interface verification limits

Local HTTP preview could not bind a port under current execution restrictions. The browser then rejected the local file URL because its URL policy permits only HTTP(S). No browser workaround was attempted. Proceed with static JavaScript/content checks and complete Markdown reviews; do not claim a visual browser check. The self-contained HTML remains an optional local review artifact for the user to open.

## Final checks and handoff

- 20 JSON maps and five complete Markdown reviews built successfully; self-contained review.html includes all five sessions and both comparison modes.
- All 331 reused evidence references validated against current polished source text and whole-turn UID boundaries. All five transcript and YAML fingerprints still match the captured source revision.
- ID/reference/hierarchy checks, eight negative/regression checks, and derived-map fingerprint links pass. These validate structure and selected failure modes, not extraction recall.
- Offline JavaScript checks pass for all ten session/view combinations, UID search, and hide-context control. Visual browser inspection was unavailable; reported in README and review-checks.json.
- Both draft skill validators passed. Drafts remain uninstalled and were not independently forward-tested.
- Scoped git diff --check passed; separate whitespace checks cover untracked text files. Final git status shows only the pre-existing Great Library/Rumplewick work plus the new experiment directory. Main branch remains selected; nothing staged or committed.
- Recommendation: two independent extraction skills with shared source evidence and revision conventions; ledgers as review foundation, chronology and place/visit/route graphs as derived views. Production installation and an unseen-session/full-read comparison remain possible follow-up choices, not changes made here.

## Full-read follow-up — setup

User requested two new sessions read in full. New reproducible sample uses seed 20261103 and excludes original five; current eligible pool and fingerprints saved in full-read/sample.json. Freeze candidate-only baseline before reading full sequential source. Keep original pilot artifacts unchanged; follow-up artifacts under full-read/.

### Full-read follow-up: Session 24 read complete
All 1,320 turns read sequentially without filtering or truncated windows. Header and parser inventory checked. Candidate baseline is frozen regex hit coverage, not an independent authored extraction (earlier candidate preview was partial). Findings: u0672 bare “Hmm, ten” answers sunset countdown; u0183 accepts 10-minute ritual; offered short rest u0105 not taken (u0717 confirms). Wellby retcons scouting at u1182 before the return, not a second visit. Two narrated overnight transitions support YAML May 11–13 conditionally on start date. 5 am wake, three-hour journey, 9–9:30 arrival leave unquantified preparation time; do not force arithmetic. Delwath scout and two clairvoyance casts are concurrent. Grash seen remotely, not visited. Session ends at bridge with departure deferred to next session.

### Full-read follow-up: Session 39 read complete
All 1,648 turns read sequentially without filtering or truncated windows. Main action: pre-dawn Tokra inn, lair, tunnel, approximately two hours north to fort, tower confrontation and mist rescue, downhill interrogation/short rest, agreed compressed return to Tokra and planned northbound departure. No completed second long rest: closing long-rest suggestion replaced by short rest. Opening overnight is a boundary prologue, so July 3-only YAML is compatible for current-day play but not literal first narrated instant. Archives return is explicitly removed by map-retention retcon; do not add visit. Combat full read matters: Riswynn physically enters mist and is rescued; no proof she crosses into Pandemonium. “11:45”, “45 minutes”, “15 minutes” late in transcript are table scheduling. Historical werewolf account is approximate and cannot supply current elapsed days. Closing second short-rest mention could be a second rest or restatement of already completed recovery; preserve ambiguity instead of summing two hours.

### Full-read follow-up: comparison and handoff
Produced all four views for Sessions 24 and 39: 53 time markers, 54 location markers, 44 local places; 327 evidence references including reuse. All 2,968 turns read, with parser accounting and recorded windows. Exact quotations/UIDs, source/YAML hashes, graph pointers and night counts pass. Added local spatial collections for reported whereabouts and remotely observed entity presence; no installed/draft skills changed.

Raw filter selects 298/1320 turns (24) and 155/1648 (39). Nine authored markers cite no raw-hit turns (2 time, 7 location; some duplicate the same event across maps). IMPORTANT limitation: frozen filter baseline, not independent candidate extraction, and a partial Session 24 candidate preview preceded full reading. Sensitivity test: ±2 neighboring turns selects 1420 total and leaves one marker without any cited turn; ±5 selects 2073 and leaves none entirely without citations, but sixteen markers still cite some unselected context. Therefore no recall score, no claim that context-based extraction necessarily misses nine events, and no cost benchmark. Recommendation remains full read as next-trial default; search as checklist, especially because decisions and corrections can be separated by long discussions.

Main findings: Session 24 supports two nights conditional on May 11 start. Session 39 supports zero in-session nights after wake, but one opening-prologue overnight; boundary convention matters. Repeated short rest left unresolved. Accepted hand-wave return separated from cure/handover/departure intentions. Readable report and complete tables in full-read/README.md. Original five maps unchanged; parent README only gains follow-up navigation.

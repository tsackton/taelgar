---
name: extract-campaign-interactions
description: Enrich an existing session YAML and registered cleaned/polished transcript with scenes, entity interactions and quotes; retain excluded ranges and review evidence in session-processing-data.json, then register relative output pointers in YAML.
---

# Extract campaign interactions

Use for transcript-only session extraction, individual sessions or reproducibly sampled batches. The canonical model supports future source kinds, but this skill implements only transcripts. Read [the format](references/format.md), [the JSON schema](references/session.schema.json) and [processing evidence](references/processing.md). Preserve existing transcripts, recaps and historical extractions.

## Scope and inputs

Read applicable AGENTS.md and inspect Git status. Resolve the campaign through `_scripts/session_note_campaigns.json`. Use the session YAML, its registered cleaned/polished transcript and a reusable vault metadata index. Prefer registered polished Markdown with embedded UID comments; retain the cleaned UID mapping source. YAML owns all source declarations. Use the bundle reader for source hashes, mappings and speaker corrections. Propose fixes to missing/machine-specific YAML paths; never silently select a sibling file or add an independent source registry to the extraction. Initial extraction must not read beats, beat-facts or authored recap narratives. The automated review phase may consult existing beat data selectively; never generate it just for this workflow.

The transcript supplies events, participation, presence and quotations. The YAML is authoritative for campaign/session identity, real-world date, participant mapping and accepted in-world date span. It may clarify unstated dates or extend beyond recorded play. Do not reinterpret this additional context as a transcript contradiction. Vault names, aliases and canonical notes resolve identities and places; do not import future lore, secrets or missing encounters. Exclude private DM material. An absent/unresolved vault page is allowed; never invent a match or create a page merely to fill a field.

A request to extract authorizes derived output, not deployment or unrelated canon edits. Prepare candidates outside the vault; completion saves to a session-specific `interactions/` output folder and appends relative output pointers to the YAML; honor a requested batch directory. Never overwrite accepted/human-edited output during regeneration: write a candidate and surface its differences. Commits/pushes require session authorization.

## Bulk sequence

1. **Prepare:** build/reuse the vault index; select sessions reproducibly if sampling was requested. Require actual transcripts. Record the seed, complete eligible population, exclusions and selected sessions before inspecting outcomes. For variety, sample at least one session per available campaign, then fill remaining slots without replacement. Do not substitute easier sessions after seeing results.
2. **Extract:** read the complete transcript, including context around entity mentions. Produce `draft.json` in schema version 6, referencing `sessionYaml` without copied metadata or source paths. Maintain `session-processing-data.json` alongside it; set `fullTranscriptRead` only after actually reading the entire source. Use honest confidence levels with `unreviewed` status for session metadata, the scene collection, each entity and each interaction. A deterministic name hit is a candidate, not evidence of participation or a reviewed match.
3. **Validate:** check JSON/schema, source hashes, ranges, joins, vault paths and exact quote text. Mechanically passing records remain unreviewed. Inspect unassigned source ranges; record every excluded non-play range and a specific reason in processing `excludedBlocks`. Every UID must belong to a scene or a reasoned exclusion before completion. Do not omit played passages simply because they lack eligible entities.
4. **Automated review:** perform a separate review pass over consistency with YAML dates/PC information, vault-linked locations and every entity's inclusion/identity/match. Review excluded blocks/reasons and unexplained ranges explicitly. Record clear date contradictions as critical `metadataFindings`, citing transcript and YAML evidence; propose corrections without changing canonical fields. Review actual transcript evidence. Use existing beats and beat-facts only now, as optional hints for omissions, locations and chronology. Check discrepancies against the transcript; no note-only events. Expand beyond selected windows when needed to detect omissions. Do not just copy the extraction's confidence.
5. **Correct once:** for medium/low critical records, make one targeted correction or contextual recheck, update affected records and revalidate. Reassess honestly; no automatic confidence promotion. Preserve reviewer evidence and the before/after candidate. Remaining uncertainty enters the human queue; it does not block other sessions.
6. **Hand off:** render an entity-first review and batch directory. Lead with the entity list and each entity's session overview, vault match, confidence and review questions. Put featured quotes and complete interactions in expandable sections beneath the entity; keep scene context in a linked appendix. Make provisional metadata and entities visible. Retain the accepted draft/review chain sufficiently to inspect decisions. Never label machine validation alone as automated semantic review or use `humanReviewed` without an actual human decision. Sample some unflagged results for omissions. Complete only after source accounting and review replay pass: save `session.json`, `session-processing-data.json` and `review.md`, then append YAML-relative pointers under `interactionExtraction`. Do not register an incomplete candidate or overwrite existing different outputs.

This is an agent-operated workflow. The Python tools prepare, validate, render and apply separately authored review decisions; they do not call a model or perform semantic extraction by themselves. Use separate agents only when authorized by the user or other applicable instructions. A sequential extraction pass followed by a distinct evidence-based review pass is supported; identify the actual execution method in the run report.

## Scene and metadata extraction

A scene has one contiguous source reference, with `sourceId` naming a dotted artifact key in the YAML: `{kind: transcript, sourceId, startUid, endUid}`. Split meaningful location changes, time skips and combat transitions; keep scene indexes ordered and unique. Minor interjections and table chatter can remain inside ranges. Retain original `u####` IDs from polished comments. A polished turn may combine UIDs or split one UID; quotes must include the whole source mapping of their turns. Partial-UID ranges are not supported. Full coverage is a processing check, not a requirement to insert excluded chatter into `session.json`.

Optional scene type is `conversation`, `exploration`, `combat` or `travel`, by dominant activity. `location` is a vault place reference; `locationDetail` describes a narrative subplace. Keep unresolved references absent/null. `dateStart`, `dateEnd` and `time` preserve supported in-world timing; never equate recording timestamps with game time. Scene `aiSummary` is optional, at most 25 words, and can be a fragment.

YAML `drStart`/`drEnd` remain the session date authority; do not copy them into JSON or truncate them to the transcript. Scene dates can cover a narrower range. The extracted `locations` list is independently reviewed; do not assume all mentioned places were visited. PC information also belongs to YAML: participant speaker mappings are evidence, not automatically actual PC attendance. Propose missing/conflicting PC information in processing findings instead of creating another PC list. Guest/recurring status belongs on PC pages. Do not generate interactions for YAML-only or post-recording events.

Review the complete scene division using session `sceneReview`. Do not put review flags on individual scenes. Important uncertainty can remain in confidence and external review evidence; do not manufacture precision to get a high rating.

## Entities and whole interactions

Entities have `kind: npc | item | organization`. Include named NPCs and distinctive unnamed individuals useful to retrieve later, items meeting the selection rule below, and meaningfully involved organizations. Exclude generic crowds, interchangeable monsters, routine inventory, hypothetical creatures and this campaign's PCs. Do not make a construct NPC into a second item, or equate an organization with every member. A collection may share a card if the source treats it as one subject; preserve distinctions such as held fragments versus sought fragments.

Ordinary treasure—gold, generic gems, routine jewelry, valuables and undifferentiated hoards—does not get an item record, even when found, promised or divided. A distinctive object with its own role can still qualify: a named jade artifact, a magical pearl or speaking jewelry is not merely a monetary treasure entry.

Select items for meaningful events involving the object: finding or acquiring it, trading or giving it, losing or destroying it, discovering an important identity/property/history, or materially changing it. Also retain objects with a supported plot role, such as a quest objective, clue, bargaining token, curse or mechanism central to the problem. Include relevant mundane objects as well as magical ones. Use this session's evidence; do not assume future plot importance from later vault lore.

Exclude routine attacks with named magical weapons, using known movement/communication/detection abilities, drinking ordinary combat consumables, checking carried equipment, and incidental furniture or containers. A magic label, a successful attack, a long combat passage, or high interaction importance does not by itself justify an item record. Merely noticing a furnishing is not a meaningful discovery. Using familiar equipment to learn a plot fact does not automatically make that equipment a plot object. Avoid a second card for a generic container when its significant contents already have records.

Apply this selection to item interactions as well: keep the acquisition, exchange, destruction, revelation or plot-bearing encounter, rather than adding every later routine use. A newly found weapon can qualify when acquired without warranting records for its subsequent attacks; a long-owned staff can qualify when it gains story-significant powers. Do not split a meaningful whole encounter simply to remove incidental gear use inside it. Retain ordinary actions in scene context where useful, without manufacturing item records for them.

Each entity requires an ID, kind and label; optional `note` resolves a vault page. Optional entity `aiSummary` is at most two sentences covering the session. Unnamed entities can have high-confidence inclusion without an existing note when the transcript clearly establishes the individual; ambiguous attempted matches should remain unresolved.

Each interaction requires an ID, entity reference, nonempty scene-index list and interaction kind. Kinds: `interacted` for direct exchange/action (including fighting and item use), `observed` for seeing/hearing without engaging, `present` for affirmative passive presence, `mentioned` for discussion without established participation. Importance is optionally `star | supporting | cameo`. `knownAs` preserves the identity available at that point. Optional interaction `aiSummary` is at most one sentence.

One ongoing conversation is one interaction through topic changes, interjections, dice checks and brief asides. A conversation or guided visit may cross scenes. Departures, overnight gaps, later meetings and combat transitions can create new interactions. Do not split to accommodate more quotes.

Optional `passages` identify the meaningful portions of the encounter. Usually use one contiguous primary passage retaining conversational context. Additional supporting passages handle meaningful gaps, such as cuts to a parallel party. Each passage requires `source`; optional `relevance` is `primary | supporting`, and optional `aiSummary` is at most one sentence. With no relevance, a single passage is the default; multiple passages remain in source order. Passages are optional because joined scenes already provide source navigation. Do not restore the old excerpts/purpose/label/continuity fields.

## Quotes

One optional `quotes` array per interaction. Each quote requires `id`, `type`, exact `text`, and `source`. Types:

- `introduction`: PC or DM wording introducing/describing the entity.
- `color`: words spoken by the entity itself, including DM-voiced NPC speech.
- `whole`: PC or DM wording capturing the entire meaningful interaction in a short quotable passage.

These rules replace separate speaker/attribution fields. Verify voice in context; omit uncertain quotations. A PC/table joke is not an NPC color quote. Item/organization color quotes require genuine entity speech; use introduction/whole for appropriate PC/DM narration. Use exact wording/punctuation from the selected polished transcript, or cleaned wording when no polished artifact is registered. Quote text must be a contiguous substring of the selected source passage; do not mix representations. Do not turn paraphrased or invented dialogue into quotes.

For major entities with significant star interactions, actively seek multiple complementary memorable quotes when supported; usually two to four for a major speaking NPC. This is a target, not a quota. The entity's optional `aiSuggestedFeaturedQuotes` orders quote IDs from its own interactions; it recommends display without duplicating text. AI summaries and suggestions are review/navigation aids, not source evidence or narrative replacements.

## Review and readiness

Use optional `{confidence: high | medium | low, status: unreviewed | automatedReviewed | humanReviewed}` on session metadata, each entity and each interaction; use `sceneReview` for the scene collection. Confidence and status are independent. Missing metadata means unreviewed/unknown, never approved.

Critical session metadata and entity records are ready for normal vault use only with high confidence after automated or human review. Other data can be browsed while unreviewed; retain flags, and preserve unresolved entity status on dependent interactions. Do not hide provisional critical data behind an overall successful batch badge.

An automated review report must name the reviewer/pass, bind to the candidate digest, and provide each target's confidence, reason and evidence. Detailed rationale lives in the formal processing companion, not per-field metadata. Reports bind both the candidate and processing-evidence digests. Session YAML/source changes invalidate the reviewed inputs; exclusion/finding changes require a fresh review request. Include `session` and `scenes` decisions so exclusions and YAML consistency are always assessed. The tooling rejects stale reports and automated overwrites of human-reviewed records. Retain candidate/report history; v6 processing history and the historical v5 batch auditor enforce at most one correction attempt per execution. Higher attempts require a new explicitly scoped run, not resetting a counter to avoid triage.

## Tools and outputs

See [operations](references/operations.md) for CLI commands. Completed v6 outputs include `session.json`, `session-processing-data.json` and an entity-first `review.md`. Processing includes excluded blocks/reasons, source/YAML fingerprints, metadata findings and replayable review snapshots. The YAML points to both JSON files using paths relative to its directory. Keep full transcript copies and the reusable index in a work directory outside the vault; source links point to the original files.

Use the v6 validator with its processing companion for new sessions. Historical v5/v3 validation remains available without migration. Include `schemaVersion: 6`, never silently reinterpret an old file. Report actual sample coverage, corrections, unresolved issues and limitations. Do not describe a partial extraction as a completed run.

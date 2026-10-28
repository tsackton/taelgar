---
name: extract-campaign-interactions
description: Extract source-linked scenes, NPC/item/organization interactions and quotes into session.json; review critical metadata and entities in a separate automated pass, with one targeted correction before human triage.
---

# Extract campaign interactions

Use for transcript-only session extraction, individual sessions or reproducibly sampled batches. The canonical model supports future source kinds, but this skill implements only transcripts. Read [the format](references/format.md) and [the JSON schema](references/session.schema.json). Preserve existing transcripts, recaps and historical extractions.

## Scope and inputs

Read applicable AGENTS.md and inspect Git status. Resolve the campaign through `_scripts/session_note_campaigns.json`. Use the prepared session manifest, cleaned transcript and a reusable vault metadata index. Initial extraction must not read beats, beat-facts or authored recap narratives. The automated review phase may consult existing beat data selectively; never generate it just for this workflow.

The transcript supplies events, participation, presence and quotations. Manifest metadata supplies campaign/session identity, real-world date, participant mapping and provisional in-world date anchors. Vault names, aliases and canonical notes resolve identities and places; do not import future lore, secrets or missing encounters. Exclude private DM material. An absent/unresolved vault page is allowed; never invent a match or create a page merely to fill a field.

A request to extract authorizes derived output, not deployment or unrelated canon edits. Default to a session-specific `interactions/` output folder; honor a requested batch directory. Never overwrite accepted/human-edited output during regeneration: write a candidate and surface its differences. Commits/pushes require session authorization.

## Bulk sequence

1. **Prepare:** build/reuse the vault index; select sessions reproducibly if sampling was requested. Require actual transcripts. Record the seed, complete eligible population, exclusions and selected sessions before inspecting outcomes. For variety, sample at least one session per available campaign, then fill remaining slots without replacement. Do not substitute easier sessions after seeing results.
2. **Extract:** read the complete transcript, including context around entity mentions. Produce `draft.json` in schema version 5. Use honest confidence levels with `unreviewed` status for session metadata, the scene collection, each entity and each interaction. A deterministic name hit is a candidate, not evidence of participation or a reviewed match.
3. **Validate:** check JSON/schema, source hashes, ranges, joins, vault paths and exact quote text. Mechanically passing records remain unreviewed. Inspect unassigned source ranges; explain non-play exclusions in execution evidence outside canonical session data. Do not omit played passages simply because they lack eligible entities.
4. **Automated review:** perform a separate review pass over critical aggregate dates, PC attendance, vault-linked locations and every entity's inclusion/identity/match. Review actual transcript evidence. Use existing beats and beat-facts only now, as optional hints for omissions, locations and chronology. Check discrepancies against the transcript; no note-only events. Expand beyond selected windows when needed to detect omissions. Do not just copy the extraction's confidence.
5. **Correct once:** for medium/low critical records, make one targeted correction or contextual recheck, update affected records and revalidate. Reassess honestly; no automatic confidence promotion. Preserve reviewer evidence and the before/after candidate. Remaining uncertainty enters the human queue; it does not block other sessions.
6. **Hand off:** render readable cards and a batch index, with critical readiness and queue visible. Retain the accepted draft/review chain sufficiently to inspect decisions. Never label machine validation alone as automated semantic review or use `humanReviewed` without an actual human decision. Sample some unflagged results for omissions.

This is an agent-operated workflow. The Python tools prepare, validate, render and apply separately authored review decisions; they do not call a model or perform semantic extraction by themselves. Use separate agents only when authorized by the user or other applicable instructions. A sequential extraction pass followed by a distinct evidence-based review pass is supported; identify the actual execution method in the run report.

## Scene and metadata extraction

A scene has one contiguous source reference: `{kind: transcript, sourceId, startUid, endUid}`. Split meaningful location changes, time skips and combat transitions; keep scene indexes ordered and unique. Minor interjections and table chatter can remain inside ranges. Full coverage is a processing check, not a requirement to insert excluded chatter into `session.json`.

Optional scene type is `conversation`, `exploration`, `combat` or `travel`, by dominant activity. `location` is a vault place reference; `locationDetail` describes a narrative subplace. Keep unresolved references absent/null. `dateStart`, `dateEnd` and `time` preserve supported in-world timing; never equate recording timestamps with game time. Scene `aiSummary` is optional, at most 25 words, and can be a fragment.

Session `dateStart`, `dateEnd` and `locations` are independently reviewed aggregate facts. Do not blindly copy a manifest end date that includes post-recording events, or assume all reported locations were visited. `pcs` contains actual participating PC page references; guest/recurring status belongs on those pages. Resolve attendance against manifest mappings and actual transcript context. Distinguish someone attending play from an absent PC discussed by the party.

Review the complete scene division using session `sceneReview`. Do not put review flags on individual scenes. Important uncertainty can remain in confidence and external review evidence; do not manufacture precision to get a high rating.

## Entities and whole interactions

Entities have `kind: npc | item | organization`. Include named NPCs and distinctive unnamed individuals useful to retrieve later, consequential items/documents/tools/transfers, and meaningfully involved organizations. Exclude generic crowds, interchangeable monsters, routine inventory, hypothetical creatures and this campaign's PCs. Do not make a construct NPC into a second item, or equate an organization with every member. A collection may share a card if the source treats it as one subject; preserve distinctions such as held fragments versus sought fragments.

Each entity requires an ID, kind and label; optional `note` resolves a vault page. Optional entity `aiSummary` is at most two sentences covering the session. Unnamed entities can have high-confidence inclusion without an existing note when the transcript clearly establishes the individual; ambiguous attempted matches should remain unresolved.

Each interaction requires an ID, entity reference, nonempty scene-index list and interaction kind. Kinds: `interacted` for direct exchange/action (including fighting and item use), `observed` for seeing/hearing without engaging, `present` for affirmative passive presence, `mentioned` for discussion without established participation. Importance is optionally `star | supporting | cameo`. `knownAs` preserves the identity available at that point. Optional interaction `aiSummary` is at most one sentence.

One ongoing conversation is one interaction through topic changes, interjections, dice checks and brief asides. A conversation or guided visit may cross scenes. Departures, overnight gaps, later meetings and combat transitions can create new interactions. Do not split to accommodate more quotes.

Optional `passages` identify the meaningful portions of the encounter. Usually use one contiguous primary passage retaining conversational context. Additional supporting passages handle meaningful gaps, such as cuts to a parallel party. Each passage requires `source`; optional `relevance` is `primary | supporting`, and optional `aiSummary` is at most one sentence. With no relevance, a single passage is the default; multiple passages remain in source order. Passages are optional because joined scenes already provide source navigation. Do not restore the old excerpts/purpose/label/continuity fields.

## Quotes

One optional `quotes` array per interaction. Each quote requires `id`, `type`, exact `text`, and `source`. Types:

- `introduction`: PC or DM wording introducing/describing the entity.
- `color`: words spoken by the entity itself, including DM-voiced NPC speech.
- `whole`: PC or DM wording capturing the entire meaningful interaction in a short quotable passage.

These rules replace separate speaker/attribution fields. Verify voice in context; omit uncertain quotations. A PC/table joke is not an NPC color quote. Item/organization color quotes require genuine entity speech; use introduction/whole for appropriate PC/DM narration. Preserve ASR wording; quote text must be a contiguous substring of joined transcript utterances. Do not turn paraphrased or invented dialogue into quotes.

For major entities with significant star interactions, actively seek multiple complementary memorable quotes when supported; usually two to four for a major speaking NPC. This is a target, not a quota. The entity's optional `aiSuggestedFeaturedQuotes` orders quote IDs from its own interactions; it recommends display without duplicating text. AI summaries and suggestions are review/navigation aids, not source evidence or narrative replacements.

## Review and readiness

Use optional `{confidence: high | medium | low, status: unreviewed | automatedReviewed | humanReviewed}` on session metadata, each entity and each interaction; use `sceneReview` for the scene collection. Confidence and status are independent. Missing metadata means unreviewed/unknown, never approved.

Critical session metadata and entity records are ready for normal vault use only with high confidence after automated or human review. Other data can be browsed while unreviewed; retain flags, and preserve unresolved entity status on dependent interactions. Do not hide provisional critical data behind an overall successful batch badge.

An automated review report must name the reviewer/pass, bind to the candidate digest, and provide each target's confidence, reason and evidence. Detailed rationale is execution evidence, not per-field metadata. The tooling rejects stale reports and automated overwrites of human-reviewed records. Retain the candidate/report chain and use the batch auditor to enforce at most one correction attempt per execution; the individual apply command is stateless. Higher attempts require a new explicitly scoped run, not resetting a counter to avoid triage.

## Tools and outputs

See [operations](references/operations.md) for CLI commands. Outputs for each trial should include `session.json`, a human-readable `review.md`, a review decision record and a concise execution report with unresolved critical issues and coverage. Keep full transcript copies and the reusable index in a work directory outside the vault; source links point to the original files.

Use the v5 validator for current sessions. Historical v3 validation remains available for old pilots; it does not migrate them. Include `schemaVersion: 5`, never silently reinterpret an old file. Report actual sample coverage, corrections, unresolved issues and limitations. Do not describe a partial extraction as a completed run.

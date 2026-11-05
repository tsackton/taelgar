---
name: extract-combat
description: Extract condensed turn-by-turn actions and outcomes, grouped into rounds, from combat segments in a classified polished RPG transcript. Uses repeated initiative order, preserves reactions and extra actions, and prioritizes correct actions over exact round placement.
---

# Extract combat

Produce **combat segment → rounds → actor, resolved actions/results, source evidence** in `combat.json`. Aim to get each turn and action right even when round placement is imperfect. Read [the combat format](references/format.md) before authoring. Use an explicitly requested output directory; otherwise write `cleaned/<stem>-combat.json` in the existing session bundle. Preserve old trials unless revision is requested. Do not register outputs in YAML as part of extraction.

Resolve the session YAML, its registered polished transcript, and a current `segments.json` from [classify-transcript-segments](../classify-transcript-segments/SKILL.md). Verify session identity, YAML/transcript hashes, classification version, and segment coverage. For a requested whole-session combat extraction, create a missing classification with that skill as the prerequisite; do not run the other package extractors. A stale classification needs reinspection before use, not a hash replacement. Historical trial cutscene labels are not current classification.

After classification or a shared transcript read, perform a **mandatory dedicated second pass through the original polished text of every selected combat segment**, using the classification's UID boundaries as the reading worklist. Reread each segment in full even if the earlier pass produced a detailed combat draft. Work through long segments in consecutive windows without gaps, including setup, tactical discussion, rules disputes, and interruptions; read adjacent source as needed to verify boundaries. During this pass, build or reconcile the action entries using the detail and sequence checks in the format reference. Shared-read notes, existing summaries, keyword searches, and spot checks cannot substitute for this pass. It does not require rereading the noncombat remainder of the transcript. If classification is being created now, its complete-transcript read is also required.

A recap or combat annotation in session notes can help locate a fight but cannot establish turns, actions, or their outcomes. Do not call an extraction complete until the dedicated combat pass is complete; if source cannot be fully read, identify the affected segment/range and impact in `limitations`.

Extract every combat segment in a whole-session request; no combat yields `combats: []`. Respect an explicitly narrower requested scope and disclose the omitted segments in `limitations` rather than presenting that output as a complete session extraction. Preserve human corrections and IDs on revision.

## Turns and rounds

Use the established initiative order as the repeating cycle. Usually, when the first actor takes their next regular turn, a new round begins. **A character acting is not necessarily taking a turn:** reactions, legendary/villain actions, readied attacks, and other extra actions do not start a round. Distinguish explicitly identified lair actions, such as an effect on initiative count 20, from the normal turns of creatures created by that effect.

Initiative stays fixed unless the source changes it. Do not invent a new order each round or require an announced “Round 2.” When the first actor dies, leaves, or loses a turn, track the cycle through the remaining order. Incapacitation does not move someone to a different initiative position. New arrivals take the initiative position given in play; do not guess an exact score when only relative order is known. Keep summoned-creature turns and off-turn actions distinct when the transcript distinguishes them.

Number rounds consecutively within the encounter. If a fight is already underway at the start of the transcript, group the available cycles without inventing earlier turns and note that round 1 is the first recorded cycle. Keep opening actions that genuinely occur before the regular cycle in `openingActions`; this is not a bucket for actions that are merely difficult to place. Keep interrupted or unfinished fights incomplete.

Round grouping is an organizational aid. **Do not emit round accuracy, round confidence, explicit/inferred-round flags, or per-round uncertainty commentary.** Spend judgment on the actor, action, target, and outcome. Material uncertainty about those details belongs in a short local note. No need to stop for ordinary round-placement ambiguity.

## Resolve what actually happened

Condense each regular turn into an entry with its meaningful movement, attacks, spells, bonus actions, effects, and results. Preserve distinct actions within that text; do not compress the fight into a sentence per round. Give reactions and other extra actions separate entries attached by their position and wording to the triggering turn. Keep actor labels consistent without requiring a new entity map or inventing names for unnamed enemies. Group enemies only when the source resolves their actions collectively.

Follow proposals through adjudication. Record the accepted action and final result, not every contemplated spell, abandoned movement, mistaken target, or superseded damage roll as an additional completed action. Apply later corrections at the affected turn and place any resulting reaction beside its trigger in the resolved action sequence, citing the later evidence; the correction's transcript position does not move the action later in combat. Briefly mention a withdrawn alternative only when it explains the resolved action. Extract how the table played it; do not replace that record with external rules adjudication.

Retain supported targets, damage, healing, conditions, concentration changes, deaths, retreats, and objective progress, including the explicit resolution details specified in the format reference. Combat summaries must remain independently useful: a detail appearing in time extraction or an interaction excerpt is not a reason to omit it here. Do not invent a missing attack or turn to fill an initiative slot, calculate a complete HP/resource ledger, or reconstruct unseen map positions. A map pointer may leave the target unnamed; say so only when that ambiguity materially affects the summary. An explicit skipped/incapacitated turn is worth recording, but absence of speech does not prove a skipped action.

Combat narration and sustained table talk never split the classification's combat segment. Narration contributes an action/event entry when it changes the fight or resolves an objective; unrelated speech does not. End with the supported encounter result or state at the transcript cutoff. Do not declare victory merely because the source stops, or extend combat to later healing, looting, or planning once initiative has ended.

## Output and verification

Write one combat record per included combat segment using the format reference. Cite whole-turn UID ranges for each action/result; multiple ranges can support one entry when a correction is resolved later. Summaries must remain traceable without embedding the entire transcript. The file fingerprint binds each `segmentId` to the exact classification used.

Verify JSON parsing, schema fields, unique combat IDs, classification references, evidence endpoints and containment, consecutive round numbers, and matching source fingerprints. Reconcile the dedicated pass in both directions: each resolved source action/result must be represented, and each entry must be supported. Check for omitted turns or qualifiers, duplicate reactions, proposed actions mistaken for completed ones, misassigned targets, ignored corrections, and invented damage totals. Check that first-actor death, extra actions, or late corrections have not shifted actions into a false sequence. Valid JSON or matching encounter/round/entry counts cannot establish this semantic coverage.

Deliver the JSON and a concise account of meaningful action/target limitations. When a detailed comparison or readable output is requested, show every included opening action, round entry, ending, evidence range, and note; do not substitute an overview for the actual extraction. No mandatory HTML, encounter analytics, review-status lifecycle, scene extraction, time/location generation, or edits to canonical session records.

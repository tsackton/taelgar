---
name: extract-session-structure
description: Coordinate the six structured transcript extractions through one shared sequential read, followed by focused combat and interaction work. Produces the existing independent outputs, without scene extraction or transcript rewriting.
---

# Structured transcript extraction coordinator — draft

Use the installed component skills as the owners of inclusion rules, schemas, evidence, and verification:

- [Time](../../../../.agents/skills/extract-time-markers/SKILL.md)
- [Location](../../../../.agents/skills/extract-location-markers/SKILL.md)
- [Entities](../../../../.agents/skills/check-session-entities/SKILL.md)
- [Interactions](../../../../.agents/skills/extract-entity-passages/SKILL.md)
- [Classification](../../../../.agents/skills/classify-transcript-segments/SKILL.md)
- [Combat](../../../../.agents/skills/extract-combat/SKILL.md)

Read these skills and their required format references before extraction. This coordinator changes how their reading is shared; it does not change their products or interpretation rules. Keep all six files independently usable. No consolidated event ledger, scene map, or seventh semantic output is required.

## Prepare once

Resolve the polished transcript through the session YAML. Parse its existing UID mappings once and retain exact original text for evidence and excerpt assembly. Bind all outputs to the same source revision. Inspect existing same-session outputs and durable human decisions, and earlier entity maps as required by the entity skill. Do not reread earlier transcripts as a default.

For a comparison trial, use an explicitly separate output directory and fingerprint the existing outputs before starting. Do not rewrite source manifests to register experiments. Record experimental reading measurements separately from the six output schemas. Mechanical source parsing is not a semantic read.

## Shared sequential read

Read the complete transcript in source order, using manageable windows and respecting shared-UID turn groups. Before advancing each window:

- Draft actual time assertion records, including separate repeated and correcting assertions, structured values when supported, and exact evidence. Do not reduce these to candidate pointers for a later full extraction pass.
- Draft location markers and dictionary entries at the narrated scale. Keep journeys together when appropriate; repeated descriptions do not automatically create new markers.
- Extend the segment classification, carrying open segments across reading windows. Classification boundaries are not scenes and do not control which other facts may be extracted.
- Record entity candidates, identity-bearing occurrences, meaningful exclusions, and provisional importance. Defer final identity matching and whole-session importance until the full read is complete.
- When combat actions are already being read closely, retain an action draft with its citations. It remains provisional until the mandatory dedicated combat pass; drafting during the shared read does not satisfy that requirement.
- Retain candidate complete interaction ranges and their focal entities, including pending exchanges continuing beyond the window. Representative entity occurrences alone are insufficient to recover these ranges later.

Temporary working notes can carry unresolved references, open exchanges, split-party context, and evidence needing focused checking. They are working state, not a new maintained extraction format. Do not substitute a prose summary for source evidence. Do not skip combat, table talk, or session framing when extracting time, places, or entities.

## Complete the dependent work

After the shared read, resolve entity identities with vault evidence and finalize importance and exclusions. Preserve accepted human decisions. Finalize classification, time relationships and YAML assessment, and location references. Do not use YAML end dates to fill missing elapsed time.

After classification is finalized, perform the combat skill's **mandatory dedicated second pass**: reopen and read the original polished text of every labeled combat segment in full, even when a shared-read action draft exists. Use the classification's UID ranges as the worklist, not candidate action citations or keyword matches. Apply the combat format's detail and sequence checks while reconciling the draft, including enemy turns, saving throws, advantage/disadvantage, concrete benefits, and retrospectively corrected reactions. Adjacent source may settle boundaries. Do not substitute spot checks or a review of the draft JSON for this source pass. Preserve the continuous ordered-turn encounter and prioritize correct actions over inferred round placement.

Extract interactions from the candidate exchanges, binding them to the finalized entity map and copying retained source wording mechanically. Reopen wider source when the candidate boundary is inadequate; never force an exchange into an incomplete candidate range.

The full combat-segment reread is required; other focused reads depend on the work remaining. Avoid a second complete transcript read for each component solely because its skill is separately callable. The shared read satisfies an initial complete-source reading requirement only when it actually covered every turn with that component's extraction rules in mind; it never replaces the dedicated combat pass.

## Verify and hand off

Run each component's structural and source checks. Check references across files only where their schemas define a dependency: entities to interactions, classification to combat, and optional time links in location. All must share the same session and source revision. Do a substantive check of uncertain decisions and boundaries; validation does not establish semantic completeness or human review.

Use the owning validators without changing installed code. If a validator hard-codes ordinary output locations, an isolated trial harness may bind its in-memory bundle to the explicit trial path while preserving every other check. Disclose that adaptation; do not write experimental files to ordinary locations just to satisfy it.

On a rerun, inspect changed source or decisions before updating hashes. Revisit affected dependent outputs; do not automatically rerun independent ones when their evidence remains current. This is not permission to bypass an owning skill's source-change confirmation or human-review protections.

For a trial report, compare only products for which a prior baseline exists. Separate schema/skill changes from effects of sharing a read, and distinguish actual observed source-window use from theoretical token savings. Report omissions and necessary rereads, not just valid JSON. Prior exposure to the same transcript makes this an operational trial, not a blind quality comparison.

---
name: check-session-entities
description: Identify and check session entities against vault notes using a session YAML, polished transcript, and existing scene map. Distinguish NPCs, divine beings, significant items, and organizations in an entity-first review with confidence, UID evidence, unresolved matches, and meaningful exclusions. Preserve all source files and scene boundaries.
---

# Check Session Entities

Use after `map-transcript-scenes`. This stage resolves **who or what is being
referred to**, whether it belongs in the entity list, and which vault page it
matches. It does not generate interactions, importance, quotations, narrative
overviews, final `session.json`, or new vault notes.

This is a development checkpoint: assisted human review and Obsidian integration
remain unfinished. Read the [pipeline/model contract](references/pipeline-model.md)
for the concrete v7 final-session structure and the current review limitations.

## Inputs and boundaries

Read repository instructions and inspect branch/worktree. Resolve the session
YAML and its current `<stem>-scene-map.json`. Reuse the scene helper for YAML,
polished-source resolution, UID ranges, draft reading, and safe writes. Do not
create another source registry or PC list. The YAML remains the calendar anchor;
carry existing date findings into the handoff, without reclassifying an unstated
calendar date as insufficient evidence. A date conflict does not prevent identity
work, but time-dependent matches must preserve that uncertainty.

The ordinary run writes only `cleaned/<stem>-entity-map.json`. Source transcripts,
reduction drafts, scene maps, YAML, and vault notes are read-only. Render review
on demand; do not generate another lengthy report by default. A user-requested
saved review may use the same preview output. Do not commit or push automatically.

This map is provisional processing data. Its entity core (`id`, `kind`, `label`,
`note`, `review`) follows the [v7 interaction schema](references/session.schema.json),
including `kind: divine`. The historical v6 extractor is not compatible without
adaptation; do not silently convert divine records back into NPCs. Occurrences, identity rationale,
candidate pages, and exclusions support checking; they are not new final-session
fields. Later integration should consume these decisions, not rematch everything.

## Read once and inventory

Read the complete source using the existing scene divisions. A validated reduction
draft can be the reading view, but reopen original polished turns for every identity
claim and any snip that could conceal names, introductions, item events, or lore.
Read contextual blocks as well as scenes. Recaps, hypothetical plans, and postgame
discussion may identify entities without placing them in current play. A brief
aside retained inside a scene is still an aside. Do not use beats or generated
recaps to populate this inventory; later review may consult them as fallible hints.

Select:

- `npc`: named individuals outside the divine category, and distinctive
  unnamed people who could plausibly receive a name. A recurring unnamed guide or
  a specific prospective companion qualifies; anonymous crowds, generic monsters,
  and rumors of unspecified creatures do not. Keep source labels for unnamed
  people; never invent a proper name.
- `divine`: gods, named religious spirits such as tanshi, and other beings whose
  established identity is divine or an object of worship. Named divine collectives
  such as the Meswati also belong here. Track meaningful mentions, prayers, beliefs,
  and attributed influence without treating them as NPC encounters. A god remains
  divine even when directly encountered; preserve that encounter's source evidence.
  Priests, godcallers, and worshippers remain NPCs; religious institutions remain
  organizations. Supernatural origin alone does not make a ghost, demon, dragon,
  or other creature divine. Use source/vault context, not a folder or keyword alone.
- `item`: particular items found, acquired, traded, destroyed, lost, meaningfully
  discovered, or central to a plot. Meaningful discussion of an item's in-world
  history, identity, powers, limitations, or possible role also qualifies, even
  when it is never used and no new property is established. Include substantive
  consideration of lore-rich artifacts such as the Binding Stones or Mirror of
  Soul Trapping as possible solutions; preserve proposed uses as discussion.
  Exclude ordinary money/gems, incidental inventory mentions, and routine combat
  uses of party equipment, such as weapon attacks, standard activations, or damage
  arithmetic. Extensive vault lore alone does not make an otherwise routine use
  significant; the session must meaningfully engage with the item. Distinguish
  separate physical items; a generic item-type page does not establish that two
  objects are the same.
- `organization`: identifiable tribes, factions, institutions, or organized groups.
  Generic species, languages, populations, and incidental crowds are not organizations.

Use YAML participant roles to identify the session's PCs; do not create entity
records merely because they are transcript speakers. A PC from another session
may be a meaningful named referent here, but do not infer attendance. Ignore player
names in scheduling. Place matching remains in the scene map; do not invent a
place entity kind or turn every mentioned place into a visited location.

Group occurrences by contextual identity, not just matching words. Keep separate
people with the same name, and combine pronouns/titles only when supported. A name
inside a place name alone is not necessarily a reference to that person. Do not
promote historical stories, speculation, or discussion of next session into events.

## Match against the vault

Search filenames first (`rg --files`), then frontmatter `name`/`aliases`, spelling
variants, both sides of wikilinks, and relevant backlinks. Reuse existing search
tools or an available name index as candidate discovery; do not persist a second
vault-wide registry. Search/read actual notes before choosing a match. Exact spelling
alone is insufficient when role, geography, time, or context disagrees. Read each
candidate in full and account for uncertainty/status comments. Avoid using future
revelations to silently identify a masked or unnamed person.

Keep `note` absent/null when unresolved. Supply plausible `candidates` and a brief
`reason` when there is a specific ambiguity. A clearly identified new person can
have high confidence and no note: missing a page is not uncertain identity. Before
claiming no match, broaden the search and state its scope in the reason. Never
create a note just to make matching succeed. Do not copy private DM information
into this shareable artifact; ordinary note targets exclude private/support paths.

The review applies to the whole entity: selection, identity grouping, and vault
match. Use `review.confidence` = `high | medium | low` and `review.status` =
`unreviewed | automatedReviewed | humanReviewed`:

- **High:** identity/selection is well supported; the note match is supported or
  the absence of a suitable note is understood.
- **Medium:** one interpretation is favored but a material identity or selection
  question remains. Explain it and retain alternatives when useful.
- **Low:** the referent or match is weak/conflicting; do not force a link.

Extraction starts `unreviewed`. Perform a distinct semantic pass over the entire
entity list, exclusions, and evidence before setting `automatedReviewed`. Mechanical
validation is not semantic review. Use `humanReviewed` only for the specific entity
decisions the user has actually reviewed, not their acceptance of scene boundaries.
Do not overwrite an earlier human decision without explicit direction; preserve
stable IDs on revision. Changed entity decisions return to `unreviewed` until
rechecked. A stale map/note invalidates relying on its old review.

## Keep evidence and review small

Record representative `occurrences` as original transcript source ranges, with at
least one useful passage per scene/context block where the entity meaningfully
appears or is discussed. Do not catalog every name token or pronoun. Prefer a short
introduction or identity-bearing passage over a whole conversation. Add another
passage in the same scene only when it materially aids identification/checking.
Each range must fit a single existing scene or context block and respect whole
UIDs/polished turns. The helper derives scene/context labels; no duplicate scene
registry is stored. Occurrence does not mean presence or interaction.
In particular, a divine mention, invocation, or claim of intervention does not
establish a manifestation or direct conversation. Retain the original wording and
uncertainty for later processing. Final v7 uses the ordinary interaction vocabulary
with distinct divine kind; contextual evidence anchors mentions, not played encounters.
This inventory stage does not assign interaction types.

Use `exclusions` for plausible candidates a reviewer might expect but which were
omitted, giving `label`, `reason`, and a representative `source`. Examples include
routine gear, a generic creature, or a named PC mentioned only in scheduling.
Do not inventory every coin, animal, or ordinary noun. These are entity-selection
decisions, not deletions or exclusions of entire transcript blocks.

No AI biography is needed. Optional `reason` is a short identity/selection rationale,
required for unresolved matches or medium/low confidence. Optional `names` contains
useful source variants/titles, not a copied vault alias list. Review is entity-first:
uncertain/unreviewed entities first, clear matches compactly, exclusions separately.
Open selected entity evidence on demand instead of reprinting every scene.

## Commands and verification

Read [the format](references/format.md). Set `HELPER` to
`.agents/skills/check-session-entities/scripts/entity_map.py` and `YAML` to the manifest.

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML inspect --note 'People/Example.md'
python3 -B HELPER --session-yaml YAML show --start-uid u0010 --end-uid u0020
python3 -B HELPER --session-yaml YAML save --proposal - --expect-input-digest DIGEST
python3 -B HELPER --session-yaml YAML validate
python3 -B HELPER --session-yaml YAML preview
python3 -B HELPER --session-yaml YAML preview --kind divine
python3 -B HELPER --session-yaml YAML preview --kind npc
python3 -B HELPER --session-yaml YAML preview --entity e001
```

Before reading candidate notes, `inspect --note` each selected/candidate/supporting
page (repeat the flag). Retain that `inputDigest` through review/save. Reinspect and
reread if adding notes or if inputs change. An existing map needs its inspected
`--expect-sha256` for intentional revision. Save the proposal through stdin or a
temporary file, never by bypassing the helper. It fingerprints sources, YAML, scene
map, and consulted vault pages; preserves original sources; and uses the existing
directory lock and atomic write helper. `evidenceNotes` can retain consulted pages
which informed a decision without being candidate targets. No fingerprint proves
all possible notes were searched or that matching was correct.

Verify source preservation, whole-turn ranges, scene/context containment, stable
IDs, duplicate identities, meaningful exclusions, and all low/medium matches.
Reopen at least the identity-bearing original passage and chosen note for the
separate semantic pass. Prefer targeted human review; do not require approval of
every clear match. Hand off the compact entity preview, open questions, map path,
and review performed. Stop before interactions and final session generation.

For maintenance run:
`python3 -B -m unittest discover -s .agents/skills/check-session-entities/tests -v`.
Install dependencies from `requirements.txt`. The separate `session_model.py`
provides read-only v7 validation and candidate projection; it is not an automated
interaction generator or review-application workflow.

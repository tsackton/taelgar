---
name: check-session-entities
description: Identify NPCs, divine beings, significant items, and organizations from a YAML-registered polished transcript, without a scene map. Check vault matches and UID evidence, flag later identifications while preserving session-era labels, and present confidence and meaningful exclusions. Preserve source files.
---

# Check Session Entities

Use after a polished transcript is registered in session YAML. Resolve who or what
is referred to, whether it belongs in the inventory, and which vault page matches.
This stage does not generate interactions, importance, quotes, biographies,
recaps, final `session.json`, or new vault notes.

## Inputs and boundary

Follow repository branch/worktree instructions. Resolve one session YAML and read
its **complete polished transcript**, in order, using bounded UID windows. No scene
map or reduction draft is required. Reuse the helper's source reader and YAML-owned
PC roles; do not build another source registry or PC list. Preserve material time
uncertainty in identity matches; full chronology/scene mapping is separate.

The ordinary run writes only `cleaned/<stem>-entity-map.json`. Transcripts, YAML,
vault notes, drafts, scene maps, and other processing files stay read-only. Render
review on demand; do not persist a lengthy report by default. A saved review needs
a user request. Do not commit or push automatically.

Read [the map format](references/format.md) for fields and validation.
[The review workflow](references/review-workflow.md) covers saved reviewers,
feedback, and handoffs; [the pipeline contract](references/pipeline-model.md)
covers v7 projection. Human feedback application is manual; Obsidian integration
and final interaction generation are unfinished.

## Inventory from speech

Infer framing from surrounding speech. Recaps, hypotheticals, and postgame lore
can identify entities without placing them in current play. An aside within a
conversation remains an aside. Do not populate the list from beats or generated
recaps; those can be later, fallible review hints.

Select these kinds:

- **`npc`:** named non-divine individuals and distinctive unnamed people who could
  plausibly receive a name. A recurring guide, prospective companion, or individually
  identified role such as Havdar's lieutenant qualifies without dialogue or a proper
  name. Keep descriptive labels; omit anonymous crowds, generic monsters, and rumors
  of unspecified creatures.
- **`divine`:** gods, named religious spirits such as tanshi, other established
  divine/worshipped beings, and named divine collectives such as the Meswati.
  Track meaningful religious mentions, prayers, beliefs, and attributed influence.
  Clergy remain NPCs and religious institutions organizations. Supernatural origin
  alone does not make a ghost, demon, or dragon divine; use source/vault identity,
  not folder or keywords. A god stays divine when encountered directly. Use an
  established divine identity even if unknown during play: Delwath's unnamed patron
  is divine when clearly identified as Yezali, with a later-identification flag.
- **`item`:** particular plot-significant objects, meaningful acquisition/trade/loss/
  destruction/discovery, or discussion of in-world history, identity, powers,
  limitations, or possible roles. Brief concrete lore, such as recognizing an old
  elven blade, qualifies without a long conversation, completed origin story, new
  property, or actual use. Proposed artifact uses remain discussion. An adjective
  like “wonderful” alone is insufficient. Omit ordinary money/gems, incidental
  inventory mentions, routine weapon attacks/activations, and damage arithmetic.
  Extensive vault lore cannot make routine use meaningful in this session.
- **`organization`:** identifiable tribes, factions, institutions, organized groups,
  distinct communities, and recognizable historical adventuring parties. A formal
  name or explicit leadership structure is unnecessary: the peaceful desert orcs
  and Heroes of the Great War qualify. Generic species, languages, populations,
  and incidental crowds do not qualify merely by being mentioned.

Use YAML roles to distinguish this session's PCs from entity referents; transcript
speakers alone do not qualify. A PC from another session can be a meaningful
referent without attending this one. Ignore player names in scheduling. Place
matching belongs to scene mapping; there is no place entity kind.

Group by contextual identity, not matching words. Separate different people with
the same name and distinct physical items described by one generic item page.
Combine titles/pronouns only when supported. A name in a place label alone need
not refer meaningfully to its namesake, but check the associated being when tomb/
monument lore discusses it: Yerkir-Khor qualifies. Do not turn historical stories
or speculation into played events.

**Dunmari Frontier exception:** when YAML identifies that campaign, track the
party's ladders as `npc` companions, including equipment use. This does not assert
animation or action. Match the Ladder page when supported and distinguish current
and destroyed ladders; a passing predecessor joke need not create a record.
Do not apply this convention to other campaigns.

## Match identities

Search filenames first, then frontmatter names/aliases, spelling variants, both
sides of wikilinks, and backlinks. Candidate discovery can use an existing index;
do not persist another registry. Inspect and read complete candidate/supporting
notes, including uncertainty/status comments. Exact spelling alone is insufficient
when role, geography, time, or context disagrees.

Use clear later material to resolve an unnamed/masked identity. Choose its `note`,
set `identifiedLater: true`, and keep `label`/`names` faithful to what the entity
was called in this session. Inspect and fingerprint the supporting page. For
example, “Captured orc spellcaster” can link to Gorkil while retaining that label.
The flag records provenance, not uncertainty;
a clear later match can have high confidence. Do not imply knowledge at the time,
rewrite transcript evidence, or import later events/private revelations.

For genuine ambiguity, leave `note` absent/null and retain plausible `candidates`
with appropriate confidence. A chosen note and competing candidates cannot coexist.
An identified new person can have high confidence without a page. Before claiming
no match, broaden the search and state its scope in the handoff; never create a
note to make matching succeed.
Keep private information out of the shareable map; private/support paths are not
permitted note targets or evidence notes.

## Evidence and review

Record representative `occurrences`: at least one focused passage per distinct
encounter or substantive discussion. Prefer identity-bearing speech, not entire
conversations or every name/pronoun. Extra passages in one discussion should
materially help checking. Respect whole polished turns and UIDs; no scene ownership
or interaction classification is needed. Separate passages when useful to preserve
recap, speculation, and played-action framing. Occurrence alone proves neither
attendance nor interaction; invocation or attributed intervention is not evidence
of a divine manifestation or direct exchange.

Keep `exclusions` for plausible candidates a reviewer might expect, with label,
reason, and the same `occurrences: [{source}]` array as included entities. Retain
multiple focused passages when a referent is excluded across distinct appearances.
Do not inventory every ordinary noun. These decisions omit
entities, not transcript blocks. Exclusion reasons are at most 40 words.
Entity records have no `reason` field; retain evidence, candidates, confidence,
and the later-identification flag instead of generated rationales. Optional `names`
contains useful source variants/titles, not copied vault aliases.

Confidence covers selection, identity grouping, and vault match together:
`high` is well supported, including an understood lack of a page; `medium` favors
an interpretation with a material question; `low` is weak or conflicting. Surface
material uncertainty in the review handoff instead of forcing links.

Start `unreviewed`. Make a **distinct semantic pass** over the whole inventory,
exclusions, identity-bearing speech, and chosen notes before `automatedReviewed`.
Validation is not review. `humanReviewed` requires explicit review of that actual
entity decision; approval of scenes, the skill, or broadly correct inclusions does
not approve every row. Preserve stable IDs and earlier human decisions. Changed
decisions return to `unreviewed` until checked; stale source/note evidence
invalidates relying on old review. Helpers do not enforce these review semantics.

## Inspect, save, and hand off

Set `HELPER` to this skill's `scripts/entity_map.py` and `YAML` to the manifest;
substitute actual paths below:

```bash
python3 -B HELPER --session-yaml YAML inspect
python3 -B HELPER --session-yaml YAML inspect --note NOTE_PATH
python3 -B HELPER --session-yaml YAML show --start-uid u0010 --end-uid u0020
python3 -B HELPER --session-yaml YAML save --proposal - --expect-input-digest DIGEST
python3 -B HELPER --session-yaml YAML validate
python3 -B HELPER --session-yaml YAML preview
python3 -B HELPER --session-yaml YAML preview --kind divine
python3 -B HELPER --session-yaml YAML preview --entity e001
```

`NOTE_PATH` is an actual vault-relative note path. Before reading notes, inspect
**every** chosen, candidate, and supporting page with repeated `--note` flags,
including unchanged records on revision. Omit that flag
when no pages are involved. Retain `inputDigest` and `mapSha256`. Adding notes
requires inspecting the full set again and checking previously read evidence for
changes. Use `evidenceNotes` for supporting pages outside chosen/candidate targets.

Save a complete proposal through stdin or a temporary file using the inspected
digest. Intentional revisions also need the inspected `--expect-sha256 HASH`.
Do not bypass guards or edit stored fingerprints. The helper rechecks sources,
YAML, and notes and uses the shared directory lock and atomic write. Legacy v1
maps require explicit evidence rechecking before a guarded v3 save. For v2 maps,
remove entity `reason` fields, wrap each exclusion's source in an occurrence array,
and save as v3 after verifying current inputs,
preserving IDs, evidence, and review values. Do not silently migrate attestations.

Verify unchanged inputs, focused whole-turn evidence, identity grouping, stable
IDs, duplicates, exclusions, and all medium/low matches. Present an entity-first
review: uncertain/unreviewed records first, clear matches compactly, exclusions
separately, later-identity flags visible even at high confidence. Open evidence
on demand. `--kind npc` and the other kinds filter the preview; unclassified
exclusions remain in the full view. Hand off map path, review performed, and
material questions; do not require approval of every clear match.

## Maintenance

Install [requirements](requirements.txt). Helpers require Python 3.9+; tests use
Python 3.10+. Run
`python3 -B -m unittest discover -s .agents/skills/check-session-entities/tests -v`.
The separate `session_model.py` validates/projects v7 candidates read-only;
its [contract](references/pipeline-model.md#final-sessionjson-v7) defines the limits.

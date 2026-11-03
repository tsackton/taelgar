---
name: check-session-entities
description: Identify NPCs, divine beings, significant items, and organizations from a YAML-registered polished transcript or prepared narrative, without a scene map. Consult existing same-session and earlier same-campaign entity maps for context without rereading earlier transcripts. Assess session importance, check vault matches and UID evidence, preserve session-era labels, and present confidence and meaningful exclusions, with short explanations for medium/low-confidence decisions. Read durable review JSON, preserve human corrections, and support feedback resolution and skill recalibration. Preserve source files.
---

# Check Session Entities

Use with a polished transcript or prepared narrative registered in session YAML. Resolve who or what
is referred to, whether it belongs in the inventory, which vault page matches,
and how important the entity is in this session.
This stage does not generate interactions, quotes, biographies,
recaps or new vault notes.

## Inputs and boundary

Follow repository branch/worktree instructions. Resolve one session YAML and read
its **complete polished transcript**, in order, using bounded UID windows. No scene
map or reduction draft is required. Reuse the helper's source reader and YAML-owned
PC roles; do not build another source registry or PC list. Preserve material time
uncertainty in identity matches; full chronology/scene mapping is separate.

Unknown session dates do not block entity mapping. The shared source reader
allows null or absent dates for this stage while retaining validation of supplied
dates, source fingerprints, and UID coverage. Preserve the YAML's uncertainty;
do not supply invented dates. Scene mapping retains its existing date requirements.

For `sourceType: narrative`, read the complete UID source registered by
`preparedSourcePath` instead of a polished transcript. The helper accepts a
bundle-relative path or relocates a legacy absolute path only when its exact
bundle/cleaned/prepared filename suffix matches. Do not substitute a generated
recap or silently use a cleaned narrative: its UIDs may differ. Keep complete
narrative units as evidence, including the author's uncertainty and attribution;
metadata and headings alone do not establish an encounter. Assess importance
from the events described, without inventing missing dialogue or detail. The
remaining inventory and review rules apply equally to narrative sources.

A new ordinary run writes only `cleaned/<stem>-entity-map.json`. Revisions with
existing review JSON also append the agent regeneration to that history. Transcripts, YAML,
vault notes, drafts, scene maps, and other processing files stay read-only. Render
review on demand; do not persist a lengthy report by default. A saved review needs
a user request. Do not commit or push automatically.

Read [the map format](references/format.md) for fields and validation.
Read [session importance](references/importance.md) for the required tiers and
calibration cases before assigning them.
[The review workflow](references/review-workflow.md) covers saved reviewers,
feedback, and handoffs; [the pipeline contract](references/pipeline-model.md)
covers source ownership and independent mapping stages. Obsidian supports table and one-at-a-time review;
`scripts/entity_review.py` owns the durable `cleaned/<stem>-entities-review.json`
feedback and human-change history. Table review supports immediate field saves
and reversible human exclusions; preserve the sidecar's archived excluded records
and never recreate them during regeneration. See the review workflow for guarded
Include, exclusion evidence, and the explicit human-only empty staging-note action.
Final interaction generation remains separate.

Before revising a map, read its review JSON, including human edit/removal history
and open comments. Consult relevant prior-session feedback alongside prior maps.
On **“recalibrate skill based on feedback”**, follow the review workflow’s
calibration procedure to update supported rules and the skill catalog. On
**“resolve feedback with my help”**, work through open issues with evidence and
focused questions, then record checked resolutions. Neither mode invents human
approval or silently replays comments against changed records.

## Prior entity maps as context

Before inventorying the current session, inspect its existing entity map, if any,
and discover earlier entity maps in the **same campaign**. Resolve campaign and
session order from their session YAMLs, not filenames or file modification times;
use the repository campaign registry for aliases. Start with the nearest earlier
session and look farther back for recurring identities, useful source names,
unresolved candidates, or relevant exclusions. If none exist, proceed from the
current source and vault notes; do not generate missing maps as a prerequisite.

Read those compact maps for context instead of loading earlier transcripts into
the reading context. Prefer reviewed decisions, but treat every prior match as a
lead to check, not independent evidence or a new source of canon. A stale or
unreviewed map can suggest searches; do not present its decisions as verified.
Open a focused earlier UID passage only when a specific identity ambiguity cannot
be resolved from the maps and complete relevant vault notes. Do not routinely
reread whole earlier transcripts. Still read the **complete current source**.

Re-establish each inclusion, exclusion, kind, grouping, and importance from the
current session. Prior attendance, importance, Mirror examinations, review status,
and occurrence ranges do not carry forward. An earlier exclusion may qualify now.
Keep session-era labels and uncertainty; later-identity flags describe what was
known in the current session, not a copied flag from another map. Entity IDs are
session-local: preserve IDs and applicable human decisions when revising the same
map, but do not equate IDs across sessions or copy another session's approval.

Prior maps are discovery aids, not `evidenceNotes` or occurrence sources. Inspect
and read the actual chosen/candidate/supporting vault pages as usual, and
ground every occurrence in the current session. If a prior map is the only basis
for a proposed identity, leave it unresolved rather than asserting the match.
Mention which earlier maps informed the run and any unresolved conflicts in the
handoff; do not persist another campaign registry or a context report by default.
For a requested one-by-one calibration, finish and present one map for feedback
before starting the next, then apply that feedback to the skill as appropriate.

## Inventory from speech

Infer framing from surrounding speech. Recaps, hypotheticals, and postgame lore
can identify entities without placing them in current play. An aside within a
conversation remains an aside. Do not populate the list from beats or generated
recaps; those can be later, fallible review hints.

Select these kinds:

- **`npc`:** named non-divine individuals and distinctive unnamed people who could
  plausibly receive a name. A recurring guide, prospective companion, or individually
  identified role such as Havdar's lieutenant qualifies without dialogue or a proper
  name. Keep descriptive labels; omit anonymous crowds, generic monsters, and
  generic creature rumors without a distinguishable referent or specific mystery
  hook. Apply the mystery-clue guidance below to unusual sightings and suspects.
  For unnamed people known only through secondhand accounts, an unclear identity
  and incidental mention weaken the case for inclusion. An unusual fate or personal
  detail alone may not establish a meaningful individual identity. **Mawar Episode
  2 calibration:** exclude the victim who spoke to his dead daughter: the user
  judged the identity too unclear, and the party only heard about him rather than
  meeting him. This is not a blanket requirement for direct encounters; meaningful
  named or historical references and specific mystery figures can still qualify.
  Direct presence does not by itself establish individual identity either.
  **Mawar Episode 2 calibration:** exclude the unnamed townsperson killed by
  Azar's lightning; the witnessed death establishes a casualty, but no distinct
  character identity beyond that event.
  For homunculi, summons, familiars, and other creatures produced by character
  abilities, distinguish a companion with an ongoing identity from a routine
  ability activation. A distinctive appearance, mechanical creature type, or
  repeated scouting commands in one encounter does not alone establish that
  identity. Look for evidence such as continuing relationships, personality, or
  explicit treatment as the same individual beyond the ability's routine use.
  **Mawar Episode 2 calibration:** exclude Wazir's mechanical flying fish; the
  user identified its appearance and scouting as routine homunculus activation,
  without a unique companion's ongoing identity. This is a borderline case whose
  initial inclusion should have had **low confidence**, not high. This does not
  exclude established companions merely because their mechanics use an ability;
  Blu / Turk remains an approved example of an individual companion.
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
  **Exclude routine use of PC magic items**, in or out of combat. Wearing,
  activating, or briefly lending an item to use its usual powers does not qualify
  by itself, even when useful or protective. Rules checks about attunement or
  standard powers are not in-world item lore. Require a separate qualifying basis,
  such as meaningful acquisition, loss, discovery, original lore, or involvement
  as a distinct plot object beyond its routine equipment function. An ordinary
  object temporarily enchanted by a PC ability is subject to the same distinction;
  routine ability use alone does not establish a significant item.
  **Magic items have a lower inclusion threshold:** a brief, concrete contribution
  from a particular magic item can suffice when it is not merely routine use of
  PC equipment, without extensive lore, a name, or recurring appearances.
  **Mawar Episode 1 calibration:** include Illius's compass
  as a cameo for helping locate the stolen drop; the user's review identifies
  this as a magic-item inclusion case. Do not invent additional powers from that
  ruling. This lower threshold concerns inclusion, not importance, and does not
  override the exclusion of incidental mentions or routine PC item use.
  **Mawar Episode 2 calibration:** exclude Wazir's Cloak of the Manta Ray. Lending
  it to Trok for underwater breathing is routine use of a PC magic item; its
  practical benefit does not by itself justify an entity entry.
  For borderline vessels or other objects serving mainly as an encounter's
  setting or transport, ask whether they have a meaningful identity beyond that
  appearance. Involvement in an important rescue or battle alone is insufficient.
  **Mawar Episode 1 calibration:** exclude the merfolk ship; despite its unusual
  arrival and rescue, it has no meaningful identity beyond its one appearance.
  This is not a blanket recurrence requirement: a single appearance can establish
  a significant object's identity, as with the stolen drop of Sentient Ocean.
- **`organization`:** persistent groups with identities of their own, such as
  tribes, factions, institutions, communities with collective identities beyond
  shared residence, and established adventuring parties. A formal name or explicit
  leadership structure is unnecessary, but
  there must be evidence of a continuing collective identity beyond the immediate
  encounter or task. The peaceful desert orcs and Heroes of the Great War qualify
  as identifiable communities or established groups. A shared mission, coordinated
  action, or group rescue alone does not establish an organization. Exclude
  transient expeditions, temporary gatherings, and incidental crowds unless the
  source establishes a persistent group identity; also exclude generic species,
  languages, and populations. **Mawar Episode 1 calibration:** the merfolk recovery
  expedition is a transient group, not an organization. Keep it in exclusions;
  individually qualifying members such as Illius remain NPCs.
  Distinguish a settlement and its residents from a separately established tribe,
  faction, institution, or other organized body. Shared residence, persistence,
  and a liaison with another town do not by themselves make a settlement an
  organization. Do not relabel a place as a community to fit the entity kinds.
  **Mawar Episode 2 calibration:** the lizardfolk settlement south of Hamri was
  initially included as an organization with **medium** confidence because Benat
  served as its liaison. The user excluded it as a settlement; the liaison did
  not establish a separate group identity. Place references belong to scene mapping.

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

**Mystery clues have a lower inclusion threshold.** Mysterious figures and
entities implicated in specific strange events can be worth retaining even when
briefly mentioned or speculative: they may become important later. A supported
later identity match strengthens that case. **Mawar Episode 1 calibration:** keep
the suspected newcomer linked to Azar, with the later-identification flag, because
the phantom-ship mystery and later match give the reference value. Preserve the
session's uncertainty and descriptive label; do not assert a speculative event
as fact, predict later significance, or inflate this session's importance tier.
Strange events are context for identifying referents, not a new entity kind.
Reconsider borderline exclusions under this rule rather than requiring an
already established name, direct encounter, or demonstrated later payoff.

**Dunmari Frontier exception:** when YAML identifies that campaign, track the
party's ladders as `npc` companions, including equipment use. This does not assert
animation or action. Match the Ladder page when supported and distinguish current
and destroyed ladders; a passing predecessor joke need not create a record.
Do not apply this convention to other campaigns.

## Assess importance in this session

Assign every included entity `importance: star | supporting | cameo` after reading
the complete session. Apply the same session-relative standard to all four kinds.
The PCs are the real protagonists; assess prominence relative to the other
non-PC entities, never by equality with the players or by campaign-wide fame.

- **Star:** a significant part of this session: a key ally or enemy, or a major
  participant in several important encounters. One decisive, sustained encounter
  can also establish this role. There is no quota: zero is valid, often there is
  one, and more than a couple is rare. A group whose members comparably drive
  important action is a legitimate exception; do not arbitrarily demote members
  to meet a numeric cap.
- **Supporting:** the entity has meaningful involvement in at least one scene,
  through a substantive conversation, negotiation, or distinctive consequential
  interaction. It need not dominate the session. Fighting an unnamed creature
  does not by itself make that creature supporting.
- **Cameo:** every other included entity. A brief description, qualifying item action,
  mention, or discovery can merit inclusion while remaining a cameo.

Inventory eligibility and importance are separate. Do not add otherwise excluded
generic monsters or incidental nouns just to classify them as cameos. Judge
substance, agency, and consequences, not name counts, transcript length, combat
rounds, or the amount of available vault lore. A long search, approach, or rules
discussion does not promote its target. Preserve representative source evidence
for the rating, expanding occurrence windows only when needed to review it.

Extensive lore about a character does not itself establish supporting involvement.
A historical figure can remain a cameo even when the party discusses their work
at length or investigates sites and objects they left behind. Assess the figure's
involvement in this episode separately from the volume of lore. Meaningful indirect
involvement can qualify; physical presence is not required. **Mawar Episode 2
calibration:** Airion the Mistspeaker is a cameo despite substantial lore about
his research, inscriptions, tower, and well, because his own involvement is minimal.
Retain useful evidence without raising importance to accommodate it.

**Mawar Episode 3 calibration:** Hiyasa is an approved star, while the stone
guardian of Yerkir-khor is supporting. The guardian was proposed as a star with
medium confidence and corrected by the user. A principal combat opponent's
tribute negotiation and climactic battle do not automatically establish star
importance. See the [episode calibration](references/importance.md#mawar-episode-3-calibration);
a single encounter can still qualify under the general star standard.

Compare the proposed tiers across the session in the semantic pass. Recheck every
star against the relative standard and the absence of a quota. Use the calibration
cases to distinguish a supporting entity's meaningful scene from a cameo's brief
moment. Importance guides later extraction depth; it is not a word count, identity
confidence, permanent biography attribute, or a claim of direct interaction.

## Match identities

Search filenames first, then frontmatter names/aliases, spelling variants, both
sides of wikilinks, and backlinks. Candidate discovery can use an existing index;
do not persist another registry. Inspect and read complete candidate/supporting
notes, including uncertainty/status comments. Exact spelling alone is insufficient
when role, geography, time, or context disagrees.

Use clear later material to resolve an unnamed/masked identity. Choose its `note`,
set `identifiedLater: true`, and keep `label`/`names` faithful to what the entity
was called in this session. Inspect and read the supporting page. For
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

For an item specifically examined in the **Mirror of the Past** during this
session, set `examinedInMirrorOfPast: true` and include an occurrence showing the
actual examination. This optional v4 item flag records an event, not importance
or proof that the vision is literally true. A proposal to examine it, an earlier
session's examination recalled in dialogue, mere appearance within another item's
vision, or use of the Mirror of Soul Trapping does not qualify. Do not flag the
Mirror of the Past itself just because it was used. Leave the flag absent when
the event has not been established; do not infer it from an item name or lore.
Preserve the flag in reviews and downstream projection.

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
Entity records have no generic `reason` field. Keep evidence, candidates,
confidence, the focused `confidenceExplanation` below, and later-identification flags. Optional `names`
contains useful source variants/titles, not copied vault aliases.

**Confidence estimates whether the agent's complete proposed decision is correct**
under the evidence and calibrated rules: inclusion, kind, identity grouping,
vault match or deliberate lack of one, and session importance. It is the agent's
own uncertainty about that judgment, not a measure of how explicit the transcript
is, how much lore exists, or how certain the characters are about an in-world claim.

- **High:** strong grounds to expect the whole decision to be correct, with no
  material unresolved alternative. An understood lack of a vault page or a
  faithfully preserved in-world uncertainty need not reduce this confidence.
- **Medium:** the proposed decision is favored, but a plausible alternative could
  change a material part of it.
- **Low:** the proposed decision is tentative; weak evidence or a genuine grey
  area leaves substantial doubt that the inclusion, classification, match, or
  importance judgment is correct.

A clear name or identity match cannot compensate for weak confidence in inclusion
or importance. State which judgment is uncertain when presenting a medium/low
decision. A human-reviewed status records the user's decision separately; approval
does not automatically change the agent's confidence to high.

For each new or revised **medium/low-confidence** decision, record
`confidenceExplanation` as one short sentence of at most 40 words, identifying the
uncertainty that controls the rating. For example: “The name fits the vault note,
but the source does not distinguish two plausible guides.” A **high-confidence**
decision may also have a sentence when it adds useful context; omit filler.
The explanation should address the actual inclusion, grouping, match, type, or
importance judgment, supported by the inspected evidence. It is separate from
exclusion reasons and human change notes. Preserve unchanged legacy decisions and
protected human records without inventing retrospective explanations. New or
changed agent-authored medium/low records need the field before saving; existing
records remain readable without it. The desktop reviewer shows it alongside the
confidence badge in the queue and inside Details on the main map.


Use feedback to calibrate future estimates as well as selection rules. Record
instructive mistakes with the original decision and confidence, the correction,
and the reasoning that led to overconfidence. Do not describe an original high
rating as low merely because the error is clear after feedback. In Mawar Episode 2:

- **Airion:** originally `supporting` with **high** confidence; the user corrected
  him to `cameo`. The agent mistook extensive discussion of his historical work
  for meaningful involvement in this episode.
- **Wazir's mechanical flying fish:** originally included as an NPC companion with
  **high** confidence; the user excluded it as routine ability activation and
  specified that the initial judgment should have had **low** confidence. The
  agent mistook a distinctive appearance and repeated scouting for ongoing identity.
- **Cloak of the Manta Ray:** originally included as an item cameo with **high**
  confidence; the user excluded it as routine use of a PC magic item. The agent
  treated a useful application of its standard power and lending it to an ally
  as sufficient significance, overextending the lower magic-item threshold.

Start `unreviewed`. Make a **distinct semantic pass** over the whole inventory,
exclusions, importance tiers, identity-bearing speech, and chosen notes before `automatedReviewed`.
Validation is not review. `humanReviewed` requires explicit review of that actual
entity decision; approval of scenes, the skill, or broadly correct inclusions does
not approve every row. Preserve stable IDs and earlier human decisions. Changed
decisions return to `unreviewed` until checked. Vault-note content changes do not
block processing or invalidate recorded human decisions. Transcript/session input
changes require explicit human confirmation before continuing; confirmation keeps
existing decisions and is not semantic rechecking. Guarded saves protect existing human-reviewed records and prevent new agent-authored
human approvals. A human can reopen a record in the reviewer before agent revision.

When the user requests confidence-based calibration, review every medium/low
decision plus a random sample of four remaining high-confidence decisions per
session, unless they specify another scope or sample size. Include uncertainty
about exclusions as well as inclusions. Follow the
[sampling procedure](references/review-workflow.md#confidence-based-calibration);
preserve the requested one-at-a-time presentation. Unsampled entries retain their
actual automated review status, and completing this selected queue is sufficient
to move to the next session within an authorized batch.

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
python3 -B HELPER --session-yaml YAML preview --importance supporting
python3 -B HELPER --session-yaml YAML preview --entity e001
```

`NOTE_PATH` is an actual vault-relative note path. Before reading notes, inspect
**every** chosen, candidate, and supporting page with repeated `--note` flags,
including unchanged records on revision. Omit that flag
when no pages are involved. Retain `inputDigest` and `mapSha256`. Notes are live
references: their contents are not hashed or included in the input digest, and
ordinary vault edits do not require a new processing run. Inspect newly consulted
paths and read the relevant current notes for research. Use `evidenceNotes` for
supporting pages outside chosen/candidate targets.

Save a complete proposal through stdin or a temporary file using the inspected
digest. Intentional revisions also need the inspected `--expect-sha256 HASH`.
The helper rechecks transcript/session inputs and map concurrency, validates vault
paths, and uses the shared directory lock and atomic write. It does not compare
vault-note content SHAs. Legacy `inputs.vaultNotes` hashes are ignored and omitted
by new saves. Do not edit stored fingerprints manually.

When `inspect` reports `sourceChanges`, show the changed transcript/session inputs
and ask the human whether to continue with the current revision. This task's
general authorization is not confirmation of a future transcript revision. Only
after explicit confirmation, use the inspected current digest and map hash:

```bash
python3 -B HELPER --session-yaml YAML confirm-sources --expect-input-digest DIGEST --expect-sha256 HASH
```

This records a human `confirmSourceChanges` history event and updates source
fingerprints without changing entity decisions/statuses or source/YAML files.
Reinspect afterwards. If either guard fails, show the new revision and obtain a
fresh confirmation. Unknown UIDs or broken whole-turn references still require
evidence repair; confirmation cannot waive structural validation. The Obsidian
reviewer offers the same explicit **Continue with current transcript** action.

New saves use
v4 and require importance on every entity. Existing v3 maps remain readable with
importance explicitly unassessed; never fill missing tiers with a default. To
upgrade, review the complete session and assign tiers, preserving identity
decisions, IDs, evidence, and unchanged fields. Whole-record review must cover the
new assessment; earlier identity approval alone does not establish that. Legacy
v1 additionally requires source/identity rechecking; v2 also requires removing
entity `reason` fields and wrapping each exclusion's source in an occurrence array.
Use the inspected old map hash for any upgrade. Do not silently migrate attestations.

Verify current confirmed transcript inputs, focused whole-turn evidence, identity grouping, stable
IDs, duplicates, importance, exclusions, and all medium/low decisions. Present an entity-first
review: uncertain/unreviewed records first, clear matches compactly, exclusions
separately, later-identity flags visible even at high confidence. Open evidence
on demand. `--kind npc` and the other kinds filter the preview; unclassified
exclusions remain in the full view. Hand off map path, review performed, and
material questions; do not require approval of every clear match.

## Maintenance

Install [requirements](requirements.txt). Helpers require Python 3.9+; tests use
Python 3.10+. Run
`python3 -B -m unittest discover -s .agents/skills/check-session-entities/tests -v`.

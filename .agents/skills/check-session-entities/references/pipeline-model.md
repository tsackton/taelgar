# Session interaction pipeline: structures and integration contract

**Development checkpoint, not a production-ready workflow.** Reduction, scene
mapping, and entity checking run on `main`. Assisted human review, Obsidian review
integration, and generation of the final session enrichment remain unfinished.
The current Python helpers validate structure and protect writes; they do not
decide identities or prove that an agent reviewed the evidence.

This document specifies the intermediate formats and the concrete **v7 final
model**, including its schema, read-only validator, and map projection. Interaction
generation and publication are not implemented here. The current formats are specified in [scene-map format](../../map-transcript-scenes/references/format.md),
[entity-map format](format.md), and [reduction draft contract](../../prepare-interaction-transcript/references/format.md).

## Pipeline and ownership

```text
session YAML + registered polished transcript
    → optional conservative reduction draft
    → scene map + YAML date compatibility assessment
    → entity map + identity/vault-link checking
    → assisted review of selected decisions                 [not implemented]
    → interactions + final session.json + processing data  [not integrated]
```

The target is bulk processing roughly 150–200 sessions with selective human
attention. Session dates, PC identity, visited locations, and entity vault links
are the most consequential claims. Scene granularity and interaction details
are lower stakes; flavor quotations and convenient transcript links are lower
stakes still. Favor extraction and short navigation aids over generated narrative.

| Artifact | Owner and purpose | Current status |
| --- | --- | --- |
| `cleaned/<stem>-session.yaml` | Canonical campaign/session metadata and source declarations. | Existing pipeline; read-only in these new stages. |
| Registered polished Markdown | Canonical readable transcript, retaining original UID mapping comments. | Existing `process-transcript` output. |
| `<stem>-interactions-draft.md` | Conservative, reversible reading view. | Reduction skill writes this file only. |
| `<stem>-scene-map.json` | Source partition, scene context, date assessment and findings. | Scene skill writes this file only. |
| `<stem>-entity-map.json` | Entity selection, identity matches, representative evidence and review confidence. | Entity skill writes this file only. |
| Review artifact / decision store | Obsidian-friendly review, explicit user decisions and resumability. | Storage and workflow still to design; no prescribed final home. |
| `session.json` | Canonical structured enrichment accompanying YAML. | v7 schema, validation, and candidate map projection implemented; interaction generation/publication not integrated. |
| `session-processing-data.json` | Input provenance, processing evidence, excluded blocks and findings. | Earlier branch prototype; integration with new maps still needed. |

Do not build a second session manifest or a competing scene division. The earlier
end-to-end prototype is on `codex/campaign-interactions-review`, under
`.agents/skills/extract-campaign-interactions/`. Its v6 schemas and validators are
reference material, not an instruction to merge that branch or enable its workflow.

## Session YAML and source references

The YAML owns campaign identity, session number, real-world date, in-world start/end
dates and optional times, participant roles, and transcript artifacts. There is no
separate guest-versus-recurring-PC distinction in the enrichment. Resolve PC roles
from YAML and character pages; speaker mappings alone do not establish attendance.

Current preflight requires `sourceType: transcript`, valid `realWorldDate`, `drStart`,
`drEnd`, and a locatable `transcriptProcessing.artifacts.polishedMarkdown` path.
Read optional registered cleaned text to verify the original UID mapping. Paths
inside `transcriptProcessing.artifacts` are bundle-relative. Propose concrete YAML
repairs if primary source paths are broken; do not guess substitute inputs.

Every structured source reference is a discriminated union. Only one kind is
implemented now:

```json
{
  "kind": "transcript",
  "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
  "startUid": "u0013",
  "endUid": "u0137"
}
```

`sourceId` is a dotted YAML artifact key, not a locally invented source ID. Ranges
are inclusive, contiguous, and in transcript order. A polished turn may combine
several UIDs; multiple turns may share one UID. Boundaries respect both whole turns
and whole UIDs. Original comments also contain character offsets, but these stages
do not invent sub-turn source ranges. Recording timestamps are not in-world time.

The model should later support authored accounts, emails, and other sources by
adding discriminated source kinds with suitable locators and YAML declarations.
No extractor for those sources is part of this checkpoint. Avoid hard-coding the
assumption that every future source is a transcript or that narrative chronology
always equals source order.

## Implemented scene map

Required envelope: `schemaVersion: 1`, `sessionYaml`, `inputs`, `scenes`,
`contextBlocks`, and, for new/revised saves, `dateValidation`. Optional `findings`.
`sessionYaml` is vault-relative. Inputs bind semantic YAML and source hashes;
adding the future `interactionExtraction` output pointer does not stale the YAML
digest, and neither do comment/formatting-only YAML changes.

| Scene field | Required? | Meaning |
| --- | --- | --- |
| `index` | Yes | Positive, unique scene index in source order. Shared by downstream references. |
| `source` | Yes | One contiguous original-source range. |
| `type` | No | `conversation`, `exploration`, `combat`, or `travel`. |
| `location` | No | Verified vault-relative place-note path, including `.md`. |
| `locationDetail` | No | Narrative subplace, such as a room or camp within that place. |
| `dateStart`, `dateEnd` | No | Supported in-world ISO dates. |
| `time` | No | Supported time description, such as “after dinner.” |
| `aiSummary` | No | At most 25 words; navigation aid, not replacement narrative. |

Optional place/date/time values may be omitted or null. There is no scene title,
participant list, “other NPCs,” or individual scene confidence. Meaningful moves,
time skips and combat boundaries divide scenes; topic changes, minor mechanics,
and jokes do not fragment a conversation. Source order may revisit an earlier
moment. A later interaction may span several scenes.

`contextBlocks` have `kind`, `source`, and `aiSummary` (at most 25 words). Kinds are
`recap`, `loreDiscussion`, and `tableChatter`. Together with scenes they cover every
UID exactly once. They are **available context, not automatic extraction exclusions**.
Postgame clarification can contain important lore; a recap is not a newly played
event. Entity occurrences can point into these blocks.

`dateValidation` contains `result`, a brief `reason`, and source `evidence`:

- `consistent`: relative chronology fits YAML as its calendar anchor. Nobody needs
  to say the calendar date aloud. Afternoon-to-evening play can validate compatibility
  with a single-day span.
- `conflict`: clear contrary evidence; record a `dateConflict` finding with affected
  YAML fields and the actual source comparison. Do not automatically edit YAML.
- `insufficientEvidence`: a material timeline uncertainty prevents assessment,
  such as ambiguous travel that could exceed the YAML span. An unstated date alone
  does not qualify.

YAML may clarify unstated dates or extend beyond recorded action. Do not truncate
it to extracted scene dates. Legacy missing assessments display `notChecked`.
Other findings identify boundary, contextual-framing, or location questions.

## Implemented entity map

Required envelope: `schemaVersion: 1`, `sessionYaml`, `inputs`, `entities`.
Optional `exclusions` and `evidenceNotes`. Inputs bind the scene helper's input
fingerprints, the exact scene-map hash, and consulted vault-note hashes. Scene
changes invalidate dependent evidence. Changed consulted notes invalidate relying
on the old review; hashes do not prove that every possible note was searched or
detect newly created candidate pages elsewhere in the vault.

| Entity field | Required? | Meaning |
| --- | --- | --- |
| `id` | Yes | Stable session-local identity; preserve across edits. |
| `kind` | Yes | `npc`, `divine`, `item`, or `organization`. |
| `label` | Yes | Readable name or a source-grounded descriptive identity. |
| `occurrences` | Yes | Ordered, nonempty array of `{source}` evidence passages. |
| `review` | Yes here | Whole-entity confidence and review status. |
| `note` | No | Matched vault-relative `.md` page or null. |
| `names` | No | Useful source variants/titles, not copied vault aliases. |
| `candidates` | No | Plausible note paths while unresolved; cannot coexist with a definite `note`. |
| `reason` | Conditional | At most 40 words; required for unlinked or medium/low-confidence entities. |

An occurrence fits one existing scene or contextual block. The helper derives the
owning scene/context; it does not store another set of scene IDs. Occurrences are
representative retrieval passages, not every name/pronoun and not final interactions.
They do not establish attendance, presence, or a completed event.

Entity selection:

- **NPC:** named individuals and distinctive unnamed people who plausibly have a
  name. Omit generic crowds, every monster, and rumors of unspecified creatures.
- **Divine:** gods, named religious spirits, comparable divine beings, and named
  divine collectives. Meaningful religious mentions are worth tracking separately
  from NPC encounters. Clergy remain NPCs; supernatural origin alone is insufficient.
- **Item:** plot-significant objects and meaningful finding, acquisition, trade,
  loss, destruction, property discovery, or discussion of in-world lore, powers,
  limitations, and possible roles. Substantive discussion of a lore-rich artifact
  qualifies without actual use or a new revelation; proposed uses remain discussion.
  Omit ordinary treasure, incidental inventory mentions, and routine combat use of
  party gear. Extensive vault lore alone does not make routine use significant.
  Do not merge separate items merely because one generic item page describes their class.
- **Organization:** identifiable tribes, factions, institutions, and organized
  groups. Religious institutions belong here; divine collectives belong under divine.

Session PCs remain YAML-owned. A named companion not acting as this session's PC
can still be an entity; do not equate that with the player's attendance. A chosen
vault match can identify an unnamed speaker while `label` preserves how the source
describes them. Conflicting names or uncertain identity retain candidate matches.

`exclusions` are `{label, reason, source}` for plausible entity candidates omitted
with a specific reason. They do not exclude those source blocks from later use.
`evidenceNotes` records consulted pages that are neither chosen nor candidate
targets. A missing individual page can coexist with high-confidence identity.

`preview`, `preview --kind divine`, `preview --kind npc`, and `preview --entity ID`
render the inventory or selected original evidence without writing a review file.
Current local-path links are command-line conveniences; they are not an implemented
portable Obsidian navigation system.

## Review state and unfinished workflow

Review objects contain `confidence: high | medium | low` and
`status: unreviewed | automatedReviewed | humanReviewed`. Confidence covers the
whole record, not separate scores for every field. Entity-map review covers
selection, identity grouping, and the vault match. Automated review is a distinct
semantic pass; validation cannot supply it. Human review requires an actual user
decision for the selected entity, not approval of a scene example or the skill.

The helpers currently accept caller-authored review values. They do **not** yet
provide a guarded human decision/apply command, enforce immutability of human
decisions, record review history, or selectively reset only affected decisions.
The skills instruct the agent to preserve decisions and recheck changes; the
desktop review implementation must make that behavior concrete and testable.

The next workflow should support selective approval/correction, inclusion/exclusion,
candidate matching, identity merge/split, deferred questions, and rerunning selected
records without discarding accepted work. Those are requirements to design against,
not implemented commands or a settled review-document schema. Choose the review
artifact's home with the user; do not assume “processing log” is the final answer.
No mandatory human approval of every entity/session is intended.

## Final session.json v7

The final JSON is the canonical structured enrichment. YAML remains canonical for
metadata and sources. [session.schema.json](session.schema.json) is the normative
JSON Schema; [session_model.py](../scripts/session_model.py) checks source ranges,
references, paths, and exact quotations against the actual registered transcript.
The model version is **7**, independent of the intermediate maps' version 1.
The predecessor branch's v6 files are not silently upgraded or accepted as v7.

| Final root field | Required? | Purpose |
| --- | --- | --- |
| `schemaVersion` | Yes | Exactly `7`. |
| `sessionYaml` | Yes | Vault-relative canonical manifest reference. |
| `locations` | No | Deduplicated visited vault place paths, independently reviewed; mentioned places are not visits. |
| `scenes` | No | Reviewed scene records with the same scene fields/indexes described above. |
| `contextBlocks` | No | Indexed non-play passages, preserving recap/lore/chatter framing and source accounting. |
| `entities` | No | Final entity records described below. |
| `interactions` | No | Entity/party interactions anchored to scenes, or mentions anchored to contextual passages. |
| `review` | No | Aggregate consistency with YAML metadata and reviewed visited locations. |
| `sceneReview` | No | Review of the overall scene division and source accounting. |

There is no copied campaign name, session number, real-world date, PC/guest list,
source registry, or aggregate date span in the final JSON. These belong in YAML.
Optional collections can be absent or empty; optional note/place/date/time values
can be absent or null. Minimal structural validity is not evidence of readiness.
Unknown properties are rejected. The smallest valid document is
`{"schemaVersion": 7, "sessionYaml": "<vault-relative manifest path>"}`;
the manifest must resolve and pass preflight during source-aware validation.

Final context blocks require `index`, `kind`, and `source`; `aiSummary` is optional
and limited to 25 words. Kinds remain `recap | loreDiscussion | tableChatter`.
Their positive indexes form a **separate namespace** from scene indexes. Projection
assigns them in source order; consumers must bind dependent references to the input
map revision, as they do scene indexes. One contiguous range per block; no source
range can overlap another scene or context block. Complete source accounting means
every UID belongs to exactly one scene or context block. It does not require an
interaction for every block. Table chatter can remain accounted with no entities.

Final entity required fields: `id`, `kind`, `label`. Kinds are
`npc | divine | item | organization`. Optional: `note`, `aiSummary` (one per entity per session,
at most two sentences), `aiSuggestedFeaturedQuotes` (quote IDs), and `review`.
Intermediate `occurrences`, `candidates`, `names`, and selection `reason` are
processing/review evidence, not automatically additional final-entity fields.

Final interaction required fields: `id`, `entity` (entity ID), and `interaction`,
plus at least one nonempty anchor array: `scenes` (existing scene indexes) or
`contexts` (existing context-block indexes). Each array is ordered and unique.
The interaction vocabulary is:

- `interacted`: meaningful direct exchange/action; replaces the misleading “met.”
- `observed`: the party observes the entity without a direct exchange.
- `present`: the entity is known to be around but does not otherwise act.
- `mentioned`: discussed without establishing current participation.

Any interaction with a nonempty `contexts` array must be `mentioned`, even if it
also references scenes. A context-only mention needs no invented played scene.
When a direct exchange has related postgame commentary, keep the played exchange
anchored to its scenes and the commentary as a separate contextual mention. This
preserves what happened versus what was said about it. In-scene recollections or
hypotheticals also use `mentioned`; a scene anchor alone does not prove presence.

All four interaction types apply to divine entities under these same evidence
rules. Prayer, invocation, belief, and attributed intervention alone are mentions;
an explicitly played manifestation can be observed/present, and a supported direct
exchange can be interacted. No additional divine interaction taxonomy is needed.
Kind allows renderers to separate religious references from NPC encounters.

Optional interaction fields: `importance` (`star | supporting | cameo`), `knownAs`
(source-specific name), `aiSummary` (at most one sentence), `passages`, `quotes`,
and `review`. No separate `fought` type. Preserve a whole conversation as one
interaction through brief interruptions, even if it spans scenes. Importance is
an interaction judgment, not a permanent entity rank.

Passage required field: `source`. Optional: `relevance` (`primary | supporting`)
and `aiSummary` (at most one sentence). Usually one primary passage is enough;
additional passages recover meaningful discontinuous portions. No `purpose` field.
Passages are the meaningful parts of the interaction, not full-scene copies.

Quote required fields: `id`, `type`, `text`, `source`. One quote structure supports:

- `introduction`: wording introducing the entity, spoken by a PC or DM.
- `color`: a memorable line spoken by the entity.
- `whole`: the entire meaningful interaction is a short quotable passage, spoken
  by a PC or DM.

No separate attribution field was chosen. Quotes are verbatim original-source
text; never quote reduction labels or silently join across cuts. Significant NPCs
may have multiple pull quotes. `aiSuggestedFeaturedQuotes` references that entity's
existing quote IDs without duplicating text. Quote IDs are unique across the
session. Selected passages/quotes must fit within the union of their interaction's
linked scene/context ranges, with no unlinked gaps. Passages are ordered and do
not overlap. Quotes can select part of a turn's text, but their source locators
still respect whole turns/UIDs. Speaker/type interpretation and summary sentence
limits require semantic review, not just the mechanical validator.

### Validation and projection

Install the skill's [requirements](../requirements.txt) in the local Python
environment. Run from the vault root:

```bash
python3 -B .agents/skills/check-session-entities/scripts/session_model.py project --session-yaml PATH
python3 -B .agents/skills/check-session-entities/scripts/session_model.py validate PATH_TO_SESSION_JSON --require-coverage
```

Both commands are read-only and print JSON to stdout. `project` requires current
scene/entity maps, preserves scene indexes and entity identities, adds indexed
context blocks, and checks full coverage. It carries entity review values without
claiming a completed final review. It does not fabricate interactions, summaries,
quotes, an accepted aggregate location list, or aggregate review statuses. Explicit
redirection can save this **candidate**, but the helper never registers it in YAML.

`validate` without `--require-coverage` accepts partial working candidates and
reports unaccounted UIDs. With that flag, it requires complete scene/context
coverage. Neither mode establishes semantic accuracy or workflow completion;
`publicationReady: false` means this helper does not certify publication. It is
not a stored final-session field. Fingerprints and publication checks belong to
the processing workflow, rather than duplicated source metadata in session.json.

For a deliberate v6 migration, preserve compatible fields/IDs, review divine
classification, and reconstruct contextual ranges from the current source map.
Do not automatically turn old excluded blocks into scenes or discard their lore.
Update references and validate as v7; merely changing the version number is not a
migration. The old branch's v6 extractor/readers need explicit adaptation before
using this model. No existing session outputs are migrated by this checkpoint.

## Processing companion and remaining workflow integration

Keep fingerprints, review evidence/history, excluded source blocks with reasons,
metadata findings, and pipeline progress outside final narrative/enrichment records.
The earlier branch's `session-processing-data.json` has `schemaVersion`,
`sessionYaml`, `inputs`, `stage`, `fullTranscriptRead`, `excludedBlocks`,
`metadataFindings`, and `reviews`. Reuse useful infrastructure after reconciling
its semantics with these stages; do not declare the review-history location settled.

The v7 accounting rule is scenes plus context blocks. Processing exclusions are
annotations explaining why material produced no interaction or entity, not a
third coverage bucket and not permission to lose contextual lore. Keep source
ranges and reasons in that companion; entity-map exclusions remain the distinct
record of omitted entity candidates. Do not treat every contextual block as an
exclusion. The companion's persistence and review-history UI are not implemented
by the final-session validator.

Remaining workflow implementation:

1. Use the projection to transfer scene/entity decisions and stable IDs, then
   generate interactions from evidence without independently rematching everything.
   Bind the result to processing fingerprints and reset stale decisions appropriately.
2. Adapt downstream readers/renderers to v7, including separate divine views and
   contextual mentions. The final schema and their representation are defined above.
3. Review the aggregate visited-location list independently. Scene links exist,
   but there is no implemented independent location review in the new entity skill.
4. Design safe review application, change invalidation and explicit completion.
   Only then wire up YAML output registration. The earlier branch uses:

   ```yaml
   interactionExtraction:
     sessionJson: ../interactions/session.json
     processingData: ../interactions/session-processing-data.json
   ```

   These output paths are relative to the YAML directory, unlike bundle-relative
   transcript artifact paths. Current new stages never append these pointers.

Beats/facts/recaps remain optional automated-review hints, not canonical source
registries or extraction prerequisites. Do not integrate or overwrite existing
note pipelines as a side effect of building the Obsidian review workflow.

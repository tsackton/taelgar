# Provisional entity map v2

Output: `cleaned/<stem>-entity-map.json`. Session metadata and source paths stay in
YAML. The helper supplies `schemaVersion: 2`, `sessionYaml`, and `inputs`.
The polished transcript is sufficient; no scene map or reduction draft is required.

Author a proposal with required `entities` (possibly empty), optional `exclusions`
and `evidenceNotes` (vault-relative consulted note paths). No final `session.json`
or source edits are made.

Each entity requires:

| Field | Purpose |
| --- | --- |
| `id` | Stable session-local identifier, e.g. `e001`; retain on revision. |
| `kind` | `npc`, `divine`, `item`, or `organization`. Divine beings and named divine collectives are distinct from ordinary NPCs. |
| `label` | Readable identity, or a source-based description for an unnamed individual. |
| `occurrences` | Nonempty ordered array of `{source}` identity-bearing passages. |
| `review` | Whole-entity `{confidence, status}` using the agreed review vocabulary. |

Optional fields: `note` (existing vault-relative `.md` path or null), `names`
(distinct source variants/titles), `candidates` (plausible vault note paths while
unresolved), `identifiedLater` (boolean, omitted or false by default), and `reason`
(at most 40 words). `identifiedLater: true` requires a chosen `note` and a `reason`
identifying the later name and supporting context. Keep `label` and `names` as
known in the session. A clear later match may have high confidence; this flag does
not mean the identity is unresolved or the characters already knew it.
Require `reason` when `note` is absent or confidence is medium/low as well.
A chosen `note` and competing `candidates` cannot
coexist: retain uncertainty instead of emitting a definite match. Two entities
cannot resolve to the same page; revisit a possible duplicate or overly broad page.

```json
{
  "entities": [{
    "id": "e001",
    "kind": "npc",
    "label": "Unnamed hunting-camp spokesman",
    "reason": "A distinct speaker with a description and sustained dialogue; no matching person page found in searched names and camp references.",
    "occurrences": [{"source": {
      "kind": "transcript",
      "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
      "startUid": "u0037", "endUid": "u0044"
    }}],
    "review": {"confidence": "high", "status": "unreviewed"}
  }]
}
```

These ranges are illustrative. Use actual whole-turn UID boundaries from the
polished transcript. Occurrences need no scene/context ownership and may cross
future scene boundaries. Keep evidence focused and preserve the surrounding
speech's recap, speculation, or played-action framing during review. No scene
indexes or interaction classifications are authored. Occurrences are representative
retrieval passages, not exhaustive name-token offsets or evidence of attendance.
A recap or future plan remains such
even when it names a real entity. Multiple entities may share a source passage.
Divine occurrences include meaningful religious mentions and invocations; they do
not imply a direct encounter or prove an attributed intervention. No extra fields
are required for divine entities. Clergy remain NPCs, and religious institutions
remain organizations.

An exclusion is `{label, reason, source}`; it records a meaningful entity candidate
omitted from this stage, not an excluded source block. `reason` is at most 40 words.

`inputs` contains:

- `sessionInputs`: the scene helper's YAML/source fingerprints, not metadata values.
- `vaultNotes`: byte hashes of selected/candidate/evidence notes, supplied by the
  helper from inspected files. Changed notes require rechecking affected decisions.

The inspection digest binds both. The reader refuses stale inputs rather
than displaying an old automated/human status as current. Reinspect, revise the
proposal, and save with the expected old output hash after semantic rechecking.
Scene-map creation, revision, or deletion and changes to a reduction draft do not
stale evidence pointing to original polished speech. Only the entity map is persisted
during an ordinary run; previews and source windows go to stdout. No copied
transcript or separate review log.

`preview` groups review priorities and produces one compact row per entity plus
exclusions. `preview --entity ID` opens that entity's rationale, candidates, and
original polished passages with direct UID links. `preview --kind divine`
or `--kind npc` separates those inventories for review; filtered views omit the
unclassified exclusions, which remain available in the full preview. Neither view
silently accepts an entity. `humanReviewed` requires actual user review; passing
validation never sets it. Automated status is an agent attestation, not a guarantee.
Later identifications display an explicit flag beside the chosen vault match;
their rationale remains visible at high confidence. `identifiedLater` is processing
metadata retained in the map, not a new final v7 entity field.

The core fields feed the concrete [v7 session model](pipeline-model.md#final-sessionjson-v7),
whose [schema](session.schema.json) includes `divine`. The read-only
`session_model.py project` preserves those fields and scene/context accounting.
Projection separately loads and validates a current scene map; entity checking
can finish before one exists. Occurrences inform retrieval, not whole-conversation
grouping; that later stage may join several scenes. Preserve selection decisions and identities while generating
interactions. Assisted review/application remains unfinished; helpers accept
caller-authored review values and do not yet enforce human-decision protection.

Legacy version 1 maps bound decisions to a scene-map hash. They are rejected with
an explicit recheck message, not silently upgraded. For an intentional version 2
revision, inspect the existing output hash, recheck source and note evidence,
preserve stable IDs and human decisions, and use the normal guarded save.

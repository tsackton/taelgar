# Provisional entity map v3

Output: `cleaned/<stem>-entity-map.json`. Session metadata and source paths stay in
YAML. The helper supplies `schemaVersion: 3`, `sessionYaml`, and `inputs`.
The polished transcript is sufficient; no scene map or reduction draft is required.

Author a proposal with required `entities` (possibly empty), optional `exclusions`
and `evidenceNotes` (vault-relative consulted note paths). No final `session.json`
or source edits are made.

Each entity requires:

| Field | Purpose |
| --- | --- |
| `id` | Stable session-local identifier, e.g. `e001`; retain on revision. |
| `kind` | `npc`, `divine`, `item`, or `organization`. Divine beings and named divine collectives are distinct from ordinary NPCs. |
| `label` | One session-facing display name, or a source-based description for an unnamed referent. |
| `occurrences` | Nonempty ordered array of `{source}` identity-bearing passages. |
| `review` | Whole-entity `{confidence, status}` using the agreed review vocabulary. |

The four identity fields have separate purposes:

| Field | Meaning |
| --- | --- |
| `label` | Required single display label for this session. Preserve what the session knew, including a descriptive unnamed identity. |
| `note` | Optional chosen vault-relative `.md` page, or null. It can resolve the identity even when the session did not use that page's name. |
| `names` | Optional array of names, spelling variants, or titles actually used for this referent in the session. These are text, not note paths or copied vault aliases. Omit when there are no useful additional variants. |
| `candidates` | Optional array of plausible vault-relative note paths while the match is unresolved. These are alternatives, not extra confirmed matches. |

Optional `identifiedLater` is a boolean, omitted or false by default.
`identifiedLater: true` requires a chosen `note`. Keep `label` and `names` as
known in the session. A clear later match may have high confidence; this flag does
not mean the identity is unresolved or the characters already knew it.
Entity records do not accept `reason`; evidence and confidence remain explicit.
A chosen `note` and competing `candidates` cannot
coexist: retain uncertainty instead of emitting a definite match. Two entities
cannot resolve to the same page; revisit a possible duplicate or overly broad page.

```json
{
  "entities": [{
    "id": "e001",
    "kind": "npc",
    "label": "Unnamed hunting-camp spokesman",
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
A recap or future plan remains such even when it names a real entity. Multiple
entities may share a source passage.
Divine occurrences include meaningful religious mentions and invocations; they do
not imply a direct encounter or prove an attributed intervention. No extra fields
are required for divine entities. Clergy remain NPCs, and religious institutions
remain organizations.

An exclusion is `{label, reason, occurrences}`; it records a meaningful entity
candidate omitted from this stage, not an excluded source block. `reason` is at
most 40 words. `occurrences` uses the same nonempty, ordered array of `{source}`
passages as an included entity. Ranges must respect whole turns/UIDs and cannot
overlap within one record. Keep more than one passage when it supports reviewing
the exclusion across separate appearances. Previews show every retained range.

`inputs` contains:

- `sessionInputs`: shared YAML/source fingerprints, not metadata values.
- `vaultNotes`: byte hashes of selected/candidate/evidence notes, supplied by the
  helper from inspected files. Changed notes require rechecking affected decisions.

The inspection digest binds both. The reader refuses stale inputs rather
than displaying an old automated/human status as current. Reinspect, revise the
proposal, and save with the expected old output hash after semantic rechecking.
Scene-map creation, revision, or deletion and changes to a reduction draft do not
stale evidence pointing to original polished speech. Only the entity map is
persisted during an ordinary run; previews and source windows go to stdout.

`preview` groups review priorities and produces one compact row per entity plus
exclusions. `preview --entity ID` opens that entity's candidates and
original polished passages with direct UID links. `preview --kind divine`
or `--kind npc` separates those inventories for review; filtered views omit the
unclassified exclusions, which remain available in the full preview. Neither view
silently accepts an entity. `humanReviewed` requires actual user review; passing
validation never sets it. Automated status is an agent attestation, not a guarantee.
Later identifications display an explicit flag beside the chosen vault match,
including at high confidence. `identifiedLater` is processing
metadata retained in the map, not a new final v7 entity field.

The core fields feed the concrete [v7 session model](pipeline-model.md#final-sessionjson-v7),
whose [schema](session.schema.json) includes `divine`. The read-only
`session_model.py project` preserves the entity core and scene/context accounting.
Projection separately loads and validates a current scene map; entity checking
can finish before one exists. Occurrences inform retrieval, not final conversation
grouping. The [review workflow](review-workflow.md) covers manual feedback; helpers
accept caller-authored review values without enforcing human-decision protection.

Version 2 maps require explicit removal of `entities[*].reason` and wrapping each
exclusion's former `source` as `occurrences: [{source: ...}]`, followed by a guarded
v3 save using the inspected old output hash and current input digest. Verify inputs
and preserve every other record field, including IDs and human decisions; removing
this prose alone does not change those decisions. Exclusion reasons remain required.

Legacy version 1 maps additionally bound decisions to a scene-map hash. Recheck
source and note evidence before an intentional v3 save; do not silently carry
stale attestations forward. No version is silently upgraded by the reader.

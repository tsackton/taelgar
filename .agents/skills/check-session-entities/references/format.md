# Provisional entity map v1

Output: `cleaned/<stem>-entity-map.json`. Session metadata and source paths stay in
YAML. The helper supplies `schemaVersion: 1`, `sessionYaml`, and `inputs`.

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
unresolved), and `reason` (at most 40 words). Require `reason` when `note` is absent
or confidence is medium/low. A chosen `note` and competing `candidates` cannot
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
selected scene map. An occurrence stays inside one scene/context block. Its owner
is derived from the scene map; no new scene indexes or interaction classifications
are authored. Occurrences are representative retrieval passages, not exhaustive
name-token offsets or evidence of attendance. A recap or future plan remains such
even when it names a real entity. Multiple entities may share a source passage.
Divine occurrences include meaningful religious mentions and invocations; they do
not imply a direct encounter or prove an attributed intervention. No extra fields
are required for divine entities. Clergy remain NPCs, and religious institutions
remain organizations.

An exclusion is `{label, reason, source}`; it records a meaningful entity candidate
omitted from this stage, not an excluded source block. `reason` is at most 40 words.

`inputs` contains:

- `sessionInputs`: the scene helper's YAML/source fingerprints, not metadata values.
- `sceneMapSha256`: exact scene-map byte hash; revisions require rechecking references.
- `vaultNotes`: byte hashes of selected/candidate/evidence notes, supplied by the
  helper from inspected files. Changed notes require rechecking affected decisions.

The inspection digest binds all three. The reader refuses stale inputs rather
than displaying an old automated/human status as current. Reinspect, revise the
proposal, and save with the expected old output hash after semantic rechecking.
Changes to a reduction draft alone do not stale evidence pointing to original
polished speech. Only the entity map is persisted during an ordinary run; previews
and source windows go to stdout. No copied transcript or separate review log.

`preview` groups review priorities and produces one compact row per entity plus
exclusions. `preview --entity ID` opens that entity's rationale, candidates, and
original polished passages with scene/context labels. `preview --kind divine`
or `--kind npc` separates those inventories for review; filtered views omit the
unclassified exclusions, which remain available in the full preview. Neither view
silently accepts an entity. `humanReviewed` requires actual user review; passing
validation never sets it. Automated status is an agent attestation, not a guarantee.

The core fields feed the concrete [v7 session model](pipeline-model.md#final-sessionjson-v7),
whose [schema](session.schema.json) includes `divine`. The read-only
`session_model.py project` preserves those fields and scene/context accounting.
Occurrences inform retrieval, not whole-conversation grouping; that later stage may
join several scenes. Preserve selection decisions and identities while generating
interactions. Assisted review/application remains unfinished; helpers accept
caller-authored review values and do not yet enforce human-decision protection.

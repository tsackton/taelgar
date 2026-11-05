# Interactions v1

The authored artifact is `cleaned/<stem>-interactions.json` in the existing session
bundle. [interactions.schema.json](interactions.schema.json) is the structural
definition. It is independent of the older v7 `session.json` model. No automatic
conversion, publication, YAML registration, or Obsidian review UI is provided.

## Document and provenance

| Field | Meaning |
| --- | --- |
| `schemaVersion` | Exactly integer `1`. |
| `sessionYaml` | Canonical vault-relative session manifest path, using `/`. |
| `inputs.transcript.sourceId` | Exactly `transcriptProcessing.artifacts.polishedMarkdown`; resolve its path through YAML. |
| `inputs.transcript.sha256` | SHA-256 of the polished source's bytes. |
| `inputs.entityMap.path` | Canonical vault-relative path of this session's entity map. |
| `inputs.entityMap.sha256` | SHA-256 of that map's bytes, binding local entity IDs to a revision. |
| `interactions` | Array of exchange records ordered by source start, then end. Empty is valid. |

Hashes use 64 lowercase hexadecimal characters. Campaign, session dates, PC
roles, source paths, and other session metadata stay in YAML. Names, matched vault
notes, session importance, and mirror-examination flags stay in the entity map.
Local roles do not replace or copy that map's session importance.

## Each exchange

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | Stable session-local interaction identifier, conventionally `i001`. Unique in this document; do not renumber surviving records on revision. |
| `title` | Yes | Short navigation label, not extraction reasoning. |
| `entities` | Yes | Nonempty array of `{id, role, action}` references to the bound map. IDs are unique within this array; at least one entry is a star. |
| `source` | Yes | Inclusive `{startUid, endUid}` original-source bounds, including internal cuts. |
| `lines` | Yes | Extracted Markdown, one physical line per entry, with original source-span comments and marked cuts. |
| `reviewContext` | Yes | `{before, after}` arrays of the five adjacent original transcript text lines outside the interaction's complete source range. |
| `review` | No | Extraction-specific confidence/status and conditional reason. |

Entity `role` is `star | supporting | cameo` **within this exchange**. Stars are
the focal entities; supporting entries contribute meaningfully or provide necessary
context; cameos have brief relevant involvement. One short interaction can star an
entity that is only a cameo in the session map. Multiple stars are permitted. Other
PCs/NPCs can speak without each becoming a star. Only mapped identities can have
array entries; PCs' speech retains YAML-owned roles in the text.

Entity `action` is `interacted | observed | present | mentioned`, describing
involvement relative to the party. Use the most substantive supported involvement
in this exchange: direct action/exchange, observation without direct exchange,
mere established presence, or discussion without establishing current participation.
Do not infer direct encounters from recaps, reported history, belief, or prayer.
An absent entity can be a star with `mentioned` action. Do not list entities whose
contributions were entirely cut or inflate retained context to justify a listing.

`lines` joins with `"\n"` to produce Markdown. Entries may be empty strings, but
may not contain embedded LF/CR characters; the collection must contain nonblank
text. Preserve original speaker labels, wording, punctuation, uncertainty, and
source comments. Combine consecutive omitted turns into one source comment containing every original span in order, followed by one `((short description))` for the run. Retained speech separates cuts. The validator flags adjacent identical whole-turn cut labels. Retain necessary attribution
and reported/recap/speculative framing in the original text; there is no separate
`framing` field. A source range never authorizes silently joining distinct accounts.

One exchange can cross geographic scene boundaries. Distinct records may overlap
when necessary, but store a shared exchange with several stars once. There is no
scene-map requirement, source-coverage claim, summary, quote collection, separate
focal list, or copied entity metadata in this format. Describe the reading scope
and unresolved limitations in chat at handoff. An empty or partial collection does
not establish exhaustive session coverage.

## Review

`reviewContext.before` and `reviewContext.after` each contain exactly five
nonblank physical text lines from the registered polished transcript, or all
available lines when a transcript edge leaves fewer than five. Retain wording,
speaker labels, order, and internal whitespace exactly. Do not count blank lines,
UID/offset comments, visual wrapping in the browser, or editorial cut markers.
The lines immediately precede `source.startUid` and follow `source.endUid`,
respecting whole-turn/shared-UID boundaries. When setup is summarized within the
source range, context goes outside that full range, not inside the summarized setup.

These arrays are review material, separate from the extracted `lines` and from
confidence/status. Do not widen the interaction bounds or add entities solely
because they appear in this context. An empty array is valid only at a matching
transcript edge. Missing context is not equivalent to an empty array; populate
it from the source when updating an earlier prototype artifact.

Use the helper to generate the object deterministically:

```bash
python -B .agents/skills/extract-entity-passages/scripts/interactions.py context --session-yaml VAULT_RELATIVE_SESSION_YAML --start-uid START_UID --end-uid END_UID
```

Readable reviews display these lines **by default**, immediately before and after
the interaction, in smaller muted/grey text with clear boundary labels. Keep
them legible; do not use low-opacity body text or hide them in a disclosure.
Individual internal cut and summary disclosures show the raw omitted/summarized
source text only. Do not add five-line windows around those internal blocks;
before/after context belongs only to the whole interaction.

When present, `review` requires:

- `confidence`: `high | medium | low` for the correctness of the whole extraction.
- `status`: `unreviewed | automatedReviewed | humanReviewed`.
- `reason`: nonblank single-line explanation **required for medium/low confidence**;
  optional for high confidence. Explain a specific uncertainty in selection,
  boundaries, roles/actions, text, or cuts, rather than a biography or reasoning trace.

Review is optional for compatibility; new agent records should include it. Omission
records no attestation. Start unreviewed, attest automated review only after a
distinct source comparison, and attest human review only following actual user
review of that exchange and its cuts. Preserve human edits and accepted records
on reruns; a schema validator does not enforce authorization or certify review.

## Validation

Requires Python 3.9+, PyYAML, and jsonschema; see [requirements](../requirements.txt).
From the vault root:

```bash
python -B .agents/skills/extract-entity-passages/scripts/interactions.py validate PATH_TO_INTERACTIONS_JSON
```

The helper is read-only. It validates the schema (including conditional reasons),
canonical manifest/map references, input hashes, current v4 map, unique interaction
and participation IDs, map ID resolution, source ordering, whole-turn/shared-UID
boundaries, exact source-span accounting inside `lines`, and equality of both
`reviewContext` arrays with the immediately adjacent original lines. It can validate a
proposal stored outside the vault; references still resolve within the selected
vault. `--vault-root PATH` supports isolated fixture vaults.

It does not establish verbatim wording, cut appropriateness, semantic classification,
coverage completeness, stable-ID preservation across revisions, or actual review.
Those require the skill's source comparison and pre-edit diff. The existing draft
reader's `match_inline` can check compatible individual cut-bearing turns, but its
full-draft validator is not a validator for this partial collection. If literal
`((...))` in original speech collides with editorial cut syntax, preserve it and
explain the distinction in chat; do not silently reinterpret or edit the source.

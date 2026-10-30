# Draft contract and integration

The single output is `cleaned/<stem>-interactions-draft.md`. It adds only three
metadata fields in its first comment:

```markdown
%% interactions-draft: {"version":4,"sessionYaml":"cleaned/example-session.yaml","sourceSha256":"<SHA-256 of polished transcript bytes>"} %%
```

- `version` identifies this draft format.
- `sessionYaml` is bundle-relative. Resolve the polished transcript through its
  `transcriptProcessing.artifacts.polishedMarkdown.path`; the draft does not
  duplicate that path, artifact key, session dates, or other session metadata.
- `sourceSha256` ensures validation and restoration use the same polished source.

There are no persisted input-hash lists, review flags/notes, body hashes, snip
categories, encounter IDs, name lists, or turn indexes. Review is a workflow step
reported in the handoff. Validation alone does not establish semantic review.
Valid YAML updates are allowed; dates and source resolution are checked afresh.

Original headers and source turns follow a clearly labelled derivative heading.
Unedited turns and wording outside snips remain verbatim. Older experimental
formats require explicit migration; ordinary runs never overwrite them.

## Snips and restoration

A whole-turn or multi-turn snip needs only its inherited source comment and label:

```markdown
%% u0041:0-36, u0042:0-55, u0043:0-22 %%
((Combat against Grash and his allies.))
```

An inline snip stays inside its original polished turn:

```markdown
%% u0041:0-36, u0042:0-55 %%
DM: ((rolls)) Grash says the gate opens tomorrow.
```

These UID spans are illustrative. Always retain the exact original spans and
partitions, including when a turn combines UIDs or a UID spans multiple turns.
Their offsets refer to **cleaned text**, not polished wording or generated labels.
No new sub-turn mapping is added.

Author inline labels in at most six words, ordinary/continuation labels in at
most 12, and one combat overview sentence per encounter in at most 40. The helper
enforces the six-word inline and 40-word whole-snip ceilings; the agent checks
stricter ordinary-label limits and encounter-level overview semantics.

`((label))` is generated text, never a quotation. Ordinary parentheses remain
original speech. Preflight rejects source text already using double parentheses
so a reader can identify snips without another annotation.

The inherited spans identify the corresponding original turns. `restore --turn N`
uses a one-based original polished turn number as a command selector; that number
is not stored. It restores the complete turn, undoing all inline snips together.
If the turn is inside a collapsed multi-turn snip, the entire snip range is
restored. Neighboring blocks are unchanged, even when they share a UID.

## Verification

Validation checks that every source span occurs exactly once in order, with its
original partition intact. Retained words must match their original turn in order,
with `((label))` marking each omission. Matching positions are temporary and are
not saved as sub-turn provenance. It also checks the polished-source hash and
label syntax/length; the YAML and other inputs are read-only.

Semantic review must still check preserved names, lore, uncertainty, conversation
continuity, outcomes, and one overview sentence per encounter. The optional
`snip --name` argument checks a supplied name against source and label when making
that edit, without persisting it. There is no machine-readable encounter grouping
or review attestation in the draft.

## Downstream reading

Scene mapping already supports this draft as a validated reading view. Entity
checking reads the original polished transcript instead. Final interaction
generation is not implemented; future consumers must follow these rules:

- Resolve metadata and original evidence through YAML and inherited UIDs.
- Quote original polished text, never generated labels or fragments joined across
  snips. Labels are retrieval hints, not evidence for outcomes or participants.
- Snips are gaps, not scene/conversation boundaries or extraction exclusions.
  Reopen original speech for consequential claims. A partly retained turn cannot
  have its entire UID range classified as excluded merely because of a cut.

No YAML pointer is registered for this experimental derivative. Model-token
savings must be measured separately from visible word reduction; retained mapping
comments can be substantial.

# Review from Markdown

Use this after cleanup, polishing, and quality review have produced the readable
transcript, or for an authorized bounded revision of finalized references.

**The review Markdown is the review state.** It travels with the original,
prepared UID, cleaned UID, readable transcript, and session YAML. It does not need
`transcript-work/state.json`, exports in JSON/HTML, job responses, or a second
review-state file. Missing old work state is normal; never fabricate it.

## Present and record decisions

Read the review Markdown and relevant retained passages. Present one session at a
time, showing original wording, proposed correction, and the complete exchange
needed to interpret it. A proposal replaces only its exact target; adjacent speech
and the rest of its UID remain intact. If the proposed correction is unknown, say
“retain unresolved” instead of presenting an unchanged string as a correction.

Record the user's actual choice in the item's **Resolution** field:

- `pending`: no decision yet.
- `proposed`: use the displayed full-UID proposal, confined to its target.
- `alternative 1` (or another displayed number): choose that alternative.
- `correction`: use the **Correction** field as replacement text for the target.
- `retain`: leave the original words/markers unchanged and close this question.

“Original is correct” can warrant removing a marker through a correction. “Leave
unresolved” retains it. Use the user's intent; do not invent approval or infer an
identity from an inconclusive clue. A confirmed noun does not by itself confirm
speculative surrounding words. Label contextual reconstruction honestly.

## Apply without the original processing queue

```bash
python3 -B HELPER review --bundle BUNDLE
python3 -B HELPER review --bundle BUNDLE --apply
```

The Markdown includes hidden `transcript-review:v1` and `transcript-issue:v1`
control blocks: relative retained paths, their fingerprints, exact targets, and
context ranges. Maintain these in the Markdown, never in a separate state file.
The visible Original and Proposed fields remain the full UID text. Editing a
proposal cannot change text outside the stored target.

Before applying a source correction, the agent fills the affected
`transcript-polish:v1` block's `after` text with the reviewed **complete readable
turn**, preserving every other word and its speaker. `index` is zero-based;
`before` must still exactly match the current readable turn. Leave unused blocks'
`after` values null. These hidden blocks are agent plumbing; ask the user about the
transcription, not offsets or serialized data.

For a changed turn that retains `[garbled]`/`[cross-talk]`, supply its exact remaining
`substitutions` against the corrected UID text using the polishing contract. The
helper refuses substitutions that hide the accepted correction. An unaffected turn
is preserved byte-for-byte except for mechanically shifted source offsets; its old
display labels do not require reconstructing the removed processing history.

The helper checks reference fingerprints, target text, proposal boundaries, source
coverage, words, symbols, annotations, and markers in revised turns. It adjusts
source offsets while retaining speaker assignments. A patch crossing an existing
turn/speaker boundary must be split into separately reviewed span edits. It also
refuses overlapping corrections or a correction overlapping another pending target.

Applying a subset removes resolved questions from the Markdown, updates remaining
positions and context, and refreshes its fingerprints. Pending decisions remain
pending. Repeating apply with no new decisions is harmless. No persistent JSON
review state is produced. Transient transaction snapshots protect interrupted
writes; use `recover` after interruption and reconcile any conflicting later edit.

## Finish or reopen

Once all questions are resolved:

```bash
python3 -B HELPER review --bundle BUNDLE --finalize
python3 -B HELPER status --bundle BUNDLE
```

Finalization preserves the four transcript references and session YAML, updates
completion fingerprints and existing speaker assignments, and retires the review
Markdown and any remaining temporary pipeline files. A human decision to retain
uncertainty is sufficient; certainty about every spoken word is not required.

For a later authorized correction to current finalized references:

```bash
python3 -B HELPER review --bundle BUNDLE --prepare u0042 u0081
```

This creates a fresh bounded review Markdown for those UIDs, without recreating
clean/polish/quality jobs. Narrow each target to the actual damaged words, provide
a supported full-UID proposal or correction, and review the affected turn as above.
It refuses to overwrite an existing report or adopt references changed since their
completion record. Legacy reports lacking portable control blocks need explicit
reconciliation against retained sources; do not pretend their absent hashes or
replacement boundaries were previously verified.

## Editorial calibration

These examples illustrate decisions, not universal substitution rules:

- **Names hidden in ordinary words:** “Frisbee teleporting away” was a missed
  Riswynn reference supported by the exchange and the earlier session. “Mylar
  adventure” was Mawar. Inspect the full exchange and relevant setting names before
  passing fluent-looking nonsense through unchanged.
- **Recoverable incidental speech:** “Church.” was an acknowledgment, “Sure.”;
  “dust shorts” addressed Schwartz. Incidental status is not a reason to skip a
  reasonable repair or hide intelligible surrounding speech under `[garbled]`.
- **Negation:** “word children a collapse” supported “were killed in a collapsed.”
  The bare possibility of an omitted “not” did not supply evidence for “weren't.”
  Keep a negative alternative only when sounds or the exchange make it credible.
- **Materiality:** an unclear roll total with an explicit successful outcome can
  remain incidental uncertainty. Do not routinely ask the DM to reconstruct old
  dice results unless the number changes the useful account or was requested.
- **Lore-assisted candidates:** “without a sunrise” was confirmed by the user.
  Lore may support that candidate without proving the spoken words. Neither replace
  a spoken factual claim merely to fit lore nor suppress a good candidate solely
  because lore helped identify it. The same distinction preserves uncertainty
  about whether Milo visited Targu even after the city's name is recognized.
- **Boundary fidelity:** the Dragonets return proposal must not repeat the preceding
  Wanderer's-hand clause; the Labyrinths correction must keep the later Ulgna/Morky
  speech; the Mawar collapse correction must leave “building” in the next UID.

During the final quality pass, inspect every `recoveryCandidates` entry and its
context, and look for ordinary words masking names or responses outside that list.
Use contextual/phonetic evidence to recover speech or retain a narrow incidental
label. Mechanical validation proves coverage and fidelity, not that every remaining
recognition error was found.

# Correction contract

All examples are illustrative; use the exact current fingerprint, text, indexes,
and source spans from `inspect`. Plans are transient command input, not review state.

```json
{
  "version": 1,
  "inputDigest": "fingerprint from inspect",
  "edits": [],
  "turns": [],
  "decisions": []
}
```

The three lists are optional, but at least one operation is required. Unknown
fields, stale fingerprints, duplicate turn indexes, and overlapping source edits
are rejected. All source edits address the **pre-edit** cleaned text. Explicit
replacement turn parts and substitution spans address the **post-edit** text.

## Wording

```json
{"uid":"u0001","start":19,"end":25,"before":"denser","after":"darker"}
```

Place this in `edits`. Character bounds are zero-based, end-exclusive Python
string offsets, not byte offsets. The helper checks exact `before` text, retains
UIDs/times/headers, shifts polished mappings and remaining review targets, and
updates the corresponding visible words when there is exactly one display match.
Repeated or differently punctuated display text requires an explicit turn update:

```json
{"index":0,"before":"Well, well, it got denser.","after":"Well, well, it got darker."}
```

Put this in `turns`. Supply the **whole** turn, retaining all unrelated words.
This cannot independently change spoken words: they must agree with the cleaned
source after `edits`. Apply several selected occurrences with several exact edits,
not an unbounded global replacement. Empty source units are not allowed.

## Speaker only

```json
{"index":0,"before":"Well, well, it got denser.","speaker":"Finnan"}
```

Only the polished speaker label changes. Speech and source mappings remain intact.
One turn may cover several UIDs; this relabels the whole inspected turn. Use parts
when only a portion belongs to the corrected speaker. Do not use a player identity
to infer a role label without evidence; explicit `Unknown` remains valid.

## Several speakers within a turn

```json
{
  "index":0,
  "before":"Well, well, it got denser.",
  "parts":[
    {"speaker":"DM","text":"Well, well,","sources":[{"uid":"u0001","start":0,"end":12}]},
    {"speaker":"Player","text":"it got denser.","sources":[{"uid":"u0001","start":12,"end":26}]}
  ]
}
```

Parts replace exactly one original polished turn, in order. Their combined source
ranges must equal that turn's full ranges, with no gaps, overlap, reordering, or
borrowed neighboring speech. Each part is separately checked against its source.
Supply every part, including unchanged speakers. `parts` cannot be combined with
the single-turn `after`, `speaker`, or `substitutions` fields. The helper does not
merge neighboring turns automatically or invent new UIDs.

## Display labels and restoration

```json
{
  "index":0,
  "before":"Well, well, it got denser.",
  "after":"Well, well, it got [garbled].",
  "substitutions":[
    {"uid":"u0001","start":19,"end":25,"kind":"garbled","reason":"User confirmed this recognition fragment is unrecoverable."}
  ]
}
```

This changes only the readable display. `kind` is `garbled` or `cross-talk`;
`reason` explains the actual judgment. Preserve intelligible surrounding words.
A revised turn containing existing labels must supply all its substitution spans;
pure speaker-only changes need no reconstructed substitution history. Parts can
each include their own `substitutions` list. Markers and annotations cannot be
hidden by a substitution.

To restore a label, provide `after` containing the cleaned wording and omit the
corresponding substitution. If the cleaned wording itself needs correcting, add
an `edits` entry. An explicitly approved source restoration plus a display label
can be applied in one plan; inspect both in the preview instead of fabricating a
second punctuation correction to trigger an update.

## Open review decisions

```json
{"id":"issue-ID-from-inspect","resolution":"corrected"}
```

Place decisions in `decisions`:

- `corrected`: close the issue with a source edit or explicit polished-turn change
  covering its target, including an approved speaker correction.
- `retain`: leave its words unchanged and count the retained uncertainty.
- `confirmed`: the user confirmed the existing wording, or approved removing its
  unnecessary marker; do not count that as unresolved. Include a marker-removal
  source edit when applicable.

Never infer these dispositions merely to finish a session. An edit overlapping a
pending issue requires its actual decision. Other pending issues keep their text,
proposals and context, with remapped positions. The generated review sections are
helper-owned; do not store unrelated notes inside them.

## Preview and results

`preview` returns a unified diff, changed paths, remaining-issue count, whether the
review will finalize, and existing downstream files to inspect separately. It
creates no files. On last-issue completion the review report and ordinary temporary
exports/work files are retired by the standard finalizer; this retirement is
reported by `finalizesReview`. `apply` adds the verified resulting session status.
All writes stay within the selected bundle and use shared transaction recovery.
Use `recover` after interruption; it completes recorded writes and finalization,
then removes committed correction snapshots without discarding other work.

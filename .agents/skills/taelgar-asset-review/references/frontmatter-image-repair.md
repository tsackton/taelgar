# Frontmatter Image Repair

Follow the shared scope in [SKILL.md](../SKILL.md). Run commands from the vault root.

Use `_scripts/repair_image_frontmatter.py` to check top-level YAML `image:`
properties. Its default is read-only; a JSON review records the proposed changes.
It checks populated properties whether bare or already linked, leaves empty
properties alone, and proposes quoted wikilinks for unambiguous existing image
files. It searches recursively, including `_incoming`, `pc-references`, and DM
folders: the folder-organization exclusions do not apply to reference validation.
It does not scan recap Image fields, body links, Leaflet code blocks, or audio
Output fields. External URLs and unusual YAML are reported for manual review,
not silently rewritten or declared locally verified.

From the vault root:

```sh
python3 -B _scripts/repair_image_frontmatter.py \
  --output /private/tmp/taelgar-image-repair/review.json
```

Use repeatable `--note 'vault-relative/Note.md'` arguments for a small review.
A normal pass is just a property check; image generation and the website build
are unnecessary. Dataview 0.5.68 was verified live with the existing expression
`embed(link(image, "240"))`: bare and linked properties resolve and render the
same way, including the width, and produce equivalent table Markdown. The two
formats can coexist during a gradual conversion; no table-query rewrite is
needed just for linking image properties.

Present the safe conversion count and affected notes as one batch. These are
mechanical frontmatter repairs: the user explicitly requires changing only the
`image:` scalar and preserving every tag exactly. Do not add `status/check/ai`
or any other status marker for this operation. Read the affected notes and
preserve all unrelated metadata, formatting, comments, and body text.
Approval to write the tool is not approval to apply its newly discovered repairs.
Existing authorization for an exact batch or replacement is sufficient; do not
ask for the same approval twice.

For a missing, ambiguous, or non-image target:

- Show the note, current property, and a short list of actual image candidates.
  Prefer a valid image already embedded in the note. The report orders these
  first, followed by ambiguity matches and similar filenames. These are
  suggestions, never automatic selections; an embedded image may be unrelated.
- Show small previews when useful, or let the user browse a folder in Finder and
  give the chosen path. Batch straightforward choices when that is faster. Allow
  defer/leave unchanged without blocking approved safe conversions.
- Record a selected replacement as the exact vault-relative image path. If the
  user wants a different image, search real files rather than inventing a name.
  Empty image fields remain empty; assigning a previously absent image or
  replacing asset bytes is separate work.

Record explicit selections in a private JSON file, for example:

```json
{"Campaigns/Example/Treasure/Example.md": "assets/selected-image.png"}
```

Generate a fresh concrete preview using those selections:

```sh
python3 -B _scripts/repair_image_frontmatter.py \
  --replacements /private/tmp/taelgar-image-repair/selections.json \
  --output /private/tmp/taelgar-image-repair/selected-review.json
```

This preview also includes other eligible conversions unless limited with
`--note`. Before applying, retain only the approved complete entries in the
review's `changes` array; preserve all other fields. Never hand-edit target
paths or hashes inside an entry. New replacement choices must go through `--replacements` and a fresh preview. Confirm that requested
choices produced actual changes, rather than assuming a manual-review entry
was repaired.

Apply the approved review:

```sh
python3 -B _scripts/repair_image_frontmatter.py \
  --apply /private/tmp/taelgar-image-repair/selected-review.json \
  --receipt /private/tmp/taelgar-image-repair/applied.json
```

The script rechecks selected notes and current image resolution, rejects stale
or edited proposals, writes atomically, and verifies resulting bytes and image
references. Its private receipt contains the original note text for recovery:
keep it outside the vault and shared code trees. On failure it attempts rollback
without overwriting concurrent edits; inspect a `recovery-required` receipt
before continuing. Re-read changed notes, review the scoped diff and whitespace
check, and run a fresh property check. Report applied, still unresolved, and
deferred counts. Do not broaden this into repairing unrelated empty tables or
other note metadata.

For speed, offer this small check after a review batch or when requested, rather
than repeating it for each rename. No background monitoring is created by this
skill.

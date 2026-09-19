---
name: taelgar-asset-review
description: Review and organize Taelgar images and audio with deterministic scans and approved directory moves; validate and repair frontmatter image references with interactive replacement selection. Use for misplaced or unlinked assets, bare image properties, and broken image references. Asset renames, file replacement, conversion, maps, and generated audio need separate handling.
---

# Taelgar Asset Review

Help the user inspect real asset folders and approve concrete batches of directory
moves, or repair frontmatter image references. Use the maintained scripts in the
Taelgar vault's `_scripts` directory: `find_misplaced_images.py`, `move_assets.py`,
and `repair_image_frontmatter.py`. Read their `--help` when needed.
The scripts require Python 3.10+ and PyYAML.

## Scope and classification

Locate the active Taelgar vault and read its `AGENTS.md`. When no vault is open,
the usual local vault is
`/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar`.
Keep asset names and contents unchanged. Choose the requested workflow: folder
organization below, or [frontmatter image repair](#frontmatter-image-repair).
For a property check, go directly to that workflow; do not run the full asset
classification scan. Both workflows require the relevant concrete scope before
applying changes.
Do not change Obsidian's attachment setting; the user manages it.

For folder organization, scan images **and audio** by default. Use `--media images`
or `--media audio` only for an explicitly narrower review. All of `assets/` is eligible, including
already categorized folders, except `assets/_incoming/` and
`assets/pc_references/`. Notes in those excluded folders still count as references
to other assets.

Apply this hierarchy:

- Any regular-page reference wins. Objects, people, places, and other ordinary
  reference pages inside Campaigns count as regular pages.
- Campaign-only references include session notes, their generated/source
  components, and campaign landing pages. Destination: `assets/campaign/`
  (singular).
- DM-only references come from `_DM_` and `_dm_notes`. Destination: `assets/dm/`.
- Worldbuilding-only references come from Worldbuilding, including chats.
  Destination: `assets/worldbuilding/`.
- No local reference or filename mention: `assets/_unlinked/`.
- Mixed special-category uses stay outside the exclusive folders. Ordinary or
  mixed-use assets discovered in an exclusive folder return to `assets/`.
  Regular assets already in other useful subfolders stay there.

The scanner distinguishes classification from move safety. Its `held` entries
identify path-dependent links, unknown filename mentions, code/config consumers,
duplicate names, drawing dependencies, existing destinations, symlinks, or moves
that would expose Git-ignored material. Describe these to the user and resolve
them through separately authorized work. Never promote a held entry into
`moves`, strip its safeguards, or invent a different destination to bypass them.

## Scan and review

Keep JSON proposals and receipts **outside the vault and searched code trees**,
in a private scratch directory. They can contain private DM reference paths.
Do not create an Obsidian asset-index note: its links would contaminate the next
scan, and the user prefers folder previews for visual review.

Locate the website checkout and include its real upstream consumers. The usual
local checkout is `/Users/tim/RPGs/taelgarverse`. Search its `taelgar-utils`
directory, `website.json`, `ignore_spec.txt`, and `autobuild_website.sh` with
repeatable `--consumer-root` arguments. Vault `_scripts` and Obsidian plugin code
are already searched. Do not treat generated `docs/` or `taelgar-static/` as
authoritative consumers. If the website checkout is unavailable, disclose that
gap before recommending moves that could depend on it.

Example, from the vault root, after resolving the actual paths:

```sh
python3 -B _scripts/find_misplaced_images.py \
  --output /private/tmp/taelgar-asset-review/potential-moves.json \
  --consumer-root /Users/tim/RPGs/taelgarverse/taelgar-utils \
  --consumer-root /Users/tim/RPGs/taelgarverse/website.json \
  --consumer-root /Users/tim/RPGs/taelgarverse/ignore_spec.txt \
  --consumer-root /Users/tim/RPGs/taelgarverse/autobuild_website.sh
```

Present counts by destination and a concrete file list for the batch under
review. Explain held files separately. The reference evidence includes source
paths and line numbers; use it to explain classifications without exposing
private DM prose in a shared report.

Facilitate review in the user's preferred surface. Offer to open the relevant
folder in Finder for icon/gallery previews. When discussing individual images,
inspect and show the actual files with absolute image paths. For audio, use the
actual clip when playback would help. Let the user choose batch size and focus;
do not force a lengthy one-file-at-a-time questionnaire.

Support decisions to move, keep in place, or defer. Keeping a file is a decision
for this batch; do not create a permanent exclusion rule unless asked. Requests
to rename, replace, convert, or delete asset files are outside this skill's workflow:
record the requested follow-up in chat and obtain the necessary separate scope.

## Approval and application

Show the proposed source/destination pairs and get explicit approval for that
batch before moving anything. Existing approval for the exact displayed batch
is sufficient; do not ask again. Approval to create the scripts or skill is not
approval to move newly discovered assets.

For a subset, copy the proposal outside the vault and retain only its approved
`moves` entries. Preserve each complete entry and all policy fields. Do not edit
hashes, destinations, categories, or evidence. Then validate:

```sh
python3 -B _scripts/move_assets.py /private/tmp/taelgar-asset-review/approved-moves.json
```

After approval, apply that same file:

```sh
python3 -B _scripts/move_assets.py /private/tmp/taelgar-asset-review/approved-moves.json \
  --apply --receipt /private/tmp/taelgar-asset-review/applied-moves.json
```

The mover re-scans the same source roots, validates every selected entry against
the current plan, refuses collisions and changed evidence, preserves basenames,
verifies contents and references after moving, and writes a receipt. On failure
it attempts to restore completed moves. Inspect any `recovery-required` receipt
before further mutations; do not blindly retry a partially completed batch.
If a plan is stale, refresh it and present any materially changed batch for
approval. An empty dry run is not evidence that previously approved moves ran;
check the receipt and actual files.

## Verification and handoff

Read the receipt and confirm the exact approved files reached their destinations.
Review the scoped changes and report counts, preserved contents, held/deferred
files, and any incomplete checks. Do not stage, commit, or deploy unless asked.

For campaign images, bare `Image:` fields in canonical session recaps are real
references even though they are not wikilinks. The generator preserves these
names in image embeds; the website resolves them through its recursive index.
Directory moves preserve that lookup. A replacement with a different filename
does not satisfy the old recap assignment. Check current filenames rather than
assuming a missing image is caused by directory layout.

When consumer code or exclusion rules changed, run the relevant targeted tests
for the materializer, website lookup/export retention, and map selection.
Respect the website checkout's separate approval requirement for a real
materialization/full rebuild; prefer isolated fixtures for ordinary validation.

The user handles ordinary image renames in Obsidian. Their testing confirmed that
plain recap `Image:` values appear as Unlinked mentions and can be linked there
immediately before a rename. Plain YAML `image:` values do not appear as Unlinked
mentions, but quoted wikilinks in those properties do update on rename. Use the
repair workflow below for those properties. Do not silently convert recap fields
or rename asset files. Leaflet maps and generated audio names remain separate
cases because plugin state, website settings, or clip-generation fields may
contain additional filename dependencies.

## Frontmatter image repair

Use `_scripts/repair_image_frontmatter.py` to check top-level YAML `image:`
properties. Its default is read-only; a JSON review records the proposed changes.
It checks populated properties whether bare or already linked, leaves empty
properties alone, and proposes quoted wikilinks for unambiguous existing image
files. It searches recursively, including `_incoming`, `pc_references`, and DM
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

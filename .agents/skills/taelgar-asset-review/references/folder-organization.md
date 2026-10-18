# Folder Organization

Follow the shared scope in [SKILL.md](../SKILL.md). Run commands from the vault root.

## Scope and classification

For folder organization, scan images **and audio** by default. Use `--media images`
or `--media audio` only for an explicitly narrower review. All of `assets/` is eligible, including
already categorized folders, except `assets/_incoming/` and
`assets/pc-references/`. Notes in those excluded folders still count as references
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
[frontmatter image repair workflow](frontmatter-image-repair.md) for those properties. Do not silently convert recap fields
or rename asset files. Leaflet maps and generated audio names remain separate
cases because plugin state, website settings, or clip-generation fields may
contain additional filename dependencies.

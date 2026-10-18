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

## Shared scope

Locate the active Taelgar vault and read its `AGENTS.md`. When no vault is open,
the usual local vault is
`/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar`.
Keep asset names and contents unchanged. Do not change Obsidian's attachment
setting; the user manages it. Do not stage, commit, or deploy unless asked.

Both workflows require approval of the relevant concrete scope before applying
changes. Existing approval for the exact batch is sufficient; do not ask again.
Approval to create scripts or this skill is not approval to apply newly
discovered changes.

## Choose the workflow

Read the selected reference in full before executing its workflow:

- **Folder organization:** read [folder-organization.md](references/folder-organization.md)
  for classification, scans, approved directory moves, recovery, and verification.
- **Frontmatter image repair:** read [frontmatter-image-repair.md](references/frontmatter-image-repair.md)
  for property checks, replacement selection, approved repairs, recovery, and
  verification. For a property check, go directly to this workflow; do not run
  the full asset classification scan.

Load the other reference only if the requested work also requires that workflow.

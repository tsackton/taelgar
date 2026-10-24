# Header experiments worktree

`D:/personal/taelgar-plugin-experiments` is a disposable view of the `taelgar`
vault for testing the Taelgarverse Obsidian plugin against native headers.
Keep its content current with the vault's local `main`, then rerun the
deterministic migration whenever work starts here.

## Start every work session

1. Confirm you are in this worktree on branch `taelgar-plugin-experiments` and
   inspect `git status --short`. Preserve unrelated work. Before rebasing a dirty
   checkout, preserve its changes in a named stash (including needed untracked
   files) or another recoverable local copy; do not discard or overwrite them.
   Do not make a convenience commit: vault commits require explicit human
   permission for that commit and scope.
2. Run `git rebase main` from this worktree. This means the **local vault main**,
   not core's main or an implicit remote update. If a rebase is already in
   progress, resolve or report that state first. Resolve conflicts while
   preserving new upstream metadata and article text, or stop and report the
   conflict if its intended resolution is unclear.
3. Restore any changes preserved in step 1. Retain the stash/recovery copy until
   restoration is verified; resolve any conflicts before continuing. A rebase or
   stash restoration can reintroduce legacy headers, so run the migration next.
4. From the worktree root run:

   ```sh
   python _scripts/migrate_taelgar_headers.py --write
   python _scripts/migrate_taelgar_headers.py --check
   ```

   If an H1 policy was selected for this work session, pass the same
   `--preserve-h1` or `--remove-h1` flag to both commands above. Without either
   flag, existing native titles are retained and legacy saved titles are removed.

5. Review `git diff --stat` and the relevant header diffs, then begin the task.
   Migration changes may remain uncommitted. Do not commit, push, publish vault
   content, or change production without the corresponding explicit permission.

The script performs no Git operations. The startup procedure is specific to
this experiments worktree; it is not an instruction to migrate the primary
vault checkout or merge these experimental note changes into `main`.

## Migration commands and contract

Python 3.9+ is sufficient; no packages, Obsidian process, core checkout, calendar
date, network connection, or legacy JavaScript execution are needed.

```sh
# Preview counts and the exact affected paths without writing.
python _scripts/migrate_taelgar_headers.py --verbose

# Apply the same deterministic replacements.
python _scripts/migrate_taelgar_headers.py --write

# Verify a second run has nothing left to do (0 = clean, 1 = migration needed).
python _scripts/migrate_taelgar_headers.py --check

# Keep the saved H1 above the block when converting a legacy header.
python _scripts/migrate_taelgar_headers.py --preserve-h1 --write
python _scripts/migrate_taelgar_headers.py --preserve-h1 --check

# Remove the H1 from both legacy and already-native headers.
python _scripts/migrate_taelgar_headers.py --remove-h1 --write
python _scripts/migrate_taelgar_headers.py --remove-h1 --check

# Synthetic regression tests, independent of editable vault data.
python -B -m unittest discover -s _scripts -p test_migrate_taelgar_headers.py
```

The default root is the vault containing the script, regardless of the caller's
current directory. `--root PATH` explicitly selects a different root, useful for
fixtures. Paths are traversed in sorted order, including untracked Markdown
notes. Hidden directories, symlinks, `assets`, `_scripts`, `_templates`,
`_sessions`, `_Plugins`, and `node_modules` are excluded so code examples,
templates, session source artifacts, and plugin files are not rewritten.

The script removes the top-level `headerVersion` field from every in-scope note,
including already-native notes and notes without a generated header. It reads
the original metadata before removing the field, so legacy header recognition
still works. Quoted field names and inline comments on the obsolete field are
supported; nested keys and body/code references are preserved. Unfamiliar
multiline version values stop the migration for review.

The script replaces a recognized leading saved H1/pronunciation/information
header with an empty `taelgar-header` fence. Legacy saved headers use both
top-level `headerVersion` and `tags` frontmatter fields, following the maintained
recognition contract in `taelgarverse-core/src/bio-block.mjs`. As an additional
migration case, a leading header containing an exact known legacy header view
(`get_PageDatedValue`, `get_Affiliations`, or `get_Whereabouts`) is recognized
even if its version or tags were lost. It also recognizes
blank separators before information callouts when those same exact legacy views
identify the callout as header output. It recognizes
the old `<!-- taelgar:header -->` / `<!-- taelgar-header -->` markers.

The mutually exclusive H1 flags choose the output for recognized headers:

- `--preserve-h1` retains the existing H1 when converting a saved legacy header
  and when processing an existing native header. The H1 stays directly above
  the empty fence, so the renderer omits its generated title.
- `--remove-h1` removes the H1 from both saved legacy headers and existing
  native headers. The empty fence then generates the title from metadata.
- Without either flag, behavior is unchanged: saved legacy titles are removed,
  while authored H1s already above native fences are preserved.

Both `# Title` and setext `===` headings work. Preservation never invents a title
for a fence-only note and cannot recover an H1 removed by a previous run. To
retain original titles, choose `--preserve-h1` on the first migration of those
original notes. Use the same flag for preview, `--write`, and `--check`; a second
run with that policy is unchanged. Switching to `--remove-h1` can remove titles
from already-native headers. Ordinary titles, later headings, and notes without
a recognized leading header keep their existing bodies; the script never inserts
headers merely because metadata exists.

Apart from removing `headerVersion`, frontmatter (including status tags),
UTF-8/BOM, line endings, and all bytes after the recognized header are preserved.
Authored callouts other than `[!info]`, prose, comments, later headings, indexes,
and body scripts remain in place. Legacy inline header Dataview calls disappear with their saved header;
the new plugin reads metadata itself. Templates and tools on this branch use
native headers; shared CustomJS query services and the specialized session
renderer remain independent consumers.

All inputs are scanned and each planned output is checked for idempotence before
the first write. Malformed native headers or unreadable inputs exit with code 2
without writing; changed inputs are checked again before overwriting. If an I/O
failure or concurrent edit interrupts writing, earlier files may already have
been migrated: preserve the concurrent edit, resolve the error, and rerun.
Repeated successful `--write` runs produce no further changes.

See [Native Headers](../_MoC/Native%20Headers.md) for the current authoring and
local export workflow. Compatibility recognition is confined to this deterministic
migrator and its tests so notes introduced by a future rebase can be converted.

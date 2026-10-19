# Dataview materializer

The CLI requests a materialization run through the Taelgar Obsidian plugin.
The source vault must be open in Obsidian with Dataview enabled and its index
ready. Output is written to a separate vault; source notes are not modified.

## Existing behavior

Without additional options, the CLI retains its current behavior: materialize
fenced `dataview` queries, supported `dataviewjs` blocks, and supported inline
JavaScript expressions, and regenerate headers using `--header-type website`.
Existing publishing commands continue to use this behavior.

## Dynamic website Markdown

From the source vault root:

```sh
node _scripts/materialize-dataview/materialize-dataview.mjs --vault . --out ../taelgar-dynamic --dynamic-website
```

`--dynamic-website` prepares Markdown for rendering headers at request time:

- Replace generated headers on notes with `headerVersion` with the standalone
  marker `<!-- taelgar:header -->`, immediately after frontmatter. The marker
  replaces the title, pronunciation, and info callout; metadata stays intact.
- Delete closed `dataviewjs` fences without executing their contents.
- Remove headings whose sections become empty after that deletion, including
  empty parent sections. Prose, DQL, other code, comments, and previously empty
  headings are retained. Campaign/date delimiters stay balanced. ATX and
  single-line Setext headings are supported.
- Materialize fenced `dataview` queries, including queries inside callouts.
- Require Dataview, but skip CustomJS loading and state changes.
- Export all notes and assets outside underscore-prefixed and Worldbuilding
  folders (at any depth, Worldbuilding case-insensitive). Hidden tooling paths
  and AGENTS.md remain omitted. The assets/dm and asset/dm directories and all
  descendants are also excluded, case-insensitively. Dynamic output preserves
  excludePublish and date metadata for request-time checks in taelgarverse-core.
  The report identifies this policy as publicationPolicy: context-v1.

This overrides `--header-type` regardless of argument order. Inline JavaScript
outside the generated header is preserved verbatim. Code examples inside other
fences are preserved. Only exported Markdown is transformed; source notes are
not rewritten.

The equivalent plugin request option is `config.dynamicWebsite: true`. It defaults
to false, including requests from older wrappers that omit it.

Strict mode still reports query errors, unsupported DQL, and unclosed dynamic
fences. Unclosed JavaScript fences are left intact for error reporting, rather
than discarding everything to the end of the file. Intentionally retained inline
JavaScript does not fail strict mode. The report records `dynamicWebsite` and
counts inserted header markers, deleted JS blocks, and removed section headings.

`--date` controls CustomJS header output in the existing full mode. It has no
effect in dynamic website mode. The website uses its request date and campaign
to generate the header when it encounters the leading marker.

The existing `autobuild_website.sh` wrapper is unchanged and does not forward
this new option. Invoke this CLI directly for dynamic website output. Reload the
materializer plugin (or restart Obsidian) after updating the plugin code.
The CLI checks the loaded plugin's dynamic website support and stops with an
explicit reload message if Obsidian is still running an older plugin version.

Dynamic website writes use two phases. Obsidian renders the Markdown and writes
a small staging bundle, then releases the plugin runtime. The Node CLI copies
the prepared notes and streams media to the output directory. Copy progress
shows the current filename and transferred bytes; rendering reaching 100% no
longer hides the media-copy phase. A successful final report is marked
`outputComplete: true` only after copying finishes. Copy failures retain the
staging bundle and write an explicit failure report.

Keep the CLI running through the copy phase. `--no-wait` is unavailable for
dynamic website writes. Legacy publishing commands retain their existing copy
behavior. No output directory is automatically cleared.

Strict mode writes only the JSON report when a query fails or is unsupported;
it does not copy the vault into the output directory. The CLI prints the final
status, affected files, and report path. Add `--no-strict` to permit partial
output, with failed or unsupported queries left unchanged:

```sh
node _scripts/materialize-dataview/materialize-dataview.mjs --vault . --out ../taelgar-dynamic --dynamic-website --no-strict
```

In `taelgarverse-core`, configure `source_dir` to use this output directory and
keep `runtime_dir` pointing at the original vault. The website consumes a leading
header marker once and preserves any following body headings. A marker shown
inside a fenced code example remains literal.

## Regression tests

These tests use synthetic inputs and temporary directories. They do not launch
Obsidian or materialize the working vault:

```sh
node --test _scripts/materialize-dataview/core.test.mjs _scripts/materialize-dataview/copy-output.test.mjs _scripts/materialize-dataview/materialize-dataview.test.mjs _scripts/materialize-dataview/materializer-plugin.test.mjs
```

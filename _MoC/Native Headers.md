# Native Headers

Person and place notes render their complete header from an empty code block
immediately after YAML frontmatter:

````markdown
---
tags: [person]
name: Example
species: human
---
```taelgar-header
```

Article text begins here.
````

The block generates the title, optional pronunciation, information callout, dated
relationships, and configured index buttons. Keep it empty; put identity,
chronology, relationships, and display overrides in frontmatter. See
[[Metadata Specification]] and [[Display Control]] for those fields and tokens.
An authored H1 directly above the block replaces its generated title; blank
lines may separate them. Both `# Custom title` and a title underlined with `===`
work. Pronunciation, information, and index controls still render. An H2 or an H1
separated by prose or another block does not suppress the generated title.
The deterministic migration normally preserves titles already above native
fences. Use `--preserve-h1` to also retain an existing H1 when converting a saved
header, or `--remove-h1` to remove H1s from both forms and let the block generate
the title. These options never invent a missing H1. See
[_scripts/header-migration.md](../_scripts/header-migration.md). Do not copy
rendered information into the Markdown.

Changing `name`, `pronunciation`, dates, affiliations, or whereabouts updates the
rendered header without a note-writing step. Preserve the block when making
metadata edits. Editorial comments belong after its closing fence; persistent
metadata and POV blocks retain their normal positions at the end of the article.
An empty generated header is not authored article content.

The Taelgarverse Obsidian plugin and website share the maintained renderer in
`taelgarverse-core/src/header-core`. Plugin source and user documentation live
in `taelgarverse-core/obsidian/taelgarverse`. The vault owns note metadata and
content. Shared CustomJS helpers still support existing data queries and session
templates; they are not needed to render a native header.

Use the person and region/realm templates for new notes that need native bios.
Session notes keep their specialized component/template rendering, and authored
report, source, species, and culture headings remain ordinary Markdown.

## Local static export

With this vault open in Obsidian and the Taelgarverse plugin loaded, use the
maintained materializer from the neighboring core checkout:

```sh
node ../taelgarverse-core/scripts/materialize-static.mjs --vault . --out ../taelgar-plugin-preview --header-type none --no-strict
```

This writes a separate local export and renders native blocks as Markdown. It
does not publish content. Website publication and production changes have their
own commands and require the corresponding human authorization.

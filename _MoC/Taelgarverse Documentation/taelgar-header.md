# `taelgar-header`

This callout displays a note’s generated reference information, such as dates, affiliations, and whereabouts. In Obsidian and on Taelgarverse, the renderer uses the note’s metadata and the active in-world date and campaign context.

Put the callout directly below the note’s H1 and optional pronunciation.

```markdown
# Display Name
*(pronunciation)*
> [!taelgar-header]
```

During rendering, Taelgarverse replaces only the callout. The H1 and pronunciation above it are ordinary Markdown. On an eligible note, **Taelgarverse: Regenerate page header** explicitly updates the saved H1, optional pronunciation, and callout summary. The saved callout body serves as fallback Markdown.

See [[Display Control#Header Format|Header Format]] for authoring and [[Display Control]] for the display templates.

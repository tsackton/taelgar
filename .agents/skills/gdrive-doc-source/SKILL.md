---
name: gdrive-doc-source
description: Import an existing Google Doc into the Taelgar vault as a readable Markdown source with its open and resolved comment threads. Use for source preservation, not canon rewriting.
---

# Google Doc Source Import

Preserve a Google Doc as source material in the Taelgar vault. Follow `AGENTS.md`: a document URL authorizes only that document's import, and an existing vault note is not overwritten without a specific request. Imported development material remains noncanonical. Do not rewrite its claims, fix spelling, or promote comment proposals into article prose.

## Read the source

Use the connected Google Drive tools to read file metadata, the full native Google Docs resource (`get_document`), and every page of `get_document_comments`, including resolved threads and replies. Check the file ID and document revision. Do not use plain text or Markdown export alone: it loses comment state and may lose strikeout styling. Include all tabs in source order. For resolved comments whose quoted wording is absent from the current document, list and fetch relevant historical revisions when available to recover a whole-sentence context. The renderer preserves simple tables and page breaks; inspect merged cells, suggestions, footnotes, or another structure it cannot represent, then extend the renderer or report the exact gap before declaring the import complete. For inline images, download each image `contentUri` into a local vault asset, include its tab's `inlineObjects` map in the bundle, and set `imagePaths` to map each object ID to the asset filename. If an image cannot be downloaded, report that gap; a temporary Google content URI alone is not a durable archive.

## Remove strikeout formatting

Keep every text run, including struck-through text, and remove the strikeout formatting in the Markdown copy. This applies whether some or all of the Google Doc is struck through. Do not interpret strikeout as an instruction to delete text. Record this treatment in the imported note. Exclude struck-through text only if the user explicitly requests exclusion for a particular import.

Convert literal angle-bracket source text such as `<A>` to `~~A~~`, and literal square-bracket source text such as `[a]` to `(a)`. Apply this to source prose and comment content before adding Markdown syntax, so intentional links in the document remain intact. Keep the words inside the brackets.

## Render and place

Save the Drive `get_document` structured result and the complete comments result as one temporary JSON object with keys `document` and `comments`. When historical revision text was fetched, include it in an optional `revisions` list with each revision's ID, modified time, and content. For local images, add `imagePaths` as described above. `scripts/render_source.py` converts that object to Markdown:

```text
python scripts/render_source.py --input <bundle.json> --output <draft.md>
```

The renderer keeps struck-through text by default while omitting the strikeout styling. It preserves headings, paragraphs, list levels, simple tables, basic emphasis, and links. It appends a visible comment archive with each thread's status, original selection, whole-sentence context when a unique match exists, author, timestamps, text, replies, and Drive ID. A quoted anchor may refer to wording from an earlier document revision; label historical context with its revision ID. If the match is ambiguous or absent, state that explicitly rather than guessing a sentence. Do not silently omit a thread or reply. Check the renderer's counts against all fetched comment pages.

Choose a source-material destination after checking filenames, relevant existing notes, and backlinks. Prefer the established `Worldbuilding/Chats and Emails/Other` area for old worldbuilding Docs. If a same-subject source copy already exists, preserve it and create a distinct reading copy unless the user specifically authorizes replacement. Add `status/check/ai` to a new or edited content note outside `_sessions` and `Worldbuilding/Agentic Review`; never alter another status tag. Use the current metadata rules before writing frontmatter. Write the source line exactly as `Source: Google Drive document ID <ID>` with the actual ID substituted. Put the document title, revision, extraction date, and strikeout treatment in separate plain-text provenance as useful, without implying the content is canon. Do not add a live link or URL to the source Google Doc unless the user explicitly asks for one.

## Verify

Read the entire rendered note. Confirm all source text is present without strikeout styling and that open/resolved thread counts and reply counts match the provider response. Verify frontmatter, links, Markdown structure, all changed paths, the complete diff, and scoped `git diff --check`. Remove temporary bundles. Do not modify the Google Doc or its comment state.

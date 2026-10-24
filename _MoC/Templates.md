# Templates

Use the appropriate `_templates/markdown` or
`_templates/realms-cultures-creatures` source for new subject notes. Person,
region, and realm templates include an empty `taelgar-header` block; fill their
frontmatter and write the article below it. The plugin renders the title and
information from metadata. See [[Native Headers]] and [[Note Categorization]].

Species and culture templates use authored headings. Session-note templates
under `_templates/session-notes` remain part of the session component renderer
and contain their specialized date, cast, source, and narrative slots.

The remaining query templates insert data tables or native indexes as appropriate.
For example, `members-of-org` and `members-of-org-historical` select current or
historical organization members. These queries are independent of note headers.

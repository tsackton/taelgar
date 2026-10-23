---
tags: [meta]
title: Example subsite
campaigns: [dufr, feywild, mawar]
---
# Example subsite

This example subsite combines Dunmar Frontier, Lost in the Feywild, and Mawar Adventures in one view of Taelgar.

## Campaigns

- [[Dunmari Frontier Campaign|Dunmar Frontier]]
- [[Lost in the Feywild]]
- [[Mawar Adventures]]

## How this page works

The filename `_website/tim.md` selects the address `tim.taelgar.org` once this file is published. The `title` property supplies the name in the site header; the first Markdown heading supplies the homepage banner. The rest of this file is ordinary Markdown, so you can replace these notes with a campaign introduction, links, images, or embedded notes.

The `campaigns` property selects the campaign-specific passages included alongside shared world content. This example uses three campaign codes:

| Code | Campaign |
| --- | --- |
| `dufr` | Dunmar Frontier |
| `feywild` | Lost in the Feywild |
| `mawar` | Mawar Adventures |

## How the date is chosen

- **One campaign:** use that campaign's latest published session date. An authored `date` does not override it.
- **Multiple campaigns:** use the `date` in this file's properties, or Modern when it is omitted.

Modern means the latest in-world date across all published campaigns, with the configured default as a fallback. It is not today's real-world date. This example omits `date`, so it follows Modern as new content is published.

To fix this three-campaign view at a particular date, add a full DR date to the properties at the top of this file, for example:

```yaml
date: 1748-05-05
```

## Keeping the selection

The subdomain keeps the campaign selection and date fixed as you follow links, search, browse sections, or open embedded notes. Editing `context`, `campaigns`, or `date` in a page's address does not override this file. The **Full site** link returns to the main site, where readers can choose their own view. **See Behind the Curtain** and appearance settings remain available on the subsite.

## Editing and publishing

Edit this file in the vault, then publish vault content using the publishing scripts in `taelgarverse-core` for the changes to appear online. Website code is deployed separately through GitHub Actions; pushing a vault commit does not publish this page.

With wildcard DNS and routing configured, another subsite needs only its own `_website/<subdomain>.md` file with a `campaigns` property and a content publication. It does not need a separate website code change.

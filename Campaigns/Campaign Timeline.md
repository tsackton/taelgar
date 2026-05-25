---
headerVersion: 2023.11.25
tags: [meta]
name: Campaign Session Timeline
excludePublish: ["all"]
---
# Campaign Session Timeline

```dataviewjs
const frontmatterFor = page => {
  const file = app.vault.getAbstractFileByPath(page.file.path);
  return app.metadataCache.getFileCache(file)?.frontmatter ?? {};
};

const asArray = value => {
  if (value == null) return [];
  return Array.isArray(value) ? value : [value];
};

const hasSessionNoteTag = frontmatter => {
  return asArray(frontmatter.tags)
    .map(tag => String(tag).replace(/^#/, ""))
    .includes("session-note");
};

const toDate = value => {
  if (value == null || value === "") return null;
  if (value.toMillis && value.toFormat) return value;
  if (value instanceof Date) return dv.date(value.toISOString().slice(0, 10));

  const text = String(value).trim();
  const match = text.match(/^(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?$/);
  if (!match) return null;

  const year = match[1];
  const month = (match[2] ?? "01").padStart(2, "0");
  const day = (match[3] ?? "01").padStart(2, "0");
  return dv.date(`${year}-${month}-${day}`);
};

const fmt = date => date ? date.toFormat("yyyy-MM-dd") : "";
const fmtList = value => asArray(value).map(String).join(", ");
const fmtSessionNumber = value => value == null ? "" : value;
const sessionSortValue = value => value == null || value === "" ? Number.MAX_SAFE_INTEGER : Number(value);

const sessions = dv.pages('"Campaigns"')
  .array()
  .map(page => ({ page, frontmatter: frontmatterFor(page) }))
  .filter(({ frontmatter }) => hasSessionNoteTag(frontmatter))
  .filter(({ frontmatter }) => frontmatter.campaign && frontmatter.DR)
  .map(({ page, frontmatter }) => {
    const start = toDate(frontmatter.DR);
    const explicitEnd = toDate(frontmatter.DR_end);

    return {
      page,
      campaign: String(frontmatter.campaign),
      sessionNumber: frontmatter.sessionNumber,
      start,
      end: explicitEnd ?? start,
      hasExplicitEnd: explicitEnd != null,
      players: fmtList(frontmatter.players)
    };
  })
  .filter(session => session.start && session.end);

dv.header(2, "Current Date by Campaign");

const latestByCampaign = new Map();

for (const session of sessions) {
  const current = latestByCampaign.get(session.campaign);
  const sessionEnd = session.end.toMillis();
  const currentEnd = current?.end.toMillis() ?? -Infinity;

  if (
    !current ||
    sessionEnd > currentEnd ||
    (sessionEnd === currentEnd && session.start.toMillis() > current.start.toMillis()) ||
    (sessionEnd === currentEnd && session.start.toMillis() === current.start.toMillis() &&
      sessionSortValue(session.sessionNumber) > sessionSortValue(current.sessionNumber))
  ) {
    latestByCampaign.set(session.campaign, session);
  }
}

dv.table(
  ["Campaign", "Current DR", "Latest Session"],
  [...latestByCampaign.values()]
    .sort((a, b) =>
      b.end.toMillis() - a.end.toMillis() ||
      String(a.campaign).localeCompare(String(b.campaign))
    )
    .map(session => [
      session.campaign,
      fmt(session.end),
      session.page.file.link
    ])
);

dv.header(2, "Campaign Timeline");

dv.table(
  ["DR Start", "DR End", "Campaign", "#", "Players", "Session"],
  sessions
    .sort((a, b) =>
      a.start.toMillis() - b.start.toMillis() ||
      a.end.toMillis() - b.end.toMillis() ||
      String(a.campaign).localeCompare(String(b.campaign)) ||
      sessionSortValue(a.sessionNumber) - sessionSortValue(b.sessionNumber) ||
      String(a.page.file.name).localeCompare(String(b.page.file.name))
    )
    .map(session => [
      fmt(session.start),
      session.hasExplicitEnd ? fmt(session.end) : "",
      session.campaign,
      fmtSessionNumber(session.sessionNumber),
      session.players,
      session.page.file.link
    ])
);
```

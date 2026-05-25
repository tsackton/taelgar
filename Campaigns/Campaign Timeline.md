---
headerVersion: 2023.11.25
tags: [meta, status/check/ai]
name: Campaign Session Timeline
excludePublish: ["all"]
---
# Campaign Session Timeline

```dataviewjs
const { DateManager } = customJS;

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

const normalizeDR = (value, isEnd) => {
  if (value == null || value === "") return null;
  if (value.isNormalizedDate) return value;
  if (value instanceof Date) value = value.toISOString().slice(0, 10);
  if (value.toISODate) value = value.toISODate();
  return DateManager.normalizeDate(value, isEnd) ?? null;
};

const formatRealWorldDate = value => {
  if (value == null || value === "") return "";
  if (value instanceof Date) return window.moment(value).format("dddd, MMMM Do, YYYY");
  if (value.toJSDate) return window.moment(value.toJSDate()).format("dddd, MMMM Do, YYYY");
  if (value.toISODate) return window.moment(value.toISODate(), "YYYY-MM-DD").format("dddd, MMMM Do, YYYY");
  const match = String(value).trim().match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/);
  if (!match) return String(value);
  return window.moment(
    `${match[1]}-${match[2].padStart(2, "0")}-${match[3].padStart(2, "0")}`,
    "YYYY-MM-DD"
  ).format("dddd, MMMM Do, YYYY");
};

const fmtDR = date => date?.display ?? "";
const fmtList = value => asArray(value).map(String).join(", ");
const fmtSessionNumber = value => value == null ? "" : value;
const sessionSortValue = value => value == null || value === "" ? Number.MAX_SAFE_INTEGER : Number(value);

const sessions = dv.pages('"Campaigns"')
  .array()
  .map(page => ({ page, frontmatter: frontmatterFor(page) }))
  .filter(({ frontmatter }) => hasSessionNoteTag(frontmatter))
  .filter(({ frontmatter }) => frontmatter.campaign && frontmatter.DR)
  .map(({ page, frontmatter }) => {
    const start = normalizeDR(frontmatter.DR, false);
    const explicitEnd = normalizeDR(frontmatter.DR_end, true);

    return {
      page,
      campaign: String(frontmatter.campaign),
      sessionNumber: frontmatter.sessionNumber,
      start,
      end: explicitEnd ?? start,
      hasExplicitEnd: explicitEnd != null,
      realWorldDate: formatRealWorldDate(frontmatter.realWorldDate),
      players: fmtList(frontmatter.players)
    };
  })
  .filter(session => session.start && session.end);

dv.header(2, "Current Date by Campaign");

const latestByCampaign = new Map();

for (const session of sessions) {
  const current = latestByCampaign.get(session.campaign);
  const sessionEnd = session.end.sort;
  const currentEnd = current?.end.sort ?? -Infinity;

  if (
    !current ||
    sessionEnd > currentEnd ||
    (sessionEnd === currentEnd && session.start.sort > current.start.sort) ||
    (sessionEnd === currentEnd && session.start.sort === current.start.sort &&
      sessionSortValue(session.sessionNumber) > sessionSortValue(current.sessionNumber))
  ) {
    latestByCampaign.set(session.campaign, session);
  }
}

dv.table(
  ["Campaign", "Current Date", "Real World Date", "Latest Session"],
  [...latestByCampaign.values()]
    .sort((a, b) =>
      b.end.sort - a.end.sort ||
      String(a.campaign).localeCompare(String(b.campaign))
    )
    .map(session => [
      session.campaign,
      fmtDR(session.end),
      session.realWorldDate,
      session.page.file.link
    ])
);

dv.header(2, "Campaign Timeline");

dv.table(
  ["Start", "End", "Campaign", "#", "Players", "Session"],
  sessions
    .sort((a, b) =>
      a.start.sort - b.start.sort ||
      a.end.sort - b.end.sort ||
      String(a.campaign).localeCompare(String(b.campaign)) ||
      sessionSortValue(a.sessionNumber) - sessionSortValue(b.sessionNumber) ||
      String(a.page.file.name).localeCompare(String(b.page.file.name))
    )
    .map(session => [
      fmtDR(session.start),
      fmtDR(session.end),
      session.campaign,
      fmtSessionNumber(session.sessionNumber),
      session.players,
      session.page.file.link
    ])
);
```

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
const LONG_SPAN_DAYS = 14;

const pad2 = value => String(value).padStart(2, "0");
const lastDayOfMonth = month => ({
  1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
})[month];

const isoDR = (value, isEnd) => {
  if (value == null || value === "") return null;
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  if (value.toISODate) return value.toISODate();

  const text = String(value).trim();
  const match = text.match(/^(\d{4})(?:-(\d{1,2})(?:-(\d{1,2}))?)?$/);
  if (!match) return null;

  const year = match[1];
  const month = match[2] ? Number(match[2]) : (isEnd ? 1 : 12);
  const day = match[3] ? Number(match[3]) : (
    match[2] ? (isEnd ? 1 : lastDayOfMonth(month)) : (isEnd ? 1 : 31)
  );
  return `${year}-${pad2(month)}-${pad2(day)}`;
};

const mermaidText = value => String(value).replace(/[,:]/g, " -").replace(/\s+/g, " ").trim();

const sessions = dv.pages('"Campaigns"')
  .array()
  .map(page => ({ page, frontmatter: frontmatterFor(page) }))
  .filter(({ frontmatter }) => hasSessionNoteTag(frontmatter))
  .filter(({ frontmatter }) => frontmatter.campaign && frontmatter.DR)
  .map(({ page, frontmatter }) => {
    const start = normalizeDR(frontmatter.DR, false);
    const explicitEnd = normalizeDR(frontmatter.DR_end, true);
    const startIso = isoDR(frontmatter.DR, false);
    const explicitEndIso = isoDR(frontmatter.DR_end, true);

    return {
      page,
      campaign: String(frontmatter.campaign),
      sessionNumber: frontmatter.sessionNumber,
      start,
      end: explicitEnd ?? start,
      hasExplicitEnd: explicitEnd != null,
      startIso,
      endIso: explicitEndIso ?? startIso,
      realWorldDate: formatRealWorldDate(frontmatter.realWorldDate),
      players: fmtList(frontmatter.players)
    };
  })
  .filter(session => session.start && session.end && session.startIso && session.endIso)
  .map(session => ({
    ...session,
    durationDays: session.end.sort - session.start.sort
  }));

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

const timelineRows = sessions.flatMap(session => {
  if (session.durationDays >= LONG_SPAN_DAYS) {
    return [
      { session, point: "Start", sort: session.start.sort, start: fmtDR(session.start), end: "" },
      { session, point: "End", sort: session.end.sort, start: "", end: fmtDR(session.end) }
    ];
  }

  return [{
    session,
    point: "",
    sort: session.start.sort,
    start: fmtDR(session.start),
    end: fmtDR(session.end)
  }];
});

dv.table(
  ["Start", "End", "Point", "Campaign", "#", "Players", "Session"],
  timelineRows
    .sort((a, b) =>
      a.sort - b.sort ||
      String(a.session.campaign).localeCompare(String(b.session.campaign)) ||
      sessionSortValue(a.session.sessionNumber) - sessionSortValue(b.session.sessionNumber) ||
      String(a.point).localeCompare(String(b.point)) ||
      String(a.session.page.file.name).localeCompare(String(b.session.page.file.name))
    )
    .map(row => [
      row.start,
      row.end,
      row.point,
      row.session.campaign,
      fmtSessionNumber(row.session.sessionNumber),
      row.session.players,
      row.session.page.file.link
    ])
);

dv.header(2, "Arc Lanes");

const longSpans = sessions
  .filter(session => session.durationDays >= LONG_SPAN_DAYS)
  .sort((a, b) =>
    String(a.campaign).localeCompare(String(b.campaign)) ||
    a.start.sort - b.start.sort ||
    a.end.sort - b.end.sort ||
    String(a.page.file.name).localeCompare(String(b.page.file.name))
  );

if (longSpans.length === 0) {
  dv.paragraph("No session notes span two weeks or more.");
} else {
  const lines = [
    "gantt",
    "    title Campaign Arcs and Long Spans",
    "    dateFormat YYYY-MM-DD",
    "    axisFormat %Y-%m"
  ];

  let activeCampaign = null;
  for (const session of longSpans) {
    if (session.campaign !== activeCampaign) {
      activeCampaign = session.campaign;
      lines.push(`    section ${mermaidText(activeCampaign)}`);
    }

    const label = mermaidText(
      session.sessionNumber == null
        ? session.page.file.name
        : `Session ${session.sessionNumber} - ${session.page.file.name}`
    );
    lines.push(`    ${label} : ${session.startIso}, ${session.endIso}`);
  }

  const element = dv.el("div", lines.join("\n"), { cls: "mermaid" });
  if (window.mermaid?.run) {
    await window.mermaid.run({ nodes: [element] });
  }
}
```

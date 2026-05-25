---
headerVersion: 2023.11.25
tags: [meta]
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
  .filter(session => session.start && session.end)
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

const laneSessions = sessions
  .sort((a, b) =>
    String(a.campaign).localeCompare(String(b.campaign)) ||
    a.start.sort - b.start.sort ||
    a.end.sort - b.end.sort ||
    String(a.page.file.name).localeCompare(String(b.page.file.name))
  );

if (laneSessions.length === 0) {
  dv.paragraph("No dated session notes found.");
} else {
  const minSort = Math.min(...laneSessions.map(session => session.start.sort));
  const maxSort = Math.max(...laneSessions.map(session => session.end.sort));
  const totalDays = Math.max(1, maxSort - minSort + 1);
  const pxPerDay = Math.max(0.45, Math.min(2.5, 6400 / totalDays));
  const chartWidth = Math.ceil(totalDays * pxPerDay);
  const labelWidth = 190;

  const campaigns = [...new Set(laneSessions.map(session => session.campaign))];
  const campaignColors = new Map(campaigns.map((campaign, index) => [
    campaign,
    [
      "#5277c3", "#9a5fbd", "#bd5f73", "#4f8f6f",
      "#b17b32", "#627d35", "#b15d3e", "#4f7f9f"
    ][index % 8]
  ]));

  const root = dv.el("div", "", { cls: "campaign-lane-chart" });
  const style = document.createElement("style");
  style.textContent = `
    .campaign-lane-chart {
      margin-top: 0.75rem;
      font-size: var(--font-ui-small);
    }
    .campaign-lane-chart__viewport {
      border: 1px solid var(--background-modifier-border);
      border-radius: 6px;
      overflow-x: auto;
      background: var(--background-primary);
    }
    .campaign-lane-chart__inner {
      min-width: ${labelWidth + chartWidth}px;
      width: ${labelWidth + chartWidth}px;
    }
    .campaign-lane-chart__axis,
    .campaign-lane-chart__row {
      display: grid;
      grid-template-columns: ${labelWidth}px ${chartWidth}px;
    }
    .campaign-lane-chart__axis-label,
    .campaign-lane-chart__label {
      position: sticky;
      left: 0;
      z-index: 2;
      box-sizing: border-box;
      border-right: 1px solid var(--background-modifier-border);
      background: var(--background-primary);
      font-weight: 600;
    }
    .campaign-lane-chart__axis-label {
      height: 28px;
      border-bottom: 1px solid var(--background-modifier-border);
    }
    .campaign-lane-chart__axis-track,
    .campaign-lane-chart__track {
      position: relative;
      box-sizing: border-box;
      width: ${chartWidth}px;
    }
    .campaign-lane-chart__axis-track {
      height: 28px;
      border-bottom: 1px solid var(--background-modifier-border);
    }
    .campaign-lane-chart__tick {
      position: absolute;
      top: 0;
      bottom: 0;
      border-left: 1px solid var(--background-modifier-border);
      color: var(--text-muted);
      font-size: 10px;
      padding-left: 4px;
      white-space: nowrap;
    }
    .campaign-lane-chart__row {
      min-height: 44px;
      border-bottom: 1px solid var(--background-modifier-border-hover);
    }
    .campaign-lane-chart__row:last-child {
      border-bottom: 0;
    }
    .campaign-lane-chart__label {
      display: flex;
      align-items: center;
      min-height: 44px;
      padding: 0 10px;
    }
    .campaign-lane-chart__track {
      min-height: 44px;
      background-image: linear-gradient(
        to right,
        var(--background-modifier-border-hover) 1px,
        transparent 1px
      );
      background-size: ${Math.max(120, Math.round(365 * pxPerDay))}px 100%;
    }
    .campaign-lane-chart__bar {
      position: absolute;
      top: 10px;
      box-sizing: border-box;
      height: 24px;
      border-radius: 4px;
      padding: 0 6px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      color: white;
      line-height: 24px;
      font-size: 11px;
      cursor: pointer;
      box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.18) inset;
    }
    .campaign-lane-chart__bar.is-short {
      top: 15px;
      height: 14px;
      min-width: 8px;
      border-radius: 999px;
      padding: 0;
    }
  `;
  root.appendChild(style);

  const viewport = document.createElement("div");
  viewport.className = "campaign-lane-chart__viewport";
  const inner = document.createElement("div");
  inner.className = "campaign-lane-chart__inner";
  viewport.appendChild(inner);
  root.appendChild(viewport);

  const positionForSort = sort => Math.round((sort - minSort) * pxPerDay);
  const widthForSession = session => Math.max(8, Math.round((session.end.sort - session.start.sort + 1) * pxPerDay));

  const layoutByCampaign = new Map();
  for (const campaign of campaigns) {
    const levels = [];
    const items = laneSessions
      .filter(session => session.campaign === campaign)
      .map(session => {
        const left = positionForSort(session.start.sort);
        const width = widthForSession(session);
        return { session, left, width, right: left + width };
      });

    for (const item of items) {
      let level = levels.findIndex(rightEdge => item.left > rightEdge + 3);
      if (level === -1) {
        level = levels.length;
        levels.push(0);
      }

      item.level = level;
      levels[level] = item.right;
    }

    layoutByCampaign.set(campaign, {
      items,
      rowHeight: Math.max(44, 42 + ((levels.length - 1) * 18))
    });
  }

  const axis = document.createElement("div");
  axis.className = "campaign-lane-chart__axis";
  const axisLabel = document.createElement("div");
  axisLabel.className = "campaign-lane-chart__axis-label";
  const axisTrack = document.createElement("div");
  axisTrack.className = "campaign-lane-chart__axis-track";
  axis.append(axisLabel, axisTrack);
  inner.appendChild(axis);

  const startYear = Math.min(...laneSessions.map(session => session.start.year));
  const endYear = Math.max(...laneSessions.map(session => session.end.year));
  for (let year = startYear; year <= endYear; year++) {
    const yearStart = DateManager.normalizeDate(year, false);
    if (!yearStart || yearStart.sort < minSort || yearStart.sort > maxSort) continue;

    const tick = document.createElement("div");
    tick.className = "campaign-lane-chart__tick";
    tick.style.left = `${positionForSort(yearStart.sort)}px`;
    tick.textContent = year;
    axisTrack.appendChild(tick);
  }

  for (const campaign of campaigns) {
    const layout = layoutByCampaign.get(campaign);
    const row = document.createElement("div");
    row.className = "campaign-lane-chart__row";
    row.style.minHeight = `${layout.rowHeight}px`;

    const label = document.createElement("div");
    label.className = "campaign-lane-chart__label";
    label.textContent = campaign;
    label.style.minHeight = `${layout.rowHeight}px`;

    const track = document.createElement("div");
    track.className = "campaign-lane-chart__track";
    track.style.minHeight = `${layout.rowHeight}px`;

    for (const { session, left, width, level } of layout.items) {
      const bar = document.createElement("div");
      const isShort = session.durationDays < LONG_SPAN_DAYS;
      bar.className = `campaign-lane-chart__bar${isShort ? " is-short" : ""}`;
      bar.style.left = `${left}px`;
      bar.style.width = `${width}px`;
      bar.style.top = `${(isShort ? 15 : 10) + (level * 18)}px`;
      bar.style.background = campaignColors.get(campaign);

      const sessionLabel = session.sessionNumber == null
        ? session.page.file.name
        : `#${session.sessionNumber} ${session.page.file.name}`;
      const dateLabel = session.start.sort === session.end.sort
        ? fmtDR(session.start)
        : `${fmtDR(session.start)} to ${fmtDR(session.end)}`;

      bar.title = `${sessionLabel}\n${dateLabel}${session.players ? `\n${session.players}` : ""}`;
      if (!isShort && width > 70) bar.textContent = sessionLabel;
      bar.onclick = event => {
        event.preventDefault();
        app.workspace.openLinkText(session.page.file.path, "", false);
      };

      track.appendChild(bar);
    }

    row.append(label, track);
    inner.appendChild(row);
  }
}
```

# Lint Review

Choose a queue, narrow it to a folder or topic, and review ten notes at a time. **Names only** selects notes whose parsed findings all concern naming, language, or pronunciation. Expand a row to read every open finding and its proposals; source links open the cited notes.

This page reads the existing reports; it does not run the linter, validate proposals, or change notes. Category assignments use rule IDs and are browsing aids. Current-version reports are selected by default using [[Taelgar Note Linter]]. Cards count notes, and categories may overlap. Reports that cannot be parsed remain accessible under **Inspect report**.

Review AI-edited content separately in [[AI Review]]. Requires Dataview JavaScript queries. Filters and position persist in this window's session; note edits appear after Dataview refreshes.

```dataviewjs
const reviewKind = "lint";
const sourcePath = dv.current().file.path;

// This view only reads vault files. UI preferences stay in this window's session storage.
const root = dv.container;
const doc = root.ownerDocument;
const values = v => v == null ? [] : Array.isArray(v) ? v : typeof v.array === "function" ? v.array() : [v];
const make = (tag, parent, text, css) => {
    const el = doc.createElement(tag);
    if (text !== undefined) el.textContent = String(text);
    if (css) el.style.cssText = css;
    parent.appendChild(el);
    return el;
};
const link = (parent, path, label) => {
    const el = make("a", parent, label);
    el.className = "internal-link";
    el.setAttribute("href", path);
    el.setAttribute("data-href", path);
    return el;
};
// Render only text, wikilinks, emphasis, and inline code; never execute embedded queries or HTML.
const inline = (parent, text, origin = sourcePath) => {
    const pattern = /\[\[([^\]\n]+)\]\]|`([^`\n]+)`|\*\*([^*\n]+)\*\*/g;
    let end = 0;
    for (const match of text.matchAll(pattern)) {
        parent.appendChild(doc.createTextNode(text.slice(end, match.index)));
        if (match[1]) {
            const [target, ...alias] = match[1].split("|");
            const resolved = target.startsWith("#") ? {path: origin} : dv.app.metadataCache.getFirstLinkpathDest(target.split("#")[0], origin);
            const hash = target.includes("#") ? "#" + target.split("#").slice(1).join("#") : "";
            link(parent, resolved ? resolved.path + hash : target, alias.join("|") || target);
        } else make(match[2] ? "code" : "strong", parent, match[2] || match[3]);
        end = match.index + match[0].length;
    }
    parent.appendChild(doc.createTextNode(text.slice(end)));
};
const noteTags = p => values(p.file.etags).map(t => String(t).replace(/^#/, ""));
const has = (p, tag) => noteTags(p).includes(tag);
const backlinks = p => new Set(values(p.file.inlinks).map(l => l.path)).size;
const byName = (a, b) => String(a.p.name || a.p.file.name).localeCompare(String(b.p.name || b.p.file.name));
const within = (p, folder) => !folder || p.file.folder === folder || p.file.folder.startsWith(folder + "/");
const nameMatches = (p, query) => [p.file.name, p.name, ...values(p.aliases)]
    .some(v => String(v ?? "").toLocaleLowerCase().includes(query.trim().toLocaleLowerCase()));
const fmt = n => n.toLocaleString();
let storage;
try { storage = doc.defaultView?.sessionStorage; } catch (_) { /* Optional in restricted renderers. */ }
const storageKey = "taelgar-review:" + dv.app.vault.getName() + ":" + reviewKind;
let saved = {};
try { saved = JSON.parse(storage?.getItem(storageKey) || "{}"); } catch (_) { /* Storage may be unavailable. */ }
let pageNumber = Number.isInteger(saved.page) && saved.page >= 0 ? saved.page : 0;
const fields = {};
const cards = make("div", root, undefined, "display:flex;flex-wrap:wrap;gap:0.65em;margin:1em 0");
const controls = make("div", root, undefined, "display:flex;flex-wrap:wrap;align-items:end;gap:0.8em;padding:1em;border:1px solid var(--background-modifier-border);border-radius:10px;background:var(--background-secondary)");
const field = (key, label, options, initial = "") => {
    const wrap = make("label", controls, undefined, "display:flex;flex-direction:column;gap:0.3em;max-width:100%;font-size:var(--font-smaller)");
    make("span", wrap, label);
    const el = make(options ? "select" : "input", wrap);
    if (options) for (const [value, title] of options) {
        const option = make("option", el, title);
        option.value = value;
    }
    else { el.type = "search"; el.placeholder = label; }
    el.style.maxWidth = "100%";
    const value = saved[key] ?? initial;
    el.value = !options || options.some(o => o[0] === value) ? value : initial;
    fields[key] = el;
    return el;
};
const folderOptions = pages => {
    const paths = new Set();
    for (const p of pages) {
        const bits = p.file.folder.split("/").filter(Boolean);
        bits.forEach((_, i) => paths.add(bits.slice(0, i + 1).join("/")));
    }
    return [["", "All folders"], ...[...paths].sort().map(p => [p, p])];
};
const remember = () => {
    try { storage?.setItem(storageKey, JSON.stringify({page: pageNumber,
        ...Object.fromEntries(Object.entries(fields).map(([key, el]) => [key, el.value]))})); } catch (_) { /* Optional. */ }
};
const summary = make("p", root, "Loading notes…", "color:var(--text-muted);font-size:var(--font-smaller)");
const navigation = make("div", root, undefined, "display:flex;flex-wrap:wrap;align-items:center;gap:0.8em;margin:1em 0");
const previous = make("button", navigation, "Previous");
const position = make("span", navigation);
const next = make("button", navigation, "Next");
const reset = make("button", navigation, "Reset filters");
const output = make("div", root, undefined, "overflow-x:auto");
const cardButtons = [];
const card = (label, count, active, action) => {
    const button = make("button", cards, undefined, "display:flex;flex-direction:column;align-items:flex-start;gap:0.3em;height:auto;white-space:normal;text-align:left;padding:0.7em 1em;border-radius:9px;min-width:125px");
    make("strong", button, fmt(count), "display:block;font-size:1.5em;line-height:1.2");
    make("span", button, label, "font-size:var(--font-smaller)");
    button.addEventListener("click", () => { action(); pageNumber = 0; render(); });
    cardButtons.push({button, active});
};
const badge = (parent, text, severity = "") => {
    const color = {error: "var(--text-error)", warning: "var(--text-warning)", suggestion: "var(--text-muted)"}[severity] || "var(--text-muted)";
    return make("span", parent, text, `display:inline-block;font-size:var(--font-smaller);padding:0.1em 0.45em;margin:0.15em 0.3em 0.15em 0;border:1px solid var(--background-modifier-border);border-radius:5px;color:${color}`);
};
const table = titles => {
    output.replaceChildren();
    const el = make("table", output, undefined, "width:100%;font-size:var(--font-smaller)");
    el.className = "dataview table-view-table";
    const tr = make("tr", make("thead", el));
    titles.forEach(t => make("th", tr, t));
    return make("tbody", el);
};
const paginate = rows => {
    const size = Number(fields.size.value);
    const count = Math.max(1, Math.ceil(rows.length / size));
    pageNumber = Math.min(pageNumber, count - 1);
    previous.disabled = pageNumber === 0;
    next.disabled = pageNumber === count - 1;
    const start = pageNumber * size;
    position.textContent = rows.length ? `Showing ${fmt(start + 1)}–${fmt(Math.min(start + size, rows.length))} of ${fmt(rows.length)} notes · Page ${pageNumber + 1} of ${count}` : "0 matching notes";
    for (const c of cardButtons) {
        const active = c.active();
        c.button.setAttribute("aria-pressed", String(active));
        c.button.style.background = active ? "var(--background-modifier-hover)" : "var(--background-primary)";
        c.button.style.border = `1px solid ${active ? "var(--interactive-accent)" : "var(--background-modifier-border)"}`;
    }
    remember();
    return rows.slice(start, start + size);
};
const wire = defaults => {
    for (const el of Object.values(fields)) el.addEventListener(el.tagName === "INPUT" ? "input" : "change", () => { pageNumber = 0; render(); });
    previous.addEventListener("click", () => { pageNumber--; render(); });
    next.addEventListener("click", () => { pageNumber++; render(); });
    reset.addEventListener("click", () => {
        Object.entries(fields).forEach(([key, el]) => { el.value = defaults[key] ?? ""; });
        pageNumber = 0; render();
    });
};
// Bound concurrent reads to keep large queues responsive and report individual failures.
const load = async (pages, transform) => {
    const rows = new Array(pages.length);
    let index = 0;
    await Promise.all(Array.from({length: Math.min(8, pages.length)}, async () => {
        while (index < pages.length) {
            const i = index++;
            const p = pages[i];
            try {
                const file = dv.app.vault.getAbstractFileByPath(p.file.path);
                if (!file) throw new Error("File not found");
                rows[i] = {p, ...transform(await dv.app.vault.cachedRead(file))};
            } catch (_) { rows[i] = {p, unreadable: true}; }
        }
    }));
    return rows;
};

const spec = dv.page("_MoC/Taelgar Note Linter");
const currentVersion = String(spec?.linterVersion ?? "");
if (!currentVersion) {
    summary.textContent = "Cannot read linterVersion from Taelgar Note Linter. Open the specification and refresh this view.";
    return;
}
const pages = dv.pages("#status/check/lint").array().filter(p => has(p, "status/check/lint"));
const category = rule => {
    if (/^(metadata\.(names(?:_|\.)|pronunciation|language)|correctness\.name(?:$|_))/.test(rule)) return "names";
    if (/^(correctness\.|temporal\.)/.test(rule) || /(?:conflict|mismatch|chronology)/.test(rule)) return "conflicts";
    if (/^coverage\.(established_fact_missing|later_material_change)/.test(rule)) return "coverage";
    return "other";
};
const parse = text => {
    const blocks = [...text.matchAll(/^%%\^Lint%%[ \t]*\r?\n([\s\S]*?)^%%\^End%%/gm)];
    if (blocks.length !== 1) return {findings: [], problem: blocks.length ? "Multiple Lint blocks" : "Missing or incomplete Lint block"};
    const section = blocks[0][1].split(/^### Open findings\s*$/m);
    if (section.length !== 2) return {findings: [], problem: "Missing or repeated Open findings heading"};
    const open = section[1].split(/^### /m)[0];
    const tasks = [...open.matchAll(/^- \[ \] ([\s\S]*?)(?=^- \[[ xX]\] |$(?![\s\S]))/gm)];
    const findings = tasks.map(m => {
        const match = m[1].match(/^\*\*(Error|Warning|Suggestion)\s*[—–-]\s*([^:*]+):\*\*\s*([\s\S]*)/i);
        if (!match) return {severity: "unknown", rule: "Unparsed finding", category: "other", text: m[1].trim()};
        const rule = match[2].trim();
        return {severity: match[1].toLowerCase(), rule, category: category(rule), text: match[3].trim()};
    });
    const problem = !findings.length ? "No open tasks found" : findings.some(f => f.severity === "unknown") ? "Unrecognized finding format" : "";
    return {findings, problem};
};
const rows = (await load(pages, parse)).map(r => ({...r, findings: r.findings || [],
    problem: r.unreadable ? "Could not read note" : r.problem,
    current: String(r.p.lintVersion ?? "") === currentVersion}));
field("version", "Report version", [["current", `Current (${currentVersion})`], ["older", "Other / missing version"], ["all", "All versions"]], "current");
field("queue", "Review queue", [["all", "All findings"], ["errors", "Errors"], ["names", "Names and pronunciation"], ["coverage", "Missing established information"], ["conflicts", "Conflicts and chronology"], ["other", "Editorial and other"], ["problems", "Report needs inspection"]], "all");
field("only", "Other findings", [["any", "Include mixed notes"], ["only", "Only this category / severity"]], "any");
field("severity", "Severity", [["", "Any severity"], ["error", "Error"], ["warning", "Warning"], ["suggestion", "Suggestion"]]);
field("folder", "Folder + subfolders", folderOptions(pages));
field("name", "Name or alias");
field("text", "Finding text or rule");
field("sort", "Sort", [["severity", "Severity, then fewest findings"], ["fewest", "Fewest findings"], ["backlinks", "Most backlinks"], ["name", "Name"]], "severity");
field("size", "Rows", [["10", "10"], ["25", "25"], ["50", "50"]], "10");
const versionRows = () => rows.filter(r => fields.version.value === "all" || (fields.version.value === "current" ? r.current : !r.current));
const queueMatch = (r, key) => key === "all" ? true : key === "problems" ? !!r.problem :
    key === "errors" ? r.findings.some(f => f.severity === "error") : r.findings.some(f => f.category === key);
const count = key => versionRows().filter(r => queueMatch(r, key)).length;
for (const [key, label] of [["all", "All notes"], ["errors", "With errors"], ["names", "Names only"], ["coverage", "Missing information"], ["conflicts", "Conflicts / chronology"], ["other", "Editorial / other"], ["problems", "Inspect report"]]) {
    card(label, key === "names" ? versionRows().filter(r => !r.problem && r.findings.length && r.findings.every(f => f.category === "names")).length : count(key),
        () => fields.queue.value === key && (key !== "names" || fields.only.value === "only"),
        () => { fields.queue.value = key; fields.only.value = key === "names" ? "only" : "any"; fields.severity.value = ""; });
    cardButtons[cardButtons.length - 1].key = key;
}
const rank = r => Math.max(0, ...r.findings.map(f => ({error: 3, warning: 2, suggestion: 1}[f.severity] || 0)));
function render() {
    for (const c of cardButtons) c.button.querySelector("strong").textContent = fmt(c.key === "names"
        ? versionRows().filter(r => !r.problem && r.findings.length && r.findings.every(f => f.category === "names")).length : count(c.key));
    const key = fields.queue.value;
    const query = fields.text.value.trim().toLocaleLowerCase();
    const selectedFinding = f => (!fields.severity.value || f.severity === fields.severity.value)
        && (key === "errors" ? f.severity === "error" : ["all", "problems"].includes(key) || f.category === key)
        && (!query || (f.rule + " " + f.text).toLocaleLowerCase().includes(query));
    const filtered = versionRows().filter(r => within(r.p, fields.folder.value) && nameMatches(r.p, fields.name.value)
        && queueMatch(r, key)
        && ((!fields.severity.value && !query && ["all", "problems"].includes(key)) || r.findings.some(selectedFinding))
        && (fields.only.value !== "only" || (!r.problem && r.findings.length > 0 && r.findings.every(f =>
            (!fields.severity.value || f.severity === fields.severity.value) &&
            (key === "errors" ? f.severity === "error" : ["all", "problems"].includes(key) || f.category === key)))));
    filtered.sort((a, b) => (fields.sort.value === "severity" ? rank(b) - rank(a) || a.findings.length - b.findings.length :
        fields.sort.value === "fewest" ? a.findings.length - b.findings.length :
        fields.sort.value === "backlinks" ? backlinks(b.p) - backlinks(a.p) : 0) || byName(a, b));
    summary.textContent = `${fmt(rows.length)} tagged notes · ${fmt(versionRows().length)} in selected version scope. Cards count notes before folder, search, and severity filters; categories can overlap. Every expanded row shows all its findings.`;
    const body = table(["Note", "Folder", "Findings", "Decision preview"]);
    for (const r of paginate(filtered)) {
        const tr = make("tr", body);
        const note = make("td", tr);
        link(note, r.p.file.path, r.p.name || r.p.file.name);
        make("div", note, `${backlinks(r.p)} backlinks · lint ${r.p.lintVersion ?? "missing"}`, "color:var(--text-muted);margin-top:0.35em");
        if (has(r.p, "status/check/ai")) badge(note, "AI review too");
        make("td", tr, r.p.file.folder, "overflow-wrap:anywhere;max-width:200px");
        const counts = make("td", tr);
        for (const sev of ["error", "warning", "suggestion"]) {
            const n = r.findings.filter(f => f.severity === sev).length;
            if (n) badge(counts, `${n} ${sev}${n === 1 ? "" : "s"}`, sev);
        }
        if (r.problem) badge(counts, r.problem, "warning");
        const cell = make("td", tr, undefined, "min-width:260px;max-width:650px;overflow-wrap:anywhere");
        if (!r.findings.length) { make("p", cell, r.problem); continue; }
        const first = r.findings.find(selectedFinding) || r.findings[0];
        const text = first.text.replace(/\s+/g, " ");
        inline(make("div", cell), text.length > 220 ? text.slice(0, 220) + "…" : text, r.p.file.path);
        const details = make("details", cell, undefined, "margin-top:0.5em");
        make("summary", details, `Read all ${r.findings.length} finding${r.findings.length === 1 ? "" : "s"}`);
        for (const f of r.findings) {
            const finding = make("div", details, undefined, "padding:0.7em 0;border-bottom:1px solid var(--background-modifier-border)");
            badge(finding, f.severity, f.severity);
            make("code", finding, f.rule);
            inline(make("div", finding, undefined, "white-space:pre-wrap;margin-top:0.4em"), f.text, r.p.file.path);
        }
    }
    if (!filtered.length) make("p", output, "No notes match these filters. Try another queue or reset the filters.");
}
wire({version: "current", queue: "all", only: "any", severity: "", sort: "severity", size: "10"});
render();
```

# AI Review

Choose a small batch of notes to read. **Short articles** is useful for a brief review session; the climate filter lets you focus on other material. Expand an article preview or open its note to read it in context.

The AI-review tag marks a need for human review; it does not establish who wrote each passage or the extent of AI changes. Article lengths and previews exclude frontmatter, generated information headers, code, comments, and persistent metadata as far as practical. Previews simplify formatting and are not a publication preview. Use the original note to check comments, embeds, and full context. A file's modified time is not its AI-tag date.

Open lint findings are a separate review in [[Lint Review]]. This page never changes notes or clears tags; absence of the lint tag does not establish a completed clean lint. Requires Dataview JavaScript queries. Filters and position persist in this window's session; note edits appear after Dataview refreshes.

```dataviewjs
const reviewKind = "ai";
const sourcePath = dv.current().file.path;

// This view only reads vault files. UI preferences stay in this window's session storage.
const root = dv.container;
const doc = root.ownerDocument;
// Dataview also reports its wrapped lists as arrays; unwrap them before native array operations.
const values = v => v == null ? [] : typeof v.array === "function" ? Array.from(v.array()) : Array.isArray(v) ? Array.from(v) : [v];
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

const pages = dv.pages("#status/check/ai").array().filter(p => has(p, "status/check/ai"));
const article = text => text
    .replace(/^---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/, "")
    .replace(/^%%\^(?:Metadata:[^%\n]+|povNotes:[^%\n]+|Lint|Campaign:none)%%[^\n]*\n[\s\S]*?^%%\^End%%[^\n]*/gmi, "")
    .replace(/%%\^Campaign:none%%[^\n]*?%%\^End%%/gi, "")
    .replace(/%%[\s\S]*?%%/g, "")
    .replace(/^>\s*\[!info\][^\n]*(?:\n>[^\n]*)*/gm, "")
    .replace(/^\s*(```|~~~)[^\n]*\n[\s\S]*?^\s*\1[^\n]*/gm, "")
    .replace(/`[^`\n]*`/g, "")
    .replace(/!\[\[[^\]]*\]\]/g, "")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, "")
    .replace(/^#+\s*/gm, "")
    .replace(/\n{3,}/g, "\n\n").trim();
const plain = text => text.replace(/\[\[([^\]]+)\]\]/g, (_, s) => s.split("|").pop())
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1").replace(/[*_~]/g, "");
const rows = (await load(pages, text => {
    const body = article(text);
    return {article: body, words: (plain(body).match(/[\p{L}\p{N}]+(?:[’'-][\p{L}\p{N}]+)*/gu) || []).length};
})).map(r => ({...r, climate: r.p.file.path.startsWith("Background/Climate and Environment/"),
    lint: has(r.p, "status/check/lint"), flags: noteTags(r.p).filter(t => t.startsWith("status/") && t !== "status/check/ai")}));
field("queue", "Review queue", [["all", "All AI review"], ["no-lint", "No open lint tag"], ["lint", "Also has open lint"], ["short", "Short articles (≤ 250 words)"], ["unreadable", "Could not read note"]], "all");
field("folder", "Folder + subfolders", folderOptions(pages));
field("name", "Name or alias");
field("climate", "Climate material", [["include", "Include climate"], ["exclude", "Exclude climate"], ["only", "Only climate"]], "include");
const flags = [...new Set(rows.flatMap(r => r.flags))].sort();
field("flag", "Other status", [["", "Any other status"], ["none", "No other status tags"], ...flags.map(t => [t, t.replace(/^status\//, "")])]);
field("sort", "Sort", [["shortest", "Shortest article"], ["backlinks", "Most backlinks"], ["name", "Name"], ["modified", "Recently modified"]], "shortest");
field("size", "Rows", [["10", "10"], ["25", "25"], ["50", "50"]], "10");
const scopeRows = () => rows.filter(r => fields.climate.value === "include" || (fields.climate.value === "only" ? r.climate : !r.climate));
const queueMatch = (r, key) => key === "all" || (key === "lint" ? r.lint : key === "no-lint" ? !r.lint : key === "unreadable" ? r.unreadable : !r.unreadable && r.words <= 250);
for (const [key, label] of [["all", "Awaiting AI review"], ["no-lint", "No open lint tag"], ["lint", "Open lint too"], ["short", "Short articles"], ["unreadable", "Unreadable notes"]]) {
    card(label, scopeRows().filter(r => queueMatch(r, key)).length, () => fields.queue.value === key, () => { fields.queue.value = key; });
    cardButtons[cardButtons.length - 1].key = key;
}
function render() {
    for (const c of cardButtons) c.button.querySelector("strong").textContent = fmt(scopeRows().filter(r => queueMatch(r, c.key)).length);
    const filtered = scopeRows().filter(r => queueMatch(r, fields.queue.value) && within(r.p, fields.folder.value) && nameMatches(r.p, fields.name.value)
        && (!fields.flag.value || (fields.flag.value === "none" ? !r.flags.length : r.flags.includes(fields.flag.value))));
    const millis = v => typeof v?.toMillis === "function" ? v.toMillis() : Number(v) || 0;
    filtered.sort((a, b) => (fields.sort.value === "shortest" ? (a.words ?? Infinity) - (b.words ?? Infinity) :
        fields.sort.value === "backlinks" ? backlinks(b.p) - backlinks(a.p) :
        fields.sort.value === "modified" ? millis(b.p.file.mtime) - millis(a.p.file.mtime) : 0) || byName(a, b));
    summary.textContent = `${fmt(rows.length)} tagged notes · ${fmt(rows.filter(r => r.climate).length)} climate · ${fmt(scopeRows().length)} in selected climate scope. Cards count notes before other filters. Word counts are approximate visible article text; modified dates describe file edits, not when AI review began.`;
    const body = table(["Note", "Folder", "Article", "Other review flags", "Backlinks"]);
    for (const r of paginate(filtered)) {
        const tr = make("tr", body);
        link(make("td", tr), r.p.file.path, r.p.name || r.p.file.name);
        make("td", tr, r.p.file.folder, "overflow-wrap:anywhere;max-width:180px");
        const cell = make("td", tr, undefined, "min-width:250px;max-width:650px;overflow-wrap:anywhere");
        if (r.unreadable) badge(cell, "Could not read note", "warning");
        else {
            make("strong", cell, `~${fmt(r.words)} words`);
            const details = make("details", cell, undefined, "margin-top:0.4em");
            make("summary", details, "Preview article");
            const preview = make("div", details, undefined, "white-space:pre-wrap;max-height:28em;overflow-y:auto;margin-top:0.6em;line-height:1.6");
            inline(preview, r.article.slice(0, 6000) || "No article text after excluding comments and generated material.", r.p.file.path);
            if (r.article.length > 6000) make("p", details, "Preview shortened. Open the note to read the full article.");
            link(make("p", details), r.p.file.path, "Open note for review →");
        }
        const status = make("td", tr);
        if (!r.flags.length) make("span", status, "—");
        for (const flag of r.flags) badge(status, flag.replace(/^status\//, ""));
        make("td", tr, backlinks(r.p));
    }
    if (!filtered.length) make("p", output, "No notes match these filters. Try another queue or reset the filters.");
}
wire({queue: "all", climate: "include", sort: "shortest", size: "10"});
render();
```

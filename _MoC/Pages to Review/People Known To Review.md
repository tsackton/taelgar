---
tags: [meta, status/check/ai]
---
# People Known To Review

Choose a campaign, then work through a small table at a time. **Start with “Linked, missing knownTo”**: these people have incoming links from that campaign’s directory but lack its code in `knownTo`. Use the folder and name filters to narrow a batch; expand the source count to open the relevant campaign pages.

This view includes indexed `#person` notes, including people outside the People folder. “Not marked known” means only that the selected code is absent, not that the party definitely does not know the person. Missing fields, blank fields, and explicit empty lists are shown separately. Links from any page in the campaign directory count as review evidence, including planning and source pages; they do not establish party knowledge. `campaignInfo` is supporting evidence only. Edit the person note after reviewing the sources; this page never changes metadata.

Campaigns and directories come from [[Campaign Registry]] and its configuration. See [[Metadata Specification#KnownTo Framework|KnownTo Framework]] for the meaning of the field. Requires Dataview JavaScript queries; tables update when Dataview refreshes after note edits.

```dataviewjs
const registry = JSON.parse(await dv.app.vault.adapter.read("_scripts/session_note_campaigns.json"));
const campaigns = Object.values(registry.campaigns).sort((a, b) => a.name.localeCompare(b.name));
const values = value => value == null ? [] : Array.isArray(value) ? value :
    typeof value.array === "function" ? value.array() : [value];
const people = dv.pages("#person").array();
const root = dv.container;
const make = (tag, parent, text) => {
    const element = document.createElement(tag);
    if (text !== undefined) element.textContent = text;
    parent.appendChild(element);
    return element;
};
const controls = make("div", root);
controls.style.cssText = "display:flex;flex-wrap:wrap;gap:0.8em;align-items:end;margin-bottom:1em";
const select = (label, options) => {
    const wrapper = make("label", controls, label + " ");
    const element = make("select", wrapper);
    for (const [value, text] of options) {
        const option = make("option", element, text);
        option.value = value;
    }
    return element;
};
const campaign = select("Campaign", campaigns.map(c => [c.code, `${c.name} (${c.code})`]));
campaign.value = campaigns.some(c => c.code === "dufr") ? "dufr" : campaigns[0].code;
const group = select("Review group", [
    ["priority", "Linked, missing knownTo"],
    ["known", "Marked known"],
    ["other", "Other not marked known"],
]);
const folder = select("Folder", [["", "All folders"], ...[...new Set(people.map(p => p.file.folder))]
    .sort().map(path => [path, path || "Vault root"])]);
const searchLabel = make("label", controls, "Name ");
const search = make("input", searchLabel);
search.type = "search";
search.placeholder = "Name or alias";
const size = select("Rows", [["25", "25"], ["50", "50"], ["10", "10"]]);
const summary = make("p", root);
const navigation = make("div", root);
navigation.style.cssText = "display:flex;gap:1em;align-items:center;margin-bottom:1em";
const previous = make("button", navigation, "Previous");
const position = make("span", navigation);
const next = make("button", navigation, "Next");
const output = make("div", root);
let pageNumber = 0;
const link = (parent, path, label) => {
    const anchor = make("a", parent, label);
    anchor.className = "internal-link";
    anchor.setAttribute("data-href", path);
    anchor.setAttribute("href", path);
};
const knownText = p => {
    if (p.knownTo === undefined) return "Missing field";
    if (p.knownTo === null || p.knownTo === "") return "Blank field";
    const entries = values(p.knownTo);
    return entries.length ? entries.map(String).join(", ") : "[] (none recorded)";
};
function render() {
    const selected = campaigns.find(c => c.code === campaign.value);
    const prefix = selected.campaignRoot.replace(/\/$/, "") + "/";
    const rows = people.map(person => {
        // Dataview resolves aliased, relative, and heading links to their target file.
        const sources = [...new Set(values(person.file.inlinks).map(l => l.path))]
            .filter(path => path.startsWith(prefix)).sort();
        const known = values(person.knownTo).some(code => code === selected.code);
        const interactions = values(person.campaignInfo)
            .filter(info => info && String(info.campaign).toLowerCase() === selected.code);
        return {person, sources, interactions, group: known ? "known" : sources.length ? "priority" : "other"};
    });
    const count = key => rows.filter(r => r.group === key).length;
    summary.textContent = `${selected.name}: ${count("priority")} linked, missing knownTo · ${count("known")} marked known · ${count("other")} other not marked known. Counts are before folder/name filters.`;
    const query = search.value.trim().toLocaleLowerCase();
    const filtered = rows.filter(r => r.group === group.value && (!folder.value || r.person.file.folder === folder.value)
        && [r.person.file.name, r.person.name, ...values(r.person.aliases)]
            .some(name => String(name ?? "").toLocaleLowerCase().includes(query)))
        .sort((a, b) => (group.value === "priority" ? b.sources.length - a.sources.length : 0)
            || a.person.file.name.localeCompare(b.person.file.name));
    const pageSize = Number(size.value);
    const pages = Math.max(1, Math.ceil(filtered.length / pageSize));
    pageNumber = Math.min(pageNumber, pages - 1);
    previous.disabled = pageNumber === 0;
    next.disabled = pageNumber >= pages - 1;
    position.textContent = `${filtered.length} people · Page ${pageNumber + 1} of ${pages}`;
    output.replaceChildren();
    if (!filtered.length) {
        make("p", output, "No people match this selection.");
        return;
    }
    const table = make("table", output);
    table.className = "dataview table-view-table";
    const heading = make("tr", make("thead", table));
    for (const title of ["Person", "Folder", "knownTo", "Campaign sources", "campaignInfo"])
        make("th", heading, title);
    const body = make("tbody", table);
    for (const row of filtered.slice(pageNumber * pageSize, (pageNumber + 1) * pageSize)) {
        const tr = make("tr", body);
        link(make("td", tr), row.person.file.path, row.person.name || row.person.file.name);
        make("td", tr, row.person.file.folder);
        make("td", tr, knownText(row.person));
        const sourceCell = make("td", tr);
        if (row.sources.length) {
            const details = make("details", sourceCell);
            make("summary", details, `${row.sources.length} source page${row.sources.length === 1 ? "" : "s"}`);
            for (const path of row.sources) {
                const line = make("div", details);
                link(line, path, path.slice(prefix.length).replace(/\.md$/, ""));
            }
        } else sourceCell.textContent = "No campaign-directory links";
        make("td", tr, row.interactions.length
            ? row.interactions.map(info => `${info.type || "Recorded interaction"}${info.date ? " — " + String(info.date) : " (undated)"}`).join("; ")
            : "—");
    }
}
for (const control of [campaign, group, folder, size]) control.addEventListener("change", () => { pageNumber = 0; render(); });
search.addEventListener("input", () => { pageNumber = 0; render(); });
previous.addEventListener("click", () => { pageNumber--; render(); });
next.addEventListener("click", () => { pageNumber++; render(); });
render();
```

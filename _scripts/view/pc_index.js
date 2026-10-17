// Read-only tables for People/PCs/PC Index.md. Roles belong to party affiliations,
// not to species, folder names, knownTo, or dm_owner.
const options = input ?? {};
const text = value => typeof value === "string" ? value.trim() : "";
const dmOwners = new Set(["tim", "mike", "schwartz", "kong", "eric", "isaac"]);
const validOwners = new Set(["player", ...dmOwners, "joint", "none"]);
const pages = dv.pages('"People/PCs" and #person').array();

// Navigation links, grounded in the campaign landing pages and PC party notes.
// These do not assert that an individual has a missing party affiliation.
const campaigns = [
    ["Addermarch", "Addermarch Mercenaries", "Campaigns/Addermarch Campaign/Addermarch Campaign.md", "Addermarch"],
    ["Dunmar Fellowship", "Dunmar Fellowship", "Campaigns/Dunmari Frontier Campaign/Dunmari Frontier Campaign.md", "Dunmari Frontier"],
    ["Cleenseau", "Heroes of Cleenseau", "Campaigns/Cleenseau Campaign/Cleenseau Campaign.md", "Cleenseau"],
    ["Silver Tempests", "Silver Tempests", "Campaigns/Great Library Campaign/Great Library Campaign.md", "Great Library"],
    ["Great War", "Heroes of the Great War", "Campaigns/Great War Campaign/Great War Campaign.md", "Great War"],
    ["Mawar", "Adventurers of Mawar", "Campaigns/Mawar Adventures/Mawar Adventures.md", "Mawar Adventures"],
    ["Other PCs/Into the Chasm", "Chasm Explorers", "Campaigns/One Shots/Into the Chasm/Into the Chasm.md", "Into the Chasm"],
    ["Other PCs/Labyrinth Prisoners", "Labyrinth Prisoners", "Campaigns/One Shots/Labyrinths of the Lost/Labyrinths of the Lost.md", "Labyrinths of the Lost"],
    ["Other PCs/Tollen Misfits", "Tollen Misfits", "Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild.md", "Lost in the Feywild"],
    ["Other PCs/Oskar's Companions", "Oskar's Companions", "Campaigns/One Shots/Oskar's Adventures/Oskar's Adventures.md", "Oskar's Adventures"]
];
const partyPages = dv.pages('"People/PCs" and #group')
    .where(page => page.typeOf === "adventuring party").array();
const partyByName = new Map();
for (const party of partyPages) {
    partyByName.set(party.file.name, party);
    if (text(party.name)) partyByName.set(text(party.name), party);
}
const name = page => text(page.file.frontmatter.name) || page.file.name;
const characterLink = page => dv.fileLink(page.file.path, false, name(page));
const markdown = value => typeof value === "string" ? value : value.markdown();
const controlGroup = owner => owner === "player" ? "player" : dmOwners.has(owner) ? "dm" : "other";
const control = owner => owner === "player" ? "Player" : dmOwners.has(owner) ? `DM: ${owner}`
    : owner === "joint" ? "Shared" : owner === "none" ? "Unassigned" : "⚠ Check ownership";

const rows = [];
for (const page of pages) {
    const fm = page.file.frontmatter;
    const player = text(fm.player);
    const raw = fm.affiliations ?? [];
    const affiliations = (Array.isArray(raw) ? raw : [raw]).map(value =>
        typeof value === "string" ? { org: value } : value).filter(Boolean);
    const parties = affiliations.map(affiliation => {
        const org = affiliation.org;
        const key = typeof org === "string" ? org.replace(/^\[\[|\]\]$/g, "").split("|")[0] : org?.path;
        const party = partyByName.get(key) ?? (key ? dv.page(key) : null);
        return { affiliation, party: party?.typeOf === "adventuring party" ? party : null };
    }).filter(entry => entry.party);
    const entries = parties.length ? parties : [{ affiliation: null, party: null }];
    for (const { affiliation, party } of entries) {
        const issues = [];
        const title = text(affiliation?.title).toLowerCase();
        let role = "Review";
        if (!party) issues.push("Missing adventuring-party affiliation; role unclassified");
        else if (title === "companion") role = "Companion";
        else if (title === "guest") role = "Guest";
        else if (title === "regular") role = "Regular";
        else if (!title || title === "member") role = "Regular";
        else issues.push(`Clarify affiliation title “${affiliation.title}” as Regular, Guest, or Companion`);

        const folder = page.file.folder.replace(/^People\/PCs\/?/, "");
        const campaign = party
            ? campaigns.find(entry => entry[1] === party.file.name)
            : campaigns.find(entry => folder === entry[0] || folder.startsWith(entry[0] + "/"));
        let campaignCell = "—";
        if (campaign && dv.page(campaign[2])) campaignCell = dv.fileLink(campaign[2], false, campaign[3]);
        else if (folder === "Other PCs/Ausson's Crossing") {
            campaignCell = "Ausson's Crossing (no campaign page)";
            issues.push("No campaign landing page recorded");
        } else issues.push("Campaign link needs mapping");

        rows.push({ page, player, owner: fm.dm_owner, role, issues,
            party: party ? dv.fileLink(party.file.path, false, text(party.name) || party.file.name) : "⚠ Missing",
            campaign: campaignCell,
            about: [text(fm.speciesAlias) || text(fm.species), text(fm.ancestry)].filter(Boolean).join(" · ") || "—"
        });
    }
}
const roleOrder = { Regular: 0, Guest: 1, Companion: 2, Review: 3 };
const sortRows = values => [...values].sort((a, b) => roleOrder[a.role] - roleOrder[b.role]
    || Number(b.owner === "player") - Number(a.owner === "player")
    || name(a.page).localeCompare(name(b.page)));
const category = row => row.role === "Companion" ? "companions" : row.role === "Review" ? "unclassified" : "pcs";
const categories = [["pcs", "PCs"], ["companions", "Companions"], ["unclassified", "Role to classify"]];
function renderCharacters(values) {
    const showRole = values.some(row => category(row) === "pcs");
    dv.table(["Character", ...(showRole ? ["Role"] : []), "Party / campaign", "About", "Control"], sortRows(values).map(row => [
        characterLink(row.page), ...(showRole ? [row.role] : []),
        `${markdown(row.party)}<br>${markdown(row.campaign)}`, row.about, control(row.owner)
    ]));
}
function renderPlayer(values) {
    if (!values.length) return dv.paragraph("No characters in this section.");
    for (const [key, label] of categories) {
        const group = values.filter(row => category(row) === key);
        if (!group.length) continue;
        dv.header(3, label);
        renderCharacters(group);
    }
}
function renderIssues(values) {
    dv.table(["Character", "Player", "Party", "Review"], sortRows(values).map(row => [
        characterLink(row.page), row.player || "—", row.party, row.issues.join("; ")
    ]));
}
function uniquePages(values) {
    return [...new Map(values.map(row => [row.page.file.path, row.page])).values()];
}

if (options.mode === "newPlayers") {
    const source = await dv.io.load(dv.current().file.path);
    const headings = new Set([...source.matchAll(/^## (.+)$/gm)].map(match => match[1]));
    const newPlayers = [...new Set(rows.map(row => row.player).filter(player => player && !headings.has(player)))].sort();
    for (const player of newPlayers) {
        dv.header(2, player);
        renderPlayer(rows.filter(row => row.player === player));
    }
} else if (options.mode === "roles") {
    const review = rows.filter(row => category(row) === "unclassified");
    if (!review.length) dv.paragraph("All characters have a recorded role.");
    else renderIssues(review.map(row => ({ ...row, issues: [...row.issues,
        ...(!row.player ? ["No player recorded; confirm whether this is a PC or companion"] : []),
        ...(!validOwners.has(row.owner) ? ["Missing or unrecognized ownership"] : [])
    ] })));
} else if (options.mode === "review") {
    const selected = rows.filter(row => category(row) === options.category);
    const issues = selected.filter(row => row.issues.length);
    const missingPlayers = selected.filter(row => !row.player);
    const owners = uniquePages(selected).filter(page => !validOwners.has(page.file.frontmatter.dm_owner));
    if (!issues.length && !owners.length && (!missingPlayers.length || options.category === "companions")) {
        dv.paragraph("No metadata issues to review.");
    }
    if (issues.length) {
        dv.header(3, "Party and campaign links");
        renderIssues(issues);
    }
    if (missingPlayers.length) {
        dv.header(3, options.category === "companions" ? "No player recorded — for reference" : "Player names to fill in");
        for (const [key, label] of [["player", "Player-controlled"], ["dm", "DM-controlled"], ["other", "Shared or unassigned"]]) {
            const group = missingPlayers.filter(row => controlGroup(row.owner) === key);
            if (!group.length) continue;
            dv.header(4, label);
            renderCharacters(group);
        }
    }
    if (owners.length) {
        dv.header(3, "Ownership to review");
        dv.table(["Character", "Player", "Recorded owner"], owners.map(page => [
            characterLink(page), text(page.file.frontmatter.player) || "—", text(page.file.frontmatter.dm_owner) || "⚠ Missing"
        ]));
    }
} else {
    renderPlayer(rows.filter(row => row.player === options.player));
}

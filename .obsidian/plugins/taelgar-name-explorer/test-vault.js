"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const os = require("node:os");
const core = require("./core");

// A miniature vault owned entirely by this test, never the working vault.
const vaultRoot = fs.mkdtempSync(path.join(os.tmpdir(), "name-explorer-test-"));

function markdownFiles(directory, output = []) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    const relative = path.relative(vaultRoot, absolute).split(path.sep).join("/");
    if (entry.isDirectory()) {
      if (entry.name === ".git" || entry.name === "node_modules") continue;
      markdownFiles(absolute, output);
    } else if (entry.isFile() && entry.name.endsWith(".md") && core.shouldScanPath(relative)) {
      output.push({ absolute, relative });
    }
  }
  return output;
}

function splitFrontmatter(text) {
  const lines = text.split(/\r?\n/);
  if (lines[0]?.replace(/^\uFEFF/, "").trim() !== "---") {
    return { lines: [], body: text };
  }
  const end = lines.findIndex((line, index) => index > 0 && line.trim() === "---");
  if (end < 0) return { lines: [], body: text };
  return {
    lines: lines.slice(1, end),
    body: lines.slice(end + 1).join("\n"),
  };
}

function stripQuotes(value) {
  const text = String(value || "").trim();
  if (
    text.length >= 2 &&
    ((text.startsWith('"') && text.endsWith('"')) ||
      (text.startsWith("'") && text.endsWith("'")))
  ) return text.slice(1, -1);
  return text;
}

function splitInlineList(value) {
  const text = String(value || "").trim();
  if (!text.startsWith("[") || !text.endsWith("]")) {
    return text ? [stripQuotes(text)] : [];
  }
  const output = [];
  let current = "";
  let quote = "";
  let depth = 0;
  for (const character of text.slice(1, -1)) {
    if (quote) {
      current += character;
      if (character === quote) quote = "";
    } else if (character === '"' || character === "'") {
      quote = character;
      current += character;
    } else if ("[{(".includes(character)) {
      depth += 1;
      current += character;
    } else if ("]})".includes(character)) {
      depth -= 1;
      current += character;
    } else if (character === "," && depth === 0) {
      if (current.trim()) output.push(stripQuotes(current));
      current = "";
    } else {
      current += character;
    }
  }
  if (current.trim()) output.push(stripQuotes(current));
  return output;
}

function field(frontmatter, key) {
  const start = frontmatter.findIndex((line) =>
    new RegExp(`^${key}:`).test(line)
  );
  if (start < 0) return [];
  const line = frontmatter[start];
  const value = line.slice(line.indexOf(":") + 1).trim();
  if (value) return splitInlineList(value);
  const output = [];
  for (let index = start + 1; index < frontmatter.length; index += 1) {
    const child = frontmatter[index];
    if (/^[A-Za-z][A-Za-z0-9_-]*:/.test(child)) break;
    const match = child.match(/^\s*-\s+(.+)$/);
    if (match) output.push(stripQuotes(match[1]));
  }
  return output;
}

function buildSubject(file) {
  const raw = fs.readFileSync(file.absolute, "utf8");
  const { lines, body } = splitFrontmatter(raw);
  const tags = field(lines, "tags").map((tag) =>
    tag.replace(/^#/, "").toLocaleLowerCase("en")
  );
  if (!tags.length) return null;
  const nameMetadata = core.parseNameMetadata(raw);
  const primaryNameMetadata = core.primaryNameMetadataEntry(nameMetadata);
  const fallbackRawName = field(lines, "name")[0] ||
    path.basename(file.relative, ".md");
  const fallbackNameInfo = core.provisionalNameInfo(fallbackRawName);
  const rawName = primaryNameMetadata?.name ||
    fallbackRawName;
  const nameInfo = core.provisionalNameInfo(rawName);
  const noteType = core.chooseNoteType(tags);
  const species = field(lines, "species");
  const subtypeInfo = core.subtypeForSubject(noteType, {
    species,
    typeOf: field(lines, "typeOf"),
  });
  const locations = [];
  for (const line of lines) {
    for (const match of line.matchAll(/\blocation:\s*([^,}\]]+)/g)) {
      locations.push(stripQuotes(match[1]));
    }
  }
  return {
    path: file.relative,
    linkTarget: file.relative.replace(/\.md$/i, ""),
    fileName: path.basename(file.relative, ".md"),
    rawName,
    name: nameInfo.text,
    provisionalName: fallbackNameInfo.provisional || nameInfo.provisional,
    noteType,
    subtypes: subtypeInfo.values,
    subtypeLabel: subtypeInfo.label,
    subtypeSource: subtypeInfo.source,
    tags,
    title: field(lines, "title"),
    species: [...species, ...field(lines, "subspecies")],
    ancestry: field(lines, "ancestry"),
    locations: [...field(lines, "whereabouts"), ...locations],
    pronunciation: primaryNameMetadata?.pronunciation ||
      field(lines, "pronunciation")[0] || "",
    nameMetadata,
    aliases: field(lines, "aliases"),
    textAliases: core.extractTextAliases(body, nameInfo.text),
    body,
  };
}

function concept(catalog, subjectPath, form) {
  return catalog.concepts.find(
    (candidate) =>
      candidate.subjectPath === subjectPath &&
      candidate.preferredForm === form,
  );
}

function writeFixture(relative, text) {
  const absolute = path.join(vaultRoot, relative);
  fs.mkdirSync(path.dirname(absolute), { recursive: true });
  fs.writeFileSync(absolute, text, "utf8");
}

function run() {
  const notes = {
    "Gazetteer/Elaris.md": [
      "---", "tags: [place]", "name: Elaris", "typeOf: waterway", "---",
      "# Elaris", "", "%%^Metadata:names:v1%%",
      "- {name: Elaris, role: primary, language: Common, pronunciation: eh-LAR-iss, status: documented}",
      "- {name: Aelira, role: historical, language: Elvish, pronunciation: eye-LEE-rah, status: documented}",
      "%%^End%%",
    ].join("\n"),
    "Gazetteer/Test Sea.md": "---\ntags: [place, status/check/name]\ntypeOf: marine feature\n---\n# Test Sea\n",
    "People/Leto Bramble.md": "---\ntags: [person]\nspecies: halfling\naliases: [Leto]\n---\n# Leto Bramble\n",
    "People/Tarin II.md": "---\ntags: [person]\nspecies: human\ntitle: King\n---\n# Tarin II\n",
    "People/Varin the Elder.md": "---\ntags: [person]\nspecies: centaur\n---\n# Varin the Elder\n",
    "Groups/House of Example.md": "---\ntags: [group]\ntypeOf: family\n---\n# House of Example\n",
    "Objects/Test Token.md": "---\ntags: [object]\n---\n# Test Token\n",
    "No Tags.md": "# An unclassified fixture\n",
    "Worldbuilding/Ignored.md": "---\ntags: [person]\n---\n# Ignored\n",
    "_DM_/Ignored.md": "---\ntags: [person]\n---\n# Ignored\n",
    ".hidden/Ignored.md": "---\ntags: [person]\n---\n# Ignored\n",
  };
  for (const [relative, text] of Object.entries(notes)) writeFixture(relative, text);

  const fixtureDecisions = [
    { type: "rule", id: "fixture-halflings", label: "Fixture rule", match: { noteType: "person", species: "halfling", role: "*" }, language: "Common", priority: 50, enabled: true },
    { type: "concept", subject: "Gazetteer/Elaris.md", concept: "primary", language: "Dwarvish" },
    { type: "concept", subject: "People/Tarin II.md", concept: "primary", language: "Common" },
    // Existing but out-of-scope objects keep dormant decisions, not orphans.
    { type: "concept", subject: "Objects/Test Token.md", concept: "primary", language: "Common" },
  ];
  writeFixture("_Plugins/Name Explorer/Name Decisions.jsonl", core.serializeDecisionStore(fixtureDecisions));
  writeFixture("_Plugins/Name Explorer/Place Name Evidence.jsonl", [
    { record_type: "meta", schema_version: 1, place_count: 1 },
    { record_type: "place-name-evidence", schema_version: 1, subject: "Gazetteer/Elaris.md", subject_name: "Elaris", embeddedness: { band: "high" } },
  ].map((record) => JSON.stringify(record)).join("\n"));

  const subjects = markdownFiles(vaultRoot).map(buildSubject).filter(Boolean);
  const baseline = core.buildCatalog(subjects, []);
  const river = concept(baseline, "Gazetteer/Elaris.md", "Elaris");
  assert.equal(river.languageSource, "name-metadata");
  assert.equal(river.effectiveLanguage.language, "Common");
  assert.equal(river.pronunciation, "eh-LAR-iss");
  const historical = concept(baseline, "Gazetteer/Elaris.md", "Aelira");
  assert.equal(historical.effectiveLanguage.language, "Elvish");
  assert.equal(historical.pronunciation, "eye-LEE-rah");

  const decisions = core.parseDecisionStore(fs.readFileSync(path.join(vaultRoot, "_Plugins/Name Explorer/Name Decisions.jsonl"), "utf8"));
  const evidence = core.parsePlaceEvidenceStore(fs.readFileSync(path.join(vaultRoot, "_Plugins/Name Explorer/Place Name Evidence.jsonl"), "utf8"));
  function scanCatalog() {
    const current = markdownFiles(vaultRoot).map(buildSubject).filter(Boolean);
    return core.attachPlaceEvidence(core.buildCatalog(current, decisions), evidence);
  }
  const catalog = scanCatalog();
  assert.equal(subjects.length, 7);
  assert.equal(catalog.subjects.length, 6);
  assert.equal(catalog.concepts.length, 7);
  assert.ok(catalog.subjects.every((item) => core.NOTE_TYPES.includes(item.noteType)));
  assert.deepEqual(catalog.orphans, []);
  const overridden = concept(catalog, "Gazetteer/Elaris.md", "Elaris");
  assert.equal(overridden.languageSource, "decision");
  assert.equal(overridden.effectiveLanguage.language, "Dwarvish");
  assert.equal(overridden.placeEvidence.embeddedness.band, "high");
  assert.equal(concept(catalog, "Gazetteer/Elaris.md", "Aelira").placeEvidence.subject, "Gazetteer/Elaris.md");

  const sea = concept(catalog, "Gazetteer/Test Sea.md", "Test Sea");
  assert.equal(sea.subject.subtypeLabel, "marine feature");
  assert.equal(sea.subject.subtypeSource, "typeOf");
  assert.equal(sea.needsNameReview, true);
  assert.deepEqual(sea.nameReviewReasons, ["status/check/name"]);
  // Partial evidence is valid input; a current-vault count is not an invariant.
  assert.equal(sea.placeEvidence, null);
  const halfling = concept(catalog, "People/Leto Bramble.md", "Leto Bramble");
  assert.equal(halfling.inferredLanguage.language, "Halfling");
  assert.equal(halfling.effectiveLanguage.language, "Common");
  assert.equal(halfling.status, "rule");
  assert.ok(halfling.forms.some((form) => form.text === "Leto"));
  const king = concept(catalog, "People/Tarin II.md", "Tarin II");
  assert.equal(king.subject.subtypeLabel, "human");
  assert.equal(king.subject.subtypeSource, "species");
  assert.ok(king.components.some((part) => part.text === "King" && part.role === "title"));
  assert.equal(concept(catalog, "Groups/House of Example.md", "House of Example").subject.subtypeLabel, "family");
  const centaur = concept(catalog, "People/Varin the Elder.md", "Varin the Elder");
  assert.equal(centaur.languageSummary, "Centaur + Trade");
  assert.deepEqual(centaur.components.map((part) => [part.text, part.role]), [["Varin", "core"], ["the Elder", "epithet"]]);
  assert.ok(catalog.corpus.some((part) => part.subjectPath === centaur.subjectPath && part.text === "Varin"));
  assert.ok(!catalog.corpus.some((part) => part.subjectPath === centaur.subjectPath && part.text === "the Elder"));
  const exports = core.catalogExportRecords(catalog);
  assert.equal(exports.length, catalog.concepts.length);
  assert.doesNotThrow(() => JSON.stringify(exports));

  // Rename, delete, and rewrite fixture notes. Stale decisions are diagnostics;
  // the catalog must still build, with no assumptions about surviving notes.
  fs.renameSync(path.join(vaultRoot, "Gazetteer/Elaris.md"), path.join(vaultRoot, "Gazetteer/Renamed.md"));
  fs.unlinkSync(path.join(vaultRoot, "People/Tarin II.md"));
  writeFixture("People/Leto Bramble.md", "---\ntags: [person]\nname: New Name\nspecies: human\n---\n# New Name\n");
  const changed = scanCatalog();
  assert.deepEqual(changed.orphans.map((item) => item.record.subject).sort(), ["Gazetteer/Elaris.md", "People/Tarin II.md"]);
  assert.ok(changed.orphans.every((item) => item.reason === "Subject file is missing"));
  assert.equal(concept(changed, "Gazetteer/Renamed.md", "Elaris").placeEvidence, null);
  assert.equal(concept(changed, "Gazetteer/Renamed.md", "Elaris").effectiveLanguage.language, "Common");
  assert.ok(concept(changed, "People/Leto Bramble.md", "New Name"));
  assert.equal(concept(changed, "People/Leto Bramble.md", "Leto Bramble"), undefined);
  console.log("Name Explorer fixture-vault integration tests passed.");
}

try {
  run();
} finally {
  fs.rmSync(vaultRoot, { recursive: true, force: true });
}

"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const core = require("./core");

const vaultRoot = path.resolve(__dirname, "../../..");

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
  const name = field(lines, "name")[0] || path.basename(file.relative, ".md");
  const locations = [];
  for (const line of lines) {
    for (const match of line.matchAll(/\blocation:\s*([^,}\]]+)/g)) {
      locations.push(stripQuotes(match[1]));
    }
  }
  const heading = body.match(/^#\s+(.+)$/m)?.[1] || "";
  return {
    path: file.relative,
    linkTarget: file.relative.replace(/\.md$/i, ""),
    fileName: path.basename(file.relative, ".md"),
    name,
    noteType: core.chooseNoteType(tags),
    tags,
    title: field(lines, "title"),
    species: [...field(lines, "species"), ...field(lines, "subspecies")],
    ancestry: field(lines, "ancestry"),
    locations: [...field(lines, "whereabouts"), ...locations],
    pronunciation: field(lines, "pronunciation")[0] || "",
    aliases: field(lines, "aliases"),
    heading,
    textAliases: core.extractTextAliases(body, name),
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

function run() {
  const subjects = markdownFiles(vaultRoot)
    .map(buildSubject)
    .filter(Boolean);
  const decisionsPath = path.join(vaultRoot, "_MoC/Name Decisions.jsonl");
  const decisions = core.parseDecisionStore(
    fs.readFileSync(decisionsPath, "utf8"),
  );
  const catalog = core.buildCatalog(subjects, decisions);

  assert.ok(subjects.length > 2600, `Expected >2600 subjects, got ${subjects.length}`);
  assert.ok(catalog.concepts.length > subjects.length);
  assert.equal(catalog.orphans.length, 0);

  const derik = concept(
    catalog,
    "People/Historical Figures/Sembaran Royalty/Derik II.md",
    "Derik II",
  );
  assert.ok(derik);
  assert.equal(derik.forms.some((form) => form.text === "King Derik II"), true);
  assert.equal(derik.forms.find((form) => form.text === "King Derik II").variantKind, "titled");

  const garret = concept(
    catalog,
    "People/Halflings/Garret Tealeaf.md",
    "Garret Tealeaf",
  );
  assert.ok(garret);
  assert.equal(garret.inferredLanguage.language, "Halfling");
  assert.equal(garret.effectiveLanguage.language, "Common");
  assert.equal(garret.status, "rule");
  assert.equal(garret.forms.some((form) => form.text === "Garret"), true);

  const sentinelConcepts = catalog.concepts.filter(
    (candidate) => candidate.subjectPath === "Gazetteer/Sentinel Range.md",
  );
  assert.deepEqual(
    sentinelConcepts.map((candidate) => candidate.preferredForm).sort(),
    ["Beredri", "Indalas", "Labkhan", "Sentinel Range", "Tushara"].sort(),
  );

  const serraniaConcepts = catalog.concepts.filter(
    (candidate) =>
      candidate.subjectPath ===
      "Gazetteer/Western Green Sea/Cymea/Serrania River.md",
  );
  assert.equal(serraniaConcepts.length, 1);

  const exports = core.catalogExportRecords(catalog);
  assert.equal(exports.length, catalog.concepts.length);
  assert.doesNotThrow(() => JSON.stringify(exports[0]));

  const statusCounts = Object.fromEntries(
    [...new Set(catalog.concepts.map((item) => item.status))].map((status) => [
      status,
      catalog.concepts.filter((item) => item.status === status).length,
    ]),
  );
  console.log(JSON.stringify({
    subjects: subjects.length,
    concepts: catalog.concepts.length,
    forms: catalog.concepts.reduce((sum, item) => sum + item.forms.length, 0),
    rules: catalog.rules.length,
    orphans: catalog.orphans.length,
    statuses: statusCounts,
  }, null, 2));
  console.log("Name Explorer vault integration tests passed.");
}

run();

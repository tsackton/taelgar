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

function run() {
  const subjects = markdownFiles(vaultRoot)
    .map(buildSubject)
    .filter(Boolean);
  const decisionsPath = path.join(
    vaultRoot,
    "_Plugins/Name Explorer/Name Decisions.jsonl",
  );
  const decisions = core.parseDecisionStore(
    fs.readFileSync(decisionsPath, "utf8"),
  );
  const catalog = core.buildCatalog(subjects, decisions);
  const evidencePath = path.join(
    vaultRoot,
    "_Plugins/Name Explorer/Place Name Evidence.jsonl",
  );
  const placeEvidence = core.parsePlaceEvidenceStore(
    fs.readFileSync(evidencePath, "utf8"),
  );
  core.attachPlaceEvidence(catalog, placeEvidence);

  assert.ok(subjects.length > 2600, `Expected >2600 subjects, got ${subjects.length}`);
  assert.ok(catalog.subjects.length > 1000);
  assert.ok(catalog.subjects.length < subjects.length);
  assert.ok(
    catalog.subjects.every((item) => core.NOTE_TYPES.includes(item.noteType)),
  );
  assert.ok(catalog.concepts.length > catalog.subjects.length);
  assert.equal(catalog.orphans.length, 0);

  const istaros = concept(
    catalog,
    "Gazetteer/Major Rivers/Istaros Watershed/Istaros.md",
    "Istaros",
  );
  assert.ok(istaros);
  assert.equal(istaros.effectiveLanguage.language, "Common");
  assert.equal(istaros.languageSource, "name-metadata");
  assert.equal(istaros.pronunciation, "ISS-tah-rohs");
  const aistane = concept(
    catalog,
    "Gazetteer/Major Rivers/Istaros Watershed/Istaros.md",
    "Aistanë",
  );
  assert.ok(aistane);
  assert.equal(aistane.effectiveLanguage.language, "Elvish");
  assert.equal(aistane.pronunciation, "EYE-stah-neh");

  const placeSubjectCount = catalog.subjects.filter(
    (subject) =>
      subject.noteType === "place" && subject.path.startsWith("Gazetteer/"),
  ).length;
  assert.equal(placeEvidence.records.length, placeSubjectCount);
  assert.equal(placeEvidence.metadata.place_count, placeSubjectCount);

  const outerOcean = concept(
    catalog,
    "Gazetteer/Outer Ocean.md",
    "Outer Ocean",
  );
  assert.ok(outerOcean);
  assert.equal(outerOcean.needsNameReview, true);
  assert.equal(outerOcean.subject.subtypeLabel, "marine feature");
  assert.equal(outerOcean.subject.subtypeSource, "typeOf");
  assert.equal(
    outerOcean.nameReviewReasons.includes("status/check/name"),
    true,
  );

  const karawaDesert = concept(
    catalog,
    "Gazetteer/Greater Dunmar/Hara Basin/Karawa Desert.md",
    "Karawa Desert",
  );
  assert.ok(karawaDesert);
  assert.equal(karawaDesert.needsNameReview, true);
  assert.deepEqual(
    karawaDesert.nameReviewReasons,
    ["status/check/name"],
  );

  const houseOfSewick = concept(
    catalog,
    "Groups/Sembaran Noble Houses/House of Sewick.md",
    "House of Sewick",
  );
  assert.ok(houseOfSewick);
  assert.equal(houseOfSewick.subject.subtypeLabel, "family");
  assert.equal(houseOfSewick.subject.subtypeSource, "typeOf");

  const derik = concept(
    catalog,
    "People/Historical Figures/Sembaran Royalty/Derik II.md",
    "Derik II",
  );
  assert.ok(derik);
  assert.equal(derik.subject.subtypeLabel, "human");
  assert.equal(derik.subject.subtypeSource, "species");
  assert.equal(derik.forms.some((form) => form.text === "King Derik II"), false);
  assert.equal(
    derik.components.some((component) =>
      component.text === "King" && component.role === "title"
    ),
    true,
  );

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
  assert.deepEqual(
    serraniaConcepts[0].components.map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Serranía", "core"],
      ["River", "classifier"],
    ],
  );

  const kaelion = concept(
    catalog,
    "People/Other Nonhumans/Kaelion the Elder.md",
    "Kaelion the Elder",
  );
  assert.ok(kaelion);
  assert.equal(kaelion.languageSummary, "Centaur + Trade");
  assert.deepEqual(
    kaelion.components.map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Kaelion", "core"],
      ["the Elder", "epithet"],
    ],
  );
  assert.equal(
    catalog.corpus.some((component) =>
      component.subjectPath === kaelion.subjectPath &&
      component.text === "Kaelion"
    ),
    true,
  );
  assert.equal(
    catalog.corpus.some((component) =>
      component.subjectPath === kaelion.subjectPath &&
      component.text === "the Elder"
    ),
    false,
  );

  const valley = catalog.concepts.filter(
    (candidate) =>
      candidate.subjectPath ===
      "Gazetteer/Central Highlands/Valley of the Hidden Forest.md",
  );
  assert.equal(
    valley.find((candidate) =>
      candidate.preferredForm === "Naun Tarvanos"
    ).effectiveLanguage.language,
    "Elvish",
  );
  assert.equal(
    valley.find((candidate) =>
      candidate.preferredForm === "Valley of the Hidden Forest"
    ).effectiveLanguage.language,
    "Common",
  );
  assert.equal(
    valley.find((candidate) =>
      candidate.preferredForm === "Valley of the Hidden Forest"
    ).sourceForm,
    "Naun Tarvanos",
  );
  assert.ok(valley.every((candidate) => candidate.placeEvidence));
  assert.equal(
    valley[0].placeEvidence.subject,
    "Gazetteer/Central Highlands/Valley of the Hidden Forest.md",
  );

  const ragath = catalog.concepts.filter(
    (candidate) =>
      candidate.subjectPath === "Gazetteer/Greater Dunmar/Ragath Dor.md",
  );
  assert.equal(
    ragath.find((candidate) =>
      candidate.preferredForm === "High Door"
    ).effectiveLanguage.language,
    "Common",
  );
  assert.equal(
    ragath.find((candidate) =>
      candidate.preferredForm === "Highdoor Pass"
    ).effectiveLanguage.language,
    "Common",
  );
  assert.equal(
    ragath.find((candidate) =>
      candidate.preferredForm === "Ragath Dor"
    ).effectiveLanguage.language,
    "Dwarvish",
  );
  assert.equal(
    ragath.find((candidate) =>
      candidate.preferredForm === "High Door"
    ).derivation,
    "literal-translation",
  );

  const kulthul = concept(
    catalog,
    "Gazetteer/Major Rivers/Istaros Watershed/Kulthul.md",
    "Kulthul",
  );
  assert.ok(kulthul);
  assert.equal(kulthul.effectiveLanguage.language, "Orcish");
  assert.equal(kulthul.status, "text-evidence");

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
    scopedSubjects: catalog.subjects.length,
    concepts: catalog.concepts.length,
    components: catalog.components.length,
    corpus: catalog.corpus.length,
    forms: catalog.concepts.reduce((sum, item) => sum + item.forms.length, 0),
    nameReview: catalog.concepts.filter(
      (item) => item.needsNameReview,
    ).length,
    rules: catalog.rules.length,
    orphans: catalog.orphans.length,
    statuses: statusCounts,
  }, null, 2));
  console.log("Name Explorer vault integration tests passed.");
}

run();

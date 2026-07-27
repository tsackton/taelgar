"use strict";

const assert = require("node:assert/strict");
const core = require("./core");

function subject(overrides = {}) {
  return {
    path: "People/Test/Example.md",
    linkTarget: "People/Test/Example",
    fileName: "Example",
    name: "Example",
    noteType: "person",
    tags: ["person"],
    title: [],
    species: ["human"],
    ancestry: [],
    locations: [],
    pronunciation: "",
    aliases: [],
    heading: "",
    textAliases: [],
    body: "",
    ...overrides,
  };
}

function run() {
  assert.deepEqual(
    core.classifyVariant("King Derik II", "Derik II", { title: ["King"] }),
    { kind: "titled", score: 95 },
  );
  assert.equal(
    core.classifyVariant("Garret", "Garret Tealeaf", {}).kind,
    "short",
  );
  assert.equal(
    core.classifyVariant("Serranía", "Serranía River", {}).kind,
    "descriptor",
  );
  assert.equal(
    core.classifyVariant("River Chasa", "Chasa River", {}).kind,
    "descriptor",
  );
  assert.equal(
    core.classifyVariant("Szoltár", "Szoltar", {}).kind,
    "orthographic",
  );
  assert.equal(
    core.classifyVariant("The Stoneworker", "Stoneworker", {}).kind,
    "article",
  );

  const derik = subject({
    path: "People/Historical Figures/Sembaran Royalty/Derik II.md",
    name: "Derik II",
    ancestry: ["Sembaran"],
    title: ["King"],
    heading: "King Derik II",
  });
  const derikConcepts = core.buildConcepts(derik);
  assert.equal(derikConcepts.length, 1);
  assert.equal(derikConcepts[0].forms.length, 2);
  assert.equal(derikConcepts[0].forms[1].variantKind, "titled");

  const garret = subject({
    path: "People/Halflings/Garret Tealeaf.md",
    name: "Garret Tealeaf",
    species: ["halfling"],
    aliases: ["Garret"],
  });
  const garretConcepts = core.buildConcepts(garret);
  assert.equal(garretConcepts.length, 1);
  assert.equal(garretConcepts[0].forms[1].variantKind, "short");

  const sentinel = subject({
    path: "Gazetteer/Sentinel Range.md",
    name: "Sentinel Range",
    noteType: "place",
    tags: ["place"],
    aliases: [
      "Sentinels",
      "Sentinel Mountains",
      "Indalas",
      "Labkhan",
      "Beredri",
      "Tushara",
    ],
  });
  const sentinelConcepts = core.buildConcepts(sentinel);
  assert.equal(sentinelConcepts.length, 5);
  assert.deepEqual(
    sentinelConcepts[0].forms.map((form) => form.text),
    ["Sentinel Range", "Sentinels", "Sentinel Mountains"],
  );

  const serrania = subject({
    path: "Gazetteer/Western Green Sea/Cymea/Serrania River.md",
    name: "Serranía River",
    noteType: "place",
    tags: ["place"],
    aliases: ["Serranía River", "Serrania", "Serranía"],
  });
  const serraniaConcepts = core.buildConcepts(serrania);
  assert.equal(serraniaConcepts.length, 1);
  assert.deepEqual(
    new Set(serraniaConcepts[0].forms[0].sources),
    new Set(["primary", "frontmatter"]),
  );

  const rules = [
    {
      type: "rule",
      id: "halfling-person-names-common",
      label: "Halfling personal names default to Common",
      match: { noteType: "person", species: "halfling", role: "*" },
      language: "Common",
      priority: 50,
      enabled: true,
    },
  ];
  const halflingCatalog = core.buildCatalog([garret], rules);
  assert.equal(
    halflingCatalog.concepts[0].inferredLanguage.language,
    "Halfling",
  );
  assert.equal(
    halflingCatalog.concepts[0].effectiveLanguage.language,
    "Common",
  );
  assert.equal(halflingCatalog.concepts[0].status, "rule");

  const conceptDecision = {
    type: "concept",
    subject: garret.path,
    concept: "primary",
    form: "Garret Tealeaf",
    language: "Halfling",
    relationship: "exonym",
    derivation: "translation",
    usage: "historical",
  };
  const decidedCatalog = core.buildCatalog([garret], [
    ...rules,
    conceptDecision,
  ]);
  const decided = decidedCatalog.concepts[0];
  assert.equal(decided.effectiveLanguage.language, "Halfling");
  assert.equal(decided.status, "confirmed");
  assert.equal(decided.kindLabel, "Historical translated exonym");

  const formDecision = {
    type: "form",
    subject: garret.path,
    form: "Garret",
    action: "separate",
  };
  const separatedCatalog = core.buildCatalog([garret], [
    ...rules,
    formDecision,
  ]);
  assert.equal(separatedCatalog.concepts.length, 2);

  const serialized = core.serializeDecisionStore([
    conceptDecision,
    rules[0],
    formDecision,
  ]);
  const parsed = core.parseDecisionStore(serialized);
  assert.equal(parsed.length, 3);
  assert.equal(parsed[0].type, "rule");
  assert.equal(parsed[1].type, "concept");
  assert.equal(parsed[2].type, "form");

  assert.throws(
    () => core.parseDecisionStore('{"type":"rule"}\nnot json\n'),
    /line 2/,
  );

  console.log("Name Explorer core tests passed.");
}

run();

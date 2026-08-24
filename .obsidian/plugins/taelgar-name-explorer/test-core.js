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
    nameMetadata: [],
    aliases: [],
    heading: "",
    textAliases: [],
    body: "",
    ...overrides,
  };
}

function run() {
  assert.deepEqual(
    core.NOTE_TYPES,
    ["ancestry", "place", "group", "power", "person"],
  );

  const parsedNameMetadata = core.parseNameMetadata([
    "# Example",
    "",
    "%%^Metadata:names:v1%%",
    "- {name: Aistanë, role: historical, language: Elvish, pronunciation: EYE-stah-neh, meaning: blessed water, status: documented}",
    "- {name: Istaros, role: primary, language: Common, derivedFrom: Aistanë, notes: \"Likely corruption, retained in Common.\", status: inferred}",
    "- {name: 'Istaros'' Root', role: name component, language: unknown}",
    "- {name: Hero's Feast, role: name component, language: Common, notes: the hero's translated title, status: documented}",
    "%%^End%%",
  ].join("\n"));
  assert.equal(parsedNameMetadata.length, 4);
  assert.deepEqual(parsedNameMetadata[1], {
    name: "Istaros",
    role: "primary",
    language: "Common",
    derivedFrom: "Aistanë",
    notes: "Likely corruption, retained in Common.",
    status: "inferred",
    source: "name-metadata",
  });
  assert.equal(parsedNameMetadata[2].name, "Istaros' Root");
  assert.equal(parsedNameMetadata[2].language, "Unknown");
  assert.equal(parsedNameMetadata[3].name, "Hero's Feast");
  assert.equal(parsedNameMetadata[3].notes, "the hero's translated title");
  assert.equal(
    core.primaryNameMetadataEntry(parsedNameMetadata).name,
    "Istaros",
  );

  const metadataSubject = subject({
    path: "Gazetteer/Major Rivers/Istaros Watershed/Istaros.md",
    rawName: "Istaros",
    name: "Istaros",
    noteType: "place",
    tags: ["place"],
    species: [],
    nameMetadata: parsedNameMetadata,
  });
  const metadataCatalog = core.buildCatalog([metadataSubject], []);
  assert.deepEqual(
    metadataCatalog.concepts.map((item) => item.preferredForm).sort(),
    ["Aistanë", "Istaros"].sort(),
  );
  const metadataPrimary = metadataCatalog.concepts.find(
    (item) => item.preferredForm === "Istaros",
  );
  const metadataHistorical = metadataCatalog.concepts.find(
    (item) => item.preferredForm === "Aistanë",
  );
  assert.equal(metadataPrimary.effectiveLanguage.language, "Common");
  assert.equal(metadataPrimary.languageSource, "name-metadata");
  assert.equal(metadataPrimary.status, "metadata-inferred");
  assert.equal(metadataHistorical.effectiveLanguage.language, "Elvish");
  assert.equal(metadataHistorical.status, "metadata-documented");
  assert.equal(metadataHistorical.pronunciation, "EYE-stah-neh");
  assert.equal(
    metadataCatalog.concepts.some((item) =>
      item.preferredForm === "Istaros' Root"
    ),
    false,
  );
  const metadataExport = core.catalogExportRecords(metadataCatalog).find(
    (item) => item.preferred_form === "Aistanë",
  );
  assert.equal(metadataExport.pronunciation, "EYE-stah-neh");
  assert.equal(metadataExport.name_metadata.meaning, "blessed water");

  const metadataOverride = core.buildCatalog([metadataSubject], [{
    type: "concept",
    subject: metadataSubject.path,
    concept: "primary",
    language: "Drankorian",
  }]).concepts.find((item) => item.preferredForm === "Istaros");
  assert.equal(metadataOverride.effectiveLanguage.language, "Drankorian");
  assert.equal(metadataOverride.languageSource, "decision");
  assert.equal(metadataOverride.status, "overridden");
  assert.deepEqual(
    core.subtypeForSubject("person", {
      species: ["elf"],
      subTypeOf: ["high elf"],
      typeOf: ["ruler"],
    }),
    {
      values: ["elf"],
      label: "elf",
      source: "species",
    },
  );
  assert.deepEqual(
    core.subtypeForSubject("place", {
      subTypeOf: ["ruined"],
      typeOf: ["settlement"],
    }),
    {
      values: ["settlement"],
      label: "settlement",
      source: "typeOf",
    },
  );
  assert.deepEqual(
    core.subtypeForSubject("place", {
      typeOf: ["marine feature"],
    }),
    {
      values: ["marine feature"],
      label: "marine feature",
      source: "typeOf",
    },
  );
  assert.deepEqual(
    core.subtypeChoices([
      { noteType: "person", subtypes: ["human", "elf"] },
      { noteType: "person", subtypes: ["Human"] },
      { noteType: "place", subtypes: ["settlement", "realm"] },
    ], "person"),
    ["elf", "human"],
  );
  assert.deepEqual(
    core.subtypeChoices([
      { noteType: "person", subtypes: ["human"] },
      { noteType: "place", subtypes: ["settlement"] },
    ]),
    ["human", "settlement"],
  );

  const taggedForNameReview = subject({
    tags: ["person", "status/check/name"],
  });
  const taggedCatalog = core.buildCatalog([taggedForNameReview], []);
  assert.equal(taggedCatalog.concepts[0].needsNameReview, true);
  assert.deepEqual(
    taggedCatalog.concepts[0].nameReviewReasons,
    ["status/check/name"],
  );

  const provisional = subject({
    path: "Gazetteer/~Unnamed River~.md",
    fileName: "~Unnamed River~",
    rawName: "~Unnamed River~",
    name: "Unnamed River",
    provisionalName: true,
    noteType: "place",
    tags: ["place"],
  });
  const provisionalCatalog = core.buildCatalog([provisional], []);
  assert.equal(
    provisionalCatalog.concepts[0].preferredForm,
    "Unnamed River",
  );
  assert.equal(provisionalCatalog.concepts[0].subjectName, "Unnamed River");
  assert.equal(provisionalCatalog.concepts[0].needsNameReview, true);
  assert.deepEqual(
    provisionalCatalog.concepts[0].nameReviewReasons,
    ["provisional-name-marker"],
  );
  assert.equal(
    provisionalCatalog.components.every(
      (component) => component.needsNameReview,
    ),
    true,
  );
  assert.deepEqual(
    core.catalogExportRecords(provisionalCatalog)[0].name_review,
    {
      needed: true,
      reasons: ["provisional-name-marker"],
    },
  );

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
  assert.equal(derikConcepts[0].forms.length, 1);
  const derikCatalog = core.buildCatalog([derik], []);
  assert.equal(derikCatalog.concepts[0].subject.subtypeLabel, "human");
  assert.equal(derikCatalog.concepts[0].subject.subtypeSource, "species");
  assert.deepEqual(
    core.catalogExportRecords(derikCatalog)[0].subtypes,
    ["human"],
  );
  assert.deepEqual(
    derikCatalog.concepts[0].components.map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Derik", "core"],
      ["II", "ordinal"],
      ["King", "title"],
    ],
  );
  assert.deepEqual(
    derikCatalog.corpus.map((component) => component.text),
    ["Derik"],
  );
  assert.equal(
    derikCatalog.components.find(
      (component) => component.text === "King",
    ).effectiveLanguage.family,
    "Trade",
  );

  const proseAlias = subject({
    name: "Example",
    heading: "Lord Example",
    textAliases: [{
      text: "The Wanderer",
      source: "text",
      evidence: 'Example is known as "The Wanderer".',
    }],
  });
  assert.deepEqual(
    core.mergeObservedForms(proseAlias).map((form) => form.text),
    ["Example", "The Wanderer"],
  );
  assert.equal(
    core.mergeObservedForms(proseAlias).some((form) =>
      form.text === "Lord Example"
    ),
    false,
  );

  const hulda = subject({
    name: "Lord Hulda",
  });
  assert.deepEqual(
    core.decomposeDisplayName(hulda.name, hulda).map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Lord", "title"],
      ["Hulda", "core"],
    ],
  );

  const samraat = subject({
    name: "Vishi",
    title: ["Samraat"],
    ancestry: ["Drankorian"],
  });
  assert.equal(
    core.buildCatalog([samraat], []).components.find(
      (component) => component.text === "Samraat",
    ).effectiveLanguage.language,
    "Drankorian",
  );

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

  const nobleHouse = subject({
    name: "House of Example",
    noteType: "group",
    tags: ["group"],
    species: [],
    subTypeOf: ["noble house"],
    typeOf: ["family"],
  });
  const nobleHouseCatalog = core.buildCatalog([nobleHouse], []);
  assert.equal(
    nobleHouseCatalog.concepts[0].subject.subtypeLabel,
    "family",
  );
  assert.equal(
    nobleHouseCatalog.components[0].subtypeLabel,
    "family",
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

  const kaelion = subject({
    path: "People/Other Nonhumans/Kaelion the Elder.md",
    name: "Kaelion the Elder",
    species: ["centaur"],
  });
  assert.deepEqual(
    core.decomposeDisplayName(kaelion.name, kaelion).map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Kaelion", "core"],
      ["the Elder", "epithet"],
    ],
  );
  const kaelionCatalog = core.buildCatalog([kaelion], []);
  assert.equal(kaelionCatalog.concepts[0].languageSummary, "Centaur + Trade");
  assert.deepEqual(
    kaelionCatalog.corpus.map((component) => component.text),
    ["Kaelion"],
  );
  assert.equal(
    kaelionCatalog.components.find(
      (component) => component.text === "the Elder",
    ).effectiveLanguage.family,
    "Trade",
  );

  const arryn = subject({
    name: "Arryn of Tollen",
    ancestry: ["Tollender"],
  });
  assert.deepEqual(
    core.decomposeDisplayName(arryn.name, arryn).map((component) => [
      component.text,
      component.role,
    ]),
    [
      ["Arryn", "core"],
      ["of Tollen", "locative"],
    ],
  );

  const wildRiver = subject({
    path: "Gazetteer/Wild River.md",
    name: "Wild River",
    noteType: "place",
    tags: ["place"],
  });
  const wildCatalog = core.buildCatalog([wildRiver], []);
  assert.equal(
    wildCatalog.concepts[0].effectiveLanguage.language,
    "Trade (unspecified)",
  );
  assert.equal(wildCatalog.concepts[0].status, "convention");
  assert.equal(
    wildCatalog.concepts[0].derivation,
    "unattested-translation",
  );
  assert.equal(wildCatalog.concepts[0].sourceForm, "unattested");
  assert.equal(wildCatalog.corpus.length, 0);

  assert.deepEqual(
    core.decomposeDisplayName("The Wild River", wildRiver).map(
      (component) => [component.text, component.role],
    ),
    [["Wild River", "descriptive"]],
  );

  const serraniaParts = core.decomposeDisplayName("Serranía River", {
    ...wildRiver,
    name: "Serranía River",
  });
  assert.deepEqual(
    serraniaParts.map((component) => [component.text, component.role]),
    [
      ["Serranía", "core"],
      ["River", "classifier"],
    ],
  );

  const valleyLine =
    "The Valley of the Hidden Forest, called *Naun Tarvanos* in Elvish, " +
    "was visited by the Dunmar Fellowship.";
  assert.equal(
    core.explicitLanguageForName(
      valleyLine,
      "Naun Tarvanos",
      "test",
    ).language,
    "Elvish",
  );
  assert.equal(
    core.explicitLanguageForName(
      valleyLine,
      "Valley of the Hidden Forest",
      "test",
    ),
    null,
  );

  const ragathLine =
    "Ragath Dor, often called High Door or the Highdoor Pass in the " +
    "Common tongue, is the principal route.";
  assert.equal(
    core.explicitLanguageForName(ragathLine, "High Door", "test").language,
    "Common",
  );
  assert.equal(
    core.explicitLanguageForName(
      ragathLine,
      "Highdoor Pass",
      "test",
    ).language,
    "Common",
  );
  assert.equal(
    core.explicitLanguageForName(ragathLine, "Ragath Dor", "test"),
    null,
  );

  const kulthulLine =
    "%% note: the Kulthul is the orcish name for this river; it likely " +
    "also has a Dunmari name, and possibly more %%";
  assert.equal(
    core.explicitLanguageForName(kulthulLine, "Kulthul", "test").language,
    "Orcish",
  );

  const componentDecisionTarget = kaelionCatalog.components.find(
    (component) => component.text === "the Elder",
  );
  const componentDecision = {
    type: "component",
    subject: kaelion.path,
    concept: "primary",
    component: componentDecisionTarget.id,
    form: "the Elder",
    language: "Common",
    corpus: "exclude",
  };
  const componentDecidedCatalog = core.buildCatalog(
    [kaelion],
    [componentDecision],
  );
  const decidedEpithet = componentDecidedCatalog.components.find(
    (component) => component.text === "the Elder",
  );
  assert.equal(decidedEpithet.effectiveLanguage.language, "Common");
  assert.equal(decidedEpithet.languageSource, "decision");
  assert.equal(decidedEpithet.corpusEligible, false);

  const serialized = core.serializeDecisionStore([
    conceptDecision,
    componentDecision,
    rules[0],
    formDecision,
  ]);
  const parsed = core.parseDecisionStore(serialized);
  assert.equal(parsed.length, 4);
  assert.equal(parsed[0].type, "rule");
  assert.equal(parsed[1].type, "concept");
  assert.equal(parsed[2].type, "component");
  assert.equal(parsed[3].type, "form");

  assert.throws(
    () => core.parseDecisionStore('{"type":"rule"}\nnot json\n'),
    /line 2/,
  );

  const evidenceText = [
    JSON.stringify({
      record_type: "meta",
      schema_version: 1,
      place_count: 1,
    }),
    JSON.stringify({
      record_type: "place-name-evidence",
      schema_version: 1,
      subject: wildRiver.path,
      subject_name: wildRiver.name,
      embeddedness: { band: "high", inbound: { unique_notes: 8 } },
      campaigns: [],
      naming: { documentation_depth: "documented", review_state: "needs-review" },
    }),
  ].join("\n");
  const evidenceStore = core.parsePlaceEvidenceStore(evidenceText);
  assert.equal(evidenceStore.metadata.place_count, 1);
  assert.equal(evidenceStore.records.length, 1);
  core.attachPlaceEvidence(wildCatalog, evidenceStore);
  assert.equal(wildCatalog.concepts[0].placeEvidence.embeddedness.band, "high");
  assert.equal(wildCatalog.subjects[0].placeEvidence.naming.review_state, "needs-review");
  assert.throws(
    () => core.parsePlaceEvidenceStore('{"record_type":"wrong"}\n'),
    /line 1/,
  );

  console.log("Name Explorer core tests passed.");
}

run();

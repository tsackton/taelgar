"use strict";

const NOTE_TYPES = [
  "ancestry",
  "place",
  "group",
  "power",
  "person",
];

const COMPONENT_ROLES = [
  "core",
  "descriptive",
  "title",
  "epithet",
  "locative",
  "dynastic",
  "classifier",
  "ordinal",
];

const CORPUS_COMPONENT_ROLES = new Set([
  "core",
  "descriptive",
]);

const LANGUAGE_DEFINITIONS = [
  ["Drankorian", "Chardonian"],
  ["Drankorian", "Cymean"],
  ["Drankorian", "Drankorian"],
  ["Drankorian", "Illorian"],
  ["Drankorian", "Isinguese"],
  ["Eastros", "Sembaran"],
  ["Eastros", "Skaegish"],
  ["Eastros", "Tollish"],
  ["Eastros", "Urskan"],
  ["Eastros", "Zimkovan"],
  ["Exotic", "Centaur"],
  ["Exotic", "Giant"],
  ["Exotic", "Gnoll"],
  ["Exotic", "Kenku"],
  ["Exotic", "Merfolk"],
  ["Extraplanar", "Primordial"],
  ["Extraplanar", "Sylvan"],
  ["Goblin", "Goblin/Katonylev"],
  ["Goblin", "Katonylev"],
  ["Hkaran", "Hkaran"],
  ["Independent human", "Dunmari"],
  ["Independent human", "Tyrwinghan"],
  ["Mixed/uncertain human", "Vosic"],
  ["Non-human", "Dwarvish"],
  ["Non-human", "Elvish"],
  ["Non-human", "Free Orcish"],
  ["Non-human", "Halfling"],
  ["Non-human", "Lizardling"],
  ["Non-human", "Orcish"],
  ["Non-human", "Stoneborn"],
  ["Northros", "Deno'qai"],
  ["Northros", "Mawaran"],
  ["Northros", "Old Zimkovan"],
  ["Northros", "Unclassified Northros"],
  ["Northros", "Vargaldi"],
  ["Trade", "Common"],
  ["Trade", "Trade (unspecified)"],
  ["Unclassified", "Svolhasian"],
  ["Special", "Language-neutral"],
  ["Special", "Mixed"],
  ["Unknown", "Unknown"],
];

const LANGUAGE_FAMILY = new Map(
  LANGUAGE_DEFINITIONS.map(([family, language]) => [language, family]),
);

const LANGUAGE_KEYWORDS = [
  [["katonylev", "army tongue"], "Goblin", "Katonylev"],
  [["hobgoblin", "goblin"], "Goblin", "Goblin/Katonylev"],
  [["svolhasian", "svolhas"], "Unclassified", "Svolhasian"],
  [["drankorian", "drankor"], "Drankorian", "Drankorian"],
  [["chardonian", "chardon"], "Drankorian", "Chardonian"],
  [["cymean", "cymea"], "Drankorian", "Cymean"],
  [["isinguese", "isinguer", "isingue"], "Drankorian", "Isinguese"],
  [["illorian", "illoria"], "Drankorian", "Illorian"],
  [["deno'qai", "deno’qai"], "Northros", "Deno'qai"],
  [["mawaran", "mawar"], "Northros", "Mawaran"],
  [["vargaldi"], "Northros", "Vargaldi"],
  [["old zimkovan"], "Northros", "Old Zimkovan"],
  [["northros"], "Northros", "Unclassified Northros"],
  [["skaegish", "skaer"], "Eastros", "Skaegish"],
  [["urksan", "urskan", "ursk"], "Eastros", "Urskan"],
  [["zimkovan", "zimka"], "Eastros", "Zimkovan"],
  [["semb aran", "sembaran", "sembara"], "Eastros", "Sembaran"],
  [["tollish", "tollender", "tollen"], "Eastros", "Tollish"],
  [["dunmari", "dunmar"], "Independent human", "Dunmari"],
  [["tyrwinghan", "tyrwingha"], "Independent human", "Tyrwinghan"],
  [["vosic", "vostok", "vos "], "Mixed/uncertain human", "Vosic"],
  [["hkaran", "hkar"], "Hkaran", "Hkaran"],
  [["dwarvish", "dwarven", "dwarf"], "Non-human", "Dwarvish"],
  [["elvish", "elven", "elf"], "Non-human", "Elvish"],
  [["lizardling", "lizardfolk"], "Non-human", "Lizardling"],
  [["free orcish", "free orc"], "Non-human", "Free Orcish"],
  [["orcish", "orc "], "Non-human", "Orcish"],
  [["stoneborn"], "Non-human", "Stoneborn"],
  [["halfling"], "Non-human", "Halfling"],
  [["giant"], "Exotic", "Giant"],
  [["kenku"], "Exotic", "Kenku"],
  [["merfolk"], "Exotic", "Merfolk"],
  [["centaur"], "Exotic", "Centaur"],
  [["gnoll"], "Exotic", "Gnoll"],
  [["sylvan", "fey "], "Extraplanar", "Sylvan"],
  [["primordial", "elemental"], "Extraplanar", "Primordial"],
  [["common"], "Trade", "Common"],
];

// Text evidence deliberately uses language adjectives and language names only.
// Cultural and geographic roots such as "Dunmar", "Tollen", or "Drankor"
// remain useful heuristic evidence, but cannot create a text-evidence result.
const EXPLICIT_LANGUAGE_TERMS = [
  [["army tongue", "katonylev"], "Goblin", "Katonylev"],
  [["hobgoblin", "goblin"], "Goblin", "Goblin/Katonylev"],
  [["svolhasian"], "Unclassified", "Svolhasian"],
  [["drankorian"], "Drankorian", "Drankorian"],
  [["chardonian"], "Drankorian", "Chardonian"],
  [["cymean"], "Drankorian", "Cymean"],
  [["isinguese"], "Drankorian", "Isinguese"],
  [["illorian"], "Drankorian", "Illorian"],
  [["deno'qai", "deno’qai"], "Northros", "Deno'qai"],
  [["mawaran"], "Northros", "Mawaran"],
  [["vargaldi"], "Northros", "Vargaldi"],
  [["old zimkovan"], "Northros", "Old Zimkovan"],
  [["skaegish"], "Eastros", "Skaegish"],
  [["urksan", "urskan"], "Eastros", "Urskan"],
  [["zimkovan"], "Eastros", "Zimkovan"],
  [["sembaran"], "Eastros", "Sembaran"],
  [["tollish"], "Eastros", "Tollish"],
  [["dunmari"], "Independent human", "Dunmari"],
  [["tyrwinghan"], "Independent human", "Tyrwinghan"],
  [["vosic"], "Mixed/uncertain human", "Vosic"],
  [["hkaran"], "Hkaran", "Hkaran"],
  [["dwarvish", "dwarven"], "Non-human", "Dwarvish"],
  [["elvish", "elven"], "Non-human", "Elvish"],
  [["lizardling", "lizardfolk"], "Non-human", "Lizardling"],
  [["free orcish"], "Non-human", "Free Orcish"],
  [["orcish"], "Non-human", "Orcish"],
  [["stoneborn"], "Non-human", "Stoneborn"],
  [["halfling"], "Non-human", "Halfling"],
  [["giant"], "Exotic", "Giant"],
  [["kenku"], "Exotic", "Kenku"],
  [["merfolk"], "Exotic", "Merfolk"],
  [["centaur"], "Exotic", "Centaur"],
  [["gnoll"], "Exotic", "Gnoll"],
  [["sylvan"], "Extraplanar", "Sylvan"],
  [["primordial"], "Extraplanar", "Primordial"],
  [["common"], "Trade", "Common"],
];

const ANCESTRY_LANGUAGE_RULES = [
  [["deno'qai", "deno’qai"], "Northros", "Deno'qai"],
  [["mawaran"], "Northros", "Mawaran"],
  [["vargaldi"], "Northros", "Vargaldi"],
  [["zimka", "zimkovan"], "Eastros", "Zimkovan"],
  [["semb aran", "sembaran", "addermarian"], "Eastros", "Sembaran"],
  [["tollish", "tollender", "tollen"], "Eastros", "Tollish"],
  [["skaer"], "Eastros", "Skaegish"],
  [["urskan", "urksan"], "Eastros", "Urskan"],
  [["chardonian", "apporian"], "Drankorian", "Chardonian"],
  [["drankorian"], "Drankorian", "Drankorian"],
  [["cymean"], "Drankorian", "Cymean"],
  [["isinguer", "isinguese", "aurbeze", "mazeanne", "maseaun"], "Drankorian", "Isinguese"],
  [["illorian"], "Drankorian", "Illorian"],
  [["dunmari"], "Independent human", "Dunmari"],
  [["tyrwinghan"], "Independent human", "Tyrwinghan"],
  [["vos", "vosic"], "Mixed/uncertain human", "Vosic"],
  [["hkaran"], "Hkaran", "Hkaran"],
  [["dwarven", "dwarf"], "Non-human", "Dwarvish"],
  [["elven", "elf"], "Non-human", "Elvish"],
  [["lizardfolk"], "Non-human", "Lizardling"],
  [["free orc"], "Non-human", "Free Orcish"],
  [["orcish", "orc"], "Non-human", "Orcish"],
  [["hobgoblin", "goblin"], "Goblin", "Goblin/Katonylev"],
  [["stoneborn"], "Non-human", "Stoneborn"],
  [["halfling"], "Non-human", "Halfling"],
  [["frost giant", "giant"], "Exotic", "Giant"],
  [["kenku"], "Exotic", "Kenku"],
  [["merfolk"], "Exotic", "Merfolk"],
  [["centaur"], "Exotic", "Centaur"],
  [["fey"], "Extraplanar", "Sylvan"],
];

const PATH_LANGUAGE_RULES = [
  ["People/Deno'qai/", "Northros", "Deno'qai"],
  ["People/Mawarans/", "Northros", "Mawaran"],
  ["People/Sembarans/", "Eastros", "Sembaran"],
  ["People/Addermarians/", "Eastros", "Sembaran"],
  ["People/Maseauns/", "Drankorian", "Isinguese"],
  ["People/Chardonians/", "Drankorian", "Chardonian"],
  ["People/Dunmari/", "Independent human", "Dunmari"],
  ["People/Dwarves/", "Non-human", "Dwarvish"],
  ["People/Elves/", "Non-human", "Elvish"],
  ["People/Giants/", "Exotic", "Giant"],
  ["People/Halflings/", "Non-human", "Halfling"],
  ["People/Kenku/", "Exotic", "Kenku"],
  ["People/Lizardfolk/", "Non-human", "Lizardling"],
  ["People/Orcs/", "Non-human", "Orcish"],
  ["People/Skaer/", "Eastros", "Skaegish"],
  ["People/Tollenders/", "Eastros", "Tollish"],
  ["People/Tyrwinghans/", "Independent human", "Tyrwinghan"],
  ["Groups/Dwarven ", "Non-human", "Dwarvish"],
  ["Groups/Dwarven/", "Non-human", "Dwarvish"],
  ["Groups/Hobgoblin Clans/", "Goblin", "Goblin/Katonylev"],
  ["Groups/Orc Hordes/", "Non-human", "Orcish"],
  ["Groups/Sembaran ", "Eastros", "Sembaran"],
  ["Groups/Tollen ", "Eastros", "Tollish"],
  ["Groups/Urskan ", "Eastros", "Urskan"],
  ["Gazetteer/Drankorian Hinterland/", "Drankorian", "Drankorian"],
  ["Gazetteer/Greater Chardon/Chardonian Empire/", "Drankorian", "Chardonian"],
  ["Gazetteer/Greater Chardon/", "Drankorian", "Chardonian"],
  ["Gazetteer/Upper Istaros/", "Drankorian", "Isinguese"],
  ["Gazetteer/Western Green Sea/Cymea/", "Drankorian", "Cymean"],
  ["Gazetteer/Greater Sembara/Tyrwingha/", "Independent human", "Tyrwinghan"],
  ["Gazetteer/Greater Sembara/Vostok/", "Mixed/uncertain human", "Vosic"],
  ["Gazetteer/Greater Sembara/", "Eastros", "Sembaran"],
  ["Gazetteer/Greater Dunmar/", "Independent human", "Dunmari"],
  ["Gazetteer/Northwest Coast/Mawar", "Northros", "Mawaran"],
  ["Gazetteer/Northwest Coast/Northern Provinces/", "Drankorian", "Chardonian"],
  ["Gazetteer/Northern Green Sea/Ursk", "Eastros", "Urskan"],
  ["Gazetteer/Northern Green Sea/Skaer", "Eastros", "Skaegish"],
  ["Gazetteer/Central Highlands/Dwarven", "Non-human", "Dwarvish"],
  ["Gazetteer/Extraplanar/Feywild/", "Extraplanar", "Sylvan"],
];

const LOCATION_LANGUAGE_RULES = [
  [["elderwood", "forest of dreams"], "Northros", "Deno'qai"],
  [["mawakel", "mawar"], "Northros", "Mawaran"],
  [["sembara", "addermarch"], "Eastros", "Sembaran"],
  [["tollen"], "Eastros", "Tollish"],
  [["skaerhem"], "Eastros", "Skaegish"],
  [["ursk"], "Eastros", "Urskan"],
  [["chardon", "chardonian empire"], "Drankorian", "Chardonian"],
  [["cymea"], "Drankorian", "Cymean"],
  [["isingue", "aurbez", "maseau"], "Drankorian", "Isinguese"],
  [["dunmar"], "Independent human", "Dunmari"],
  [["tyrwingha"], "Independent human", "Tyrwinghan"],
  [["vostok"], "Mixed/uncertain human", "Vosic"],
  [["feywild"], "Extraplanar", "Sylvan"],
];

const COMMON_DESCRIPTOR_WORDS = new Set([
  "abbey", "alliance", "army", "archipelago", "archive", "barony", "battle",
  "bay", "bridge", "canal", "castle", "cavern", "city", "clan", "cliffs",
  "coast", "company", "confederacy", "county", "crossing", "desert", "duchy",
  "empire", "falls", "fellowship", "fens", "forest", "fort", "fortress",
  "freehold", "gap", "garden", "gate", "gorge", "guild", "gulf", "hall",
  "harbor", "haven", "heights", "highlands", "hill", "hills", "hold", "house",
  "inn", "island", "islands", "isle", "isles", "kingdom", "lake", "lands",
  "library", "manor", "march", "marsh", "mine", "monastery", "mount",
  "mountain", "mountains", "ocean", "order", "palace", "pass", "peak",
  "plains", "plateau", "port", "province", "range", "realm", "republic",
  "river", "road", "sea", "settlement", "siege", "society", "spring",
  "stones", "strait", "swamp", "temple", "tower", "trail", "university",
  "vale", "valley", "village", "war", "waters", "watershed", "wood", "woods",
]);

const COMMON_COMPOUND_PARTS = [
  "ash", "black", "bright", "brook", "clear", "cloud", "cold", "dark", "deep",
  "dragon", "dream", "east", "ever", "fall", "field", "fire", "ford", "forest",
  "frost", "gold", "green", "grey", "high", "hill", "iron", "lake", "light",
  "long", "marsh", "mist", "moon", "north", "oak", "red", "river", "rock",
  "sea", "shadow", "silver", "south", "star", "stone", "storm", "sun", "thorn",
  "vale", "water", "west", "white", "wild", "wind", "winter", "wood",
];

// This is intentionally a naming lexicon, not an English dictionary. A phrase
// is a Trade rendering only when all of its lexical tokens are transparent.
// Unknown tokens are retained as possible in-world roots and may be separated
// from a Trade-language classifier such as "River" or "Kingdom".
const TRADE_NAME_WORDS = new Set([
  ...COMMON_DESCRIPTOR_WORDS,
  ...COMMON_COMPOUND_PARTS,
  "ancient", "angel", "apple", "arrow", "badger", "bear", "blind", "blood",
  "blue", "broken", "burning", "cat", "copper", "crown", "dawn", "dead",
  "death", "door", "dust", "eagle", "elder", "empty", "eye", "far", "fat",
  "father", "feather", "fox", "free", "giant", "glass", "golden", "great",
  "hammer", "hawk", "hidden", "holy", "horse", "hound", "ice", "inner",
  "lion", "little", "lost", "lower", "merchant", "midnight", "mother",
  "new", "night", "northern", "old", "open", "outer", "owl", "path",
  "rainbow", "raven", "royal", "sage", "salt", "sand", "secret", "seven",
  "singing", "snake", "southern", "spirit", "stag", "steel", "sunken",
  "teeth", "thunder", "twilight", "upper", "western", "wolf", "worker",
  "young",
  "abyssal", "air", "all", "archive", "astral", "azure", "bank", "barking",
  "bastion", "battery", "blessing", "bloom", "boreal", "bridgeward",
  "caravanserai", "cedar", "channel", "charitable", "children", "circular",
  "cleaver", "cold", "colossus", "compound", "consciousness", "court",
  "creation", "crimson", "crystal", "dandelion", "divine", "dolphin",
  "dreamworld", "drunken", "dyer", "earth", "eastern", "eightfold",
  "elegant", "elemental", "emerald", "empty", "ending", "energy", "evening",
  "faculty", "fate", "feast", "flagon", "flame", "folly", "forge",
  "fortune", "foundry", "fraternity", "gossamer", "grace", "granite",
  "grove", "guildhall", "harmony", "heartwood", "hero", "highmoor",
  "history", "honeybloom", "hunter", "imperial", "islander", "keep",
  "knife", "lair", "law", "leaf", "leviathan", "lily", "lonely", "luck",
  "mad", "magic", "market", "material", "mayor", "metal", "metaphysics",
  "mill", "mirror", "mist", "muddy", "mug", "mundane", "negative",
  "oracle", "ox", "palace", "philosopher", "pig", "positive", "presence",
  "prime", "prince", "purple", "pyre", "quarter", "queen", "quill",
  "radiant", "refuge", "rest", "resting", "reaver", "riven", "riverside",
  "rocky", "salty", "scroll", "seal", "setting", "shield", "shrouded",
  "sleepless", "smiling", "sober", "society", "splendor", "spire", "spout",
  "squid", "summit", "sunset", "swan", "tanner", "theology", "thirsty",
  "tideswell", "toad", "tower", "traveler", "trench", "tribe", "twenty",
  "umber", "underhill", "veil", "wandering", "watch", "watcher",
  "watchtower", "wave", "whale", "windward", "workhouse",
  "bandit", "baron", "bog", "chaos", "chasm", "covenant", "crab",
  "crossroads", "dead", "edge", "endless", "ethereal", "fair", "gleam",
  "gull", "havoc", "home", "host", "land", "laughing", "lord", "mesa",
  "mind", "one", "own", "people", "plane", "ruin", "rust", "sail", "scholar",
  "sentient", "sentinel", "seventh", "shimmering", "smiling", "street",
  "umbral", "village", "void", "wall", "wanderer", "way", "world",
  "a", "an", "and", "at", "by", "for", "from", "in", "of", "on", "s", "the",
]);

const PLACE_CLASSIFIERS = [
  "archipelago", "bay", "bridge", "canal", "castle", "cavern", "city",
  "cliffs", "coast", "crossing", "desert", "falls", "fens", "forest",
  "fort", "fortress", "gap", "gate", "gorge", "gulf", "harbor", "heights",
  "highlands", "hill", "hills", "hold", "island", "islands", "isle",
  "isles", "lake", "lands", "march", "marsh", "mount", "mountain",
  "mountains", "ocean", "pass", "peak", "plains", "plateau", "port",
  "province", "range", "realm", "river", "road", "sea", "strait", "swamp",
  "tower", "trail", "vale", "valley", "village", "waters", "watershed",
  "wood", "woods",
];

const ORGANIZATION_CLASSIFIERS = [
  "alliance", "army", "church", "clan", "company", "confederacy", "cult",
  "duchy", "empire", "fellowship", "guild", "house", "kingdom", "order",
  "republic", "society", "temple", "university",
];

const HONORIFICS = [
  "archfey", "archmage", "baroness", "baron", "captain", "caretaker",
  "chiefling", "chief archivist", "chief", "commander", "countess", "count",
  "duchess", "duke", "elder", "emperor", "empress", "general", "grandpa",
  "hakeasa", "head priest", "high king", "king", "lady", "laivan",
  "loremaster", "lord", "magistros", "major", "marshal", "master", "prince",
  "princess", "proconsul", "queen", "saint", "samraat", "sergeant", "sir",
  "speaker",
];

const LEXICAL_HONORIFICS = new Set([
  "hakeasa",
  "laivan",
  "magistros",
  "samraat",
]);

const VARIANT_KINDS = [
  "exact",
  "titled",
  "article",
  "orthographic",
  "descriptor",
  "abbreviation",
  "short",
  "manual",
];

const UNKNOWN_LANGUAGE = {
  family: "Unknown",
  language: "Unknown",
  confidence: "unknown",
  basis: "No reliable language evidence found",
};

function languageResult(family, language, confidence, basis) {
  return { family, language, confidence, basis };
}

function familyForLanguage(language) {
  return LANGUAGE_FAMILY.get(language) || "Unknown";
}

function normalizeTypography(value) {
  return String(value || "")
    .normalize("NFKC")
    .replace(/[’‘]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/[‐‑‒–—]/g, "-")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizeStrict(value) {
  return normalizeTypography(value)
    .toLocaleLowerCase("en")
    .replace(/[^a-z0-9À-ž]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizeLoose(value) {
  return normalizeTypography(value)
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLocaleLowerCase("en")
    .replace(/[^a-z0-9]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function provisionalNameInfo(value) {
  const original = normalizeTypography(value);
  const match = original.match(/^~\s*(.+?)\s*~$/);
  return {
    original,
    text: match ? normalizeTypography(match[1]) : original,
    provisional: Boolean(match),
  };
}

function nameReviewForSubject(subject) {
  const tags = toStrings(subject.tags).map((tag) =>
    String(tag).replace(/^#/, "").toLocaleLowerCase("en")
  );
  const marker = provisionalNameInfo(
    subject.rawName || subject.name || subject.fileName,
  );
  const reasons = [];
  if (tags.includes("status/check/name")) reasons.push("status/check/name");
  if (subject.provisionalName || marker.provisional) {
    reasons.push("provisional-name-marker");
  }
  return {
    needsNameReview: reasons.length > 0,
    nameReviewReasons: [...new Set(reasons)],
  };
}

function subtypeForSubject(noteType, fields = {}) {
  const candidates = noteType === "person"
    ? [["species", fields.species]]
    : [["typeOf", fields.typeOf]];
  for (const [source, rawValues] of candidates) {
    const values = [];
    const seen = new Set();
    for (const rawValue of toStrings(rawValues)) {
      const value = cleanAlias(rawValue);
      const key = normalizeLoose(value);
      if (!value || !key || seen.has(key)) continue;
      seen.add(key);
      values.push(value);
    }
    if (values.length) {
      return {
        values,
        label: values.join(" · "),
        source,
      };
    }
  }
  return { values: [], label: "", source: "" };
}

function subtypeChoices(subjects, noteType = "") {
  const byKey = new Map();
  for (const subject of subjects || []) {
    if (noteType && subject.noteType !== noteType) continue;
    for (const subtype of toStrings(subject.subtypes)) {
      const key = normalizeLoose(subtype);
      if (key && !byKey.has(key)) byKey.set(key, subtype);
    }
  }
  return [...byKey.values()].sort((left, right) =>
    left.localeCompare(right)
  );
}

function normalizedTokens(value) {
  const normalized = normalizeLoose(value);
  return normalized ? normalized.split(" ") : [];
}

function cleanAlias(value) {
  let output = String(value || "");
  output = output.replace(/!\[\[[^\]]+\]\]/g, "");
  output = output.replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "$2");
  output = output.replace(/\[\[([^\]]+)\]\]/g, "$1");
  output = output.trim().replace(/^[*_`"'“”‘’]+|[*_`"'“”‘’]+$/g, "");
  return output.replace(/\s+/g, " ").replace(/^[ ,;:.]+|[ ,;:.]+$/g, "");
}

function plausibleName(value) {
  if (!value || value.length < 2 || value.length > 100) return false;
  if ((value.match(/ /g) || []).length > 12) return false;
  if (/(\$=|dv\.view|<[^>]+>|::)/.test(value)) return false;
  if (/^(names?|information|dm notes)$/i.test(value)) return false;
  if (/^(?:status|campaign|source|type)\//i.test(value)) return false;
  if (/[.!?]\s/.test(value)) return false;
  return /[A-Za-zÀ-ž]/.test(value);
}

function stripArticles(value) {
  return normalizeStrict(value).replace(/^(the|a|an)\s+/, "");
}

function titleCandidates(subject) {
  const values = new Set(HONORIFICS);
  for (const title of toStrings(subject.title)) {
    const normalized = normalizeStrict(title);
    if (normalized) values.add(normalized);
  }
  return [...values].sort((a, b) => b.length - a.length);
}

function titleRendering(value) {
  const normalized = normalizeStrict(value);
  if (transparentTradePhrase(value)) return "trade";
  if (HONORIFICS.includes(normalized) && !LEXICAL_HONORIFICS.has(normalized)) {
    return "trade";
  }
  return "lexical";
}

function stripLeadingTitle(value, subject) {
  let normalized = normalizeStrict(value);
  for (const title of titleCandidates(subject)) {
    if (normalized === title) return "";
    if (normalized.startsWith(`${title} `)) {
      return normalized.slice(title.length + 1).trim();
    }
  }
  return normalized;
}

function descriptorCore(value) {
  const tokens = normalizedTokens(value).filter(
    (token) => !COMMON_DESCRIPTOR_WORDS.has(token) && !["the", "of"].includes(token),
  );
  return tokens.map(singularizeToken).join(" ");
}

function singularizeToken(token) {
  if (token.length > 4 && token.endsWith("ies")) {
    return `${token.slice(0, -3)}y`;
  }
  if (token.length > 3 && token.endsWith("s") && !token.endsWith("ss")) {
    return token.slice(0, -1);
  }
  return token;
}

function isContiguousSubsequence(shorter, longer) {
  if (!shorter.length || shorter.length >= longer.length) return false;
  for (let start = 0; start <= longer.length - shorter.length; start += 1) {
    let matches = true;
    for (let index = 0; index < shorter.length; index += 1) {
      if (shorter[index] !== longer[start + index]) {
        matches = false;
        break;
      }
    }
    if (matches) return true;
  }
  return false;
}

function initialsFor(value) {
  const tokens = normalizedTokens(value).filter(
    (token) => !COMMON_DESCRIPTOR_WORDS.has(token) && !["the", "of"].includes(token),
  );
  return tokens.map((token) => token[0]).join("");
}

function isInitialForm(value) {
  const tokens = normalizedTokens(value);
  return tokens.length >= 2 && tokens.every((token) => token.length === 1);
}

function classifyVariant(form, preferred, subject = {}) {
  const formStrict = normalizeStrict(form);
  const preferredStrict = normalizeStrict(preferred);
  if (!formStrict || !preferredStrict) return null;
  if (formStrict === preferredStrict) return { kind: "exact", score: 100 };

  const formUntitled = stripLeadingTitle(form, subject);
  const preferredUntitled = stripLeadingTitle(preferred, subject);
  if (
    formUntitled &&
    preferredUntitled &&
    formUntitled === preferredUntitled &&
    (formUntitled !== formStrict || preferredUntitled !== preferredStrict)
  ) {
    return { kind: "titled", score: 95 };
  }

  if (stripArticles(form) === stripArticles(preferred)) {
    return { kind: "article", score: 90 };
  }

  if (normalizeLoose(form) === normalizeLoose(preferred)) {
    return { kind: "orthographic", score: 85 };
  }

  const formCore = descriptorCore(form);
  const preferredCore = descriptorCore(preferred);
  const formHasDescriptor = normalizedTokens(form).some((token) =>
    COMMON_DESCRIPTOR_WORDS.has(token)
  );
  const preferredHasDescriptor = normalizedTokens(preferred).some((token) =>
    COMMON_DESCRIPTOR_WORDS.has(token)
  );
  if (
    formCore &&
    formCore === preferredCore &&
    normalizeLoose(form) !== normalizeLoose(preferred) &&
    (formHasDescriptor || preferredHasDescriptor)
  ) {
    return { kind: "descriptor", score: 80 };
  }

  if (isInitialForm(form) && initialsFor(form) === initialsFor(preferred)) {
    return { kind: "abbreviation", score: 75 };
  }
  if (isInitialForm(preferred) && initialsFor(form) === initialsFor(preferred)) {
    return { kind: "abbreviation", score: 75 };
  }

  const formTokens = normalizedTokens(stripLeadingTitle(form, subject));
  const preferredTokens = normalizedTokens(stripLeadingTitle(preferred, subject));
  if (
    isContiguousSubsequence(formTokens, preferredTokens) ||
    isContiguousSubsequence(preferredTokens, formTokens)
  ) {
    return { kind: "short", score: 65 };
  }

  return null;
}

function removeObsidianComments(text) {
  return String(text || "").replace(/%%.*?%%/gs, "");
}

function extractTextAliases(body, primary) {
  let cleaned = removeObsidianComments(body);
  cleaned = cleaned.split(/^##\s+DM\s+notes?\s*$/im, 1)[0] || cleaned;
  const lines = cleaned.split(/\r?\n/);
  const patterns = [
    /\b(?:also\s+known\s+as|known\s+as|called|named)\s+(?:the\s+)?[“"]([^”"\n]{2,100})[”"]/gi,
    /\b(?:also\s+known\s+as|known\s+as|called|named)\s+(?:the\s+)?\*\*([^*\n]{2,100})\*\*/gi,
  ];
  const output = [];
  const seen = new Set();
  const primaryNeedle = normalizeLoose(primary);

  lines.forEach((line, index) => {
    if (!normalizeLoose(line).includes(primaryNeedle)) return;
    for (const pattern of patterns) {
      pattern.lastIndex = 0;
      let match;
      while ((match = pattern.exec(line)) !== null) {
        const form = cleanAlias(match[1]);
        const key = normalizeStrict(form);
        if (
          plausibleName(form) &&
          key &&
          key !== normalizeStrict(primary) &&
          !seen.has(key)
        ) {
          seen.add(key);
          output.push({
            text: form,
            source: "text",
            line: index + 1,
            evidence: line.trim().slice(0, 300),
          });
        }
      }
    }
  });
  return output;
}

function evidenceText(value) {
  return normalizeTypography(value)
    .replace(/%%/g, " ")
    .replace(/!\[\[[^\]]+\]\]/g, " ")
    .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "$2")
    .replace(/\[\[([^\]]+)\]\]/g, "$1")
    .replace(/[*_`"“”]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function exactSpans(text, needle) {
  const haystack = normalizeTypography(text).toLocaleLowerCase("en");
  const target = normalizeTypography(needle).toLocaleLowerCase("en");
  if (!target) return [];
  const spans = [];
  let start = 0;
  while (start < haystack.length) {
    const index = haystack.indexOf(target, start);
    if (index < 0) break;
    const before = haystack[index - 1] || "";
    const after = haystack[index + target.length] || "";
    const word = /[a-z0-9À-ž']/i;
    if (!word.test(before) && !word.test(after)) {
      spans.push({ start: index, end: index + target.length });
    }
    start = index + Math.max(1, target.length);
  }
  return spans;
}

function languageMentions(text) {
  const output = [];
  for (const [terms, family, language] of EXPLICIT_LANGUAGE_TERMS) {
    for (const term of terms) {
      for (const span of exactSpans(text, term)) {
        output.push({ ...span, term, family, language });
      }
    }
  }
  return output.sort((left, right) =>
    left.start - right.start || right.end - left.end
  );
}

function lastNamingVerbBefore(text, limit) {
  const prefix = text.slice(0, limit);
  const pattern = /\b(?:called|known\s+as|named|rendered\s+as)\b/gi;
  let match;
  let last = -1;
  while ((match = pattern.exec(prefix)) !== null) last = match.index;
  return last;
}

function evidenceRelation(clause, nameSpan, languageSpan) {
  const lowered = clause.toLocaleLowerCase("en");
  const beforeLanguage = lowered.slice(0, languageSpan.start);
  const afterLanguage = lowered.slice(languageSpan.end);
  const languageEndsPhrase =
    !/^\s+[a-z]/.test(afterLanguage) ||
    /^\s+(?:tongue|language|speech)\b/.test(afterLanguage);

  if (nameSpan.start < languageSpan.start) {
    const between = lowered.slice(nameSpan.end, languageSpan.start);
    const namingVerb = lastNamingVerbBefore(lowered, languageSpan.start);
    if (
      namingVerb >= 0 &&
      namingVerb < nameSpan.start &&
      nameSpan.start - namingVerb < 120 &&
      /\bin\s+(?:the\s+)?$/.test(between) &&
      !/[,;][^,;]*\bin\s+(?:the\s+)?$/.test(between) &&
      languageEndsPhrase
    ) {
      return "called NAME in LANGUAGE";
    }
    if (
      /^\s+(?:is|was|remains|became)\s+(?:the\s+)?$/.test(between) &&
      /^\s+(?:tongue|language)\b/.test(afterLanguage)
    ) {
      return "NAME is LANGUAGE language";
    }
    if (
      /^\s+(?:is|was|remains|became)\s+(?:the\s+)?$/.test(between) &&
      /^\s+(?:name|word|term|phrase|exonym|endonym)\b/.test(afterLanguage)
    ) {
      return "NAME is the LANGUAGE name";
    }
    if (
      /\b(?:means|translated|rendered)\b/.test(between) &&
      /\bin\s+(?:the\s+)?$/.test(between)
    ) {
      return "NAME translated in LANGUAGE";
    }
    if (
      /^\s*,?\s*(?:is\s+|was\s+)?$/.test(between) &&
      /^\s+(?:for|meaning)\b/.test(afterLanguage)
    ) {
      return "NAME, LANGUAGE for";
    }
  } else {
    const between = lowered.slice(languageSpan.end, nameSpan.start);
    const introducedAsNamingLanguage =
      /\b(?:in|to|by|from)\s+(?:the\s+)?$/.test(beforeLanguage) &&
      /^\s*[,.:-]/.test(between);
    const languageAsCallingSubject =
      /^\s+(?:people\s+)?(?:called|call|named|name|knew|know)\b/.test(
        between,
      );
    if (
      (introducedAsNamingLanguage || languageAsCallingSubject) &&
      /\b(?:called(?:\s+(?:him|her|it|them))?|known\s+as|named|rendered\s+as)\s+(?:the\s+)?$/.test(
        between,
      )
    ) {
      return "in LANGUAGE, called NAME";
    }
    if (
      /^\s+(?:tongue|language)?\s*(?:name|word|term|phrase|exonym|endonym)\s*(?:(?:is|was)\s+|[:,—-]\s*)?(?:the\s+)?$/.test(
        between,
      )
    ) {
      return "LANGUAGE name NAME";
    }
  }
  return "";
}

function languageFromNamingContext(context, name, basis) {
  const clause = evidenceText(context);
  const candidates = [];
  for (const nameSpan of exactSpans(clause, name)) {
    for (const mention of languageMentions(clause)) {
      const pattern = evidenceRelation(clause, nameSpan, mention);
      if (pattern) candidates.push({ ...mention, pattern });
    }
  }
  const languages = new Set(candidates.map((candidate) => candidate.language));
  if (languages.size > 1) {
    return {
      ...UNKNOWN_LANGUAGE,
      confidence: "conflict",
      basis: `${basis}: conflicting text evidence (${[...languages].join(", ")})`,
      evidence: candidates,
    };
  }
  const candidate = candidates[0];
  if (!candidate) return null;
  return {
    ...languageResult(
      candidate.family,
      candidate.language,
      "text-evidence",
      `${basis}: ${candidate.pattern}`,
    ),
    evidence: candidates,
  };
}

function explicitLanguageForName(body, name, label) {
  if (!normalizeLoose(name)) return null;
  const candidates = [];
  let inComment = false;

  String(body || "").split(/\r?\n/).forEach((line, index) => {
    const markerCount = (line.match(/%%/g) || []).length;
    const lineIsComment = inComment || markerCount > 0;
    const clauses = evidenceText(line).split(/\s*(?:;|(?<=[.!?])\s+)\s*/);
    for (const clause of clauses) {
      if (!exactSpans(clause, name).length) continue;
      const suffix = lineIsComment ? " (comment)" : "";
      const result = languageFromNamingContext(
        clause,
        name,
        `${label}, body line ${index + 1}${suffix}`,
      );
      if (result) {
        candidates.push({
          result,
          quote: clause.trim().slice(0, 300),
          line: index + 1,
        });
      }
    }
    if (markerCount % 2) inComment = !inComment;
  });

  if (!candidates.length) return null;
  const languages = new Set(
    candidates
      .filter((candidate) => candidate.result.language !== "Unknown")
      .map((candidate) => candidate.result.language),
  );
  if (
    languages.size > 1 ||
    candidates.some((candidate) => candidate.result.confidence === "conflict")
  ) {
    return {
      ...UNKNOWN_LANGUAGE,
      confidence: "conflict",
      basis: `${label}: conflicting text evidence (${[...languages].join(", ")})`,
      evidence: candidates,
    };
  }
  const chosen = candidates[0].result;
  return {
    ...chosen,
    evidence: candidates.map((candidate) => ({
      line: candidate.line,
      quote: candidate.quote,
      pattern: candidate.result.evidence?.[0]?.pattern || "",
      language: candidate.result.language,
    })),
  };
}

function looksCommon(name) {
  const words = normalizedTokens(name);
  if (words.some((word) => COMMON_DESCRIPTOR_WORDS.has(word))) return true;
  const squashed = words.join("");
  let matches = 0;
  for (const part of COMMON_COMPOUND_PARTS) {
    if (squashed.includes(part)) matches += 1;
  }
  return matches >= 2;
}

function transparentTradePhrase(name) {
  const words = normalizedTokens(name).filter((word) => !/^\d+$/.test(word));
  if (!words.length) return false;
  if (words.every((word) => TRADE_NAME_WORDS.has(word))) return true;
  if (words.length === 1) {
    const squashed = words[0];
    let matches = 0;
    for (const part of COMMON_COMPOUND_PARTS) {
      if (part.length >= 4 && squashed.includes(part)) matches += 1;
    }
    return matches >= 2;
  }
  return false;
}

function tradeRenderingResult(basis) {
  return languageResult(
    "Trade",
    "Trade (unspecified)",
    "convention",
    basis || "transparent English trade-tongue rendering",
  );
}

function languageFromAncestry(values, basisPrefix) {
  const strings = toStrings(values);
  const lowered = strings.join(" ").toLocaleLowerCase("en");
  for (const [keywords, family, language] of ANCESTRY_LANGUAGE_RULES) {
    if (keywords.some((keyword) => lowered.includes(keyword))) {
      return languageResult(
        family,
        language,
        "inferred",
        `${basisPrefix}: ${strings.join(", ")}`,
      );
    }
  }
  return null;
}

function languageFromPath(path) {
  for (const [fragment, family, language] of PATH_LANGUAGE_RULES) {
    if (String(path || "").includes(fragment)) {
      return languageResult(
        family,
        language,
        "inferred",
        `vault path: ${fragment.replace(/\/$/, "")}`,
      );
    }
  }
  return null;
}

function languageFromLocations(locations) {
  const strings = toStrings(locations);
  const lowered = strings.join(" ").toLocaleLowerCase("en");
  for (const [keywords, family, language] of LOCATION_LANGUAGE_RULES) {
    if (keywords.some((keyword) => lowered.includes(keyword))) {
      return languageResult(
        family,
        language,
        "inferred",
        `whereabouts: ${strings.join(", ")}`,
      );
    }
  }
  return null;
}

function inferPrimaryLanguage(subject) {
  const explicit = explicitLanguageForName(
    subject.body,
    subject.name,
    "primary-name text evidence",
  );
  if (explicit) return explicit;

  if (
    subject.noteType !== "person" &&
    transparentTradePhrase(subject.name)
  ) {
    return tradeRenderingResult();
  }

  const ancestry = languageFromAncestry(subject.ancestry, "ancestry");
  if (ancestry) return ancestry;
  const species = languageFromAncestry(subject.species, "species");
  if (species) return species;
  const fromPath = languageFromPath(subject.path);
  if (fromPath) return fromPath;
  const location = languageFromLocations(subject.locations);
  if (location) return location;

  if (transparentTradePhrase(subject.name)) {
    return tradeRenderingResult();
  }
  return { ...UNKNOWN_LANGUAGE };
}

function inferConceptLanguage(concept, subject, primaryLanguage) {
  if (concept.role === "primary") return primaryLanguage;
  const explicit = explicitLanguageForName(
    subject.body,
    concept.preferredForm,
    "alternate-name text evidence",
  );
  if (explicit) return explicit;
  if (transparentTradePhrase(concept.preferredForm)) {
    return tradeRenderingResult();
  }
  if (primaryLanguage.language !== "Unknown") {
    return languageResult(
      primaryLanguage.family,
      primaryLanguage.language,
      "inferred",
      "same-subject naming context; alternate-name language is not text-bound",
    );
  }
  return { ...UNKNOWN_LANGUAGE };
}

function conceptIdForForm(form) {
  return `form:${normalizeStrict(form)}`;
}

function formDecisionKey(subjectPath, form) {
  return `${subjectPath}\u0000${normalizeStrict(form)}`;
}

function conceptDecisionKey(subjectPath, conceptId) {
  return `${subjectPath}\u0000${conceptId}`;
}

function mergeObservedForms(subject) {
  const primaryName = provisionalNameInfo(subject.name).text;
  const candidates = [
    { text: primaryName, source: "primary" },
    ...toStrings(subject.aliases).map((text) => ({ text, source: "frontmatter" })),
    ...(subject.textAliases || []),
  ];

  const byKey = new Map();
  for (const candidate of candidates) {
    const text = cleanAlias(candidate.text);
    const key = normalizeStrict(text);
    if (!plausibleName(text) || !key) continue;
    if (!byKey.has(key)) {
      byKey.set(key, {
        text,
        normalized: key,
        sources: [],
        evidence: [],
      });
    }
    const record = byKey.get(key);
    if (!record.sources.includes(candidate.source)) record.sources.push(candidate.source);
    if (candidate.evidence && !record.evidence.includes(candidate.evidence)) {
      record.evidence.push(candidate.evidence);
    }
  }
  return [...byKey.values()];
}

function makeConcept(subject, form, role) {
  const id = role === "primary" ? "primary" : conceptIdForForm(form.text);
  return {
    id,
    subjectPath: subject.path,
    subjectName: subject.name,
    preferredForm: form.text,
    normalized: normalizeLoose(form.text),
    role,
    forms: [
      {
        ...form,
        variantKind: "canonical",
        automatic: true,
      },
    ],
  };
}

function addVariant(concept, form, variantKind, automatic = true) {
  concept.forms.push({
    ...form,
    variantKind,
    automatic,
  });
}

function buildConcepts(subject, formDecisionMap = new Map()) {
  const forms = mergeObservedForms(subject);
  if (!forms.length) return [];
  const primaryIndex = forms.findIndex((form) => form.sources.includes("primary"));
  const primaryForm = forms.splice(primaryIndex >= 0 ? primaryIndex : 0, 1)[0];
  const concepts = [makeConcept(subject, primaryForm, "primary")];

  for (const form of forms) {
    const decision = formDecisionMap.get(formDecisionKey(subject.path, form.text));
    if (decision?.action === "group-primary") {
      addVariant(
        concepts[0],
        form,
        VARIANT_KINDS.includes(decision.variantKind) ? decision.variantKind : "manual",
        false,
      );
      continue;
    }
    if (decision?.action === "separate") {
      concepts.push(makeConcept(subject, form, form.sources.includes("text") ? "text" : "alias"));
      continue;
    }

    let best = null;
    for (const concept of concepts) {
      const classification = classifyVariant(form.text, concept.preferredForm, subject);
      if (classification && (!best || classification.score > best.classification.score)) {
        best = { concept, classification };
      }
    }

    if (best) {
      addVariant(best.concept, form, best.classification.kind, true);
      continue;
    }

    concepts.push(makeConcept(subject, form, form.sources.includes("text") ? "text" : "alias"));
  }
  return concepts;
}

function componentIdForPart(text, index) {
  return `part:${index}:${normalizeStrict(text)}`;
}

function componentDecisionKey(subjectPath, conceptId, componentId) {
  return `${subjectPath}\u0000${conceptId}\u0000${componentId}`;
}

function makeComponents(parts) {
  return parts
    .filter((part) => normalizeTypography(part.text))
    .map((part, index) => ({
      id: componentIdForPart(part.text, index),
      text: normalizeTypography(part.text),
      normalized: normalizeStrict(part.text),
      role: part.role,
      rendering: part.rendering || "lexical",
      reference: part.reference || "",
      automatic: true,
    }));
}

function matchingLeadingTitle(value, subject) {
  const text = normalizeTypography(value);
  for (const title of titleCandidates(subject)) {
    const match = text.match(new RegExp(`^(${escapeRegExp(title)})\\s+`, "i"));
    if (match) return match[1];
  }
  return "";
}

function decomposePersonName(value, subject) {
  let remainder = normalizeTypography(value);
  const parts = [];
  const articleMatch = remainder.match(/^(?:the|a|an)\s+/i);
  if (articleMatch) remainder = remainder.slice(articleMatch[0].length).trim();

  const title = matchingLeadingTitle(remainder, subject);
  if (title) {
    parts.push({
      text: title,
      role: "title",
      rendering: titleRendering(title),
    });
    remainder = remainder.slice(title.length).trim();
  }

  let ordinal = "";
  const ordinalMatch = remainder.match(
    /\s+((?:[IVXLCDM]+)|(?:\d+(?:st|nd|rd|th)?))$/i,
  );
  if (ordinalMatch) {
    ordinal = ordinalMatch[1];
    remainder = remainder.slice(0, ordinalMatch.index).trim();
  }

  let modifier = null;
  const epithetMatch = remainder.match(/\s+(the\s+[^,;]+)$/i);
  const locativeMatch = remainder.match(/\s+((?:of|from)\s+[^,;]+)$/i);
  const chosen = [epithetMatch, locativeMatch]
    .filter(Boolean)
    .sort((left, right) => left.index - right.index)[0];
  if (chosen) {
    modifier = {
      text: chosen[1],
      role: chosen === epithetMatch ? "epithet" : "locative",
      rendering: "trade",
      reference: chosen === locativeMatch
        ? chosen[1].replace(/^(?:of|from)\s+(?:the\s+)?/i, "")
        : "",
    };
    remainder = remainder.slice(0, chosen.index).trim();
  }

  if (remainder) parts.push({ text: remainder, role: "core" });
  if (modifier) parts.push(modifier);
  if (ordinal) {
    parts.push({
      text: ordinal,
      role: "ordinal",
      rendering: "neutral",
    });
  }
  return makeComponents(parts.length ? parts : [{ text: value, role: "core" }]);
}

function classifierPattern(values) {
  return values
    .slice()
    .sort((left, right) => right.length - left.length)
    .map(escapeRegExp)
    .join("|");
}

const PLACE_CLASSIFIER_PATTERN = classifierPattern(PLACE_CLASSIFIERS);
const ORGANIZATION_CLASSIFIER_PATTERN = classifierPattern(
  ORGANIZATION_CLASSIFIERS,
);

function decomposeNonPersonName(value, subject) {
  let remainder = normalizeTypography(value);
  const parts = [];
  const articleMatch = remainder.match(/^(the|a|an)\s+/i);
  if (articleMatch) remainder = remainder.slice(articleMatch[0].length).trim();

  if (transparentTradePhrase(remainder)) {
    parts.push({
      text: remainder,
      role: "descriptive",
      rendering: "trade",
    });
    return makeComponents(parts);
  }

  const classifiers = subject.noteType === "place"
    ? PLACE_CLASSIFIER_PATTERN
    : `${ORGANIZATION_CLASSIFIER_PATTERN}|${PLACE_CLASSIFIER_PATTERN}`;
  const ofPrefix = remainder.match(
    new RegExp(`^((?:${classifiers})\\s+of)\\s+(?:the\\s+)?(.+)$`, "i"),
  );
  if (ofPrefix) {
    parts.push({
      text: ofPrefix[1],
      role: "classifier",
      rendering: "trade",
    });
    parts.push({
      text: ofPrefix[2],
      role: transparentTradePhrase(ofPrefix[2]) ? "descriptive" : "core",
      rendering: transparentTradePhrase(ofPrefix[2]) ? "trade" : "lexical",
    });
    return makeComponents(parts);
  }

  const suffix = remainder.match(
    new RegExp(`^(.+?)\\s+(${classifiers})$`, "i"),
  );
  if (suffix) {
    const rootIsTrade = transparentTradePhrase(suffix[1]);
    parts.push({
      text: suffix[1],
      role: rootIsTrade ? "descriptive" : "core",
      rendering: rootIsTrade ? "trade" : "lexical",
    });
    parts.push({
      text: suffix[2],
      role: "classifier",
      rendering: "trade",
    });
    return makeComponents(parts);
  }

  const prefix = remainder.match(
    new RegExp(`^(${classifiers})\\s+(.+)$`, "i"),
  );
  if (prefix) {
    parts.push({
      text: prefix[1],
      role: "classifier",
      rendering: "trade",
    });
    const rootIsTrade = transparentTradePhrase(prefix[2]);
    parts.push({
      text: prefix[2],
      role: rootIsTrade ? "descriptive" : "core",
      rendering: rootIsTrade ? "trade" : "lexical",
    });
    return makeComponents(parts);
  }

  parts.push({
    text: remainder,
    role: transparentTradePhrase(remainder) ? "descriptive" : "core",
    rendering: transparentTradePhrase(remainder) ? "trade" : "lexical",
  });
  return makeComponents(parts);
}

function decomposeDisplayName(value, subject) {
  return subject.noteType === "person"
    ? decomposePersonName(value, subject)
    : decomposeNonPersonName(value, subject);
}

function inferredLanguageForComponent(component, concept, subject) {
  if (component.role === "ordinal") {
    return languageResult(
      "Special",
      "Language-neutral",
      "structural",
      "ordinal or numeric discriminator",
    );
  }

  if (["locative", "classifier"].includes(component.role)) {
    return tradeRenderingResult(
      `${component.role} component uses a transparent trade-tongue construction`,
    );
  }

  const textEvidence = explicitLanguageForName(
    subject.body,
    component.text,
    `text evidence for ${component.role} component`,
  );
  if (textEvidence) return textEvidence;

  if (
    component.rendering === "trade" ||
    component.role === "epithet" ||
    transparentTradePhrase(component.text)
  ) {
    return tradeRenderingResult(
      `${component.role} component uses a transparent trade-tongue rendering`,
    );
  }

  const ancestry = languageFromAncestry(subject.ancestry, "ancestry");
  if (ancestry) return ancestry;
  const species = languageFromAncestry(subject.species, "species");
  if (species) return species;
  const fromPath = languageFromPath(subject.path);
  if (fromPath) return fromPath;
  const location = languageFromLocations(subject.locations);
  if (location) return location;

  return { ...UNKNOWN_LANGUAGE };
}

function normalizeMatchValue(value) {
  return normalizeLoose(value);
}

function valueMatches(actualValues, expected) {
  if (!expected || expected === "*") return true;
  const expectedNormalized = normalizeMatchValue(expected);
  return toStrings(actualValues).some(
    (value) => normalizeMatchValue(value) === expectedNormalized,
  );
}

function ruleMatches(rule, subject, concept, inferredLanguage, component = null) {
  if (rule.enabled === false) return false;
  const match = rule.match || {};
  if (!valueMatches(subject.noteType, match.noteType)) return false;
  if (!valueMatches(subject.species, match.species)) return false;
  if (!valueMatches(subject.ancestry, match.ancestry)) return false;
  if (!valueMatches(concept.role, match.role)) return false;
  if (!valueMatches(component?.role || "", match.componentRole)) return false;
  if (!valueMatches(inferredLanguage.language, match.inferredLanguage)) return false;
  if (match.folder && !subject.path.toLocaleLowerCase("en").startsWith(
    String(match.folder).toLocaleLowerCase("en"),
  )) return false;
  return true;
}

function firstMatchingRule(
  rules,
  subject,
  concept,
  inferredLanguage,
  component = null,
) {
  return [...rules]
    .filter((rule) => rule.type === "rule")
    .sort((left, right) => {
      const priority = Number(right.priority || 0) - Number(left.priority || 0);
      return priority || String(left.id).localeCompare(String(right.id));
    })
    .find((rule) =>
      ruleMatches(rule, subject, concept, inferredLanguage, component)
    );
}

function decorateConcept(concept, subject, inferredLanguage, conceptDecision, rules) {
  let effective = inferredLanguage;
  let languageSource = ["text-evidence", "conflict"].includes(
    inferredLanguage.confidence,
  )
    ? inferredLanguage.confidence
    : "inference";
  let matchedRule = null;

  if (conceptDecision && Object.prototype.hasOwnProperty.call(conceptDecision, "language")) {
    effective = languageResult(
      familyForLanguage(conceptDecision.language),
      conceptDecision.language,
      "decided",
      conceptDecision.notes || "Human catalog decision",
    );
    languageSource = "decision";
  } else if (
    !["text-evidence", "conflict"].includes(inferredLanguage.confidence)
  ) {
    matchedRule = firstMatchingRule(rules, subject, concept, inferredLanguage);
    if (matchedRule) {
      effective = languageResult(
        familyForLanguage(matchedRule.language),
        matchedRule.language,
        "rule",
        `catalog rule: ${matchedRule.label || matchedRule.id}`,
      );
      languageSource = "rule";
    }
  }

  let status;
  if (languageSource === "decision") {
    if (effective.language === "Unknown") status = "reviewed-unknown";
    else if (effective.language === inferredLanguage.language) status = "confirmed";
    else status = "overridden";
  } else if (languageSource === "rule") status = "rule";
  else if (languageSource === "text-evidence") status = "text-evidence";
  else if (languageSource === "conflict") status = "conflict";
  else if (effective.confidence === "convention") status = "convention";
  else if (effective.language === "Unknown") status = "unknown";
  else status = "inferred";

  return {
    ...concept,
    subject,
    inferredLanguage,
    effectiveLanguage: effective,
    languageSource,
    status,
    matchedRuleId: matchedRule?.id || null,
    decision: conceptDecision || null,
    relationship: conceptDecision?.relationship || "",
    derivation: conceptDecision?.derivation || "",
    usage: conceptDecision?.usage || "",
    community: conceptDecision?.community || "",
    decisionNotes: conceptDecision?.notes || "",
  };
}

function kindLabel(concept) {
  const labels = [];
  if (concept.usage) labels.push(capitalize(concept.usage));
  if (concept.derivation && concept.derivation !== "original") {
    const derivationLabels = {
      translation: "translated",
      "literal-translation": "literal translation",
      "conventional-translation": "conventional translation",
      "unattested-translation": "unattested translation",
    };
    labels.push(
      derivationLabels[concept.derivation] || concept.derivation,
    );
  }
  if (concept.relationship) labels.push(concept.relationship);
  return labels.join(" ") || "—";
}

function decorateComponent(
  rawComponent,
  concept,
  subject,
  conceptDecision,
  componentDecision,
  rules,
  isPrimaryComponent,
) {
  const component = {
    ...rawComponent,
    role: componentDecision?.role || rawComponent.role,
  };
  let inferredLanguage = inferredLanguageForComponent(
    component,
    concept,
    subject,
  );
  let effectiveLanguage = inferredLanguage;
  let languageSource = [
    "text-evidence",
    "conflict",
  ].includes(inferredLanguage.confidence)
    ? inferredLanguage.confidence
    : inferredLanguage.confidence === "convention"
      ? "convention"
    : "inference";
  let matchedRule = null;
  let decision = componentDecision || null;

  const inheritedConceptLanguage = (
    isPrimaryComponent &&
    conceptDecision &&
    Object.prototype.hasOwnProperty.call(conceptDecision, "language")
  )
    ? conceptDecision.language
    : "";
  const decidedLanguage = componentDecision &&
    Object.prototype.hasOwnProperty.call(componentDecision, "language")
    ? componentDecision.language
    : inheritedConceptLanguage;

  if (decidedLanguage) {
    effectiveLanguage = languageResult(
      familyForLanguage(decidedLanguage),
      decidedLanguage,
      "decided",
      componentDecision?.notes ||
        conceptDecision?.notes ||
        "Human catalog decision",
    );
    languageSource = "decision";
  } else if (
    !["text-evidence", "conflict"].includes(inferredLanguage.confidence) &&
    CORPUS_COMPONENT_ROLES.has(component.role)
  ) {
    matchedRule = firstMatchingRule(
      rules,
      subject,
      concept,
      inferredLanguage,
      component,
    );
    if (matchedRule) {
      effectiveLanguage = languageResult(
        familyForLanguage(matchedRule.language),
        matchedRule.language,
        "rule",
        `catalog rule: ${matchedRule.label || matchedRule.id}`,
      );
      languageSource = "rule";
    }
  }

  let status;
  if (languageSource === "decision") {
    if (effectiveLanguage.language === "Unknown") status = "reviewed-unknown";
    else if (effectiveLanguage.language === inferredLanguage.language) {
      status = "confirmed";
    } else status = "overridden";
  } else if (languageSource === "rule") status = "rule";
  else if (languageSource === "text-evidence") status = "text-evidence";
  else if (languageSource === "conflict") status = "conflict";
  else if (languageSource === "convention") status = "convention";
  else if (effectiveLanguage.confidence === "structural") status = "structural";
  else if (effectiveLanguage.language === "Unknown") status = "unknown";
  else status = "inferred";

  const corpusSetting = componentDecision?.corpus || "auto";
  const automaticCorpusEligibility =
    CORPUS_COMPONENT_ROLES.has(component.role) &&
    !["Trade", "Unknown", "Special"].includes(effectiveLanguage.family) &&
    component.rendering !== "trade";
  const corpusEligible = corpusSetting === "include" ||
    (corpusSetting !== "exclude" && automaticCorpusEligibility);

  return {
    ...component,
    subjectPath: subject.path,
    subjectName: subject.name,
    noteType: subject.noteType,
    subtypes: subject.subtypes,
    subtypeLabel: subject.subtypeLabel,
    subtypeSource: subject.subtypeSource,
    needsNameReview: subject.needsNameReview,
    nameReviewReasons: subject.nameReviewReasons,
    conceptId: concept.id,
    displayName: concept.preferredForm,
    conceptRole: concept.role,
    inferredLanguage,
    effectiveLanguage,
    languageSource,
    status,
    matchedRuleId: matchedRule?.id || null,
    decision,
    corpusSetting,
    corpusEligible,
    notes: componentDecision?.notes || "",
  };
}

function languageSummary(components) {
  const labels = [];
  for (const component of components) {
    const { family, language } = component.effectiveLanguage;
    if (language === "Language-neutral") continue;
    const label = family === "Trade" ? "Trade" : language;
    if (!labels.includes(label)) labels.push(label);
  }
  return labels.join(" + ") || "Language-neutral";
}

function buildCatalog(subjects, records, options = {}) {
  const normalizedRecords = normalizeStoreRecords(records);
  const rules = normalizedRecords.filter((record) => record.type === "rule");
  const conceptDecisionMap = new Map();
  const formDecisionMap = new Map();
  const componentDecisionMap = new Map();
  for (const record of normalizedRecords) {
    if (record.type === "concept") {
      conceptDecisionMap.set(conceptDecisionKey(record.subject, record.concept), record);
    } else if (record.type === "form") {
      formDecisionMap.set(formDecisionKey(record.subject, record.form), record);
    } else if (record.type === "component") {
      componentDecisionMap.set(
        componentDecisionKey(
          record.subject,
          record.concept,
          record.component,
        ),
        record,
      );
    }
  }

  const concepts = [];
  const components = [];
  const subjectsWithConcepts = [];
  const scopedSubjects = (subjects || []).filter((subject) =>
    NOTE_TYPES.includes(subject.noteType)
  );
  for (const rawSubject of scopedSubjects) {
    const nameInfo = provisionalNameInfo(
      rawSubject.rawName || rawSubject.name || rawSubject.fileName,
    );
    const subtypeInfo = toStrings(rawSubject.subtypes).length
      ? {
          values: toStrings(rawSubject.subtypes),
          label: rawSubject.subtypeLabel ||
            toStrings(rawSubject.subtypes).join(" · "),
          source: rawSubject.subtypeSource || "",
        }
      : subtypeForSubject(rawSubject.noteType, rawSubject);
    const subject = {
      ...rawSubject,
      rawName: rawSubject.rawName || rawSubject.name || rawSubject.fileName,
      name: nameInfo.text,
      provisionalName: rawSubject.provisionalName || nameInfo.provisional,
      subtypes: subtypeInfo.values,
      subtypeLabel: subtypeInfo.label,
      subtypeSource: subtypeInfo.source,
      ...nameReviewForSubject({
        ...rawSubject,
        provisionalName: rawSubject.provisionalName || nameInfo.provisional,
      }),
    };
    const rawConcepts = buildConcepts(subject, formDecisionMap);
    const decorated = rawConcepts.map((concept) => {
      const conceptDecision = conceptDecisionMap.get(
        conceptDecisionKey(subject.path, concept.id),
      );
      const forms = concept.forms.map((form) => ({
        ...form,
        components: decomposeDisplayName(form.text, subject),
      }));
      const preferredComponents = decomposeDisplayName(
        concept.preferredForm,
        subject,
      ).map((component) => ({
        ...component,
        preferredFormComponent: true,
        observedIn: [concept.preferredForm],
      }));
      const rawComponents = [...preferredComponents];
      const componentByShape = new Map(
        rawComponents.map((component) => [
          `${component.role}\u0000${normalizeLoose(component.text)}`,
          component,
        ]),
      );
      for (const form of forms) {
        for (const component of form.components) {
          const shape = `${component.role}\u0000${normalizeLoose(component.text)}`;
          if (componentByShape.has(shape)) {
            const existing = componentByShape.get(shape);
            if (!existing.observedIn.includes(form.text)) {
              existing.observedIn.push(form.text);
            }
            continue;
          }
          // Grouped short and orthographic forms should not create duplicate
          // lexical corpus entries. They may still contribute a title,
          // epithet, classifier, or other structural component.
          if (CORPUS_COMPONENT_ROLES.has(component.role)) continue;
          const observed = {
            ...component,
            preferredFormComponent: false,
            observedIn: [form.text],
          };
          componentByShape.set(shape, observed);
          rawComponents.push(observed);
        }
      }
      if (concept.role === "primary") {
        for (const rawTitle of toStrings(subject.title)) {
          const titleText = cleanAlias(rawTitle);
          if (!plausibleName(titleText)) continue;
          const titleComponent = makeComponents([{
            text: titleText,
            role: "title",
            rendering: titleRendering(titleText),
          }])[0];
          if (!titleComponent) continue;
          const shape =
            `${titleComponent.role}\u0000${normalizeLoose(titleComponent.text)}`;
          if (componentByShape.has(shape)) {
            const existing = componentByShape.get(shape);
            if (!existing.observedIn.includes("frontmatter:title")) {
              existing.observedIn.push("frontmatter:title");
            }
            continue;
          }
          const observed = {
            ...titleComponent,
            preferredFormComponent: false,
            observedIn: ["frontmatter:title"],
          };
          componentByShape.set(shape, observed);
          rawComponents.push(observed);
        }
      }
      const primaryIndex = Math.max(
        0,
        preferredComponents.findIndex((component) =>
          CORPUS_COMPONENT_ROLES.has(component.role)
        ),
      );
      const decoratedComponents = rawComponents.map((component, index) => {
        const componentDecision = componentDecisionMap.get(
          componentDecisionKey(subject.path, concept.id, component.id),
        );
        const result = decorateComponent(
          component,
          concept,
          subject,
          conceptDecision,
          componentDecision,
          rules,
          index === primaryIndex,
        );
        components.push(result);
        return result;
      });
      const primaryComponent = decoratedComponents[primaryIndex] ||
        decoratedComponents[0];
      const conventionalUnattestedTranslation =
        !conceptDecision?.derivation &&
        concept.role === "primary" &&
        subject.noteType === "place" &&
        primaryComponent?.effectiveLanguage.family === "Trade" &&
        primaryComponent?.role === "descriptive";
      const result = {
        ...concept,
        forms,
        subject,
        components: decoratedComponents,
        inferredLanguage: primaryComponent?.inferredLanguage ||
          { ...UNKNOWN_LANGUAGE },
        effectiveLanguage: primaryComponent?.effectiveLanguage ||
          { ...UNKNOWN_LANGUAGE },
        languageSource: primaryComponent?.languageSource || "inference",
        status: primaryComponent?.status || "unknown",
        needsNameReview: subject.needsNameReview,
        nameReviewReasons: subject.nameReviewReasons,
        matchedRuleId: primaryComponent?.matchedRuleId || null,
        decision: conceptDecision || null,
        relationship: conceptDecision?.relationship || "",
        derivation: conceptDecision?.derivation ||
          (conventionalUnattestedTranslation
            ? "unattested-translation"
            : ""),
        derivationSource: conceptDecision?.derivation
          ? "decision"
          : conventionalUnattestedTranslation
            ? "convention"
            : "",
        usage: conceptDecision?.usage || "",
        community: conceptDecision?.community || "",
        sourceLanguage: conceptDecision?.sourceLanguage || "",
        sourceForm: conceptDecision?.sourceForm ||
          (conventionalUnattestedTranslation ? "unattested" : ""),
        decisionNotes: conceptDecision?.notes || "",
        languageSummary: languageSummary(decoratedComponents),
        corpusComponents: decoratedComponents.filter(
          (component) => component.corpusEligible,
        ),
      };
      result.kindLabel = kindLabel(result);
      concepts.push(result);
      return result;
    });
    subjectsWithConcepts.push({ ...subject, concepts: decorated });
  }

  concepts.sort((left, right) =>
    left.effectiveLanguage.family.localeCompare(right.effectiveLanguage.family) ||
    left.effectiveLanguage.language.localeCompare(right.effectiveLanguage.language) ||
    left.preferredForm.localeCompare(right.preferredForm) ||
    left.subjectPath.localeCompare(right.subjectPath)
  );

  const catalog = {
    subjects: subjectsWithConcepts,
    concepts,
    components,
    corpus: components.filter((component) => component.corpusEligible),
    rules,
    records: normalizedRecords,
    knownSubjectPaths: new Set([
      ...(options.knownSubjectPaths || []),
      ...(subjects || []).map((subject) => subject.path),
    ]),
  };
  catalog.orphans = findOrphans(catalog);
  return catalog;
}

function findOrphans(catalog) {
  const subjectMap = new Map(
    catalog.subjects.map((subject) => [subject.path, subject]),
  );
  const conceptKeys = new Set(
    catalog.concepts.map((concept) => conceptDecisionKey(concept.subjectPath, concept.id)),
  );
  const componentKeys = new Set(
    catalog.components.map((component) =>
      componentDecisionKey(
        component.subjectPath,
        component.conceptId,
        component.id,
      )
    ),
  );
  const formKeys = new Set();
  for (const subject of catalog.subjects) {
    for (const form of mergeObservedForms(subject)) {
      formKeys.add(formDecisionKey(subject.path, form.text));
    }
  }

  const output = [];
  for (const record of catalog.records) {
    if (record.type === "rule") continue;
    if (!subjectMap.has(record.subject)) {
      // Decisions for note types outside the current five-type catalog remain
      // dormant rather than appearing as orphans.
      if (!catalog.knownSubjectPaths.has(record.subject)) {
        output.push({ record, reason: "Subject file is missing" });
      }
    } else if (
      record.type === "concept" &&
      !conceptKeys.has(conceptDecisionKey(record.subject, record.concept))
    ) {
      output.push({ record, reason: "Name concept no longer exists" });
    } else if (
      record.type === "form" &&
      !formKeys.has(formDecisionKey(record.subject, record.form))
    ) {
      output.push({ record, reason: "Observed form no longer exists" });
    } else if (
      record.type === "component" &&
      !componentKeys.has(
        componentDecisionKey(
          record.subject,
          record.concept,
          record.component,
        ),
      )
    ) {
      output.push({ record, reason: "Name component no longer exists" });
    }
  }
  return output;
}

function chooseNoteType(tags) {
  const normalized = toStrings(tags).map((tag) =>
    String(tag).replace(/^#/, "").toLocaleLowerCase("en"),
  );
  const bases = new Set(normalized.map((tag) => tag.split("/", 1)[0]));
  for (const noteType of NOTE_TYPES) {
    if (normalized.includes(noteType) || bases.has(noteType)) return noteType;
  }
  return "unknown";
}

function shouldScanPath(path) {
  const parts = String(path || "").split("/");
  if (parts[0] === "Worldbuilding") return false;
  return !parts.slice(0, -1).some(
    (part) => part.startsWith("_") || part.startsWith("."),
  );
}

function parseDecisionStore(text) {
  const records = [];
  String(text || "").split(/\r?\n/).forEach((line, index) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) return;
    let record;
    try {
      record = JSON.parse(trimmed);
    } catch (error) {
      throw new Error(`Invalid JSON on decision-store line ${index + 1}: ${error.message}`);
    }
    if (
      !record ||
      !["concept", "component", "form", "rule"].includes(record.type)
    ) {
      throw new Error(`Invalid record type on decision-store line ${index + 1}`);
    }
    records.push(record);
  });
  return normalizeStoreRecords(records);
}

function recordIdentity(record) {
  if (record.type === "rule") return `rule\u0000${record.id}`;
  if (record.type === "concept") {
    return `concept\u0000${record.subject}\u0000${record.concept}`;
  }
  if (record.type === "component") {
    return `component\u0000${record.subject}\u0000${record.concept}\u0000${record.component}`;
  }
  if (record.type === "form") {
    return `form\u0000${record.subject}\u0000${normalizeStrict(record.form)}`;
  }
  return JSON.stringify(record);
}

function normalizeStoreRecords(records) {
  const byIdentity = new Map();
  for (const record of records || []) {
    if (!record || !record.type) continue;
    byIdentity.set(recordIdentity(record), { ...record });
  }
  return [...byIdentity.values()];
}

function serializeDecisionStore(records) {
  const order = { rule: 0, concept: 1, component: 2, form: 3 };
  const normalized = normalizeStoreRecords(records).sort((left, right) =>
    (order[left.type] ?? 9) - (order[right.type] ?? 9) ||
    String(left.subject || "").localeCompare(String(right.subject || "")) ||
    String(left.component || left.concept || left.form || left.id || "").localeCompare(
      String(right.component || right.concept || right.form || right.id || ""),
    )
  );
  return normalized.map((record) => JSON.stringify(record)).join("\n") +
    (normalized.length ? "\n" : "");
}

function upsertStoreRecord(records, nextRecord) {
  const identity = recordIdentity(nextRecord);
  return [
    ...normalizeStoreRecords(records).filter(
      (record) => recordIdentity(record) !== identity,
    ),
    nextRecord,
  ];
}

function removeStoreRecord(records, targetRecord) {
  const identity = recordIdentity(targetRecord);
  return normalizeStoreRecords(records).filter(
    (record) => recordIdentity(record) !== identity,
  );
}

function catalogExportRecords(catalog) {
  return catalog.concepts.map((concept) => ({
    subject: concept.subjectPath,
    subject_name: concept.subjectName,
    note_type: concept.subject.noteType,
    subtypes: concept.subject.subtypes,
    subtype_label: concept.subject.subtypeLabel,
    subtype_source: concept.subject.subtypeSource,
    preferred_form: concept.preferredForm,
    normalized: concept.normalized,
    role: concept.role,
    language_summary: concept.languageSummary,
    language: {
      effective: concept.effectiveLanguage.language,
      family: concept.effectiveLanguage.family,
      inferred: concept.inferredLanguage.language,
      source: concept.languageSource,
      status: concept.status,
      basis: concept.effectiveLanguage.basis,
    },
    name_review: {
      needed: concept.needsNameReview,
      reasons: concept.nameReviewReasons,
    },
    kind: {
      relationship: concept.relationship || null,
      derivation: concept.derivation || null,
      derivation_source: concept.derivationSource || null,
      usage: concept.usage || null,
      community: concept.community || null,
      source_language: concept.sourceLanguage || null,
      source_form: concept.sourceForm || null,
    },
    components: concept.components.map((component) => ({
      id: component.id,
      text: component.text,
      role: component.role,
      rendering: component.rendering,
      reference: component.reference || null,
      language: component.effectiveLanguage.language,
      language_family: component.effectiveLanguage.family,
      language_source: component.languageSource,
      status: component.status,
      corpus_eligible: component.corpusEligible,
      corpus_setting: component.corpusSetting,
      basis: component.effectiveLanguage.basis,
    })),
    forms: concept.forms.map((form) => ({
      text: form.text,
      variant_kind: form.variantKind,
      sources: form.sources,
      automatic: form.automatic,
      components: form.components.map((component) => ({
        text: component.text,
        role: component.role,
        rendering: component.rendering,
      })),
    })),
    pronunciation: concept.subject.pronunciation || "",
    tags: concept.subject.tags,
  }));
}

function parsePlaceEvidenceStore(text) {
  const records = [];
  let metadata = null;
  String(text || "").split(/\r?\n/).forEach((line, index) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) return;
    let record;
    try {
      record = JSON.parse(trimmed);
    } catch (error) {
      throw new Error(`Invalid JSON on place-evidence line ${index + 1}: ${error.message}`);
    }
    if (record?.record_type === "meta") {
      metadata = record;
      return;
    }
    if (
      !record ||
      record.record_type !== "place-name-evidence" ||
      typeof record.subject !== "string" ||
      !record.subject
    ) {
      throw new Error(`Invalid place-evidence record on line ${index + 1}`);
    }
    records.push(record);
  });
  return {
    metadata,
    records,
    bySubject: new Map(records.map((record) => [record.subject, record])),
  };
}

function attachPlaceEvidence(catalog, evidenceStore) {
  const store = evidenceStore?.bySubject instanceof Map
    ? evidenceStore
    : parsePlaceEvidenceStore("");
  for (const subject of catalog.subjects || []) {
    subject.placeEvidence = store.bySubject.get(subject.path) || null;
  }
  for (const concept of catalog.concepts || []) {
    concept.placeEvidence = store.bySubject.get(concept.subjectPath) || null;
  }
  catalog.placeEvidence = store;
  return catalog;
}

function toStrings(value) {
  if (value == null) return [];
  if (Array.isArray(value)) {
    return value.flatMap((item) => toStrings(item));
  }
  if (typeof value === "object") {
    if (typeof value.path === "string") return [value.path];
    if (typeof value.location === "string") return [value.location];
    return Object.values(value).flatMap((item) => toStrings(item));
  }
  const text = String(value).trim();
  return text ? [text] : [];
}

function capitalize(value) {
  const text = String(value || "");
  return text ? text[0].toUpperCase() + text.slice(1) : "";
}

function escapeRegExp(value) {
  return String(value || "").replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

module.exports = {
  NOTE_TYPES,
  COMPONENT_ROLES,
  LANGUAGE_DEFINITIONS,
  VARIANT_KINDS,
  UNKNOWN_LANGUAGE,
  familyForLanguage,
  normalizeTypography,
  normalizeStrict,
  normalizeLoose,
  provisionalNameInfo,
  nameReviewForSubject,
  subtypeForSubject,
  subtypeChoices,
  cleanAlias,
  plausibleName,
  classifyVariant,
  extractTextAliases,
  explicitLanguageForName,
  looksCommon,
  transparentTradePhrase,
  inferPrimaryLanguage,
  inferConceptLanguage,
  conceptIdForForm,
  formDecisionKey,
  conceptDecisionKey,
  componentDecisionKey,
  mergeObservedForms,
  buildConcepts,
  decomposeDisplayName,
  ruleMatches,
  buildCatalog,
  kindLabel,
  chooseNoteType,
  shouldScanPath,
  parseDecisionStore,
  serializeDecisionStore,
  recordIdentity,
  normalizeStoreRecords,
  upsertStoreRecord,
  removeStoreRecord,
  catalogExportRecords,
  parsePlaceEvidenceStore,
  attachPlaceEvidence,
  toStrings,
};

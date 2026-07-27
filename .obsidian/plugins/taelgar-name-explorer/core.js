"use strict";

const NOTE_TYPES = [
  "person",
  "power",
  "place",
  "event",
  "object",
  "group",
  "ancestry",
  "creature",
  "session-note",
  "source",
  "background",
  "meta",
];

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
  ["Unclassified", "Svolhasian"],
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

const HONORIFICS = [
  "archfey", "baroness", "baron", "captain", "chiefling", "chief", "commander",
  "countess", "count", "duchess", "duke", "elder", "emperor", "empress",
  "general", "grandpa", "hakeasa", "high king", "king", "lady", "laivan",
  "loremaster", "lord", "magistros", "marshal", "master", "prince",
  "princess", "proconsul", "queen", "saint", "samraat", "sergeant", "sir",
];

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

function languageFromNamingContext(context, name, basis) {
  const contextWithoutName = String(context || "").replace(
    new RegExp(escapeRegExp(name), "gi"),
    " ",
  );
  const lowered = contextWithoutName
    .toLocaleLowerCase("en")
    .replace(/\[\[|\]\]/g, " ");
  for (const [keywords, family, language] of LANGUAGE_KEYWORDS) {
    for (const rawKeyword of keywords) {
      const keyword = rawKeyword.trim();
      const escaped = escapeRegExp(keyword);
      const patterns = [
        new RegExp(`\\bin\\s+(?:the\\s+)?${escaped}\\b`, "i"),
        new RegExp(`\\b${escaped}\\b[^.;:]{0,35}\\b(?:name|term|phrase|word|exonym|endonym|translation)\\b`, "i"),
        new RegExp(`\\b(?:name|term|phrase|word|exonym|endonym|translation)\\b[^.;:]{0,55}\\b${escaped}\\b`, "i"),
      ];
      if (patterns.some((pattern) => pattern.test(lowered))) {
        return languageResult(family, language, "explicit", basis);
      }
    }
  }
  return null;
}

function explicitLanguageForName(body, name, label) {
  const needle = normalizeLoose(name);
  if (!needle) return null;
  const namingWords = /\b(?:name|called|known|rendered|translated|translation|term|phrase|word|exonym|endonym|in\s+common|locally)\b/i;
  const candidates = [];
  let inComment = false;
  let inNamesSection = false;

  String(body || "").split(/\r?\n/).forEach((line, index) => {
    const stripped = line.trim();
    if (/^##\s+Names?\s*$/i.test(stripped)) inNamesSection = true;
    else if (inNamesSection && /^##\s+/.test(stripped)) inNamesSection = false;

    const markerCount = (line.match(/%%/g) || []).length;
    const lineIsComment = inComment || markerCount > 0;
    if (normalizeLoose(line).includes(needle) && namingWords.test(line)) {
      const suffix = lineIsComment ? " (comment)" : "";
      const explicit = languageFromNamingContext(
        line,
        name,
        `${label}, body line ${index + 1}${suffix}`,
      );
      if (explicit) {
        let score = 0;
        if (/\bin\s+(?:the\s+)?common\b/i.test(line)) score += 8;
        if (inNamesSection) score += 5;
        if (/\b(?:name|term|phrase|word|exonym|endonym|translation)\b/i.test(line)) score += 4;
        if (/\b(?:called|known)\b/i.test(line)) score += 2;
        if (lineIsComment) score -= 1;
        candidates.push([score, explicit]);
      }
    }
    if (markerCount % 2) inComment = !inComment;
  });

  candidates.sort((left, right) => right[0] - left[0]);
  return candidates.length ? candidates[0][1] : null;
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
    "explicit primary-name text",
  );
  if (explicit) return explicit;

  if (subject.noteType !== "person" && looksCommon(subject.name)) {
    return languageResult(
      "Trade",
      "Common",
      "inferred",
      "descriptive or translated Common-form name",
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

  if (looksCommon(subject.name)) {
    return languageResult(
      "Trade",
      "Common",
      "inferred",
      "descriptive or translated Common-form name",
    );
  }
  return { ...UNKNOWN_LANGUAGE };
}

function inferConceptLanguage(concept, subject, primaryLanguage) {
  if (concept.role === "primary") return primaryLanguage;
  const explicit = explicitLanguageForName(
    subject.body,
    concept.preferredForm,
    "explicit alternate-name text",
  );
  if (explicit) return explicit;
  if (looksCommon(concept.preferredForm)) {
    return languageResult(
      "Trade",
      "Common",
      "inferred",
      "descriptive or translated Common-form name",
    );
  }
  if (primaryLanguage.language !== "Unknown") {
    return languageResult(
      primaryLanguage.family,
      primaryLanguage.language,
      "inferred",
      "same-subject naming context; alternate-name language is not explicit",
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
  const candidates = [
    { text: subject.name, source: "primary" },
    ...toStrings(subject.aliases).map((text) => ({ text, source: "frontmatter" })),
    ...(subject.textAliases || []),
  ];
  if (subject.heading) candidates.push({ text: subject.heading, source: "heading" });

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

    // A differing H1 is presentation evidence, not automatically a distinct name.
    if (form.sources.every((source) => source === "heading")) continue;
    concepts.push(makeConcept(subject, form, form.sources.includes("text") ? "text" : "alias"));
  }
  return concepts;
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

function ruleMatches(rule, subject, concept, inferredLanguage) {
  if (rule.enabled === false) return false;
  const match = rule.match || {};
  if (!valueMatches(subject.noteType, match.noteType)) return false;
  if (!valueMatches(subject.species, match.species)) return false;
  if (!valueMatches(subject.ancestry, match.ancestry)) return false;
  if (!valueMatches(concept.role, match.role)) return false;
  if (!valueMatches(inferredLanguage.language, match.inferredLanguage)) return false;
  if (match.folder && !subject.path.toLocaleLowerCase("en").startsWith(
    String(match.folder).toLocaleLowerCase("en"),
  )) return false;
  return true;
}

function firstMatchingRule(rules, subject, concept, inferredLanguage) {
  return [...rules]
    .filter((rule) => rule.type === "rule")
    .sort((left, right) => {
      const priority = Number(right.priority || 0) - Number(left.priority || 0);
      return priority || String(left.id).localeCompare(String(right.id));
    })
    .find((rule) => ruleMatches(rule, subject, concept, inferredLanguage));
}

function decorateConcept(concept, subject, inferredLanguage, conceptDecision, rules) {
  let effective = inferredLanguage;
  let languageSource = inferredLanguage.confidence === "explicit" ? "explicit" : "inference";
  let matchedRule = null;

  if (conceptDecision && Object.prototype.hasOwnProperty.call(conceptDecision, "language")) {
    effective = languageResult(
      familyForLanguage(conceptDecision.language),
      conceptDecision.language,
      "decided",
      conceptDecision.notes || "Human catalog decision",
    );
    languageSource = "decision";
  } else if (inferredLanguage.confidence !== "explicit") {
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
  else if (languageSource === "explicit") status = "explicit";
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
    labels.push(concept.derivation === "translation" ? "translated" : concept.derivation);
  }
  if (concept.relationship) labels.push(concept.relationship);
  return labels.join(" ") || "—";
}

function buildCatalog(subjects, records) {
  const normalizedRecords = normalizeStoreRecords(records);
  const rules = normalizedRecords.filter((record) => record.type === "rule");
  const conceptDecisionMap = new Map();
  const formDecisionMap = new Map();
  for (const record of normalizedRecords) {
    if (record.type === "concept") {
      conceptDecisionMap.set(conceptDecisionKey(record.subject, record.concept), record);
    } else if (record.type === "form") {
      formDecisionMap.set(formDecisionKey(record.subject, record.form), record);
    }
  }

  const concepts = [];
  const subjectsWithConcepts = [];
  for (const subject of subjects) {
    const rawConcepts = buildConcepts(subject, formDecisionMap);
    const primaryLanguage = inferPrimaryLanguage(subject);
    const decorated = rawConcepts.map((concept) => {
      const inferred = inferConceptLanguage(concept, subject, primaryLanguage);
      const decision = conceptDecisionMap.get(
        conceptDecisionKey(subject.path, concept.id),
      );
      const result = decorateConcept(concept, subject, inferred, decision, rules);
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
    rules,
    records: normalizedRecords,
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
      output.push({ record, reason: "Subject file is missing or excluded" });
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
    if (!record || !["concept", "form", "rule"].includes(record.type)) {
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
  const order = { rule: 0, concept: 1, form: 2 };
  const normalized = normalizeStoreRecords(records).sort((left, right) =>
    (order[left.type] ?? 9) - (order[right.type] ?? 9) ||
    String(left.subject || "").localeCompare(String(right.subject || "")) ||
    String(left.concept || left.form || left.id || "").localeCompare(
      String(right.concept || right.form || right.id || ""),
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
    preferred_form: concept.preferredForm,
    normalized: concept.normalized,
    role: concept.role,
    language: {
      effective: concept.effectiveLanguage.language,
      family: concept.effectiveLanguage.family,
      inferred: concept.inferredLanguage.language,
      source: concept.languageSource,
      status: concept.status,
      basis: concept.effectiveLanguage.basis,
    },
    kind: {
      relationship: concept.relationship || null,
      derivation: concept.derivation || null,
      usage: concept.usage || null,
      community: concept.community || null,
    },
    forms: concept.forms.map((form) => ({
      text: form.text,
      variant_kind: form.variantKind,
      sources: form.sources,
      automatic: form.automatic,
    })),
    pronunciation: concept.subject.pronunciation || "",
    tags: concept.subject.tags,
  }));
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
  LANGUAGE_DEFINITIONS,
  VARIANT_KINDS,
  UNKNOWN_LANGUAGE,
  familyForLanguage,
  normalizeTypography,
  normalizeStrict,
  normalizeLoose,
  cleanAlias,
  plausibleName,
  classifyVariant,
  extractTextAliases,
  explicitLanguageForName,
  looksCommon,
  inferPrimaryLanguage,
  inferConceptLanguage,
  conceptIdForForm,
  formDecisionKey,
  conceptDecisionKey,
  mergeObservedForms,
  buildConcepts,
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
  toStrings,
};

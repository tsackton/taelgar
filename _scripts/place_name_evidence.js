"use strict";

const crypto = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");

const nameCore = require("../.obsidian/plugins/taelgar-name-explorer/core.js");

const SCHEMA_VERSION = 1;
const MAX_EVIDENCE_EXAMPLES = 12;
const WIKILINK_RE = /(!?)\[\[([^\]\n]+)\]\]/g;
const HEADING_RE = /^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$/;
const TRANSCRIPT_LINE_RE = /^\[(u\d+)(?:\s*\|[^\]]*?\|\s*([^\]]+))?\]\s*(.*)$/u;
const PRIMARY_GRAPH_EXCLUSIONS = new Set([
  "session-processing",
  "support",
  "template",
  "generated",
]);

const CANON_TOP_LEVEL = new Set([
  "Background",
  "Cosmology",
  "Creatures",
  "Events",
  "Gazetteer",
  "Gods and Religions",
  "Groups",
  "History",
  "People",
  "Things",
]);

function normalizeSlashes(value) {
  return String(value || "").replace(/\\/g, "/");
}

function relativePath(root, absolute) {
  return normalizeSlashes(path.relative(root, absolute));
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

function normalizeExact(value) {
  return normalizeTypography(value).toLocaleLowerCase("en");
}

function normalizeKey(value) {
  return normalizeExact(value)
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizePathKey(value) {
  let output = normalizeSlashes(value).trim().replace(/^\.\//, "");
  if (output.toLocaleLowerCase("en").endsWith(".md")) output = output.slice(0, -3);
  return normalizeKey(output);
}

function sha256(text) {
  return crypto.createHash("sha256").update(String(text || ""), "utf8").digest("hex");
}

function walkFiles(root, predicate = () => true) {
  const output = [];
  const visit = (directory) => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      if (entry.name === ".git" || entry.name === ".backups") continue;
      const absolute = path.join(directory, entry.name);
      if (entry.isDirectory()) visit(absolute);
      else if (entry.isFile() && predicate(absolute)) output.push(absolute);
    }
  };
  visit(root);
  return output.sort((left, right) => left.localeCompare(right));
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

function splitFrontmatter(text) {
  const lines = String(text || "").split(/\r?\n/);
  if (lines[0]?.replace(/^\uFEFF/, "").trim() !== "---") {
    return { lines: [], body: String(text || ""), bodyStart: 0 };
  }
  const end = lines.findIndex((line, index) => index > 0 && line.trim() === "---");
  if (end < 0) return { lines: [], body: String(text || ""), bodyStart: 0 };
  return {
    lines: lines.slice(1, end),
    body: lines.slice(end + 1).join("\n"),
    bodyStart: end + 1,
  };
}

function parseFrontmatter(lines) {
  const fields = {};
  for (let index = 0; index < lines.length; index += 1) {
    const match = lines[index].match(/^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$/);
    if (!match) continue;
    const key = match[1];
    const inline = (match[2] || "").trim();
    if (inline) {
      fields[key] = inline.startsWith("[") && inline.endsWith("]")
        ? splitInlineList(inline)
        : stripQuotes(inline);
      continue;
    }
    const values = [];
    for (let childIndex = index + 1; childIndex < lines.length; childIndex += 1) {
      const child = lines[childIndex];
      if (/^[A-Za-z][A-Za-z0-9_-]*:/.test(child)) break;
      const item = child.match(/^\s*-\s+(.+)$/);
      if (item) values.push(stripQuotes(item[1]));
    }
    fields[key] = values;
  }
  return fields;
}

function fieldStrings(fields, key) {
  const value = fields[key];
  if (value == null) return [];
  if (Array.isArray(value)) return value.map(stripQuotes).filter(Boolean);
  const text = stripQuotes(value);
  return text ? [text] : [];
}

function fieldScalar(fields, key) {
  return fieldStrings(fields, key)[0] || "";
}

function parseTopLevelScalars(text) {
  const output = {};
  for (const line of String(text || "").split(/\r?\n/)) {
    const match = line.match(/^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$/);
    if (!match) continue;
    const value = stripQuotes((match[2] || "").trim());
    if (value && !["null", "~"].includes(value.toLocaleLowerCase("en"))) {
      output[match[1]] = value;
    }
  }
  return output;
}

function parseInlineMap(text) {
  const source = String(text || "").trim().replace(/^\{/, "").replace(/\}$/, "");
  const output = {};
  for (const part of splitInlineList(`[${source}]`)) {
    const match = part.match(/^\s*([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$/);
    if (match) output[match[1]] = stripQuotes(match[2]);
  }
  return output;
}

function parseCampaignInfo(frontmatterLines) {
  const start = frontmatterLines.findIndex((line) => /^campaignInfo\s*:/.test(line));
  if (start < 0) return [];
  const header = frontmatterLines[start];
  const inline = header.slice(header.indexOf(":") + 1).trim();
  if (inline.startsWith("[") && inline.endsWith("]")) {
    const maps = inline.match(/\{[^{}]*\}/g) || [];
    return maps.map(parseInlineMap).filter((entry) => entry.campaign);
  }
  const records = [];
  let current = null;
  for (let index = start + 1; index < frontmatterLines.length; index += 1) {
    const line = frontmatterLines[index];
    if (/^[A-Za-z][A-Za-z0-9_-]*:/.test(line)) break;
    const inlineItem = line.match(/^\s*-\s*(\{.*\})\s*$/);
    if (inlineItem) {
      records.push(parseInlineMap(inlineItem[1]));
      current = null;
      continue;
    }
    const first = line.match(/^\s*-\s*([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$/);
    if (first) {
      current = { [first[1]]: stripQuotes(first[2]) };
      records.push(current);
      continue;
    }
    const child = line.match(/^\s+([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*?)\s*$/);
    if (child && current) current[child[1]] = stripQuotes(child[2]);
  }
  return records.filter((entry) => entry.campaign);
}

function parseReferenceValues(frontmatterLines) {
  const references = [];
  const simpleFields = new Set(["whereabouts", "partOf"]);
  for (let index = 0; index < frontmatterLines.length; index += 1) {
    const match = frontmatterLines[index].match(/^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$/);
    if (!match) continue;
    const key = match[1];
    if (![...simpleFields, "affiliations"].includes(key)) continue;
    const inline = (match[2] || "").trim();
    if (inline && !inline.startsWith("[") && !inline.startsWith("{")) {
      references.push({ field: key, value: stripQuotes(inline) });
    }
    const block = [];
    for (let childIndex = index + 1; childIndex < frontmatterLines.length; childIndex += 1) {
      const child = frontmatterLines[childIndex];
      if (/^[A-Za-z][A-Za-z0-9_-]*:/.test(child)) break;
      block.push(child);
    }
    const combined = [inline, ...block].join("\n");
    for (const nested of combined.matchAll(/\b(?:location|org|place)\s*:\s*["']?([^,}\]\n"']+)/g)) {
      references.push({ field: key, value: nested[1].trim() });
    }
    if (simpleFields.has(key)) {
      for (const child of block) {
        const item = child.match(/^\s*-\s+([^:{][^\n]*)$/);
        if (item) references.push({ field: key, value: stripQuotes(item[1]) });
      }
    }
  }
  const seen = new Set();
  return references.filter((reference) => {
    const key = `${reference.field}\u0000${normalizeKey(reference.value)}`;
    if (!reference.value || seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

function loadIgnoreFilters(root) {
  const configPath = path.join(root, ".obsidian", "app.json");
  if (!fs.existsSync(configPath)) return [];
  try {
    const payload = JSON.parse(fs.readFileSync(configPath, "utf8"));
    return (payload.userIgnoreFilters || []).filter((value) => typeof value === "string");
  } catch (_error) {
    return [];
  }
}

function indexedMarkdown(relative, ignoreFilters = []) {
  const normalized = normalizeSlashes(relative);
  const parts = normalized.split("/");
  if (parts.some((part) => part === ".git" || part === ".backups")) return false;
  if (parts.some((part) => part.startsWith("."))) return false;
  return !ignoreFilters.some((filter) => {
    try {
      return new RegExp(filter).test(normalized);
    } catch (_error) {
      return normalized.includes(filter);
    }
  });
}

function sourceCategory(relative, publishedSessionPaths = new Set()) {
  const normalized = normalizeSlashes(relative);
  const parts = normalized.split("/");
  const top = parts[0];
  if (parts.includes("_generated")) return "generated";
  if (top === "_sessions") return "session-processing";
  if (publishedSessionPaths.has(normalized)) return "published-session";
  if (top === "Campaigns") return "campaign-material";
  if (top === "Primary Sources") return "primary-source";
  if (top === "Worldbuilding") return "worldbuilding";
  if (top === "_DM_" || top === "_dm_notes") return "dm-material";
  if (top === "_MoC" || top === "_scripts" || top === ".obsidian") return "support";
  if (top === "_templates") return "template";
  if (CANON_TOP_LEVEL.has(top)) return "canonical";
  return "other";
}

function contextualLines(text) {
  const lines = String(text || "").split(/\r?\n/);
  const frontmatter = splitFrontmatter(text);
  let inFence = false;
  let inComment = false;
  let campaignScope = "";
  let section = "";
  const output = [];
  for (let index = 0; index < lines.length; index += 1) {
    const original = lines[index];
    const lineNumber = index + 1;
    if (/^\s*(```|~~~)/.test(original)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;
    if (frontmatter.bodyStart && lineNumber <= frontmatter.bodyStart) {
      output.push({ line: lineNumber, text: original, context: "frontmatter", section, campaignScope });
      continue;
    }
    const campaignStart = original.match(/^\s*%%\^Campaign:([^%]+)%%\s*$/i);
    if (campaignStart) {
      campaignScope = campaignStart[1].trim();
      continue;
    }
    if (/^\s*%%\^End%%\s*$/i.test(original)) {
      campaignScope = "";
      continue;
    }
    const heading = original.match(HEADING_RE);
    if (heading && !inComment) section = heading[2].trim();

    let cursor = 0;
    let visible = "";
    let comment = "";
    while (cursor <= original.length) {
      const marker = original.indexOf("%%", cursor);
      if (marker < 0) {
        if (inComment) comment += original.slice(cursor);
        else visible += original.slice(cursor);
        break;
      }
      if (inComment) comment += original.slice(cursor, marker);
      else visible += original.slice(cursor, marker);
      inComment = !inComment;
      cursor = marker + 2;
    }
    if (visible.trim()) {
      output.push({ line: lineNumber, text: visible, context: "visible", section, campaignScope });
    }
    if (comment.trim()) {
      output.push({ line: lineNumber, text: comment, context: "comment", section, campaignScope });
    }
  }
  return output;
}

function fragmentBase(target) {
  return String(target || "").split(/[#^]/, 1)[0].trim();
}

function wikilinksInLine(line) {
  const output = [];
  WIKILINK_RE.lastIndex = 0;
  let match;
  while ((match = WIKILINK_RE.exec(String(line || ""))) !== null) {
    const inside = match[2];
    const parts = inside.split("|");
    const target = fragmentBase(parts[0].replace(/\\$/, "").trim());
    const display = parts.length > 1
      ? parts.slice(1).join("|").trim()
      : path.posix.basename(target.replace(/\.md$/i, ""));
    output.push({
      raw: match[0],
      embed: Boolean(match[1]),
      target,
      display,
      start: match.index,
      end: match.index + match[0].length,
    });
  }
  return output;
}

function markdownLinksInLine(line) {
  const output = [];
  const source = String(line || "");
  let position = 0;
  while (position < source.length) {
    const start = source.indexOf("[", position);
    if (start < 0) break;
    if (start > 0 && source[start - 1] === "!") {
      position = start + 1;
      continue;
    }
    const labelEnd = source.indexOf("]", start + 1);
    if (labelEnd < 0 || source[labelEnd + 1] !== "(") {
      position = start + 1;
      continue;
    }
    let cursor = labelEnd + 2;
    let depth = 1;
    while (cursor < source.length && depth) {
      if (source[cursor] === "(") depth += 1;
      else if (source[cursor] === ")") depth -= 1;
      cursor += 1;
    }
    if (depth) break;
    const destination = source.slice(labelEnd + 2, cursor - 1).trim();
    const pathMatch = destination.match(/^<?([^>\s]+\.md)(?:#[^>\s]+)?>?(?:\s+.*)?$/i);
    if (pathMatch) {
      output.push({
        raw: source.slice(start, cursor),
        label: source.slice(start + 1, labelEnd),
        destination: decodeURIComponent(pathMatch[1]),
        start,
        end: cursor,
      });
    }
    position = cursor;
  }
  return output;
}

function renderVisibleText(line) {
  let output = String(line || "");
  const markdown = markdownLinksInLine(output);
  for (const link of [...markdown].reverse()) {
    output = output.slice(0, link.start) + link.label + output.slice(link.end);
  }
  output = output.replace(WIKILINK_RE, (_raw, embed, inside) => {
    if (embed) return " ";
    const parts = inside.split("|");
    if (parts.length > 1) return parts.slice(1).join("|").trim();
    return path.posix.basename(fragmentBase(parts[0]).replace(/\.md$/i, ""));
  });
  return output.replace(/[*_`]/g, " ").replace(/\s+/g, " ").trim();
}

function createNoteIndex(root, ignoreFilters = loadIgnoreFilters(root)) {
  const files = walkFiles(root, (absolute) => absolute.endsWith(".md"));
  const notes = [];
  const byPath = new Map();
  const byStem = new Map();
  const byAlias = new Map();
  for (const absolute of files) {
    const relative = relativePath(root, absolute);
    if (!indexedMarkdown(relative, ignoreFilters)) continue;
    const text = fs.readFileSync(absolute, "utf8");
    const frontmatter = splitFrontmatter(text);
    const fields = parseFrontmatter(frontmatter.lines);
    const note = {
      absolute,
      path: relative,
      stem: path.basename(relative, ".md"),
      text,
      frontmatterLines: frontmatter.lines,
      fields,
      aliases: fieldStrings(fields, "aliases"),
    };
    notes.push(note);
    byPath.set(normalizePathKey(relative), note);
    const stemKey = normalizeKey(note.stem);
    if (!byStem.has(stemKey)) byStem.set(stemKey, []);
    byStem.get(stemKey).push(note);
    for (const alias of note.aliases) {
      const aliasKey = normalizeKey(alias);
      if (!byAlias.has(aliasKey)) byAlias.set(aliasKey, []);
      byAlias.get(aliasKey).push(note);
    }
  }

  const resolve = (target, sourcePath = "") => {
    const base = fragmentBase(target);
    if (!base) return { status: "missing", candidates: [] };
    const exact = byPath.get(normalizePathKey(base));
    if (exact) return { status: "resolved-path", note: exact, candidates: [exact] };
    if (base.includes("/")) {
      const suffix = notes.filter((note) =>
        normalizePathKey(note.path).endsWith(` ${normalizePathKey(base)}`) ||
        normalizePathKey(note.path) === normalizePathKey(base)
      );
      if (suffix.length === 1) return { status: "resolved-path", note: suffix[0], candidates: suffix };
      if (suffix.length > 1) return { status: "ambiguous", candidates: suffix };
    }
    const stemMatches = byStem.get(normalizeKey(path.posix.basename(base).replace(/\.md$/i, ""))) || [];
    if (stemMatches.length === 1) {
      return { status: "resolved-stem", note: stemMatches[0], candidates: stemMatches };
    }
    if (stemMatches.length > 1) {
      const sourceParts = normalizeSlashes(sourcePath).split("/").slice(0, -1);
      const ranked = stemMatches.map((note) => {
        const parts = note.path.split("/").slice(0, -1);
        let score = 0;
        while (score < sourceParts.length && score < parts.length && sourceParts[score] === parts[score]) score += 1;
        return { note, score };
      }).sort((left, right) => right.score - left.score || left.note.path.localeCompare(right.note.path));
      if (ranked.length === 1 || ranked[0].score > ranked[1].score) {
        return { status: "resolved-proximity", note: ranked[0].note, candidates: stemMatches };
      }
      return { status: "ambiguous", candidates: stemMatches };
    }
    const aliasMatches = byAlias.get(normalizeKey(base)) || [];
    if (aliasMatches.length === 1) {
      return { status: "resolved-alias", note: aliasMatches[0], candidates: aliasMatches };
    }
    if (aliasMatches.length > 1) return { status: "ambiguous", candidates: aliasMatches };
    return { status: "missing", candidates: [] };
  };

  const resolveMarkdown = (destination, sourcePath = "") => {
    const sourceDirectory = path.posix.dirname(normalizeSlashes(sourcePath));
    const local = path.posix.normalize(path.posix.join(sourceDirectory, destination));
    const localNote = byPath.get(normalizePathKey(local));
    if (localNote) return { status: "resolved-markdown-path", note: localNote, candidates: [localNote] };
    const rootNote = byPath.get(normalizePathKey(destination));
    if (rootNote) return { status: "resolved-markdown-path", note: rootNote, candidates: [rootNote] };
    return resolve(path.posix.basename(destination, ".md"), sourcePath);
  };

  return { notes, byPath, byStem, byAlias, resolve, resolveMarkdown };
}

function buildPlaceCatalog(index, root, options = {}) {
  const subjects = [];
  const placeNotes = new Map();
  for (const note of index.notes) {
    if (!note.path.startsWith("Gazetteer/")) continue;
    const tags = fieldStrings(note.fields, "tags").map((tag) =>
      tag.replace(/^#/, "").toLocaleLowerCase("en")
    );
    if (nameCore.chooseNoteType(tags) !== "place") continue;
    const rawName = fieldScalar(note.fields, "name") || note.stem;
    const nameInfo = nameCore.provisionalNameInfo(rawName);
    const subtypeInfo = nameCore.subtypeForSubject("place", note.fields);
    const subject = {
      path: note.path,
      linkTarget: note.path.replace(/\.md$/i, ""),
      fileName: note.stem,
      rawName,
      name: nameInfo.text,
      provisionalName: nameInfo.provisional,
      noteType: "place",
      subtypes: subtypeInfo.values,
      subtypeLabel: subtypeInfo.label,
      subtypeSource: subtypeInfo.source,
      tags,
      title: fieldStrings(note.fields, "title"),
      species: [],
      ancestry: fieldStrings(note.fields, "ancestry"),
      locations: fieldStrings(note.fields, "whereabouts"),
      pronunciation: fieldScalar(note.fields, "pronunciation"),
      aliases: note.aliases,
      textAliases: nameCore.extractTextAliases(note.text, nameInfo.text),
      body: note.text,
    };
    subjects.push(subject);
    placeNotes.set(note.path, note);
  }
  const decisionPath = path.resolve(
    root,
    options.decisionPath || "_Plugins/Name Explorer/Name Decisions.jsonl",
  );
  const relativeDecisionPath = path.relative(root, decisionPath);
  if (
    relativeDecisionPath.startsWith("..") ||
    path.isAbsolute(relativeDecisionPath)
  ) {
    throw new Error(`Decision store must remain inside the vault: ${options.decisionPath}`);
  }
  const decisionText = fs.existsSync(decisionPath) ? fs.readFileSync(decisionPath, "utf8") : "";
  const records = nameCore.parseDecisionStore(decisionText);
  const catalog = nameCore.buildCatalog(subjects, records, {
    knownSubjectPaths: new Set(index.notes.map((note) => note.path)),
  });
  return { catalog, subjects, placeNotes, decisionRecords: records };
}

function escapeRegExp(value) {
  return String(value || "").replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function buildFormMatcher(catalog) {
  const forms = new Map();
  const subjectForms = new Map();
  for (const concept of catalog.concepts) {
    const observed = new Set([
      concept.preferredForm,
      ...concept.forms.map((form) => form.text),
    ]);
    for (const rawForm of observed) {
      const normalized = normalizeExact(rawForm);
      if (!normalized) continue;
      if (!forms.has(normalized)) forms.set(normalized, { subjects: new Set(), displays: new Set() });
      forms.get(normalized).subjects.add(concept.subjectPath);
      forms.get(normalized).displays.add(rawForm);
      if (!subjectForms.has(concept.subjectPath)) subjectForms.set(concept.subjectPath, new Set());
      subjectForms.get(concept.subjectPath).add(rawForm);
    }
  }
  const alternatives = [...forms.keys()]
    .sort((left, right) => right.length - left.length || left.localeCompare(right))
    .map(escapeRegExp);
  const regex = alternatives.length
    ? new RegExp(`(?<![\\p{L}\\p{N}])(?:${alternatives.join("|")})(?![\\p{L}\\p{N}])`, "gu")
    : null;
  const collisions = [...forms.entries()]
    .filter(([, value]) => value.subjects.size > 1)
    .map(([form, value]) => ({ form, subjects: [...value.subjects].sort() }));
  return { forms, subjectForms, regex, collisions };
}

function shortSnippet(value, limit = 260) {
  const text = normalizeTypography(value);
  if (text.length <= limit) return text;
  return `${text.slice(0, limit - 1).trimEnd()}…`;
}

function exactMatchesInLine(line, formMatcher, entityLinks = []) {
  if (!formMatcher.regex) return [];
  const visible = normalizeExact(renderVisibleText(line));
  const output = [];
  formMatcher.regex.lastIndex = 0;
  let match;
  while ((match = formMatcher.regex.exec(visible)) !== null) {
    const normalizedForm = match[0];
    const entry = formMatcher.forms.get(normalizedForm);
    if (!entry) continue;
    let subjects = [...entry.subjects];
    let disambiguatedByLink = false;
    if (subjects.length > 1) {
      const linked = entityLinks.filter((link) =>
        subjects.includes(link.subject) && normalizeExact(link.display) === normalizedForm
      );
      const uniqueLinked = [...new Set(linked.map((link) => link.subject))];
      if (uniqueLinked.length === 1) {
        subjects = uniqueLinked;
        disambiguatedByLink = true;
      } else {
        output.push({
          kind: "ambiguous-form",
          form: normalizedForm,
          subjects: subjects.sort(),
        });
        continue;
      }
    }
    output.push({
      kind: "exact-form",
      form: [...entry.displays].sort((left, right) => left.localeCompare(right))[0],
      normalizedForm,
      subject: subjects[0],
      disambiguatedByLink,
    });
  }
  return output;
}

function parseTranscriptLine(text) {
  const match = String(text || "").match(TRANSCRIPT_LINE_RE);
  if (!match) return { uid: "", speaker: "", speakerRole: "unknown", text: String(text || "") };
  const speaker = normalizeTypography(match[2] || "");
  return {
    uid: match[1],
    speaker,
    speakerRole: !speaker ? "unknown" : /^dm$/i.test(speaker) ? "dm" : "player",
    text: match[3] || "",
  };
}

function scanEvidenceText({ text, sourcePath, channel, index, formMatcher, transcript = false }) {
  const bySubject = new Map();
  const ambiguous = [];
  const add = (subject, kind, record) => {
    if (!bySubject.has(subject)) bySubject.set(subject, { exact: [], entityLinks: [] });
    bySubject.get(subject)[kind].push(record);
  };
  for (const contextual of contextualLines(text)) {
    if (contextual.context !== "visible") continue;
    if (/^Source Files$/i.test(contextual.section)) continue;
    const transcriptLine = transcript
      ? parseTranscriptLine(contextual.text)
      : { uid: "", speaker: "", speakerRole: "unknown", text: contextual.text };
    const sourceText = transcriptLine.text;
    const entityLinks = [];
    for (const link of wikilinksInLine(sourceText)) {
      if (link.embed) continue;
      const resolution = index.resolve(link.target, sourcePath);
      if (!resolution.note || !resolution.note.path.startsWith("Gazetteer/")) continue;
      const subject = resolution.note.path;
      entityLinks.push({ subject, display: link.display });
      add(subject, "entityLinks", {
        path: sourcePath,
        line: contextual.line,
        section: contextual.section || "",
        campaign_scope: contextual.campaignScope || "",
        display: link.display,
        target: link.target,
        uid: transcriptLine.uid,
        speaker: transcriptLine.speaker,
        speaker_role: transcriptLine.speakerRole,
        snippet: shortSnippet(renderVisibleText(sourceText)),
      });
    }
    for (const match of exactMatchesInLine(sourceText, formMatcher, entityLinks)) {
      if (match.kind === "ambiguous-form") {
        ambiguous.push({
          ...match,
          path: sourcePath,
          line: contextual.line,
          uid: transcriptLine.uid,
        });
        continue;
      }
      add(match.subject, "exact", {
        path: sourcePath,
        line: contextual.line,
        section: contextual.section || "",
        campaign_scope: contextual.campaignScope || "",
        form: match.form,
        normalized_form: match.normalizedForm,
        disambiguated_by_link: match.disambiguatedByLink,
        uid: transcriptLine.uid,
        speaker: transcriptLine.speaker,
        speaker_role: transcriptLine.speakerRole,
        snippet: shortSnippet(renderVisibleText(sourceText)),
      });
    }
  }
  return { channel, bySubject, ambiguous };
}

function loadCampaignDefinitions(root) {
  const definitions = new Map();
  const sessionConfigPath = path.join(root, "_scripts", "session_note_campaigns.json");
  if (fs.existsSync(sessionConfigPath)) {
    const payload = JSON.parse(fs.readFileSync(sessionConfigPath, "utf8"));
    for (const [slug, raw] of Object.entries(payload.campaigns || {})) {
      definitions.set(slug, {
        slug,
        name: slug,
        aliases: new Set([slug, ...(raw.aliases || [])]),
        sessionRoot: raw.sessionRoot || "",
        campaignRoot: normalizeSlashes(raw.campaignRoot || ""),
        notePattern: raw.notePattern || "",
        code: (raw.aliases || [])[0] || slug,
      });
    }
  }
  const metadataPath = path.join(root, ".obsidian", "metadata.json");
  if (fs.existsSync(metadataPath)) {
    const payload = JSON.parse(fs.readFileSync(metadataPath, "utf8"));
    for (const campaign of payload.campaigns || []) {
      const folder = normalizeSlashes(campaign.sessionNoteFolder || "");
      let definition = [...definitions.values()].find((candidate) =>
        folder && candidate.campaignRoot && folder.startsWith(candidate.campaignRoot)
      );
      if (!definition) {
        const aliases = [campaign.code, ...(campaign.aliases || [])].map(normalizeKey);
        definition = [...definitions.values()].find((candidate) =>
          [...candidate.aliases].some((alias) => aliases.includes(normalizeKey(alias)))
        );
      }
      if (!definition) {
        const baseName = (campaign.aliases || [])[0] || campaign.code || path.posix.basename(folder);
        const slug = normalizeKey(baseName).replace(/\s+/g, "-") || `campaign-${definitions.size + 1}`;
        definition = {
          slug,
          name: baseName,
          aliases: new Set([slug]),
          sessionRoot: "",
          campaignRoot: folder ? path.posix.dirname(folder) : "",
          notePattern: "",
          code: campaign.code || slug,
        };
        definitions.set(slug, definition);
      }
      definition.code = campaign.code || definition.code;
      definition.name = (campaign.aliases || [])[0] || definition.name;
      definition.sessionNoteFolder = folder;
      for (const alias of [campaign.code, ...(campaign.aliases || [])]) {
        if (alias) definition.aliases.add(alias);
      }
    }
  }
  for (const definition of definitions.values()) {
    if (definition.campaignRoot) {
      const base = path.posix.basename(definition.campaignRoot)
        .replace(/\s+Campaign$/i, "")
        .trim();
      if (base) definition.aliases.add(base);
    }
    definition.aliases.add(definition.slug);
    definition.aliases.add(definition.name);
    definition.aliasKeys = new Set([...definition.aliases].map(normalizeKey).filter(Boolean));
  }
  return definitions;
}

function campaignFor(value, sourcePath, definitions) {
  const normalizedPath = normalizeSlashes(sourcePath);
  for (const definition of definitions.values()) {
    if (definition.campaignRoot && normalizedPath.startsWith(`${definition.campaignRoot}/`)) {
      return definition.slug;
    }
    if (
      definition.sessionRoot &&
      normalizedPath.startsWith(`_sessions/${definition.sessionRoot}/`)
    ) return definition.slug;
  }
  const key = normalizeKey(value);
  if (!key) return "unknown";
  for (const definition of definitions.values()) {
    if (definition.aliasKeys.has(key)) return definition.slug;
  }
  return key.replace(/\s+/g, "-");
}

function sessionNumberFrom(...values) {
  for (const value of values) {
    const direct = String(value || "").trim();
    if (/^\d+$/.test(direct)) return Number(direct);
    const match = direct.match(/(?:session|episode|arc|[-_])\s*0*(\d+)\b/i);
    if (match) return Number(match[1]);
  }
  return null;
}

function sessionIdentity(campaign, number, sessionKey, sourcePath, realWorldDate = "") {
  if (campaign && campaign !== "unknown" && Number.isInteger(number)) {
    return `${campaign}:${number}`;
  }
  if (sessionKey) return `key:${normalizeKey(sessionKey).replace(/\s+/g, "-")}`;
  if (campaign && campaign !== "unknown" && realWorldDate) {
    return `${campaign}:date:${realWorldDate}`;
  }
  return `path:${normalizeSlashes(sourcePath).replace(/\.md$/i, "")}`;
}

function findFirst(directory, predicate) {
  if (!fs.existsSync(directory)) return "";
  return fs.readdirSync(directory)
    .filter(predicate)
    .sort((left, right) => left.localeCompare(right))[0] || "";
}

function discoverSessionRegistry(root, index, definitions) {
  const sessions = new Map();
  const publishedPaths = new Set();

  const ensure = (identity, seed) => {
    if (!sessions.has(identity)) {
      sessions.set(identity, {
        id: identity,
        campaign: seed.campaign,
        number: seed.number,
        session_key: seed.sessionKey || "",
        real_world_date: seed.realWorldDate || "",
        dr_date: seed.drDate || "",
        join: {
          method: seed.joinMethod || "source-only",
          confidence: seed.joinConfidence ?? 0.5,
        },
        published_notes: [],
        recap: "",
        transcript: "",
        transcript_source: "",
        session_metadata: "",
        bundle: "",
        identity_warnings: [],
      });
    }
    return sessions.get(identity);
  };

  for (const note of index.notes) {
    if (!note.path.startsWith("Campaigns/")) continue;
    const tags = fieldStrings(note.fields, "tags").map((tag) =>
      tag.replace(/^#/, "").toLocaleLowerCase("en")
    );
    if (!tags.includes("session-note")) continue;
    const campaign = campaignFor(fieldScalar(note.fields, "campaign"), note.path, definitions);
    const fieldNumber = sessionNumberFrom(fieldScalar(note.fields, "sessionNumber"));
    const filenameNumber = sessionNumberFrom(note.stem, fieldScalar(note.fields, "name"));
    const number = filenameNumber ?? fieldNumber;
    const sessionKey = fieldScalar(note.fields, "sessionKey");
    const realWorldDate = fieldScalar(note.fields, "realWorldDate");
    const drDate = fieldScalar(note.fields, "DR") || fieldScalar(note.fields, "dr");
    const identity = sessionIdentity(campaign, number, sessionKey, note.path, realWorldDate);
    const record = ensure(identity, {
      campaign,
      number,
      sessionKey,
      realWorldDate,
      drDate,
      joinMethod: "published-note-identity",
      joinConfidence: Number.isInteger(number) && campaign !== "unknown" ? 0.96 : 0.7,
    });
    record.published_notes.push(note.path);
    if (fieldNumber != null && filenameNumber != null && fieldNumber !== filenameNumber) {
      record.identity_warnings.push({
        path: note.path,
        field: "sessionNumber",
        frontmatter_value: fieldNumber,
        filename_value: filenameNumber,
        resolution: "used-filename-value",
      });
    }
    publishedPaths.add(note.path);
  }

  const sessionsRoot = path.join(root, "_sessions");
  if (fs.existsSync(sessionsRoot)) {
    for (const rootEntry of fs.readdirSync(sessionsRoot, { withFileTypes: true })) {
      if (!rootEntry.isDirectory() || rootEntry.name === "to-process") continue;
      const campaignDirectory = path.join(sessionsRoot, rootEntry.name);
      for (const bundleEntry of fs.readdirSync(campaignDirectory, { withFileTypes: true })) {
        if (!bundleEntry.isDirectory()) continue;
        const bundleAbsolute = path.join(campaignDirectory, bundleEntry.name);
        const bundleRelative = relativePath(root, bundleAbsolute);
        const cleaned = path.join(bundleAbsolute, "cleaned");
        const sources = path.join(bundleAbsolute, "sources");
        const sessionYamlName = findFirst(cleaned, (name) => /-session\.yaml$/i.test(name));
        let sessionMetadata = sessionYamlName ? path.join(cleaned, sessionYamlName) : "";
        if (!sessionMetadata) {
          const sourceYamlName = findFirst(sources, (name) => /\.ya?ml$/i.test(name) && !/participants|mapping/i.test(name));
          if (sourceYamlName) sessionMetadata = path.join(sources, sourceYamlName);
        }
        const metadataText = sessionMetadata && fs.existsSync(sessionMetadata)
          ? fs.readFileSync(sessionMetadata, "utf8")
          : "";
        const metadata = parseTopLevelScalars(metadataText);
        const campaign = campaignFor(metadata.campaign, bundleRelative, definitions);
        const metadataNumber = sessionNumberFrom(metadata.sessionNumber);
        const bundleNumber = sessionNumberFrom(bundleEntry.name);
        const number = bundleNumber ?? metadataNumber;
        const realWorldDate = metadata.realWorldDate || "";
        const drDate = metadata.drStart || metadata.DR || "";
        let identity = sessionIdentity(campaign, number, metadata.sessionKey, bundleRelative, realWorldDate);
        let joinMethod = "bundle-identity";
        let joinConfidence = Number.isInteger(number) && campaign !== "unknown" ? 0.98 : 0.65;
        if (!sessions.has(identity) && campaign !== "unknown" && realWorldDate) {
          const dateMatches = [...sessions.values()].filter((session) =>
            session.campaign === campaign && session.real_world_date === realWorldDate
          );
          if (dateMatches.length === 1) {
            identity = dateMatches[0].id;
            joinMethod = "campaign-and-real-world-date";
            joinConfidence = 0.88;
          }
        } else if (sessions.has(identity)) {
          joinMethod = "campaign-and-session-number";
          joinConfidence = 0.98;
        }
        const record = ensure(identity, {
          campaign,
          number,
          sessionKey: metadata.sessionKey || "",
          realWorldDate,
          drDate,
          joinMethod,
          joinConfidence,
        });
        record.bundle = bundleRelative;
        if (metadataNumber != null && bundleNumber != null && metadataNumber !== bundleNumber) {
          record.identity_warnings.push({
            path: bundleRelative,
            field: "sessionNumber",
            metadata_value: metadataNumber,
            bundle_value: bundleNumber,
            resolution: "used-bundle-value",
          });
        }
        if (sessionMetadata) record.session_metadata = relativePath(root, sessionMetadata);
        if (record.join.method === "published-note-identity" || joinConfidence > record.join.confidence) {
          record.join = { method: joinMethod, confidence: joinConfidence };
        }
        const recapName = findFirst(cleaned, (name) => /-session-recap\.md$/i.test(name));
        if (recapName) record.recap = relativePath(root, path.join(cleaned, recapName));
        const cleanedName = findFirst(cleaned, (name) => /-source-cleaned\.md$/i.test(name));
        const preparedName = findFirst(cleaned, (name) => /-source-prepared\.md$/i.test(name));
        let sourceType = normalizeKey(metadata.sourceType);
        if (!sourceType && preparedName) {
          const sample = fs.readFileSync(path.join(cleaned, preparedName), "utf8").slice(0, 2000);
          if (/^\[u\d+\s*\|[^\]]+\]/m.test(sample)) sourceType = "transcript";
        }
        if (sourceType === "transcript") {
          if (cleanedName) {
            record.transcript = relativePath(root, path.join(cleaned, cleanedName));
            record.transcript_source = "cleaned";
          } else if (preparedName) {
            record.transcript = relativePath(root, path.join(cleaned, preparedName));
            record.transcript_source = "prepared";
          }
        }
      }
    }
  }

  for (const record of sessions.values()) {
    record.published_notes.sort();
    if (!record.bundle) record.join = { method: "published-only", confidence: record.join.confidence };
    if (!record.published_notes.length) record.join = { method: "bundle-only", confidence: record.join.confidence };
  }

  return {
    sessions: [...sessions.values()].sort((left, right) =>
      left.campaign.localeCompare(right.campaign) ||
      (left.number ?? Number.MAX_SAFE_INTEGER) - (right.number ?? Number.MAX_SAFE_INTEGER) ||
      left.id.localeCompare(right.id)
    ),
    publishedPaths,
  };
}

function incrementMap(map, key, amount = 1) {
  map.set(key, (map.get(key) || 0) + amount);
}

function sortedObject(map) {
  return Object.fromEntries([...map.entries()].sort((left, right) =>
    left[0].localeCompare(right[0])
  ));
}

function percentileRank(values, value) {
  if (!values.length) return null;
  const below = values.filter((candidate) => candidate < value).length;
  const equal = values.filter((candidate) => candidate === value).length;
  return Number(((below + Math.max(0, equal - 1) / 2) / Math.max(1, values.length - 1)).toFixed(4));
}

function embeddednessBand(percentile, inbound) {
  if (!inbound) return "unlinked";
  if (percentile >= 0.9) return "very-high";
  if (percentile >= 0.7) return "high";
  if (percentile >= 0.3) return "medium";
  return "low";
}

function buildGraphEvidence(index, placeCatalog, publishedSessionPaths) {
  const placePaths = new Set(placeCatalog.subjects.map((subject) => subject.path));
  const raw = new Map(placeCatalog.subjects.map((subject) => [subject.path, {
    inbound: [],
    outbound: [],
    semanticInbound: [],
    semanticOutbound: [],
  }]));

  for (const note of index.notes) {
    const category = sourceCategory(note.path, publishedSessionPaths);
    for (const contextual of contextualLines(note.text)) {
      for (const link of wikilinksInLine(contextual.text)) {
        const resolution = index.resolve(link.target, note.path);
        if (!resolution.note) continue;
        const targetPath = resolution.note.path;
        const record = {
          source: note.path,
          target: targetPath,
          source_class: category,
          context: contextual.context,
          line: contextual.line,
          display: link.display,
        };
        if (placePaths.has(targetPath)) raw.get(targetPath).inbound.push(record);
        if (placePaths.has(note.path)) raw.get(note.path).outbound.push(record);
      }
      for (const link of markdownLinksInLine(contextual.text)) {
        const resolution = index.resolveMarkdown(link.destination, note.path);
        if (!resolution.note) continue;
        const targetPath = resolution.note.path;
        const record = {
          source: note.path,
          target: targetPath,
          source_class: category,
          context: contextual.context,
          line: contextual.line,
          display: link.label,
        };
        if (placePaths.has(targetPath)) raw.get(targetPath).inbound.push(record);
        if (placePaths.has(note.path)) raw.get(note.path).outbound.push(record);
      }
    }
    for (const reference of parseReferenceValues(note.frontmatterLines)) {
      const resolution = index.resolve(reference.value, note.path);
      if (!resolution.note || !placePaths.has(resolution.note.path)) continue;
      const record = {
        source: note.path,
        target: resolution.note.path,
        source_class: category,
        field: reference.field,
        value: reference.value,
      };
      raw.get(resolution.note.path).semanticInbound.push(record);
      if (placePaths.has(note.path)) raw.get(note.path).semanticOutbound.push(record);
    }
  }

  const evidence = new Map();
  for (const subject of placeCatalog.subjects) {
    const graph = raw.get(subject.path);
    const eligibleInbound = graph.inbound.filter((event) =>
      !PRIMARY_GRAPH_EXCLUSIONS.has(event.source_class) && event.context !== "comment"
    );
    const eligibleOutbound = graph.outbound.filter((event) =>
      !PRIMARY_GRAPH_EXCLUSIONS.has(event.source_class) && event.context !== "comment"
    );
    const eligibleSemanticIn = graph.semanticInbound.filter((event) =>
      !PRIMARY_GRAPH_EXCLUSIONS.has(event.source_class)
    );
    const eligibleSemanticOut = graph.semanticOutbound.filter((event) =>
      !PRIMARY_GRAPH_EXCLUSIONS.has(event.source_class)
    );
    const inboundSources = new Set(eligibleInbound.map((event) => event.source));
    const outboundTargets = new Set(eligibleOutbound.map((event) => event.target));
    const semanticInSources = new Set(eligibleSemanticIn.map((event) => event.source));
    const semanticOutTargets = new Set(eligibleSemanticOut.map((event) => event.target));
    const sourceClasses = new Map();
    const contexts = new Map();
    const sourceCounts = new Map();
    for (const event of graph.inbound) {
      incrementMap(sourceClasses, event.source_class);
      incrementMap(contexts, event.context);
      incrementMap(sourceCounts, event.source);
    }
    const score =
      Math.log1p(inboundSources.size) +
      0.25 * Math.log1p(outboundTargets.size) +
      0.5 * Math.log1p(semanticInSources.size + semanticOutTargets.size);
    evidence.set(subject.path, {
      inbound: {
        unique_notes: inboundSources.size,
        mentions: eligibleInbound.length,
        all_mentions_including_excluded: graph.inbound.length,
        by_source_class: sortedObject(sourceClasses),
        by_context: sortedObject(contexts),
        top_sources: [...sourceCounts.entries()]
          .sort((left, right) => right[1] - left[1] || left[0].localeCompare(right[0]))
          .slice(0, 10)
          .map(([source, mentions]) => ({ source, mentions })),
      },
      outbound: {
        unique_notes: outboundTargets.size,
        mentions: eligibleOutbound.length,
      },
      semantic_edges: {
        inbound_unique_notes: semanticInSources.size,
        outbound_unique_notes: semanticOutTargets.size,
      },
      score: Number(score.toFixed(6)),
      percentile_all_places: null,
      percentile_same_type: null,
      band: "unlinked",
      score_basis: "log1p(inbound unique notes) + 0.25*log1p(outbound unique notes) + 0.5*log1p(semantic edge breadth)",
    });
  }

  const allScores = [...evidence.values()].map((item) => item.score);
  const byType = new Map();
  for (const subject of placeCatalog.subjects) {
    const type = subject.subtypeLabel || "unknown";
    if (!byType.has(type)) byType.set(type, []);
    byType.get(type).push(evidence.get(subject.path).score);
  }
  for (const subject of placeCatalog.subjects) {
    const record = evidence.get(subject.path);
    record.percentile_all_places = percentileRank(allScores, record.score);
    record.percentile_same_type = percentileRank(
      byType.get(subject.subtypeLabel || "unknown") || [],
      record.score,
    );
    record.band = embeddednessBand(record.percentile_all_places, record.inbound.unique_notes);
  }
  return evidence;
}

function summarizeOccurrences(events, fields = {}) {
  const formCounts = new Map();
  const sectionCounts = new Map();
  const speakerCounts = new Map();
  let playerOccurrences = 0;
  let dmOccurrences = 0;
  for (const event of events || []) {
    if (event.form) incrementMap(formCounts, event.form);
    if (event.section) incrementMap(sectionCounts, event.section);
    if (event.speaker) incrementMap(speakerCounts, event.speaker);
    if (event.speaker_role === "player") playerOccurrences += 1;
    if (event.speaker_role === "dm") dmOccurrences += 1;
  }
  return {
    ...fields,
    occurrence_count: (events || []).length,
    forms: sortedObject(formCounts),
    sections: sortedObject(sectionCounts),
    speakers: sortedObject(speakerCounts),
    player_occurrences: playerOccurrences,
    dm_occurrences: dmOccurrences,
    examples: (events || []).slice(0, MAX_EVIDENCE_EXAMPLES),
  };
}

function emptyChannel(available, paths = [], source = "") {
  return {
    available,
    paths,
    source,
    exact_mentions: summarizeOccurrences([]),
    entity_links: summarizeOccurrences([]),
  };
}

function channelForScan(scan, subject, available, paths = [], source = "") {
  const evidence = scan?.bySubject.get(subject) || { exact: [], entityLinks: [] };
  return {
    available,
    paths,
    source,
    exact_mentions: summarizeOccurrences(evidence.exact),
    entity_links: summarizeOccurrences(evidence.entityLinks),
  };
}

function mergeCampaignInfoEntry(entry, campaign, definitions) {
  return {
    campaign: campaignFor(entry.campaign, "", definitions),
    campaign_raw: entry.campaign,
    type: entry.type || "seen",
    date: entry.date || "",
    person: entry.person || "",
  };
}

function buildCampaignEvidence(root, index, placeCatalog, formMatcher, registry, definitions) {
  const subjectCampaigns = new Map(placeCatalog.subjects.map((subject) => [subject.path, new Map()]));
  const unattributedBySubject = new Map(
    placeCatalog.subjects.map((subject) => [subject.path, []])
  );
  const coverage = new Map();
  const ambiguousMatches = [];
  const ensureCampaign = (subject, campaign) => {
    const map = subjectCampaigns.get(subject);
    if (!map.has(campaign)) {
      map.set(campaign, {
        campaign,
        sessions: [],
        campaign_material: [],
        structured_campaign_info: [],
      });
    }
    return map.get(campaign);
  };

  for (const session of registry.sessions) {
    if (!coverage.has(session.campaign)) {
      coverage.set(session.campaign, {
        sessions: 0,
        with_published_note: 0,
        with_recap: 0,
        with_transcript: 0,
      });
    }
    const campaignCoverage = coverage.get(session.campaign);
    campaignCoverage.sessions += 1;
    if (session.published_notes.length) campaignCoverage.with_published_note += 1;
    if (session.recap) campaignCoverage.with_recap += 1;
    if (session.transcript) campaignCoverage.with_transcript += 1;

    const publishedScans = [];
    for (const sourcePath of session.published_notes) {
      const note = index.byPath.get(normalizePathKey(sourcePath));
      if (!note) continue;
      const scan = scanEvidenceText({
        text: note.text,
        sourcePath,
        channel: "published_note",
        index,
        formMatcher,
      });
      publishedScans.push(scan);
      ambiguousMatches.push(...scan.ambiguous.map((item) => ({ ...item, channel: "published_note", session: session.id })));
    }
    const combineScans = (scans) => {
      const bySubject = new Map();
      for (const scan of scans) {
        for (const [subject, evidence] of scan.bySubject) {
          if (!bySubject.has(subject)) bySubject.set(subject, { exact: [], entityLinks: [] });
          bySubject.get(subject).exact.push(...evidence.exact);
          bySubject.get(subject).entityLinks.push(...evidence.entityLinks);
        }
      }
      return { bySubject };
    };
    const publishedScan = combineScans(publishedScans);
    let recapScan = { bySubject: new Map(), ambiguous: [] };
    if (session.recap) {
      const absolute = path.join(root, session.recap);
      if (fs.existsSync(absolute)) {
        recapScan = scanEvidenceText({
          text: fs.readFileSync(absolute, "utf8"),
          sourcePath: session.recap,
          channel: "recap",
          index,
          formMatcher,
        });
        ambiguousMatches.push(...recapScan.ambiguous.map((item) => ({ ...item, channel: "recap", session: session.id })));
      }
    }
    let transcriptScan = { bySubject: new Map(), ambiguous: [] };
    if (session.transcript) {
      const absolute = path.join(root, session.transcript);
      if (fs.existsSync(absolute)) {
        transcriptScan = scanEvidenceText({
          text: fs.readFileSync(absolute, "utf8"),
          sourcePath: session.transcript,
          channel: "transcript",
          index,
          formMatcher,
          transcript: true,
        });
        ambiguousMatches.push(...transcriptScan.ambiguous.map((item) => ({ ...item, channel: "transcript", session: session.id })));
      }
    }
    const subjects = new Set([
      ...publishedScan.bySubject.keys(),
      ...recapScan.bySubject.keys(),
      ...transcriptScan.bySubject.keys(),
    ]);
    for (const subject of subjects) {
      if (!subjectCampaigns.has(subject)) continue;
      const published = channelForScan(
        publishedScan,
        subject,
        session.published_notes.length > 0,
        session.published_notes,
      );
      const recap = channelForScan(
        recapScan,
        subject,
        Boolean(session.recap),
        session.recap ? [session.recap] : [],
      );
      const transcript = channelForScan(
        transcriptScan,
        subject,
        Boolean(session.transcript),
        session.transcript ? [session.transcript] : [],
        session.transcript_source,
      );
      const exactCount =
        published.exact_mentions.occurrence_count +
        recap.exact_mentions.occurrence_count +
        transcript.exact_mentions.occurrence_count;
      const entityCount =
        published.entity_links.occurrence_count +
        recap.entity_links.occurrence_count +
        transcript.entity_links.occurrence_count;
      if (!exactCount && !entityCount) continue;
      const sceneSignals = [];
      const recapSections = Object.keys(recap.exact_mentions.sections);
      const publishedSections = Object.keys(published.exact_mentions.sections);
      if (recapSections.some((section) => /location/i.test(section))) sceneSignals.push("recap-location-section");
      if (publishedSections.some((section) => /^(narrative|places)$/i.test(section))) {
        sceneSignals.push("published-scene-section");
      }
      if (transcript.exact_mentions.occurrence_count) sceneSignals.push("transcript-exact-mention");
      ensureCampaign(subject, session.campaign).sessions.push({
        id: session.id,
        number: session.number,
        real_world_date: session.real_world_date,
        dr_date: session.dr_date,
        join: session.join,
        bundle: session.bundle,
        scene_signals: sceneSignals,
        published_note: published,
        recap,
        transcript,
      });
    }
  }

  const campaignMaterialNotes = index.notes.filter((note) =>
    note.path.startsWith("Campaigns/") &&
    !note.path.split("/").includes("_generated") &&
    !registry.publishedPaths.has(note.path)
  );
  for (const note of campaignMaterialNotes) {
    const campaign = campaignFor(fieldScalar(note.fields, "campaign"), note.path, definitions);
    const scan = scanEvidenceText({
      text: note.text,
      sourcePath: note.path,
      channel: "campaign_material",
      index,
      formMatcher,
    });
    ambiguousMatches.push(...scan.ambiguous.map((item) => ({ ...item, channel: "campaign_material" })));
    for (const [subject, evidence] of scan.bySubject) {
      if (!subjectCampaigns.has(subject)) continue;
      const material = {
        path: note.path,
        exact_mentions: summarizeOccurrences(evidence.exact),
        entity_links: summarizeOccurrences(evidence.entityLinks),
      };
      if (campaign === "unknown") {
        unattributedBySubject.get(subject).push(material);
      } else {
        ensureCampaign(subject, campaign).campaign_material.push(material);
      }
    }
  }

  for (const subject of placeCatalog.subjects) {
    const note = placeCatalog.placeNotes.get(subject.path);
    for (const entry of parseCampaignInfo(note.frontmatterLines)) {
      const parsed = mergeCampaignInfoEntry(entry, "", definitions);
      ensureCampaign(subject.path, parsed.campaign).structured_campaign_info.push(parsed);
    }
  }

  const output = new Map();
  for (const subject of placeCatalog.subjects) {
    const campaigns = [];
    for (const campaign of subjectCampaigns.get(subject.path).values()) {
      campaign.sessions.sort((left, right) =>
        (left.number ?? Number.MAX_SAFE_INTEGER) - (right.number ?? Number.MAX_SAFE_INTEGER) ||
        left.id.localeCompare(right.id)
      );
      const sessionCount = campaign.sessions.length;
      const sceneSessions = campaign.sessions.filter((session) => session.scene_signals.length).length;
      const transcriptSessions = campaign.sessions.filter((session) =>
        session.transcript.exact_mentions.occurrence_count > 0
      ).length;
      const recapSessions = campaign.sessions.filter((session) =>
        session.recap.exact_mentions.occurrence_count > 0
      ).length;
      const publishedSessions = campaign.sessions.filter((session) =>
        session.published_note.exact_mentions.occurrence_count > 0
      ).length;
      const entityOnlySessions = campaign.sessions.filter((session) => {
        const exact =
          session.published_note.exact_mentions.occurrence_count +
          session.recap.exact_mentions.occurrence_count +
          session.transcript.exact_mentions.occurrence_count;
        const links =
          session.published_note.entity_links.occurrence_count +
          session.recap.entity_links.occurrence_count +
          session.transcript.entity_links.occurrence_count;
        return !exact && links > 0;
      }).length;
      const formsExposed = new Set();
      let transcriptOccurrences = 0;
      let playerOccurrences = 0;
      let dmOccurrences = 0;
      for (const session of campaign.sessions) {
        for (const channel of [session.published_note, session.recap, session.transcript]) {
          Object.keys(channel.exact_mentions.forms).forEach((form) => formsExposed.add(form));
        }
        transcriptOccurrences += session.transcript.exact_mentions.occurrence_count;
        playerOccurrences += session.transcript.exact_mentions.player_occurrences;
        dmOccurrences += session.transcript.exact_mentions.dm_occurrences;
      }
      let introduced = "none";
      if (transcriptSessions) introduced = "confirmed-transcript";
      else if (recapSessions) introduced = "documented-recap";
      else if (publishedSessions) introduced = "documented-published-note";
      else if (entityOnlySessions) introduced = "entity-reference-only";
      else if (campaign.structured_campaign_info.length) introduced = "structured-campaign-info-only";
      else if (campaign.campaign_material.length) introduced = "campaign-material-only";

      let recurrence = "none";
      if (sessionCount >= 5 && sceneSessions >= 3) recurrence = "campaign-core";
      else if (sessionCount >= 2) recurrence = "recurring";
      else if (sessionCount === 1) recurrence = "one-off";
      else if (campaign.campaign_material.length || campaign.structured_campaign_info.length) recurrence = "campaign-context-only";

      campaigns.push({
        campaign: campaign.campaign,
        classification_method: "deterministic-evidence-signals-v1",
        session_count: sessionCount,
        scene_session_count: sceneSessions,
        background_session_count: Math.max(0, sessionCount - sceneSessions),
        transcript_session_count: transcriptSessions,
        recap_session_count: recapSessions,
        published_note_session_count: publishedSessions,
        entity_reference_only_session_count: entityOnlySessions,
        transcript_occurrences: transcriptOccurrences,
        player_transcript_occurrences: playerOccurrences,
        dm_transcript_occurrences: dmOccurrences,
        forms_exposed: [...formsExposed].sort((left, right) => left.localeCompare(right)),
        introduced_in_play: introduced,
        recurrence,
        structured_campaign_info: campaign.structured_campaign_info,
        campaign_material: campaign.campaign_material,
        sessions: campaign.sessions,
      });
    }
    output.set(subject.path, campaigns.sort((left, right) =>
      left.campaign.localeCompare(right.campaign)
    ));
  }
  return {
    bySubject: output,
    unattributedBySubject,
    coverage: sortedObject(coverage),
    ambiguousMatches,
  };
}

const NAMING_PATTERNS = [
  ["naming", /\b(?:also\s+known\s+as|known\s+as|locally\s+known|called|named|naming)\b/i],
  ["etymology", /\b(?:etymolog\w*|means?|meaning|derived\s+from|word\s+for)\b/i],
  ["translation", /\b(?:translation|translated|calque|rendered\s+as|literal(?:ly)?\s+means?)\b/i],
  ["language", /\b(?:language|tongue|endonym|exonym)\b/i],
  ["debate", /(?:\bname\w*\b.{0,80}\b(?:maybe|might|need|needs|proposed|debate|uncertain|not\s+sure|edit)\b|\b(?:maybe|proposed|uncertain|not\s+sure)\b.{0,80}\bname\w*\b)/i],
];

function namingEvidenceForSubject(subject, note, concepts, decisionRecords) {
  const evidence = [];
  const subjectForms = new Set([
    subject.name,
    ...subject.aliases,
    ...concepts.flatMap((concept) => [
      concept.preferredForm,
      ...concept.forms.map((form) => form.text),
    ]),
  ].map(normalizeExact).filter(Boolean));
  for (const contextual of contextualLines(note.text)) {
    if (contextual.context === "frontmatter") continue;
    for (const [kind, pattern] of NAMING_PATTERNS) {
      if (!pattern.test(contextual.text)) continue;
      if (
        ["etymology", "translation", "language"].includes(kind) &&
        ![...subjectForms].some((form) => normalizeExact(contextual.text).includes(form))
      ) continue;
      evidence.push({
        kind,
        path: note.path,
        line: contextual.line,
        context: contextual.context,
        campaign_scope: contextual.campaignScope || "",
        snippet: shortSnippet(renderVisibleText(contextual.text)),
      });
    }
  }
  const deduped = [];
  const seen = new Set();
  for (const item of evidence) {
    const key = `${item.kind}\u0000${item.line}\u0000${item.context}`;
    if (seen.has(key)) continue;
    seen.add(key);
    deduped.push(item);
  }
  const languages = new Set();
  const supportedLanguages = new Set();
  const languageAssignments = [];
  for (const concept of concepts) {
    const language = concept.effectiveLanguage?.language;
    if (language && language !== "Unknown") languages.add(language);
    const supported = [
      "overridden",
      "confirmed",
      "reviewed-unknown",
      "text-evidence",
      "conflict",
    ].includes(concept.status);
    if (supported && language && language !== "Unknown") supportedLanguages.add(language);
    languageAssignments.push({
      concept: concept.id,
      form: concept.preferredForm,
      language: language || "Unknown",
      source: concept.languageSource,
      status: concept.status,
      supported,
    });
  }
  const subjectDecisions = decisionRecords.filter((record) => record.subject === subject.path);
  const kinds = new Set(deduped.map((item) => item.kind));
  let documentationDepth = "none";
  if (deduped.length >= 3 || kinds.size >= 2) documentationDepth = "developed";
  else if (deduped.length) documentationDepth = "documented";
  else if (concepts.length > 1 || subject.pronunciation) documentationDepth = "form-only";

  const reviewReasons = nameCore.nameReviewForSubject(subject).nameReviewReasons;
  let reviewState = "unreviewed";
  if (concepts.some((concept) => concept.status === "conflict")) reviewState = "conflicting";
  else if (reviewReasons.includes("provisional-name-marker")) reviewState = "explicitly-provisional";
  else if (kinds.has("debate")) reviewState = "explicitly-debated";
  else if (reviewReasons.includes("status/check/name")) reviewState = "needs-review";
  else if (subjectDecisions.length) reviewState = "curated";
  else if (deduped.length) reviewState = "no-debate-signal";

  return {
    classification_method: "deterministic-naming-signals-v1",
    review_flags: reviewReasons,
    documentation_depth: documentationDepth,
    review_state: reviewState,
    aliases: subject.aliases,
    concept_count: concepts.length,
    pronunciation: subject.pronunciation || "",
    languages: [...languages].sort((left, right) => left.localeCompare(right)),
    supported_languages: [...supportedLanguages].sort((left, right) => left.localeCompare(right)),
    language_assignments: languageAssignments,
    multiple_languages: supportedLanguages.size > 1,
    multiple_languages_including_inference: languages.size > 1,
    decision_count: subjectDecisions.length,
    signal_counts: Object.fromEntries([...NAMING_PATTERNS.map(([kind]) => kind)].map((kind) => [
      kind,
      deduped.filter((item) => item.kind === kind).length,
    ])),
    evidence: deduped.slice(0, 24),
  };
}

function buildEvidenceRecords(root, options = {}) {
  const index = createNoteIndex(root);
  const placeCatalog = buildPlaceCatalog(index, root, options);
  const formMatcher = buildFormMatcher(placeCatalog.catalog);
  const definitions = loadCampaignDefinitions(root);
  const registry = discoverSessionRegistry(root, index, definitions);
  const graph = buildGraphEvidence(index, placeCatalog, registry.publishedPaths);
  const campaigns = buildCampaignEvidence(
    root,
    index,
    placeCatalog,
    formMatcher,
    registry,
    definitions,
  );
  const conceptsBySubject = new Map();
  for (const concept of placeCatalog.catalog.concepts) {
    if (!conceptsBySubject.has(concept.subjectPath)) conceptsBySubject.set(concept.subjectPath, []);
    conceptsBySubject.get(concept.subjectPath).push(concept);
  }
  const exportBySubject = new Map();
  for (const record of nameCore.catalogExportRecords(placeCatalog.catalog)) {
    if (!exportBySubject.has(record.subject)) exportBySubject.set(record.subject, []);
    exportBySubject.get(record.subject).push(record);
  }

  const records = placeCatalog.subjects.map((subject) => {
    const note = placeCatalog.placeNotes.get(subject.path);
    const naming = namingEvidenceForSubject(
      subject,
      note,
      conceptsBySubject.get(subject.path) || [],
      placeCatalog.decisionRecords,
    );
    return {
      record_type: "place-name-evidence",
      schema_version: SCHEMA_VERSION,
      subject: subject.path,
      subject_name: subject.name,
      type_of: subject.subtypes,
      names: exportBySubject.get(subject.path) || [],
      embeddedness: graph.get(subject.path),
      campaigns: campaigns.bySubject.get(subject.path) || [],
      unattributed_campaign_material:
        campaigns.unattributedBySubject.get(subject.path) || [],
      naming,
      source_sha256: sha256(note.text),
    };
  }).sort((left, right) => left.subject.localeCompare(right.subject));

  const meta = {
    record_type: "meta",
    schema_version: SCHEMA_VERSION,
    generated_at: new Date().toISOString(),
    root: normalizeSlashes(root),
    place_count: records.length,
    session_count: registry.sessions.length,
    campaign_coverage: campaigns.coverage,
    unattributed_campaign_material: {
      place_count: records.filter((record) =>
        record.unattributed_campaign_material.length > 0
      ).length,
      note_count: new Set(records.flatMap((record) =>
        record.unattributed_campaign_material.map((item) => item.path)
      )).size,
      treatment: "Retained separately because the source note could not be assigned to one configured campaign.",
    },
    matching: {
      algorithm: "exact-after-NFKC-typography-whitespace-and-case-normalization; diacritics preserved; Unicode letter-number boundaries",
      candidate_form_count: formMatcher.forms.size,
      ambiguous_form_count: formMatcher.collisions.length,
      ambiguous_forms: formMatcher.collisions,
      ambiguous_occurrence_count: campaigns.ambiguousMatches.length,
      ambiguous_occurrence_examples: campaigns.ambiguousMatches.slice(0, MAX_EVIDENCE_EXAMPLES),
    },
    session_joining: {
      methods: Object.fromEntries([...new Set(registry.sessions.map((session) => session.join.method))]
        .sort()
        .map((method) => [method, registry.sessions.filter((session) => session.join.method === method).length])),
      records: registry.sessions.map((session) => ({
        id: session.id,
        campaign: session.campaign,
        number: session.number,
        join: session.join,
        published_notes: session.published_notes,
        bundle: session.bundle,
        recap: session.recap,
        transcript: session.transcript,
        transcript_source: session.transcript_source,
        identity_warnings: session.identity_warnings,
      })),
    },
  };
  return { meta, records };
}

module.exports = {
  SCHEMA_VERSION,
  MAX_EVIDENCE_EXAMPLES,
  normalizeTypography,
  normalizeExact,
  normalizeKey,
  splitFrontmatter,
  parseFrontmatter,
  fieldStrings,
  fieldScalar,
  parseTopLevelScalars,
  parseCampaignInfo,
  parseReferenceValues,
  contextualLines,
  wikilinksInLine,
  markdownLinksInLine,
  renderVisibleText,
  createNoteIndex,
  buildPlaceCatalog,
  buildFormMatcher,
  exactMatchesInLine,
  parseTranscriptLine,
  scanEvidenceText,
  loadCampaignDefinitions,
  campaignFor,
  sessionNumberFrom,
  sessionIdentity,
  discoverSessionRegistry,
  buildGraphEvidence,
  buildCampaignEvidence,
  namingEvidenceForSubject,
  buildEvidenceRecords,
  sourceCategory,
  sha256,
  relativePath,
  walkFiles,
  nameCore,
  PRIMARY_GRAPH_EXCLUSIONS,
};

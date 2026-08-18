#!/usr/bin/env node
"use strict";

const fs = require("node:fs");
const path = require("node:path");

const evidence = require("./place_name_evidence.js");

const DEFAULT_DATA_DIR = "_Plugins/Name Explorer";

function parseArgs(argv) {
  const options = {
    root: process.cwd(),
    decisions: `${DEFAULT_DATA_DIR}/Name Decisions.jsonl`,
    output: `${DEFAULT_DATA_DIR}/Place Name Evidence.jsonl`,
    summary: `${DEFAULT_DATA_DIR}/Place Name Evidence Summary.json`,
    stdout: false,
  };
  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (value === "--root") options.root = argv[++index];
    else if (value === "--decisions") options.decisions = argv[++index];
    else if (value === "--output") options.output = argv[++index];
    else if (value === "--summary") options.summary = argv[++index];
    else if (value === "--stdout") options.stdout = true;
    else if (value === "--help" || value === "-h") options.help = true;
    else throw new Error(`Unknown argument: ${value}`);
  }
  return options;
}

function usage() {
  return [
    "Usage: node _scripts/analyze_place_names.js [options]",
    "",
    "Options:",
    "  --root PATH       Vault root (default: current directory)",
    "  --decisions PATH  Vault-relative Name Explorer decision store",
    "  --output PATH     Vault-relative JSONL output path",
    "  --summary PATH    Vault-relative summary JSON path",
    "  --stdout          Print JSONL instead of writing files",
    "  -h, --help        Show this help",
  ].join("\n");
}

function writeFile(root, relative, text) {
  const absolute = path.resolve(root, relative);
  const relativeCheck = path.relative(root, absolute);
  if (relativeCheck.startsWith("..") || path.isAbsolute(relativeCheck)) {
    throw new Error(`Output must remain inside the vault: ${relative}`);
  }
  fs.mkdirSync(path.dirname(absolute), { recursive: true });
  fs.writeFileSync(absolute, text, "utf8");
  return absolute;
}

function main(argv = process.argv.slice(2)) {
  const options = parseArgs(argv);
  if (options.help) {
    process.stdout.write(`${usage()}\n`);
    return 0;
  }
  const root = path.resolve(options.root);
  const result = evidence.buildEvidenceRecords(root, {
    decisionPath: options.decisions,
  });
  const jsonl = [result.meta, ...result.records]
    .map((record) => JSON.stringify(record))
    .join("\n") + "\n";
  if (options.stdout) {
    process.stdout.write(jsonl);
  } else {
    const output = writeFile(root, options.output, jsonl);
    const summary = writeFile(root, options.summary, `${JSON.stringify(result.meta, null, 2)}\n`);
    process.stdout.write(JSON.stringify({
      output,
      summary,
      places: result.records.length,
      sessions: result.meta.session_count,
      campaigns: Object.keys(result.meta.campaign_coverage).length,
      ambiguous_forms: result.meta.matching.ambiguous_form_count,
      ambiguous_occurrences: result.meta.matching.ambiguous_occurrence_count,
    }, null, 2) + "\n");
  }
  return 0;
}

if (require.main === module) {
  try {
    process.exitCode = main();
  } catch (error) {
    process.stderr.write(`Place-name analysis failed: ${error.stack || error.message}\n`);
    process.exitCode = 1;
  }
}

module.exports = { parseArgs, main, writeFile };

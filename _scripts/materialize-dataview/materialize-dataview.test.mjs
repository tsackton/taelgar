import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import {
  buildEvalCode,
  buildMaterializerRequest,
  buildObsidianCliArgs,
  formatWaitingForProgressLine,
  formatProgressLine,
  parseArgs,
  resolveObsidianCommand,
  truncateLine,
  writePrefixedLines,
} from "./materialize-dataview.mjs";

test("parseArgs accepts Obsidian CLI options", () => {
  const args = parseArgs([
    "--vault",
    "/tmp/Taelgar",
    "--out",
    "/tmp/Taelgar-static",
    "--no-strict",
    "--obsidian-command",
    "/bin/obsidian",
    "--obsidian-vault",
    "Taelgar",
    "--header-type",
    "static",
    "--no-progress",
    "--progress-interval",
    "2",
    "--no-obsidian-output",
  ]);

  assert.equal(args.vaultPath, "/tmp/Taelgar");
  assert.equal(args.outputPath, "/tmp/Taelgar-static");
  assert.equal(args.strict, false);
  assert.equal(args.obsidianCommand, "/bin/obsidian");
  assert.equal(args.obsidianVault, "Taelgar");
  assert.equal(args.headerType, "static");
  assert.equal(args.progress, false);
  assert.equal(args.progressIntervalMs, 2000);
  assert.equal(args.obsidianOutput, false);
});

test("parseArgs rejects removed protocol bridge options", () => {
  assert.throws(
    () => parseArgs(["--launcher", "open {url}"]),
    /official Obsidian CLI/,
  );
});

test("buildMaterializerRequest resolves defaults", () => {
  const { request, reportPath } = buildMaterializerRequest(
    {
      outputPath: "/tmp/Taelgar-static",
      strict: false,
      timeoutMs: 120000,
      blockTimeoutMs: 30000,
    },
    { cwd: "/tmp/Taelgar", id: "test-run" },
  );

  assert.equal(request.id, "test-run");
  assert.equal(request.config.vaultPath, path.resolve("/tmp/Taelgar"));
  assert.equal(request.config.outputPath, path.resolve("/tmp/Taelgar-static"));
  assert.equal(request.config.mode, "write");
  assert.equal(request.config.strict, false);
  assert.equal(request.config.headerType, "website");
  assert.equal(reportPath, path.resolve("/tmp/Taelgar-static/.dataview-materialization-report.json"));
});

test("buildEvalCode invokes plugin runRequest", () => {
  const code = buildEvalCode({ id: "abc", config: { mode: "audit" } });

  assert.match(code, /app\.plugins\.plugins\["taelgar-dataview-materializer"\]/);
  assert.match(code, /plugin\.runRequest/);
  assert.match(code, /"id":"abc"/);
});

test("buildObsidianCliArgs uses eval code and optional vault target", () => {
  assert.deepEqual(buildObsidianCliArgs({ code: "1 + 1" }), ["eval", "code=1 + 1"]);
  assert.deepEqual(buildObsidianCliArgs({ code: "1 + 1", vaultTarget: "Taelgar" }), [
    "vault=Taelgar",
    "eval",
    "code=1 + 1",
  ]);
});

test("resolveObsidianCommand preserves explicit command", async () => {
  assert.equal(await resolveObsidianCommand("/custom/obsidian"), "/custom/obsidian");
});

test("formatProgressLine describes startup before file counts are known", () => {
  assert.equal(
    formatProgressLine({ status: "starting", fileIndex: 0, totalFiles: 0 }, { columns: 120 }),
    "Materializing: starting Obsidian runtime and waiting for Dataview/CustomJS",
  );
});

test("formatProgressLine includes useful running counts", () => {
  const line = formatProgressLine(
    {
      status: "running",
      fileIndex: 50,
      totalFiles: 100,
      currentFile: "People/Example.md",
      counts: {
        filesChanged: 20,
        headersRegenerated: 15,
        dataviewBlocks: 3,
        dataviewJsBlocks: 4,
        inlineExpressions: 100,
        errors: 1,
        unsupported: 2,
      },
    },
    { width: 10, columns: 200 },
  );

  assert.match(line, /50\/100/);
  assert.match(line, /50\.0%/);
  assert.match(line, /headers 15/);
  assert.match(line, /dv 7/);
  assert.match(line, /inline 100/);
  assert.match(line, /People\/Example\.md/);
});

test("truncateLine shortens long progress lines", () => {
  assert.equal(truncateLine("abcdefghijklmnopqrstuvwxyz", 10), "abcdefg...");
});

test("formatWaitingForProgressLine explains long startup waits", () => {
  assert.match(formatWaitingForProgressLine("/tmp/report.progress.json", 65000), /waiting 65s/);
  assert.match(formatWaitingForProgressLine("/tmp/report.progress.json", 65000), /has not written startup progress/);
});

test("writePrefixedLines prefixes non-empty process output lines", () => {
  let output = "";
  const stream = {
    write(value) {
      output += value;
    },
  };

  writePrefixedLines(stream, "CLI: ", "one\n\n two \n");

  assert.equal(output, "CLI: one\nCLI:  two \n");
});

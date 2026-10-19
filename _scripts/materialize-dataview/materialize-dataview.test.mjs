import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import {
  buildEvalCode,
  buildMaterializerRequest,
  buildObsidianCliArgs,
  formatWaitingForProgressLine,
  formatProgressLine,
  formatReportOutcome,
  parseArgs,
  summarizeReport,
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

test("parseArgs defaults to obsidian-cli", () => {
  assert.equal(parseArgs([]).obsidianCommand, "obsidian-cli");
  assert.equal(parseArgs([]).dynamicWebsite, false);
});

test("dynamic-website requests disable static header regeneration regardless of option order", () => {
  for (const argv of [
    ["--dynamic-website"],
    ["--header-type", "website", "--dynamic-website"],
    ["--dynamic-website", "--header-type", "static"],
  ]) {
    const args = parseArgs(argv);
    const { request } = buildMaterializerRequest(args, { cwd: "/tmp/Taelgar" });
    assert.equal(args.dynamicWebsite, true);
    assert.equal(request.config.dynamicWebsite, true);
    assert.equal(request.config.headerType, "none");
    assert.match(buildEvalCode(request), /"dynamicWebsite":true/);
  }
});

test("parseArgs rejects removed protocol bridge options", () => {
  assert.throws(
    () => parseArgs(["--launcher", "open {url}"]),
    /official Obsidian CLI/,
  );
});

test("parseArgs rejects overall materialization timeout", () => {
  assert.throws(
    () => parseArgs(["--timeout", "600"]),
    /--timeout was removed/,
  );
});

test("buildMaterializerRequest resolves defaults", () => {
  const { request, reportPath } = buildMaterializerRequest(
    {
      outputPath: "/tmp/Taelgar-static",
      strict: false,
      blockTimeoutMs: 30000,
    },
    { cwd: "/tmp/Taelgar", id: "test-run" },
  );

  assert.equal(request.id, "test-run");
  assert.equal(request.config.vaultPath, path.resolve("/tmp/Taelgar"));
  assert.equal(request.config.outputPath, path.resolve("/tmp/Taelgar-static"));
  assert.equal(request.config.mode, "write");
  assert.equal(request.config.strict, false);
  assert.equal(request.config.dynamicWebsite, false);
  assert.equal(request.config.headerType, "website");
  assert.equal("timeoutMs" in request.config, false);
  assert.equal(reportPath, path.resolve("/tmp/Taelgar-static/.dataview-materialization-report.json"));
});

test("dynamic write requests require the Node copy phase while audit and legacy no-wait behavior remains", () => {
  const result = buildMaterializerRequest(parseArgs(["--out", "/tmp/output", "--dynamic-website"]), { cwd: "/tmp/vault", id: "handoff" });
  assert.equal(result.request.config.externalCopy, true);
  assert.equal(result.request.config.requestId, "handoff");
  assert.equal(path.dirname(result.request.config.stagedMarkdownPath), result.outputPath);
  const customReport = buildMaterializerRequest(parseArgs(["--out", "/tmp/output", "--report", "/tmp/reports/job.json", "--dynamic-website"]));
  assert.equal(path.dirname(customReport.request.config.stagedMarkdownPath), customReport.outputPath);
  assert.throws(() => buildMaterializerRequest(parseArgs(["--out", "/tmp/output", "--dynamic-website", "--no-wait"])), /Node CLI must finish/);
  assert.equal(buildMaterializerRequest(parseArgs(["--out", "/tmp/output", "--no-wait"])).request.config.externalCopy, false);
});

test("copy progress identifies the phase and current file instead of showing the last note at 100 percent", () => {
  const line = formatProgressLine({ status: "running", phase: "copying", filesCopied: 12, bytesCopied: 2097152, currentFile: "assets/image.png" }, { columns: 200 });
  assert.match(line, /Copying output: 12 files, 2\.0 MiB/);
  assert.match(line, /assets\/image\.png/);
  assert.doesNotMatch(line, /100.*%/);
});

test("buildEvalCode invokes plugin runRequest", () => {
  const code = buildEvalCode({ id: "abc", config: { mode: "audit" } });

  assert.match(code, /app\.plugins\.plugins\["taelgar-dataview-materializer"\]/);
  assert.match(code, /plugin\.runRequest/);
  assert.match(code, /"id":"abc"/);
});

test("dynamic requests reject an outdated loaded plugin before materialization and write a failure report", async () => {
  let called = false, written;
  const plugin = {
    runRequest: async () => { called = true; },
    writeReport: async (file, report) => { written = { file, report }; },
  };
  const request = { id: "stale-plugin", config: { dynamicWebsite: true, reportPath: "/tmp/report.json" } };
  const result = await vm.runInNewContext(buildEvalCode(request), { app: { plugins: { plugins: { "taelgar-dataview-materializer": plugin } } } });
  assert.equal(called, false);
  assert.match(result, /Reload.*plugin or restart Obsidian/);
  assert.equal(written.file, request.config.reportPath);
  assert.equal(written.report.id, request.id);
  assert.equal(written.report.status, "failed");
  assert.equal(written.report.exitCode, 1);
});

test("dynamic writes require a loaded plugin that supports handing the copy phase to Node", async () => {
  let called = false, written;
  const plugin = { supportsDynamicWebsite: true, runRequest: async () => { called = true; }, writeReport: async (_path, report) => { written = report; } };
  await vm.runInNewContext(buildEvalCode({ id: "handoff", config: { dynamicWebsite: true, externalCopy: true, reportPath: "/tmp/report.json" } }), { app: { plugins: { plugins: { "taelgar-dataview-materializer": plugin } } } });
  assert.equal(called, false);
  assert.equal(written.exitCode, 1);
  assert.match(written.error.message, /Reload.*plugin or restart Obsidian/);
});

test("eval dispatch supports current dynamic plugins and unchanged legacy requests", async () => {
  for (const [config, supportsDynamicWebsite] of [[{ dynamicWebsite: true }, true], [{ mode: "audit" }, undefined]]) {
    let received;
    const plugin = { supportsDynamicWebsite, runRequest: async (request) => { received = request; } };
    await vm.runInNewContext(buildEvalCode({ id: "dispatch", config }), { app: { plugins: { plugins: { "taelgar-dataview-materializer": plugin } } } });
    assert.equal(received.id, "dispatch");
    assert.equal(received.config.dynamicWebsite, config.dynamicWebsite);
    assert.equal(received.config.mode, config.mode);
  }
});

test("failed strict exports clearly explain why output was not written and identify query issues", () => {
  const text = formatReportOutcome({ status: "failed", exitCode: 1, mode: "write", strict: true,
    counts: { filesScanned: 3, errors: 1, unsupported: 2 },
    files: [{ path: "Fixture.md", issues: [{ type: "error", line: 7, message: "Query parse\nfailed" }] }],
  }, "/tmp/report.json");
  assert.match(text, /Strict mode blocked writing vault output/);
  assert.match(text, /errors 1; unsupported 2/);
  assert.match(text, /Fixture\.md:7 \[error\]: Query parse failed/);
  assert.match(text, /--no-strict/);
  assert.match(text, /Report: \/tmp\/report\.json/);
});

test("non-strict exports disclose partial output and remaining blocks", () => {
  const text = formatReportOutcome({ status: "ok", exitCode: 0, mode: "write", strict: false,
    outputPath: "/tmp/output", counts: { filesScanned: 2, errors: 1, unsupported: 0 },
  }, "/tmp/report.json");
  assert.match(text, /completed with partial output/);
  assert.match(text, /Output: \/tmp\/output/);
  assert.match(text, /blocks remain unchanged/);
  assert.doesNotMatch(text, /blocked writing/);
});

test("startup failure reports print the error even without counts", () => {
  const text = formatReportOutcome({ status: "failed", exitCode: 1, error: { message: "Reload the plugin." } }, "/tmp/report.json");
  assert.match(text, /Materialization failed/);
  assert.match(text, /Reload the plugin/);
  assert.match(text, /Report:/);
});

test("buildObsidianCliArgs uses eval code and optional vault target", () => {
  assert.deepEqual(buildObsidianCliArgs({ code: "1 + 1" }), ["eval", "code=1 + 1"]);
  assert.deepEqual(buildObsidianCliArgs({ code: "1 + 1", vaultTarget: "Taelgar" }), [
    "vault=Taelgar",
    "eval",
    "code=1 + 1",
  ]);
});

test("summarizeReport includes performance timings when present", () => {
  const summary = summarizeReport({
    status: "ok",
    exitCode: 0,
    mode: "write",
    strict: false,
    dynamicWebsite: true,
    counts: {
      filesScanned: 2,
      filesSkipped: 1,
      filesChanged: 2,
      dataviewBlocks: 0,
      dataviewJsBlocks: 0,
      inlineExpressions: 0,
      headersRegenerated: 2,
      unsupported: 0,
      errors: 0,
      remainingDataviewBlocks: 0,
      remainingDataviewJsBlocks: 0,
      remainingInlineExpressions: 0,
    },
    performance: {
      totalMs: 100,
      prepareRuntimeMs: 10,
      processFilesMs: 70,
      copyMs: 20,
      timingTotals: {
        readMs: 30,
        headerMs: 5,
        dataviewMs: 10,
        dataviewJsMs: 20,
        inlineMs: 0,
        totalFileMs: 65,
      },
      slowFiles: [{ path: "A.md", totalMs: 50 }],
    },
  });

  assert.equal(summary.performance.totalMs, 100);
  assert.equal(summary.dynamicWebsite, true);
  assert.equal(summary.performance.timingTotals.readMs, 30);
  assert.deepEqual(summary.performance.slowFiles, [{ path: "A.md", totalMs: 50 }]);
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

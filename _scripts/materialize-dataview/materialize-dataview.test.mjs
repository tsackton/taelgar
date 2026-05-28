import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import {
  buildEvalCode,
  buildMaterializerRequest,
  buildObsidianCliArgs,
  parseArgs,
  resolveObsidianCommand,
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
  ]);

  assert.equal(args.vaultPath, "/tmp/Taelgar");
  assert.equal(args.outputPath, "/tmp/Taelgar-static");
  assert.equal(args.strict, false);
  assert.equal(args.obsidianCommand, "/bin/obsidian");
  assert.equal(args.obsidianVault, "Taelgar");
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

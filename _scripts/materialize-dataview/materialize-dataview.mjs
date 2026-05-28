#!/usr/bin/env node

import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import { spawn, spawnSync } from "node:child_process";

const PLUGIN_ID = "taelgar-dataview-materializer";
const PROTOCOL_ACTION = "taelgar-materializer";

function parseArgs(argv) {
  const args = {
    strict: true,
    timeoutMs: 120000,
    blockTimeoutMs: 30000,
    protocolDelayMs: 10000,
    requestOnly: false,
    vaultRequest: false,
    wait: true,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    const next = () => {
      index += 1;
      if (index >= argv.length) throw new Error(`Missing value for ${arg}`);
      return argv[index];
    };

    if (arg === "--vault") args.vaultPath = next();
    else if (arg === "--out" || arg === "--output") args.outputPath = next();
    else if (arg === "--date") args.overrideDate = next();
    else if (arg === "--mode") args.mode = next();
    else if (arg === "--report") args.reportPath = next();
    else if (arg === "--request-path") args.requestPath = next();
    else if (arg === "--timeout") args.timeoutMs = Number(next()) * 1000;
    else if (arg === "--block-timeout") args.blockTimeoutMs = Number(next()) * 1000;
    else if (arg === "--protocol-delay") args.protocolDelayMs = Number(next()) * 1000;
    else if (arg === "--launcher") args.launcher = next();
    else if (arg === "--strict") args.strict = true;
    else if (arg === "--no-strict") args.strict = false;
    else if (arg === "--request-only") args.requestOnly = true;
    else if (arg === "--vault-request") args.vaultRequest = true;
    else if (arg === "--no-wait") args.wait = false;
    else if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

function printHelp() {
  console.log(`Usage:
  materialize-dataview --vault /path/to/Taelgar --out /path/to/Taelgar-static --date YYYY-MM-DD --strict

Options:
  --vault PATH       Source Obsidian vault. Defaults to the current working directory.
  --out PATH         Output vault path. Enables write mode unless --mode is supplied.
  --mode MODE        audit, write, or check. Defaults to write when --out is set, otherwise audit.
  --date DATE        Override CustomJS target date.
  --report PATH      Report JSON path.
  --request-path PATH
                    Request JSON path. Defaults to a temp file outside the vault.
  --strict           Fail when unsupported blocks or errors are found. Default.
  --no-strict        Produce partial output and report unsupported blocks.
  --timeout SECONDS  Time to wait for Obsidian to finish. Default: 120.
  --block-timeout SECONDS
                    Per-block Dataview render timeout. Default: 30.
  --protocol-delay SECONDS
                    Delay before sending the materializer protocol URL. Default: 10.
  --launcher CMD     Command used to open the Obsidian protocol URL.
  --vault-request    Use the legacy request file inside .obsidian/plugins.
  --request-only     Write the plugin request and do not launch Obsidian.
  --no-wait          Launch Obsidian but do not wait for the report.
`);
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const vaultPath = path.resolve(args.vaultPath || process.cwd());
  const mode = args.mode || (args.outputPath ? "write" : "audit");
  const id = `materialize-${Date.now()}`;
  const pluginDir = path.join(vaultPath, ".obsidian", "plugins", PLUGIN_ID);
  const requestPath = path.resolve(
    args.requestPath ||
      (args.vaultRequest
        ? path.join(pluginDir, "request.json")
        : path.join(os.tmpdir(), PLUGIN_ID, `${id}.request.json`)),
  );
  const outputPath = args.outputPath ? path.resolve(args.outputPath) : undefined;
  const reportPath = path.resolve(
    args.reportPath ||
      (outputPath
        ? path.join(outputPath, ".dataview-materialization-report.json")
        : path.join(pluginDir, "last-report.json")),
  );

  const request = {
    id,
    config: {
      vaultPath,
      outputPath,
      mode,
      strict: args.strict,
      reportPath,
      progressPath: `${reportPath}.progress.json`,
      overrideDate: args.overrideDate,
      timeoutMs: args.timeoutMs,
      blockTimeoutMs: args.blockTimeoutMs,
    },
  };

  await fs.mkdir(path.dirname(requestPath), { recursive: true });
  await fs.rm(reportPath, { force: true });
  await fs.rm(`${reportPath}.progress.json`, { force: true });
  await fs.writeFile(requestPath, JSON.stringify(request, null, 2) + "\n", "utf8");

  if (args.requestOnly) {
    console.log(`Wrote request: ${requestPath}`);
    console.log(`Report path: ${reportPath}`);
    return;
  }

  const url = `obsidian://open?vault=${encodeURIComponent(path.basename(vaultPath))}`;
  launchObsidian(url, args.launcher || process.env.OBSIDIAN_MATERIALIZER_LAUNCHER);
  await sleep(args.protocolDelayMs);
  launchObsidian(
    `obsidian://${PROTOCOL_ACTION}?request=${encodeURIComponent(requestPath)}`,
    args.launcher || process.env.OBSIDIAN_MATERIALIZER_LAUNCHER,
  );

  if (!args.wait) {
    console.log(`Report path: ${reportPath}`);
    return;
  }

  const report = await waitForReport(reportPath, args.timeoutMs, id);
  console.log(JSON.stringify(summarizeReport(report), null, 2));
  process.exitCode = report.exitCode || 0;
}

function launchObsidian(url, launcher) {
  if (launcher) {
    const command = launcher.includes("{url}") ? launcher.replace("{url}", url) : `${launcher} ${url}`;
    const child = spawn(command, {
      shell: true,
      stdio: "ignore",
      detached: true,
    });
    child.unref();
    return;
  }

  if (process.platform === "darwin") {
    const result = spawnSync("open", [url], { stdio: "inherit" });
    if (result.status !== 0) {
      throw new Error(`Failed to open Obsidian URL: ${url}`);
    }
    return;
  }

  const child = spawn("xdg-open", [url], {
    stdio: "ignore",
    detached: true,
  });
  child.unref();
}

async function waitForReport(reportPath, timeoutMs, expectedId) {
  const deadline = Date.now() + timeoutMs;
  let lastError;

  while (Date.now() < deadline) {
    try {
      const report = JSON.parse(await fs.readFile(reportPath, "utf8"));
      if (!expectedId || report.id === expectedId) return report;
      lastError = new Error(`found report for ${report.id}, waiting for ${expectedId}`);
    } catch (error) {
      lastError = error;
      await sleep(1000);
    }
  }

  throw new Error(`Timed out waiting for report at ${reportPath}: ${lastError?.message || "not found"}`);
}

function summarizeReport(report) {
  if (!report.counts) return report;
  return {
    status: report.status,
    exitCode: report.exitCode,
    mode: report.mode,
    strict: report.strict,
    filesScanned: report.counts.filesScanned,
    filesSkipped: report.counts.filesSkipped,
    filesChanged: report.counts.filesChanged,
    dataviewBlocks: report.counts.dataviewBlocks,
    dataviewJsBlocks: report.counts.dataviewJsBlocks,
    inlineExpressions: report.counts.inlineExpressions,
    unsupported: report.counts.unsupported,
    errors: report.counts.errors,
    remaining: {
      dataviewBlocks: report.counts.remainingDataviewBlocks,
      dataviewJsBlocks: report.counts.remainingDataviewJsBlocks,
      inlineExpressions: report.counts.remainingInlineExpressions,
    },
  };
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});

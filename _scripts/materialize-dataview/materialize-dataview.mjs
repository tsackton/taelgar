#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

const PLUGIN_ID = "taelgar-dataview-materializer";
const DEFAULT_OBSIDIAN_COMMAND = "obsidian";
const MACOS_OBSIDIAN_CLI = "/Applications/Obsidian.app/Contents/MacOS/obsidian";

export function parseArgs(argv) {
  const args = {
    strict: true,
    timeoutMs: 120000,
    blockTimeoutMs: 30000,
    wait: true,
    obsidianCommand: process.env.OBSIDIAN_COMMAND || DEFAULT_OBSIDIAN_COMMAND,
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
    else if (arg === "--timeout") args.timeoutMs = Number(next()) * 1000;
    else if (arg === "--block-timeout") args.blockTimeoutMs = Number(next()) * 1000;
    else if (arg === "--obsidian-command" || arg === "--obsidian-cli") {
      args.obsidianCommand = next();
    } else if (arg === "--obsidian-vault") {
      args.obsidianVault = next();
    } else if (arg === "--strict") args.strict = true;
    else if (arg === "--no-strict") args.strict = false;
    else if (arg === "--no-wait") args.wait = false;
    else if (
      [
        "--launcher",
        "--protocol-delay",
        "--request-only",
        "--request-path",
        "--vault-request",
      ].includes(arg)
    ) {
      throw new Error(`${arg} was removed; this wrapper now uses the official Obsidian CLI.`);
    } else if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

export function printHelp() {
  console.log(`Usage:
  materialize-dataview --vault /path/to/Taelgar --out /path/to/Taelgar-static --date YYYY-MM-DD --strict

Options:
  --vault PATH       Source Obsidian vault. Defaults to the current working directory.
  --out PATH         Output vault path. Enables write mode unless --mode is supplied.
  --mode MODE        audit, write, or check. Defaults to write when --out is set, otherwise audit.
  --date DATE        Override CustomJS target date.
  --report PATH      Report JSON path.
  --strict           Fail when unsupported blocks or errors are found. Default.
  --no-strict        Produce partial output and report unsupported blocks.
  --timeout SECONDS  Time to wait for Obsidian to finish. Default: 120.
  --block-timeout SECONDS
                    Per-block Dataview render timeout. Default: 30.
  --obsidian-command PATH
                    Official Obsidian CLI command. Defaults to OBSIDIAN_COMMAND or "obsidian".
  --obsidian-vault NAME_OR_ID
                    Optional explicit Obsidian vault target. By default the CLI runs with
                    the source vault as its working directory.
  --no-wait          Run the CLI request and print the report path without reading it.
`);
}

export function buildMaterializerRequest(args, options = {}) {
  const cwd = options.cwd || process.cwd();
  const vaultPath = path.resolve(args.vaultPath || cwd);
  const mode = args.mode || (args.outputPath ? "write" : "audit");
  const id = options.id || `materialize-${Date.now()}`;
  const pluginDir = path.join(vaultPath, ".obsidian", "plugins", PLUGIN_ID);
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

  return { request, vaultPath, outputPath, reportPath };
}

export function buildEvalCode(request) {
  return `(async () => {
  const plugin = app.plugins.plugins[${JSON.stringify(PLUGIN_ID)}];
  if (!plugin) throw new Error(${JSON.stringify(`Plugin not loaded: ${PLUGIN_ID}`)});
  if (typeof plugin.runRequest !== "function") {
    throw new Error(${JSON.stringify(`Plugin does not expose runRequest(): ${PLUGIN_ID}`)});
  }
  await plugin.runRequest(${JSON.stringify(request)});
  return ${JSON.stringify(`Materializer request ${request.id} finished`)};
})()`;
}

export function buildObsidianCliArgs({ code, vaultTarget } = {}) {
  const args = [];
  if (vaultTarget) args.push(`vault=${vaultTarget}`);
  args.push("eval", `code=${code}`);
  return args;
}

export async function runObsidianCli(command, args, options = {}) {
  const timeoutMs = options.timeoutMs;

  return new Promise((resolve, reject) => {
    let settled = false;
    let stdout = "";
    let stderr = "";

    const child = spawn(command, args, {
      cwd: options.cwd,
      stdio: ["ignore", "pipe", "pipe"],
    });

    const finish = (callback, value) => {
      if (settled) return;
      settled = true;
      if (timer) clearTimeout(timer);
      callback(value);
    };

    const timer = timeoutMs
      ? setTimeout(() => {
          child.kill("SIGTERM");
          finish(
            reject,
            new Error(`Obsidian CLI timed out after ${Math.round(timeoutMs / 1000)} seconds.`),
          );
        }, timeoutMs)
      : undefined;

    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });

    child.on("error", (error) => {
      if (error.code === "ENOENT") {
        finish(
          reject,
          new Error(
            `Obsidian CLI command not found: ${command}. ` +
              `Pass --obsidian-command or set OBSIDIAN_COMMAND to the registered CLI path.`,
          ),
        );
      } else {
        finish(reject, error);
      }
    });

    child.on("close", (code, signal) => {
      if (code === 0) {
        finish(resolve, { stdout, stderr });
        return;
      }

      const suffix = [
        signal ? `signal ${signal}` : `exit code ${code}`,
        stderr.trim() ? `stderr:\n${stderr.trim()}` : undefined,
        stdout.trim() ? `stdout:\n${stdout.trim()}` : undefined,
      ]
        .filter(Boolean)
        .join("\n");
      finish(reject, new Error(`Obsidian CLI failed with ${suffix}`));
    });
  });
}

export async function resolveObsidianCommand(command) {
  if (command !== DEFAULT_OBSIDIAN_COMMAND) return command;

  if (process.platform === "darwin") {
    try {
      await fs.access(MACOS_OBSIDIAN_CLI);
      return MACOS_OBSIDIAN_CLI;
    } catch {
      // Fall through to PATH lookup for nonstandard installs.
    }
  }

  return command;
}

export async function waitForReport(reportPath, timeoutMs, expectedId) {
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

export function summarizeReport(report) {
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

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const { request, vaultPath, reportPath } = buildMaterializerRequest(args);

  await fs.rm(reportPath, { force: true });
  await fs.rm(`${reportPath}.progress.json`, { force: true });

  const code = buildEvalCode(request);
  const obsidianArgs = buildObsidianCliArgs({
    code,
    vaultTarget: args.obsidianVault,
  });
  const obsidianCommand = await resolveObsidianCommand(args.obsidianCommand);

  await runObsidianCli(obsidianCommand, obsidianArgs, {
    cwd: vaultPath,
    timeoutMs: args.timeoutMs + 30000,
  });

  if (!args.wait) {
    console.log(`Report path: ${reportPath}`);
    return;
  }

  const report = await waitForReport(reportPath, args.timeoutMs, request.id);
  console.log(JSON.stringify(summarizeReport(report), null, 2));
  process.exitCode = report.exitCode || 0;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const isMain =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  });
}

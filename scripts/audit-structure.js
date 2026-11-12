#!/usr/bin/env node
"use strict";

const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();
const canonicalControlPlane = [
  "sentinel-manager.md",
  "verifier-officer.md",
  "operator.md",
  "researcher.md",
  "critical-analyst.md",
  "co-developer.md",
  "IDENTIFIER_NAMING_STANDARD.md",
  "VERIFICATION_TRACEABILITY_MATRIX.md",
];
const required = [
  ...canonicalControlPlane.map((name) => path.join("00_Control_Plane_v4.0", name)),
  "GEMINI.md",
  path.join("01_Governance_Rules", "SOURCE_OF_TRUTH.md"),
];
const failures = [];

for (const relative of required) {
  const absolute = path.join(root, relative);
  if (!fs.existsSync(absolute) || !fs.statSync(absolute).isFile()) {
    failures.push(`Missing required canonical file: ${relative}`);
    continue;
  }
  const header = fs.readFileSync(absolute, "utf8").split(/\r?\n/).slice(0, 20).join("\n");
  if (/^\s*(?:\*\*Status:\*\*|Status:)\s*[^\n]*\bDRAFT\b/im.test(header)) {
    failures.push(`Canonical file has a DRAFT status header: ${relative}`);
  }
}

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules" || entry.name === "02_Archive_Legacy") continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(absolute);
    else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) auditLinks(absolute);
  }
}

function auditLinks(file) {
  const content = fs.readFileSync(file, "utf8");
  const markdownLink = /!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+["'][^"']*["'])?\)/g;
  for (const match of content.matchAll(markdownLink)) {
    let target = match[1].replace(/^<|>$/g, "");
    if (/^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i.test(target)) continue;
    target = target.split("#", 1)[0].split("?", 1)[0];
    if (!target) continue;
    try { target = decodeURIComponent(target); }
    catch { failures.push(`Malformed link encoding in ${path.relative(root, file)}: ${match[1]}`); continue; }
    const resolved = path.resolve(path.dirname(file), target);
    if (!fs.existsSync(resolved)) {
      failures.push(`Broken relative Markdown link in ${path.relative(root, file)}: ${match[1]}`);
    }
  }
}

walk(root);
if (failures.length) {
  console.error(`Structure/link audit failed with ${failures.length} issue(s):`);
  for (const failure of failures) console.error(` - ${failure}`);
  process.exit(1);
}
console.log(`Structure/link audit passed: ${required.length} canonical files present, no DRAFT status headers, and active Markdown relative links resolve.`);

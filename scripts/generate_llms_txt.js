#!/usr/bin/env node
/**
 * Regenerate docs/llms.txt with readable section titles + all paths.
 * Usage: node scripts/generate_llms_txt.js
 *
 * Prefer hand-editing llms.txt when you only tweak wording;
 * run this after adding/removing many pages.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const DOCS = path.join(ROOT, 'docs');
const OUT = path.join(DOCS, 'llms.txt');
const SKIP = new Set(['SUMMARY.md']);

const SECTIONS = [
  ['_root', 'Intro (what TBL is)'],
  ['start-here', 'Start here (first bot)'],
  ['tutorials', 'Tutorials list'],
  ['getting-started-with-tbl', 'Commands (headers, answer, keyboard, matching)'],
  ['guides', 'Guides'],
  ['globals', 'Globals (user, chat, params, message, …)'],
  ['bot-instance', 'Bot helpers (current chat)'],
  ['api-instance', 'Api (full Telegram API)'],
  ['msg-instance', 'msg helpers'],
  ['db-instance', 'Database (db.bot / db.user / db.global)'],
  ['http-instance', 'HTTP client (outbound)'],
  ['webhook-instance', 'Webhooks (inbound)'],
  ['webapp-instance', 'Webapps / public web'],
  ['res-instance', 'res (HTTP reply for web/webhook)'],
  ['modules', 'Modules (modules.*)'],
  ['libs', 'Libs (Libs.*)'],
  ['tbl-instance', 'Bot account (clone / transfer)'],
  ['user-instance', 'Old storage docs (prefer /db-instance/)'],
  ['global-instance', 'Old storage docs (prefer /db-instance/)']
];

function walk(dir, base = '') {
  let out = [];
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const rel = path.posix.join(base, ent.name);
    if (ent.isDirectory()) out = out.concat(walk(path.join(dir, ent.name), rel));
    else if (ent.name.endsWith('.md') && !SKIP.has(ent.name)) out.push(rel);
  }
  return out;
}

function srcToPath(rel) {
  if (rel === 'index.md') return '/';
  if (rel.endsWith('/index.md')) return `/${rel.slice(0, -'index.md'.length)}`;
  return `/${rel.slice(0, -3)}/`;
}

function sectionKey(rel) {
  return rel.includes('/') ? rel.split('/')[0] : '_root';
}

const pages = walk(DOCS).sort();
const by = {};
for (const rel of pages) {
  const key = sectionKey(rel);
  (by[key] = by[key] || []).push(rel);
}

const lines = [
  '# TeleBotHost docs — path index for AI',
  '# Site: https://docs.telebothost.com',
  '# Open ONE path: https://docs.telebothost.com{path}',
  '# Plain map: /for-agents/',
  ''
];

const seenDeprecated = new Set();
const known = new Set(SECTIONS.map(([k]) => k));

for (const [key, title] of SECTIONS) {
  const rels = by[key];
  if (!rels) continue;

  if (key === 'user-instance' || key === 'global-instance') {
    if (!seenDeprecated.has('old')) {
      lines.push(`## ${title}`);
      seenDeprecated.add('old');
    }
  } else {
    lines.push(`## ${title}`);
  }

  rels
    .slice()
    .sort((a, b) => {
      const ai = a.endsWith('index.md') || !a.includes('/') ? 0 : 1;
      const bi = b.endsWith('index.md') || !b.includes('/') ? 0 : 1;
      return ai - bi || a.localeCompare(b);
    })
    .forEach((rel) => lines.push(srcToPath(rel)));
  lines.push('');
}

for (const key of Object.keys(by).sort()) {
  if (known.has(key)) continue;
  lines.push(`## ${key}`);
  by[key].sort().forEach((rel) => lines.push(srcToPath(rel)));
  lines.push('');
}

fs.writeFileSync(OUT, `${lines.join('\n').trim()}\n`, 'utf8');
console.log(`Wrote ${OUT} (${pages.length} paths)`);

// Modified by Acrazie on 2026-11-03 for the independent EGM fork.
// Copyright 2026 Google LLC. SPDX-License-Identifier: Apache-2.0

import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('the public catalog exposes exactly four supported commands', () => {
  const source = readFileSync(new URL('../../docs/site/skills.md', import.meta.url), 'utf8');
  const commands = [...source.matchAll(/`\/(egm-[a-z-]+)`/g)].map((match) => match[1]);
  assert.deepEqual([...new Set(commands)].sort(), ['egm-bootstrap', 'egm-design', 'egm-drift-report', 'egm-review']);
  for (const command of commands) {
    assert.ok(existsSync(new URL(`../../skills/${command}/SKILL.md`, import.meta.url)), command);
  }
});

test('all catalog icon imports resolve after removing retired skills', () => {
  const source = readFileSync(new URL('../src/components/SkillIcon.astro', import.meta.url), 'utf8');
  const imports = [...source.matchAll(/from '([^']+)\?url'/g)];
  assert.equal(imports.length, 4);
  const component = new URL('../src/components/SkillIcon.astro', import.meta.url);
  for (const [, path] of imports) assert.ok(existsSync(new URL(path, component)), path);
});

test('fork catalog and installation links agree with the published repository identity', () => {
  const { repository } = JSON.parse(readFileSync(new URL('../../plugin.json', import.meta.url), 'utf8'));
  for (const name of ['Footer', 'Nav', 'Home']) {
    const source = readFileSync(new URL(`../src/components/${name}.astro`, import.meta.url), 'utf8');
    assert.ok(source.includes(repository), `${name} points to another repository`);
  }
  const install = readFileSync(new URL('../../docs/site/install.md', import.meta.url), 'utf8');
  const slug = new URL(repository).pathname.slice(1);
  assert.ok(install.includes(`claude plugin marketplace add ${slug}`));
  assert.ok(install.includes(`codex plugin marketplace add ${slug}`));
});

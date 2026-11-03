// Modified by Acrazie on 2026-11-03 for the independent EGM fork.
// Copyright 2026 Google LLC. SPDX-License-Identifier: Apache-2.0

import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import test from 'node:test';

test('the public catalog exposes exactly four supported commands', () => {
  const source = readFileSync(new URL('../src/components/Skills.astro', import.meta.url), 'utf8');
  const commands = [...source.matchAll(/command: '\/(egm-[a-z-]+)'/g)].map((match) => match[1]);
  assert.deepEqual(commands.sort(), ['egm-bootstrap', 'egm-design', 'egm-drift-report', 'egm-review']);
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

test('the main journey requires one explicit command rather than three invocations', () => {
  const source = readFileSync(new URL('../src/components/Loop.astro', import.meta.url), 'utf8');
  const commands = [...source.matchAll(/command: '\/(egm-[a-z-]+)'/g)].map((match) => match[1]);
  assert.deepEqual(commands, ['egm-design']);
});

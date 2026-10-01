// Run with: node --test .agents/skills/transcribe-session/scripts/test_review_pages.js
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

function page(name) {
  const html = fs.readFileSync(path.join(__dirname, '..', 'assets', name), 'utf8');
  const element = {addEventListener() {}, classList: {toggle() {}}, style: {}};
  const context = vm.createContext({
    document: {
      getElementById: () => element,
      addEventListener() {},
      querySelectorAll: () => [],
    },
    // Keep the automatic initial load pending; each test supplies its response.
    fetch: () => new Promise(() => {}),
    alert: () => {},
    setInterval, clearInterval,
  });
  vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
  vm.runInContext(`
    var moves = 0, renders = 0;
    render = () => { renders += 1; };
    if (typeof moveToNextUnreviewed === 'function') moveToNextUnreviewed = () => { moves += 1; };
    if (typeof moveToNextOpen === 'function') moveToNextOpen = () => { moves += 1; };
  `, context);
  return {
    context,
    run: code => vm.runInContext(code, context),
    value: code => JSON.parse(vm.runInContext(`JSON.stringify(${code})`, context)),
  };
}

function reviewPage() {
  const p = page('speaker-review.html');
  p.run(`
    state.mode = 'exceptions';
    state.labels = {
      schemaVersion: 1, reviewId: 'test', updatedAt: null,
      groupLabels: {},
      utteranceOverrides: {cue: {status: 'assigned', participantId: 'p01', modelMargin: 0.2}},
      verification: {p01: {status: 'confirmed', sampleUtteranceIds: ['cue']}}
    };
    state.savedLabels = JSON.stringify(state.labels);
  `);
  return p;
}

function reject(p) {
  p.context.fetch = async () => ({ok: false, json: async () => ({error: 'write refused'})});
}

function accept(p) {
  p.context.fetch = async () => ({ok: true, json: async () => ({updatedAt: 'saved'})});
}

test('failed speaker save restores labels and confirmations without advancing', async () => {
  const p = reviewPage();
  const before = p.value('state.labels');
  reject(p);
  await p.run("setLabel({id: 'cue'}, 'assigned', 'p02')");
  assert.deepEqual(p.value('state.labels'), before);
  assert.equal(p.run('moves'), 0);
  assert.equal(p.run('state.saving'), false);
});

test('speaker correction advances only after saving and invalidates affected confirmation', async () => {
  const p = reviewPage();
  accept(p);
  await p.run("setLabel({id: 'cue'}, 'assigned', 'p02')");
  assert.deepEqual(p.value('state.labels.utteranceOverrides.cue'), {status: 'assigned', participantId: 'p02'});
  assert.deepEqual(p.value('state.labels.verification'), {});
  assert.equal(p.run('moves'), 1);
  assert.equal(p.run('state.labels.updatedAt'), 'saved');
});

test('focused reference changes and clears preserve existing confirmations', async () => {
  const p = reviewPage();
  const confirmation = p.value('state.labels.verification');
  p.run("state.referenceIds = ['cue']");
  accept(p);
  await p.run("setLabel({id: 'cue'}, 'assigned', 'p02')");
  assert.deepEqual(p.value('state.labels.verification'), confirmation);
  assert.equal(p.run('state.labels.utteranceOverrides.cue.humanVerified'), true);
  await p.run("clearLabel({id: 'cue'})");
  assert.deepEqual(p.value('state.labels.verification'), confirmation);
  assert.equal(p.run("'cue' in state.labels.utteranceOverrides"), false);
});

test('a second speaker click cannot change a pending save', async () => {
  const p = reviewPage();
  let complete;
  p.context.fetch = () => new Promise(resolve => { complete = resolve; });
  const first = p.run("setLabel({id: 'cue'}, 'assigned', 'p02')");
  await p.run("setLabel({id: 'other'}, 'unknown', null)");
  assert.equal(p.run("'other' in state.labels.utteranceOverrides"), false);
  complete({ok: true, json: async () => ({updatedAt: 'saved'})});
  await first;
  assert.equal(p.run('moves'), 1);
});

function auditPage() {
  const p = page('speaker-audit.html');
  p.run("state.decisions = {schemaVersion: 1, auditId: 'test', decisions: {}};");
  return p;
}

test('failed audit save leaves no completed decision and permits retry', async () => {
  const p = auditPage();
  reject(p);
  await p.run("saveDecision({id: 'clip'}, 'assigned', 'p01')");
  assert.deepEqual(p.value('state.decisions.decisions'), {});
  assert.equal(p.run('moves'), 0);
  accept(p);
  await p.run("saveDecision({id: 'clip'}, 'assigned', 'p01')");
  assert.equal(p.run('state.decisions.decisions.clip.participantId'), 'p01');
  assert.equal(p.run('moves'), 1);
});

test('failed audit correction retains the previously saved human decision', async () => {
  const p = auditPage();
  p.run("state.decisions.decisions.clip = {status: 'assigned', participantId: 'p01'};");
  reject(p);
  await p.run("saveDecision({id: 'clip'}, 'overlap', null)");
  assert.deepEqual(p.value('state.decisions.decisions.clip'), {status: 'assigned', participantId: 'p01'});
});

test('a second audit click cannot change a pending save', async () => {
  const p = auditPage();
  let complete;
  p.context.fetch = () => new Promise(resolve => { complete = resolve; });
  const first = p.run("saveDecision({id: 'clip'}, 'assigned', 'p01')");
  await p.run("saveDecision({id: 'clip'}, 'overlap', null)");
  assert.equal(p.run('state.decisions.decisions.clip.participantId'), 'p01');
  complete({ok: true});
  await first;
  assert.equal(p.run('moves'), 1);
});

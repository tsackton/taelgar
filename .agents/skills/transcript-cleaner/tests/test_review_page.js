const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

function page() {
  const html = fs.readFileSync(path.join(__dirname, '..', 'assets', 'cleanup-review.html'), 'utf8');
  const elements = {};
  const get = id => elements[id] ||= {textContent:'', value:'unsaved correction', disabled:false};
  const context = vm.createContext({
    document:{getElementById:get, querySelectorAll:()=>Object.values(elements)},
    fetch:()=>new Promise(()=>{}),
  });
  vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
  vm.runInContext(`state.review={issues:[{uid:'u0001'}, {uid:'u0002'}]}; var renders=0; render=()=>{renders++};`, context);
  return {context, elements, run:code=>vm.runInContext(code, context)};
}

test('failed save keeps text and position and allows retry', async () => {
  const p = page();
  p.context.fetch = async()=>({ok:false,json:async()=>({error:'write failed'})});
  await p.run("save({uid:'u0001',status:'correct',text:'A correction'})");
  assert.equal(p.run('state.index'), 0);
  assert.equal(p.run('renders'), 0);
  assert.equal(p.run('state.saving'), false);
  assert.equal(p.elements.status.textContent, 'write failed');
  assert.equal(p.run('Object.keys(state.decisions).length'), 0);
});

test('success advances only after decisions persist', async () => {
  const p=page();
  let resolve;
  p.context.fetch=()=>new Promise(r=>resolve=r);
  const pending=p.run("save({uid:'u0001',status:'skip'})");
  assert.equal(p.run('state.index'),0);
  await p.run('save({skipRemaining:true})');
  resolve({ok:true,json:async()=>({decisions:{u0001:{status:'skip'}}})});
  await pending;
  assert.equal(p.run('state.index'),1);
  assert.equal(p.run('renders'),1);
  assert.equal(p.run('state.saving'),false);
});

test('skip remaining completes the review without replacing saved corrections', async () => {
  const p=page();
  p.run("state.decisions={u0001:{status:'correct',text:'Nura'}}");
  p.context.fetch=async()=>({ok:true,json:async()=>({decisions:{u0001:{status:'correct',text:'Nura'},u0002:{status:'skip'}}})});
  await p.run('save({skipRemaining:true})');
  assert.equal(p.run('state.decisions.u0001.text'),'Nura');
  assert.match(p.elements.status.textContent,/Review complete/);
});

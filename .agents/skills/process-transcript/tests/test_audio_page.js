const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const test=require('node:test');
function page(){
 const elements={};const get=id=>elements[id]??={value:'Words I heard',textContent:'',disabled:false};
 const context=vm.createContext({document:{getElementById:get,querySelectorAll:()=>Object.values(elements)},window:{addEventListener:()=>{}},fetch:()=>new Promise(()=>{})});
 const html=fs.readFileSync(path.join(__dirname,'../assets/audio-review.html'),'utf8');
 vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
 const run=code=>vm.runInContext(code,context);
 run("state.items=[{key:'a',version:'v1',resolution:'pending'},{key:'b',version:'v2',resolution:'pending'}];var renders=0;render=()=>{renders++};");
 return {context,elements,run};
}
test('failed save preserves typed answer and position',async()=>{
 const p=page();p.context.fetch=async()=>({ok:false,json:async()=>({error:'Changed question'})});
 await p.run("save('answer')");
 assert.equal(p.run('state.index'),0);assert.equal(p.run('renders'),0);
 assert.equal(p.elements.answer.value,'Words I heard');assert.equal(p.elements.status.textContent,'Changed question');
 assert.equal(p.run('state.saving'),false);
});
test('save advances only after persistence and updates answer version',async()=>{
 const p=page();let finish;p.context.fetch=()=>new Promise(r=>finish=r);
 const saved=p.run("save('answer')");assert.equal(p.run('state.index'),0);
 await p.run("save('retain')");
 finish({ok:true,json:async()=>({answer:{choice:'answer',text:'Words I heard'},version:'v3'})});await saved;
 assert.equal(p.run('state.index'),1);assert.equal(p.run('state.items[0].version'),'v3');
 assert.equal(p.run('renders'),1);
});
test('defer stays visibly distinct from retaining uncertainty',async()=>{
 const p=page();let sent;p.context.fetch=async(_,options)=>{sent=JSON.parse(options.body);return {ok:true,json:async()=>({answer:{choice:sent.choice,text:sent.text},version:'v3'})}};
 await p.run("save('defer')");assert.equal(sent.choice,'defer');assert.equal(p.run('state.items[0].answer.choice'),'defer');
});
test('saving one answer keeps other unsaved drafts protected',async()=>{
 const p=page();p.run("state.drafts.b='Unsaved other answer';state.dirty=true");
 p.context.fetch=async()=>({ok:true,json:async()=>({answer:{choice:'answer',text:'Words I heard'},version:'v3'})});
 await p.run("save('answer')");assert.equal(p.run('state.dirty'),true);
});

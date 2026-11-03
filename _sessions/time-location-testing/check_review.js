// Offline string-generation checks only; no browser, network, or visual rendering.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const base = __dirname;
const page = fs.readFileSync(path.join(base, 'review.html'), 'utf8');
const script = page.match(/<script>([\s\S]*)<\/script>/)[1];
function control(value='') { return {value, checked:true, innerHTML:'', children:[], addEventListener(){}, append(x){this.children.push(x);if(!this.value)this.value=x.value}}; }
const controls = {'#session':control(), '#kind':control('time'), '#search':control(), '#context':control(), '#intro':control(), '#a':control(), '#b':control(), '#issues':control()};
const context = vm.createContext({document:{querySelector:id=>controls[id],querySelectorAll:()=>Object.values(controls),createElement:()=>control()}});
new vm.Script(script).runInContext(context);
if (controls['#session'].children.length!==5) throw Error('Missing session option');
let checks=[];
for(const n of [17,32,41,98,109]) {
  controls['#session'].value=n;
  for(const kind of ['time','location']) {
    controls['#kind'].value=kind;
    controls['#search'].value=''; controls['#context'].checked=true;
    vm.runInContext('draw()',context);
    for(const side of ['#a','#b']) {
      const text=controls[side].innerHTML;
      if (!text.includes('<tbody>') || text.includes('undefined')) throw Error('Broken projection '+n+' '+kind+' '+side);
    }
    checks.push({session:n,view:kind,result:'passed string-generation check'});
  }
}
controls['#session'].value=109;controls['#kind'].value='time';controls['#search'].value='u9868';
vm.runInContext('draw()',context);
if(!controls['#a'].innerHTML.includes('u9868'))throw Error('UID filter failed');
controls['#session'].value=98;controls['#kind'].value='location';controls['#search'].value='';controls['#context'].checked=false;
vm.runInContext('draw()',context);
if(controls['#a'].innerHTML.includes('<code>l23</code>'))throw Error('Future movement filter failed');
const report={status:'passed',method:'Offline mocked document API: JavaScript syntax and HTML-string generation. Not a browser or visual layout test.',views:checks,additional:['UID search','hide planned movement'],visualInspection:'not performed; local file URL rejected by browser policy'};
fs.writeFileSync(path.join(base,'review-checks.json'),JSON.stringify(report,null,2)+'\n');
process.stdout.write('10 view projections, UID search, and context filter passed; no visual browser test.\n');

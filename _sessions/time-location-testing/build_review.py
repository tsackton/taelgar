"""Validate manually authored evidence, project four experimental formats, render review.
Run from vault root: python3 -B _sessions/time-location-testing/build_review.py
This script does not extract semantics, infer dates, or alter the source bundles.
"""
from pathlib import Path
import json,hashlib,html,copy,datetime,re
from authoring import ROOT,Study,digest
from read_source import SAMPLE

def dump(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def order(x): return min(int(e['startUid'][1:]) for e in x['evidence'])
def validate(d,study):
 assert d['session']==study.n
 groups=[d['timeMarkers'],d['locationMarkers'],d['places'],d['timelineNodes'],d['timeConstraints']]
 for g in groups:assert len(g)==len({x['id'] for x in g}),'Duplicate ID'
 ti={x['id']:x for x in d['timeMarkers']}; pi={x['id']:x for x in d['places']}; ni={x['id']:x for x in d['timelineNodes']}
 def ev(e):
  assert e['quote'],'Empty quote'
  actual=study.e(e['startUid'],e['quote'],e['endUid'])
  assert actual==e,'Evidence must align to complete polished turns, including shared UIDs'
 def walk(o):
  if isinstance(o,dict):
   if set(('startUid','endUid','quote'))<=set(o):ev(o)
   for v in o.values():walk(v)
  elif isinstance(o,list):
   for v in o:walk(v)
 walk(d)
 for t in d['timeMarkers']:
  assert t['frame'] in {'current','retrospective','table','planned','reported','flashback','framing','vision','opening_boundary'}
  assert t['evidence']
 for p in d['places']:
  assert p['parentId'] is None or p['parentId'] in pi
  seen={p['id']}; parent=p['parentId']
  while parent:
   assert parent not in seen,'Place hierarchy cycle';seen.add(parent);parent=pi[parent]['parentId']
  if p['kind']=='mobile_platform':assert p['parentId'] is None,'Vessels cannot have permanent city parent'
  if p['vaultPath']:assert Path(p['vaultPath']).is_file(),'Broken vault link'
 for l in d['locationMarkers']:
  assert l['evidence']
  for k in ['placeId','fromPlaceId','toPlaceId','vehicleId']:
   assert l.get(k) is None or l[k] in pi,(l['id'],k)
  for p in l.get('viaPlaceIds',[]):assert p in pi
  for n in l.get('timeNodeIds',[]):assert n in ni
  if l['kind']=='journey':assert l['fromPlaceId'] is not None or l['toPlaceId'] is not None
 for n in d['timelineNodes']:
  assert n['markerIds'] and all(t in ti for t in n['markerIds'])
  assert n['date'] is None or datetime.date.fromisoformat(n['date'])
  assert n['date'] is None or n['dateBasis']!='relative_only','Date needs explicit derivation'
 for c in d['timeConstraints']:
  assert c['fromNode'] in ni and c['toNode'] in ni
  assert c['markerIds'] and all(t in ti for t in c['markerIds'])
  if c.get('dateBoundaries',0) and c.get('includeInCurrentSpan',True):
   assert any(ti[t]['frame'] in {'current','flashback','retrospective'} for t in c['markerIds']),'Planned event cannot prove completed date boundary'
 expected=(datetime.date.fromisoformat(str(study.yaml['drEnd']))-datetime.date.fromisoformat(str(study.yaml['drStart']))).days
 assert d['audit']['yamlExpectedDateBoundaries']==expected
 if d['audit']['supportedDateBoundaries'] is not None:
  total=sum(c.get('dateBoundaries') or 0 for c in d['timeConstraints'] if c.get('includeInCurrentSpan',True))
  assert total==d['audit']['supportedDateBoundaries'],'Date-boundary audit disagrees with constraints'
 for r in d['spatialRelations']:
  assert r['fromPlaceId'] in pi and r['toPlaceId'] in pi
 return {'session':study.n,'timeMarkers':len(ti),'locationMarkers':len(d['locationMarkers']),'places':len(pi),'evidenceRefs':sum(len(t['evidence']) for t in d['timeMarkers']+d['locationMarkers']),'sourceHashMatches':True,'yamlHashMatches':True}

def provenance(s):
 return {'sessionId':f'dunmar-frontier:{s.n:03}','campaignDisplay':'Dunmari Frontier','sessionYaml':s.s['yaml'],'sessionYamlSha256':s.s['yamlSha256'],'sourceKey':'transcriptProcessing.artifacts.polishedMarkdown','transcriptPath':s.s['transcript'],'transcriptSha256':s.s['sourceSha256'],'transcriptStatus':s.s['status'],'yamlDates':{'start':str(s.yaml['drStart']),'end':str(s.yaml['drEnd'])}}

def build(d,s):
 common={'schemaVersion':'0.1-experiment','provenance':provenance(s),'review':{'status':'pilot-human-unreviewed','method':'Ordered candidate sweep of all polished turns; expanded full-turn context at selected decisions; supplementary numeric-clock/spatial sweep; focused semantic review; deterministic provenance checks.','limitation':'Not an independent exhaustive semantic audit of every turn. Recall not measured. Source transcription uncertainty retained.'},'summary':d['summary'],'issues':d['issues']}
 ta=common|{'model':'time-A-evidence-ledger','markers':sorted(d['timeMarkers'],key=order)}
 tb=common|{'model':'time-B-constraint-chronology','nodes':d['timelineNodes'],'constraints':d['timeConstraints'],'yamlAudit':d['audit'],'evidenceLedger':'time-A.json','evidenceLedgerSha256':None,'nonAdvancingInSourceOrder':[t['id'] for t in d['timeMarkers'] if t['frame'] in {'table','planned','vision','reported','flashback'}],'contextSources':d['contextSources']}
 pi={p['id']:p for p in d['places']}
 def label(id):return pi[id]['label'] if id else None
 la=common|{'model':'location-A-transition-ledger','markers':[l|{'placeLabel':label(l['placeId']),'fromLabel':label(l['fromPlaceId']),'toLabel':label(l['toPlaceId'])} for l in sorted(d['locationMarkers'],key=order)]}
 physical=[l for l in d['locationMarkers'] if l['frame'] in {'current','flashback'}]
 visits=[{'id':'v-'+l['id'],'placeId':l['placeId'] or l['toPlaceId'],'actors':l['actors'],'frame':l['frame'],'timeNodeIds':l.get('timeNodeIds',[]),'evidenceMarkerIds':[l['id']],'concurrencyGroup':l.get('concurrencyGroup'),'confidence':l.get('confidence','high'),'statement':l['reading'],'occupancyExtent':'attested at marker; no exhaustive UID occupancy implied'} for l in physical if l['kind'] in {'presence','arrival'}]
 journeys=[{'id':'r-'+l['id'],'fromPlaceId':l['fromPlaceId'],'toPlaceId':l['toPlaceId'],'viaPlaceIds':l.get('viaPlaceIds',[]),'mode':l.get('mode','unspecified'),'vehicleId':l.get('vehicleId'),'actors':l['actors'],'frame':l['frame'],'completion':l.get('completion','narrated'),'timeNodeIds':l.get('timeNodeIds',[]),'evidenceMarkerIds':[l['id']],'concurrencyGroup':l.get('concurrencyGroup'),'geometry':None,'statement':l['reading']} for l in physical if l['kind']=='journey']
 # Movements establish destination arrivals, but a begun route only establishes departure.
 for j in journeys:
  if j['toPlaceId'] and j['completion']!='begun':
   visits.append({'id':'v-'+j['evidenceMarkerIds'][0],'placeId':j['toPlaceId'],'actors':j['actors'],'frame':j['frame'],'timeNodeIds':j['timeNodeIds'],'evidenceMarkerIds':j['evidenceMarkerIds'],'concurrencyGroup':j['concurrencyGroup'],'confidence':'see source marker','statement':'Arrival via narrated journey: '+j['statement'],'occupancyExtent':'arrival only; no exhaustive UID occupancy implied'})
 marker_order={l['id']:order(l) for l in d['locationMarkers']}
 visits.sort(key=lambda v:marker_order[v['evidenceMarkerIds'][0]])
 observations=[l for l in d['locationMarkers'] if l['kind'] in {'remote_observation','observation'}]
 places=[]
 for p in d['places']:
  refs=[l['id'] for l in d['locationMarkers'] if p['id'] in [l['placeId'],l['fromPlaceId'],l['toPlaceId']]+l.get('viaPlaceIds',[])]
  places.append(p|{'identityStatus':'vault_match' if p['vaultPath'] else 'local_transcript_label','evidenceMarkerIds':refs,'hierarchyBasis':'transcript spatial context; named vault match where supplied','parentRelation':p.get('parentRelation','within_or_local_context' if p['parentId'] else None)})
 lb=common|{'model':'location-B-place-visit-route-graph','places':places,'visits':visits,'journeys':journeys,'observations':observations,'plannedMovements':[l for l in d['locationMarkers'] if l['frame']=='planned'],'spatialRelations':d['spatialRelations'],'evidenceLedger':'location-A.json','evidenceLedgerSha256':None,'timeMap':'time-B.json','timeMapSha256':None,'notes':['Local place IDs are session-scoped. A vault link is an identity match, not proof of a visit.','Routes express topology and direction; geometry remains null. A place mentioned in a vision is not physical presence.','Visit markers do not assign every transcript line or every speaker to a place. No NPC whereabouts are automatically published.','parentRelation distinguishes containment, adjacency, approach, and inferred shared base; inspect its evidence before aggregating presence.']}
 return ta,tb,la,lb

def esc(s):return str(s if s is not None else '—').replace('|','\\|').replace('\n',' ')
def table(headers,rows):return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(esc(v) for v in row)+' |' for row in rows])+'\n'
def evtext(es,s):
 text=Path(s.s['transcript']).read_text(); lines=text.splitlines()
 out=[]
 for e in es:
  line=next(i+1 for i,l in enumerate(lines) if re.search(r'\b'+re.escape(e['startUid'])+r':',l))
  uid=e['startUid'] if e['startUid']==e['endUid'] else e['startUid']+'–'+e['endUid']
  path=Path(s.s['transcript']).resolve()
  out.append(f'[{uid}](<{path}:{line}>) “{e["quote"]}”')
 return '<br>'.join(out)
def render(d,s,maps):
 ta,tb,la,lb=maps
 out=[f'# Session {s.n}: time and location comparison','',d['summary'],'',f'YAML: {s.yaml["drStart"]} → {s.yaml["drEnd"]}. **{d["audit"]["assessment"]}** — {d["audit"]["explanation"]}','','Provisional pilot; not human-reviewed. Candidate-led inspection with contextual checks; completeness has not been independently measured. Source IDs below are session-local UIDs, not global UUIDs.','', '## Time A — evidence ledger','', 'Source order; literal markers, corrections, and rejected advances remain visible.','',table(['ID / frame','Time or date reading','Evidence and UID'],[(t['id']+' / '+t['frame'],t['reading'],evtext(t['evidence'],s)) for t in ta['markers']]),'## Time B — chronology and constraints','', 'Chronological anchors; dates say where their authority comes from. Main-day audit excludes framed visions and prior-night retcons.','']
 ti={t['id']:t for t in ta['markers']}
 out.append(table(['Anchor','Date / time','Basis','Evidence markers / UIDs'],[(n['id']+' — '+n['label'],str(n['date'] or 'Unknown civil date')+'; '+str(n['timeOfDay'] or 'time unknown'),n['dateBasis'],', '.join(n['markerIds'])+'; '+', '.join(ti[t]['evidence'][0]['startUid'] for t in n['markerIds'])) for n in tb['nodes']]))
 out+=['',table(['Relation','Meaning','Duration / date boundaries','Evidence'],[(c['fromNode']+' → '+c['toNode'],c['relation'],json.dumps(c.get('duration'),ensure_ascii=False) if c.get('duration') else str(c.get('dateBoundaries','unknown'))+' boundaries',', '.join(c['markerIds'])+('; '+c['note'] if c.get('note') else '')) for c in tb['constraints']]),'## Location A — transition ledger','','Source order, including observations and plans. Actors prevent accidental whole-party movement.','',table(['ID / frame','Actors','Place / route','Meaning','Evidence and UID'],[(l['id']+' / '+l['frame'],', '.join(l['actors']),l['placeLabel'] or str(l['fromLabel'] or '?')+' → '+str(l['toLabel'] or '?'),l['reading'],evtext(l['evidence'],s)) for l in la['markers']]),'## Location B — place, visit, and route graph','','Places are reusable nodes; repeat visits stay separate. Ships have no permanent geographic parent. Read parentRelation before interpreting a parent as containment.','']
 pi={p['id']:p for p in lb['places']}; label=lambda p:pi[p]['label'] if p else 'Unknown'
 out.append(table(['Place ID','Place','Kind','Parent / context','Vault identity'],[(p['id'],p['label'],p['kind'],(p['parentRelation']+': '+label(p['parentId'])) if p['parentId'] else '—',p['vaultPath'] or 'Local label; not resolved to a vault note') for p in lb['places']]))
 out+=['',table(['Visit','Actors','Place','Time anchors','Evidence marker'],[(v['id'],', '.join(v['actors']),label(v['placeId']),', '.join(v['timeNodeIds']) or 'Unknown',', '.join(v['evidenceMarkerIds'])) for v in lb['visits']]),'',table(['Journey','Actors','From → To','Mode / completion','Evidence'],[(r['id'],', '.join(r['actors']),label(r['fromPlaceId'])+' → '+label(r['toPlaceId']),r['mode']+'; '+r['completion'],', '.join(r['evidenceMarkerIds'])) for r in lb['journeys']]),'',table(['Topology','Evidence UID'],[(label(r['fromPlaceId'])+' '+r['relation']+' '+label(r['toPlaceId']),', '.join(e['startUid'] for e in r['evidence'])) for r in lb['spatialRelations']]),'', 'Remote views, threshold observations, and planned movements stay in separate graph collections; they do not become visits.','', '## Review questions and limits','']
 out += ['- '+x for x in d['issues']]
 out += ['', 'Machine-readable versions: [Time A](time-A.json), [Time B](time-B.json), [Location A](location-A.json), [Location B](location-B.json).', '']
 return '\n'.join(out)

def main():
 reports=[]; bundles=[]
 for sample in sorted(SAMPLE['selected'],key=lambda s:s['session']):
  s=Study(sample['session']);folder=ROOT/f'session-{s.n:03}';d=json.loads((folder/'authored.json').read_text());reports.append(validate(d,s));maps=build(d,s)
  for name,m in zip(['time-A','time-B','location-A','location-B'],maps):
   if name=='time-B':m['evidenceLedgerSha256']=digest(folder/'time-A.json')
   if name=='location-B':m['evidenceLedgerSha256']=digest(folder/'location-A.json');m['timeMapSha256']=digest(folder/'time-B.json')
   dump(folder/(name+'.json'),m)
  (folder/'review.md').write_text(render(d,s,maps))
  bundles.append({'session':s.n,'authored':d,'maps':maps})
 # Meaningful negative checks: corrupt evidence, graph cycle, nonexistent pointer, stale source.
 tested=[]
 orig=bundles[0]['authored'];s=Study(orig['session'])
 for label,mutate in [
  ('reject quote absent from source',lambda x:x['timeMarkers'][0]['evidence'][0].update(quote='THIS QUOTE DOES NOT EXIST 7654321')),
  ('reject containment cycle',lambda x:x['places'][0].update(parentId=x['places'][0]['id'])),
  ('reject nonexistent timeline pointer',lambda x:x['timelineNodes'][0]['markerIds'].append('missing')),
  ('reject inconsistent night total',lambda x:x['audit'].update(supportedDateBoundaries=999))]:
  d=copy.deepcopy(orig);mutate(d)
  try:validate(d,s)
  except (AssertionError,KeyError):tested.append(label)
  else:raise AssertionError('Negative check failed: '+label)
 # Explicit regression checks for real pilot failure modes, not wording assertions.
 b98=next(b for b in bundles if b['session']==98)['maps'];b109=next(b for b in bundles if b['session']==109)['maps']
 assert b98[1]['yamlAudit']['supportedDateBoundaries']==2
 assert all(r['evidenceMarkerIds']!=['l23'] for r in b98[3]['journeys'])
 assert all(v['placeId']!='harbor-a' or v['evidenceMarkerIds']!=['l05'] for v in b98[3]['visits'])
 assert next(c for c in b109[1]['constraints'] if c['id']=='c5')['duration']['value']==2
 assert b109[1]['yamlAudit']['supportedDateBoundaries']==0
 tested+=['future sailing absent from physical routes','scrying absent from physical visits','overlapping rest not added to two study hours','prior-night retcon excluded from current-day count']
 dump(ROOT/'validation.json',{'status':'passed','sessions':reports,'negativeAndRegressionChecks':tested,'limits':'Validates references, structure, source hashes, projections, and selected failure modes; does not certify completeness or semantic correctness.'})
 make_html(bundles)
 print(json.dumps({'sessions':reports,'negativeAndRegressionChecks':len(tested),'outputs':'20 maps; 5 complete Markdown reviews; review.html'},indent=2))

def make_html(bundles):
 payload=json.dumps(bundles,ensure_ascii=False).replace('<','\\u003c')
 page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Time & location experiments</title><style>
:root{font-family:system-ui,sans-serif;color:#172d36;background:#f3f4ef}body{margin:0}header{padding:24px 4vw;background:#143d43;color:#fff}h1{margin:0 0 8px;font-size:27px}main{padding:24px 4vw}nav{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:20px}select,input{padding:9px;font-size:15px;border:1px solid #9faeaa;border-radius:6px}label{font-size:14px}article{background:white;border:1px solid #d8ded8;border-radius:10px;padding:20px;margin-bottom:20px;overflow:auto}h2{font-size:21px;color:#154a50}h3{font-size:17px}table{border-collapse:collapse;width:100%;font-size:14px}th{text-align:left;background:#e9efeb;position:sticky;top:0}td,th{padding:10px;vertical-align:top;border-bottom:1px solid #e0e6e1}td{min-width:100px}blockquote{margin:6px 0;color:#425c64;font-size:13px}code{background:#eef1ef;font-size:12px;white-space:normal}.pill{font-size:12px;background:#e3ece8;padding:3px 7px;border-radius:20px}.muted{color:#53686d}details{margin:6px 0}summary{cursor:pointer}.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}@media(max-width:1100px){.grid{display:block}}a{color:#086f79}p{max-width:95ch;line-height:1.5}.scroll{overflow:auto;max-height:75vh}footer{font-size:13px;color:#53686d;margin:20px 0}</style>
<header><h1>Time & location experiments</h1><div>Five random Dunmari Frontier sessions · Two time models · Two location models</div></header><main>
<p>Start with Session 17 for travel, 32 for flashbacks, 41 for uncertain end dates, 98 for split parties and ships, and 109 for rooms and overlapping rests. All artifacts are provisional and awaiting your review.</p>
<nav><label>Session <select id="session"></select></label><label>Compare <select id="kind"><option value="time">Time</option><option value="location">Location</option></select></label><label>Find <input id="search" placeholder="UID, place, rest, actor…"></label><label><input type="checkbox" id="context" checked> Show plans / visions / context</label></nav>
<div id="intro"></div><div class="grid"><article id="a"></article><article id="b"></article></div><article id="issues"></article>
<footer>Candidate-led pilot extraction with expanded context checks; completeness has not been independently measured. Quotes and UIDs were checked against fingerprinted polished transcripts. Dates inferred from YAML are labeled. No source bundles were edited. <a href="README.md">Comparison report</a> · <a href="notes.md">Working notes</a> · <a href="validation.json">Validation</a></footer></main><script>
const DATA=PAYLOAD;
const esc=x=>String(x??'—').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const sel=document.querySelector('#session');DATA.forEach(b=>{let o=document.createElement('option');o.value=b.session;o.textContent=b.session;sel.append(o)});
function tab(headers,rows){return '<div class="scroll"><table><thead><tr>'+headers.map(h=>'<th>'+esc(h)+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+r.map(c=>'<td>'+c+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>'}
function evidence(es){return es.map(e=>'<details><summary><code>'+esc(e.startUid+(e.endUid!==e.startUid?'–'+e.endUid:''))+'</code></summary><blockquote>'+esc(e.quote)+'</blockquote></details>').join('')}
function draw(){const b=DATA.find(b=>b.session==sel.value),time=document.querySelector('#kind').value==='time',q=document.querySelector('#search').value.toLowerCase(),ctx=document.querySelector('#context').checked,d=b.authored,[ta,tb,la,lb]=b.maps;
 const keep=x=>(!q||JSON.stringify(x).toLowerCase().includes(q))&&(ctx||['current','opening_boundary'].includes(x.frame||'current'));
 const p=Object.fromEntries(lb.places.map(p=>[p.id,p]));const name=id=>id?p[id]?.label||id:'Unknown';
 document.querySelector('#intro').innerHTML='<p><strong>'+esc(d.summary)+'</strong></p><p><span class="pill">'+esc(d.audit.assessment)+'</span> YAML '+esc(ta.provenance.yamlDates.start)+' → '+esc(ta.provenance.yamlDates.end)+'. '+esc(d.audit.explanation)+'</p><p><a href="session-'+String(b.session).padStart(3,'0')+'/review.md">Full Markdown review with transcript links</a></p>';
 let a='',bb='';
 if(time){a='<h2>A · Evidence ledger</h2><p class="muted">Source order. Literal markers, corrections, and rejected advances remain visible.</p>'+tab(['Marker / frame','Time reading','Evidence'],ta.markers.filter(keep).map(t=>['<code>'+esc(t.id)+'</code><br>'+esc(t.frame),esc(t.reading),evidence(t.evidence)]));
 const tm=Object.fromEntries(ta.markers.map(t=>[t.id,t]));
 bb='<h2>B · Chronology & constraints</h2><p class="muted">Chronological order. Civil dates and their derivation are separate. No line-by-line clock assignment.</p>'+tab(['Anchor','Date / time','Basis / evidence'],tb.nodes.filter(n=>keep({...n,evidence:n.markerIds.map(id=>tm[id])})).map(n=>[esc(n.id+' · '+n.label),esc(n.date||'Unknown date')+'<br>'+esc(n.timeOfDay),esc(n.dateBasis)+'<br><code>'+esc(n.markerIds.join(', '))+'</code>'+evidence(n.markerIds.flatMap(id=>tm[id].evidence))]))+'<h3>Constraints</h3>'+tab(['Between','Relation','Duration / boundaries'],tb.constraints.filter(keep).map(c=>[esc(c.fromNode+' → '+c.toNode),esc(c.relation),esc(c.duration?JSON.stringify(c.duration):(c.dateBoundaries??'Unknown')+' date boundaries')+(c.note?'<p>'+esc(c.note)+'</p>':'')]))}
 else{a='<h2>A · Location transitions</h2><p class="muted">Source order. Actor-specific moves, visits, remote views, and plans.</p>'+tab(['Marker / actors','Place or movement','Evidence'],la.markers.filter(keep).map(l=>['<code>'+esc(l.id)+'</code><br>'+esc(l.actors.join(', '))+'<br><span class="pill">'+esc(l.frame)+'</span>',esc(l.placeLabel||((l.fromLabel||'?')+' → '+(l.toLabel||'?')))+'<p>'+esc(l.reading)+'</p>',evidence(l.evidence)]));
 bb='<h2>B · Places, visits & paths</h2><p class="muted">Local hierarchy and topology. Vessels move; visions are separate. Typed parent links distinguish containment from vicinity.</p><h3>Places</h3>'+tab(['Place','Kind','Parent / context'],lb.places.filter(keep).map(p=>['<code>'+esc(p.id)+'</code><br>'+esc(p.label),esc(p.kind),esc(p.parentId?p.parentRelation+': '+name(p.parentId):'—')]))+'<h3>Visits & arrivals</h3>'+tab(['Actors','Place','Evidence'],lb.visits.filter(keep).map(v=>[esc(v.actors.join(', ')),esc(name(v.placeId)),esc(v.evidenceMarkerIds.join(', '))+'<br>'+esc(v.timeNodeIds.join(', '))]))+'<h3>Physical journeys</h3>'+tab(['Path','Actors / mode','Evidence'],lb.journeys.filter(keep).map(r=>[esc(name(r.fromPlaceId)+' → '+name(r.toPlaceId)),esc(r.actors.join(', ')+'; '+r.mode+'; '+r.completion),esc(r.evidenceMarkerIds.join(', '))]))+'<h3>Spatial relationships</h3>'+tab(['Topology','Evidence'],lb.spatialRelations.filter(keep).map(r=>[esc(name(r.fromPlaceId)+' '+r.relation+' '+name(r.toPlaceId)),evidence(r.evidence)]))+'<p class="muted">Remote observations and plans are retained in separate JSON collections and in ledger A; they create no physical visit.</p>'}
 document.querySelector('#a').innerHTML=a;document.querySelector('#b').innerHTML=bb;document.querySelector('#issues').innerHTML='<h2>Review points</h2><ul>'+d.issues.map(i=>'<li>'+esc(i)+'</li>').join('')+'</ul>';
}document.querySelectorAll('select,input').forEach(x=>x.addEventListener('input',draw));draw();
</script></html>'''.replace('PAYLOAD',payload)
 (ROOT/'review.html').write_text(page)
if __name__=='__main__':main()

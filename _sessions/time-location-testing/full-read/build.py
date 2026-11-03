"""Render and validate the full-read follow-up; semantics are authored, not regex-extracted."""
from setup import ROOT,Study,load
from pathlib import Path
import json,hashlib,copy
import build_review as base
base.ROOT=ROOT
coverage=json.loads((ROOT/'coverage.json').read_text())
results=[]; comparisons=[]; bundles=[]
for n in (24,39):
 s=Study(n);folder=ROOT/f'session-{n:03}';d=json.loads((folder/'authored.json').read_text());c=coverage['sessions'][str(n)]
 seen=[i for a,b in c['windowsRead'] for i in range(a,b+1)]
 assert seen==list(range(1,len(s.turns)+1)) and c['complete']
 assert c['turnCount']==len(s.turns) and c['sourceSha256']==s.s['sourceSha256'] and c['yamlSha256']==s.s['yamlSha256']
 report=base.validate(d,s);report['fullReadTurns']=len(seen);results.append(report)
 maps=base.build(d,s)
 for m in maps:
  m['schemaVersion']='0.2-full-read-experiment'
  m['review']={'status':'full-read-pilot-human-unreviewed','method':'Assistant read every polished transcript turn sequentially without keyword/speaker filtering, then authored sparse markers and context exclusions; deterministic validation of provenance and references.','coverage':c,'limitation':'Full reading is not an independent second annotator or a gold-standard recall measurement. Source transcription uncertainty retained.'}
 # Keep remote entity attestations and reported routes available for future whereabouts work.
 maps[3]['observations']=[l for l in d['locationMarkers'] if l['kind'] in {'observation','remote_observation','observed_presence'}]
 maps[3]['reportedLocations']=[l for l in d['locationMarkers'] if l['frame']=='reported']
 maps[3]['notes'].append('Reported whereabouts and remotely observed entity presence are retained separately; neither becomes a physical party visit.')
 maps[1]['nonAdvancingInSourceOrder']=[t['id'] for t in d['timeMarkers'] if t['frame']!='current']
 for name,m in zip(['time-A','time-B','location-A','location-B'],maps):
  if name=='time-B':m['evidenceLedgerSha256']=base.digest(folder/'time-A.json')
  if name=='location-B':m['evidenceLedgerSha256']=base.digest(folder/'location-A.json');m['timeMapSha256']=base.digest(folder/'time-B.json')
  base.dump(folder/(name+'.json'),m)
 md=base.render(d,s,maps).replace('Candidate-led inspection with contextual checks; completeness has not been independently measured.','Every polished transcript turn was read in order, without keyword or speaker filtering. Full-read coverage is documented; semantic completeness has not been independently measured.').replace('Ships have no permanent geographic parent. ','')
 md=md.replace('Main-day audit excludes framed visions and prior-night retcons.','Main-day audit distinguishes current action from prior-night framing; all civil dates here are conditional on YAML.')
 (folder/'review.md').write_text(md)
 baseline=json.loads((ROOT/f'candidate-baseline-{n:03}.json').read_text());hits=set(baseline['matchedTurnIndexes'])
 assert baseline['sourceSha256']==s.s['sourceSha256']
 def turn_indexes(e):
  return [i for i,t in enumerate(s.turns,1) if int(t['end'][1:])>=int(e['startUid'][1:]) and int(t['start'][1:])<=int(e['endUid'][1:])]
 cmp={'session':n,'turns':len(s.turns),'candidateTurns':len(hits),'nonCandidateTurnsRead':len(s.turns)-len(hits),'scope':'Coverage of cited evidence by frozen keyword filter, NOT extraction precision/recall or a controlled independent A/B test','time':[],'location':[]}
 for key,field in [('time','timeMarkers'),('location','locationMarkers')]:
  for marker in d[field]:
   ix=sorted({i for e in marker['evidence'] for i in turn_indexes(e)})
   misses=[i for i in ix if i not in hits]
   cmp[key].append({'id':marker['id'],'reading':marker['reading'],'citedTurnIndexes':ix,'nonCandidateCitedTurnIndexes':misses,'allCitedTurnsMatched':not misses,'anyCitedTurnMatched':bool(set(ix)&hits)})
  cmp[key+'Summary']={'markers':len(cmp[key]),'markersWithNonCandidateEvidence':sum(not x['allCitedTurnsMatched'] for x in cmp[key]),'markersWithNoCandidateEvidence':sum(not x['anyCitedTurnMatched'] for x in cmp[key])}
 cmp['contextWindowSensitivity']=[]
 for width in (0,2,5):
  expanded={j for i in hits for j in range(max(1,i-width),min(len(s.turns),i+width)+1)}
  allmarkers=cmp['time']+cmp['location']
  cmp['contextWindowSensitivity'].append({'neighborTurnsEachSide':width,'turnsSelected':len(expanded),'markersWithNoSelectedCitedTurn':sum(not set(m['citedTurnIndexes'])&expanded for m in allmarkers),'markersWithSomeCitedEvidenceOutsideSelection':sum(not set(m['citedTurnIndexes'])<=expanded for m in allmarkers)})
 comparisons.append(cmp);bundles.append({'session':n,'authored':d,'maps':maps})
base.dump(ROOT/'candidate-comparison.json',comparisons)
# Concrete regressions from this full read, using structure rather than prose matching.
a,b=bundles
assert a['maps'][1]['yamlAudit']['supportedDateBoundaries']==2
assert b['maps'][1]['yamlAudit']['supportedDateBoundaries']==0
assert b['maps'][1]['yamlAudit']['literalNarrativeDateBoundariesIncludingOpening']==1
assert not any(v['placeId']=='archives' for v in b['maps'][3]['visits'])
assert any(v['placeId']=='mist' and v['actors']==['Riswynn'] for v in b['maps'][3]['visits'])
assert not any(v['placeId']=='throne' for v in a['maps'][3]['visits'])
assert any(o['kind']=='observed_presence' for o in a['maps'][3]['observations'])
assert any(l['kind']=='reported_journey' for l in b['maps'][3]['reportedLocations'])
assert not any(r['evidenceMarkerIds']==['l30'] for r in a['maps'][3]['journeys'])
assert not any(r['evidenceMarkerIds']==['l22'] for r in b['maps'][3]['journeys'])
base.dump(ROOT/'validation.json',{'status':'passed','sessions':results,'checks':['all turns covered once in full-read windows','source and YAML hashes unchanged','quotes exact and evidence aligned to complete polished turns','unique IDs, valid graph pointers, no parent cycles','YAML boundary arithmetic consistent with explicit scope','Session 24 two completed nights','Session 39 opening night preserved outside current span','canceled archives absent from visits','Riswynn mist entry preserved as physical visit','remote throne view and NPC presence do not become party visits','reported past route retained separately','future departures absent from physical routes'],'limits':'No independent semantic ground truth; no claim of perfect recall or exact elapsed hours.'})
print(json.dumps({'sessions':results,'comparisonSummaries':[{k:c[k] for k in ['session','turns','candidateTurns','nonCandidateTurnsRead','timeSummary','locationSummary']} for c in comparisons]},indent=2))

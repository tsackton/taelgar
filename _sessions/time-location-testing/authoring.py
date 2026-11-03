"""Helpers for manually authored pilot evidence; not an automatic extractor."""
from pathlib import Path
import hashlib,json,yaml
from read_source import load,ROOT

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
class Study:
 def __init__(self,n):
  self.s,self.turns=load(n); self.n=n; self.times=[]; self.locations=[]; self.places=[]; self.nodes=[]; self.constraints=[]; self.spatial=[]; self.issues=[]; self.context=[]
  assert digest(self.s['transcript'])==self.s['sourceSha256'],'Source changed; review before regenerating'
  assert digest(self.s['yaml'])==self.s['yamlSha256'],'YAML changed; review before regenerating'
  self.yaml=yaml.safe_load(Path(self.s['yaml']).read_text())
 def e(self,uid,quote=None,end=None):
  uid=f'u{uid:04}' if isinstance(uid,int) else uid
  end=f'u{end:04}' if isinstance(end,int) else end or uid
  ts=[t for t in self.turns if int(t['end'][1:])>=int(uid[1:]) and int(t['start'][1:])<=int(end[1:])]
  assert ts,(self.n,uid)
  body='\n'.join(t['speaker']+': '+t['text'] for t in ts)
  if quote is None: quote=ts[0]['text']
  assert quote in body,(self.n,uid,quote)
  return {'startUid':ts[0]['start'],'endUid':ts[-1]['end'],'quote':quote}
 def t(self,id,kind,reading,ev,frame='current',actor='party',**kw):
  self.times.append(dict(id=id,kind=kind,frame=frame,actor=actor,reading=reading,evidence=ev,**kw))
 def p(self,id,label,kind='site',parent=None,note=None,**kw):
  kw.setdefault('parentRelation', 'within' if parent else None)
  self.places.append(dict(id=id,label=label,kind=kind,parentId=parent,vaultPath=note,**kw))
 def l(self,id,kind,reading,ev,place=None,origin=None,destination=None,frame='current',actors=None,**kw):
  self.locations.append(dict(id=id,kind=kind,frame=frame,actors=actors or ['party'],reading=reading,placeId=place,fromPlaceId=origin,toPlaceId=destination,evidence=ev,**kw))
 def node(self,id,label,markers,date=None,basis='relative_only',time=None,**kw):
  self.nodes.append(dict(id=id,label=label,markerIds=markers,date=date,dateBasis=basis,timeOfDay=time,**kw))
 def c(self,id,a,b,relation,markers,**kw): self.constraints.append(dict(id=id,fromNode=a,toNode=b,relation=relation,markerIds=markers,**kw))
 def rel(self,a,b,relation,ev,**kw):self.spatial.append(dict(fromPlaceId=a,toPlaceId=b,relation=relation,evidence=ev,**kw))
 def save(self,audit,summary):
  out=ROOT/f'session-{self.n:03}'; out.mkdir(exist_ok=True)
  d=dict(session=self.n,timeMarkers=self.times,locationMarkers=self.locations,places=self.places,timelineNodes=self.nodes,timeConstraints=self.constraints,spatialRelations=self.spatial,issues=self.issues,contextSources=self.context,audit=audit,summary=summary)
  (out/'authored.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

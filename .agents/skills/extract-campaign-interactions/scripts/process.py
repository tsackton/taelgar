#!/usr/bin/env python3
"""Deterministic support for agent-operated extract/review/correct batches; no hidden model calls."""
import argparse
import copy
import datetime
import hashlib
import json
import random
import re
from pathlib import Path
import yaml
from session_model import validate, render, apply_review, critical_queue, digest, vault_path


def write(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def normalize(value):
    return re.sub(r'\W+', '', str(value).casefold())

def build_index(vault):
    entries=[]
    for path in sorted(vault.rglob('*.md')):
        relative=path.relative_to(vault)
        if any(p.startswith(('.', '_')) for p in relative.parts) or relative.parts[0] in {'Worldbuilding','Primary Sources','assets'}:
            continue
        try:vault_path(vault,str(relative))
        except (ValueError,OSError):continue
        text=path.read_text(errors='replace')
        if not text.startswith('---\n'):continue
        try:meta=yaml.safe_load(text.split('---',2)[1]) or {}
        except yaml.YAMLError:continue
        if not isinstance(meta,dict):continue
        tags=meta.get('tags') or []
        if isinstance(tags,str):tags=[tags]
        if any(str(t).startswith(('session-note','session/')) for t in tags):continue
        aliases=meta.get('aliases') or []
        if isinstance(aliases,str):aliases=[aliases]
        names=list(dict.fromkeys(str(n) for n in [path.stem,meta.get('name'),*aliases] if n))
        entries.append({'path':str(relative),'names':names,'keys':[normalize(n) for n in names],
                        'tags':tags,'typeOf':meta.get('typeOf'),'species':meta.get('species')})
    return {'schemaVersion':1,'entries':entries}

def inventory(vault):
    registry=json.loads((vault/'_scripts/session_note_campaigns.json').read_text())['campaigns']
    codes={v['sessionRoot']:v['code'] for v in registry.values()}
    rows=[];excluded=[]
    for p in sorted((vault/'_sessions').glob('*/*/cleaned/*-session.yaml')):
        manifest=yaml.safe_load(p.read_text())
        source=p.with_name(p.name.replace('-session.yaml','-source-cleaned.md'))
        campaign=p.relative_to(vault).parts[1]
        if manifest.get('sourceType')!='transcript' or not source.exists() or campaign not in codes:
            excluded.append({'manifest':str(p.relative_to(vault)),'reason':'Not an available supported transcript'})
            continue
        rows.append({'id':p.parent.parent.name,'campaign':codes[campaign],'session':manifest['sessionNumber'],
                     'manifest':str(p.relative_to(vault)),'source':str(source.relative_to(vault)),
                     'sha256':digest(source),'words':len(source.read_text().split())})
    return rows,excluded

def sample(vault,count,seed):
    rows,excluded=inventory(vault)
    require_count=len(rows)>=count and count>0
    if not require_count:raise ValueError('Insufficient eligible transcripts')
    rng=random.Random(seed)
    groups={c:[r for r in rows if r['campaign']==c] for c in sorted({r['campaign'] for r in rows})}
    chosen=[]
    for c in rng.sample(list(groups),min(count,len(groups))):chosen.append(rng.choice(groups[c]))
    remaining=[r for r in rows if r not in chosen]
    chosen+=rng.sample(remaining,count-len(chosen))
    return {'seed':seed,'method':'One random session per available transcript campaign, then random remaining sessions without replacement; sorted input population.',
            'population':rows,'excluded':excluded,'selected':chosen}

def prepare(vault,selection,index,output,resume=False):
    output=Path(output)
    if (output/'session.json').exists() or (output/'draft.json').exists():
        if resume and (output/'execution.json').exists():
            saved=json.loads((output/'execution.json').read_text())
            if saved.get('selection') == selection and digest(vault/selection['source']) == selection['sha256']:
                return 'preserved'
        raise ValueError('Refusing to overwrite existing or changed execution')
    source=vault_path(vault,selection['source']);manifest=yaml.safe_load(vault_path(vault,selection['manifest']).read_text())
    if digest(source) != selection['sha256']:raise ValueError('Source changed since sampling')
    entries=index['entries'];pcs=[];unresolved=[]
    for participant in manifest.get('participants',[]):
        role=participant.get('gameRole')
        if not role or role.casefold() in {'dm','gm','unknown','dungeon master'}:continue
        matches=[e for e in entries if normalize(role) in e['keys']]
        if len(matches)==1:pcs.append(matches[0]['path'])
        else:unresolved.append({'role':role,'candidates':[e['path'] for e in matches]})
    raw=source.read_text()
    matches=[]
    # Literal name hits are navigation candidates, never evidence of an interaction or automatic vault resolution.
    for e in entries:
        hits=[]
        for n in e['names']:
            if len(n)<4:continue
            if re.search(r'(?<!\w)'+re.escape(n)+r'(?!\w)',raw,re.I):hits.append(n)
        if hits:matches.append({**e,'matchedNames':hits})
    data={'schemaVersion':5,'campaign':selection['campaign'],'session':selection['session'],'realWorldDate':str(manifest['realWorldDate']),
          'pcs':list(dict.fromkeys(pcs)),'sources':[{'id':'transcript-1','kind':'transcript','path':selection['source'],'sha256':digest(source)}],
          'locations':[],'scenes':[],'entities':[],'interactions':[],
          'review':{'confidence':'low','status':'unreviewed'},'sceneReview':{'confidence':'low','status':'unreviewed'}}
    date_issues=[]
    for a,b in [('drStart','dateStart'),('drEnd','dateEnd')]:
        if manifest.get(a):
            value=str(manifest[a])
            try:datetime.date.fromisoformat(value)
            except ValueError:date_issues.append({'field':a,'value':value,'reason':'Not an exact ISO date; omitted from candidate'})
            else:data[b]=value
    write(output/'draft.json',data)
    write(output/'candidates.json',{'pcIssues':unresolved,'matches':matches})
    write(output/'execution.json',{'selection':selection,'stage':'prepared','correctionAttempts':0,'unresolvedPCs':unresolved,'dateIssues':date_issues})
    compact=[]
    for line in raw.splitlines():
        m=re.match(r'^\[(u\d+)(?:\s*\|\s*(.*?))?\]\s?(.*)$',line)
        if m:
            uid,attribution,text=m.groups()
            speaker=(attribution or '').split('|')[-1].strip()
            compact.append(f'{uid} {speaker}: {text}')
    (output/'transcript.txt').write_text('\n'.join(compact)+'\n')
    return 'prepared'

def review_request(data,vault):
    checked=validate(data,vault)
    cat=checked['catalog']
    windows=[]
    # The reviewing agent may expand these windows; full transcript paths always remain available.
    for e in data.get('entities',[]):
        own=[r for r in data.get('interactions',[]) if r['entity']==e['id']]
        passages=[p['source'] for r in own for p in r.get('passages',[])]
        if not passages:
            indexes={i for r in own for i in r['scenes']}
            passages=[s['source'] for s in data.get('scenes',[]) if s['index'] in indexes]
        windows.append({'target':'entity:'+e['id'],'record':e,'sourceRanges':passages})
    hints=[]
    for source in data['sources']:
        path=vault/source['path']
        for suffix in ['beats.json','beat-facts.json']:
            p=path.with_name(path.name.replace('source-cleaned.md',suffix))
            if p.exists():hints.append(str(p.relative_to(vault)))
    return {'inputDigest':hashlib.sha256(json.dumps(data,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
            'criticalMetadata':{k:data.get(k) for k in ['campaign','session','realWorldDate','pcs','dateStart','dateEnd','locations']},
            'entityEvidence':windows,'optionalReviewHints':hints,
            'instructions':'Separately verify each critical record against transcript context and vault identities. Inspect dates, attendance, locations and omissions across the session. Beats are optional review hints, never sole evidence. No validation-only promotion. Return reviewer, inputDigest, attempt (0 or 1), decisions with target, confidence, reason, evidence.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault',type=Path,required=True)
    sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('index');a.add_argument('--output',required=True)
    a=sub.add_parser('sample');a.add_argument('--output',required=True);a.add_argument('--count',type=int,default=10);a.add_argument('--seed',type=int,default=20261028)
    a=sub.add_parser('prepare');a.add_argument('--sample',required=True);a.add_argument('--index',required=True);a.add_argument('--output',required=True);a.add_argument('--resume',action='store_true')
    a=sub.add_parser('review-request');a.add_argument('--input',required=True);a.add_argument('--output',required=True)
    a=sub.add_parser('apply-review');a.add_argument('--input',required=True);a.add_argument('--report',required=True);a.add_argument('--output',required=True);a.add_argument('--human',action='store_true')
    a=sub.add_parser('render');a.add_argument('--input',required=True);a.add_argument('--output',required=True);a.add_argument('--queue');a.add_argument('--report',action='append',default=[])
    args=p.parse_args();vault=args.vault.resolve()
    if args.command=='index':write(args.output,build_index(vault))
    elif args.command=='sample':write(args.output,sample(vault,args.count,args.seed))
    elif args.command=='prepare':
        selection=json.loads(Path(args.sample).read_text());index=json.loads(Path(args.index).read_text())
        results=[]
        for row in selection['selected']:
            try:results.append({'id':row['id'],'status':prepare(vault,row,index,Path(args.output)/row['id'],args.resume)})
            except (ValueError,KeyError,OSError) as error:results.append({'id':row['id'],'status':'failed','reason':str(error)})
        print(json.dumps(results))
        if any(r['status']=='failed' for r in results):raise SystemExit(1)
    elif args.command=='review-request':write(args.output,review_request(json.loads(Path(args.input).read_text()),vault))
    elif args.command=='apply-review':
        data=json.loads(Path(args.input).read_text());report=json.loads(Path(args.report).read_text())
        if Path(args.output).exists():raise ValueError('Refusing to overwrite a saved session; write a candidate for review')
        write(args.output,apply_review(data,report,vault,'humanReviewed' if args.human else 'automatedReviewed'))
    elif args.command=='render':
        data=json.loads(Path(args.input).read_text())
        findings={}
        for report in args.report:
            findings.update({d['target']:d['reason'] for d in json.loads(Path(report).read_text())['decisions']})
        Path(args.output).write_text(render(data,vault,args.output,findings))
        if args.queue:write(args.queue,critical_queue(data))

if __name__=='__main__':main()

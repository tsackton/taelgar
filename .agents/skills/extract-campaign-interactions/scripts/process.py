#!/usr/bin/env python3
"""Deterministic support for agent-operated extract/review/correct batches; no hidden model calls."""
import argparse
import json
import random
import re
from pathlib import Path
import yaml
from session_model import validate, render, apply_review, critical_queue, digest, vault_path
from session_bundle import BundleError, BundleCatalog, fingerprint, load_bundle
from session_processing import new_processing, processing_digest, apply_processing_review, complete


def write(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str) + '\n')

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
    rows=[];excluded=[]
    for p in sorted((vault/'_sessions').glob('*/*/cleaned/*-session.yaml')):
        reference=str(p.relative_to(vault))
        try:
            bundle=load_bundle(vault,reference)
            manifest=bundle['metadata']
            names=[v for v in registry.values() if manifest['campaign'] in
                   [v.get('name'),v['code'],v['sessionRoot'],*v.get('aliases',[])]]
            if len(names)!=1:raise ValueError('Session YAML campaign is unknown or ambiguous')
            source=bundle['sources'][bundle['sourceId']]
            rows.append({'id':p.parent.parent.name,'campaign':names[0]['code'],'session':manifest['sessionNumber'],
                         'manifest':reference,'sourceId':bundle['sourceId'],'source':source['path'],
                         'sha256':source['sha256'],'inputs':bundle['inputs'],
                         'words':len((vault/source['path']).read_text().split())})
        except (ValueError,KeyError,OSError,yaml.YAMLError) as error:
            excluded.append({'manifest':reference,'reason':str(error),'proposedYamlFixes':getattr(error,'proposals',[])})
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
    data={'schemaVersion':6,'sessionYaml':selection['manifest'],
          'locations':[],'scenes':[],'entities':[],'interactions':[],
          'review':{'confidence':'low','status':'unreviewed'},'sceneReview':{'confidence':'low','status':'unreviewed'}}
    catalog=BundleCatalog(data,vault)
    source=catalog.sources[catalog.bundle['sourceId']]
    if source['sha256']!=selection['sha256'] or source['path']!=selection['source'] or catalog.inputs!=selection.get('inputs'):
        raise ValueError('Session YAML or source changed since sampling')
    if (output/'session.json').exists() or (output/'draft.json').exists():
        saved=output/'session-processing-data.json'
        if resume and saved.exists():
            processing=json.loads(saved.read_text())
            if processing['sessionYaml']==data['sessionYaml'] and processing['inputs']==catalog.inputs:
                return 'preserved'
        raise ValueError('Refusing to overwrite existing or changed execution')
    entries=index['entries'];pc_candidates=[]
    for participant in catalog.metadata.get('participants',[]):
        role=participant.get('gameRole')
        if not role or role.casefold() in {'dm','gm','unknown','dungeon master'}:continue
        pc_candidates.append({'role':role,'candidates':[e['path'] for e in entries if normalize(role) in e['keys']]})
    raw=catalog.compact()
    matches=[]
    for e in entries:
        hits=[n for n in e['names'] if len(n)>=4 and re.search(r'(?<!\w)'+re.escape(n)+r'(?!\w)',raw,re.I)]
        if hits:matches.append({**e,'matchedNames':hits})
    write(output/'draft.json',data)
    write(output/'candidates.json',{'pcCandidates':pc_candidates,'matches':matches})
    write(output/'session-processing-data.json',new_processing(data,catalog))
    (output/'transcript.txt').write_text(raw)
    return 'prepared'

def review_request(data,vault,processing=None):
    if data.get('schemaVersion')==6 and processing is None:raise ValueError('v6 review requires session-processing-data.json')
    checked=validate(data,vault,processing=processing)
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
    if data.get('schemaVersion')==6:
        manifest=cat.bundle['manifest']
        candidates=[manifest.with_name(manifest.name.replace('session.yaml',suffix)) for suffix in ['beats.json','beat-facts.json']]
        metadata=cat.metadata
    else:
        candidates=[(vault/source['path']).with_name(Path(source['path']).name.replace('source-cleaned.md',suffix))
                    for source in data['sources'] for suffix in ['beats.json','beat-facts.json']]
        metadata=data
    hints=[str(p.relative_to(vault)) for p in candidates if p.exists()]
    result={'inputDigest':fingerprint(data),'criticalMetadata':metadata,
            'entityEvidence':windows,'optionalReviewHints':hints,
            'instructions':'Independently review YAML consistency, PC participation, linked locations, entity inclusion and omissions. '
            'Beats and subsequent artifacts are noncanonical hints only. A YAML date span extending beyond the recording or clarifying an unstated date is not a contradiction. '
            'Record clear transcript/YAML date contradictions as critical metadataFindings with both kinds of evidence; do not change YAML. '
            'Review all excluded blocks and their reasons, plus unexplained coverage. Return reviewer, inputDigest, processingDigest, attempt, and decisions with evidence. '
            'Include session and scenes decisions; scene review covers exclusions as well as the scene division.'}
    if processing is not None:
        result.update(processingDigest=processing_digest(processing),inputs=processing['inputs'],
                      excludedBlocks=processing['excludedBlocks'],metadataFindings=processing['metadataFindings'],
                      unexplainedUtterances=checked['unexplainedUtterances'])
        assigned=set().union(*(cat.span(s['source']) for s in data.get('scenes',[])),
                             *(cat.span(b['source']) for b in processing['excludedBlocks']))
        missing=[]
        for sid,rows in cat.rows.items():
            run=[]
            for uid,row in rows.items():
                if (sid,row['position']) not in assigned:run.append(uid)
                elif run:
                    missing.append({'kind':'transcript','sourceId':sid,'startUid':run[0],'endUid':run[-1]});run=[]
            if run:missing.append({'kind':'transcript','sourceId':sid,'startUid':run[0],'endUid':run[-1]})
        result['unexplainedRanges']=missing
        result['locations']=data.get('locations',[])
    return result


def read_processing(data,input_path,explicit=None):
    if data.get('schemaVersion')!=6:return None
    path=Path(explicit) if explicit else Path(input_path).parent/'session-processing-data.json'
    return json.loads(path.read_text())

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--vault',type=Path,required=True)
    sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('index');a.add_argument('--output',required=True)
    a=sub.add_parser('sample');a.add_argument('--output',required=True);a.add_argument('--count',type=int,default=10);a.add_argument('--seed',type=int,default=20261028)
    a=sub.add_parser('inspect');a.add_argument('--session-yaml',required=True);a.add_argument('--output',required=True)
    a=sub.add_parser('prepare');group=a.add_mutually_exclusive_group(required=True);group.add_argument('--sample');group.add_argument('--session-yaml');a.add_argument('--index',required=True);a.add_argument('--output',required=True);a.add_argument('--resume',action='store_true')
    a=sub.add_parser('review-request');a.add_argument('--input',required=True);a.add_argument('--output',required=True);a.add_argument('--processing')
    a=sub.add_parser('apply-review');a.add_argument('--input',required=True);a.add_argument('--report',required=True);a.add_argument('--output',required=True);a.add_argument('--human',action='store_true');a.add_argument('--processing')
    a=sub.add_parser('render');a.add_argument('--input',required=True);a.add_argument('--output',required=True);a.add_argument('--queue');a.add_argument('--report',action='append',default=[]);a.add_argument('--processing')
    a=sub.add_parser('complete');a.add_argument('--input',required=True);a.add_argument('--processing');a.add_argument('--output',required=True)
    args=p.parse_args();vault=args.vault.resolve()
    if args.command=='index':write(args.output,build_index(vault))
    elif args.command=='sample':write(args.output,sample(vault,args.count,args.seed))
    elif args.command=='inspect':
        try:
            bundle=load_bundle(vault,args.session_yaml)
            write(args.output,{'sourceId':bundle['sourceId'],'inputs':bundle['inputs'],'proposedYamlFixes':bundle['proposals']})
        except BundleError as error:
            write(args.output,{'error':str(error),'proposedYamlFixes':error.proposals});raise SystemExit(1)
    elif args.command=='prepare':
        index=json.loads(Path(args.index).read_text())
        if args.sample:selection=json.loads(Path(args.sample).read_text())
        else:
            bundle=load_bundle(vault,args.session_yaml);source=bundle['sources'][bundle['sourceId']]
            selection={'selected':[{'id':bundle['root'].name,'manifest':args.session_yaml,'source':source['path'],
                                   'sha256':source['sha256'],'inputs':bundle['inputs']}]}

        results=[]
        for row in selection['selected']:
            try:results.append({'id':row['id'],'status':prepare(vault,row,index,Path(args.output)/row['id'],args.resume)})
            except (ValueError,KeyError,OSError) as error:results.append({'id':row['id'],'status':'failed','reason':str(error)})
        print(json.dumps(results))
        if any(r['status']=='failed' for r in results):raise SystemExit(1)
    elif args.command=='review-request':
        data=json.loads(Path(args.input).read_text())
        write(args.output,review_request(data,vault,read_processing(data,args.input,args.processing)))
    elif args.command=='apply-review':
        data=json.loads(Path(args.input).read_text());report=json.loads(Path(args.report).read_text())
        if Path(args.output).exists():raise ValueError('Refusing to overwrite a saved session; write a candidate for review')
        stage='humanReviewed' if args.human else 'automatedReviewed'
        processing=read_processing(data,args.input,args.processing)
        if processing is not None:
            result,evidence=apply_processing_review(data,processing,report,vault,stage)
            processing_output=Path(args.output).parent/'session-processing-data.json'
            original=Path(args.processing) if args.processing else Path(args.input).parent/'session-processing-data.json'
            if processing_output.exists() and processing_output.resolve()!=original.resolve():
                raise ValueError('Refusing to overwrite unrelated processing data')
            write(args.output,result);write(processing_output,evidence)
        else:write(args.output,apply_review(data,report,vault,stage))
    elif args.command=='render':
        data=json.loads(Path(args.input).read_text())
        processing=read_processing(data,args.input,args.processing)
        findings={}
        if processing:
            for record in processing['reviews']:findings.update({d['target']:d['reason'] for d in record['report']['decisions']})
        for report in args.report:
            findings.update({d['target']:d['reason'] for d in json.loads(Path(report).read_text())['decisions']})
        Path(args.output).write_text(render(data,vault,args.output,findings,processing=processing))
        if args.queue:write(args.queue,critical_queue(data,processing))

    elif args.command=='complete':
        data=json.loads(Path(args.input).read_text())
        print(json.dumps(complete(data,read_processing(data,args.input,args.processing),vault,args.output)))

if __name__=='__main__':main()

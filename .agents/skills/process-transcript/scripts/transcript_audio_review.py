"""Optional audio-review page. Answers live in session review Markdown only."""
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
import sys
import tempfile
from urllib.parse import urlparse

import transcript_core as core
import transcript_review as review
import transcript_finalize as final

VAULT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(VAULT / '_scripts'))
import audio_tools as audio

ASSET = Path(__file__).resolve().parents[1] / 'assets/audio-review.html'
CACHE_MARKER = '.taelgar-audio-review'


def cache_folder(path, create=False):
    path = Path(path).expanduser().resolve()
    core.require(not path.is_relative_to(VAULT), 'Keep temporary audio/page files outside the vault')
    if create and not path.exists(): path.mkdir(parents=True)
    marker = path / CACHE_MARKER
    if create and not marker.exists():
        core.require(not any(path.iterdir()), 'Use an empty audio-review output directory')
        marker.write_text('Generated audio-review cache. Answers are in session Markdown.\n')
    core.require(marker.is_file(), 'Not an owned audio-review cache directory')
    return path


def clean_cache(path):
    path = cache_folder(path)
    files = list(path.iterdir())
    core.require(all(p.is_file() and not p.is_symlink() and
                     (p.name in (CACHE_MARKER, 'index.html') or re.fullmatch(r'[a-f0-9]{64}\.m4a', p.name))
                     for p in files), 'Cache contains unrelated files; remove only reviewed generated files manually')
    for p in files: p.unlink()
    path.rmdir()
    return dict(removed=str(path))


def ensure_questions(root, uids):
    """Open selected finalized passages without initial-processing jobs."""
    if not review.report_path(root):
        review.prepare(root, uids)
        return
    if not uids: return
    path, meta, issues, updates, units, _, turns, _ = review.inputs(root)
    by_uid = {u['uid']: u for u in units}
    core.require(set(uids) <= set(by_uid), 'Unknown audio-review UID')
    missing = [uid for uid in dict.fromkeys(uids) if not any(i['uid'] == uid for i in issues)]
    if not missing: return
    for uid in missing:
        unit = by_uid[uid]
        issues.append(dict(id='audio-'+uid, uid=uid, target=dict(start=0,end=len(unit['text']),before=unit['text']),
                           contextRange=review.context_range(units,uid), proposal='',alternatives=[],
                           recommendation='Listen to this selected passage; preserve uncertainty if it remains unclear.',
                           question='What do you hear, or who is speaking?',resolution='pending',correction=''))
    meta['revisionActive'] = True
    text = review.document(meta,issues,units,turns)
    existing = {u['index']:u for u in updates}
    text = review.POLISH.sub(lambda m:'%% transcript-polish:v1 '+json.dumps(
        existing.get(json.loads(m[1])['index'], json.loads(m[1])),ensure_ascii=False)+' %%',text)
    core.atomic(root,str(path.relative_to(root)),text.encode())


def answer_version(meta, issue):
    return core.fingerprint(dict(hashes=meta['hashes'],audioReview=meta.get('audioReview'),issue=issue))


def clip_path(folder, clip):
    source = Path(clip['path'])
    st = source.stat()
    key = core.fingerprint(dict(source=str(source),size=st.st_size,mtime=st.st_mtime_ns,
                                start=clip['start'],end=clip['end'],profile='sample-v1'))
    return folder / (key+'.m4a')


def items_for(root, folder, *, extract=False, config=None, durations=None, prepared=None, work=None):
    if not review.report_path(root):
        core.require(final.completion(root), 'No review Markdown; prepare selected passages first')
        return []
    _, meta, issues, _, units, _, turns, _ = review.inputs(root)
    config = config or meta.get('audioReview')
    core.require(config, 'No audio selections saved for this session; run prepare')
    chosen = set(config['issueIds'])
    result = []
    by_uid = {u['uid']:u for u in units}
    for issue in issues:
        if issue['id'] not in chosen: continue
        clip = audio.map_audio_range(units,config['recordings'],issue['uid'],
                                    padding=config['paddingSeconds'],durations=durations)
        path = clip_path(folder,clip)
        if extract and not path.exists():
            source = Path(clip['path'])
            if source not in prepared:
                backend = audio.resolve_clip_backend()
                prepared[source] = audio.prepare_clip_source(source,backend=backend,work_dir=work)
            media, backend = prepared[source]
            # Interrupted extraction cannot leave a valid-looking cache entry.
            tmp = work / path.name
            audio.extract_audio_clip(media,tmp,start_seconds=clip['start'],end_seconds=clip['end'],backend=backend)
            tmp.replace(path)
        core.require(path.is_file() and path.stat().st_size > 0, 'Audio cache is missing or recording changed; run prepare again')
        uid = issue['uid']
        result.append(dict(key=hashlib.sha256((str(root)+'\0'+issue['id']).encode()).hexdigest(),
                           bundle=str(root), issueId=issue['id'], version=answer_version(meta,issue),
                           session=meta['title'],uid=uid,time=by_uid[uid]['timing'],target=issue['target']['before'],
                           original=issue['original'],proposal=issue['proposal'],question=issue['question'],
                           recommendation=issue['recommendation'],resolution=issue['resolution'],
                           answer=issue.get('audio'),
                           context=[dict(speaker=u['speaker'],text=u['text']) for u in review.context_units(units,issue['contextRange'])],
                           polished=[dict(speaker=t['speaker'],text=t['text']) for t in turns if any(s['uid']==uid for s in t['sources'])],
                           clip=path.name,targetStart=clip['targetStart'],targetEnd=clip['targetEnd']))
    return result


def prepare(selection, folder):
    core.require(isinstance(selection,dict) and isinstance(selection.get('sessions'),list) and selection['sessions'], 'Supply sessions')
    roots = [Path(s['bundle']).expanduser().resolve() for s in selection['sessions']]
    core.require(len(roots)==len(set(roots)), 'List each session once')
    folder = cache_folder(folder,create=True)
    durations, prepared, count = {}, {}, 0
    with tempfile.TemporaryDirectory(prefix='taelgar-audio-') as temp:
        for root, spec in zip(roots,selection['sessions']):
            core.require(root.is_dir(), 'Missing session bundle')
            with core.lock(root):
                if review.report_path(root):
                    core.require(review.read(root)[1].get('qualityComplete') is True,
                                 'This export is not ready for human review; finish its existing quality work first')
                ensure_questions(root,spec.get('uids',[]))
                path,meta,issues,_ = review.read(root)
                before = path.read_bytes()
                selected = spec.get('issueIds')
                if selected is None:
                    selected = [i['id'] for i in issues if not spec.get('uids') or i['uid'] in spec['uids']]
                core.require(selected and set(selected) <= {i['id'] for i in issues}, 'Select existing review questions')
                config = dict(issueIds=selected,recordings=spec.get('recordings',meta.get('audioReview',{}).get('recordings',[])),
                              paddingSeconds=spec.get('paddingSeconds',10))
                # Verify paths, clocks, references and clips before saving configuration.
                items = items_for(root,folder,extract=True,config=config,durations=durations,
                                  prepared=prepared,work=Path(temp))
                core.require(path.read_bytes()==before,'Review changed while preparing clips; rerun preparation without overwriting its answers')
                meta.update(audioReview=config,revisionActive=True)
                text = before.decode('utf-8')
                text = review.HEADER.sub(lambda m:'%% transcript-review:v1 '+json.dumps(meta,ensure_ascii=False)+' %%',text)
                core.atomic(root,str(path.relative_to(root)),text.encode())
                count += len(items)
    (folder/'index.html').write_bytes(ASSET.read_bytes())
    return dict(items=count,bundles=[str(p) for p in roots],output=str(folder),
                next='Serve this output directory with the same --bundle arguments. Answers remain in each review Markdown.')


def save_answer(root, issue_id, version, choice, answer):
    core.require(choice in ('answer','proposed','retain','defer'), 'Unknown audio answer choice')
    core.require(isinstance(answer,str) and len(answer)<=20000 and (choice!='answer' or answer.strip()), 'Type an answer or choose another disposition')
    with core.lock(root):
        path,meta,issues,_ = review.read(root)
        for rel,digest in meta['hashes'].items():
            core.require(core.current_hash(core.safe(root,rel))==digest,'Transcript changed; return to chat before saving')
        issue = next((i for i in issues if i['id']==issue_id),None)
        core.require(issue is not None and answer_version(meta,issue)==version,'This question or answer changed; reload before saving')
        core.require(issue['resolution']=='pending','This question already has a decision in chat')
        core.require(choice!='proposed' or issue['proposal'],'This question has no proposed reading')
        text = path.read_text(encoding='utf-8')
        matches = list(review.ITEM.finditer(text))
        n = next(n for n,m in enumerate(matches) if json.loads(m[1])['id']==issue_id)
        start = matches[n].end()
        end = matches[n+1].start() if n+1<len(matches) else len(text)
        section = text[start:end]
        for name,value in [('Audio choice',choice),('Audio answer',json.dumps(answer,ensure_ascii=False))]:
            pattern = r'^\*\*'+name+r':\*\*.*$'
            line = '**'+name+':** '+value
            if re.search(pattern,section,re.M): section = re.sub(pattern,lambda m:line,section,count=1,flags=re.M)
            else:
                at = section.index('**Conversation context:**')
                section = section[:at]+line+'\n\n'+section[at:]
        text = text[:start]+section+text[end:]
        meta['revisionActive'] = True
        text = review.HEADER.sub(lambda m:'%% transcript-review:v1 '+json.dumps(meta,ensure_ascii=False)+' %%',text)
        core.atomic(root,str(path.relative_to(root)),text.encode())
        issue['audio'] = dict(choice=choice,text=answer)
        return dict(answer=issue['audio'],version=answer_version(meta,issue))


def make_server(roots, folder, port=0):
    folder = cache_folder(folder)
    token = secrets.token_urlsafe(24)
    # Fixed allowlist; requests cannot supply arbitrary filesystem paths.
    initial = [item for root in roots for item in items_for(root,folder,durations={})]
    allowed = {item['key']:(Path(item['bundle']),item['issueId']) for item in initial}
    clips = {item['clip']:folder/item['clip'] for item in initial}
    html = (folder/'index.html').read_text().replace('__REVIEW_TOKEN__',token).encode()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args): pass
        def send(self,data,kind,status=200):
            self.send_response(status)
            self.send_header('Content-Type',kind)
            self.send_header('Content-Length',str(len(data)))
            self.send_header('Cache-Control','no-store')
            self.end_headers()
            self.wfile.write(data)
        def respond(self,value,status=200): self.send(json.dumps(value).encode(),'application/json',status)
        def do_GET(self):
            path = urlparse(self.path).path
            try:
                if path=='/': self.send(html,'text/html; charset=utf-8')
                elif path=='/api/review':
                    durations={}
                    self.respond(dict(items=[i for r in roots for i in items_for(r,folder,durations=durations) if i['key'] in allowed]))
                elif path.startswith('/clips/') and path[7:] in clips:
                    self.send(clips[path[7:]].read_bytes(),'audio/mp4')
                else: self.send_error(404)
            except (core.PipelineError,audio.MediaToolError,OSError,ValueError) as exc: self.respond(dict(error=str(exc)),409)
        def do_POST(self):
            if self.path!='/api/answer' or self.headers.get('X-Review-Token')!=token:
                self.send_error(403); return
            try:
                size=int(self.headers.get('Content-Length','0'))
                core.require(0<size<=100000,'Invalid request size')
                body=json.loads(self.rfile.read(size))
                root,issue=allowed[body['key']]
                self.respond(save_answer(root,issue,body['version'],body['choice'],body.get('text','')))
            except (core.PipelineError,ValueError,KeyError,TypeError,OSError) as exc: self.respond(dict(error=str(exc)),409)
    return ThreadingHTTPServer(('127.0.0.1',port),Handler)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('prepare');p.add_argument('--selection',choices=['-'],required=True);p.add_argument('--output-dir',type=Path,required=True)
    p=sub.add_parser('serve');p.add_argument('--bundle',type=Path,action='append',required=True);p.add_argument('--output-dir',type=Path,required=True);p.add_argument('--port',type=int,default=0)
    p=sub.add_parser('answers');p.add_argument('--bundle',type=Path,action='append',required=True)
    p=sub.add_parser('clean');p.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    try:
        if args.command=='prepare': result=prepare(json.load(sys.stdin),args.output_dir)
        elif args.command=='clean': result=clean_cache(args.output_dir)
        elif args.command=='answers':
            result=[dict(bundle=str(root.resolve()),issue=i) for root in args.bundle if review.report_path(root)
                    for i in review.read(root)[2] if i.get('audio')]
        else:
            server=make_server([p.expanduser().resolve() for p in args.bundle],args.output_dir,args.port)
            print(f'Audio review: http://127.0.0.1:{server.server_port}',flush=True)
            try: server.serve_forever()
            except KeyboardInterrupt: pass
            finally: server.server_close()
            return 0
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except (core.PipelineError,audio.MediaToolError,ValueError,KeyError,TypeError,OSError) as exc:
        print(json.dumps(dict(error=str(exc))),file=sys.stderr);return 1


if __name__=='__main__': raise SystemExit(main())

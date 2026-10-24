from pathlib import Path
import sys,re,json,hashlib,subprocess,yaml,importlib.util
B=Path(__file__).resolve().parent;BASE=B.parent;P='dunmari-frontier-045'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(n):return json.loads((B/f'{P}-{n}.json').read_text())
d=load('working-ledger');r=load('cleanup-report');a=load('cleanup-assessment');inv=load('morning-review-inventory');progress=load('cleanup-progress')
src=BASE/f'{P}-source-prepared.md';dst=BASE/f'{P}-source-cleaned.md'
source=src.read_bytes().splitlines(keepends=True);clean=dst.read_bytes().splitlines(keepends=True)
assert len(source)==len(clean)==1256
headers=lambda rows:[re.match(rb'^(\[[^\]]+\]\s)',s)[1] for s in rows]
assert headers(source)==headers(clean)
uids=lambda rows:[re.match(rb'^\[(u\d+)',s)[1].decode() for s in rows]
assert uids(source)==uids(clean)==[f'u{n:04d}' for n in range(1,1257)]
assert [re.search(rb'(\r?\n)?$',s)[0] for s in source]==[re.search(rb'(\r?\n)?$',s)[0] for s in clean]
for rel,h in d['inputFingerprints'].items():assert sha(BASE.parent/rel)==h,rel
assert sha(Path('_sessions/campaign-glossary.json'))==d['glossarySha256']
assert not r['validationErrors']
assert sum(x!=y for x,y in zip(source,clean))==r['changedLineCount']==561
fingerprint=sha(dst)
assert all(x==fingerprint for x in [r['review']['transcriptSha256'],a['transcriptSha256'],inv['transcriptSha256'],progress['transcriptSha256']])
marked={re.match(r'\[(u\d+)',s.decode())[1]:re.findall(r'\[\[(.+?)\]\]',s.decode()) for s in clean if b'[[' in s}
assert len(marked)==47 and sum(map(len,marked.values()))==48
assert set(marked)=={i['uid'] for i in a['issues']}=={i['uid'] for i in inv['material']}
assert all(i['importance']=='material' for i in a['issues'])
assert r['review']['pendingMaterialCount']==47 and r['review']['acceptedCount']==0
assert len(inv['incidental'])==73 and sum(len(i['spans']) for i in inv['incidental'])==75
assert not (B/f'{P}-cleanup-decisions.json').exists()
assert yaml.safe_load((BASE/f'{P}-session.yaml').read_text())['sessionNumber']==45
cor=yaml.safe_load((B/f'{P}-session-corrections.yaml').read_text());assert cor['allReplacements']
for p in B.glob('*.json'):json.loads(p.read_text())
for p in B.glob('*.yaml'):yaml.safe_load(p.read_text())
# Rebuild standard artifacts in memory, rather than rereading the transcript for a model-authored report.
sys.path.insert(0,str(Path('.agents/skills/transcript-cleaner/scripts').resolve()))
import report_cleanup_diff as report
before=report.read_transcript(src);after=report.read_transcript(dst)
report2,cor2=report.build_reports(before,after)
assert cor2==cor
for key in ('summary','lineCount','changedLineCount','validationErrors','unresolvedCount','unresolvedPhrases','changedLines'):assert report2[key]==r[key],key
assert report.build_human_transcript(after)==(B/f'{P}-human-transcript.md').read_text()
assert report.build_cleanup_summary_markdown(r,cor)==(B/f'{P}-cleanup-summary.md').read_text()
# Verify every contiguous first-pass and second-pass range is covered exactly once.
for passnum in (1,2):
 covered=[]
 for row in d['passes']:
  if row['pass']==passnum:
   lo,hi=map(lambda x:int(x[1:]),row['range'].split('-'));covered.extend(range(lo,hi+1))
 assert covered==list(range(1,1257)),passnum
scoped=subprocess.run(['git','diff','--check','--',str(BASE)],capture_output=True,text=True)
assert scoped.returncode==0 and not scoped.stdout and not scoped.stderr,(scoped.returncode,scoped.stdout,scoped.stderr)
# New files are untracked, so also check their full contents as additions.
additionChecks=[]
for p in sorted([dst]+[p for p in B.rglob('*') if p.is_file() and '__pycache__' not in p.parts]):
 if p.name==f'{P}-cleanup-verification.json':continue
 q=subprocess.run(['git','diff','--no-index','--check','--','/dev/null',str(p)],capture_output=True,text=True)
 assert q.returncode in (0,1) and not q.stdout and not q.stderr,(str(p),q.returncode,q.stdout,q.stderr)
 additionChecks.append(str(p.relative_to(BASE)))
status=subprocess.run(['git','status','--short','--',str(BASE.parent)],capture_output=True,text=True,check=True).stdout
assert all(('source-cleaned.md' in x or 'cleanup-artifacts/' in x) for x in status.splitlines()),status
verification={'status':'passed','unitCount':1256,'changedLineCount':561,'twoPassRangesVerified':True,'exactHeaderSeparatorTimestampSpeakerOrderPreservation':True,'lineEndingsPreserved':True,'preparedSha256':sha(src),'cleanedSha256':fingerprint,'originalSessionFilesVerifiedUnchanged':d['inputFingerprints'],'sharedGlossaryVerifiedUnchanged':d['glossarySha256'],'reportAssessmentInventoryProgressFingerprintsMatch':True,'standardArtifactsRebuiltAndCompared':True,'jsonAndYamlParse':True,'materialLines':47,'materialSpans':48,'incidentalLines':73,'incidentalSpans':75,'acceptedMaterialLines':0,'scopedGitDiffCheck':'passed','untrackedAdditionsWhitespaceChecks':'passed','checkedAdditions':additionChecks,'sessionGitStatus':status,'artifactSha256':{str(p.relative_to(BASE)):sha(p) for p in sorted([dst]+[x for x in B.glob(f'{P}-*') if x.is_file() and x.name!=f'{P}-cleanup-verification.json'])}}
(B/f'{P}-cleanup-verification.json').write_text(json.dumps(verification,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in verification.items() if k not in ('artifactSha256','originalSessionFilesVerifiedUnchanged','checkedAdditions','sessionGitStatus')},indent=2))

from pathlib import Path
import sys,json,re,hashlib,subprocess,datetime
import yaml
D=Path(__file__).resolve().parent
C=D.parent
P='dunmari-frontier-064'
root=C.parents[3]
sys.path.insert(0,str(root/'.agents/skills/transcript-cleaner/scripts'))
import report_cleanup_diff as diff
from review_cleanup import inventory

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def readj(p): return json.loads(p.read_text())
src=C/(P+'-source-prepared.md');clean=C/(P+'-source-cleaned.md')
a=src.read_bytes().splitlines(keepends=True);b=clean.read_bytes().splitlines(keepends=True)
assert len(a)==len(b)==2390
head=lambda v:v.split(b'] ',1)[0]+b'] '
assert all(head(x)==head(y) for x,y in zip(a,b))
assert all(x.endswith(b'\n')==y.endswith(b'\n') for x,y in zip(a,b))
ids=[re.match(rb'^\[(u\d+) \|',v).group(1).decode() for v in a]
assert ids==[f'u{i:04d}' for i in range(1,2391)] and len(set(ids))==2390
inputs=readj(D/'input-fingerprints.json')
for path,fingerprint in inputs.items(): assert sha(Path(path))==fingerprint,('input changed',path)
original=diff.read_transcript(src);cleaned=diff.read_transcript(clean)
report,corrections=diff.build_reports(original,cleaned)
assert not report['validationErrors']
actual=readj(D/(P+'-cleanup-report.json'))
for k,v in report.items(): assert actual[k]==v,('report mismatch',k)
assessment=readj(D/(P+'-cleanup-assessment.json'))
assert assessment['transcriptSha256']==sha(clean)==actual['review']['transcriptSha256']
assert actual['review']==inventory(clean,assessment,None)
assert yaml.safe_load((D/(P+'-session-corrections.yaml')).read_text())==corrections
assert (D/(P+'-human-transcript.md')).read_text()==diff.build_human_transcript(cleaned)
assert (D/(P+'-cleanup-summary.md')).read_text()==diff.build_cleanup_summary_markdown(actual,corrections)
review=readj(D/(P+'-morning-review.json'));audit=readj(D/(P+'-unit-review-audit.json'));progress=readj(D/(P+'-cleanup-progress.json'))
assert review['transcriptSha256']==audit['transcriptSha256']==progress.get('transcriptSha256',sha(clean))==sha(clean)
assert review['preparedSourceSha256']==audit['preparedSourceSha256']==sha(src)
assert review['counts']==progress['counts']
assert len(audit['units'])==2390 and all(u['firstPassInspected'] and u['strictSecondPassInspected'] for u in audit['units'])
assert sum(u['changed'] for u in audit['units'])==660
for e in review['material']+review['incidental']:
 j=e['lineNumber']-1
 assert e['uid']==ids[j]
 assert e['preparedSource']['quote']==original[j]['header']+' '+original[j]['text']
 assert e['cleanedVersion']['wording']==cleaned[j]['header']+' '+cleaned[j]['text']
 assert e['preparedSource']['contextBefore']==[x['header']+' '+x['text'] for x in original[max(0,j-2):j]]
 assert e['preparedSource']['contextAfter']==[x['header']+' '+x['text'] for x in original[j+1:j+3]]
 assert e['cleanedVersion']['contextBefore']==[x['header']+' '+x['text'] for x in cleaned[max(0,j-2):j]]
 assert e['cleanedVersion']['contextAfter']==[x['header']+' '+x['text'] for x in cleaned[j+1:j+3]]
 for excerpt in e.get('sourceReviewSpans',[]): assert excerpt in original[j]['text']
assert review['humanAcceptance'] is None and actual['review']['acceptedCount']==0
assert {e['uid'] for e in review['material']}=={e['uid'] for e in actual['review']['issues']}
assert sum(e['spanCount'] for e in review['material'])==actual['unresolvedCount']==64
assert len(review['material'])==actual['review']['pendingMaterialCount']==61
metadata=yaml.safe_load((C/(P+'-session.yaml')).read_text());assert metadata['sessionNumber']==64
for p in D.glob('*.json'):readj(p)
for p in D.glob('*.yaml'):yaml.safe_load(p.read_text())
for p in (D/(P+'-human-transcript.md'),D/(P+'-cleanup-summary.md'),D/(P+'-morning-review.md')):assert p.stat().st_size>0
tracked=subprocess.run(['git','diff','--check','--',str(C.relative_to(root))],cwd=root,text=True,capture_output=True)
assert tracked.returncode==0,tracked.stdout+tracked.stderr
whitespace=[]
for p in [clean]+sorted(q for q in D.iterdir() if q.is_file() and q.name!=P+'-verification.json'):
 result=subprocess.run(['git','diff','--no-index','--check','/dev/null',str(p)],cwd=root,text=True,capture_output=True)
 assert result.returncode in (0,1) and not result.stdout and not result.stderr,(str(p),result.returncode,result.stdout,result.stderr)
 whitespace.append(p.name)
files=[clean]+sorted(q for q in D.iterdir() if q.is_file() and q.name!=P+'-verification.json')
result={'status':'passed','verifiedAtUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'transcriptUnits':2390,'changedUnits':660,'exactHeadersSeparatorsSpeakersTimestampsAndOrder':True,'unitIdsUniqueAndContinuous':True,'lineEndingsPreserved':True,'bothFullPassesAudited':True,'inputFingerprintsUnchanged':len(inputs),'preparedSourceSha256':sha(src),'transcriptSha256':sha(clean),'standardReportRecomputedAndMatched':True,'correctionsYamlParsedAndMatched':True,'humanTranscriptAndSummaryRecomputedAndMatched':True,'assessmentFingerprintCurrent':True,'morningReviewQuotesAndContextsVerifiedAgainstPreparedSource':True,'allJsonAndYamlParse':True,'humanAcceptanceRecorded':False,'counts':review['counts'],'gitDiffCheck':'passed (scoped tracked diff plus no-index checks covering all new files)','whitespaceFilesChecked':whitespace,'outputs':{str(p.relative_to(C)):sha(p) for p in files},'scope':'Only session-064 cleaned output and cleanup-artifacts created; existing prepared/raw sources, metadata, stats and shared glossary are byte-identical to initial fingerprints.'}
(D/(P+'-verification.json')).write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in {'outputs','whitespaceFilesChecked'}},indent=2))

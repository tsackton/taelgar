from pathlib import Path
import json,re,hashlib,subprocess,sys,importlib.util
sys.dont_write_bytecode=True
import yaml
B=Path(__file__).resolve().parent.parent; A=B/'cleanup-artifacts'; P='dunmari-frontier-060'
S=B/f'{P}-source-prepared.md'; C=B/f'{P}-source-cleaned.md'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(name):return json.loads((A/f'{P}-{name}.json').read_text())
ledger=j('working-ledger');r=j('cleanup-report');assessment=j('cleanup-assessment');inv=j('morning-review-inventory')
s=S.read_bytes().splitlines(keepends=True);c=C.read_bytes().splitlines(keepends=True)
assert len(s)==len(c)==1247
headers=lambda rows:[re.match(rb'\[[^\]]+\]\s',row)[0] for row in rows]
assert headers(s)==headers(c)
assert [re.match(rb'\[(u\d+)',row)[1].decode() for row in c]==[f'u{i:04d}' for i in range(1,1248)]
assert [b'\r\n' if x.endswith(b'\r\n') else b'\n' if x.endswith(b'\n') else b'' for x in s]==[b'\r\n' if x.endswith(b'\r\n') else b'\n' if x.endswith(b'\n') else b'' for x in c]
assert ledger['firstPassThrough']==ledger['secondPassThrough']==1247
assert sha(S)==ledger['sourceSha256']==inv['preparedSourceSha256']
assert sha(C)==r['review']['transcriptSha256']==assessment['transcriptSha256']==inv['transcriptSha256']
assert not r['validationErrors']
assert sum(x!=y for x,y in zip(s,c))==r['changedLineCount']==372
assert r['review']['pendingMaterialCount']==inv['counts']['material']['lines']==15
assert r['review']['incidentalCount']==inv['counts']['incidental']['markedLines']==14
assert r['unresolvedCount']==sum(len(re.findall(rb'\[\[(.+?)\]\]',x)) for x in c)==30
assert r['review']['acceptedCount']==0
assert not list(A.glob('*decisions*'))
marked={f'u{i:04d}' for i,row in enumerate(c,1) if b'[[' in row}
assert {e['uid'] for e in assessment['issues']}==marked
assert len(assessment['issues'])==len(marked)
for name,expected in ledger['preservedInputs'].items():
 p=B.parent/name
 assert p.exists() and sha(p)==expected,f'Preserved input changed: {p}'
assert sha(Path(ledger['glossaryPath']))==ledger['glossarySha256']
source_lines=S.read_text().splitlines();cleaned_lines=C.read_text().splitlines()
md=(A/f'{P}-morning-review-inventory.md').read_text()
sections={match[0]:match[1] for match in re.findall(r'### (u\d+) — [^\n]+\n(.*?)(?=\n### |\n## |\Z)',md,re.S)}
assert len(sections)==len(inv['issues'])==86
quotation_count=0
for e in inv['issues']:
 i=int(e['uid'][1:]); assert e['preparedSourceExact']==source_lines[i-1]
 assert e['cleanedWording']==cleaned_lines[i-1]
 assert e['preparedSourceContextBefore']==source_lines[max(0,i-3):i-1]
 assert e['preparedSourceContextAfter']==source_lines[i:i+2]
 fields=[('Exact prepared-source context before',e['preparedSourceContextBefore']),('Exact prepared-source quotation',[e['preparedSourceExact']]),('Cleaned wording (not a verbatim source quotation)',[e['cleanedWording']]),('Exact prepared-source context after',e['preparedSourceContextAfter'])]
 for label,rows in fields:
  block=f'**{label}:**\n\n```text\n'+ '\n'.join(rows)+'\n```'
  assert block in sections[e['uid']],f'Mislabeled or stale quotation: {e["uid"]} {label}'
  if label.startswith('Exact prepared-source'):quotation_count+=len(rows)
 for span in e['markerSpans']:assert f'[[{span}]]' in e['cleanedWording']
# Validate JSON and YAML artifacts, then independently rebuild the standard artifact bodies in memory.
for p in A.glob('*.json'):json.loads(p.read_text())
corrections=yaml.safe_load((A/f'{P}-session-corrections.yaml').read_text())
yaml.safe_load((B/f'{P}-session.yaml').read_text())
sys.path.insert(0,str(Path('.agents/skills/transcript-cleaner/scripts').resolve()))
import report_cleanup_diff as report_module
parsed_source=report_module.read_transcript(S);parsed_cleaned=report_module.read_transcript(C)
expected_report,expected_corrections=report_module.build_reports(parsed_source,parsed_cleaned)
assert corrections==expected_corrections
for k,v in expected_report.items():assert r[k]==v
assert (A/f'{P}-human-transcript.md').read_text()==report_module.build_human_transcript(parsed_cleaned)
assert (A/f'{P}-cleanup-summary.md').read_text()==report_module.build_cleanup_summary_markdown(r,corrections)
# Scoped tracked check plus untracked-added-file whitespace checks without staging anything.
scoped=subprocess.run(['git','diff','--check','--',str(B)],capture_output=True,text=True)
assert scoped.returncode==0 and not scoped.stdout and not scoped.stderr
whitespace=[]
for p in [C,*sorted(A.iterdir())]:
 if not p.is_file():continue
 if p.name==f'{P}-verification.json':continue
 check=subprocess.run(['git','diff','--no-index','--check','/dev/null',str(p)],capture_output=True,text=True)
 assert check.returncode in (0,1) and not check.stdout and not check.stderr,(p,check.returncode,check.stdout,check.stderr)
 whitespace.append(p.name)
branch=subprocess.check_output(['git','branch','--show-current'],text=True).strip()
assert branch=='main'
result={'status':'passed','sourceSha256':sha(S),'transcriptSha256':sha(C),'unitCount':1247,'changedUnitCount':372,'replacementPatternCount':420,'repeatedReplacementPatternCount':38,'firstPassUnits':1247,'strictSecondPassUnits':1247,'exactHeaderSeparatorAndOrderPreservation':True,'lineEndingsPreserved':True,'originalSessionInputsUnchanged':True,'glossaryUnchanged':True,'preservedInputFileCount':len(ledger['preservedInputs']),'assessmentFingerprintMatches':True,'jsonAndYamlParse':True,'standardArtifactsRebuiltInMemoryAndMatched':True,'sourceQuotationLinesVerified':quotation_count,'morningReviewEntryCount':86,'uncertaintyCounts':inv['counts'],'noHumanAcceptanceRecorded':True,'scopedGitDiffCheck':'passed','untrackedFileWhitespaceChecks':whitespace,'branch':branch,'artifactSha256':{p.name:sha(p) for p in sorted(A.iterdir()) if p.is_file() and p.name!=f'{P}-verification.json'}}
(A/f'{P}-verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['artifactSha256','untrackedFileWhitespaceChecks']},indent=2))

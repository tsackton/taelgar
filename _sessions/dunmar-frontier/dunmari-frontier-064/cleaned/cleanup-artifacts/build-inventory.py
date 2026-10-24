from pathlib import Path
import json,re,hashlib,datetime
D=Path(__file__).resolve().parent
C=D.parent
P='dunmari-frontier-064'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def writej(name,x): (D/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
src=C/(P+'-source-prepared.md'); out=C/(P+'-source-cleaned.md')
a=src.read_text().splitlines(); b=out.read_text().splitlines()
r=json.loads((D/(P+'-cleanup-report.json')).read_text())
l=json.loads((D/'cleanup-ledger.json').read_text())
assert len(a)==len(b)==2390
for p in (1,2):
 coverage=[]
 for row in l['passes']:
  if row['pass']==p: coverage.extend(range(row['start'],row['end']+1))
 assert coverage==list(range(1,2391)),p
material=[]; incidental=[]
group_sets={
 'staff-ki-terminology':[63,2115,2123,2146,2150,2193,2197,2199],
 'infant-name-variants':[727,827],
 'dryad-travel-question':[1033,1044,1045],
 'kenzo-autobiographical-phrase':[1941,1942],
 'grash-recap':[2287,2290,2292,2298],
}
group_lookup={i:g for g,ids in group_sets.items() for i in ids}
def evidence(i):
 j=i-1
 return {'uid':f'u{i:04d}','lineNumber':i,'header':a[j].split('] ',1)[0]+']',
 'preparedSource':{'label':'Exact prepared-source quotations; verbatim, not corrected','quote':a[j],'contextBefore':a[max(0,j-2):j],'contextAfter':a[j+1:j+3]},
 'cleanedVersion':{'label':'Cleaned wording; editorial output, not a verbatim source quotation','wording':b[j],'contextBefore':b[max(0,j-2):j],'contextAfter':b[j+1:j+3]}}
for issue in r['review']['issues']:
 i=int(issue['uid'][1:]); e=evidence(i)
 e.update({'importance':'material','reason':issue['reason'],'group':group_lookup.get(i,f'unit-u{i:04d}'),'cleanedMarkedSpans':issue['phrases'],'spanCount':len(issue['phrases']),'decision':'pending'})
 material.append(e)
inc_reasons={k:v for k,v in l['incidentalReasons'].items() if k not in {'632','956','1319','1495'}}
inc_reasons['2203']="Trailing repeated 'I'm a way to' fragment after clear decision to wait; listed apart from the material cleansing-effect clause in this unit."
for k,reason in sorted(inc_reasons.items(),key=lambda kv:int(kv[0])):
 i=int(k);e=evidence(i)
 span="I'm a way to" if i==2203 else a[i-1].split('] ',1)[1]
 assert span in a[i-1]
 e.update({'importance':'incidental','reason':reason,'sourceReviewSpans':[span],'spanCount':1,'decision':'not requested; retained without human acceptance'})
 incidental.append(e)
counts={'transcriptUnits':len(a),'changedUnits':r['changedLineCount'],'replacementPatterns':r['summary']['replacementCount'],'materialLines':len(material),'materialSpans':sum(e['spanCount'] for e in material),'materialReviewGroups':len(set(e['group'] for e in material)),'incidentalLines':len(incidental),'incidentalSpans':sum(e['spanCount'] for e in incidental),'linesInBothCategories':len({e['uid'] for e in material}&{e['uid'] for e in incidental}),'humanAcceptedLines':0}
inventory={'schemaVersion':1,'session':P,'status':'cleanup_complete_review_pending','preparedSourceSha256':sha(src),'transcriptSha256':sha(out),'counts':counts,'sourceQuotationPolicy':'Every preparedSource.quote and context string is copied directly from the prepared file and verified against its indexed line. cleanedVersion and cleanedMarkedSpans are explicitly editorial wording and never labeled as verbatim prepared source.','incidentalSpanPolicy':'Each incidental review span is the whole exact source unit text unless a narrower span is supplied (u2203). Counts describe review excerpts, not guessed missing words. Material spans are individual [[...]] spans in the cleaned transcript. A unit may appear in both categories.','judgment':r['review']['assessment'],'material':material,'incidental':incidental,'humanAcceptance':None,'audioReviewRequested':False}
for e in material+incidental:
 j=e['lineNumber']-1
 assert e['preparedSource']['quote']==a[j]
 assert e['preparedSource']['contextBefore']==a[max(0,j-2):j]
 assert e['preparedSource']['contextAfter']==a[j+1:j+3]
 assert e['cleanedVersion']['wording']==b[j]
writej(P+'-morning-review.json',inventory)
md=['# Session 064 morning cleanup review','',
'Cleanup is complete. Human review remains pending; no acceptance or skipped decision has been recorded. Questions are logged here as requested.','',
f"Both passes inspected all {len(a):,} units. {counts['changedUnits']} units changed. Remaining material uncertainty: {counts['materialLines']} lines / {counts['materialSpans']} marked spans, arranged in {counts['materialReviewGroups']} review groups. Incidental review: {counts['incidentalLines']} lines / {counts['incidentalSpans']} excerpts. One line (u2203) appears in both categories for different spans.",'',
'The standard report counts marked lines only (61 material, 0 marked incidental). This inventory separately includes unmarked incidental speech. Incidental counts use one whole-unit review excerpt per line, except the narrower trailing fragment in u2203.','',
'Prepared-source quotations below are exact copies from the prepared file. Cleaned wording is explicitly labeled and may contain corrections and uncertainty markers; it is not a verbatim source quote. Source quotations and context have been checked against the prepared-file fingerprint.','',
'Priority review groups: staff ki/symbol spellings; infant-name variants and instructions; Kenzo’s mentor name (u1875); restoration/curse wording (u2028/u2033); the expected reunion contact (u2385). Other material fragments are listed individually. The earlier Grash vision is clearer than the garbled later recap.','',
f"Prepared SHA-256: `{sha(src)}`",f"Cleaned SHA-256: `{sha(out)}`",'',
'## Material review inventory','']
for e in material:
 md.extend([f"### {e['uid']} — {e['group']}",'',e['reason'],'',f"**Exact prepared-source quotation ({e['uid']}):**",'', '> '+e['preparedSource']['quote'],'',f"**Cleaned wording ({e['uid']}; editorial output):**",'', '> '+e['cleanedVersion']['wording'],'','**Exact prepared-source context before:**',''])
 md.extend(['> '+s for s in e['preparedSource']['contextBefore']] or ['(start of transcript)'])
 md.extend(['','**Exact prepared-source context after:**',''])
 md.extend(['> '+s for s in e['preparedSource']['contextAfter']] or ['(end of transcript)'])
 md.extend(['','Decision: pending.',''])
md.extend(['## Incidental speech inventory','','These fragments do not change the intelligible session actions or decisions. They remain available for optional review; no human acceptance is implied.',''])
for e in incidental:
 md.extend([f"### {e['uid']}",'',e['reason'],'','**Exact prepared-source quotation:**','', '> '+e['preparedSource']['quote'],'','**Cleaned wording (editorial output):**','', '> '+e['cleanedVersion']['wording'],'','**Exact prepared-source context:**',''])
 md.extend(['> '+s for s in e['preparedSource']['contextBefore']+e['preparedSource']['contextAfter']])
 md.append('')
(D/(P+'-morning-review.md')).write_text('\n'.join(md).rstrip()+'\n')
changed={x['lineNumber'] for x in r['changedLines']}
mat={e['lineNumber'] for e in material};inc={e['lineNumber'] for e in incidental}
units=[]
for i in range(1,2391):
 status=[]
 if i in changed: status.append('corrected_or_marked')
 if i in mat: status.append('material_uncertainty')
 if i in inc: status.append('incidental_speech')
 units.append({'uid':f'u{i:04d}','firstPassInspected':True,'strictSecondPassInspected':True,'classification':status or ['clean'],'changed':i in changed})
writej(P+'-unit-review-audit.json',{'preparedSourceSha256':sha(src),'transcriptSha256':sha(out),'units':units})
writej(P+'-cleanup-progress.json',{'status':'completed_with_pending_morning_review','preparedSourceSha256':sha(src),'transcriptSha256':sha(out),'modelRequested':'gpt-6.1-sol/high','passes':l['passes'],'counts':counts,'protectedNames':['Kenzo','Izzarak','DM'],'primaryEvidence':['dunmari-frontier-064-session.yaml','dunmari-frontier-064-source-prepared.md'],'glossary':'_sessions/campaign-glossary.json','secondaryEvidence':[],'archivalSourcesUsedAsCorrectionEvidence':False,'rawSourcesHashedOnlyForPreservation':True,'scope':'Session 064 cleaned output and cleanup-artifacts only. No recap, session pipeline, campaign note, shared index, commit, push, or new cleanup chat.','humanAcceptance':None})
print(json.dumps(counts,indent=2))

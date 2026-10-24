from pathlib import Path
import json,re,hashlib,yaml
B=Path(__file__).resolve().parent; BASE=B.parent; P='dunmari-frontier-045'
load=lambda n:json.loads((B/f'{P}-{n}.json').read_text())
r=load('cleanup-report');d=load('working-ledger')
d['incidental']['u1081']={'spans':["I wouldn't let me see",'be since'],'reason':'Garbled table lead-in and tail around the explicit pre/post Great War question; the DM immediately gives the timeframe.'}
(B/f'{P}-working-ledger.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
raw=(BASE/f'{P}-source-prepared.md').read_text().splitlines();clean=(BASE/f'{P}-source-cleaned.md').read_text().splitlines()
byuid={re.match(r'\[(u\d+)',s)[1]:j for j,s in enumerate(clean)}
material=[]
for i in r['review']['issues']:
 material.append({'uid':i['uid'],'importance':'material','spans':i['phrases'],'reason':i['reason'],'header':i['header'],'sourceLine':raw[i['index']],'cleanedLine':i['raw'],'contextBefore':i['before'],'contextAfter':i['after'],'status':'pending_human_review'})
incidental=[]
for uid,v in sorted(d['incidental'].items()):
 j=byuid[uid];spans=v.get('spans',[v.get('span')]);assert all(spans)
 for s in spans:assert s.casefold() in (raw[j]+'\n'+clean[j]).casefold(),(uid,s)
 incidental.append({'uid':uid,'importance':'incidental','spans':spans,'reason':v['reason'],'header':clean[j].split('] ',1)[0]+']','sourceLine':raw[j],'cleanedLine':clean[j],'contextBefore':clean[max(0,j-2):j],'contextAfter':clean[j+1:j+3],'status':'retained_unclear_no_acceptance_requested'})
assert not set(i['uid'] for i in material)&set(i['uid'] for i in incidental)
groups=[
 ('Opening Society reference',[7]),('Recovered items and addressee',[22,29]),('Creature discussion and prior family',[107,109,110,116,119,133,146]),('Mirror setup and position',[180,202,224]),('Surprise, visibility, and attack rulings',[283,293,304,305,328,340,352,353,355,378,379,389,390]),('Damage, flight, horn, and turns',[413,414,422,437,441,451,467]),('Earlier travelers',[718]),('Geography and maps',[855,868,894]),('Proposed object history and item function',[910,941]),('Dwarf vision setting and forest reference',[1046,1048,1057,1059]),('Diamond acquisition qualification',[1139]),('Coast, boats, and Seeker’s journey',[1177,1202,1211])]
groups=[{'id':f'M{x:02d}','topic':title,'unitIds':[f'u{n:04d}' for n in ns]} for x,(title,ns) in enumerate(groups,1)]
assert sorted(uid for g in groups for uid in g['unitIds'])==sorted(i['uid'] for i in material)
counts={'unitsInspectedPerPass':len(clean),'completedPasses':2,'changedLines':r['changedLineCount'],'replacementPatterns':r['summary']['replacementCount'],'repeatedReplacementPatterns':r['summary']['repeatedReplacementCount'],'materialLines':len(material),'materialSpans':sum(len(i['spans']) for i in material),'incidentalLines':len(incidental),'incidentalSpans':sum(len(i['spans']) for i in incidental),'acceptedMaterialLines':r['review']['acceptedCount']}
inv={'schemaVersion':'1.0','session':45,'status':'cleanup_complete_human_review_deferred','transcriptSha256':r['review']['transcriptSha256'],'sourceSha256':hashlib.sha256((BASE/f'{P}-source-prepared.md').read_bytes()).hexdigest(),'counts':counts,'reviewDisposition':'The user requested logging questions for morning review instead of chat. No uncertainty was accepted, no decisions file was created, no audio page or clips were requested or generated, and no downstream pipeline was run.','judgment':load('cleanup-assessment')['judgment'],'evidenceUsed':['adjacent session YAML','current prepared transcript','_sessions/campaign-glossary.json'],'archivalSources':'Fingerprint verification only; no archival transcript/config content used as correction evidence.','retainedPlausibleNewTerms':[{'uid':'u1241','term':'Navin','note':'Name is explicitly introduced in the source; retained as a plausible new entity without forcing a glossary match.'},{'uid':'u1219','term':'Emerald Sea','note':'Source wording retained with sea spelling/capitalization; glossary absence alone does not warrant replacing a plausible geographic name.'}],'materialGroups':groups,'material':material,'incidental':incidental}
(B/f'{P}-morning-review-inventory.json').write_text(json.dumps(inv,indent=2,ensure_ascii=False)+'\n')
m=['# Session 045 — morning cleanup review','',f"Cleanup is complete across {len(clean):,} units and both passes. **Human review remains pending; no uncertainty has been accepted.**",'',f"Changed lines: {counts['changedLines']}. Material uncertainty: **{counts['materialLines']} lines / {counts['materialSpans']} spans**. Incidental uncertainty: **{counts['incidentalLines']} lines / {counts['incidentalSpans']} spans**, retained without uncertainty markers.",'',f"Cleaned transcript SHA-256: `{inv['transcriptSha256']}`",'',inv['reviewDisposition'],'','This is a cleanup review inventory, not a session recap. Confirm uncertain wording or leave it unresolved; a later tolerance decision would not establish uncertain names or events as fact.','', '## Material review groups','']
for g in groups:m.append(f"- **{g['id']} — {g['topic']}**: {', '.join(g['unitIds'])}.")
m+=['','## Material lines — pending review','']
for i in material:
 m += [f"### {i['uid']}",'',f"**Review:** {i['reason']}",'',f"**Unresolved spans:** {'; '.join('`'+s+'`' for s in i['spans'])}",'','**Prepared source**','',i['sourceLine'],'','**Cleaned context**','']
 m += ['> '+s for s in i['contextBefore']+[i['cleanedLine']]+i['contextAfter']];m.append('')
m+=['## Incidental lines — retained unclear','', 'These fragments are not marked in the cleaned transcript. They concern table chatter, broken lead-ins, jokes, or redundant wording whose operative meaning is explicit nearby. They remain logged for optional review.','']
for i in incidental:
 m += [f"### {i['uid']}",'',f"**Spans:** {'; '.join('`'+s+'`' for s in i['spans'])}",'',i['reason'],'','**Prepared source**','',i['sourceLine'],'','**Cleaned context**','']
 m += ['> '+s for s in i['contextBefore']+[i['cleanedLine']]+i['contextAfter']];m.append('')
m+=['## Plausible source terms retained','']
for x in inv['retainedPlausibleNewTerms']:m.append(f"- {x['uid']} — **{x['term']}**: {x['note']}")
(B/f'{P}-morning-review-inventory.md').write_text('\n'.join(m)+'\n')
progress={'session':45,'status':'both_passes_complete_artifacts_generated_review_deferred','counts':counts,'passRanges':d['passes'],'sourceSha256':inv['sourceSha256'],'transcriptSha256':inv['transcriptSha256'],'protectedNames':['Kenzo','Wellby','Delwath','Seeker','Riswynn','Tim Sackton'],'usageChecksRemainingPercent':[95,94,94],'humanAcceptance':False,'decisionsFileCreated':False,'nextAction':'Human reviews the morning inventory; any later corrections require regenerating and reassessing fingerprinted artifacts.'}
(B/f'{P}-cleanup-progress.json').write_text(json.dumps(progress,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(counts,indent=2))

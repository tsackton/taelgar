from pathlib import Path
import json,re,hashlib,collections
B=Path(__file__).resolve().parent.parent
A=B/'cleanup-artifacts'; P='dunmari-frontier-060'
source=B/f'{P}-source-prepared.md'; cleaned=B/f'{P}-source-cleaned.md'
def read(p):return p.read_text().splitlines()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=read(source);cln=read(cleaned)
report=json.loads((A/f'{P}-cleanup-report.json').read_text())
ledger=json.loads((A/f'{P}-working-ledger.json').read_text())
judgments={
2:('material','departure-name','The identity/name rendered Phoeba is not securely resolved by the supplied glossary or same-session repetitions.'),
61:('incidental','gulf-circuit-word','The kind of circuit is garbled, but its Western Gulf setting and approximate week-long duration are clear.'),
72:('incidental','rumor-fragment','An abandoned rumor description; the response clearly discusses sailing rumors and the safe western waters.'),
89:('incidental','captain-rebuke','Garbled rebuke while deferring conversation; the request for sailing help and subsequent plan remain clear.'),
112:('material','scouting-negation','Cannot confidently distinguish can from can\'t in the list of abilities; negation changes the assertion.'),
156:('incidental','fire-reaction','Fragmentary reaction to using fire; the proposed action and later slowing of the pursuer are independently clear in this transcript.'),
192:('incidental','baxter-prompt','Garbled prompt about Baxter; the next response and subsequent stowing of him establish the action.'),
289:('material','command-reference','The referent after being commanded by the is unclear. The next unit mentions the scepter, but that does not establish the missing wording.'),
438:('incidental','burning-strike-leadin','Garbled lead-in to burning strike; subsequent explicit charge choices and actions establish what was used.'),
484:('material','attack-total','Garbled numerical attack total. The DM confirms a hit, but the exact result remains unknown.'),
491:('material','smoke-visibility','The smoke-obscuration clause contains an ambiguous or not; its exact substantive meaning is unresolved although the fire and enemy response are clear.'),
544:('material','armor-class-number','The number/AC reference is garbled. Earlier AC seventeen supports the likely reading but does not justify reconstructing all of this phrase.'),
656:('material','kenku-acquaintance','The assertion about knowing kenku or knowing of them is garbled; degree of personal familiarity is uncertain.'),
696:('incidental','story-timing-reaction','Garbled timing/reaction before telling the story. The following food and storytelling sequence is clear.'),
750:('incidental','welcome-leadin','Unclear transition or reaction; the following invitation to sail is explicit.'),
849:('material','salt-flavor-example','The salt example has a missing/unclear food referent. Preserve its limitation rather than inventing which food or drink changes flavor.'),
853:('material','salt-flavor-example','Unclear word in the same salt-flavor example; it may identify a food or drink.'),
860:('material','sea-people-names','Unclear name or place associated with the people being discussed; identity cannot be safely reconstructed.'),
866:('material','sea-people-names','The people rendered seals may be a name or other referent; do not infer their identity or species.'),
882:('material','sea-people-names','Two unclear spans obscure who might advise Wellby and the conditional comparison; Ceos may repeat the unresolved people reference.'),
905:('material','rotating-island-name','The rotating island name rendered calling me is unresolved. Quanyi is a possible hypothesis, not an established correction.'),
932:('material','language-name','The language name is rendered Easter; the exact language name is not established.'),
934:('material','language-name','Repeated Easter in the language-teaching passage; learning to communicate is clear, exact name uncertain.'),
1027:('incidental','tour-preference','Garbled tail of a tour request; the request, limited flight and ensuing tour are clear.'),
1046:('incidental','armor-interest-word','Unclear final word about armor\'s place in the people\'s work/culture; the expressed interest and identity of the armor experts are clear.'),
1073:('incidental','noisy-flight-reaction','Unclear aside after the observation that whistle flight is noisy; does not change the action.'),
1076:('incidental','pinnacle-description','Garbled repeated fragment in a visual description; red-stone pinnacles, the high landmark and route are clear.'),
1118:('incidental','water-description-leadin','Garbled lead-in; deep dark water and no signs of life are clear in this and the next unit.'),
1221:('incidental','pigment-modifier','Unclear additional word/modifier in the cargo list; dried chilies and rock pigment are explicit.'),
}
marked={i:re.findall(r'\[\[(.+?)\]\]',s.split('] ',1)[1]) for i,s in enumerate(cln,1) if '[[' in s}
assert set(marked)==set(judgments),(set(marked)-set(judgments),set(judgments)-set(marked))
assessment={'transcriptSha256':sha(cleaned),'judgment':'Both complete cleanup passes are finished. Main actions remain readable. Exact names/referents, a language name, a scouting negation, combat numbers, a smoke clause and the salt example retain material uncertainty. Review is logged for the morning at user direction; no human tolerance or acceptance is recorded.','issues':[{'uid':f'u{i:04d}','importance':judgments[i][0],'reason':judgments[i][2]} for i in marked]}
(A/f'{P}-cleanup-assessment.json').write_text(json.dumps(assessment,indent=2,ensure_ascii=False)+'\n')
entries=[]
for i in sorted(set(marked)|{int(k) for k in ledger['incidental']}):
 importance,group,reason=judgments[i] if i in marked else ('incidental','verbatim-table-fragments',ledger['incidental'][str(i)])
 body=cln[i-1].split('] ',1)[1]
 e={'uid':f'u{i:04d}','importance':importance,'issueGroup':group,'reason':reason,'markerSpans':marked.get(i,[]),'loggedSpanKind':'explicit-cleaned-marker' if i in marked else 'whole-unit-review-scope-retained-fragment','loggedSpanCount':len(marked[i]) if i in marked else 1,'preparedSourceExact':src[i-1],'cleanedWording':cln[i-1],'preparedSourceContextBefore':src[max(0,i-3):i-1],'preparedSourceContextAfter':src[i:i+2],'reviewStatus':'pending-morning-review' if importance=='material' else 'incidental-retained'}
 assert e['preparedSourceExact']==src[i-1]
 assert e['cleanedWording']==cln[i-1]
 if i not in marked: e['retainedVerbatim'] = src[i-1] == cln[i-1]
 entries.append(e)
counts={}
for imp in ['material','incidental']:
 es=[e for e in entries if e['importance']==imp]
 counts[imp]={'lines':len(es),'loggedSpans':sum(e['loggedSpanCount'] for e in es),'markedLines':sum(bool(e['markerSpans']) for e in es),'markedSpans':sum(len(e['markerSpans']) for e in es),'unmarkedRetainedLines':sum(not e['markerSpans'] for e in es),'unmarkedVerbatimLines':sum(not e['markerSpans'] and e['retainedVerbatim'] for e in es),'unmarkedPartiallyCorrectedLines':sum(not e['markerSpans'] and not e['retainedVerbatim'] for e in es),'issueGroups':len({e['issueGroup'] for e in es})}
inv={'schemaVersion':'1.0','sessionNumber':60,'preparedSourceSha256':sha(source),'transcriptSha256':sha(cleaned),'reviewStatus':'logged-for-morning-no-human-acceptance','quotationPolicy':'preparedSourceExact and preparedSourceContext fields are exact full prepared-source lines. cleanedWording is explicitly cleaned text, not a verbatim source quotation. All source quotations verified by unit position against the prepared file.','counts':counts,'issues':entries}
(A/f'{P}-morning-review-inventory.json').write_text(json.dumps(inv,indent=2,ensure_ascii=False)+'\n')
md=['# Session 060 morning cleanup review','', 'Cleanup is complete; material questions remain pending. The user requested logging for later review. No uncertainty has been accepted and no audio review page or clips were created.','',f'Prepared-source SHA-256: `{sha(source)}`',f'Cleaned-transcript SHA-256: `{sha(cleaned)}`','', '## Counts','',f"- Material: {counts['material']['lines']} units, {counts['material']['loggedSpans']} marked spans, {counts['material']['issueGroups']} grouped issues.",f"- Incidental: {counts['incidental']['lines']} units, {counts['incidental']['loggedSpans']} logged spans ({counts['incidental']['markedSpans']} explicit markers; {counts['incidental']['unmarkedRetainedLines']} whole-unit review scopes, including {counts['incidental']['unmarkedVerbatimLines']} unchanged units and {counts['incidental']['unmarkedPartiallyCorrectedLines']} partially corrected unit).",'', 'A logged span is an explicit `[[...]]` span, or one whole-unit review scope for an unmarked incidental fragment. Partially corrected units are identified in the JSON and their cleaned wording is always labeled separately. These are not additional removed lines.','', 'Source quotations below are exact full units from the prepared file. Cleaned wording is labeled separately and must not be quoted as verbatim prepared source. Context before/after is also exact prepared text.','']
for imp,title in [('material','Material questions'),('incidental','Incidental retained speech')]:
 md.extend([f'## {title}',''])
 for e in entries:
  if e['importance']!=imp: continue
  md.extend([f"### {e['uid']} — {e['issueGroup']}",'',e['reason'],'',f"- Logged spans: {e['loggedSpanCount']}; type: {e['loggedSpanKind']}.",'- Status: '+e['reviewStatus']+'.','', '**Exact prepared-source context before:**','', '```text',*e['preparedSourceContextBefore'],'```','', '**Exact prepared-source quotation:**','', '```text',e['preparedSourceExact'],'```','', '**Cleaned wording (not a verbatim source quotation):**','', '```text',e['cleanedWording'],'```','', '**Exact prepared-source context after:**','', '```text',*e['preparedSourceContextAfter'],'```',''])
(A/f'{P}-morning-review-inventory.md').write_text('\n'.join(md).rstrip()+'\n')
print(json.dumps(counts,indent=2))

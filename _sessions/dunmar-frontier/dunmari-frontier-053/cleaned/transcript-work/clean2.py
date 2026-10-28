from editor import *
j=json.loads((W/'jobs/clean-chunk-002.json').read_text()); s={int(u['uid'][1:]):u['text'] for u in j['source']}; c={}
def rep(n,a,b,why,kind='asr'): c[n]=(c.get(n,(s[n],))[0].replace(a,b),why,kind)
rep(181,'{{where Ainumarya was in the forest}}','where Ainumarya was in the forest','Question and answer establish a spoken geographical question, not a recognition error.','uncertainty')
rep(202,'{{word but kinky let up}}','where the kenku live','Immediately preceding unit introduces kenku beyond the mountains; sounds and syntax recover their plains habitat.')
rep(203,'{{some up looped in}}',"Cha'mutte moved in",'Earlier Great War account names Cha’mutte; near-sound wording and destruction context support this recovery.')
rep(222,'{{Mexico}}',"the Te'kula",'Direct reply to the preceding statement about time spent at the Te’kula village.')
rep(226,'{{we probably hear me}}','we probably hear me','Unrecoverable incidental interjection before the clear scheduling exchange; no distinct substantive reading can be established.','uncertainty')
rep(227,'{{Now said me}}','No, he said','Following mid-fall and didn’t he make the remembered statement construction clear.')
rep(228,'{{strike them}}','scryed him','Near-sound recovery in discussion of what Grash most recently said remotely, not an attack.')
rep(267,'{{more than a year ago now August, the past summer}}','more than a year ago now August, the past summer','Keep spoken timing and disfluency; chronological inconsistency alone is not ASR evidence.','uncertainty')
issues=[]
def issue(n,span,kind,proposal,reason,recommendation,question,alternatives=[]):
 issues.append(dict(uid=f'u{n:04}',span=span,kind=kind,importance='material',proposal=proposal,reason=reason,recommendation=recommendation,question=question,alternatives=alternatives))
issue(203,'{{hours}}','place',s[203].replace('{{some up looped in}}',"Cha'mutte moved in"),'The geographical referent after north of the is not recoverable from hours; it could identify a boundary or people.','Retain this span unresolved pending an audio check of 19:12–19:26; no defensible named replacement is established.','Supply the spoken geographical referent, or retain {{hours}} as unresolved?')
issue(278,'{{Dunbar}}','item',"Yeah, it's exactly the day that the armband was destroyed.",'Dunbar may be a misrecognition of armband; choosing changes what event anchors the date.','Prefer armband from the immediately preceding destruction/date discussion, but check the noun in the audio at 26:25–26:29.','Replace Dunbar with armband, supply the spoken noun, or retain unresolved?')
issue(304,'{{maybe destroying them has some time, maybe good return}}','action',s[304],'The damaged clause may assert a delayed return or merely the possibility of release; the causal claim is consequential.','Retain unresolved pending audio at 28:37–28:45. Destruction enabling a return is clear from the exchange, but reconstructing the timing claim would invent wording.','Supply the damaged clause, or retain it unresolved without adding a timing claim?')
issue(319,'{{when the sun rise}}','time',s[319].replace('{{when the sun rise}}','without a sunrise'),'Recognition may have lost a negative/without, changing whether the battle ended at sunrise or endured without one.','Prefer without a sunrise from the name Endless Dark and the following shadow description, but those facts do not prove the spoken wording.','Use without a sunrise, use when the sun rose, supply other wording, or retain unresolved?',[s[319].replace('{{when the sun rise}}','when the sun rose')])
clean(2,c,issues)

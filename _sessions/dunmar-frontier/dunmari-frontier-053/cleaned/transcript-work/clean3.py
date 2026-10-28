from editor import *
j=json.loads((W/'jobs/clean-chunk-003.json').read_text()); s={int(u['uid'][1:]):u['text'] for u in j['source']}; c={}
def rep(n,a,b,why,kind='asr'): c[n]=(s[n].replace(a,b),why,kind)
rep(360,'{{Oh ma}}','Ohma','Repeated near-identical pronunciation in u0361 establishes a personal name. Preserve this spoken name rather than substituting the later session-note name Jotha.','name')
rep(361,'{{oh my}}','Ohma','Same warrior named in preceding sentence; recognition split a repeated personal name into an exclamation.','name')
rep(404,'{{like his name it\'ll be a feat}}',"like his name it'll be a feat",'Damaged incidental hypothetical spell banter; subsequent giant demon reply remains intact, no concrete decision needs human adjudication.','uncertainty')
rep(461,'{{I accurate}}','I accurate','Unrecoverable abandoned filler after the clearly spoken two-day stay; no competing time reading.','uncertainty')
rep(497,'{{On the enemy}}','On the enemy','Incidental fragment in shield decoration description; preserve words without a material-review marker.','uncertainty')
rep(513,'I suspect, to text me','I suspect he’ll text me','Missing subject/auxiliary recovered from the prediction of receiving a Thursday text.')
clean(3,c)

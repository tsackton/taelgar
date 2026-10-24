from pathlib import Path
import json, hashlib, re
BASE=Path(__file__).resolve().parent.parent
PREFIX='dunmari-frontier-060'
SRC=BASE/f'{PREFIX}-source-prepared.md'
OUT=BASE/f'{PREFIX}-source-cleaned.md'
ART=BASE/'cleanup-artifacts'
LEDGER=ART/f'{PREFIX}-working-ledger.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if not LEDGER.exists():
    state={'sourceSha256':sha(SRC),'protectedNames':['Wellby','DM','David Schwartz','Tim Sackton'], 'glossaryPath':'_sessions/campaign-glossary.json','glossarySha256':sha(Path('_sessions/campaign-glossary.json')), 'preservedInputs':{str(p.relative_to(BASE.parent)):sha(p) for p in BASE.parent.rglob('*') if p.is_file() and 'cleanup-artifacts' not in p.parts and p!=OUT},'changes':{},'incidental':{},'firstPassThrough':0,'secondPassThrough':0,'notes':[]}
else: state=json.loads(LEDGER.read_text())
original=SRC.read_text().splitlines()
texts={int(re.match(r'\[u(\d+)',s)[1]):s.split('] ',1)[1] for s in original}
def patch(changes, through=None, second=None, incidental=None, note=None):
    for uid,text in changes.items():
        assert uid in texts
        state['changes'][str(uid)]=text
    if through is not None: state['firstPassThrough']=through
    if second is not None: state['secondPassThrough']=second
    if incidental: state['incidental'].update({str(k):v for k,v in incidental.items()})
    if note: state['notes'].append(note)
    assert sha(SRC)==state['sourceSha256']
    OUT.write_text('\n'.join(s.split('] ',1)[0]+'] '+state['changes'].get(str(i),texts[i]) for i,s in enumerate(original,1))+'\n')
    LEDGER.write_text(json.dumps(state,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__': patch({})

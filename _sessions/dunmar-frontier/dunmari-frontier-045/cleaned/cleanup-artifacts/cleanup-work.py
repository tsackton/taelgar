from pathlib import Path
import json, re, hashlib
BASE=Path(__file__).resolve().parent.parent
ART=BASE/'cleanup-artifacts'
PREFIX='dunmari-frontier-045'
SOURCE=BASE/f'{PREFIX}-source-prepared.md'
TARGET=BASE/f'{PREFIX}-source-cleaned.md'
LEDGER=ART/f'{PREFIX}-working-ledger.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
    return json.loads(LEDGER.read_text()) if LEDGER.exists() else {'edits':{},'incidental':{},'materialReasons':{},'passes':[], 'inputFingerprints':{str(p.relative_to(BASE.parent)):sha(p) for p in BASE.parent.rglob('*') if p.is_file() and 'cleanup-artifacts' not in p.parts and not p.name.endswith('source-cleaned.md')},'glossarySha256':sha(Path('_sessions/campaign-glossary.json'))}
def save(d):
    lines=[]
    for raw in SOURCE.read_text().splitlines():
        if not raw: lines.append(raw); continue
        h,t=raw.split('] ',1); uid=h[1:].split(' |')[0]
        t=d['edits'].get(uid,t)
        # Unambiguous orthographic errors only; no sentence rephrasing.
        t=re.sub(r'\bi\b','I',t)
        t=re.sub(r'\b(kenzo|wellby|delwath|riswynn|seeker)\b',lambda m:m[0].capitalize(),t,flags=re.I)
        lines.append(h+'] '+t)
    TARGET.write_text('\n'.join(lines)+'\n')
    LEDGER.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def change(d,n,*pairs):
    uid=f'u{n:04d}'
    source=next(x.split('] ',1)[1] for x in SOURCE.read_text().splitlines() if x.startswith('['+uid+' |'))
    t=d['edits'].get(uid,source)
    for a,b in pairs:
        assert a in t,(uid,a,t)
        t=t.replace(a,b)
    d['edits'][uid]=t

def flag(d,n,span,reason):
    change(d,n,(span,'[['+span+']]'))
    d['materialReasons'][f'u{n:04d}']=reason

def incidental(d,n,span,reason='Unclear incidental table chatter; does not alter the recorded action.'):
    d['incidental'][f'u{n:04d}']={'span':span,'reason':reason}
if __name__=='__main__':
    save(load())

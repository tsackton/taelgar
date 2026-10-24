import hashlib,json,re
from pathlib import Path
BASE=Path('_sessions/dunmar-frontier/dunmari-frontier-054/cleaned')
ART=BASE/'cleanup-artifacts'
SRC=BASE/'dunmari-frontier-054-source-prepared.md'
OUT=BASE/'dunmari-frontier-054-source-cleaned.md'
LEDGER=ART/'dunmari-frontier-054-edit-ledger.json'
def apply(edits, end, pass_number=1):
    lines=(OUT if OUT.exists() else SRC).read_text().splitlines()
    ledger=json.loads(LEDGER.read_text()) if LEDGER.exists() else []
    for uid,pairs in edits.items():
        i=int(uid.removeprefix('u'))-1
        before=lines[i]
        header,text=before.split('] ',1)
        for old,new in pairs:
            assert old in text,(uid,old,text)
            text=text.replace(old,new)
        lines[i]=header+'] '+text
        ledger.append({'uid':f'u{i+1:04d}','pass':pass_number,'before':before.split('] ',1)[1],'after':text})
    OUT.write_text('\n'.join(lines)+'\n')
    LEDGER.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
    p=ART/'dunmari-frontier-054-progress.json'
    state=json.loads(p.read_text()) if p.exists() else {}
    state.update({f'pass{pass_number}InspectedThrough':f'u{end:04d}','complete':False})
    p.write_text(json.dumps(state,indent=2)+'\n')
if not (ART/'dunmari-frontier-054-input-fingerprints.json').exists():
    files=list(BASE.parent.rglob('*'))+[Path('_sessions/campaign-glossary.json')]
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file() and 'cleanup-artifacts' not in p.parts and p!=OUT}
    (ART/'dunmari-frontier-054-input-fingerprints.json').write_text(json.dumps(hashes,indent=2)+'\n')

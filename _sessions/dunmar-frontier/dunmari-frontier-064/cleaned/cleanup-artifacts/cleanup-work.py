from pathlib import Path
import json, hashlib, re, sys
D=Path(__file__).resolve().parent
C=D.parent
P='dunmari-frontier-064'
src=C/(P+'-source-prepared.md')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if not (D/'input-fingerprints.json').exists():
 files=list(C.parent.rglob('*'))+[Path('_sessions/campaign-glossary.json').resolve()]
 (D/'input-fingerprints.json').write_text(json.dumps({str(p.resolve()):sha(p) for p in files if p.is_file() and D not in p.resolve().parents},indent=2)+'\n')
payload=json.load(sys.stdin)
(D/"last-request.json").write_text(json.dumps(payload,indent=2)+"\n")
ledger_path=D/'cleanup-ledger.json'
ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {'edits':{},'materialReasons':{},'incidentalReasons':{},'passes':[]}
for k,v in payload.get('edits',{}).items():
 ledger['edits'].setdefault(k,[]).extend(v)
for field in ('materialReasons','incidentalReasons'):
 ledger[field].update(payload.get(field,{}))
ledger['passes'].extend(payload.get('passes',[]))
lines=src.read_text().splitlines()
for k,pairs in ledger['edits'].items():
 i=int(k)-1
 header,text=lines[i].split('] ',1)
 for old,new in pairs:
  assert old in text, (k,old,text)
  text=text.replace(old,new)
 lines[i]=header+'] '+text
(C/(P+'-source-cleaned.md')).write_text('\n'.join(lines)+'\n')
ledger_path.write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
print('Saved',len(ledger['edits']),'edited units;',ledger['passes'][-1] if ledger['passes'] else '')

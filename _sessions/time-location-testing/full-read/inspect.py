"""Lossless spoken-turn windows. No speaker/keyword filtering in full mode."""
from setup import ROOT,load,PAT
import sys,json,re,hashlib
n=int(sys.argv[1]);mode=sys.argv[2];s,ts=load(n)
if mode=='inventory':
 raw=__import__('pathlib').Path(s['transcript']).read_text()
 print(raw.split('## Transcript')[0]);print('TURNS',len(ts),'CHARS',sum(len(t['text']) for t in ts))
 # Check parser preserves all transcript body text except source maps and headings.
 matched=list(re.finditer(r'%% ([^%]+) %%\s*([^\n]+): ([\s\S]*?)(?=\n%% |\Z)',raw))
 assert len(matched)==len(ts)
 suffix=raw[raw.index('## Transcript')+len('## Transcript'):].strip()
 assert re.sub(r'\s+', '', suffix)==re.sub(r'\s+', '', ''.join(m.group(0) for m in matched))
 print('All body text accounted for by parsed turns.')
else:
 lo=int(sys.argv[3]) if len(sys.argv)>3 else 1;hi=int(sys.argv[4]) if len(sys.argv)>4 else len(ts)
 for i,t in enumerate(ts,1):
  if lo<=i<=hi and (mode=='full' or PAT.search(t['text'])):print(f"[{i}] {t['start']}-{t['end']} {t['speaker']}: {t['text']}")
 print(f'END {n}: turn indexes {lo}-{min(hi,len(ts))} / {len(ts)}')

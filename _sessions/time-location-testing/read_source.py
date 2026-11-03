"""Read-only transcript inspection; all outputs go to stdout."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parent
SAMPLE=json.loads((ROOT/'sample.json').read_text())
def load(n):
 s=next(s for s in SAMPLE['selected'] if s['session']==int(n))
 text=Path(s['transcript']).read_text()
 turns=[]
 for m in re.finditer(r'%% ([^%]+) %%\s*([^\n]+): ([\s\S]*?)(?=\n%% |\Z)',text):
  uids=re.findall(r'u\d+',m[1]); turns.append({'start':uids[0],'end':uids[-1],'mapping':m[1],'speaker':m[2],'text':m[3].strip()})
 return s,turns
PAT=re.compile(r'\b(morning|afternoon|evening|night|dawn|dusk|sunset|sunrise|noon|midday|midnight|rest|sleep|slept|wake|woke|hours?|minutes?|days?|weeks?|months?|today|tomorrow|yesterday|later|next|arriv\w*|enter\w*|leave|leaving|left|return\w*|head\w*|reach\w*|travel\w*|walk\w*|ride|riding|journey|teleport\w*|camp|room|chamber|corridor|stairs|door|passage|outside|inside|across|towards|through)\b',re.I)
if __name__=='__main__':
 s,ts=load(sys.argv[1]); mode=sys.argv[2] if len(sys.argv)>2 else 'candidates'
 lo=int(sys.argv[3]) if len(sys.argv)>3 else 0; hi=int(sys.argv[4]) if len(sys.argv)>4 else 99999
 for i,t in enumerate(ts):
  if int(t['end'][1:])<lo or int(t['start'][1:])>hi:continue
  if mode=='all' or mode=='dm' and t['speaker']=='DM' or mode=='candidates' and PAT.search(t['text']):
   print(f"{t['start']}-{t['end']} {t['speaker']}: {t['text']}")

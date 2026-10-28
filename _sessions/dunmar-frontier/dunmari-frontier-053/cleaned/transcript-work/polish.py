from editor import *
def polish(n):
 j=json.loads((W/f'jobs/polish-chunk-{n:03}.json').read_text()); units={int(u['uid'][1:]):u for u in j['source']}; turns=[]
 subs={49:'the idea track',177:'The best hundreds',178:'now before us',226:'we probably hear me',248:"Is one that's daily",257:"her now it'll actually here",367:'foreign car',404:"like his name it'll be a feat",461:'I accurate',497:'On the enemy',511:'is complaining'}
 for line in (W/f'polish{n}.txt').read_text().splitlines():
  if not line.strip():continue
  bounds,t=line.split('|',1); ab=bounds.split('-'); a=int(ab[0]); b=int(ab[-1]); us=[units[k] for k in range(a,b+1)]; speakers={('Delwath' if u['uid']=='u0036' else u['speaker']) for u in us}; assert len(speakers)==1,(a,b,speakers)
  if t=='=': t=' '.join(u['text'] for u in us)
  turn=dict(speaker=speakers.pop(),sources=[dict(uid=u['uid'],start=0,end=len(u['text'])) for u in us],text=t)
  ss=[]
  for k in range(a,b+1):
   if k in subs:
    u=units[k]; phrase=subs[k]; st=u['text'].index(phrase);ss.append(dict(uid=u['uid'],start=st,end=st+len(phrase),kind='garbled',reason='Unrecoverable incidental recognition debris; retain intelligible speech and substantive content around this exact span.'))
  if ss:turn['substitutions']=ss
  turns.append(turn)
 if n in (2,3,4):turns[0]['joinPrevious']=True
 r=dict(schemaVersion=1,stage='polish',chunkId=j['chunk']['id'],sourceSha256=j['sourceSha256'],turns=turns)
 (B/j['responsePath']).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':polish(int(sys.argv[1]))

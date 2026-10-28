import json,pathlib,sys
B=pathlib.Path('/workspace/taelgar/_sessions/dunmar-frontier/dunmari-frontier-053'); W=B/'cleaned/transcript-work'
def clean(n,changes,issues=[],attrs={}):
 j=json.loads((W/f'jobs/clean-chunk-{n:03}.json').read_text()); edits=[]; mentions=[]
 terms={'person':['Theba','Aasimti',"Birich'iko","Ch'ik'a",'Kenzo','Wellby','Seeker','Delwath','Yezali','Nisir',"K'onisati","Yalik'I",'Taraka','Midri','Ninu','Zevi',"A'gaza","Cha'mutte",'Grash','Jotha','Istari','Enon',"Mo'kati",'the man', 'the stoneborn','the wildfire druid','the younger boy'], 'group':["Te'kula","Deno'qai",'Meswati','silent ones',"Ko'zula","Shu'anra",'stoneborn','kenku','dwarves'], 'place':['material world','Feywild',"Eudomes' Tower",'Ainumarya','Elder Forest','Elderwood','Tinitaka','Forest of Nightmares','Forest of Dreams','Pandar','Voltara','Chardon','Blackwater Fens','Yemo\'te','the village','our village','hunting camp'], 'time':['late afternoon','dusk','evening','in the morning','two day journey','Great War','Battle of Darkfire','hundreds of years','many generations','a generation','400, 500 years ago','October 2','10 days','mid-fall','June','after dinner','more than a year ago','August','the past summer','a few years back','the next day','two days','Thursday','September'], 'item':['longbow','scale mail','shield','mammoth tusk','Mage Hand','armband','circlets','runes','mithral','magic circle','magical arrows']}
 for u in j['source']:
  t=u['text']; num=int(u['uid'][1:])
  if num in changes:
   after,reason,kind=changes[num]; edits.append(dict(uid=u['uid'],before=t,after=after,reason=reason,kind=kind,evidence=[f"u{max(1,num-2):04}-u{min(531,num+2):04}"])); t=after
  for kind,ts in terms.items():
   for term in ts:
    if term in t: mentions.append(dict(uid=u['uid'],kind=kind,text=term))
 r=dict(schemaVersion=1,stage='clean',chunkId=j['chunk']['id'],sourceSha256=j['sourceSha256'],checks=['people','groups','places','time_transitions','items','actions','unmarked_errors','second_pass'],edits=edits,issues=issues,mentions=mentions)
 if attrs: r['attributions']=[dict(uid=f'u{k:04}',start=0,end=len(next(u['text'] for u in j['source'] if u['uid']==f'u{k:04}')),speaker=v,reason='First-person player reply continues Delwath’s action during DM description.',evidence=['u0031-u0038']) for k,v in attrs.items()]
 (B/j['responsePath']).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
 j=json.loads((W/'jobs/clean-chunk-001.json').read_text()); s={int(u['uid'][1:]):u['text'] for u in j['source']}
 clean(1,{1:(s[1].replace('have to have the', 'of, of the'),'ASR substituted a verb phrase for repeated preposition before the tribe name.','asr'),91:(s[91].replace('90','I need').replace('riskin','reskin'),'Answer to what brings him here and tabletop discussion of character reskin recover near-sound recognition errors.','asr'),152:(s[152].replace('{{','').replace('}}',''),'Geographical doubt is not evidence of misrecognition; preserve spoken distance and direction.','uncertainty')},attrs={36:'Delwath'})

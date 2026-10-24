import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={1008:[('does good, but [[with a bitch]]','[[does good]], but with advantage')],1012:[('That not show up','Did that not show up')],1034:[('her will actually','her— well actually')],1042:[("underground's",'underground')],1052:[('dwarves than','dwarves then')],1059:[('secret where where the [[secret Copyright Office]]','[[secret where where the secret Copyright Office]]')],1064:[('Next Chardon— next','Next chart next')],1067:[('heart hardly','Hardly hardly')],1078:[('you got turned','who got turned')],1090:[('Ending you','And then you')],1103:[('What it looked like','What did he look like')],1119:[('walking in holding','walking and holding')],1128:[('treating this','treating us')],1131:[('[[list the courts]]','lift the corpse')],1144:[('ERA','era')],1145:[('Now, maybe','No, maybe')],1177:[('enough up the coast','[[enough up the coast]]')],1192:[('you can sea','you can see')],1197:[('river in the city','river and the city')],1205:[('point where the rulers','point were the rulers')],1206:[('those halflings',"there's halflings")],1211:[('to be','to [[be]]')],1213:[('or here','over here')],1219:[('[[Emerald see]]','Emerald Sea')],1221:[('ships that are Dunmari themselves','ships. The Dunmari themselves')],1224:[('So Songara','to Songara')],1235:[('All the way this','All the way east')],1240:[("UN you've learned","and you've learned")],1242:[('He is a','His')],1250:[('week we','We we')],1252:[('next time to','next time too')]}
for n,p in C.items():w.change(d,n,*p)
# Orthography of a compound creature name is unambiguous, without changing the entity.
for n in (1206,1207):w.change(d,n,('lizard folk','lizardfolk'))
for n in (1131,1219):d['materialReasons'].pop(f'u{n:04d}',None)
for n,r in {1008:'Unclear words describing inspiration; advantage is recoverable from the surrounding explanation.',1177:'Unclear location wording in explanation of why Chardon does not offer an ocean view.',1211:'Unclear destination at the end of Seeker’s lizardfolk-contact story.'}.items():d['materialReasons'][f'u{n:04d}']=r
d['incidental'].pop('u1240',None)
w.incidental(d,1064,'chart','Abandoned fragment before the clear statement that the vision shows Chardon.')
w.incidental(d,1081,"I wouldn't let me see",'Garbled lead-in to the explicit pre/post Great War question and answer.')
w.incidental(d,1151,'that again point','Incidental praise of the mirror as a storytelling device.')
d['passes'].append({'pass':2,'range':'u1001-u1256','status':'every unit inspected again; compound spelling, phonetic errors, and unintended replacement fixed'});w.save(d)
print('Strict second pass complete through u1256')

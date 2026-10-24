import importlib
w=importlib.import_module('cleanup-work');d=w.load()
C={
1052:[('sun and for us','sun and forest')],1054:[('Be for us','Big forests')],
1057:[("we're doing current place that that sounds like a river that's flowing down for its turn","[[we're doing current place that]] that sounds like a river that's flowing down towards Chardon")],
1059:[('secret Copyright Office','[[secret Copyright Office]]')],
1062:[('this trend that is','this then is'),('charting','Chardon')],
1064:[('chart next','Chardon— next'),('charting','Chardon')],
1067:[('racking as a discharge and','recognize it as Chardon')],1075:[('hassling','Halfling')],
1078:[('got turned to would','got turned to wood')],
1081:[('TIM','Tim'),('chart in','Chardon'),('progress for pre great work was Great War be since','post- or pre-Great War, post-Great War, [[be since]]')],
1083:[('half flings','halflings')],1084:[('well be','Wellby')],1088:[('done mar','Dunmar')],
1090:[('toker','Tokra')],1093:[('a goddess',"Agata's")],1094:[('hot','hut')],
1095:[('tea drinking tea','[[tea]] drinking tea')],1096:[("And all they're done Marty man",'An older Dunmari man')],
1099:[('a gotta','Agata')],1103:[('distinction','distinctive')],
1111:[('done Mari','Dunmari'),('close','clothes')],1113:[('TIM','Tim')],
1114:[('working wearing','wearing'),("Royal and Sydney hasn't shipped",'royal insignia and shit')],
1116:[('know','No')],1121:[('tails','tales'),("i'll get to",'Agata')],
1125:[('damn it','diamond')],1126:[("there's no use the diamond",'if she used the diamond')],
1128:[('treating us','treating this')],1129:[('nobody to think','no reason to think')],
1131:[('list the courts','[[list the courts]]')],
1135:[('seem','scene'),('took her','Tokra')],
1139:[('completely','[[completely]]')],
1144:[('seven years','70 years')],
1154:[('with a woman, I don\'t like this',"[[with a woman, I don't like this]]")],1155:[('TIM','Tim')],
1165:[('DARPA','Darba'),('garbage','Darba')],1167:[('the in where','the inn where')],
1170:[('darby','Darba')],1171:[('in the sun','and the sun')],
1172:[('route on river','Rudhan River')],1175:[('well beer cans out','Wellby or Kenzo')],
1177:[('The other chart and does actually enough','Although Chardon is actually enough'),('charmin','Chardon')],
1178:[('our secret','or Seeker')],1179:[('My not','Might not')],
1181:[("well he's he's", "Wellby who's")],1182:[('della','Delwath')],1183:[('della','Delwath')],
1188:[('don\'t bow down','On a boat down')],
1192:[('white class i\'m stone click','white limestone cliffs'),('see','sea')],
1194:[('garbage','Darba')],
1195:[('Korean Korean for','Drankorian fort')],
1196:[('A six','The six'),('oh four','old fort'),('Captain ending','commanding')],
1198:[('drain Korean','Drankorian'),('motifs have confronted','motifs of confronted'),('gate invisible','gate visible')],
1199:[('densely set all','densely settled'),("wouldn't",'wooden')],
1202:[('high proud loria hold','high-prowed [[loria hold]]')],
1203:[('delorean','Illorian')],1204:[('Laurens','Illorians'),('Navajo see','Nevos Sea')],
1205:[('conquer darby','conquered Darba')],1206:[('happenings','halflings')],
1208:[('He created really','[[He created really]]')],
1215:[('selling ships','sailing ships'),('math and square rig cardone and trading carnivals','masted square-rigged Chardonian trading caravels')],
1216:[('lorean','Illorian'),('sales','sails')],
1217:[('sea of storms','Sea of Storms')],
1219:[('Emerald see','[[Emerald see]]'),('dharma','Darba')],
1221:[('done Mari','Dunmari'),('Mario','Dunmari'),('single master and then Mari','single-masted Dunmari')],
1222:[('dunmore','Dunmari'),('as a trainer','is a trader'),('chart Ionian carnivals','Chardonian caravels')],
1224:[('son got South tonight Har','Songara, south to Nayahar')],
1227:[("where's",'Weirs'),('adopt','dot'),('Linda dharma','inland of Darba')],
1229:[('males','mills')],1231:[('token','Tokra')],
1232:[('dark done margin','Dunmar')],1233:[('Nice car','Nashtkar')],
1234:[('I archaeologists out okay','[[I archaeologists out]] okay')],
1235:[('toker','Tokra'),('constraints','constructed'),('nyan','Nayan')],
1236:[('DARPA','Darba'),('Denmark','Dunmar'),('grand Korean Ford','Drankorian fort')],
1240:[('UN', '[[UN]]')],
1241:[('DARPA','Darba'),('navin','Navin')],1243:[('drink Korean','Drankorian')],
1245:[('ends','inns')],1246:[('done Mary','Dunmari')],
1252:[("you would stand out much", "you wouldn't stand out much"),('noted on','noted')],
1253:[('to humans to doors and to half links with','two humans two dwarves and two halflings would')],
1254:[('dealt with','Delwath'),('poses hood','pulls his hood')],
}
for n,p in C.items():w.change(d,n,*p)
for n,sp in [(1154,"with a woman, I don't like this"),(1234,'I archaeologists out'),(1240,'UN')]:
    d['materialReasons'].pop(f'u{n:04d}',None)
# Keep clearly incidental chatter verbatim, not marked.
for n in (1154,1234,1240):
    d['edits'][f'u{n:04d}']=d['edits'][f'u{n:04d}'].replace('[[','').replace(']]','')
for n,sp in [(1081,'be since'),(1095,'tea')]:
    d['edits'][f'u{n:04d}']=d['edits'][f'u{n:04d}'].replace('[['+sp+']] ',sp+' ').replace('[['+sp+']]',sp)
    w.incidental(d,n,sp)
for n,sp in [(1154,"with a woman, I don't like this"),(1234,'I archaeologists out'),(1240,'UN')]:w.incidental(d,n,sp)
R={1057:'Unclear lead-in to recognizing the river/forest route in the vision.',1059:'Unclear secret place/object associated with the forest.',1131:'Unclear proposed way Agata might fulfill a resurrection request literally.',1139:'Unclear qualification of how the man acquired the diamond.',1202:'Unclear boat description beyond the high prow.',1208:'Unclear question/comment about Seeker’s prior lizardfolk contact.',1219:'Unclear sea name in description of distant trading partners.'}
for n,r in R.items():d['materialReasons'][f'u{n:04d}']=r
d['passes'].append({'pass':1,'range':'u1051-u1256','status':'individually inspected; local corrections and uncertainty recorded'});w.save(d)
print('First pass complete through u1256')

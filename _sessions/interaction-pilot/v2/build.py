"""Reproduce five reviewed trial sidecars from the frozen vault sources."""
from pathlib import Path
import json, hashlib, re, sys, copy
V=Path('/workspace/taelgar'); OUT=Path(__file__).parent
sys.path.insert(0,str(V/'.agents/skills/extract-campaign-interactions/scripts'))
from validate import validate, render

def uid(n): return f'u{n:04d}'
def sp(a,b=None): return {'startUid':uid(a),'endUid':uid(a if b is None else b)}
def frozen(p): return {'path':str(p),'sha256':hashlib.sha256((V/p).read_bytes()).hexdigest()}
def rows(d):
 return {m[1]:m[2] for line in (V/d['source']['path']).read_text().splitlines() if (m:=re.match(r'^\[(u\d+)(?:\s*\|.*?)?\]\s?(.*)$',line))}
def quote(d,r,a,b=None,text=None,kind='dialogue',attribution=None):
 b=b or a; rr=rows(d); passage=' '.join(rr[uid(n)] for n in range(a,b+1))
 assert text is None or text in passage,(a,b,text,passage)
 r['pull_quote']={**sp(a,b),'kind':kind,'quote':text or passage,'speaker':r['npc'],'attribution':attribution or 'DM voices this NPC during the surrounding direct exchange.'}
 return r

def rec(d,npc,a,b,overview,kind='interacted',importance='supporting',ex=None,**kw):
 ss=[s['index'] for s in d['scenes'] if int(s['startUid'][1:])<=b and int(s['endUid'][1:])>=a]
 r={'id':f'{npc}-{a:04d}','npc':npc,'scenes':ss,'interaction':kind,'importance':importance,'overview':overview,'transcript':[sp(a,b)]}
 if len(ss)>1:r['continuity']='One encounter continues across these location/time boundaries; other speakers and brief asides remain inside its source range.'
 if ex:r['excerpts']=[sp(*x) if isinstance(x,tuple) else sp(x) for x in ex]
 r.update(kw);d['interactions'].append(r);return r

def ent(d,id,label,overview,note=None,basis=None,eligibility=None):
 e={'id':id,'label':label,'canonical_name':Path(note).stem if note else None,'note':note,'eligibility':eligibility or ('named' if note else 'individual'),'basis':basis or 'Named in the session transcript; identity corroborated by the linked note.','session_overview':overview}
 d['entities'].append(e)
 if note and not any(s['path']==note for s in d['supporting_sources']):d['supporting_sources'].append(frozen(note))
 return e

def finish(d):
 for e in d['entities']:
  own=[r for r in d['interactions'] if r['npc']==e['id']];qs=[r for r in own if r.get('pull_quote')]
  e['overview_records']=[r['id'] for r in own]
  e['quote_review']='selected' if qs else e.get('quote_review','no_suitable_dialogue' if any(r['interaction']=='interacted' for r in own) else 'not_applicable')
  if qs:e['featured_quote_interaction']=e.get('featured_quote_interaction',qs[0]['id'])
 p=OUT/d['session'];p.mkdir(exist_ok=True)
 rr,span=validate(d,V)
 (p/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
 (p/'review.md').write_text(render(d,V,rr,span))
 (p/'evidence.md').write_text(render(d,V,rr,span,excerpts=True))
 print(d['session'],len(d['scenes']),'scenes',len(d['entities']),'NPCs',len(d['interactions']),'interactions',sum(bool(r.get('pull_quote')) for r in d['interactions']),'quotes')
 return d

def base(root,sid,campaign,note):
 folder=f'_sessions/{root}/{sid}/cleaned'; stem=f'{folder}/{sid}'
 return {'schema_version':2,'campaign':campaign,'session':sid,'segmentation_revision':1,
 'source':{**frozen(stem+'-source-cleaned.md'),'kind':'transcript'},
 'supporting_sources':[frozen(stem+s) for s in ('-session.yaml','-beats.json','-beat-facts.json')]+[frozen(note)],
 'scenes':[],'excluded_ranges':[],'entities':[],'interactions':[],'review_notes':[]}

def scene(d,a,b,loc,day,time,boundary,basis=None,end=None):
 d['scenes'].append({'index':len(d['scenes'])+1,**sp(a,b),'location':loc,'boundary':boundary,
 'date':{'start':day,'end':end or day,'time':time,'basis':basis or 'Day from session-note timeline; relative time and movement from this source passage.','evidence':[d['supporting_sources'][0]['path'],d['supporting_sources'][3]['path'],f'{uid(a)}–{uid(b)}']}})

def old(n):
 d=json.loads((OUT.parent/f'session-{n}/extraction.json').read_text());d['schema_version']=2
 d['interactions']=[]
 d['review_notes'] += ['Version 2 retest: full conversational encounters replace highlight-only bounds; original segmentation is retained for stable scene joins. NPC cards carry one session overview and a featured attributed quote where available.']
 return d

d=old('008')
views={'candrosa':'Candrosa is recalled as the intended recipient of the centaurs’ warning; she does not appear.', 'kisa':'The party draws on Kisa’s earlier account of raids while interpreting the hyena-headed creatures; she does not appear.', 'taster':'Seeker names and keeps Taster after testing the stream water on him, and the party carries and protects the rabbit during the outpost exploration.', 'inakara':'The cavern ruler demands help against a creature in exchange for passage, guides the party to it, watches their battle, and afterward declines to guarantee their onward safety.'}
for e in d['entities']:e['session_overview']=views[e['id']]
rec(d,'candrosa',5,6,'Opening narration recalls the centaurs leaving to warn Candrosa about the corruption.','mentioned','cameo')
rec(d,'kisa',129,144,'The party recalls Kisa’s account of raids while considering the creatures’ origin.','mentioned')
r=rec(d,'taster',547,596,'Seeker tests the stream water on a rabbit, names him Taster, and decides to keep him.',ex=[(563,564),(578,589)])
r['introduction']={**sp(586),'kind':'dialogue','quote':'Previously unnamed rabbit. I now dub thee Taster.'}
rec(d,'taster',620,624,'Seeker tells the party to watch Taster for effects from the water.','mentioned','cameo')
rec(d,'taster',707,713,'Seeker takes Taster along as the party leaves the horses outside.','interacted','cameo')
rec(d,'taster',1299,1306,'Someone protectively strokes Taster when Kenzo suggests testing the illusory rubble with him.','interacted','cameo')
r=rec(d,'inakara',1383,1848,'The party bargains for passage with the cavern ruler and follows her to the creature she demands they kill.','interacted','star',[(1472,1524),(1689,1703),(1737,1744)])
r['introduction']={**sp(1418),'kind':'description','quote':'black nails and sort of gray and purple skin that looks bruised'}
rec(d,'inakara',1974,1979,'During the fight, the party notices the cavern ruler watching and chuckling.','observed','cameo')
r=rec(d,'inakara',2808,2835,'After the creature dies, the ruler points out the exit but declines to guarantee the party’s safety.','interacted','star',[(2809,2832)])
quote(d,r,2827,text='The door is that way; you make safe passage for yourself.')
d['review_notes'] += ['Inakara’s negotiation and guided approach now form one interaction across scenes 13–15; combat observation and the subsequent exchange remain separate. Taster’s naming line is a PC introduction, not speech by the rabbit.']
finish(d)

d=old('060')
views={'wella':'Wella welcomes Wellby aboard, accepts his help escaping pirates, offers onward passage, and discusses routes home before introducing him to Makha at Wahacha.', 'pearl':'Pearl accepts Wellby’s help defending the Wave Dancer and warns him about the pursuing ship’s weapons before his sabotage attempt.', 'corrin':'Corrin conceals the ship in fog, sketches Wellby a map of the shifting islands, and later reports a clear horizon.', 'rose':'Rose accompanies the evening meal and conversation with guitar music after Wella introduces her as her wife.', 'makha':'Makha guides Wellby around Wahacha, explains the raids and missing kenku, offers food, and arranges a meeting with other travelers who may help.', 'skoda':'Wellby learns that the kidnapped Skoda may understand his kenku armor and help him find a route home.', 'nahto':'Wellby hears that Nahto, Skoda’s kidnapped partner, traveled widely through the Eastern Isles and might help with his search for the Feywild.', 'baxter':'Baxter accompanies Wellby aboard the Wave Dancer, is stabled below during the danger, and is introduced to Makha at Wahacha.', 'chamutte':'Wella mentions Cha’mutte’s enslavement of kenku while explaining how Wahacha’s people differ from that lineage.', 'session060-hold-sailor':'An unnamed sailor helps Wellby stable Baxter, explains the dragonhide cargo, and recommends asking Corrin for a map.'}
for e in d['entities']:e['session_overview']=views[e['id']]
rec(d,'wella',23,190,'Wellby explains his arrival to the captain and offers to help the Wave Dancer escape its pursuers.','interacted','star',[(27,45),(100,125)],known_as='Wave Dancer captain')
rec(d,'pearl',114,190,'Pearl meets Wellby and accepts his offer to help defend the ship.',ex=[(114,125)])
rec(d,'baxter',191,194,'Baxter stands on deck while Wellby asks for a place to stable him.','present','cameo',presence_basis='u0191 explicitly places Baxter standing on deck.')
rec(d,'session060-hold-sailor',195,232,'A sailor helps stable Baxter, explains the dragonhide trade, and suggests asking Corrin for a map.',ex=[(195,205),(208,227)])
rec(d,'baxter',195,197,'Wellby and a sailor settle Baxter in the hold.','interacted','cameo')
rec(d,'corrin',195,232,'The sailor recommends Corrin as someone who could draw Wellby a map.','mentioned','cameo',[(224,227)])
rec(d,'wella',233,242,'The captain remains on deck when Wellby returns from the hold.','present','cameo',presence_basis='u0233–u0242 explicitly says the captain is still on deck.')
r=rec(d,'pearl',255,281,'Wellby asks Pearl about the pursuers’ defenses before attempting aerial sabotage.',ex=[(265,276)])
quote(d,r,267,text='Watch out for that ballista.')
rec(d,'wella',257,258,'Wellby notices the captain monitoring the wind and sails.','observed','cameo')
rec(d,'baxter',279,281,'Before flying off, Wellby asks the crew to care for Baxter if he does not return.','mentioned','cameo')
r=rec(d,'corrin',560,697,'Wellby congratulates Corrin on the concealing fog and receives a map and explanation of the shifting islands.',ex=[(560,574),(589,606),(683,697)])
quote(d,r,593,594,text='Maps are not much use out here. The land moves too much.')
rec(d,'wella',566,569,'The captain nods to the navigator before he creates the fog bank.','observed','cameo')
r=rec(d,'wella',580,927,'Over a shared meal, Wellby tells Wella his story and discusses onward passage and possible crossings into the Feywild.','interacted','star',[(581,588),(729,753),(884,900)])
quote(d,r,751,753)
rec(d,'rose',700,725,'Rose plays guitar during Wellby’s meal and conversation with the crew.','observed','cameo',[(700,702),719])
rec(d,'corrin',726,728,'Corrin reports that there are no lights on the horizon.','observed','cameo')
rec(d,'chamutte',729,927,'Wella describes Cha’mutte’s enslavement of kenku while distinguishing Wahacha’s inhabitants.','mentioned','cameo',[(774,789)])
rec(d,'wella',944,980,'Wella tells Wellby that Wahacha’s unusually quiet harbor worries her.',ex=[(965,973)])
rec(d,'wella',981,1011,'At the dock, Wella introduces Wellby and Baxter to Makha.','interacted','cameo',[(1002,1005)])
r=rec(d,'makha',981,1243,'Makha guides Wellby around Wahacha, explains the kidnappings, buys lunch, and arranges a meeting with other travelers.','interacted','star',[(1002,1023),(1101,1125),(1199,1209),(1225,1243)])
quote(d,r,1001,text='The seas here are not safe these days.')
rec(d,'baxter',1002,1011,'Baxter is beside Wellby during the introductions to Makha.','present','cameo',presence_basis='u1002–u1005 explicitly brings Wellby and Baxter over together; no independent action by Baxter is described.')
rec(d,'skoda',981,1243,'Makha explains that the kidnapped Skoda may understand Wellby’s armor and offer help finding a route home.','mentioned','supporting',[(1031,1047),(1155,1170),(1179,1186)])
rec(d,'nahto',981,1243,'Makha describes Nahto’s kidnapping and travels as Wellby considers possible help reaching the Feywild.','mentioned','supporting',[(1039,1047),(1162,1177)])
rec(d,'wella',1217,1243,'Makha suggests asking Wella or another halfling for help finding the inn.','mentioned','cameo',[(1225,1234)])
d['review_notes'] += ['Makha’s seven former scene records become one continuous guided visit spanning scenes 14–20. Wella’s dinner conversation stays together through Corrin’s report and topic changes. Explicit idle presence now covers Baxter on deck and at introductions, and Wella remaining on deck.']
finish(d)

# Lost in the Feywild 6: one sustained library conversation, then the prison threshold.
d=base('feywild','lost-in-the-feywild-006','feywild','Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 06.md')
for a,b,loc,boundary in [(56,946,'Library — research assistant’s desk','Played opening; conversation and preparations remain in the library.'),(947,972,'Library — crossing the stacks','Party leaves the desk and crosses the room.'),(973,1043,'Prison doorway — three windows','Arrival at the prison door.'),(1044,1078,'Prison doorway — sudden attack','Menestheus transforms and attacks as the party enters.'),(1079,1096,'Inside the prison','Door closes behind the party.')]:
 scene(d,a,b,loc,'1740-10-06','evening (session date; Feywild time uncertain)',boundary,basis='Manifest and session note date the continuing Feywild expedition; no tighter clock time is supported.')
d['excluded_ranges']=[{**sp(1,55),'reason':'Opening recap of earlier sessions, including previously heard prisoner speech.'},{**sp(1097,1128),'reason':'Closing scheduling and out-of-character discussion.'}]
ent(d,'aurae','Aurae','The party befriends the research assistant, learns about the prison and soul binding, names her Aurae, and takes her along in a backpack.','People/Other Nonhumans/Aurae.md')
ent(d,'menestheus','Menestheus','Menestheus accompanies the party while increasingly ill, denies expertise in soul binding, then transforms and grabs Txarro before being left outside the prison.','People/Other Humans/Menestheus.md')
ent(d,'prisoner','Central prisoner','The party debates the prisoner’s confinement and sees one figure at different ages through the door’s three windows before entering.',basis='One specific captive, explicitly represented across three windows; no unsupported identity assigned.')
ent(d,'endless-ending','Lord Endless Ending','The party considers Lord Endless Ending’s key and their agreement with him while deciding whether to enter the prisoner’s chamber.','People/Fey/Lord Endless Ending.md')
ent(d,'hulda','Lord Hulda','Ayveen recalls the party’s earlier work for Lord Hulda while questioning whom they should help.','People/Sembarans/Lord Hulda.md')
ent(d,'kallipseis','Dwarven gardener','The party recalls the gardener’s key advice and her association with the order while considering what lies beyond the library.','People/Dwarves/Kallipseis.md',basis='The previously encountered dwarven gardener/fungus lady is identified as Kallipseis by the session sources.',eligibility='named')
ent(d,'f6-order-visitor','Unnamed human visitor','Aurae recalls a recent human visitor who requested an order text and passed through the prisoner’s door.',basis='Specific human woman who last visited the assistant and entered the prison, u0327–u0353.')
ent(d,'f6-soul-author','Unnamed author of Soul Bindery','The party reads an order author’s argument for exploiting captive souls, uses it to interpret the prison, and burns the book.',basis='Specific author explicitly asked about at u0500–u0501; central to the interpretation of this prison, not merely a bibliography name.')
r=rec(d,'aurae',156,932,'The party questions the assistant about the prison, souls, and escape, names her Aurae, and rigs a backpack so she can accompany them.','interacted','star',[(156,175),(325,338),(475,505),(819,840),(912,932)])
quote(d,r,829,text="I know that I'm not happy, alone by myself. I've read all of these books already.")
r['introduction']={**sp(175),'kind':'description','quote':"an automaton that's sort of made out of clockwork and painted porcelain."}
rec(d,'aurae',947,1096,'Aurae accompanies the party in Edric’s backpack as they cross the library and escape through the prison door.','present','cameo',[(1064,1081)],presence_basis='u0925–u0932 establishes the backpack; u1064–u1081 explicitly confirms Edric is carrying Aurae through the door. No new speech or action by her is described; this transit record includes the brief attack and door crossing.')
r=rec(d,'menestheus',149,932,'The increasingly ill Menestheus accompanies the library discussion and tells Edric that soul binding is outside his expertise.',ex=[(149,152),(589,611)])
quote(d,r,602,604,text="Listen… A lot of wizards did a lot of weird shit, right? You saw the fungus, lady. That's not my department.")
rec(d,'menestheus',1038,1081,'Menestheus transforms and seizes Txarro, who escapes in anole form while the party leaves Menestheus outside.','interacted','star',[(1044,1061),(1079,1081)])
rec(d,'prisoner',187,810,'The party and Aurae discuss the prisoner’s confinement, the key, and the possibility of a soul-powered prison.','mentioned','star',[(187,236),(461,501),(758,773)])
rec(d,'prisoner',973,1043,'Through three windows, the party observes the same captive as a child, a young adult, and an aged figure.','observed','supporting',[(973,1007)])
rec(d,'endless-ending',187,810,'The party weighs Lord Endless Ending’s instructions and the key against the dangers of entering the prison.','mentioned','supporting',[(190,236),(461,470),(758,773)])
rec(d,'hulda',115,120,'Ayveen reflects on the party’s earlier attempt to help Lord Hulda and its changed loyalties.','mentioned','cameo')
rec(d,'kallipseis',187,611,'The party recalls the gardener’s advice about the key and questions Menestheus about the order’s disturbing practices.','mentioned','cameo',[(196,198),(602,611)],known_as='dwarven gardener / fungus lady')
rec(d,'f6-order-visitor',295,353,'Aurae describes the human woman who requested an order text and then entered the prisoner’s chamber.','mentioned','supporting',[(325,353)])
r=rec(d,'f6-soul-author',475,810,'The party studies the author’s proposed exploitation of captive souls and then burns the book in disgust.','mentioned','supporting',[(481,501),(799,810)])
quote(d,r,488,text='one can drink from a stream, but the wise man builds a water wheel and binds the force of moving water to use.',kind='written',attribution='The DM explicitly introduces this as a passage written by the author of On the Science and Possibilities of Soul Bindery.')
d['review_notes']=[
 'Selected for its sustained library dialogue: three narrative beats become five source-bounded scenes, with Aurae’s entire conversation retained as one interaction.',
 'One overview per NPC; Aurae’s idle presence after recruitment is separate from the completed conversation. Menestheus’s direct reply takes precedence over idle presence during the same library encounter.',
 'The captive’s three apparent ages represent one individual. The unnamed recent visitor and central book author qualify as distinct consequential individuals; generic story characters and bibliographic name drops do not.',
 'Exclude current-campaign PCs including Tarek, who is carried along despite the absent player. Kallipseis is mentioned, not newly met. The opening recap and prisoner monologue are not new-session interactions.',
 'Ashara Ven’s book attribution is explicitly retracted at u0966–u0969. Marcion, Eucostus and Yendela are incidental bibliographic references, not developed NPC interactions here. Lord Hulda’s later mistaken identification with Lord Endless Ending is corrected, not indexed as a second interaction.',
 'Written words by the Soul Bindery author are labeled written, not spoken dialogue; Aurae and Menestheus quotes are direct NPC speech.'
]
finish(d)

# Mawar 2: many independent interviews plus two genuine visits to the same smith.
d=base('mawar','mawar-adventures-002','mawar','Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 02.md')
parts=[
 (1,505,'Leviathan Inn','1747-08-03','evening','Opening scroll discussion before the overnight rest.'),
 (506,697,'North Cliffs — ruined tower grounds and roof','1747-08-04','morning','Next morning at the tower; party investigates exterior and roof.'),
 (698,791,'Ruined tower — interior','1747-08-04','morning','Entry into the tower; descent follows.'),
 (792,960,'Ruined tower — flooded basement and sea cave','1747-08-04','morning','Descent into the water illusion; party regroups after escaping it.'),
 (961,993,'Routes back toward Hamri','1747-08-04','morning','Party splits to question informants.'),
 (994,1101,'North Cliffs — Jaeson’s hut','1747-08-04','morning','Ryu and Trok arrive to question Jaeson.'),
 (1102,1197,'Drowned Flats — Samar’s shack','1747-08-04','morning','Cut to Wazir and Kaleho visiting Samar.'),
 (1198,1318,'Beach huts north of the Drowned Flats — Orden','1747-08-04','morning','Ryu and Trok question Orden; closing clarification follows.'),
 (1319,1383,'Drowned Flats — collapsed lodging','1747-08-04','late morning','Wazir and Kaleho inspect the collapsed building.'),
 (1384,1714,'Hamri fish market','1747-08-04','just past lunch','Party reunites, interviews Benat, and chooses afternoon leads.'),
 (1715,1817,'Shark’s Dock — Ovina’s smithy','1747-08-04','afternoon','Kaleho and Trok visit the smith.'),
 (1818,1876,'Glitter Cliff — Sulfi’s entrance','1747-08-04','afternoon','Cut to Wazir and Ryu speaking with the servant.'),
 (1877,1891,'Route from Glitter Cliff to Shark’s Dock','1747-08-04','late afternoon, around 5 PM','Return toward the other party members.'),
 (1892,2043,'Shark’s Dock — party rendezvous','1747-08-04','late afternoon','Party compares clues before splitting again.'),
 (2044,2058,'Ovina’s smithy — return visit','1747-08-04','late afternoon','Wazir returns to examine the ring and lead box.'),
 (2059,2103,'Outside Ovina’s smithy','1747-08-04','late afternoon','The same examination continues outside the shop.'),
 (2104,2129,'Yaz’s tower — entrance and ascent','1747-08-04','evening','Ryu and Trok arrive and climb up.'),
 (2130,2147,'Yaz’s tower — roof','1747-08-04','sunset','Arrival on the roof and greetings.'),
 (2148,2282,'Yaz’s tower — roof after the sunset watch','1747-08-04','evening','A quiet wait for sunset precedes the conversation; same visit.'),
 (2283,2419,'Leviathan Inn','1747-08-04','after dark','Party regroups to plan the next morning’s approach.'),
 (2420,2490,'Shark’s Dock — concealed lookout positions','1747-08-05','dawn','Next morning; party takes positions and scouts.'),
 (2491,2533,'Outside Ovina’s smithy','1747-08-05','early morning','Azar arrives, collects the box, and is approached.'),
 (2534,2659,'Route from the smithy toward Shark’s Dock','1747-08-05','early morning','Conversation continues as Azar heads for the dock.'),
 (2660,3444,'Shark’s Dock and the water beside the phantom boat','1747-08-05','early morning','Weapons come out; one continuous moving dockside fight.'),
 (3445,3494,'Shark’s Dock — aftermath','1747-08-05','after the fight','Healing, restraint, and a narrated interrogation.'),
 (3495,3497,'Azar’s lair in the Splinters','1747-08-05','later; exact time not transcribed','Narrated fast-forward to recovering and containing the knife.')]
for args in parts:scene(d,*args)
d['excluded_ranges']=[{**sp(3498,3597),'reason':'Hypothetical knife outcomes, game debrief, and closing conversation rather than further played encounters.'}]
people=[
 ('azar','Azar the Lost','The party traces Azar through witnesses, confronts him over Nadine and the murders, defeats and binds him, and learns how the knife exploited his hope of restoring his family.','People/Mawarans/Azar the Lost.md'),
 ('jaeson','Jaeson','Ryu and Trok trade fish for Jaeson’s account of the tower occupant, his gatza use, and his suspicious cleanup.','People/Mawarans/Jaeson.md'),
 ('samar','Samar','Samar tells Wazir and Kaleho about deaths in a collapsed lodging and the old man seeking a discreet smith; they warn her to take care.','People/Mawarans/Samar.md'),
 ('reliah','Reliah','Reliah is mentioned while the party plans and conducts its visit to Samar; the transcript does not clearly establish that Reliah is there.','People/Mawarans/Reliah.md'),
 ('orden','Orden','Orden describes a strange boat crossing the shoals toward Shark’s Dock and agrees to keep watching for the party.','People/Mawarans/Orden.md'),
 ('benat','Benat','Benat trades stories about Airion and the tower’s water magic for Trok’s promise to write to his family.','People/Lizardfolk/Benat.md'),
 ('ovina','Ovina','Ovina reveals the old man’s lead-box commission, lets the party inspect the dismantled ring and box on a return visit, and opens early for his collection.','People/Dwarves/Ovina.md'),
 ('yaz','Yaz','Ryu and Trok visit Yaz, who shares ocean-watcher lore and his fascination with the living ocean.','People/Mawarans/Yaz.md'),
 ('sulfi','Sulfi Mahadra','Sulfi declines an immediate audience, sends information about ships through her servant, and invites Wazir to tea eight days later.','People/Mawarans/Sulfi Mahadra.md'),
 ('nadine','Nadine','Nadine’s death and Azar’s hope of bringing her back emerge from the scroll, the dockside confrontation, and his account after capture.','People/Mawarans/Nadine.md'),
 ('gazankoa','Gazankoa','The party connects Gazankoa to the scroll and Azar’s belief that killing people with the knife will restore his family.','People/Extraplanar Powers/Gazankoa.md'),
 ('airion','Airion','The party follows the scroll’s references to Airion, investigates his ruined tower, and questions Benat and Yaz about his water magic.','People/Other Humans/Airion.md'),
 ('nimessa','Nimessa','The party discusses the marid Nimessa’s summoning and the ring while interpreting the scroll and planning how to handle its author.','People/Other Nonhumans/Nimessa.md')]
for args in people:ent(d,*args)
ent(d,'m2-blue','Blue (Ryu’s companion)','Ryu keeps Blue nearby during the investigation, brings Blue to Yaz, and uses Blue to scout and watch the harbor before the confrontation.',basis='Ryu repeatedly names this specific companion; not the unrelated Silver Tempests PC named Blue.',eligibility='named')
ent(d,'m2-market-woman','Older market storyteller','An older woman who keeps order among the market storytellers directs the party to Benat and Yaz.',basis='A specific older woman takes charge and answers the party’s question at u1403–u1409.')
ent(d,'m2-servant','Sulfi’s servant','Sulfi’s servant carries the party’s inquiry inside and returns with her answer; no personal name is recorded.',basis='One specific intermediary conducts a sustained exchange and is asked for a name at u1861–u1872.')
ent(d,'m2-bystander','Dockside lightning victim','The party witnesses Azar’s lightning kill a bystander during the dockside fight.',basis='One specific towns-person killed on screen at u3314–u3324; the session note identifies the victim as a woman, but no name is supplied.')
# The opening scroll conversation is one unit for each of its consequential subjects.
for who,summary,ev in [
 ('azar','The party studies the unnamed scroll author’s experiments and search for a way to restore his wife.',[(27,43),(83,115)]),
 ('nadine','The scroll introduces Nadine as the author’s dead wife and motive for his experiments.',[(27,43)]),
 ('gazankoa','The party connects Gazankoa to the scroll author’s experiments and promised resurrection.',[(27,43),(255,270)]),
 ('airion','The party discusses Airion’s elemental magic and the scroll author’s pursuit of his work.',[(92,115),(195,210)]),
 ('nimessa','The party discusses the scroll’s account of summoning Nimessa through a ring.',[(215,230)])]:
 rec(d,who,1,505,summary,'mentioned','supporting',ev,**({'known_as':'unnamed scroll author'} if who=='azar' else {}))
rec(d,'airion',506,960,'Investigating the ruined tower, the party considers its older magical foundations and connection to Airion.','mentioned','supporting',[(575,598),(800,832)])
rec(d,'azar',506,960,'The party searches the recent occupant’s abandoned tower and finds signs of a hurried attempt to conceal his stay.','mentioned','supporting',[(565,575),(643,665)],known_as='recent tower occupant')
rec(d,'m2-blue',666,674,'Ryu calms Blue when Wazir releases a small mechanical scout.','interacted','cameo')
rec(d,'m2-blue',833,845,'Blue remains outside under Ryu’s watch while the others explore the dangerous water illusion.','present','cameo',presence_basis='u0839 explicitly says Ryu is keeping Blue from entering and watching above.')
rec(d,'reliah',961,993,'The party chooses Samar and Reliah among the informants to question.','mentioned','cameo',[(965,980)])
r=rec(d,'jaeson',994,1101,'Ryu and Trok question Jaeson about the tower occupant and promise fish in exchange for his information.',ex=[(998,1020),(1085,1101)])
quote(d,r,1091,1092,attribution='Jaeson responds to Ryu’s question about the occupant picking up his trash; the source retains its disfluencies.')
rec(d,'azar',994,1101,'Jaeson describes an older tower occupant who smoked gatza and later cleared away his refuse.','mentioned','supporting',[(1050,1092)],known_as='old man at the tower')
r=rec(d,'samar',1102,1197,'Wazir and Kaleho ask Samar about the collapsed lodging and old man seeking a discreet smith, then warn her to be careful.',ex=[(1111,1146),(1170,1189)])
quote(d,r,1146,text='Who knows anybody down here.')
rec(d,'reliah',1102,1197,'Samar’s sister is referred to during the visit, without a clear on-screen appearance.','mentioned','cameo',[(1178,1189)])
rec(d,'azar',1102,1197,'Samar reports that an old man asked about a smith shortly before the lodging collapsed.','mentioned','supporting',[(1150,1180)],known_as='old man seeking a smith')
r=rec(d,'orden',1198,1318,'Ryu and Trok question Orden about the phantom boat and enlist him to keep watching.',ex=[(1205,1246),(1275,1293)])
quote(d,r,1246,text="don't laugh I i'm not actually sure it was real.")
rec(d,'m2-blue',1289,1293,'Ryu addresses Blue while concluding the conversation with Orden.','interacted','cameo')
r=rec(d,'m2-market-woman',1392,1410,'The party asks for tower stories, and an older woman directs them to Benat or Yaz.','interacted','cameo',[(1403,1409)])
rec(d,'yaz',1392,1714,'The party hears Yaz recommended as the oldest living ocean watcher and plans to visit him.','mentioned','cameo',[(1403,1409),(1613,1615)])
r=rec(d,'benat',1411,1587,'Benat asks Trok to write to his family in exchange for stories about Airion and the tower’s unusual water magic.','interacted','star',[(1438,1442),(1450,1479),(1533,1560)])
quote(d,r,1439,1442)
rec(d,'airion',1411,1587,'Benat explains Airion’s association with the tower and its ability to draw water from other places.','mentioned','supporting',[(1450,1479),(1533,1560)])
rec(d,'ovina',1588,1714,'The party identifies Ovina as a smith who might handle a discreet lead-box commission.','mentioned','supporting',[(1598,1612)])
rec(d,'sulfi',1588,1714,'The party decides Sulfi might know about the phantom boat and plans to seek her out.','mentioned','cameo',[(1617,1630),(1694,1711)])
r=rec(d,'ovina',1715,1817,'Kaleho and Trok persuade Ovina to reveal the old man’s lead-box commission and unusual payment.','interacted','star',[(1737,1747),(1755,1805)])
quote(d,r,1742)
rec(d,'azar',1715,1817,'Ovina describes the old man who paid a valuable ring for a sealed lead-lined box to quiet his troubles.','mentioned','supporting',[(1755,1805)],known_as='Ovina’s old customer')
r=rec(d,'m2-servant',1818,1876,'The servant carries the inquiry to Sulfi and returns her response about boats, harbor dues, and a future tea invitation for Wazir.',ex=[(1824,1835),(1846,1876)])
quote(d,r,1872,text='I am a simple servant, sir.')
rec(d,'sulfi',1818,1876,'Through her servant, Sulfi declines an immediate meeting, asks for strange ships to be reported, and invites Wazir to tea eight days later.','mentioned','supporting',[(1846,1856)])
rec(d,'azar',1892,2043,'The reunited party compares evidence about the old man, the lead box, and the knife before choosing its next steps.','mentioned','supporting',[(1940,1980)],known_as='old man / scroll author')
rec(d,'gazankoa',1892,2043,'The party identifies Gazankoa as the likely power behind the knife and the true danger driving the murders.','mentioned','star',[(1991,2007)])
rec(d,'nadine',1892,2043,'The party connects the suspected murders to the scroll author’s attempt to restore his dead wife.','mentioned','cameo',[(1952,1965)])
rec(d,'airion',1892,2043,'Wazir suspects the ring traded to Ovina is Airion’s and proposes testing it for magic.','mentioned','cameo',[(1972,1984)])
rec(d,'ovina',1892,2043,'The party plans a return visit to Ovina to test the ring’s remaining magic.','mentioned','supporting',[(1975,1984),(2014,2031)])
rec(d,'yaz',1892,2043,'Ryu chooses to visit Yaz while the others return to Ovina.','mentioned','cameo',[(2032,2043)])
rec(d,'nimessa',1892,2043,'The party revisits Nimessa and the summoning ring while comparing its clues.','mentioned','cameo',[(1950,1990)])
r=rec(d,'ovina',2044,2103,'On a return visit, Ovina lets Wazir test the dismantled ring and lead-lined box for magic.','interacted','supporting',[(2046,2065),(2080,2103)])
r=rec(d,'yaz',2104,2282,'Ryu and Trok visit Yaz, watch the sunset, and discuss the ancient tower, missing people, and the living ocean.','interacted','star',[(2130,2155),(2189,2206),(2220,2245)])
quote(d,r,2238,text='what does that even mean living ocean, the Ocean is already alive.')
rec(d,'m2-blue',2134,2155,'Blue greets Yaz, then Ryu lets Blue play in the water.','interacted','cameo')
rec(d,'airion',2104,2282,'Yaz recounts the old tower’s water lore during the party’s visit.','mentioned','supporting',[(2215,2238)])
rec(d,'azar',2104,2282,'Ryu and Trok discuss the suspected killer and the tower during their visit to Yaz.','mentioned','cameo',[(2195,2206)],known_as='suspected old man')
rec(d,'azar',2283,2419,'The party plans a cautious approach to the old man when he collects the box, with others hidden nearby.','mentioned','supporting',[(2290,2315),(2358,2375),(2405,2419)],known_as='old man / scroll author')
rec(d,'m2-blue',2283,2419,'The party considers having Blue follow the old man if the conversation fails.','mentioned','cameo',[(2393,2415)])
rec(d,'m2-blue',2439,2483,'Ryu uses Blue to scout the harbor and keep watch as the party takes its positions.',ex=[(2439,2447),(2481,2483)])
rec(d,'ovina',2491,2505,'Ovina is at the smithy, opened early for the planned collection, while the party watches Azar arrive.','present','cameo',presence_basis='u2494 explicitly establishes Ovina opening early, aware of the party waiting; Azar enters and returns with the box at u2504–u2505.')
r=rec(d,'azar',2491,2659,'Ryu confronts the old man, Wazir invokes Nadine’s name, and Azar identifies himself while insisting he can still save his family.','interacted','star',[(2491,2515),(2550,2565),(2602,2622),(2640,2659)],known_as='old man; names himself Azar at u2602')
quote(d,r,2613,2615)
r['introduction']={**sp(2492),'kind':'description','quote':'This sort of older man like hunched over with like this pile of cloaks over his shoulders'}
rec(d,'nadine',2491,2659,'The party invokes Nadine’s name, prompting Azar to confirm she is his wife and insist he is saving his family.','mentioned','supporting',[(2550,2565),(2602,2615)])
rec(d,'gazankoa',2491,2659,'Azar insists Gazankoa is helping him restore the dead while the party tries to persuade him to talk.','mentioned','supporting',[(2602,2619)])
rec(d,'azar',2660,3444,'Azar attacks, flees toward his boat, and is defeated after a fight involving tentacles, cold armor, and lethal lightning.','interacted','star',[(2744,2770),(3313,3334),(3390,3415)])
rec(d,'m2-blue',2998,3004,'Ryu brings Blue into the combat turn discussion; the transcript does not clearly resolve the subsequent familiar action.','present','cameo',presence_basis='u2998–u3002 explicitly discusses Blue taking a turn in the ongoing encounter; later ASR renders another name, so no specific action is asserted.')
rec(d,'m2-bystander',3313,3334,'The party witnesses Azar’s lightning kill a dockside bystander.','observed','supporting',[(3313,3324)])
rec(d,'azar',3445,3494,'The party heals and binds Azar, then hears a narrated account of how the knife’s promises led him to murder.','interacted','star',[(3445,3465),(3477,3494)])
rec(d,'nadine',3445,3494,'Azar’s account explains how grief for his wife drove his hope that the killings would bring her back.','mentioned','supporting',[(3488,3494)])
rec(d,'gazankoa',3445,3494,'The party learns that the knife’s patron falsely promised Azar his wife’s return if he killed people correctly.','mentioned','supporting',[(3488,3494)])
d['review_notes']=[
 'Transcript-backed scope: August 3 evening through the August 5 aftermath and brief lair fast-forward. The fuller session note additionally describes Sefa, restitution, August 6 identification, and August 9 departure with Benat; these are outside the recorded interaction coverage and are not assigned invented transcript links.',
 'Reliah is mentioned, not asserted present: the recap says both sisters were involved, but the actual exchange clearly gives Samar the dialogue. Sulfi answers through a servant and is also mentioned, not present.',
 'One visit to Yaz remains one interaction across arrival, the roof, a sunset pause, and conversation. Ovina has two genuine separate visits plus dawn presence; the afternoon return is not merged across the intervening party split.',
 'Blue is Ryu’s named companion, not the Silver Tempests PC of the same name. Later combat ASR shifts between Blue, chirk and Turkey; retain explicit presence without claiming that a specific later boat-moving action belongs to Blue.',
 'Keep the distinct servant, market woman and lightning victim because each has a specific consequential role. Exclude generic drowned combatants, crowds, unnamed mass victims, and the hypothetical future guest-PC introduction. No individual record for every monster or rumor.',
 'Pull quotes are exact contiguous source text, including awkward ASR. No quote is forced for nonspeaking Blue, the lightning victim, or characters only discussed. Jaeson’s question, Samar’s reply, Benat’s family appeal, Ovina’s reputation, the servant’s refusal, Yaz’s ocean observation, and Azar’s hope are selected.',
 'All scenes retain source boundaries even when they have no eligible NPC interaction. Minor PC interjections and mechanical discussion remain within whole conversation ranges.'
]
finish(d)

# Dunmari 108: high-beat, all-core-PC conversational stress case.
d=base('dunmar-frontier','dunmari-frontier-108','dufr','Campaigns/Dunmari Frontier Campaign/Session Notes/Session 108 (DuFr).md')
for a,b,loc,time,boundary in [
 (1,530,'Wanderer statue complex','afternoon, about 2 PM','Opening survey and planning at the statue.'),
 (531,562,'Route from the pilgrim hostel toward a ruined manor','afternoon','Party leaves the statue complex.'),
 (563,848,'Ruined manor grounds — approach to the dragonets','afternoon','Arrival at the grounds; scouting and approach.'),
 (849,1706,'Ruined manor tower — dice game','afternoon','Kenzo approaches the dragonets and begins bargaining.'),
 (1707,2217,'Route to Megren’s tower','late afternoon','Guided journey, with party coordination and a race along the way.'),
 (2218,2688,'Megren’s tower and grounds','late afternoon','Arrival and a sustained conversation with Megren.'),
 (2689,3099,'Rendezvous outside the dragonet settlement','late afternoon','Kenzo reunites with the party and they compare plans.'),
 (3100,3132,'Open terrain approaching the forest','early evening','Travel across open ground under concealment.'),
 (3133,3401,'Memorial forest — pilgrim road','around 7 PM into sunset','Party enters the forest and senses the elder’s location.'),
 (3402,3448,'Pilgrim road beside the first memory pool','around 8 PM','An hour’s progress along the road brings the party to the pool.'),
 (3449,3521,'First memory pool — viewing area','around 8 PM','Kenzo steps off the road to inspect the water.'),
 (3522,3555,'Pilgrim road — approaching a second pool','evening','Party resumes walking to a position within divination range.'),
 (3556,3998,'Pilgrim road — rest and divination stop','roughly 8–9 PM','Party stops to scout, send a message, scry and rest; the source clarifies the scry retroactively.'),
 (3999,4008,'Spiral-road junction — memorial approach','after the rest, about half an hour later','Walk to the memorial at the mountain road junction.'),
 (4009,4563,'Elven memorial at the spiral-road junction','night','Delwath touches the memorial; Kenzo communes with the forest and Seeker investigates.'),
 (4564,4686,'Summit courtyard — Temple of the Sibyl entrance','about 10:30 PM','Arrival at the summit and disarming the entrance trap.'),
 (4687,5644,'Temple of the Sibyl — interior','late night','Party enters and holds one sustained exchange with the elder.')]:
 scene(d,a,b,loc,'1749-05-18',time,boundary,basis='May 18 from the session timeline; transcript gives about 2 PM at u0504, 7 PM at u3147, 8 PM at u3423, and about 10:30 PM at u4566–u4568. Intermediate times are relative, not exact.')
d['excluded_ranges']=[{**sp(5645,5690),'reason':'Closing break arrangements and next-session planning; the proposed long rest is not played on screen.'}]
for args in [
 ('ghesh','Ghesh','Kenzo gambles with Ghesh, buys his discretion and guidance, races him on the way to Megren, and pays him after the introduction.','People/Other Nonhumans/Ghesh.md'),
 ('megren','Megren','Megren tells Kenzo she traded the jade fragment to Ra’ghemdros, describes the dragon’s dangerous lair, and passes on rumors of an elder despite fearing reprisals.','People/Other Nonhumans/Megren.md'),
 ('raghemdros',"Ra'ghemdros",'The party learns that Ra’ghemdros holds the jade, rules the dragonets through fear and rewards, and is Cha’mutte’s daughter, then debates negotiation, theft, or fighting her.',"People/Other Nonhumans/Ra'ghemdros.md"),
 ('dimitaur','Dimitaur','After hearing rumors, locating and scrying the elder, the party bypasses Dimitaur’s trap and earns a conversation about Rai, Ra’ghemdros, Drankor, and Apollyon.','People/PCs/Great War/Companions/Dimitaur.md'),
 ('rai','Rai','The party uses its connection to Rai to seek the elder’s help and learns from Dimitaur about Rai’s disappearance and failed attempt to heal the land.','People/PCs/Great War/Rai.md'),
 ('chamutte',"Cha'mutte",'The party connects Cha’mutte to the plague and learns from Dimitaur that Ra’ghemdros is his daughter and may still carry out an assigned task.',"People/Extraplanar Powers/Cha'mutte.md"),
 ('apollyon','Apollyon','Apollyon’s impending escape drives the party’s search for the jade, questions for Dimitaur, and debate over the guarded forge and possible alliances.','People/Historical Figures/Drankorian Emperors/Apollyon.md'),
 ('revaka','Hobgoblin wizard in the mirror','During the Dimitaur conversation, the party considers consulting the imprisoned hobgoblin wizard as a potential ally against Cha’mutte’s daughter.','People/Other Nonhumans/Revaka.md')]:ent(d,*args)
ent(d,'d108-zadar','Zadar','Megren cites Zadar’s account of an acid pool associated with dragonets who supposedly sought the rumored elder.',basis='Named individual and specific source of Megren’s hearsay, u2516–u2627; not met by the party.',eligibility='named')
ent(d,'d108-forest','Memorial forest','Kenzo communes with the forest about its memorials, isolation, and lost pilgrims, then honors its memories in his staff.',basis='The DM explicitly establishes one collective consciousness at u4278–u4282 and u4422–u4425, speaking through the tree; keep one distinct entity, not one record per tree.')
ent(d,'d108-quartermaster','Elven quartermaster remembered in the memorial','Delwath sees a dead elf’s life as a quartermaster and their death in battle through the memorial.',basis='A specific individual’s memories are selected by the memorial at u4031–u4075; the written name is not transcribed.')
rec(d,'apollyon',447,530,'The party checks the time remaining before Apollyon wakes while deciding how to explore the island.','mentioned','cameo',[(499,505)])
r=rec(d,'ghesh',849,2688,'Kenzo gambles with Ghesh, bargains for secrecy and an introduction, travels with him to Megren, and pays the agreed reward.','interacted','star',[(1121,1180),(1527,1540),(1975,2010),(2194,2210),(2657,2666)])
r['continuity']='One continuous visit with Ghesh: the dice bargain becomes a guided journey and introduction, ending with payment. Topic changes, party coordination, the race and Megren’s intervening dialogue remain within the encounter.'
quote(d,r,1180,text="I'm always happy to play dice with people who seemingly don't know the rules.")
rec(d,'megren',1298,1706,'Ghesh tells Kenzo that Megren brought back valuable treasure and offers to introduce them.','mentioned','supporting',[(1299,1311),(1527,1540)])
rec(d,'raghemdros',849,2217,'Ghesh describes Ra’ghemdros’s control over the dragonets and the rewards and dangers of serving her.','mentioned','star',[(1206,1240),(1877,1940),(2194,2210)])
rec(d,'raghemdros',2247,2688,'Megren describes giving Ra’ghemdros the jade, the acidic lair, and a reported reprisal against dissenters.','mentioned','star',[(2340,2376),(2432,2467),(2535,2573)])
rec(d,'chamutte',1458,1468,'The party connects the haunted red-mist dreams to Cha’mutte’s plague.','mentioned','supporting')
rec(d,'apollyon',1458,1468,'The party speculates that Cha’mutte unleashed the plague partly to end Apollyon.','mentioned','cameo')
r=rec(d,'megren',2247,2688,'Kenzo questions Megren about the jade, Ra’ghemdros, and the rumored elder, then leaves her with a carved likeness.','interacted','star',[(2247,2265),(2340,2376),(2432,2467),(2535,2638),(2664,2688)])
quote(d,r,2605,2606,text="But if you want to take a risk, you can take risks. I don't want to be turned into a pool of acid.")
rec(d,'d108-zadar',2247,2688,'Megren cites Zadar’s account of an acid pool as evidence behind the story of dragonets punished for seeking the elder.','mentioned','supporting',[(2516,2520),(2535,2573),(2616,2627)])
rec(d,'dimitaur',2247,2688,'Megren passes on a dangerous rumor of an elder living with the elves, while doubting the elder actually exists.','mentioned','supporting',[(2535,2638)],known_as='rumored elder; identification as Dimitaur is only confirmed later')
rec(d,'raghemdros',2689,3099,'The reunited party debates stealing, trading for, or fighting Ra’ghemdros for the jade.','mentioned','star',[(2692,2724),(2890,2934)])
rec(d,'ghesh',2689,3099,'The party considers using Ghesh as an intermediary in a possible trade with the dragon.','mentioned','cameo',[(2713,2720)])
rec(d,'megren',2689,3099,'Kenzo’s report establishes that Megren handed the jade to the dragon and informs the party’s plans.','mentioned','supporting',[(2692,2704)])
rec(d,'dimitaur',3171,3401,'The party connects the rumored elder to Kenzo’s earlier vision, and Kenzo senses an elder dragonet at the summit monastery.','observed','supporting',[(3180,3184),(3220,3259),(3320,3338)],known_as='elder dragonet; possible Dimitaur')
rec(d,'rai',3171,3401,'The party recalls Kenzo’s dream of Rai and an elderly dragonet while deciding how to locate the rumored elder.','mentioned','supporting',[(3220,3268)])
rec(d,'dimitaur',3659,3830,'Delwath sends the elder a request for an audience; the spirit messenger finds him but returns without a reply.','interacted','supporting',[(3665,3720),(3798,3819)],known_as='elder dragonet')
r=rec(d,'dimitaur',3843,3998,'Delwath scries the elderly dragonet preparing a stone trap inside the Temple of the Sibyl and ignoring the messenger.','observed','supporting',[(3864,3899),(3902,3927),(3953,3984)],known_as='elder dragonet; possible Dimitaur')
r['continuity']='The source explains this scry after describing the completed rest, then explicitly places it earlier during the same rest. This is a separate remote observation, not a new conversational exchange.'
rec(d,'rai',3659,3998,'The party invokes Rai’s mission in its message to the elder while seeking help recovering the jade.','mentioned','supporting',[(3665,3712)])
rec(d,'raghemdros',3659,3998,'The party names Ra’ghemdros as the holder of Rai’s jade in the message requesting the elder’s help.','mentioned','cameo',[(3680,3697)])
rec(d,'d108-quartermaster',4009,4093,'Touching the memorial, Delwath witnesses an elf’s quartermaster work and death defending a battlement.','observed','supporting',[(4031,4047),(4058,4075)])
r=rec(d,'d108-forest',4094,4442,'Kenzo communes with the forest about its lost pilgrims and memories, and asks for an image to preserve in his staff.','interacted','star',[(4128,4145),(4227,4248),(4325,4348),(4365,4399),(4419,4442)])
quote(d,r,4332,4334)
rec(d,'apollyon',4443,4563,'The party discusses whether the island’s origins and divine magic explain Apollyon’s interest, then investigates its structure.','mentioned','supporting',[(4455,4465)])
r=rec(d,'dimitaur',4687,5644,'After bypassing his trap, the party earns Dimitaur’s trust and questions him about Rai, the jade, the dragon, Drankor, and Apollyon.','interacted','star',[(4724,4755),(4842,4896),(4955,5018),(5060,5103),(5335,5350),(5639,5644)],known_as='elder dragonet; names himself Dimitaur at u5068')
quote(d,r,5103,text='The important thing is to just not keep the plans you make.')
r['introduction']={**sp(4882,4883),'kind':'description','quote':"Um, and he's walking slowly. He's carrying like a short staff in one hand and a wand in the other that he's still kind of pointing at you."}
r['continuity']='One temple conversation continues through jokes, thought-reading, gifts, tactical asides and many subject changes. It ends when the party proposes further discussion and a long rest.'
rec(d,'rai',4687,5644,'Dimitaur recounts Rai’s disappearance after trying to heal the land and suggests the party may still find him.','mentioned','star',[(4955,4986),(5194,5241),(5335,5416)])
rec(d,'raghemdros',4687,5644,'Dimitaur identifies Ra’ghemdros as Cha’mutte’s daughter and discusses her task, temper, and possible hostility toward Apollyon.','mentioned','star',[(5014,5054),(5087,5124),(5429,5485),(5553,5576)])
rec(d,'chamutte',4687,5644,'Dimitaur connects Cha’mutte to Ra’ghemdros’s lineage, the plague, and the conflict with Apollyon.','mentioned','supporting',[(5022,5035),(5244,5259),(5544,5568)])
rec(d,'apollyon',4687,5644,'The party warns Dimitaur about Apollyon’s imminent escape and seeks advice about his prison, phylactery, tower, and forge.','mentioned','star',[(4987,5018),(5152,5193),(5553,5576),(5598,5628)])
rec(d,'revaka',4687,5644,'During the conversation, the party considers consulting the imprisoned hobgoblin wizard against Ra’ghemdros.','mentioned','supporting',[(5272,5312),(5584,5593)],known_as='hobgoblin wizard in the mirror')
d['review_notes']=[
 'Selection: 21 narrative beats, fifth-highest raw count among 34 available Dunmari beat files (110:46, 109:33, 136:32, 139:23, 108:21). Chosen for sustained multi-NPC conversations rather than mostly combat or postgame discussion. All four core PCs are listed in the session note and speak in this transcript: Kenzo, Wellby, Delwath and Seeker.',
 'Seventeen scenes follow actual movement and rest boundaries. The 21 editorial beats are supporting evidence, not automatic interaction boundaries. Ghesh’s extended visit, Megren’s interview, the forest communion and Dimitaur’s temple conversation each stay together.',
 'Dimitaur’s card distinguishes rumor, remote detection, a delivered message, scrying, and the later direct meeting. Source order includes a retrospective clarification of the scry during the rest, not an additional hour or second rest.',
 'Name knowledge is explicit: the party guesses at the elder’s identity earlier, but his in-world introduction is u5068. Revaka is only discussed as the wizard in the mirror; she is not summoned or released in this recording.',
 'Zadar’s account is hearsay through Megren, not an encounter or confirmed observation of the alleged victims. Ra’ghemdros is mentioned throughout, never actually encountered. Do not use Dimitaur’s imitation of the dragon as a direct quote from her.',
 'The forest is one explicitly established speaking consciousness, retained as a distinctive entity. The selected dead quartermaster is one observed individual; exclude generic dragonet groups, the unintelligent messenger spirit, and crowds of dead souls.',
 'Exclude incidental deity iconography, loot-provenance names, the DM’s background-history reminders about Omnis Pura and Orestes, and current-campaign PCs including absent Riswynn. Rai and Dimitaur were PCs/companions in another campaign but are NPC subjects here.',
 'The session metadata ends May 19, but this transcript ends with plans for a long rest. Played interactions are dated May 18; no unseen morning encounter is invented.'
]
finish(d)

# Small entry point to the five NPC-card previews and their machine-readable data.
index=['# NPC interaction extraction trials — version 2','','[Extraction skill](/workspace/taelgar/.agents/skills/extract-campaign-interactions/SKILL.md) · [Format](/workspace/taelgar/.agents/skills/extract-campaign-interactions/references/format.md)','','Each NPC card has one session overview, an optional featured pull quote, and complete encounters linked to the frozen transcript. Scenes retain separate locations and dates; short evidence links help navigate long conversations. Original v1 pilots are preserved.','','| Session | Scenes | NPCs | Interactions | Quotes | Data |','| --- | ---: | ---: | ---: | ---: | --- |']
for sid,title in [('dunmari-frontier-008','Dunmari 8 — retest'),('dunmari-frontier-060','Dunmari 60 — retest'),('mawar-adventures-002','Mawar 2'),('lost-in-the-feywild-006','Lost in the Feywild 6'),('dunmari-frontier-108','Dunmari 108')]:
 p=OUT/sid;data=json.loads((p/'extraction.json').read_text())
 index.append(f'| [{title}]({p}/review.md) | {len(data["scenes"])} | {len(data["entities"])} | {len(data["interactions"])} | {sum(bool(r.get("pull_quote")) for r in data["interactions"])} | [JSON]({p}/extraction.json) · [Evidence]({p}/evidence.md) |')
index += ['','## What changed','','- Pull quotes have exact source ranges and contextual attribution, distinct from introduction descriptions. Select one featured quote per speaking NPC where a suitable line exists; absence is allowed. One written quote is explicitly labeled as such.', '- Exactly one session overview per NPC, grounded in all of its interaction records.', '- `present` captures affirmative idle presence, such as Baxter on deck and Aurae carried in a backpack. A cast entry, a mention, or an earlier location is insufficient.', '- `scenes` replaces the single `scene` on interactions. Full encounter bounds are separate from short evidence excerpts; topics, jokes, and minor interjections stay together. Makha’s seven old records become one guided visit, and Inakara’s negotiation and approach become one encounter across three scenes.', '- Dimitaur’s temple conversation remains one interaction through 958 source utterances, with short evidence links and one selected quote. His earlier rumor, remote observation, and message delivery remain distinct.', '', '## Selection and limits','', 'Dunmari 108 has 21 beats, fifth-highest among 34 available Dunmari beat files, and all four core PCs speak: Kenzo, Wellby, Delwath and Seeker. It provides several sustained conversations and party splits, rather than mainly combat rounds or postgame discussion.', '', 'Mawar 2’s note continues beyond the recorded session with Sefa, restitution, item identification and Azar’s later departure. This transcript-backed trial explicitly flags those unrecorded follow-ups. Reliah’s presence is not clear in the transcript despite the recap grouping her with Samar. ASR wording is preserved in quotes.', '', 'Dunmari 60 retains its previously recorded date uncertainty. Dunmari 108’s played interactions stay on May 18 even though session metadata extends to May 19. The planned overnight rest is not treated as a recorded morning encounter.', '', 'All five JSON files pass source hashes, source coverage, scene and entity joins, bounds, exact quote text, NPC overview coverage, and overlap checks. Twelve validator tests pass. Contextual review also checked quote speakers, presence and conversation boundaries; structural validation alone cannot settle those judgments.', '', 'Links use local transcript lines. The stored source hash and utterance ranges support a future web viewer; these files do not implement Taelgarverse runtime integration.']
(OUT/'README.md').write_text('\n'.join(index)+'\n')

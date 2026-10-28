"""Add reviewed item records, scene labels and extra NPC quotes to frozen v2 trials."""
from pathlib import Path
import json, hashlib, re, sys, copy
V=Path('/workspace/taelgar'); OUT=Path(__file__).parent; OLD=OUT.parent/'v2'
sys.path.insert(0,str(V/'.agents/skills/extract-campaign-interactions/scripts'))
from validate import validate, render

def uid(n):return f'u{n:04d}'
def sp(a,b=None):return {'startUid':uid(a),'endUid':uid(a if b is None else b)}
def frozen(p):return {'path':p,'sha256':hashlib.sha256((V/p).read_bytes()).hexdigest()}
def texts(d):
 return {m[1]:m[2] for line in (V/d['source']['path']).read_text().splitlines() if (m:=re.match(r'^\[(u\d+)(?:\s*\|.*?)?\]\s?(.*)$',line))}
TYPES={
 'dunmari-frontier-008':'conversation exploration travel exploration travel exploration exploration travel exploration travel exploration travel conversation travel conversation combat conversation',
 'dunmari-frontier-060':'travel conversation conversation exploration conversation travel combat travel exploration conversation conversation travel travel conversation travel conversation travel conversation travel conversation',
 'lost-in-the-feywild-006':'conversation travel exploration combat exploration',
 'mawar-adventures-002':'conversation exploration exploration exploration travel conversation conversation conversation exploration conversation conversation conversation travel conversation conversation exploration travel conversation conversation conversation exploration conversation conversation combat conversation exploration',
 'dunmari-frontier-108':'exploration travel exploration conversation travel conversation conversation travel exploration travel exploration travel exploration travel exploration exploration conversation'}

def base(sid):
 d=json.loads((OLD/sid/'extraction.json').read_text());d['schema_version']=3
 assert len(d['scenes'])==len(TYPES[sid].split())
 for scene,t in zip(d['scenes'],TYPES[sid].split()):scene['type']=t
 for e in d['entities']:
  e['kind']='npc';e['featured_quote_ids']=[]
  oldfeatured=e.pop('featured_quote_interaction',None)
  for r in d['interactions']:
   if r['npc']!=e['id']:continue
   if q:=r.pop('pull_quote',None):
    q['id']=r['id']+'-quote-1';r['quotes']=[q]
    if r['id']==oldfeatured:e['featured_quote_ids'].append(q['id'])
 for r in d['interactions']:r['entity']=r.pop('npc')
 d['review_notes'] += ['Version 3 adds important-item cards and one dominant type per scene; existing scene boundaries, indexes, dates and NPC encounter ranges are preserved. Extra NPC quotes stay inside the same conversations.']
 return d

def item(d,id,label,overview,basis,note=None):
 e={'id':id,'kind':'item','label':label,'canonical_name':Path(note).stem if note else None,'note':note,'eligibility':'named' if note else 'distinctive','basis':basis,'session_overview':overview,'overview_records':[],'quote_review':'no_suitable_excerpt','featured_quote_ids':[]}
 d['entities'].append(e)
 if note and not any(s['path']==note for s in d['supporting_sources']):d['supporting_sources'].append(frozen(note))
 return e

def rec(d,id,a,b,overview,kind='interacted',importance='supporting',ex=(),**kw):
 scenes=[s['index'] for s in d['scenes'] if int(s['startUid'][1:])<=b and int(s['endUid'][1:])>=a]
 r={'id':f'{id}-{a:04d}','entity':id,'scenes':scenes,'interaction':kind,'importance':importance,'overview':overview,'transcript':[sp(a,b)]}
 if ex:r['excerpts']=[sp(*x) if isinstance(x,tuple) else sp(x) for x in ex]
 if len(scenes)>1:r['continuity']='One continuous conversation, investigation or encounter across the listed scene boundaries; minor interjections and movement remain in the complete range.'
 r.update(kw);d['interactions'].append(r)
 return r

def quote(d,id,record_start,a,b=None,text=None,kind='dialogue',speaker=None,attribution=None):
 r=next(r for r in d['interactions'] if r['entity']==id and r['transcript'][0]['startUid']==uid(record_start))
 e=next(e for e in d['entities'] if e['id']==id)
 b=b or a; rr=texts(d);passage=' '.join(rr[uid(i)] for i in range(a,b+1))
 assert text is None or text in passage,(id,a,text,passage)
 q={**sp(a,b),'id':r['id']+f'-quote-{len(r.get("quotes",[]))+1}','kind':kind,'quote':text or passage,'speaker':id if e['kind']=='npc' else speaker,'attribution':attribution or 'The DM voices this NPC’s response in the surrounding conversation.'}
 r.setdefault('quotes',[]).append(q);e['featured_quote_ids'].append(q['id']);e['quote_review']='selected'
 return q

def finish(d):
 for e in d['entities']:
  e['overview_records']=[r['id'] for r in d['interactions'] if r['entity']==e['id']]
 p=OUT/d['session'];p.mkdir(exist_ok=True)
 rr,span=validate(d,V)
 old=json.loads((OLD/d['session']/'extraction.json').read_text())
 # Extension must not fragment any of the accepted NPC encounters or move scene boundaries.
 assert [(r['id'],r['scenes'],r['transcript']) for r in old['interactions']]==[(r['id'],r['scenes'],r['transcript']) for r in d['interactions'] if next(e for e in d['entities'] if e['id']==r['entity'])['kind']=='npc']
 assert [{k:v for k,v in s.items() if k!='type'} for s in d['scenes']]==old['scenes']
 (p/'extraction.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
 (p/'review.md').write_text(render(d,V,rr,span));(p/'evidence.md').write_text(render(d,V,rr,span,True))
 # Separate short views reuse the same shared scenes and source, not separate extraction identities.
 for kind in ('npc','item'):
  view=copy.deepcopy(d);view['entities']=[e for e in view['entities'] if e['kind']==kind];ids={e['id'] for e in view['entities']};view['interactions']=[r for r in view['interactions'] if r['entity'] in ids]
  (p/f'{kind}s.md').write_text(render(view,V,rr,span))
 print(d['session'],len(d['scenes']),'scenes',sum(e['kind']=='item' for e in d['entities']),'items',sum(len(r.get('quotes',[])) for r in d['interactions']),'quotes')

# Dunmari 8: navigation clues, not every lever and ordinary weapon.
d=base('dunmari-frontier-008')
item(d,'d8-maps',"Riswynn’s maps of Raven’s Hold and the dwarven outpost",'The party consults Riswynn’s maps to choose an approach, orient itself inside the outpost, and interpret the route onward after the fight.','The source explicitly asks Riswynn to get out the maps at u0237 and compares their features; treat this referenced pair as one navigation set.')
rec(d,'d8-maps',187,344,'The party compares the maps and considers the outpost’s connection to Raven’s Hold and the Long Road.','interacted','star',[(206,243),(264,275)])
rec(d,'d8-maps',1099,1280,'Inside the guard chamber, the party tries to locate itself on the incomplete sketch map.','interacted','supporting',[(1163,1176)])
rec(d,'d8-maps',1684,1848,'At the ruined marketplace, the party uses mapped landmarks to assess the surrounding passages.','interacted','supporting',[(1725,1736),(1775,1788)])
rec(d,'d8-maps',2808,2835,'After the fight, the party compares the ruler’s indicated route with the map.','interacted','cameo',[(2827,2835)])
quote(d,'inakara',1383,1514,1515,attribution='The cavern ruler makes passage conditional on the party’s help.')
d['review_notes'] += ['Item selection retains the consequential navigation maps; excludes ordinary weapons, armor, loose ball bearings and the outpost’s fixed mechanisms as inventory clutter.']
finish(d)

# Dunmari 60: meaningful equipment use and a newly drawn navigation aid.
d=base('dunmari-frontier-060')
item(d,'kenku-armor','Kenku Glamoured Armor','Wellby’s armor cushions his fall during the pirate attack; later Makha recognizes its kenku origin and identifies kidnapped Skoda as a possible source of help.','Explicit armor effects at u0362 and recognition at u1031–u1039; no repair or wing upgrade occurs in this session.','Campaigns/Dunmari Frontier Campaign/Treasure/Kenku Glamoured Armor.md')
rec(d,'kenku-armor',333,544,'Wellby’s armor lets him use Feather Fall when incoming fire interrupts his flight.','interacted','supporting',[(350,364)])
rec(d,'kenku-armor',981,1243,'Makha recognizes Wellby’s armor and discusses its lost wing capability and Skoda’s possible help.','interacted','star',[(1031,1047),(1155,1186)])
quote(d,'kenku-armor',981,1180,1182,kind='dialogue',speaker='makha',attribution='Makha describes an earlier capability of this kind of armor; no restoration is performed here.')
item(d,'raven-whistle','Raven Whistle','Wellby uses the Raven Whistle to fly during his attack on the pirates and later to follow Makha around Wahacha.','A proposed prior equipment swap is corrected at u0135–u0141; the subsequent transcript explicitly shows Wellby using the whistle.','Campaigns/Dunmari Frontier Campaign/Treasure/Raven Whistle.md')
rec(d,'raven-whistle',100,190,'Wellby confirms he still has the Raven Whistle and plans to use it to reach the pirates.','mentioned','supporting',[(135,153),(167,183)])
rec(d,'raven-whistle',290,550,'Wellby uses the whistle to reach the pirate ship, resumes flight after being hit, and returns after the sabotage.','interacted','star',[(295,320),(350,364),(535,550)])
rec(d,'raven-whistle',981,1243,'Wellby uses the Raven Whistle to follow Makha on the airborne portions of the tour.','interacted','supporting',[(1066,1079),(1187,1198)])
item(d,'flaming-bowstring','Flaming Bowstring','Wellby uses his fire-starting bowstring while setting the pursuing pirate ship’s sails alight.','Named at u0435; the following actions use pyrotechnic and burning strikes.','Campaigns/Dunmari Frontier Campaign/Treasure/Flaming Bowstring.md')
rec(d,'flaming-bowstring',100,190,'Wellby proposes setting the pursuers’ sails alight with his fire-starting bow.','mentioned','supporting',[(148,155)])
rec(d,'flaming-bowstring',333,544,'Wellby discusses the bowstring’s ignition effect and fires burning arrows into the pirate ship’s sails.','interacted','star',[(430,460),(473,491),(500,530)])
item(d,'d60-chart','Corrin’s sketch chart','Corrin draws and leaves a chart for Wellby while explaining the shifting Eastern Isles and their relation to familiar lands.','One specific chart drawn during the conversation at u0601–u0606 and left at u0692; not a generic map reference.')
rec(d,'d60-chart',580,697,'Corrin sketches a chart for Wellby, explains the moving islands, and leaves it for further discussion.','interacted','supporting',[(589,625),(683,697)])
quote(d,'d60-chart',580,593,594,kind='dialogue',speaker='corrin',attribution='Corrin warns Wellby about the limits of maps before sketching this chart.')
quote(d,'wella',23,133,attribution='The captain reassures Wellby while discussing how to outlast the pursuers.')
quote(d,'makha',981,1180,1182,attribution='Makha explains the heritage of the kenku armor that Wellby wears.')
d['review_notes'] += ['Items cover active quest-relevant equipment and Corrin’s chart. The armor is not described as repaired or already upgraded; later canonical item powers do not supply session events. Ships serving as scene locations and routine cargo do not receive inventory cards here.']
finish(d)

# Lost in the Feywild 6: key and two consequential texts.
d=base('lost-in-the-feywild-006')
item(d,'f6-glass-key','Pale blue glass key','The party weighs uses for the glass key, opens the prisoner’s door, and learns that the key must remain engaged in the lock.','Specific six-inch pale blue glass key at u0187–u0189, with its final use and removal constraint at u1024 and u1085–u1089.')
rec(d,'f6-glass-key',156,932,'The party studies the key and debates using it to enter the prison or escape the house.','observed','star',[(187,198),(758,778)])
rec(d,'f6-glass-key',973,1096,'The party uses the key to open the chosen prison doorway and cannot take it along while the door is open.','interacted','star',[(1011,1024),(1085,1092)])
quote(d,'f6-glass-key',973,1089,text='to open the door, the key has to remain in the lock engaged.',kind='description',attribution='The DM explains the lock’s requirement when Ayveen asks to take the key.')
item(d,'soul-bindery','On the Science and Possibilities of Soul Bindery','The party reads the treatise’s proposals for exploiting captive souls, uses its clues to interpret the prison, and then burns it.','The title, reading and burning are explicit at u0479–u0501 and u0799–u0808.','Things/Books/On the Science and Possibilities of Soul Bindery.md')
rec(d,'soul-bindery',475,810,'The party studies the book’s soul-binding arguments and possible escape clue before Txarro burns it in solidarity with Edric.','interacted','star',[(475,501),(799,810)])
quote(d,'soul-bindery',475,488,text='one can drink from a stream, but the wise man builds a water wheel and binds the force of moving water to use.',kind='written',speaker='f6-soul-author',attribution='The DM reads a passage by the book’s unnamed author; the author’s view is not asserted as fact.')
item(d,'allegories','Allegories for the Initiated','The party examines the order’s book of stories and riddles while learning about the visitor who left it on Aurae’s desk.','Named and paged through at u0335–u0347.','Things/Books/Allegories for the Initiated.md')
rec(d,'allegories',295,353,'Aurae identifies the abandoned book, and the party examines its unsettling allegories while asking about its previous reader.','interacted','supporting',[(325,353)])
quote(d,'aurae',156,283,attribution='Aurae explains how she measures time by attending to the books.')
quote(d,'aurae',156,826,attribution='Aurae answers Kaito’s offer to try taking her out of the library.')
quote(d,'aurae',156,833,attribution='The assistant chooses the name Aurae during the same conversation.')
d['review_notes'] += ['The key and two studied books qualify as items. Aurae stays an NPC despite being constructed and carried. Soul Bindery and its author remain distinct entities sharing an explicitly written source quote; ordinary shelves and incidental book titles are excluded.']
finish(d)

# Mawar 2: clue document, dangerous artifact, container, spent ring and mystery boat.
d=base('mawar-adventures-002')
item(d,'ciphered-scroll','The Ciphered Scroll','The decoded scroll guides the investigation into Azar’s experiments, Airion’s magic, Nimessa’s service, and the missing people.','The session opens with Wazir presenting and discussing this specific decoded document.','Campaigns/Mawar Adventures/Notes/The Ciphered Scroll.md')
rec(d,'ciphered-scroll',1,505,'Wazir presents the decoded scroll, and the party interprets its account of experiments, summoning, and attempted resurrection.','interacted','star',[(27,43),(83,115),(218,245)])
rec(d,'ciphered-scroll',1319,1383,'At the collapsed lodging, the party compares the missing victims with the scroll’s account of remaining experiments.','mentioned','supporting',[(1367,1380)])
rec(d,'ciphered-scroll',1892,2043,'The reunited party uses the scroll’s account to connect the suspect, ring, knife, Nimessa, and Gazankoa.','mentioned','star',[(1938,2007)])
item(d,'blood-knife','Blood Knife','The party learns that a speaking knife drove Azar’s murderous hopes, plans to contain it, and ultimately recovers it from his lair and seals it in lead.','Distinct knife discussed in Ovina’s commission and Azar’s account, then explicitly recovered at u3495–u3497.','Things/Magic Items/Blood Knife.md')
rec(d,'blood-knife',1715,1817,'Ovina reports that her customer wanted a lead-lined box to stop a knife from talking and troubling his dreams.','mentioned','star',[(1757,1772),(1799,1808)])
rec(d,'blood-knife',1892,2043,'The party connects the knife to Gazankoa and considers it the source of the danger.','mentioned','star',[(1938,1948),(1991,2007)])
rec(d,'blood-knife',2283,2419,'The party debates how to contain the knife and approach the man it may be influencing.','mentioned','star',[(2294,2315),(2367,2395)])
rec(d,'blood-knife',3445,3494,'Azar’s account describes a knife that replaces victims’ blood with water under a false promise of restoring his wife.','mentioned','star',[(3488,3494)])
rec(d,'blood-knife',3495,3497,'In the narrated lair search, the party finds the knife and seals it in the lead-lined box, quieting it.','interacted','star')
item(d,'m2-lead-box','Ovina’s lead-lined box','The party investigates Azar’s commissioned lead-lined box, watches him collect it, and later uses it to contain the recovered knife.','A specific carefully fitted container, not a generic chest; construction, testing and use are explicit at u1760–u1772, u2057–u2102 and u3496–u3497.')
rec(d,'m2-lead-box',1715,1817,'Ovina shows the almost-finished lead-lined box and explains the unusual commission.','observed','supporting',[(1757,1772)])
rec(d,'m2-lead-box',2044,2103,'Wazir examines the box outside the smithy and confirms that its lead lining can block magic.','interacted','star',[(2057,2076),(2088,2103)])
rec(d,'m2-lead-box',2491,2659,'The party watches Azar collect the box and carry it toward the dock during the confrontation.','observed','supporting',[(2491,2505)])
rec(d,'m2-lead-box',2660,3444,'During the fight, the party notices Azar has dropped the box in the boat and keeps track of it.','observed','supporting',[(2869,2875),(3058,3065)])
rec(d,'m2-lead-box',3495,3497,'The party seals the recovered knife inside the lead-lined box.','interacted','star')
item(d,'elemental-ring','Airion’s Ring of Elemental Binding','The party connects the ring in Azar’s account to his payment to Ovina, examines its dismantled pieces, and finds no remaining magic.','The transcript links the summoning ring to the smith’s payment; its dismantling and loss of magic are directly inspected.','Campaigns/Mawar Adventures/Items and Treasure/Airion\'s Ring of Elemental Binding.md')
rec(d,'elemental-ring',1,505,'Wazir describes the scroll’s account of Airion’s ring being used to summon and command Nimessa.','mentioned','supporting',[(218,245)])
rec(d,'elemental-ring',1715,1817,'Kaleho examines the dismantled gold ring and sapphires that Ovina accepted as payment.','interacted','supporting',[(1763,1787)])
rec(d,'elemental-ring',1892,2043,'The party suspects the payment ring is Airion’s and proposes checking it for magic.','mentioned','supporting',[(1968,1984),(2014,2027)])
rec(d,'elemental-ring',2044,2103,'Wazir tests the dismantled ring and learns that it is no longer magical, though a sapphire may once have held its power.','interacted','star',[(2052,2087)])
quote(d,'elemental-ring',2044,2071,kind='description',attribution='The DM gives the result of Wazir’s magical examination of the ring.')
item(d,'m2-phantom-boat','Azar’s phantom boat','Witnesses describe a boat passing through the shoals; the party later boards and moves it during the confrontation to interfere with Azar’s escape.','Specific unusual vessel described by Orden and used during the dockside fight; separate from the other submerged boat he initially recalls.')
rec(d,'m2-phantom-boat',1,505,'Wazir recalls an odd boat that no one saw arrive or depart while introducing the scroll investigation.','mentioned','cameo',[(1,7)])
rec(d,'m2-phantom-boat',1198,1318,'Orden tells Ryu and Trok about a small boat that passed through the shoals toward Shark’s Dock.','mentioned','star',[(1243,1275)])
quote(d,'m2-phantom-boat',1198,1253,kind='dialogue',speaker='orden',attribution='Orden reports what he believes he saw; the boat’s mechanism remains unexplained.')
rec(d,'m2-phantom-boat',1818,1876,'Wazir asks Sulfi’s servant about the strange vessel and receives a denial of knowledge.','mentioned','supporting',[(1830,1848)])
rec(d,'m2-phantom-boat',1892,2043,'The party compares the boat reports with the old man’s suspected activities.','mentioned','supporting',[(1895,1948)])
rec(d,'m2-phantom-boat',2283,2419,'The party considers whether Blue could follow the phantom boat if the old man leaves in it.','mentioned','supporting',[(2393,2406)])
rec(d,'m2-phantom-boat',2420,2490,'The party scouts the incoming boat while waiting near the smithy.','observed','supporting',[(2439,2448)])
rec(d,'m2-phantom-boat',2491,2659,'During the confrontation, Azar invites Ryu toward the boat while invisible Wazir moves to board it.','interacted','supporting',[(2620,2640)])
rec(d,'m2-phantom-boat',2660,3444,'The party grapples beside the boat and pushes it away to interfere with Azar’s escape.','interacted','star',[(2831,2875),(2990,3004),(3050,3065)])
quote(d,'ovina',1715,1810,attribution='Ovina makes the personal cost of providing the information explicit to Kaleho.')
quote(d,'yaz',2104,2189,2190,attribution='Yaz reflects on what the ocean-watchers’ stories mean.')
quote(d,'azar',2491,2622,attribution='Azar invites Ryu toward the boat; the subsequent insight check at u2648–u2654 reveals hostile intent.')
d['review_notes'] += ['Item selection captures the investigation’s document, knife, spent ring, deliberately constructed container and unusual boat; routine combat gear is excluded. The knife’s recovered location and containment follow the transcript’s brief lair fast-forward, not the players’ earlier guess that it was already inside the dockside box. The later note-only brass bowl and identification scenes remain outside transcript coverage.']
finish(d)

# Dunmari 108: distinguish the jade collection, its carrier, the payment and discussed artifacts.
d=base('dunmari-frontier-108')
item(d,'rai-jade','Rai’s jade hand fragments','The party learns Megren gave the sought fifth fragment to Ra’ghemdros, weighs how to recover it, and shows Dimitaur the four fragments already held in Kenzo’s staff.','One quest collection with explicitly differentiated parts: four already held versus the remaining fragment reported with the dragon; no acquisition of the fifth occurs here.','Campaigns/Dunmari Frontier Campaign/Treasure/Jade Piece of Rai\'s Hand.md')
rec(d,'rai-jade',849,2217,'Ghesh’s account of Megren’s valuable mainland find gives the party a lead on the missing jade fragment.','mentioned','star',[(1298,1315)])
rec(d,'rai-jade',2247,2688,'Megren describes finding the green gem and giving it to Ra’ghemdros in exchange for her tower.','mentioned','star',[(2319,2376),(2403,2427)],known_as='Megren’s green gem; identified as the sought fragment')
quote(d,'rai-jade',2247,2341,2343,kind='dialogue',speaker='megren',attribution='Megren recounts finding the gem; this is a report of an earlier discovery, not a present transfer to the party.')
rec(d,'rai-jade',2689,3099,'The reunited party debates trading, theft, and fighting to recover the jade held by the dragon.','mentioned','star',[(2692,2711),(2733,2759),(2890,2915)])
rec(d,'rai-jade',3659,3998,'The party invokes Rai’s jade and mission in the message asking the elder for an audience.','mentioned','supporting',[(3665,3712)])
rec(d,'rai-jade',4687,5644,'Kenzo reveals the four fragments to Dimitaur, recounts their recovery, and discusses whether completing the hand will help locate Apollyon’s phylactery.','interacted','star',[(4776,4795),(4837,4888),(4898,4930),(5152,5193),(5364,5388)])
item(d,'forest-staff','Staff of the Forest Soul','Kenzo uses his staff while communing with the memorial forest, seeks an image to preserve in it, and reveals its concealed jade fragments to Dimitaur.','The transcript explicitly places Kenzo’s staff in the communion and jade reveal; canonical note resolves its identity only.','Campaigns/Dunmari Frontier Campaign/Treasure/Staff of the Forest Soul.md')
rec(d,'forest-staff',2247,2688,'Kenzo explains that the staff’s ordinary appearance conceals its four jade fragments beneath growing wood.','mentioned','supporting',[(2348,2364)])
rec(d,'forest-staff',4094,4442,'Kenzo nestles the staff among the roots, communes with the forest, and asks for a memory to preserve in its design.','interacted','star',[(4102,4121),(4291,4308),(4350,4408)])
rec(d,'forest-staff',4687,5644,'Kenzo reveals the jade within his staff to demonstrate the party’s connection to Rai.','interacted','supporting',[(4779,4795),(4837,4888)])
item(d,'d108-circlet','Gold circlet with four alexandrite gems','Kenzo offers the circlet for Ghesh’s secrecy and guidance, then pays it over after the introduction to Megren.','A specific gold circlet from Grimbaskal’s hoard is selected at u1614; the party negotiates its transfer and pays at u2657–u2663. Do not identify it with another named magic circlet.')
rec(d,'d108-circlet',849,2688,'Kenzo negotiates the circlet as payment for Ghesh’s discretion and introduction, then hands over the promised reward.','interacted','star',[(1537,1540),(1612,1655),(2657,2663)])
quote(d,'d108-circlet',849,1614,text='the golden circlet set with four green alexandrite gems from Grimbaskal\'s hoard, worth at least 500 gold.',kind='dialogue',speaker='Delwath',attribution='Delwath identifies the particular treasure proposed as payment; this is not an NPC line.')
item(d,'soul-mirror','Mirror of Soul Trapping','The party considers consulting the hobgoblin wizard confined in the mirror as a possible ally against Ra’ghemdros, without actually contacting or releasing her.','The plan explicitly refers to the mirror prison at u5272–u5312; no present use occurs in the recording.','Campaigns/Dunmari Frontier Campaign/Treasure/Mirror of Soul Trapping.md')
rec(d,'soul-mirror',4687,5644,'The party discusses speaking through the mirror to the imprisoned wizard and weighs the danger of freeing her.','mentioned','supporting',[(5272,5312),(5584,5593)])
item(d,'d108-phylactery','Apollyon’s phylactery','The party hopes completing Rai’s jade hand will reveal the phylactery’s location and questions Dimitaur about finding and destroying it.','A specific central quest object discussed at u5152–u5193 and u5330–u5335; its form and location are not established here.')
rec(d,'d108-phylactery',4687,5644,'The party explains its plan to locate and destroy Apollyon’s phylactery, but Dimitaur cannot identify its location.','mentioned','star',[(5152,5193),(5328,5340)])
quote(d,'ghesh',849,1539,1540,attribution='Ghesh demands a meaningful payment before promising secrecy.')
quote(d,'ghesh',849,2210,attribution='Ghesh answers Kenzo’s questions about whether he would miss Ra’ghemdros.')
quote(d,'megren',2247,2342,2343,attribution='Megren explains her opportunistic view of finding the jade on the mainland.')
quote(d,'dimitaur',4687,4842,attribution='Dimitaur, still posing as the temple’s divine voice, admits he cannot see Kenzo’s dramatic display.')
quote(d,'dimitaur',4687,5347,5348,attribution='Dimitaur recounts why he abandoned Drankor while waiting for Rai.')
quote(d,'dimitaur',4687,5448,attribution='Dimitaur answers Kenzo’s request for advice on recovering the jade from the dragon.')
d['review_notes'] += ['The jade card is a collection, not a claim that the party has an intact hand: four fragments are already held and one is still sought. The staff is a separate object. The mirror is only discussed and the phylactery’s form is not established. Later canonical item histories and powers are not imported into the session.', 'Major NPC quotes now include three from Ghesh, two from Megren and four from Dimitaur, without adding NPC interaction records. The short source excerpt on the circlet is explicitly Delwath’s inventory description, not speech by the object or an NPC.', 'Scene types use dominant activity: the guided journey is travel, the memorial investigation and magical communion are exploration, and the temple exchange is conversation. Existing source boundaries are unchanged.']
finish(d)

index=['# Campaign interaction trials — version 3','','[Skill](/workspace/taelgar/.agents/skills/extract-campaign-interactions/SKILL.md) · [Format](/workspace/taelgar/.agents/skills/extract-campaign-interactions/references/format.md)','','Adds important-item cards, a type for every scene, and multiple complementary quotes for major NPCs. Every entity still gets one session overview. Existing NPC encounters and source boundaries are preserved, including long conversations. Earlier v2 results remain available.','','| Session | NPCs | Items | NPC quotes | Scene types | Reviews |','| --- | ---: | ---: | ---: | --- | --- |']
for sid,title in [('dunmari-frontier-008','Dunmari 8'),('dunmari-frontier-060','Dunmari 60'),('mawar-adventures-002','Mawar 2'),('lost-in-the-feywild-006','Lost in the Feywild 6'),('dunmari-frontier-108','Dunmari 108')]:
 p=OUT/sid;d=json.loads((p/'extraction.json').read_text());npcs={e['id'] for e in d['entities'] if e['kind']=='npc'};items=len(d['entities'])-len(npcs);nquotes=sum(len(r.get('quotes',[])) for r in d['interactions'] if r['entity'] in npcs)
 types=', '.join(f'{t}: {sum(s["type"]==t for s in d["scenes"])}' for t in ('conversation','exploration','combat','travel'))
 index.append(f'| [{title}]({p}/review.md) | {len(npcs)} | {items} | {nquotes} | {types} | [Items]({p}/items.md) · [NPCs]({p}/npcs.md) · [JSON]({p}/extraction.json) · [Evidence]({p}/evidence.md) |')
index += ['', 'Rai’s jade card distinguishes four held fragments from the fifth reported with Ra’ghemdros. The same session also indexes Kenzo’s staff, the circlet paid to Ghesh, the mirror prison and the discussed phylactery. No future acquisition or secret object identity is inferred.', '', 'Item interactions use the existing four kinds: interacted, observed, present and mentioned. Their exact source quotes are labeled as descriptions, writing or dialogue with the real speaker. Routine inventory, every weapon attack and background furnishings remain excluded.', '', 'Each scene has exactly one dominant type: conversation, exploration, combat or travel. Travel with incidental dialogue remains travel; magical investigation can remain exploration despite questions. Types do not fragment the full conversation records.', '', 'Major NPCs can feature several quotes from one conversation: Aurae has four, Ghesh three, and Dimitaur four. The single overview and whole interaction stay intact; shorter NPCs have fewer quotes when appropriate.', '', 'Mawar retains the transcript coverage limit: note-only later events involving Sefa, identification and departure are not assigned transcript links. Prior date and identity uncertainties remain in the session reviews. Quoted ASR wording is preserved.', '', 'Validation checks source hashes, all source coverage, typed scenes, NPC/item joins, complete ranges, exact quote text and attribution fields, multiple featured quote joins, and one overview per entity. The builder also checks that all accepted NPC interaction bounds and scene boundaries exactly match v2. Local line links remain the navigation mechanism; no web runtime is changed.']
(OUT/'README.md').write_text('\n'.join(index)+'\n')

import collections,hashlib,json,re
from pathlib import Path
B=Path('_sessions/dunmar-frontier/dunmari-frontier-054/cleaned');A=B/'cleanup-artifacts';P='dunmari-frontier-054'
src=(B/f'{P}-source-prepared.md').read_text().splitlines();cln=(B/f'{P}-source-cleaned.md').read_text().splitlines()
r=json.loads((A/f'{P}-cleanup-report.json').read_text());sha=r['review']['transcriptSha256']
material_text='''
103|The timing and village of Delwath's recent arrival remain garbled; do not infer a precise chronology.
120|This fragment may specify the number of armbands destroyed or who destroyed them; the following circlet discussion does not fully resolve it.
158|The subject described as a great hero in Dark Fire is unclear, potentially an entity name.
196|The reference following experience with may identify a battlefield or a map label; its spelling/identity is not secure.
199|The opening phrase may identify Iascaire's previous travel area. The two river names are separately supported by the glossary.
228|The phrase within the description of the timeless village may contain a location name or a substantive descriptor.
773|An entire utterance in the discussion of the spirit and offerings is unintelligible; its intent cannot be safely recovered.
843|The clarification of which combatant was the wizard is garbled; retain the surrounding vision without inventing a rider/beast distinction.
992|The quoted smite damage dice are uncertain; do not substitute rules knowledge for what was spoken.
1003|The requested saving throw's opening words, potentially its ability, are unclear.
1116|The hypothetical saving throw result on a natural one is unclear; the later discussion does not fully settle this arithmetic.
1611|The name of the battlefield just visited is garbled; no canonical battlefield identity was forced onto it.
1629|The route lists a further battlefield name that remains unclear; Dark Fire and Endless Dark are readable but the third label is not.
1759|The word attached to placing the wildfire spirit may be a name or merely a fragment; compare the repeated rendering at u2257.
1934|The closing qualification of the DM's pact-weapon ruling is garbled; earlier explicit restrictions are retained, but this qualification needs review.
1974|The alternative discussed in place of a sword charge may be a spell name; the complete phrase cannot be recovered reliably.
1975|This continuation of u1974's spell comparison is unintelligible and may affect the intended tactical comparison.
2257|This rendering, repeated after u1759, may name the wildfire spirit; no name has been invented.
2314|The opening could mean no damage or a correction that the pike does damage. The following resistance explanation favors reduced damage but does not establish the exact words.
2594|The initiative count at which the boar emerges is unclear.
2730|The requested summoned beast form is unclear; later flight confirms the eventual capability but not these words.
2731|The DM's response about summoning a form has two unclear spans; do not infer a specific form label or ruling.
2732|The selected form label is garbled and the adjacent Strength discussion includes a self-correction.
2902|The remaining creature's damage/outcome statement is unclear after the preceding save and vulnerability calculations.
2974|The attack's damage figure is garbled; it may be a number rather than the ordinary adjective great.
2979|The target's existing damage state or a question about killing it is unclear; the following correction says it was not wounded yet.
2984|The damage figure following the second blast is unclear; do not turn not into a guessed number.
3135|The final instruction explicitly defers a long rest, but the intended qualification about succeeding at it remains garbled.
'''
incidental_text='''
67|The armor's workmanship and pride are clear; only a descriptive modifier is garbled.
71|An isolated sound occurs within Aristaea's appearance description; the speaker and subject are already established.
72|Skin color is explicit; the introductory fragment adds no recoverable fact.
86|Stories and the guide pointing out the two PCs are clear; the trailing fragment does not establish a new event.
99|Personability is explicit in the surrounding description; the opening verbal fragment does not change it.
118|The question about who destroyed the armbands is explicit after this false start; the substantive count uncertainty is separately recorded at u0120.
175|The warning about low hit points is explicit here and at u0168-u0169; the final colloquial qualifier does not change that warning.
217|Horses not increasing pace is explicit across this line and u0218; the extra fragment does not obscure the conclusion.
223|Efficient forest travel is explicit; the introduction is garbled.
308|The approach to the village is clear in the immediately following map description; this fragment supplies no separate action.
336|The pale shadow of village life is explicit; only its trailing wording is unclear.
345|The offer of a protective blessing is clear in u0342-u0344 and both PCs accept in u0348-u0349; this elaboration does not obscure the decision.
346|A short continuation of the blessing offer; the later acceptance and target dialogue preserve the action.
361|The armor-class question is clear; the final table aside does not affect the spell choice.
363|The tentative selection wording is garbled, but the later spell discussion explicitly addresses Delwath and confirms his protection.
374|A joke/aside about clustering and area attacks; the aura's ten-foot range is explicit.
380|The knife-as-focus question is explicit; only its introduction is unclear.
392|The aura-edge query is garbled, but u0393 explicitly confirms that square counts.
421|A dice-interface troubleshooting aside; no character action or roll outcome is lost.
435|The creature emerging from the corner is described fully in u0437-u0441; the initial fragment overlaps map zooming.
527|A garbled transitional address precedes an explicit statement that Aristaea returns in u0528; no new person is inferred.
543|An aside after two declared misses; the actual attack outcomes are explicit at u0538 and u0542.
567|The ability's four uses per long rest and the optional nature of its use remain readable; the aside does not change those facts.
576|The speaker starts and then corrects an ability name; u0578 explicitly says Enhanced Bond does not apply.
577|Part of the same abandoned ability-name discussion; the ruling is explicit immediately after it.
583|Delwath entering the flame and receiving the vision are explicit; an intervening verbal sound does not alter them.
600|The dead-body location is clarified by the subsequent grave question and answer; this opening fragment is not an independent fact.
608|The room search/magic question is explicit; a garbled scope fragment does not produce a result or decision.
631|The following line explicitly explains the creature did not claw out of a grave; the final fragment is redundant.
641|The action removes dirt and uncovers skeletons in u0642; the verb describing the digging is incidental.
656|The disadvantage correction is explicit after this false start; the reminder is acknowledged by the DM.
663|The request to stay within ten feet for the save bonus is explicit; the surrounding false starts do not obscure the positioning request.
689|The reply explicitly reports six scattered bodies; the garbled search question does not change that discovery.
769|Both PCs seeing the spirit and Iascaire pointing it out are readable; the turn-taking fragment adds no action.
774|The speaker clearly distinguishes approaching the altar from approaching the party; the garbled beginning does not change that distinction.
788|A brief positioning/turn-taking fragment; subsequent stated actions remain explicit.
816|The coppiced tree's many branches are explicit; the garbled common noun is descriptive rather than an entity identity.
841|The wizard's westward direction is separately stated at u0845; the map-pointing phrase adds no usable bearing.
858|Casting Cure Wounds on the reeling Delwath is explicit; the arm/gesture description is garbled.
869|The group crossing the threshold together is readable; only a linking fragment is unclear.
876|The roof rubble being piled is explicit from u0873-u0875; the modifying word adds no separate discovery.
895|The immediately following description explains the harpoon arm attack; the initial fragment does not establish a separate ranged attack.
926|The discussion of staying out of melee is explicit; the modifier is garbled and the later movement supersedes the tentative plan.
931|The corner target is explicitly confirmed at u0940-u0942; the short fragment does not change it.
933|The Moonbeam/melee question is abandoned when concentration prevents casting that spell; no resulting attack is inferred.
946|The concentration conflict is explicit in u0947-u0948; the garbled spell-description fragment does not change the ruling.
999|A short pike/attack fragment after the decision to stop at two hits; no extra attack is inferred.
1019|The wildfire spirit only dodging is explicit; the final fragment does not obscure that action.
1052|An attack-roll aside followed by the DM explicitly declaring a hit at u1054.
1057|The question about severing the harpoon cord and the DM's answer are explicit; the inserted phrase does not change it.
1065|A roll-interface question about disadvantage; the following instruction is to roll twice.
1086|The roll of 21 is explicit; the preceding verbal fragment adds no result.
1094|The enemy's wounded state is explicit; the garbled introduction does not alter it.
1111|A brief health-status query; the response explicitly says bloodied.
1177|A check/coordination question immediately followed by rolling a perception/investigation check; no discovery relies on this fragment.
1217|A main-party comparison during rubble lifting; no action in the current session depends on it.
1260|Fifteen points are explicit and the surrounding discussion explains destruction; the final sound does not establish an alternate statistic.
1273|A dice/spell aside; the ongoing heat damage is explicitly discussed at u1275 and u1281-u1282.
1279|The heat damage dice are explicitly repeated as 2d8 in u1281-u1282; this garbled question adds no different value.
1282|The spell lasting for a minute and eventual destruction are explicit; the modifier of concentration is garbled.
1311|The two blessings are named explicitly at u1301 and u1304; the item-selection fragment adds no new blessing.
1316|An inventory/temporary-hit-point interface aside; the ten temporary hit points were explicitly awarded in u1299.
1325|A retrospective spell-slot concern during item setup; no actual expenditure is declared here.
1340|A coordination aside; Aristaea states her movement and vantage point immediately after it.
1396|The question about godcaller terminology is followed by an explicit identification with priests at u1397.
1413|The hundreds/thousands estimate is explicit; the trailing word is incidental.
1428|Organizing a burial is explicit and acted upon in the following exchange; the opening false start adds no separate action.
1443|The body being dug up and the spirit returning to the tree are confirmed in u1465; the linking sound is unclear.
1471|Prayer/sacrifice and the spirit vanishing as the ceremony finishes are explicit; only the introductory phrase is unclear.
1473|The tree-growth proposal is explicit both before and after this line; the unusual verb does not change it.
1475|A brief spell-slot aside followed by an explicit decision to cast Plant Growth.
1497|Sparks moving around and lush growth are explicit in the description; the movement verb is not a separate event.
1516|The tree splitting and fires finding the bodies are explicit; only a verbal transition is unclear.
1559|The temporary-hit-point duration question is answered in u1560-u1561; the stray noun adds no game fact.
1569|The short-rest meal at a campfire is explicit; the place modifier is garbled.
1750|The resource is identified as Wild Shape and the next line of discussion gives its remaining use; the final fragment adds no different cost.
1757|The conditional possibility of a fight is explicit; the exact verb does not change the subsequent decision to summon.
1780|A fragment immediately after the magic-circle proposal; later dialogue establishes its actual use and properties.
1796|Elves resting is explicit across u1792-u1796; the final phrase does not alter the four-hour duration.
1861|The proposal to protect the wildfire spirit from trees and wasps is explicit; the intervening fragment adds no target.
1878|Moving within sixty feet so the spell continues is explicit; the garbled gesture/position phrase does not obscure that plan.
1893|The closer position and continued Heat Metal are clear in the adjacent exchange; no exact map coordinate can be derived from the garbled words.
1910|Creating another pact weapon is the clear topic and the DM's following ruling is explicit; the fragment is not treated as a distinct object.
1919|The question is about the magic pact weapon and ruling; the unclear preface does not alter the explicit answer at u1923.
1930|The bound-weapon restriction is explicit before and after the redundant garbled word; no separate weapon category is inferred.
1995|A visual circle-size aside; the fifteen-foot radius is explicit at u1979.
2033|A short exclamation directed at the tree after a hit; no extra action is implied.
2058|A verbal preface to the explicit question about who maintains concentration; it does not identify a new item or actor.
2139|Turn coordination while retrieving a spell template; Aristaea proceeds immediately afterward.
2145|The sword being committed to the circle is explicit elsewhere; the introductory fragment adds no separate action.
2199|A preface to rolling the big tree's save; the next line explicitly states it succeeds.
2268|The save discussion and DC 18 are readable; the trailing word adds no result beyond the DM's failure statement.
2273|The tree burning and taking extra damage are explicit; the false-start noun does not change that outcome.
2346|A short aside before reading the spell; the action needed to move Moonbeam is explicitly confirmed next.
2374|A tentative positioning remark; the actual Moonbeam placement is discussed around it.
2376|The end of the turn is explicit in u2378; the stray word does not create an ability or resource.
2435|The attack roll is followed by an explicit miss at u2436; the animation/gesture description adds no event.
2500|The swarm's death, wolf's roll and initial half-damage statement are explicit, with the wolf-save effect corrected at u2506; the interjection adds no result.
2501|The next line explicitly distinguishes big tree from little tree; the final noun does not identify a new target.
2527|A recommendation to target the tree is followed by an explicit Moonbeam placement; the garbled command does not establish an attack.
2571|The d4 save penalty is explicit at u2562/u2567 and the actual reduced save is calculated next; the reminder's wording adds no new modifier.
2586|A short target/coordination fragment; u2587-u2588 explicitly resolve the wolf's failed save and death.
2622|The little trees' ten hit points are explicit; the opening fragment is not a new creature name.
2664|A descriptive adjective for the already-present tree is unclear; its save and attack are fully stated afterward.
2674|The intended Moonbeam action is repeated explicitly at u2676; this false start does not add a separate action.
2830|Turning the critical hit into a regular hit is repeated explicitly at u2836; the garbled mechanism preface does not change it.
2844|Concentration remaining and nine damage are explicit; the stray sound adds no condition.
2846|A thank-you after the critical-hit reduction; the person and action are clear from the surrounding exchange.
2847|An explanation of confusion about an ability; no action or item is established by the garbled phrase.
2852|The warning about another opportunity attack is explicit in u2853; the garbled question is not a separate move.
2866|Cone targeting is explicitly finalized as three trees at u2881; the conjunction does not change those targets.
2963|The bracelet's position and need for another turn are explicit; the final roll/effort aside does not imply it has been retrieved yet.
3046|The shadow beast's action has just been described; the garbled transition does not establish another action, and the PC's next action is narrated explicitly.
'''
def parse(s):
    return {f'u{int(k):04d}':v for k,v in (line.split('|',1) for line in s.strip().splitlines())}
mat=parse(material_text);inc=parse(incidental_text)
mat.update(parse('''
1627|The spoken route distances/comparison are fused into a number; do not guess the intended separate distances.
1628|Continuation of the route-distance comparison; the fused numerical rendering is not safely separable.
'''))
inc.update(parse('''
1564|The temporary-hit-point discussion refers back to the known blessings; this casual garbled item description does not establish a new key.
2317|A garbled recommendation is followed by the explicit discussion of Smite and radiant damage; the available action is clear from u2320-u2323.
'''))
marked={i['uid'] for i in r['review']['issues']}
assert not(set(mat)&set(inc))
assert marked==set(mat)|set(inc),(marked-(set(mat)|set(inc)),(set(mat)|set(inc))-marked)
issues=[{'uid':i['uid'],'importance':'material' if i['uid'] in mat else 'incidental','reason':(mat|inc)[i['uid']]} for i in r['review']['issues']]
assessment={'transcriptSha256':sha,'judgment':'Both passes are complete. The central actions remain intelligible, but some battlefield references, a summoning-form exchange, a pact-weapon qualification, and several tactical/numeric statements need human review. Questions are logged for morning review as requested; no tolerance or acceptance is recorded. Incidental flags preserve redundant or nonconsequential garble without inventing wording.','issues':issues}
(A/f'{P}-cleanup-assessment.json').write_text(json.dumps(assessment,indent=2,ensure_ascii=False)+'\n')
# Additional unclear incidental speech deliberately left unmarked. Each listed whole unit is one
# inventory span; a fragment is not made material merely by being short.
raw_groups={
'Off-game Zoom/setup anecdote; no session action or lore depends on this chatter.':[2,5,7,8,10,11,12],
'Speech fragment during appearance, introduction or table coordination; the defining facts and actions are explicit in adjacent units.':[44,55,77,79,102,109,123,136,137,176,177,192,203,204,216,227,257,273,314,320,321,356,357,390,393,398,404,419,430],
'Roll-interface, verbal filler or redundant combat coordination; actual rolls, outcomes or chosen actions are stated separately.':[486,487,496,497,509,511,514,557,561,566,601,614,619,621,626,628,640,650,662,668,669,670,677,679,693,696,698,725,754,761,783,797,801,813,842,844,855,856,875,896,925,934,945,960,962,967,973,985,1006,1024,1029,1031,1042,1055,1061,1071,1090,1095,1098,1127,1131,1137,1152,1172,1178,1190,1199],
'Meta or rest/interface chatter; the discoveries, choices, resources, or mechanics are explicit in the surrounding exchange.':[1216,1218,1225,1227,1228,1236,1250,1256,1268,1280,1285,1287,1302,1307,1320,1338,1345,1352,1357,1363,1368,1401,1416,1449,1450,1451,1459,1464,1478,1482,1521,1537,1540,1552,1555,1560,1564,1566,1568,1627,1628,1631,1635,1639,1640,1686,1698],
'Unclear personal break conversation, deliberately retained verbatim; unrelated to the session record.':[1583,1585,1586,1587,1588,1590,1592,1593,1594,1595,1596],
'Combat/strategy aside, gesture, false start or interface fragment; the actual action, limit, or outcome is explicit nearby.':[1714,1721,1728,1742,1749,1761,1762,1786,1787,1791,1836,1837,1858,1865,1881,1882,1886,1897,1898,1916,1927,1932,1933,1937,1938,1940,1948,1951,1954,1970,1971,1988,1999,2004,2015,2016,2018,2021,2027,2043,2053,2075,2076,2077,2078,2079,2083,2087,2096,2101,2120,2122,2140,2143,2152,2157,2164,2173,2180,2186,2187,2193,2220,2230,2243,2250,2253,2254,2278,2289,2295,2297,2299,2312,2317,2325,2336,2339,2362,2364,2369,2375,2377,2380,2389,2417,2421,2440,2445,2454,2456,2467,2478,2480,2484,2489,2490,2491,2497,2503,2506,2512,2534,2543,2547,2548,2563,2568,2585,2607,2611,2624,2636,2637,2640,2645,2647,2649,2663,2665,2678,2696,2704,2705,2709,2710,2728,2733,2735,2742,2753,2757,2760,2761,2767,2770,2772,2775,2798,2800,2815,2816,2822,2829,2831,2839,2842,2854,2855,2856,2873,2877,2889,2890,2898,2905,2908,2917,2925,2927,2935,2936,2938,2944,2945,2964,2966,2967,2975,2988,2990,2994,2995,2997,2999,3009,3010,3013,3019,3029,3030,3035,3036,3038,3039,3044,3048,3050,3056,3078,3080,3084,3085,3093,3106,3114,3115,3117,3121,3123,3124,3132]
}
# Inventory only actual residual garble; ordinary repetitions and intelligible
# unfinished utterances are not counted merely because they are informal speech.
raw_whitelist={2,5,7,8,10,11,12,77,123,136,137,176,177,204,257,356,398,404,557,566,601,650,693,754,761,960,1024,1090,1131,1137,1152,1178,1199,1218,1228,1345,1352,1363,1449,1537,1552,1555,1583,1585,1586,1587,1588,1590,1592,1593,1594,1595,1596,1635,1698,1728,1761,1786,1787,1836,1858,1881,1882,1897,1932,1933,1940,1970,1999,2015,2021,2053,2075,2096,2101,2120,2143,2152,2164,2243,2297,2299,2336,2364,2369,2375,2377,2417,2440,2445,2491,2506,2547,2585,2611,2624,2647,2649,2678,2728,2742,2760,2761,2770,2800,2831,2873,2877,2890,2905,2944,3010,3029,3030,3056,3078,3085}
raw_groups={reason:[n for n in ns if n in raw_whitelist] for reason,ns in raw_groups.items()}
assert set(n for ns in raw_groups.values() for n in ns)==raw_whitelist
rows=[]
for a in issues:
    n=int(a['uid'][1:])-1
    rows.append(a|{'kind':'marked','cleanedSpans':re.findall(r'\[\[(.+?)\]\]',cln[n]),'preparedSourceQuotation':src[n],'cleanedWording':cln[n],'preparedContextBefore':src[max(0,n-2):n],'preparedContextAfter':src[n+1:n+3],'cleanedContextBefore':cln[max(0,n-2):n],'cleanedContextAfter':cln[n+1:n+3]})
for reason,ns in raw_groups.items():
    for num in ns:
        uid=f'u{num:04d}';n=num-1
        assert uid not in marked,uid
        rows.append({'uid':uid,'importance':'incidental','kind':'unmarked-verbatim-noise','reason':reason,'cleanedSpans':[cln[n].split('] ',1)[1]],'preparedSourceQuotation':src[n],'cleanedWording':cln[n],'preparedContextBefore':src[max(0,n-2):n],'preparedContextAfter':src[n+1:n+3],'cleanedContextBefore':cln[max(0,n-2):n],'cleanedContextAfter':cln[n+1:n+3]})
assert len(rows)==len({a['uid'] for a in rows})
rows.sort(key=lambda a:int(a['uid'][1:]))
counts={}
for importance in ['material','incidental']:
    selected=[a for a in rows if a['importance']==importance]
    counts[importance]={'lines':len(selected),'spans':sum(len(a['cleanedSpans']) for a in selected),'markedLines':sum(a['kind']=='marked' for a in selected),'markedSpans':sum(len(a['cleanedSpans']) for a in selected if a['kind']=='marked'),'unmarkedVerbatimLines':sum(a['kind']!='marked' for a in selected)}
inventory={'schemaVersion':1,'preparedSourceSha256':hashlib.sha256((B/f'{P}-source-prepared.md').read_bytes()).hexdigest(),'transcriptSha256':sha,'reviewStatus':'pending-morning-review','humanAcceptanceRecorded':False,'quotationPolicy':'preparedSourceQuotation and preparedContext fields are exact prepared-source lines, including original headers and original errors. cleanedWording/cleanedContext fields are cleaned text and are not labeled verbatim source. Unmarked verbatim-noise spans count each listed unit as one span. Ordinary unfinished but intelligible speech is not treated as an additional unresolved issue.','counts':counts,'issues':rows}
# Verify every field labeled prepared/source against the actual prepared file.
source_set=set(src)
for a in rows:
    n=int(a['uid'][1:])-1
    assert a['preparedSourceQuotation']==src[n]
    for q in a['preparedContextBefore']+a['preparedContextAfter']:
        assert q in source_set
    assert a['cleanedWording']==cln[n]
(A/f'{P}-morning-review-inventory.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False)+'\n')
md=['# Session 054 morning review','',f'Cleaned transcript SHA-256: `{sha}`','',assessment['judgment'],'',inventory['quotationPolicy'],'','## Counts','', '| Class | Lines | Spans | Marked lines | Marked spans | Additional unmarked noise lines |','| --- | ---: | ---: | ---: | ---: | ---: |']
for k,c in counts.items():md.append(f'| {k} | {c["lines"]} | {c["spans"]} | {c["markedLines"]} | {c["markedSpans"]} | {c["unmarkedVerbatimLines"]} |')
for importance in ['material','incidental']:
    md+=['',f'## {importance.title()} review inventory','']
    for a in rows:
        if a['importance']!=importance:continue
        md += [f'### {a["uid"]} — {a["kind"]}', '',a['reason'],'','Prepared-source quotation (verbatim):','```text',a['preparedSourceQuotation'],'```','','Cleaned wording (edited transcript, not verbatim source):','```text',a['cleanedWording'],'```','','Prepared-source context (verbatim; nearest preceding/following units):','```text']
        if a['preparedContextBefore']:md.append(a['preparedContextBefore'][-1])
        if a['preparedContextAfter']:md.append(a['preparedContextAfter'][0])
        md += ['```','']
(A/f'{P}-morning-review-inventory.md').write_text('\n'.join(md).rstrip()+'\n')
print(json.dumps(counts,indent=2))

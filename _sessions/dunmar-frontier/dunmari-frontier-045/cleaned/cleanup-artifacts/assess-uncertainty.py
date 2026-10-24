import importlib,re
w=importlib.import_module('cleanup-work');d=w.load()
# Final local-context resolutions: direct address answered immediately by Wellby;
# Tim addressed by the player deciding who takes the stealth approach.
w.change(d,211,('So, [[while the]]', 'So, Wellby'))
w.change(d,201,('[[Our 10am]]','All right, Tim'))
# Keep protected-name spellings even within unresolved material.
w.change(d,353,('[[welby is complete to lb can do it every once]]','[[Wellby is complete to Wellby can do whatever he wants]]'))
for n in (201,211):d['materialReasons'].pop(f'u{n:04d}',None)
incidental={
78:'Garbled aside about not attacking random monsters; Kenzo’s opposition and the eventual mirror plan are explicit elsewhere.',
99:'Table banter about Wellby being woken by the horn; no new decision or event depends on the garbled lead-in.',
115:'Garbled aside about Riswynn not being present; the answer that Kenzo thinks it eats people is recoverable.',
120:'Conversational lead-in; the actual question to Delwath is intact.',
127:'Garbled self-interruption during debate; the explicit decision yes let’s kill it is intact, followed by the mirror plan.',
204:'Broken range lead-in; the operative 30-foot range is intact and reiterated in u0483.',
230:'Joking label for the operation; the three-person mirror plan is fully stated in surrounding units.',
240:'Table comment about another roll; the rolled outcomes are stated separately.',
297:'Redundant description of the plan; the trigger and flight response are stated in u0296.',
348:'Unclear reaction after saying Kenzo takes the hit; that action and damage are explicit later.',
448:'Garbled lead-in and filler; the declaration to blow the Horn of Silent Alarm is explicit in this same unit.',
452:'Broken filler before the stated half-mile distance; the out-of-range consequence is explicit in surrounding dialogue.',
459:'Unclear end of a repeated half-mile-range remark; no separate action is obscured.',
474:'Table pacing suggestion about giving the absent players something to do; no in-world action declared.',
475:'Table banter about Seeker occupying himself with rocks while absent; not a new declared session action.',
515:'Broken lead-in to the perception roll; Delwath and the natural 20 are recoverable, and the discovered gem is narrated explicitly.',
558:'Unclear false start; the question about needing a prisoner’s name is intact and immediately restated.',
568:'Broken ending to a sentence whose operative rule, summoning a named prisoner to the mirror surface, is intact and contextualized by u0554-u0560.',
571:'Unclear lead-in to the question about learning command words; the question’s subject and the following explanation are clear.',
589:'Brief banter following explicit confirmation that the creature is trapped; no additional action or decision recoverable.',
641:'Broken lead-in before the explicit one-week recharge and second-use opportunity.',
739:'Unclear aside reacting to an unusual mount; Baxter’s identity and stable arrangements are stated in the following units.',
784:'Table question about whether to roleplay the information gathering; the information requested and resulting narration are intact.',
808:'Unclear qualitative city-size label; quantitative comparisons and city identity are stated explicitly around it.',
916:'Garbled joke about how Wellby would use the horn; he explicitly declines taking it.',
922:'Unclear word in a repeated de-escalation joke; no event, identity, or decision depends on it.',
1008:'Unclear wording of a reaction to the inspiration rule; the actual roll-twice/take-higher rule is explicit in u1007.',
1039:'An illustrative/joking hypothetical dwarf-family name, not an identified character; DM explicitly says the dwarf is unrecognized.',
1208:'Brief reaction to Seeker’s lizardfolk contact; the actual contact and timing discussion are stated in adjacent units.',
}
for n,reason in incidental.items():
    uid=f'u{n:04d}'; t=d['edits'][uid];spans=re.findall(r'\[\[(.+?)\]\]',t)
    assert spans,(uid,t)
    d['edits'][uid]=re.sub(r'\[\[(.+?)\]\]',r'\1',t)
    d['incidental'][uid]={'spans':spans,'reason':reason}
    d['materialReasons'].pop(uid,None)
d['passes'].append({'pass':'assessment','status':'all remaining uncertainty classified in context; review deferred to morning by explicit user instruction; no acceptance recorded'})
w.save(d)
print('Assessment classifications saved')

"""Reviewed v4 pilot migration: merge session-note events with frozen v3 encounters."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

VAULT = Path('/workspace/taelgar')
ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location('validator', ROOT / 'validate-v4.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
NOTES = {
 'dunmari-frontier-008': 'Campaigns/Dunmari Frontier Campaign/Session Notes/Session 8 (DuFr).md',
 'dunmari-frontier-060': 'Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md',
 'dunmari-frontier-108': 'Campaigns/Dunmari Frontier Campaign/Session Notes/Session 108 (DuFr).md',
 'mawar-adventures-002': 'Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 02.md',
 'lost-in-the-feywild-006': 'Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 06.md',
}

def frozen(path):
 return {'path': path, 'sha256': hashlib.sha256((VAULT / path).read_bytes()).hexdigest()}

def select(d, text):
 lines = (VAULT / NOTES[d['session']]).read_text().splitlines()
 matches = [(i, line) for i, line in enumerate(lines, 1) if text in line]
 assert len(matches) == 1, (text, len(matches))
 line = matches[0][0]
 return {'source': 'session-note', 'startLine': line, 'endLine': line, 'text': text}

def phrase(d, start, end):
 text = (VAULT / NOTES[d['session']]).read_text()
 a = text.index(start)
 b = text.index(end, a) + len(end)
 return select(d, text[a:b])

def ent(d, eid):
 return next(e for e in d['entities'] if e['id'] == eid)

def record(d, rid):
 return next(r for r in d['interactions'] if r['id'] == rid)

def enrich(d, scene, selector, ids=()):
 d['scenes'][scene - 1]['evidence'].append(selector)
 for rid in ids:
  r = record(d, rid)
  r['evidence'].append(copy.deepcopy(selector))
  r['continuity'] = r.get('continuity', '') + ' The session note supplies additional detail about the same encounter, not a second encounter.'

def scene(d, kind, location, start, end, time, boundary, selectors):
 index = len(d['scenes']) + 1
 d['scenes'].append({'index': index, 'type': kind, 'location': location, 'boundary': boundary,
  'date': {'start': start, 'end': end, 'time': time,
   'basis': 'Session-note timeline and narrative; ' + boundary,
   'evidence': [f"{NOTES[d['session']]}:L{s['startLine']}" for s in selectors]}, 'evidence': selectors})
 return index

def add_entity(d, eid, kind, label, overview, note=None, canonical=None):
 d['entities'].append({'id': eid, 'kind': kind, 'label': label, 'canonical_name': canonical,
  'note': note, 'eligibility': 'named' if note else 'distinctive',
  'basis': 'Named session-note subject.' if note else 'Specific recovered coins used for consequential restitution, not routine inventory.',
  'session_overview': overview, 'overview_records': [], 'quote_review': 'not_applicable', 'featured_quote_ids': []})
 if note and not any(s['path'] == note for s in d['supporting_sources']):
  d['supporting_sources'].append(frozen(note))

def add_record(d, eid, index, interaction, importance, overview, selectors, perspective=None):
 r = {'id': f'{eid}-notes-{index}', 'entity': eid, 'scenes': [index], 'interaction': interaction,
      'importance': importance, 'overview': overview, 'evidence': copy.deepcopy(selectors)}
 if len(selectors) > 1:
  r['continuity'] = 'These note passages document one event.'
 if perspective:
  r.update(perspective='session_record', observation_basis=perspective)
 d['interactions'].append(r)
 return r

def mawar(d):
 d['segmentation_revision'] += 1
 d['review_notes'] = [x for x in d['review_notes'] if not x.startswith(('Transcript-backed scope:', 'Reliah is mentioned,', 'Version 3 adds', 'Item selection captures'))]
 d['review_notes'][:0] = [
  'Version 4 includes documented events beyond the recording: Sefa, lair treasure and restitution, August 6 identification, and August 9 departure. Each note-backed claim links to an exact passage in the original session note; no transcript UIDs are invented.',
  'Reliah’s visit record now includes the session note’s affirmative account that the party inquires with both sisters. Samar retains the transcript dialogue; no speech is invented for Reliah. Sulfi still answers through a servant.',
  'Scenes 1–25 retain their indexes and transcript boundaries. The notes add a lair combat before the recovery (formerly scene 26, now 27), and later events; segmentation revision increases to 2.',
  'The note says Sefa is found dead, then describes restitution “to Sefa” and families of the dead. Preserve that wording as an unresolved recipient ambiguity; do not imply Sefa survived or personally received payment. Payment time and precise location are unspecified.',
  'The departure is a documented event; the note does not establish that the PCs witnessed a farewell. Its observed records explicitly use session-record perspective.',
 ]
 # Same visit, stronger evidence for Reliah, no duplicate encounter.
 interview = phrase(d, 'Seeking more information,', 'before lunch.')
 enrich(d, 7, interview, ['reliah-1102'])
 r = record(d, 'reliah-1102')
 r.update(interaction='interacted', overview='The session note records the party questioning Reliah alongside Samar, although only Samar’s dialogue is clear in the transcript.')
 ent(d, 'reliah')['session_overview'] = 'The party plans to consult Reliah, and the session note records her participation alongside Samar in the Drowned Flats interview.'
 aftermath = phrase(d, 'Afterward, [[Wazir]]', "[[Azar's Tale|Azar's full tale]].")
 enrich(d, 25, aftermath, ['azar-3445'])
 add_record(d, 'm2-bystander', 25, 'interacted', 'supporting', 'After the fight, the party tends the woman killed by Azar’s lightning.', [aftermath])
 ent(d, 'm2-bystander')['session_overview'] = 'The party witnesses Azar’s lightning kill a dockside bystander and tends her after the fight.'
 # Keep the brief recorded recovery, insert the separately documented combat before it.
 recovery = d['scenes'].pop()
 combat = select(d, 'That evening, the party searches the [[Splinters]], quickly destroys two more drowned zombies, and finds [[Sefa]] dead in the lair.')
 scene(d, 'combat', 'Azar’s lair in the Splinters', '1747-08-05', '1747-08-05', 'evening', 'The notes document a separate lair fight before the search; exact movement within the lair is unspecified.', [combat])
 recovery['index'] = 27
 recovery['date'].update(time='evening', basis='August 5 from the session-note timeline; “That evening” explicitly dates the lair search.')
 recovery['boundary'] = 'Post-combat search and recovery, briefly fast-forwarded in the transcript and expanded in the session note.'
 loot = phrase(d, 'From the lair,', 'who can be found.')
 recovery['evidence'].extend([combat, loot])
 d['scenes'].append(recovery)
 for r in d['interactions']:
  if 26 in r['scenes']:
   r['scenes'] = [27 if i == 26 else i for i in r['scenes']]
 sefa_note = 'People/Mawarans/Sefa.md'
 add_entity(d, 'sefa', 'npc', 'Sefa', 'The party finds Sefa dead in Azar’s lair; the notes also associate restitution with her, without clarifying the recipient after her death.', sefa_note, 'Sefa')
 add_record(d, 'sefa', 27, 'observed', 'supporting', 'The party finds Sefa dead while searching Azar’s lair.', [combat])
 add_entity(d, 'airion-research', 'item', 'Airion’s annotated research books', 'The party recovers three annotated books from Airion’s library in Azar’s lair.', "Campaigns/Mawar Adventures/Items and Treasure/Airion's Elemental Research.md", "Airion's Research on the Elemental Plane of Water")
 add_record(d, 'airion-research', 27, 'interacted', 'supporting', 'The party recovers three annotated books from Airion’s library.', [loot])
 add_entity(d, 'airion-bowl', 'item', 'Airion’s brass bowl', 'The party recovers a brass bowl, which Wazir identifies as commanding water elementals when filled with fresh ocean water and used immediately.', "Campaigns/Mawar Adventures/Items and Treasure/Airion's Bowl of Commanding Water Elementals.md", "Airion's Bowl of Commanding Water Elementals")
 r = add_record(d, 'airion-bowl', 27, 'interacted', 'supporting', 'The party recovers a brass bowl from Azar’s lair.', [loot])
 r['known_as'] = 'Brass bowl; its function is identified the following day.'
 add_entity(d, 'm2-restitution-coins', 'item', 'Recovered restitution coins', 'Coins recovered from Azar’s lair are used for restitution associated with Sefa and the families of the dead who can be found.')
 add_record(d, 'm2-restitution-coins', 27, 'interacted', 'supporting', 'The party recovers scattered coins from Azar’s lair.', [loot])
 scene(d, 'conversation', 'Unspecified; associated with the Hamri aftermath', '1747-08-05', '1747-08-09', None, 'Restitution follows recovery; the exact date, setting and recipient on Sefa’s behalf are unspecified within the session period. Conversation denotes the settlement, with no dialogue reconstructed.', [loot])
 add_record(d, 'm2-restitution-coins', 28, 'interacted', 'supporting', 'The recovered coins fund restitution associated with Sefa and families of the dead who can be found.', [loot])
 add_record(d, 'sefa', 28, 'mentioned', 'cameo', 'The notes name Sefa in the restitution account, without explaining who receives payment on her behalf after her death.', [loot])
 identify = phrase(d, 'On Aug 6,', 'used immediately.')
 scene(d, 'exploration', 'Unspecified; associated with the Hamri aftermath', '1747-08-06', '1747-08-06', None, 'Explicit August 6 identification, separate from the previous evening’s recovery; no exact room or site is stated.', [identify])
 add_record(d, 'blood-knife', 29, 'interacted', 'star', 'Wazir attempts to identify the contained Blood Knife but finds it a mystery beyond his magic.', [identify])
 add_record(d, 'm2-lead-box', 29, 'present', 'supporting', 'The lead-lined box contains the Blood Knife during Wazir’s identification attempt.', [identify])['presence_basis'] = 'The note explicitly describes the knife as now locked in the lead-lined box at identification.'
 add_record(d, 'airion-bowl', 29, 'interacted', 'star', 'Wazir identifies the bowl’s command over water elementals and its requirement for fresh ocean water used immediately.', [identify])
 ent(d, 'blood-knife')['session_overview'] = 'The party traces Azar’s murders to the speaking knife, recovers and seals it in lead, but Wazir’s subsequent identification cannot resolve its mystery.'
 ent(d, 'm2-lead-box')['session_overview'] = 'The party investigates Azar’s commissioned lead-lined box and uses it to contain the recovered knife, which remains locked inside during Wazir’s later identification attempt.'
 departure = phrase(d, 'A few days later,', 'make amends to [[Hamri]].')
 destination = select(d, '- (DR:: 1747-08-09): [[Azar the Lost]] leaves [[Hamri]] with [[Benat]] for the [[Lizardfolk|lizardfolk]] village.')
 scene(d, 'travel', 'South from Hamri toward the lizardfolk village', '1747-08-09', '1747-08-09', None, 'Explicit August 9 departure; destination comes from the timeline. Neither arrival nor an on-screen farewell is established.', [destination, departure])
 for eid, overview in [('azar', 'The session note records Azar leaving Hamri southward with Benat to heal before returning to make amends.'), ('benat', 'The session note records Benat accompanying Azar south from Hamri toward the lizardfolk village.')]:
  add_record(d, eid, 30, 'observed', 'supporting', overview, [destination, departure], 'The note states the departure occurred but does not identify a PC witness or direct exchange.')
 ent(d, 'azar')['session_overview'] = 'The party traces, confronts and defeats Azar, hears how the knife exploited his hope of restoring his family, and the notes later record his departure with Benat to heal.'
 ent(d, 'benat')['session_overview'] = 'Benat trades stories about Airion’s water magic for Trok’s promise to write to his family, then later accompanies Azar south from Hamri to heal.'


def dunmar60(d):
 d['segmentation_revision'] += 1
 night = select(d, 'Spend the night in [[Wahacha]].')
 scene(d, 'exploration', 'Wahacha — lodging not specified', '1748-10-12', '1748-10-12', 'night', 'The timeline confirms the overnight stay after the recorded tour; no named NPC is established as staying with Wellby. Exploration includes rest under the four-type vocabulary.', [night])
 d['review_notes'].append('Version 4 includes the note-confirmed night in Wahacha as scene 21. No NPC presence or next-morning meeting is inferred; the voyage language learning already has transcript coverage in scene 12.')


def dunmar108(d):
 d['segmentation_revision'] += 1
 talk = select(d, "- The party stays up into the night talking to Dimitaur about Drankor, Rai's quest to break Isingue free of the [[Seeds of Chaos]] caused by Cha'mutte's death, his failure and disappearance, and Apollyon's growing strength. They also discuss Apollyon and Cha'mutte's hatred of each other.")
 enrich(d, 17, talk, ['dimitaur-4687', 'rai-4687', 'chamutte-4687', 'apollyon-4687'])
 scry = select(d, '- Before bed: Used clairvoyance to see the basic layout of Ra’ghemdros’ lair, noting chimeras sleeping.')
 scene(d, 'exploration', 'Temple resting area; remote view of Ra’ghemdros’ lair', '1749-05-18', '1749-05-19', 'before the long rest', 'The note confirms clairvoyance beyond the recording. Midnight timing is unresolved, so retain the session’s bounded dates; the casting site follows the preceding temple encounter.', [scry])
 rest = select(d, '- Long rest.')
 scene(d, 'exploration', 'Temple resting area (inferred from preceding encounter)', '1749-05-18', '1749-05-19', 'overnight', 'Raw notes confirm the long rest. No separate morning encounter or continued NPC presence is established.', [rest])
 d['review_notes'] = [x for x in d['review_notes'] if not x.startswith(('Seventeen scenes follow', 'The session metadata ends', 'Scene types use'))]
 d['review_notes'].append('Version 4 merges note-documented late conversation into the existing Dimitaur encounter and adds the confirmed clairvoyance and long rest as scenes 18–19. It does not invent a meeting with Ra’ghemdros, cards for generic chimeras, or a next-morning encounter; the time relative to midnight remains bounded May 18–19.')


def finish(d):
 for e in d['entities']:
  e['overview_records'] = [r['id'] for r in d['interactions'] if r['entity'] == e['id']]
 rows, span = v.validate(d, VAULT)
 folder = ROOT / d['session']
 folder.mkdir(exist_ok=True)
 (folder / 'extraction.json').write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n')
 (folder / 'review.md').write_text(v.render(d, VAULT, rows, span))
 (folder / 'evidence.md').write_text(v.render(d, VAULT, rows, span, excerpts=True))
 for kind, filename in [('npc', 'npcs.md'), ('item', 'items.md')]:
  subset = copy.deepcopy(d)
  subset['entities'] = [e for e in d['entities'] if e['kind'] == kind]
  ids = {e['id'] for e in subset['entities']}
  subset['interactions'] = [r for r in d['interactions'] if r['entity'] in ids]
  (folder / filename).write_text(v.render(subset, VAULT, rows, span))
 print(d['session'], len(d['scenes']), 'scenes;', len(d['entities']), 'entities;', len(d['interactions']), 'records')

if __name__ == '__main__':
 for sid, note in NOTES.items():
  original = json.loads((ROOT.parent / 'v3' / sid / 'extraction.json').read_text())
  d = v.upgrade_v3(original)
  d['sources'].append({'id': 'session-note', 'kind': 'session_notes', **frozen(note)})
  d['supporting_sources'] = [s for s in d['supporting_sources'] if s['path'] != note]
  # Remove obsolete historical assertions from the active review, preserving them in v3.
  d['review_notes'] = [x for x in d['review_notes'] if not x.startswith('Version 3 adds')]
  if sid == 'mawar-adventures-002': mawar(d)
  elif sid == 'dunmari-frontier-060': dunmar60(d)
  elif sid == 'dunmari-frontier-108': dunmar108(d)
  else: d['review_notes'].append('Version 4 review: the complete session note was checked against the transcript-backed events; no additional eligible note-only encounter was identified. Existing segmentation and records are retained.')
  # Every accepted quote, full transcript range and identity is preserved across migration.
  originals = {r['id']: r for r in original['interactions']}
  for r in d['interactions']:
   if r['id'] in originals:
    assert [{k: val for k, val in x.items() if k != 'source'} for x in r['evidence'] if x['source'] == 'transcript'] == originals[r['id']]['transcript']
    assert [{k: val for k, val in x.items() if k != 'source'} for x in r.get('quotes', [])] == originals[r['id']].get('quotes', [])
  finish(d)

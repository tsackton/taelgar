"""Read prepared/cleaned UID transcript units without changing their text."""
import re
from .storage import require

LINE = re.compile(r'^(\[(u\d{4,})\s*\|\s*([^|]+)\|\s*([^\]]+)\])(\s+)(.*)$')
MARKER = re.compile(r'\{\{([^{}\n]+)\}\}')


def seconds(value):
    require(bool(re.fullmatch(r'\d+(?::\d+){0,2}(?:\.\d+)?', value.strip())), f'Invalid time: {value}')
    parts = [float(x) for x in value.split(':')]
    require(len(parts) == 1 or parts[-1] < 60, f'Invalid seconds: {value}')
    require(len(parts) < 3 or parts[1] < 60, f'Invalid minutes: {value}')
    return sum(x * 60 ** i for i, x in enumerate(reversed(parts)))


def parse_units(text):
    units, seen = [], set()
    for number, line in enumerate(text.lstrip('\ufeff').splitlines(), 1):
        if not line.strip():
            continue
        match = LINE.fullmatch(line)
        require(match is not None, f'Invalid UID transcript line {number}')
        header, uid, timing, speaker, separator, wording = match.groups()
        require(uid not in seen, f'Duplicate UID: {uid}')
        seen.add(uid)
        pair = timing.strip().split('-')
        require(len(pair) == 2 and seconds(pair[1]) >= seconds(pair[0]), f'Invalid timing: {uid}')
        remainder = MARKER.sub('', wording)
        require('{{' not in remainder and '}}' not in remainder, f'Malformed uncertainty marker: {uid}')
        require(bool(wording.strip()), f'Empty source unit: {uid}')
        units.append({'uid': uid, 'header': header, 'separator': separator,
                      'speaker': speaker.strip(), 'timing': timing.strip(), 'text': wording})
    require(bool(units), 'Transcript is empty')
    return units

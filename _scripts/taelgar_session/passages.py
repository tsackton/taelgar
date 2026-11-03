"""Read-only checks for marked omissions in verbatim source passages."""
import re
from .transcript import require

INLINE = re.compile(r'\(\(([^()\n]+)\)\)')


def check_label(label, limit):
    require(isinstance(label, str) and label.strip() and '\n' not in label and '%%' not in label, 'Label must be one nonempty line')
    require(not any(c in label for c in '<>[]()\r'), 'Labels must be plain text, without parentheses, links or markup')
    require(len(label.split()) <= limit, f'Label exceeds {limit} words')
    require(not re.search(r'[.!?]\s+\S', label), 'A snip may contain at most one sentence')


def apply_cuts(turn, cuts):
    """Validate transient matches against source; no cut positions are persisted."""
    original = turn['body']
    prefix = re.match(r'[^\n:]+: ', original).end()
    require(isinstance(cuts, list) and cuts, 'Inline cuts must be a nonempty list')
    cursor, output, retained = 0, [], []
    protected = list(re.finditer(r'\{\{.*?\}\}|\[\[.*?\]\]|%%.*?%%', original, re.S))
    for item in cuts:
        require(isinstance(item, list) and len(item) == 3, 'Each inline cut is [start,end,label]')
        start, end, label = item
        require(type(start) is int and type(end) is int, 'Inline offsets must be integers')
        require(prefix <= start < end <= len(original.rstrip()), 'Inline cut must stay inside speech, outside speaker/separator')
        require(start >= cursor, 'Inline cuts overlap or are out of order')
        require(original[start:end].strip(), 'Do not substitute whitespace alone')
        word = lambda c: c.isalnum() or c in "_'’"
        require(not (word(original[start-1]) and word(original[start])), 'Inline cut starts inside a word')
        require(end == len(original) or not (word(original[end-1]) and word(original[end])), 'Inline cut ends inside a word')
        require(not any(start < m.end() and m.start() < end for m in protected),
                'Inline cut overlaps an uncertainty marker, wikilink or source comment')
        check_label(label, 6)
        output.extend([original[cursor:start], '((' + label + '))'])
        retained.append(original[max(cursor, prefix):start])
        cursor = end
    output.append(original[cursor:])
    retained.append(original[cursor:])
    require(any(c.isalnum() for c in ''.join(retained)), 'Inline cuts must leave original speech; use a whole-turn snip otherwise')
    return ''.join(output)


def match_inline(turn, body):
    """Check retained wording in order, treating ((labels)) as omitted source text.

    Matches exist only during validation. Restoration always uses the whole turn;
    there is no stored sub-turn alignment or individually restorable cut.
    """
    if body == turn['body']:
        return []
    markers = list(INLINE.finditer(body))
    literals = INLINE.split(body)[::2]
    require(markers and all('((' not in part and '))' not in part for part in literals),
            'Unmarked change or malformed ((label)) in retained turn')
    pattern = '(.+?)'.join(re.escape(part) for part in literals)
    match = re.fullmatch(pattern, turn['body'], flags=re.S)
    require(match is not None, 'Unmarked change to retained wording or speaker')
    cuts = [[*match.span(i + 1), marker.group(1)] for i, marker in enumerate(markers)]
    require(apply_cuts(turn, cuts) == body, 'Invalid inline substitution')
    return cuts

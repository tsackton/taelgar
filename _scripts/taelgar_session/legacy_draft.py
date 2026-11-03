"""Read legacy reduction drafts; no authoring, editing, or repair commands."""
import json
import re
from .transcript import META, parse_polished, coverage, require
from .passages import INLINE, check_label, match_inline


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def comment(prefix, value):
    text = compact(value)
    require('%%' not in text, 'Comment values cannot contain %%')
    return prefix + text + ' %%\n'


def read_comment(line, prefix, value_type=dict):
    require(line.startswith(prefix) and line.endswith(' %%'), 'Malformed draft control comment')
    value = json.loads(line[len(prefix):-3])
    require(isinstance(value, value_type), f'Control comment must contain a {value_type.__name__}')
    return value


def check_draft_syntax(turns):
    for turn in turns:
        require('((' not in turn['body'] and '))' not in turn['body'],
                'Polished source uses reserved ((...)) syntax; report the collision without editing it')


def metadata(bundle):
    check_draft_syntax(bundle['turns'])
    return {'version': 4, 'sessionYaml': bundle['manifest'].relative_to(bundle['root']).as_posix(),
            'sourceSha256': bundle['sourceSha256']}


def assemble(bundle, meta, blocks):
    return (comment(META, meta) + '# Interaction processing draft\n\n'
            '> Derived working copy. Double-parenthesized snips are generated, not dialogue.\n\n'
            + bundle['header'] + ''.join(blocks))


def inspect_draft(bundle, text=None):
    if text is None:
        text = bundle['draft'].read_text(encoding='utf-8')
    line, rest = text.split('\n', 1)
    meta = read_comment(line, META)
    require(type(meta.get('version')) is int and meta['version'] == 4, 'Unsupported draft version')
    require(meta == metadata(bundle), 'Draft source or metadata changed; do not overwrite or silently rebase this draft')
    header, blocks = parse_polished(rest)
    expected_header = assemble(bundle, meta, []).split('\n', 1)[1]
    require(header == expected_header, 'Draft/source header changed outside permitted substitutions')
    require(coverage(blocks) == bundle['coverage'], 'Draft source coverage differs from polished transcript')
    cursor, snippets = 0, []
    for block in blocks:
        start, spans = cursor, []
        # Exact inherited span partitions identify the original turns, even when
        # a turn combines UIDs or a UID spans multiple turns. No saved turn IDs.
        while len(spans) < len(block['spans']):
            require(cursor < len(bundle['turns']), 'Block has no source turn')
            spans.extend(bundle['turns'][cursor]['spans'])
            cursor += 1
        require(block['spans'] == spans, 'A block source map was reassigned or changed')
        block['startTurn'], block['endTurn'] = start + 1, cursor
        marker = re.fullmatch(INLINE.pattern + r'\n\n', block['body'])
        block['snipped'] = marker is not None
        if marker:
            label = marker.group(1)
            check_label(label, 40)
            snippets.append({'startTurn': start + 1, 'endTurn': cursor, 'label': label})
        else:
            require(cursor == start + 1, 'Retained text must stay within one original polished turn')
            block['cuts'] = match_inline(bundle['turns'][start], block['body'])
    require(cursor == len(bundle['turns']), 'Some polished turns are missing')
    return meta, blocks, snippets

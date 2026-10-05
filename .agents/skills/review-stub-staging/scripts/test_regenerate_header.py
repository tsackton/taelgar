import unittest
import json
import os
from pathlib import Path
import subprocess
import yaml
from regenerate_header import frontmatter, replace_header


class FrontmatterDiscoveryTests(unittest.TestCase):
    def test_opening_horizontal_rule_is_not_frontmatter(self):
        text = '---\n## Pre-campaign notable events\n\nTimeline content.\n'
        self.assertEqual(frontmatter(text, required=False), (None, {}))

    def test_closed_frontmatter_is_still_read(self):
        text = '---\nname: Example\naliases: [Alternate]\n---\n# Example\n'
        self.assertEqual(frontmatter(text, required=False)[1],
                         {'name': 'Example', 'aliases': ['Alternate']})

    def test_invalid_closed_frontmatter_still_fails(self):
        with self.assertRaises(yaml.YAMLError):
            frontmatter('---\nname: [unfinished\n---\n', required=False)
        with self.assertRaisesRegex(ValueError, 'must be a mapping'):
            frontmatter('---\n- not a mapping\n---\n', required=False)

    def test_target_note_still_requires_frontmatter(self):
        with self.assertRaisesRegex(ValueError, 'Expected YAML frontmatter'):
            frontmatter('---\n# Article without frontmatter\n')


class HeaderPreservationTests(unittest.TestCase):
    def test_body_and_frontmatter_survive(self):
        prefix = '---\r\nheaderVersion: old\r\nname: Example\r\n---\r\n'
        body = '\r\n%% private guidance %%\r\n![[portrait.png]]\r\nArticle.\r\n%%^Metadata:names:v1%%\r\n- {name: Example, language: unknown}\r\n%%^End%%'
        text = prefix + '# Old\r\n*(old)*\r\n>[!info]+ Old\r\n> old data\r\n' + body
        generated = '# Example\n*(new)*\n>[!info]+ Biographical Info  \n> new data\n'
        result = replace_header(text, generated)
        self.assertTrue(result.startswith(prefix))
        self.assertTrue(result.endswith(body))
        self.assertNotIn('> old data', result)
        self.assertEqual(replace_header(result, generated), result)

    def test_body_without_blank_separator_is_preserved(self):
        text = '---\nname: Example\n---\n# Example\n>[!info]+ Info\n> data\nArticle without separator.\n'
        self.assertTrue(replace_header(text, '# Example\n').endswith('Article without separator.\n'))

    def test_yaml_only_receives_header(self):
        self.assertEqual(replace_header('---\nname: Example\n---\n', '# Example\n'),
                         '---\nname: Example\n---\n# Example\n\n')


class StandaloneRuntimeTests(unittest.TestCase):
    root = Path(__file__).resolve().parents[4]

    def test_full_header_renders_without_obsidian_or_preload(self):
        metadata = {
            'name': 'Fixture Person', 'species': 'human',
            'pronunciation': 'FIX-cher',
            'whereabouts': [{'type': 'home', 'location': 'Fixture Place'}],
            'affiliations': ['Fixture Group'],
            'campaignInfo': [{'campaign': 'dufr', 'date': '1748-08-23', 'type': 'met'}],
        }
        files = [{'path': name + '.md', 'basename': name, 'frontmatter': fm}
                 for name, fm in [('Fixture Person', metadata),
                                  ('Fixture Place', {'name': 'Fixture Place', 'tags': ['place']}),
                                  ('Fixture Group', {'name': 'Fixture Group', 'tags': ['group']})]]
        payload = {'root': str(self.root), 'files': files, 'name': 'Fixture Person',
                   'metadata': metadata, 'date': '1750-01-01'}
        environment = dict(os.environ)
        environment.pop('NODE_OPTIONS', None)
        result = subprocess.run(['node', str(Path(__file__).with_name('render_header.js'))],
                                input=json.dumps(payload), text=True, encoding='utf-8',
                                capture_output=True, env=environment, check=True)
        self.assertIn('*(FIX-cher)*', result.stdout)
        self.assertIn('August 23rd, 1748', result.stdout)

    def test_day_ordinals_include_twenty_first_and_teens(self):
        script = r'''
const fs = require('node:fs');
const vm = require('node:vm');
const DateManager = vm.runInNewContext('(' + fs.readFileSync(process.argv[1], 'utf8') + ')');
const manager = new DateManager();
console.log(JSON.stringify(Array.from({length: 31}, (_, i) =>
    manager.normalizeDate('1748-08-' + String(i + 1).padStart(2, '0'), false).display)));
'''
        result = subprocess.run(['node', '-e', script, str(self.root / '_scripts/customJS/dataUtil.js')],
                                capture_output=True, text=True, encoding='utf-8', check=True)
        displays = json.loads(result.stdout)
        for day in range(1, 32):
            suffix = 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
            self.assertEqual(displays[day - 1], f'August {day}{suffix}, 1748')


if __name__ == '__main__':
    unittest.main()

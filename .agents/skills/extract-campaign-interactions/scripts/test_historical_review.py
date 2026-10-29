"""Historical rendering must preserve the original provenance checks."""
import copy
import json
import subprocess
import unittest
import test_session_model as fixtures
from batch import audit_chain
from session_model import apply_review, digest, render, validate


class HistoricalReviewTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ModelTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.vault, self.data = self.fixture.vault, self.fixture.data
        self.data['sources'][0]['sha256'] = digest(self.vault / 'source.md')
        self.data['interactions'][0]['quotes'] = [{
            'id': 'q', 'type': 'color', 'text': 'Follow me.',
            'source': {**self.fixture.loc, 'startUid': 'u0002', 'endUid': 'u0002'}}]
        self.data['entities'][0]['aiSuggestedFeaturedQuotes'] = ['q']
        self.git('init', '-q')
        self.git('remote', 'add', 'origin', 'https://github.com/example/vault.git')
        self.git('add', '.')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'Original source')
        self.revision = self.git('rev-parse', 'HEAD').strip()
        (self.vault / 'source.md').write_text('\n[u0001 | DM] Changed introduction.\n[u0002 | DM] Go away.\n[u0003 | PC] We leave.\n')

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.vault), *args], text=True)

    def test_snapshot_preserves_hash_quote_and_line_checks(self):
        with self.assertRaisesRegex(ValueError, 'Source hash changed'):
            validate(self.data, self.vault)
        before = copy.deepcopy(self.data)
        current = (self.vault / 'source.md').read_bytes()
        catalog = validate(self.data, self.vault, self.revision)['catalog']
        self.assertEqual(catalog.current_changed, ['source.md'])
        output = render(self.data, self.vault, self.vault / 'review.md', source_revision=self.revision)
        self.assertIn(f'https://github.com/example/vault/blob/{self.revision}/source.md?plain=1#L2', output)
        self.assertIn('current transcript has changed', output)
        self.assertIn('> Follow me.', output)
        self.assertEqual(self.data, before)
        self.assertEqual((self.vault / 'source.md').read_bytes(), current)
        wrong = copy.deepcopy(self.data)
        wrong['sources'][0]['sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'Source hash changed'):
            validate(wrong, self.vault, self.revision)
        wrong = copy.deepcopy(self.data)
        wrong['interactions'][0]['quotes'][0]['text'] = 'Go away.'
        with self.assertRaisesRegex(ValueError, 'not verbatim'):
            validate(wrong, self.vault, self.revision)

    def test_replay_still_binds_sample_and_reviewed_claims(self):
        report = self.fixture.report()
        report['decisions'].append({**report['decisions'][0], 'target': 'session'})
        reviewed = apply_review(self.data, report, self.vault, source_revision=self.revision)
        folder = self.vault / 'run'
        folder.mkdir()
        for name, data in [('extraction.json', self.data), ('review-decisions-0.json', report),
                           ('session.json', reviewed), ('execution.json', {'fullTranscriptRead': True, 'correctionAttempts': 0})]:
            (folder / name).write_text(json.dumps(data))
        selection = {'campaign': 'test', 'session': 1, 'source': 'source.md', 'sha256': self.data['sources'][0]['sha256']}
        result, _ = audit_chain(folder, self.vault, selection, self.revision)
        self.assertEqual(result, reviewed)
        with self.assertRaises(ValueError):
            audit_chain(folder, self.vault, {**selection, 'sha256': '0' * 64}, self.revision)
        reviewed['entities'][0]['label'] = 'Changed after review'
        (folder / 'session.json').write_text(json.dumps(reviewed))
        with self.assertRaisesRegex(ValueError, 'differs from its reviewed'):
            audit_chain(folder, self.vault, selection, self.revision)


if __name__ == '__main__':
    unittest.main()

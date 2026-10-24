"""Synthetic regression cases; no working vault data is used."""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from migrate_taelgar_headers import main, migrate_source


FM = b'---\nheaderVersion: 2023.11.25\ntags: [person]\nname: "Example" # preserve\n---\n'
CLEAN_FM = b'---\ntags: [person]\nname: "Example" # preserve\n---\n'
BLOCK = b'```taelgar-header\n```\n'
ARTICLE = b'\nArticle [[Link]].\n\n%% Comment %%\n\n## History\nKeep.\n'


class HeaderMigrationTests(unittest.TestCase):
    def test_legacy_variants_and_second_pass(self):
        for header in (
            b'# Example\n',
            b'# Example\n*(eg-ZAM-pul)*\n>[!info]+ Biographical Info  \n> Human  \n'
            b'> `$=dv.view("_scripts/view/get_PageDatedValue")`  \n'
            b'> `$=dv.view("_scripts/view/get_Affiliations")`\n'
            b'>> `$=dv.view("_scripts/view/get_Whereabouts")`\n'
            b'>> %%^Campaign:test%% Met the party %%^End%%\n',
            b'# Example\n> Old static details\n',
            b'# Example\n[[Home]]\n',
            b'# Example\n`$=dv.view("_scripts/view/get_Whereabouts")`\n',
            b'\n# Example\n> [!info] Old info\n> > Nested whereabouts\n',
            b'<!-- taelgar:header -->\n',
            b'<!-- taelgar-header -->\n',
            b'<!-- taelgar:header -->\n\n# Example\n>[!info] Details\n> Old\n',
        ):
            with self.subTest(header=header):
                result = migrate_source(FM + header + ARTICLE)
                self.assertEqual(result, CLEAN_FM + BLOCK + ARTICLE)
                self.assertEqual(migrate_source(result), result)

    def test_preserves_authored_h1_before_native_block(self):
        for title in (b'# Custom title\n', b'# Custom title\n \t\n',
                      b'Custom title\n============\n\n'):
            for block in (BLOCK, b'~~~taelgar-header\n\n~~~~\n'):
                for frontmatter in (FM, CLEAN_FM):
                    with self.subTest(title=title, block=block, frontmatter=frontmatter):
                        expected = CLEAN_FM + title + block + ARTICLE
                        self.assertEqual(migrate_source(frontmatter + title + block + ARTICLE), expected)
                        self.assertEqual(migrate_source(expected), expected)
                marked = FM + b'<!-- taelgar:header -->\n\n' + title + block + ARTICLE
                expected = CLEAN_FM + title + BLOCK + ARTICLE
                self.assertEqual(migrate_source(marked), expected)
                self.assertEqual(migrate_source(expected), expected)
        original = (FM + b'# Caf\xc3\xa9\n\n' + BLOCK + ARTICLE).replace(b'\n', b'\r\n')
        expected = (CLEAN_FM + b'# Caf\xc3\xa9\n\n' + BLOCK + ARTICLE).replace(b'\n', b'\r\n')
        self.assertEqual(migrate_source(original), expected)

    def test_explicit_h1_policy_for_saved_headers(self):
        for title in (b'# Custom title\n', b'Custom title\n============\n'):
            for prefix in (b'', b'<!-- taelgar:header -->\n\n'):
                source = FM + prefix + title + b'*(old pronunciation)*\n>[!info] Old details\n> Old data\n' + ARTICLE
                for preserve in (True, False):
                    with self.subTest(title=title, prefix=prefix, preserve=preserve):
                        expected = CLEAN_FM + (title if preserve else b'') + BLOCK + ARTICLE
                        result = migrate_source(source, preserve_h1=preserve)
                        self.assertEqual(result, expected)
                        self.assertEqual(migrate_source(result, preserve_h1=preserve), result)
        self.assertEqual(migrate_source(FM + b'# Final title', preserve_h1=True),
                         CLEAN_FM + b'# Final title\n' + BLOCK)
        source = b'# Unversioned\n> `$=dv.view("_scripts/view/get_Whereabouts")`\n' + ARTICLE
        self.assertEqual(migrate_source(source, preserve_h1=True), b'# Unversioned\n' + BLOCK + ARTICLE)

    def test_explicit_h1_policy_for_native_headers(self):
        for title in (b'# Custom title\n\n', b'Custom title\n============\n\n'):
            for block in (BLOCK, b'~~~taelgar-header\n\n~~~~\n'):
                for prefix in (b'', b'<!-- taelgar:header -->\n\n'):
                    source = FM + prefix + title + block + ARTICLE
                    for preserve in (True, False):
                        with self.subTest(title=title, block=block, prefix=prefix, preserve=preserve):
                            expected = CLEAN_FM + (title if preserve else b'') + (BLOCK if prefix else block) + ARTICLE
                            result = migrate_source(source, preserve_h1=preserve)
                            self.assertEqual(result, expected)
                            self.assertEqual(migrate_source(result, preserve_h1=preserve), result)
        original = b'\xef\xbb\xbf' + (FM + b'# Caf\xc3\xa9\n\n' + BLOCK + ARTICLE).replace(b'\n', b'\r\n')
        for preserve in (True, False):
            expected = b'\xef\xbb\xbf' + (CLEAN_FM + (b'# Caf\xc3\xa9\n\n' if preserve else b'') + BLOCK + ARTICLE).replace(b'\n', b'\r\n')
            self.assertEqual(migrate_source(original, preserve_h1=preserve), expected)

    def test_h1_options_do_not_invent_titles_or_remove_unrelated_headings(self):
        for source in (CLEAN_FM + BLOCK + ARTICLE, b'<!-- taelgar:header -->\n',
                       b'# Ordinary title\n\nProse.\n', CLEAN_FM + b'# Earlier title\n\nProse.\n' + BLOCK,
                       CLEAN_FM + b'````markdown\n# Example\n' + BLOCK + b'````\n'):
            for preserve in (True, False):
                with self.subTest(source=source, preserve=preserve):
                    self.assertEqual(migrate_source(source, preserve_h1=preserve), migrate_source(source))

    def test_preserves_adjacent_authored_content(self):
        for suffix in (b'Prose immediately after title.\n',
                       b'> [!warning] Keep this\n> Authored details\n',
                       b'## Heading\nBody\n', b'%% Comment %%\n',
                       b'```dataviewjs\ndv.table([]);\n```\n',
                       b'```taelgar-index\ntype: residents\n```\n'):
            with self.subTest(suffix=suffix):
                self.assertEqual(migrate_source(FM + b'# Example\n' + suffix), CLEAN_FM + BLOCK + b'\n' + suffix)
        source = FM + b'# Example\n>[!info] Header\n> Detail\n> [!note] Authored\n> Keep\n'
        self.assertEqual(migrate_source(source), CLEAN_FM + BLOCK + b'\n> [!note] Authored\n> Keep\n')

    def test_ordinary_titles_examples_templates_and_native_blocks_unchanged(self):
        for source in (
            b'# Authored title\n> Authored quote\n',
            b'---\ntags: [person]\n---\n# Authored title\n',
            CLEAN_FM + b'Opening prose.\n' + BLOCK,
            CLEAN_FM + b'````markdown\n' + BLOCK + b'````\n',
            CLEAN_FM + b'    ```taelgar-header\n    ```\n',
            CLEAN_FM + BLOCK + ARTICLE,
            CLEAN_FM + b'~~~taelgar-header\n\n~~~~\n' + ARTICLE,
            CLEAN_FM + b'<% template code %>\n',
        ):
            with self.subTest(source=source):
                self.assertEqual(migrate_source(source), source)

    def test_bom_unicode_crlf_and_missing_final_newline(self):
        source = b'\xef\xbb\xbf' + (FM + b'# Example\n>[!info] Details\n> Old\n' + ARTICLE).replace(b'\n', b'\r\n')
        expected = b'\xef\xbb\xbf' + (CLEAN_FM + BLOCK + ARTICLE).replace(b'\n', b'\r\n')
        self.assertEqual(migrate_source(source), expected)
        self.assertEqual(migrate_source(FM + b'# Example'), CLEAN_FM + BLOCK)
        self.assertEqual(migrate_source(FM + '# Caf\u00e9\n'.encode() + ARTICLE), CLEAN_FM + BLOCK + ARTICLE)
        self.assertEqual(migrate_source(b'<!-- taelgar:header -->'), BLOCK)

    def test_malformed_native_blocks_fail(self):
        for header in (b'```taelgar-header\n', b'```taelgar-header\nsettings\n```\n'):
            for prefix in (b'', b'# Example\n', b'<!-- taelgar:header -->\n'):
                with self.subTest(header=header, prefix=prefix), self.assertRaises(ValueError):
                    migrate_source(FM + prefix + header)

    def test_known_header_views_without_version_or_tags(self):
        header = b'# Example\n>[!info] Information\n> `$=dv.view("_scripts/view/get_Affiliations")`\n'
        for prefix in (b'', b'---\ntags: [place]\n---\n', b'---\ntentativeReason: unknown\n---\n'):
            with self.subTest(prefix=prefix):
                self.assertEqual(migrate_source(prefix + header + ARTICLE), (CLEAN_FM if prefix == FM else prefix) + BLOCK + ARTICLE)
        # A view later in the article cannot turn an authored title into a header.
        authored = b'# Example\nOpening prose.\n\n' + header
        self.assertEqual(migrate_source(authored), authored)

    def test_blank_before_info_callout_requires_known_header_views(self):
        header = b'# Example\n\n> [!info]+ Information\n> `$=dv.view("_scripts/view/get_Affiliations")`\n> \n> > `$=dv.view("_scripts/view/get_Whereabouts")`\n'
        for prefix in (FM, b'---\ntags: [place]\n---\n'):
            with self.subTest(prefix=prefix):
                self.assertEqual(migrate_source(prefix + header + ARTICLE), (CLEAN_FM if prefix == FM else prefix) + BLOCK + ARTICLE)
        authored = b'\n> [!info] Authored information\n> Keep this.\n'
        self.assertEqual(migrate_source(FM + b'# Example\n' + authored), CLEAN_FM + BLOCK + authored)

    def test_removes_obsolete_field_without_changing_headerless_or_native_body(self):
        for body in (b'', b'Opening prose.\n', b'# Authored title without tags\n', BLOCK + ARTICLE,
                     b'~~~taelgar-header\n\n~~~~\n' + ARTICLE):
            with self.subTest(body=body):
                original = b'---\nheaderVersion: 2023.11.25 # old\nname: Example\n---\n' + body
                expected = b'---\nname: Example\n---\n' + body
                self.assertEqual(migrate_source(original), expected)
                self.assertEqual(migrate_source(expected), expected)

    def test_only_top_level_frontmatter_field_is_removed(self):
        for field in (b'headerVersion: 2023.11.25\n', b'headerVersion : null\n', b'"headerVersion": "old"\n', b"'headerVersion': ''\n"):
            with self.subTest(field=field):
                remaining = b'displayDefaults:\n  headerVersion: keep nested\n# Preserve this comment\n'
                body = b'Opening prose.\n\n```yaml\nheaderVersion: keep body example\n```\n'
                original = b'---\n' + field + remaining + b'---\n' + body
                self.assertEqual(migrate_source(original), b'---\n' + remaining + b'---\n' + body)
        self.assertEqual(migrate_source(b'headerVersion: keep ordinary text\n'), b'headerVersion: keep ordinary text\n')

    def test_unfamiliar_multiline_version_is_rejected(self):
        for value in (b'|-\n  old\n', b'\n  old\n', b'"old\n  continued"\n'):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, 'Multiline headerVersion'):
                migrate_source(b'---\nheaderVersion: ' + value + b'name: Example\n---\n')

    def run_cli(self, root, *arguments):
        with contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()) as errors:
            code = main(['--root', str(root), *arguments])
        return code, output.getvalue(), errors.getvalue()

    def test_preview_write_check_order_and_excluded_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = FM + b'# Example\n' + ARTICLE
            for name in ('z.md', 'a.md', 'new/untracked.md', '_scripts/fixture.md', '_templates/template.md',
                         '_sessions/source.md', '.obsidian/cache.md', '_Plugins/support.md', 'assets/example.md'):
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(original)
            code, preview, _ = self.run_cli(root, '--verbose')
            self.assertEqual(code, 0)
            self.assertEqual(preview, 'a.md\nz.md\nnew/untracked.md\nWould migrate 3 of 3 Markdown notes.\n')
            self.assertEqual((root / 'a.md').read_bytes(), original)
            self.assertEqual(self.run_cli(root, '--check')[0], 1)
            self.assertEqual(self.run_cli(root, '--write')[0], 0)
            self.assertEqual((root / 'a.md').read_bytes(), CLEAN_FM + BLOCK + ARTICLE)
            self.assertEqual((root / '_templates/template.md').read_bytes(), original)
            self.assertEqual(self.run_cli(root, '--check')[0], 0)
            self.assertIn('Migrated 0', self.run_cli(root, '--write')[1])

    def test_cli_h1_policy_preview_write_check_and_mode_switch(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            note = root / 'example.md'
            original = FM + b'# Saved title\n>[!info] Old details\n> Old data\n' + ARTICLE
            note.write_bytes(original)
            self.assertEqual(self.run_cli(root, '--preserve-h1', '--check')[0], 1)
            self.assertEqual(note.read_bytes(), original)
            self.assertEqual(self.run_cli(root, '--preserve-h1', '--write')[0], 0)
            self.assertEqual(note.read_bytes(), CLEAN_FM + b'# Saved title\n' + BLOCK + ARTICLE)
            self.assertEqual(self.run_cli(root, '--preserve-h1', '--check')[0], 0)
            self.assertEqual(self.run_cli(root, '--check')[0], 0, 'default preserves native titles')
            self.assertEqual(self.run_cli(root, '--remove-h1', '--check')[0], 1)
            self.assertEqual(self.run_cli(root, '--remove-h1', '--write')[0], 0)
            self.assertEqual(note.read_bytes(), CLEAN_FM + BLOCK + ARTICLE)
            self.assertEqual(self.run_cli(root, '--remove-h1', '--check')[0], 0)
            self.assertEqual(self.run_cli(root, '--preserve-h1', '--check')[0], 0, 'preservation cannot recover a deleted title')
            with self.assertRaises(SystemExit) as error, contextlib.redirect_stderr(io.StringIO()):
                main(['--root', str(root), '--write', '--preserve-h1', '--remove-h1'])
            self.assertEqual(error.exception.code, 2)
            self.assertEqual(note.read_bytes(), CLEAN_FM + BLOCK + ARTICLE)

    def test_h1_options_validate_all_inputs_before_writing(self):
        for option in ('--preserve-h1', '--remove-h1'):
            with self.subTest(option=option), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                original = FM + b'# Saved title\n' + ARTICLE
                (root / 'a.md').write_bytes(original)
                (root / 'z.md').write_bytes(b'# Title\n```taelgar-header\ninvalid\n```\n')
                self.assertEqual(self.run_cli(root, option, '--write')[0], 2)
                self.assertEqual((root / 'a.md').read_bytes(), original)

    def test_errors_abort_before_any_write(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            original = FM + b'# Example\n' + ARTICLE
            (root / 'a.md').write_bytes(original)
            (root / 'z.md').write_bytes(b'```taelgar-header\nnot empty\n```\n')
            code, _, errors = self.run_cli(root, '--write')
            self.assertEqual(code, 2)
            self.assertIn('z.md', errors)
            self.assertIn('No files written', errors)
            self.assertEqual((root / 'a.md').read_bytes(), original)


if __name__ == '__main__':
    unittest.main()

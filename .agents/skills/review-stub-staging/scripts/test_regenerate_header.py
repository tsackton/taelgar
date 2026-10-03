import unittest
from regenerate_header import replace_header


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


if __name__ == '__main__':
    unittest.main()

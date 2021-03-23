""" module which test all_prefixes module """
from unittest import TestCase
from unittest import main as unittest_run
from all_prefixes import all_prefixes


class TestPrefixes(TestCase):
    """ class TestPrefixes """
    def test_list_with_three_char_as_first(self):
        """ test an string with three char as first """
        line = 'авангард'
        line_res = {'а', 'ав', 'ава', 'аван', 'аванг', 'аванга', 'авангар',
                     'авангард', 'ан', 'анг', 'анга', 'ангар',
                     'ангард', 'ар', 'ард'}

        self.assertEqual(all_prefixes(line), line_res, 'string with three char'
                                                       ' as first fail')

    def test_list_with_one_char_as_first(self):
        """ test an string with one char as first """
        line = 'line'
        line_res = {'l', 'li', 'lin', 'line'}

        self.assertEqual(all_prefixes(line), line_res, 'string with one char'
                                                       'as first fail')

    def test_empty_str(self):
        """ test an empty str ing """
        line = 'line'
        line_res = {'l', 'li', 'lin', 'line'}

        self.assertEqual(all_prefixes(line), line_res, 'empty string fail')

    def test_not_str(self):
        """ test noy str type of argument """
        with self.assertRaises(TypeError):
            _ = all_prefixes(None)


if __name__ == '__main__':
    unittest_run()

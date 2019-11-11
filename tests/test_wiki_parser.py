"""Module used to test dota_wiki_parser module methods."""

import json
import unittest

import config
from parsers import wiki_parser, requests

__author__ = 'Jonarzz'
__maintainer__ = 'MePsyDuck'


class WikiParserTest(unittest.TestCase):
    """Class used to test dota_wiki_parser module.
    Inherits from TestCase class of unittest module.
    """

    def test_pages_to_parse(self):
        """Method testing pages_to_parse method from dota_wiki_parser module.

        The method checks if the requested response is consists of JSON payload as expected.
        """
        parsed_json = json.loads(requests.get(url=config.API_PATH,
                                              params=wiki_parser.get_params_for_category_api(
                                                  config.RESPONSES_CATEGORY)).text)

        self.assertIsNotNone(parsed_json)
        category_members = parsed_json["query"]["categorymembers"]
        self.assertNotEqual(category_members, [])
        self.assertTrue(len(category_members) > 150)
        self.assertEqual(category_members[0]['title'], 'Abaddon/Responses')
        self.assertEqual(category_members[-1]['title'], 'Zeus/Responses')

    def test_pages_for_category(self):
        """Method testing pages_for_category method from dota_wiki_parser module.

        The method checks if the list generated by the method is not empty.
        """
        self.assertNotEqual(wiki_parser.pages_for_category(config.RESPONSES_CATEGORY), [])

    def test_clean_key(self):
        """Method testing clean_response_text method from dota_wiki_parser module.

        Please, check help for clean_response_text method for further information about the expected results.
        """
        self.assertEqual(wiki_parser.clean_response_text('   Earthshaker  !  '), 'earthshaker')

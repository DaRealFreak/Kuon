# !/usr/bin/python
# -*- coding: utf-8 -*-

import json
import unittest
from time import time

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.item import Item
from kuon.watcher.adapters.models.search_response import SearchResponse
from kuon.watcher.adapters.models.sticker import Sticker


class TestSearchResponse(unittest.TestCase):
    """
    Test cases for the search response model like proper JSON dump and ability to parse to APIResponse object
    """

    def setUp(self):
        """Set up the item to add

        :return:
        """
        sticker = Sticker(
            name="Howling Dawn",
            image="some_sticker_image_link",
            wear_value=0.43092
        )

        self._item = Item(
            market_name='some_market_name',
            item_id=12345,
            app_id=730,
            class_id=12345,
            context_id=2,
            instance_id=54321,
            price=109999,
            wear_value=0.14305446,
            image="some_item_image_link",
            inspect_link="some_steam_inspect_link",
            stickers=[sticker]
        )

    def test_response(self):
        """Test the conversion to the APIResponse object and the json.dumps

        :return:
        """
        response = SearchResponse(success=True, checked_time=time())
        response.add_item(self._item)
        json_response_dump = json.dumps(response.__dict__)
        api_response = APIResponse(json_response_dump)
        self.assertEqual(api_response.data.success, True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchResponse)
    unittest.TextTestRunner(verbosity=2).run(suite)
